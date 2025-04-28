---
title: "backend/whatsapp-web-backend.py"
description: "
Thus, when you want a message for the backend, now edit . In the if-else-compound starting in line 88, add your own branch for the command name you chose. Then, edit backend/whatsapp.py and add a function similar to generateQRCode in line 223. Just using something like in getLoginInfo may not be enough, as your command may require an asynchronous request to the WhatsApp Web servers. In this case, make sure to add an entry to self.messageQueue with the message tag you chose and send an appropriate message to self.activeWs. The servers will respond to your request with a response containing the same tag, thus this is resolved in line 134. Make sure to eventually call pend[\"callback\"][\"func\"]({...}) with the JSON object containing your response data to resolve the callback.
"
external_url: "https://github.com/sigalor/whatsapp-web-reveng/blob/master/backend/whatsapp-web-backend.py"
category: "Web Exploitation"
---
