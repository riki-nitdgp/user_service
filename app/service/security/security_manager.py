from app.exception import UnAuthorizedException
from jose import jwt, JWTError
from app.secrets import Secret
from datetime import datetime, timedelta
from passlib.context import CryptContext
from app.constants import ApiError


class SecurityManager:
    PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    async def validate_authorization_token(cls, authorization_token: str, raise_exception: bool = False):
        unauthorized_exception = UnAuthorizedException(ApiError.UNAUTHORIZED_USER.value)
        try:
            payload = jwt.decode(
                authorization_token,
                Secret.JWT_SECRET,
                algorithms=[Secret.ALGORITHM],
                options={"verify_aud": False},
            )
            username = payload.get("sub")
            is_authorized_user = True if username else False
            if username is None and raise_exception:
                raise unauthorized_exception
        except JWTError:
            raise unauthorized_exception
        return {"is_authorized_user": is_authorized_user}

    @classmethod
    async def create_authorization_token(cls, user_id: str) -> str:

        token_payload = {
            "type": Secret.AUTH_TOKEN_TYPE,
            "exp": datetime.utcnow() + timedelta(minutes=Secret.AUTH_TOKEN_LIFE_TIME),
            "iat": datetime.utcnow(),
            "sub": str(user_id)
        }
        return jwt.encode(token_payload, Secret.JWT_SECRET, algorithm=Secret.ALGORITHM)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.PWD_CONTEXT.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls.PWD_CONTEXT.hash(password)
