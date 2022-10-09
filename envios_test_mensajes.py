# Para enviar mensajes debemos prebiamente recibir uno del otro lado.
# No alcanza con el envío del template:

import requests
import json

url = "https://graph.facebook.com/v14.0/100417452857527/messages"

payload = json.dumps({
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": 543492575809,
  "type": "text",
  "text": {
    "preview_url": False,
    "body": "Vamo' lo pibe"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer EAAtOJ6bxteQBAHDrRM58a4jH7zs7woX9RJZC5M996zdHzIsx0IElm8B0iZBQ5hZAgz2EH7xpZBOr0cLwrGaJKu7JKJZAsjuBLZAn3QyNfpFa6xYHnNNrEpr8FYcOOsczDbbp6UlM6gptAxBGAPWVfS6p68t7keCmKuTBkdAKB0fJI8yw4ZChIQtWIsv1Y8IHyZCgkASulwGxegZDZD'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)