class Secret:
    JWT_SECRET: str = "57bbe626-9beb-4384-9414-bba77242ef65"
    AUTH_TOKEN_LIFE_TIME: int = 60 * 24 * 8
    AUTH_TOKEN_TYPE: str = "access_token"
    ALGORITHM: str = "HS256"
    ENCRYPTION_DECRYPTION_KEY = "auth_token"
