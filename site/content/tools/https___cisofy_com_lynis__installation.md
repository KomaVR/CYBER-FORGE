---
title: "https://cisofy.com/lynis/#installation"
description: "
Install lynis.  has detailed instructions on how to install it for your distribution.
On Debian based systems, using CISOFY's community software repository:
sudo apt install apt-transport-https ca-certificates host
sudo wget -O - https://packages.cisofy.com/keys/cisofy-software-public.key | sudo apt-key add -
sudo echo \"deb https://packages.cisofy.com/community/lynis/deb/ stable main\" | sudo tee /etc/apt/sources.list.d/cisofy-lynis.list
sudo apt update
sudo apt install lynis host
"
external_url: "https://cisofy.com/lynis/#installation"
category: "Miscellaneous"
---
