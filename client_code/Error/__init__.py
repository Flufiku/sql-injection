from ._anvil_designer import ErrorTemplate
from anvil import *
import anvil.server
from anvil_extras import routing

@routing.error_form
class Error(ErrorTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)