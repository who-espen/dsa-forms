from base64 import b64encode
import codecs
import json
import segno
import zlib

settings = {
  "general": {
    "server_url": "https://submit.datastandard.co/espen/cote-d-ivoire-espen-3",
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
    "name": "Côte d'Ivoire 3",
    "icon": "C",
    "color": "#0066ff"
  }
}

qr_data = b64encode(zlib.compress(json.dumps(settings).encode("utf-8")))

code = segno.make(qr_data, micro=False)
code.save("ONCHO/Entomological survey Survey/Cote d'Ivoire/2025/ci-settings.png", scale=5)
