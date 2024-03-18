import openai 
import requests
import os 
from io import BytesIO
from PIL import Image
def gerador_de_imagens(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Image.create(
         prompt = prompt,
        n=1,
        size = '1024x1024'
        response_format = 'url'
    )
    image_url = response["data"][0]["url"]
    image_data = requests.get(image_url).content
    image = Image.open(BytesIO('image_data'))
    image.show()
gerador_de_imagens('pato com oculos')