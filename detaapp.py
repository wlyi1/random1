import streamlit as st
import pandas as pd
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime
from datetime import datetime as dt
from deta import Deta
import pandas as pd
from io import BytesIO
import requests
import urllib.request

def _font_as_bytes():
    with open('https://raw.githubusercontent.com/wlyi1/random/main/Random/Quicksand-Regular.ttf', 'rb') as f:
        font_bytes = BytesIO(f.read())
    return font_bytes

resp = requests.get('https://raw.githubusercontent.com/wlyi1/random/main/Random/dw.png')
image3 = Image.open(BytesIO(resp.content))

#Data Sources
data = pd.read_csv('rand_aktivitas.csv')
image1 = 'https://raw.githubusercontent.com/wlyi1/random/main/Random/a3a.png'
#image2 = Image.open('a3a.png')
st.image(image1)
#st.image(image2)
#stwrite

list_rand = data.name
tgl_random = datetime.datetime.now()
today_rand = random.choice(list_rand)
hari = dt.today().strftime('%Y-%m-%d')
path_font = "Quicksand-Regular.ttf"
path_font_2 = 'Quicksand-Bold.ttf'
font = ImageFont.truetype(path_font, 55)
font1 = ImageFont.truetype(path_font_2, 28)

img= ImageDraw.Draw(image3)
img.text((80,470), today_rand, font=font, fill=(0,0,0))
img.text((450,390), hari, font=font1, fill=(0,0,0))


# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["project_key"])

# Create a new database "example-db sss"
# If you need a new database, just use another name.
db = deta.Base("random")

if st.button('Show'):
    st.image(image3)
    db.put({'Tanggal' : tgl_random, 'Random' : today_rand})


# Data to be written to Deta Base of Cerita
db1 = deta.Base('Cerita')
with st.form("my_form"):
    st.write("Ceritain ke RandomKu dong tentang aktivitas randommu hari ini 😃")
    nama = st.text_input("Namanya? ")
    age = st.number_input('Umurnya? ', min_value=5, max_value=70)
    cerita = st.text_input("Cerita singkatnya gimana nih?")
    submitted = st.form_submit_button("Submit")

# If the user clicked the submit button. write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).

if submitted:
    db1.put({"Nama": nama, 'Umur' : age, "Cerita": cerita})

st.write('Test Your Knowledge')

db_content = db.fetch().items
st.write(db_content)
df = pd.DataFrame(db_content)
st.write(df)
#st.write(df['Random'][0])


