---
title: "pWhois server"
description: "Detailed hop info reporting and RPKI validation can be turned on by passing the [-d|--detailed] command line switch. This will enable querying the public  and the RIPEStat RPKI validation API for every hop in the mtr trace. Relevant info will be displayed as a \"tree\" below the hop data, in addition to Team Cymru's server output (which only reports the AS name that the organization originating the prefix gave to its autonomous system number). This can be useful to figure out more details regarding the organization's name, the prefix' intended designation, and even (to a certain extent) its geographical scope.
Furthermore, this will enable a warning whenever RPKI validation fails for one of the hops in the trace, indicating which AS in the path is wrongly announcing (as per current pWhois data) the hop prefix, indicating a potential route leak or BGP hijacking incident."
external_url: "https://pwhois.org/server.who"
category: "Miscellaneous"
---
