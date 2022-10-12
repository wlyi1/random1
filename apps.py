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

# Data to be written to Deta Base
with st.form("form"):
    name = st.text_input("Your name")
    age = st.number_input("Your age")
    submitted = st.form_submit_button("Store in database")

def _font_as_bytes():
    with open('https://raw.githubusercontent.com/wlyi1/random/main/Random/Quicksand-Regular.ttf', 'rb') as f:
        font_bytes = BytesIO(f.read())
    return font_bytes

resp = requests.get('https://raw.githubusercontent.com/wlyi1/random/main/Random/dw.png')
image3 = Image.open(BytesIO(resp.content))

#Data Sources
data = pd.read_csv('rand_aktivitas.csv')
image1 = 'https://raw.githubusercontent.com/wlyi1/random/main/Random/a3a.png'
st.image(image1)
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


deta = Deta(st.secrets["project_key"])

# Create a new database "example-db"
# If you need a new database, just use another name.
db = deta.Base("random")

# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    st.image(image3)
    db.put({'Tanggal' : tgl_random, 'Random' : today_rand})
    #db.put({"names": name, "ages": age})

"---"
"Here's everything stored in the database:"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch().items
st.write(db_content)
df = pd.DataFrame(db_content)
st.dataframe(df)
