---
title: "index.js"
description: "
Next, edit . It contains a couple of blocks beginning with clientWebsocket.waitForMessage. You can copy one of these blocks and edit the parameters. The waitForMessage function needs the following attributes:

condition: when a message is received and this condition evaluates to true on it, the message will be processed by the following .then(...) block
keepWhenHit: it is possible for a message handler to be detached immediately after it receives its first fitting message. Control this here.
The returned promise's then block finally handles a received message. It gets a clientCallRequest you can call .respond({...}) on to send a JSON response to the caller. If the NodeJS API is not the message's final destination, you need to instantiate a new BootstrapStep here which will contact to the Python backend and, after it receives its response, will return it to the original caller.

"
url: "https://github.com/sigalor/whatsapp-web-reveng/blob/master/index.js"
category: "Web Exploitation"
---
