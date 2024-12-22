import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3


@anvil.server.callable
def get_UserID(email, password):
  conn = sqlite3.connect(data_files['database.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT UserID FROM User WHERE Email = '{email}' AND Password = '{password}'"))
  conn.close()
  return res


@anvil.server.callable
def get_UserID_secure(email, password):
  conn = sqlite3.connect(data_files['database.db'])
  cursor = conn.cursor()
  query = "SELECT UserID FROM User WHERE Email = ? AND Password = ?"
  res = list(cursor.execute(query, (email, password)))
  conn.close()
  return res


@anvil.server.callable
def get_info(UserID):
  conn = sqlite3.connect(data_files['database.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"SELECT Name, Balance FROM User WHERE UserID = '{UserID}'"))
  conn.close()
  return res


@anvil.server.callable
def get_info_secure(UserID):
  conn = sqlite3.connect(data_files['database.db'])
  cursor = conn.cursor()
  query = "SELECT Name, Balance FROM User WHERE UserID = ?"
  res = list(cursor.execute(query, (UserID)))
  conn.close()
  return res