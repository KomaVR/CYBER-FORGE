---
title: "Alex Ionescu"
description: "
You said it works on uncached memory, but all your demos ensure that the memory is cached!
Making it work on uncached memory is trickier, and often requires a bit of tweaking of the parameters. Thus, we ensure that the memory is cached in the PoC to make it easier to reproduce. However, you can simply remove the code that caches the values and replace it by a clflush to test the exploit on uncached memory (see Video #5 for an example).
Although not in the original blog post by Google, this was also confirmed by independent researchers (e.g. , Raphael Carvalho, Pavel Boldin).
"
external_url: "https://twitter.com/aionescu/status/951261470343360513"
category: "Black Hat Tools"
---
