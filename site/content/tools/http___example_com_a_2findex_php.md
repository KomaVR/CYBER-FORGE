---
description: "

瀏覽器會把 a%2findex.php 當成一個檔案
Web Server 則會正常解析成 a/index.php
所以當使用相對路徑載入 css 時，就可以透過這種方式讓瀏覽器解析到其他層目錄下的檔案

如果該檔案內容可控，則有機會 XSS


舉例：

/test.php 中有 <link href=\"1/\" ...>
另有 /1/index.php 給 ?query= 參數，會直接輸出該參數內容
訪問 /1%2f%3Fquery={}*{background-color%3Ared}%2f..%2f../test.php 就會讓背景變紅色

Server: /test.php
Browser: /1%2f%3Fquery={}*{background-color%3Ared}%2f..%2f../test.php

CSS 會載入/1/?query={}*{background-color:red}/../../1/


CSS 語法容錯率很高





"
external_category: "Web Exploitation"
---
[Visit Website](http://example.com/a%2findex.php)

[Visit Website](http://example.com/a%2findex.php)

