---
title: "RIPEStat RPKI validation API"
description: "
It will perform RPKI validity lookups for every possible IP. Data is validated using the . For path traces, the tool will match each hop's ASN/Prefix pair (retrieved from the Prefix Whois public server) with relevant published RPKI ROAs. In case of origin AS mismatch or unallowed more-specific prefixes, it will warn the user of a potential route leak / BGP hijack along with the offending AS in the path (requires -d option, see below for usage info).

Read more about BGP hijacking here.
Read more about RPKI here, here, or here.

"
url: "https://stat.ripe.net/docs/data_api#rpki-validation"
category: "Miscellaneous"
---
