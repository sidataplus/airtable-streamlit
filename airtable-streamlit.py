import streamlit as st
import requests
from requests.structures import CaseInsensitiveDict

# The read-only API key generated for this demo; for proper deployment, API key must not be in the code like this!
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer key7tx4lPIfvcaezz"

"""
# Airtable-Streamlit

Access Airtable data via Streamlit  
*For demo purpose*

see source Airtable here: https://airtable.com/shrgCbVCeTbLNjLA4

"""

id = st.text_input('ID no.', value='A123')
name = st.text_input('Name', value='Alex')

if st.button('Retrieve Status'):
  res = requests.get(f'https://api.airtable.com/v0/appNr2Fzg61jfT6wR/Table%201?filterByFormula=AND(%7BID%7D=%27{id}%27,+Name=%27{name}%27)', headers=headers)       

  if len(res.json()['records']) == 1:
    st.subheader(f"Status of {name}'s case ID: {id}")    
    st.text(res.json()['records'][0]['fields']['Status']) 
  else:
    st.text('Case not found!')              