from dotenv import load_dotenv
import pymysql.cursors
import os

load_dotenv()

db_host = os.getenv("DB_HOST") or "localhost"
db_user = os.getenv("DB_USER") or "root"
db_password = os.getenv("DB_PASSWORD") or ""
db_name = os.getenv("DB_NAME") or "test"


def get_connection():
    return pymysql.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        database=db_name,
    )
