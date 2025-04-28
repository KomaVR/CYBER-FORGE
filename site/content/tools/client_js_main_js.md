---
title: "client/js/main.js"
description: "
Now, look at . In line 214, you can see an instantiation of the BootstrapStep JavaScript class. It needs the following information:

websocket: is probably always the same
request.type: should generally be call, as this allows a response to be passed back to the command's sender
request.callArgs: an object which has to contain a command attribute specifying the name of your command and as many additional key-value-pairs as you want. All of these will be passed to the receiver.
request.successCondition: on receiving a response for a call, this shall be a function returning true when the response is valid/expected. Use the next attribute for specifying code to be executed when the response is valid.
request.successActor: when the success condition evaluated to true, this success actor function is called

When the BootstrapStep object has been constructed, call .run() for running indefinitely or .run(timeout_ms) for failing when no response has been received after a specific timeout. The run function returns a Promise.
"
url: "https://github.com/sigalor/whatsapp-web-reveng/blob/master/client/js/main.js"
category: "Web Exploitation"
---
