---
title: "HITCON CTF 2018 - One Line PHP Challenge"
description: "session.upload_progress

PHP 預設開啟
用來監控上傳檔案進度
當 session.upload_progress.enabled 開啟，可以 POST 在 $_SESSION 中添加資料 (sess_{PHPSESSID})
配合 LFI 可以 getshell
session.upload_progress.cleanup=on 時，可以透過 Race condition
上傳 zip

開頭會有 upload_progress_，結尾也有多餘資料，導致上傳 zip 正常狀況無法解析
利用 zip 格式鬆散特性，刪除前 16 bytes 或是手動修正 EOCD 和 CDH 的 offset 後上傳，可以讓 php 正常解析 zip


Example


0CTF 2021 Qual - 1linephp



"
external_category: "Miscellaneous"
---[Visit Website](https://blog.kaibro.tw/2018/10/24/HITCON-CTF-2018-Web/)

