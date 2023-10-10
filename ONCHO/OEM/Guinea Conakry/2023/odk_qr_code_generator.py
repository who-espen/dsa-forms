from base64 import b64encode
import codecs
import json
import segno
import zlib

settings = {
  "general": {
    "server_url": "https://demo.getodk.org",
    "constraint_behavior": "on_finalize"
  },
  "admin": {
    
    "admin_pw": "1325",
    "admin_login": "1325",
    "edit_saved": False,
  },
  "project": {
    "name": "QR code project",
    "icon": "Q",
    "color": "#ff0000"
  }
}

qr_data = b64encode(zlib.compress(json.dumps(settings).encode("utf-8")))

code = segno.make(qr_data, micro=False)
code.save('settings.png', scale=5)