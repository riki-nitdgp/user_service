from app.models import User
from app.exception import BadRequestException, NotFoundException, ForbiddenException
from app.service.security import SecurityManager
from app.constants import ApiError
from simplecrypt import encrypt
from app.secrets import Secret
import uuid
import time


class UserManager:

    @classmethod
    async def sign_up(cls, email: str, phone_number: int, password: str):
        user_by_email = await cls.check_existing_user_using_email(email)
        if user_by_email["is_existing_user"]:
            raise BadRequestException(ApiError.USER_EXIST_WITH_EMAIL.value.format(email=email))

        user_by_phone_number = await cls.check_existing_user_using_phone_number(phone_number)

        if user_by_phone_number["is_existing_user"]:
            raise BadRequestException(ApiError.USER_EXIST_WITH_PHONE_NO.value.format(phone_number=str(phone_number)))
        user_id = cls.generate_user_id()
        auth_token = await SecurityManager.create_authorization_token(user_id)
        hash_password = SecurityManager.get_password_hash(password)
        payload = {
            "username": user_id,
            "email": email,
            "phone_number": phone_number,
            "authorization_token": auth_token,
            "created_at": int(time.time()),
            "hash_key": hash_password
        }
        user = await User.create(**payload)
        return {"username": str(user.username), "email": user.email, "phone_number": user.phone_number}

    @classmethod
    async def login(cls, email: str, password: str):
        user = await cls.check_existing_user_using_email(email)
        if not user["is_existing_user"]:
            raise NotFoundException(ApiError.USER_NOT_FOUND.value)

        user_data = user["user"]
        hash_key = user_data.hash_key
        username = user_data.username
        authorization_token = user_data.authorization_token
        # encrypted_auth_token = SecurityManager.encrypt_auth_token(authorization_token)
        if not SecurityManager.verify_password(password, hash_key):
            raise ForbiddenException(ApiError.INVALID_CREDENTIALS.value)

        valid_authorization_token = await SecurityManager.validate_authorization_token(authorization_token)
        if not valid_authorization_token["is_authorized_user"]:
            new_authorization_token = await SecurityManager.create_authorization_token(username)
            await User.filter(**{"username": username}).update(**{"authorization_token": new_authorization_token})
            encrypted_auth_token = SecurityManager.encrypt_auth_token(Secret.ENCRYPTION_DECRYPTION_KEY,
                                                                      authorization_token)
        return {
            "is_logged_in": True,
            "authorization_token": authorization_token,
            "user_info": {
                "username": str(username),
                "email": user_data.email,
                "phone_number": user_data.phone_number
            }
        }

    @classmethod
    async def check_existing_user_using_email(cls, email: str):
        result = {"user": None, "is_existing_user": False}
        user = await User.filter(email=email)
        if user:
            result["user"] = user[0]
            result["is_existing_user"] = True
        return result

    @classmethod
    async def check_existing_user_using_phone_number(cls, phone_number: int):
        result = {"user": None, "is_existing_user": False}
        user = await User.filter(phone_number=phone_number)
        if user:
            result["user"] = user[0]
            result["is_existing_user"] = True
        return result

    @classmethod
    def generate_user_id(cls):
        return str(uuid.uuid4())
