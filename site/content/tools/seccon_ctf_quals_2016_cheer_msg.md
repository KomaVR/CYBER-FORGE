---
title: "Seccon CTF quals 2016 cheer_msg"
description: "
scanf(\"%d\", &num)

Used with alloca(num)

Since alloca allocates memory from the stack frame of the caller, there is an instruction sub esp, eax to achieve that.
If we make num negative, it will have overlapped stack frame.
E.g. 


Use num to access some data structures

In most of the time, programs only check the higher bound and forget to make num unsigned.
Making num negative may let us overwrite some important data to control the world!



"
external_category: "Miscellaneous"
---[Visit Website](https://github.com/ctfs/write-ups-2016/tree/master/seccon-ctf-quals-2016/exploit/cheer-msg-100)

