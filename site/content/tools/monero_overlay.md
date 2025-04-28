---
title: "Monero overlay"
description: "
Gentoo 
emerge --noreplace eselect-repository
eselect repository enable monero
emaint sync -r monero
echo '*/*::monero ~amd64' >> /etc/portage/package.accept_keywords
emerge net-p2p/monero
"
external_category: "Miscellaneous"
---[Visit Website](https://github.com/gentoo-monero/gentoo-monero)

