from base64 import b64encode
import codecs
import json
import segno
import zlib

settings = {
  "general": {
    "server_url": "https://submit.datastandard.co/espen/congo-espen",
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
    "name": "Congo",
    "icon": "c",
    "color": "#800000"
  }
}

qr_data = b64encode(zlib.compress(json.dumps(settings).encode("utf-8")))

code = segno.make(qr_data, micro=False)
code.save('LF/PreTAS/Congo/2024/configuration-congo.png', scale=5)
