from anvil import *
from anvil_extras import routing

@routing.error_form
class ErrorPage():
  def __init__(self, **properties):
    self.init_components(**properties)