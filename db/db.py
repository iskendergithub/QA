from peewee import MySQLDatabase

# local imports
from data import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DATABASE


db = MySQLDatabase(
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    database=MYSQL_DATABASE,
)
