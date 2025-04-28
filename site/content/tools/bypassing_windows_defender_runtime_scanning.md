---
title: "Bypassing Windows Defender Runtime Scanning"
description: "枚举测试调用哪些api会触发Defender检测，发现创建CreateProcess和CreateRemoteThread时触发Defender，提出三种解决方案，重写api调用、添加修改指令动态解密加载、使Defender不扫描该区域，作者针对Defender扫描机制(虚拟内存比较大，只扫描MEM_PRIVATE或RWX页权限)，当可疑的API被调用时动态设置PAGE_NOACCESS内存权限Defender不会对其安全扫描"
url: "https://labs.f-secure.com/blog/bypassing-windows-defender-runtime-scanning/"
category: "Grey Hat Tools"
---
