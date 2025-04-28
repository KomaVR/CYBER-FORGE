---
title: "ref"
description: "
HTTP Method

OPTIONS method

查看可用 HTTP method
curl -i -X OPTIONS 'http://evil.com/'


HEAD method

特殊場景下容易出現邏輯問題 if(request.method == get) {...} else {...}
Werkzeug 只要有設定接受 GET 請求，也會自動接受 HEAD ()
Example:

FwordCTF 2021 - Shisui
Bypassing GitHub's OAuth flow





"
url: "https://werkzeug.palletsprojects.com/en/2.0.x/routing/#werkzeug.routing.Rule"
category: "Black Hat Tools"
---
