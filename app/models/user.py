from tortoise import Model, fields


class User(Model):
    id = fields.BigIntField(pk=True)
    username = fields.UUIDField(max_length=100, index=True)
    email = fields.CharField(max_length=100, index=True, unique=True)
    phone_number = fields.IntField(max_length=100, index=True, unique=True)
    is_super_user = fields.BooleanField(default=False)
    authorization_token = fields.CharField(max_length=1000)
    hash_key = fields.TextField()
    created_at = fields.BigIntField(null=False)

    class Meta:
        table = "user"
