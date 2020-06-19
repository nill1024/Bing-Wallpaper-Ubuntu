
import requests
import json
from io import BytesIO
from PIL import Image

url2 = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'

headers = {'Content-Type':'application/json; charset=utf-8'}
response = requests.get(url2,headers=headers)

urlbase = 'https://www.bing.com'

dic = response.json().get('images')[0]
wh = dic.get('url')
out = urlbase+wh

response_img = requests.get(out)
image = Image.open(BytesIO(response_img.content))
image.save('./wallpaper.png')
