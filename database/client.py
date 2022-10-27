import pymysql.cursors
import os

from dotenv import load_dotenv
load_dotenv()

class DB:
  def __init__(self) -> None:
    connection = pymysql.connect(
      host=os.environ.get('DB_HOST'),
      port=int(os.environ.get('DB_PORT')),
      user=os.environ.get('DB_USER'),
      password=os.environ.get('DB_PASS'),
      database=os.environ.get('DB_NAME'),
      cursorclass=pymysql.cursors.DictCursor)
    self.db = connection
  def query(self, text):
    with self.db:
      with self.db.cursor() as cursor:
        cursor.execute(text)
        result = cursor.fetchall()
        return result