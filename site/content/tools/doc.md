---
title: "doc"
description: "
Javascript Proxy


嘗試取得被 Proxy 保護住的 flag: var p = new Proxy({flag: window.flag || 'flag'}, { get: () => 'nope' }
解法: Object.getOwnPropertyDescriptor(p, 'flag')
Example

corCTF 2022 - sbxcalc



"
external_category: "Miscellaneous"
---[Visit Website](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)

