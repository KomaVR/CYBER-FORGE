---
title: "Issue #1"
description: "
Then find and edit or add these settings, and set values as per your requirements:



Setting
Valid Values
Example
Description
Notes




AllowGroups
local UNIX group name
AllowGroups sshusers
group to allow SSH access to



ClientAliveCountMax
number
ClientAliveCountMax 0
maximum number of client alive messages sent without response



ClientAliveInterval
number of seconds
ClientAliveInterval 300
timeout in seconds before a response request



ListenAddress
space separated list of local addresses
ListenAddress 0.0.0.0ListenAddress 192.168.1.100
local addresses sshd should listen on
See  for important details.


LoginGraceTime
number of seconds
LoginGraceTime 30
time in seconds before login times-out



MaxAuthTries
number
MaxAuthTries 2
maximum allowed attempts to login



MaxSessions
number
MaxSessions 2
maximum number of open sessions



MaxStartups
number
MaxStartups 2
maximum number of login sessions



PasswordAuthentication
yes or no
PasswordAuthentication no
if login with a password is allowed



Port
any open/available port number
Port 22
port that sshd should listen on




Check man sshd_config for more details what these settings mean.
"
external_category: "Miscellaneous"
---[Visit Website](https://github.com/imthenachoman/How-To-Secure-A-Linux-Server/issues/1)

