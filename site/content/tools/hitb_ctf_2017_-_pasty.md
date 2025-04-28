---
title: "HITB CTF 2017 - Pasty"
description: "
kid 參數 (key ID)

是一個可選參數
用於指定加密算法的密鑰
任意文件讀取

\"kid\" : \"/etc/passwd\"


SQL注入

kid 有可能從資料庫提取數據
\"kid\" : \"key11111111' || union select 'secretkey' -- \"


Command Injection

Ruby open: \"/path/to/key_file|whoami\"


Example: 

"
url: "https://chybeta.github.io/2017/08/29/HITB-CTF-2017-Pasty-writeup/"
category: "Web Exploitation"
---
