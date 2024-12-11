from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_login_click(self, **event_args):
    email_empty = self.text_box_email.text == ""
    password_empty = self.text_box_password == ""
    email_has_semicolon = ';' in self.text_box_email.text
    password_has_semicolon = ';' in self.text_box_password.text

    email = self.text_box_email.text
    password = self.text_box_password.text
    
    if email_has_semicolon or password_has_semicolon:
      self.label_output.text = "; ist keine gültige Eingabe."
    elif (not email_empty) and (not password_empty):
      try:
        acc_nums = anvil.server.call('get_account_number',email, password)
        if acc_nums == []:
          self.label_output.text = "E-Mail oder Passwort ist ungültig"
        else:
          print(self.label_output.text)
          self.label_output.text = acc_nums[0][0]
        #tom.wagner@gmail.com
        #8lZH5Ox#
      except Exception as e:
        self.label_output.text = f"Error in SQL Query: SELECT UserID FROM User WHERE Email = '{email}' AND Password = '{password}' \n {e}"