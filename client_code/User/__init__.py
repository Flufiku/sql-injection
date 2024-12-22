from ._anvil_designer import UserTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing

@routing.route('User', url_keys=[routing.ANY])
class User(UserTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    http_get_dict = routing.get_url_dict()

    secured = http_get_dict.get('s', False)
    UserID = http_get_dict.get('UserID', None)

    if secured:
      UserInfo = anvil.server.call('get_info', UserID)
    else:
      UserInfo = anvil.server.call('get_info_secure', UserID)

    self.label_output.text = f"Willkommen {UserInfo[0][0]}. Dein Kontostand beträgt {UserInfo[0][1]:2}€"

  def image_logo_mouse_down(self, x, y, button, keys, **event_args):
    routing.set_url_hash(url_pattern='')

    


