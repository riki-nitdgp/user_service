from app.models import User
from app.service.security import SecurityManager
from app.exception import UnAuthorizedException, ForbiddenException
from app.constants import ApiError


class AuthorizationManager:

    @classmethod
    async def authorized_user(cls, authorization_token: str):
        user = await User.filter(authorization_token=authorization_token)
        if user:
            user = user[0]
            username = str(user.username)
            authorization_data = await SecurityManager.validate_authorization_token(authorization_token,
                                                                                    raise_exception=True)
            username_from_authorization = authorization_data.get("username")
            is_authorized_user = authorization_data.get("is_authorized_user")

            if is_authorized_user and (username == username_from_authorization):
                payload = {
                    "username": username,
                    "phone_number": user.phone_number,
                    "email": user.email,
                    "authorization_token": user.authorization_token
                }

                return payload
            else:
                raise ForbiddenException(ApiError.UNAUTHORIZED_USER.value)
        else:
            raise UnAuthorizedException(ApiError.UNAUTHORIZED_USER.value)
