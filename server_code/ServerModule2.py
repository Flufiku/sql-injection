import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3


@anvil.server.callable
def nuke_db():
  database_path = "path/to/database"
  original_database_path = "path/to/original_database"
  
  try:
    # Open 'database' in write mode to clear its content
    with open(database_path, 'wb') as database_file:
      pass  # Opening in write mode ('w' or 'wb') clears the file

    # Copy content from 'original_database' to 'database'
    with open(original_database_path, 'rb') as original_file:
      with open(database_path, 'wb') as database_file:
        # Copy all data from original_database to database
        database_file.write(original_file.read())
    
    print("Content copied successfully from 'original_database' to 'database'.")
  except Exception as e:
    print(f"An error occurred: {e}")