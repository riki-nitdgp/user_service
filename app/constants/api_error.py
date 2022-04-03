from enum import Enum


class ApiError(Enum):
    USER_EXIST_WITH_EMAIL = "User Already Exist With Email: {email}."
    USER_EXIST_WITH_PHONE_NO = "User Already Exist With Phone No: {phone_number}."
    USER_NOT_FOUND = "User Not Found."
    INVALID_CREDENTIALS = "Opps Invalid Credential !!!."
    UNAUTHORIZED_USER = "Unauthorized User, Please Re-login."
    REQUIRED_PARAMETERS = "{} is required."
    INVALID_EMAIL = "Email is not valid {}"
    INVALID_PHONE_NO = "Phone No. is not valid {}"
    INVALID_PASSWORD = "Invalid Password 1. Should have at least one number." \
                       "2. Should have at least one uppercase and one lowercase character." \
                       "3. Should have at least one special symbol." \
                       "4. Should be between 6 to 20 characters long."
