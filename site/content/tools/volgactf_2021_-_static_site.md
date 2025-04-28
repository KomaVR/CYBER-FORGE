---
title: "VolgaCTF 2021 - Static Site"
description: "
Nginx $url CRLF Injection

$uri 是解碼後的請求路徑，可能包含換行，有機會導致 CRLF Injection

應改用 $request_uri


Example: 

proxy_pass https://volga-static-site.s3.amazonaws.com$uri;
CRLF Injection 蓋掉 S3 Bucket 的 Host header，控 Response 內容做 XSS



"
external_category: "Web Exploitation"
---[Visit Website](https://github.com/w181496/CTF/tree/master/volgactf2021_quals/Static_Site)

