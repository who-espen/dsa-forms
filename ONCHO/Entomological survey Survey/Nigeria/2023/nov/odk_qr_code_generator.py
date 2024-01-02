from base64 import b64encode
import codecs
import json
import segno
import zlib

settings = {
  "general": {
    "server_url": "https://submit.datastandard.co/espen/nigeria-espen-4",
    "username": "collect",
    "password": "espen47",
  },
  "admin": {
    #"edit_saved": False,
    "send_finalized": True,
    "view_sent": True,
    #"delete_saved": False,
    "admin_pw": "1325",
  },
  "project": {
    "name": "Nigeria Surveys",
    "icon": "N",
    "color": "#33cc33"
  }
}

qr_data = b64encode(zlib.compress(json.dumps(settings).encode("utf-8")))

code = segno.make(qr_data, micro=False)
code.save('ONCHO/Entomological survey Survey/Nigeria/2023/nov/nigeria-settings.png', scale=5)
