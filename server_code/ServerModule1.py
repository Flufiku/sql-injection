import anvil.server


# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_account_number(email, password):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute("SELECT Name FROM Gefaengnis"))
  new_res = [(item[0], item[0]) for item in res]
  conn.close()
  return new_res