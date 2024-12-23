from ._anvil_designer import InitTemplate
from anvil import *
import anvil.server
from ..Login import Login
from ..User import User
from ..Error import Error

class Init(InitTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    anvil.server.call('nuke_db')
    open_form('Login')