from base64 import b64encode
import codecs
import json
import segno
import zlib

settings = {
  "general": {
    "server_url": "https://submit.datastandard.co/espen/guinnee-conakry-espen",
    "username": "collect",
    "password": "espen47",
    "constraint_behavior": "on_finalize"
  },
  "admin": {
    "edit_saved": False,
  },
  "project": {
    "name": "QR code project",
    "icon": "ESPEN",
    "color": "#3399ff"
  }
}

qr_data = b64encode(zlib.compress(json.dumps(settings).encode("utf-8")))

code = segno.make(qr_data, micro=False)
code.save('settings.png', scale=5)
