---
title: "manufacturing error"
description: "
Generate a list of trusted USB devices as a JSON file (trusted/auth.json) with VID and PID attributes containing the first three devices connected on November 30, 1984:
~$ sudo usbrip events genauth trusted/auth.json -a vid pid -n 3 -d '1984-11-30'
⚠️ Warning: there are cases when different USB flash drives might have identical serial numbers. This could happen as a result of a  or just some black hats were able to rewrite the drive's memory chip which turned out to be non-one-time programmable and so on... Anyways, \"no system is safe\". usbrip does not handle such cases in a smart way so far, namely it will treat a pair of devices with identical SNs (if there exists one) as the same device regarding to the trusted device list and genauth module.
"
external_category: "Miscellaneous"
---[Visit Website](https://forums.anandtech.com/threads/changing-creating-a-custom-serial-id-on-a-flash-drive-low-level-blocks.2099116/)

