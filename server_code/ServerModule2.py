import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3


@anvil.server.callable
def nuke_db():
  database = anvil.files.open_file('database')
  original_database = anvil.files.open_file('original_database')
  
  if database is None or original_database is None:
      raise ValueError("database or original_database not found")
  
  # Read the content of original_database
  original_database_content = original_database.read()
  
  # Clear the contents of database
  with anvil.files.write_file('database') as f:
      f.truncate(0)  # Clear the file by truncating its size to 0
  
  # Write the contents of original_database to database
  with anvil.files.write_file('database') as f:
      f.write(original_database_content)