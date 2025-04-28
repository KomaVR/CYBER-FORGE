---
title: "BalsnCTF 2019 - 卍乂Oo韓國魚oO乂卍"
description: "
DNS rebinding

rebind.network


  # butit still works
  A.192.168.1.1.forever.rebind.network
  
  #alternate between localhost and 10.0.0.1 forever
  A.127.0.0.1.1time.10.0.0.1.1time.repeat.rebind.network
  
  #first respond with 192.168.1.1 then 192.168.1.2. Now respond 192.168.1.3forever.
  A.192.168.1.1.1time.192.168.1.2.2times.192.168.1.3.forever.rebind.network
  
  #respond with 52.23.194.42 the first time, then whatever `whonow--default-address`
  # isset to forever after that (default: 127.0.0.1)
  A.52.23.194.42.1time.rebind.network




rbndr.us

36573657.7f000001.rbndr.us


Example


DEFCON CTF 2019 Qual - ooops



"
external_url: "https://github.com/w181496/My-CTF-Challenges/tree/master/Balsn-CTF-2019#%E5%8D%8D%E4%B9%82oo%E9%9F%93%E5%9C%8B%E9%AD%9Aoo%E4%B9%82%E5%8D%8D-koreanfish"
category: "White Hat Tools"
---
