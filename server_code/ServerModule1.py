import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_account_number(email, password):
  conn = sqlite3.connect(data_files['database.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT UserID FROM User WHERE Email = '{email}' AND Password = '{password}'"))
  conn.close()
  return res



@anvil.server.http_endpoint("/users", methods=["GET"])
def get_data(**kwargs):
    # Extract query parameters
    UserID = kwargs.get("UserID")
    
    return 