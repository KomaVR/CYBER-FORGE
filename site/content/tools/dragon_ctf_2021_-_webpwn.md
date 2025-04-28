---
title: "Dragon CTF 2021 - webpwn"
description: "
Javascript replace 特性

replace string 中可以使用 $

> \"123456\".replace(\"34\", \"xx\")
'12xx56'
> \"123456\".replace(\"34\", \"$`\")
'121256'
> \"123456\".replace(\"34\", \"$&\")
'123456'
> \"123456\".replace(\"34\", \"$'\")
'125656'
> \"123456\".replace(\"34\", \"$$\")
'12$56'


Example





"
external_url: "https://github.com/w181496/CTF/tree/master/dragonctf-2021"
category: "Web Exploitation"
---
