import peewee

# local import
from .db import db


class BaseModel(peewee.Model):
    class Meta:
        database = db


class TGUser(BaseModel):
    tg_user_id = peewee.IntegerField()

    username = peewee.CharField(null=True)


class Course(BaseModel):
    course_id = peewee.IntegerField()

    image = peewee.TextField(null=True)
    title = peewee.CharField(null=True)
    slug = peewee.CharField(null=True)
    youtube_url = peewee.CharField(null=True)
    blocks = peewee.TextField(null=True)

    @classmethod
    def create_from_list(cls, list_of_data):
        for data in list_of_data:
            course, course_created = cls.get_or_create(course_id=data['course_id'])
            course.update(**data)


if not TGUser.table_exists():
    TGUser.create_table()

if not Course.table_exists():
    Course.create_table()
