---
title: "pilvar's challenge"
description: "
PHP Warnings

In PHP, when you return any body data before header() is called, the call will be ignored because the response was already sent to the user and headers must be sent first.
Parameters Limit

$_GET / $_POST: maximum 1000 parameters
A request containing more than 1000 GET parameters, a warning will be sent, and the CSP header won't


Buffering

PHP is known for buffering the response to 4096 bytes by default


ref:


justCTF 2020 - BabyCSP



"
url: "https://twitter.com/pilvar222/status/1784618120902005070"
category: "Miscellaneous"
---
