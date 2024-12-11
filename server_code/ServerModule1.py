import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3
import urllib.parse

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#

@anvil.server.callable
def login(username, password, sqlinjection):
   conn = sqlite3.connect(data_files["database.db"])
   cursor = conn.cursor()
   query = f"SELECT username FROM Users WHERE username = '{username}' AND password = '{password}'"
   print(query)
   try:
     data = list(cursor.execute(query)) if sqlinjection else list(cursor.execute("SELECT username FROM Users WHERE username = ? AND password = ?", (username, password)))
     if (data == []):
       raise ValueError("Data is empty")
     elif (username in data[0]):
       return "Task completed!"
     return "Login successfull but AccountNo not passed"
   except:
     return f"{query} \nLogin nicht möglich"

@anvil.server.callable
def get_query_params(url):
    query_string = url.split('?')[-1] if '?' in url else ''
    if query_string:
        query_params = urllib.parse.parse_qs(query_string)
        return query_params
    return {}

@anvil.server.callable
def get_data_accountno(accountno):
   conn = sqlite3.connect(data_files["database.db"])
   cursor = conn.cursor()
   querybalance = f"SELECT balance FROM Balances WHERE AccountNo = {accountno}"
   queryusername = f"SELECT username FROM Users WHERE AccountNo = {accountno}"
   try:
    return f"Willkommen {list(cursor.execute(queryusername))}! Dein Kontostand ist: {list(cursor.execute(querybalance))}"
   except: return ""

@anvil.server.callable
def set_sessiondata(usecase, data):
   anvil.server.session[usecase] = data

@anvil.server.callable
def get_sessiondata(usecase):
   return anvil.server.session.get(usecase, 0)
     
    
    

