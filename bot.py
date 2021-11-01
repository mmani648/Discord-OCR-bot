import requests
import json
import discord
client=discord.Client()
#https://ocr.space/ocrapi
def ocr_space_url(url, overlay=False, api_key='', language='eng'):
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()
link=""
@client.event
async def on_message(message):
  if message.author == client.user:
        return
  if message.channel.id == 903686814269861930:
    if message.attachments:
      link=(message.attachments[0])

   
    
    test_url = ocr_space_url(url=link)
    print(test_url)
    text_json  = json.loads(test_url)
    final_text = text_json['ParsedResults'][0]['ParsedText']
    await message.channel.send(f"```{final_text}```")
client.run('your token')
