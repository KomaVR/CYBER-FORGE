---
title: "Joomla XSS"
description: "
mb_strpos / mb_substr

當 mb_strpos 讀到 utf-8 leading byte ，他會繼續嘗試往下讀; 遇到 invalid byte 時，前面的內容會被當成一個 character

Example: mb_strpos(\"\xf0\x9fAAA<BB\", '<') -> 4


而 mb_substr 則有不一致，當遇到 leading byte 時，會跳過 continuation bytes

Example: mb_substr(\"\xf0\x9fAAA<BB\", 0, 4) -> \"\xf0\x9fAAA<B\"


ref: 

"
url: "https://www.sonarsource.com/blog/joomla-multiple-xss-vulnerabilities/"
category: "Web Exploitation"
---
