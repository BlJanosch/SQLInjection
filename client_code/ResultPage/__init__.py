from ._anvil_designer import ResultPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ResultPage(ResultPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    # Wenn Form2 geöffnet wird
    anvil.server.call('set_sessiondata', 'Logout', 'false')
    anvil.server.call('set_sessiondata', 'last_opened_form', 'resultpage')

  def button_1_click(self, **event_args):
    anvil.server.call('set_sessiondata', 'Logout', 'true')
    open_form('Form1')
