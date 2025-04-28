---
title: "known issue"
description: "
If you still receive the error, sign_and_send_pubkey: signing failed: agent refused operation - it is a  that openssh 8.9p1 and higher has issues with YubiKey. Adding KexAlgorithms -sntrup761x25519-sha512@openssh.com to /etc/ssh/ssh_config often resolves the issue.
"
external_url: "https://bbs.archlinux.org/viewtopic.php?id=274571"
category: "Miscellaneous"
---
