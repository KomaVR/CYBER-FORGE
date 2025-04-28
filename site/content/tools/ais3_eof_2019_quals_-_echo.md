---
title: "AIS3 EOF 2019 Quals - echo"
description: "EJS RCE

outputFunctionName
直接拼接到模板執行
污染即可 RCE: Object.prototype.outputFunctionName = \"x;process.mainModule.require('child_process').exec('touch pwned');x\";
補充: 不需要 Prototype Pollution 的 RCE (ejs render 誤用)

漏洞成因: res.render('index.ejs', req.body);
req.body 會污染到 options 進而污染到 outputFunctionName (HPP)
Example: 



"
url: "https://github.com/CykuTW/My-CTF-Challenges/tree/master/AIS3-EOF-CTF-2019-Quals/echo"
category: "Miscellaneous"
---
