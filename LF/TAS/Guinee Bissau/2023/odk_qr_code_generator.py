from base64 import b64encode
import codecs
import json
import segno
import zlib

settings = {
  "general": {
    "server_url": "https://submit.datastandard.co/espen/guinee-bissau-espen-2",
    "username": "collect",
    "password": "espen47",
  },
  "admin": {
   # "edit_saved": False,
    "send_finalized": True,
    "view_sent": True,
    #"delete_saved": False,
    # "admin_pw": "1325",
  },
  "project": {
    "name": "Guiné-Bissau Pesquisa SCH/STH",
    "icon": "G",
    "color": "#ebc634"
  }
}

qr_data = b64encode(zlib.compress(json.dumps(settings).encode("utf-8")))

code = segno.make(qr_data, micro=False)
code.save('LF/TAS/Guinee Bissau/2023/guine-bissau-settings.png', scale=5)
