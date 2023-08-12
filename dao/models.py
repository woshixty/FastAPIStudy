from tortoise import Model, fields

class Todo(Model):
    """dataset table"""
    id = fields.IntField(pk=True)
    content1 = fields.CharField(max_length=500)
    create_at = fields.DatetimeField(auto_now_add=True)
    update_at = fields.DatetimeField(auto_now=True)