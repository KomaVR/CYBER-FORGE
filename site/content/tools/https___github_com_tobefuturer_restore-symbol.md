---
description: "
Configure IPPatch Options


You can config IPAPatch's behavior with Tools/options.plist



Name
Description
Default




RESTORE_SYMBOLS
When YES, IPAPatch will try to restore symbol table from Mach-O for debugging propose (with tools from , also thanks to @henrayluo and @dannion)
NO


CREATE_IPA_FILE
When YES, IPAPatch will generate a ipa file on each build. Genrated file is located at SRCROOT/Product
NO


IGNORE_UI_SUPPORTED_DEVICES
When YES, IPAPatch will delete UISupportedDevices from source app's Info.plist
NO


REMOVE_WATCHPLACEHOLDER
When YES, IPAPatch will remove com.apple.WatchPlaceholder folder from source app's bundle
YES


USE_ORIGINAL_ENTITLEMENTS
When YES, IPAPatch will use source app's entitlements to resign, you need to make sure your Provisioning Profile matches the entitlements, or you need to disable AMFI on target device
NO





"
external_category: "Reverse Engineering"
---
[Visit Website](https://github.com/tobefuturer/restore-symbol)

[Visit Website](https://github.com/tobefuturer/restore-symbol)

