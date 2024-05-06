from base64 import b64encode
import codecs
import json
import segno
import zlib

settings = {
  "general": {
    "server_url": "https://submit.datastandard.co/espen/nigeria-espen-5",
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
    "name": "Nigeria TAS1",
    "icon": "G",
    "color": "#ebc634"
  }
}

qr_data = b64encode(zlib.compress(json.dumps(settings).encode("utf-8")))

code = segno.make(qr_data, micro=False)
code.save('LF/TAS/Nigeria/2024/mar_2024/nigeria-settings.png', scale=5)
