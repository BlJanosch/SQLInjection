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

    if (anvil.server.call('get_sessiondata', 'Level1') == 'true'):
      self.check_box_1.checked = True
    else:
      self.check_box_1.checked = False
    if (anvil.server.call('get_sessiondata', 'Level2') == 'true'):
      self.check_box_2.checked = True
    else:
      self.check_box_2.checked = False
    if (anvil.server.call('get_sessiondata', 'Level3') == 'true'):
      self.check_box_3.checked = True
    else:
      self.check_box_3.checked = False

  def button_1_click(self, **event_args):
    anvil.server.call('set_sessiondata', 'Logout', 'true')
    open_form('Form1')
