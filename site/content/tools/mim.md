---
title: "MIM"
description: "
Now you need to append the public key ~/.ssh/id_ed25519.pub from your client to the ~/.ssh/authorized_keys file on your server. Since we're presumable still at home on the LAN, we're probably safe from  attacks, so we will use ssh-copy-id to transfer and append the public key:
ssh-copy-id user@server

/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: \"/home/user/.ssh/id_ed25519.pub\"
The authenticity of host 'host (192.168.1.96)' can't be established.
ECDSA key fingerprint is SHA256:QaDQb/X0XyVlogh87sDXE7MR8YIK7ko4wS5hXjRySJE.
Are you sure you want to continue connecting (yes/no)? yes
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@host's password:

Number of key(s) added: 1

Now try logging into the machine, with:   \"ssh 'user@host'\"
and check to make sure that only the key(s) you wanted were added.


"
url: "https://en.wikipedia.org/wiki/Man-in-the-middle_attack"
category: "Miscellaneous"
---
