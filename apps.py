import streamlit as st
from google.cloud import firestore
import pandas as pd
import json
from google.oauth2 import service_account
from google.cloud.firestore import Client

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="testrandom1-6cf06")

st.subheader("Punya ide aktivitas random? ✍️")
    #st.caption('tulisin disini, bebas apa aja!')
colide = db.collection('list')
with st.form("ide randommu", clear_on_submit=True):
    #st.write("tulisin apa aja ya bebas!")
    ide = st.text_input('')
    sub = st.form_submit_button('Kirim')
    if sub:
        colide.add({'name': ide})
        st.write('makasih idenya ya')
