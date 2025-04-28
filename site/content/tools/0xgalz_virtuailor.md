---
title: "0xgalz/virtuailor"
description: "[607星][3m] [Py]  利用IDA调试获取的信息，自动创建C++的虚表


重复区段: IDA->插件->调试->调试数据 |

查看详情
静态部分:

检测非直接调用
利用条件断点, Hook非直接调用的值赋值过程

动态 部分

创建虚表结构
重命名函数和虚表地址
给反汇编非直接调用添加结构偏移
给非直接调用到虚表之间添加交叉引用

使用

File -> Script File -> Main.py(设置断点) -> IDA调试器执行




"
external_url: "https://github.com/0xgalz/virtuailor"
category: "Miscellaneous"
---
