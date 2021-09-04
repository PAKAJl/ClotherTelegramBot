from mysql.connector import connect, Error
from config import *

def db_pattern(data):
  return "('"+str(data)+"',)"

def add_user(userId):
  try:
    with connect(
      host=DB_HOST,
      user=DB_LOGIN,
      password=DB_PASS,
      database=DB_NAME
    ) as connection:
      sql = "SELECT telegramId FROM users"
      with connection.cursor() as cursor:
        cursor.execute(sql)
        for id in cursor:
          if str(id) == db_pattern(userId): 
            print("user is exist")
            return 1
      sql = f"INSERT INTO users (telegramId) VALUES ({userId})"
      with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
  except Error as e:
    print(e)

def update_sex(userId, data):
  try:
    with connect(
      host=DB_HOST,
      user=DB_LOGIN,
      password=DB_PASS,
      database=DB_NAME
    ) as connection:      
      sql = f"UPDATE users SET sex='{data}' WHERE telegramId={userId}"
      with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
  except Error as e:
    print(e)
  
def update_outwearsize(userId, data):
  try:
    with connect(
      host=DB_HOST,
      user=DB_LOGIN,
      password=DB_PASS,
      database=DB_NAME
    ) as connection:      
      sql = f"UPDATE users SET outwearsize='{data}' WHERE telegramId={userId}"
      with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
  except Error as e:
    print(e)
  
def update_footsize(userId, data):
  try:
    with connect(
      host=DB_HOST,
      user=DB_LOGIN,
      password=DB_PASS,
      database=DB_NAME
    ) as connection:      
      sql = f"UPDATE users SET footsize='{data}' WHERE telegramId={userId}"
      with connection.cursor() as cursor:
        cursor.execute(sql)
        connection.commit()
  except Error as e:
    print(e)
  