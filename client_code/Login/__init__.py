from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing
import anvil.server

@routing.default_template
@routing.route('')
class Login(LoginTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def button_login_click(self, **event_args):
    email_empty = self.text_box_email.text == ""
    password_empty = self.text_box_password == ""
    email_has_semicolon = ';' in self.text_box_email.text
    password_has_semicolon = ';' in self.text_box_password.text

    email = self.text_box_email.text
    password = self.text_box_password.text
    
    if email_has_semicolon or password_has_semicolon:
      self.label_output.text = "; ist kein gültiges Zeichen."
    elif (not email_empty) and (not password_empty):
      try:
        if self.check_box_secure.checked:
          UserIDs = anvil.server.call('get_UserID_secure',email, password)
        else:
          UserIDs = anvil.server.call('get_UserID',email, password)
          
        if UserIDs == []:
          self.label_output.text = "E-Mail oder Passwort ist ungültig"
        else:
          self.label_output.text = UserIDs
          UserID_Dict = {'s': self.check_box_secure.checked,'UserID': UserIDs[0][0]}
          routing.set_url_hash(url_pattern='User', url_dict=UserID_Dict)
        #tom.wagner@gmail.com
        #8lZH5Ox#
      except Exception as e:
        self.label_output.text = f"Error in SQL Query: SELECT UserID FROM User WHERE Email = '{email}' AND Password = '{password}' \n {e}"