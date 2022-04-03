from app.exception import BadRequestException
from app.constants import ApiError
import re


class DataValidator:

    @classmethod
    def validate_mandatory_params(cls, **kwargs):
        for key, value in kwargs.items():
            if value is None:
                raise BadRequestException(ApiError.REQUIRED_PARAMETERS.value.format(key))

    @classmethod
    def validate_email(cls, email: str):
        cls.validate_mandatory_params(email=email)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, email)):
            raise BadRequestException(ApiError.INVALID_EMAIL.value.format(email))

    @classmethod
    def validate_phone_number(cls, phone_number: int):
        cls.validate_mandatory_params(phone_number=phone_number)
        if not re.compile("(0|91)?[7-9][0-9]{9}").match(str(phone_number)):
            raise BadRequestException(ApiError.INVALID_PHONE_NO.value.format(str(phone_number)))

    @classmethod
    def validate_password(cls, password: str):
        cls.validate_mandatory_params(password=password)
        regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pattern = re.compile(regex)
        match = re.search(pattern, password)
        if not match:
            raise BadRequestException(ApiError.INVALID_PASSWORD.value)
