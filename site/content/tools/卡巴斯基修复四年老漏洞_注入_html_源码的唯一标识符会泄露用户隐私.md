---
title: "卡巴斯基修复四年老漏洞 注入 HTML 源码的唯一标识符会泄露用户隐私"
description: "
kaspersky

事件记录




安全研究人员在测试卡巴斯基杀毒软件时发现它会以安全的名义在用户访问的每一个网页注入它的脚本,而这个脚本还带有唯一 ID,这个 ID 在不同计算机上是不同的,也就是说它可以作为跟踪代码使用.研究人员将这一发现报告给了卡巴斯基.卡巴斯基承认了数据泄漏,它释出了补丁修复了编号为 CVE-2019-8286 的问题.这个补丁去除了唯一 ID,留下了相同的 ID,也就是说网站仍然会知道有安装了卡巴斯基软件的用户访问了.


Unique Kaspersky AV User ID Allowed 3rd-Party Web Tracking



"
external_category: "Web Exploitation"
---[Visit Website](http://hackernews.cc/archives/26982)

