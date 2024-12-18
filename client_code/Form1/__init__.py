from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    if anvil.server.call('get_sessiondata', 'last_opened_form') == "resultpage" and anvil.server.call('get_sessiondata', 'Logout') != "true":
      self.init_components(**properties)
      url = anvil.js.window.location.href
      query_params = anvil.server.call('get_query_params', url)
      key1_value = query_params.get('AccountNo', [None])[0] 
      result = anvil.server.call('get_data_accountno', key1_value)
      ResultPage = open_form('ResultPage')
      ResultPage.text_area_1.text = result
  

    if (anvil.server.call('get_sessiondata', 'Level1') == 'true'):
      self.check_box_2.checked = True
    else:
      self.check_box_2.checked = False
    if (anvil.server.call('get_sessiondata', 'Level2') == 'true'):
      self.check_box_3.checked = True
    else:
      self.check_box_3.checked = False
    if (anvil.server.call('get_sessiondata', 'Level3') == 'true'):
      self.check_box_4.checked = True
    else:
      self.check_box_4.checked = False

  def button_1_click(self, **event_args):
    username = self.text_box_1.text
    password = self.text_box_2.text
    sqlinjection = self.check_box_1.checked 
    result = anvil.server.call('login', username, password, sqlinjection)
    ResultPage = open_form('ResultPage')
    ResultPage.text_area_1.text = result


  def button_2_click(self, **event_args):
    anvil.server.call('set_sessiondata', 'Level1', 'false')
    anvil.server.call('set_sessiondata', 'Level2', 'false')
    anvil.server.call('set_sessiondata', 'Level3', 'false')
    open_form("Form1")
