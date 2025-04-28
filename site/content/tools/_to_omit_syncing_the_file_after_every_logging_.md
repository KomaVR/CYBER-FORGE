---
title: ""to omit syncing the file after every logging""
description: "
After you've added a prefix to the firewall logs, we need to tell rsyslog to send those lines to its own file. Do this by creating the file /etc/rsyslog.d/10-iptables.conf and adding this:
:msg, contains, \"[IPTABLES] \" /var/log/iptables.log
& stop

If you're expecting a lot if data being logged by your firewall, prefix the filename with a - . For example:
:msg, contains, \"[IPTABLES] \" -/var/log/iptables.log
& stop

Note: Remember to change the prefix to whatever you use.
For the lazy:
cat << EOF | sudo tee /etc/rsyslog.d/10-iptables.conf
:msg, contains, \"[IPTABLES] \" /var/log/iptables.log
& stop
EOF
"
external_category: "Miscellaneous"
---[Visit Website](https://www.rsyslog.com/doc/v8-stable/configuration/actions.html#regular-file)

