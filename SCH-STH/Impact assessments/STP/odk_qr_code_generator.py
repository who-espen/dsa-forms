from base64 import b64encode
import codecs
import json
import segno
import zlib

settings = {
  "general": {
    "server_url": "https://submit.datastandard.co/espen/mali-espen",
    "username": "collect",
    "password": "espen47",
  },
  "admin": {
    "edit_saved": False,
    "send_finalized": True,
    "view_sent": True,
    #"delete_saved": False,
    # "admin_pw": "1325",
  },
  "project": {
    "name": "Mali ESPEN",
    "icon": "M",
    "color": "#34e5eb"
  }
}

qr_data = b64encode(zlib.compress(json.dumps(settings).encode("utf-8")))

code = segno.make(qr_data, micro=False)
code.save('SCH-STH/Impact assessments/Mali/2025/ml-settings.png', scale=5)
