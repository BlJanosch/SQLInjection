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
      ResultPage = open_form('ResultPage')
      ResultPage.text_area_1.text = anvil.server.call('get_data_accountno', key1_value)

  def button_1_click(self, **event_args):
    username = self.text_box_1.text
    password = self.text_box_2.text
    sqlinjection = self.check_box_1.checked
    ResultPage = open_form('ResultPage')
    ResultPage.text_area_1.text = anvil.server.call('login', username, password, sqlinjection) 
    