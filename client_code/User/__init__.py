from ._anvil_designer import UserTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class User(UserTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    query_params = anvil.routing.get_url_hash()
    self.user_id = query_params.get("UserID", "Unknown")

    # Display the UserID in a label or text area
    self.label_output.text = f"User ID: {self.user_id}"