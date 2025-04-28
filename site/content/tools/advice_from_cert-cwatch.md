---
title: "advice from cert-cwatch"
description: "
If you are using offline mode install the ADLDS role on a Windows Server edition in order to use dsamain.exe and mount the NTDS database.
The version of the Windows Server you install the role on should be the same as the version of the Windows Server which the ntds.dit came from. If you do not know that version and you have the SOFTWARE hive available, you can look at the CurrentVersion key.
If you can not mount the ntds.dit file with dsamain.exe, this might be because the NTDS dump is corrupted. In that case, you can follow .
"
external_category: "Miscellaneous"
---[Visit Website](https://github.com/ANSSI-FR/ADTimeline/issues/17#issuecomment-1984049537)

