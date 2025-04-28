---
title: "GPP.png"
description: "
域组策略

为什么会需要域组策略？例如域内默认的密码过于简单，一个一个修改太过麻烦，可以使用域组策略批量修改密码

如何解决呢，抄一下xq17师傅文章中的内容：

通过在域中下发脚本执行
在GPP（组策略首选项）中设置
LAPS（这个在 基础篇 - PTH 防御提及过）

跟着xq17师傅的文章，先看一看sysvol，netlogon这两个文件夹。
netlogon
挂载点为 SYSVOL\domain\SCRIPTS ，存放脚本信息
sysvol
是AD域中的一个共享文件夹，存放组策略数据和脚本配置，供域成员访问。在域中，用户登录时会先在sysvol下查找GPO

GPO又是什么呢
GPO（Group Policy Object）是组策略设置的集合，用GPO来存储不同的组策略信息，可以指定作用范围（安装完了后默认存在两个）一：Default Domain Policy 即默认组策略。二：Default Domain Controllers Policy即默认域控制器策略。

GPP
终于看到了之前看到多次的GPP。组策略首选项（Group Policy Preference，GPP）借助了GPO实现域中所有资源的管理。截个图，在组策略管理中可以找到

GPP是2008中新增的，在这之前统一管理只能写脚本，GPP的出现方便了管理。
同样搬运xq17师傅的文章，这里就不复现了
shell for /r \\dc/sysvol %i in (*.vbs) do @echo %i
shell for /r \\dc/sysvol %i in (*.bat) do @echo %i
有关GPP的漏洞，只存在于winserver 2008没有上补丁（KB2962486）的时候（如windows server 2012就不存在），在sysvol下会有一个xml文件，其中的 password 字段是以aes-256保存的，但是微软把密钥放出来了...所以可以解密的。所以我认为搜索的脚本就是这样的，快速找到xml文件即可：
shell for /r \\dc/sysvol %i in (*.xml) do @echo %i
可以直接使用 PowerSploit下的 Get-GPPPassword.ps1 进行解密操作
"
url: "https://github.com/chriskaliX/AD-Pentest-Notes/raw/master/imgs/GPP.png"
category: "Miscellaneous"
---
