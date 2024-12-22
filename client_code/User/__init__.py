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

    self.label_output.text = http_get_dict.get('UserID', None)

    


