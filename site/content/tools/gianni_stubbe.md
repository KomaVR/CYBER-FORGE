---
title: "Gianni Stubbe"
description: "
Docker (thanks , anarcat, Francesco Colista, arbal)
Note: the Docker image runs by default in server mode, if no parameters are given. This is equivalent to running the tool as asn -l :: (run server, bind to all interfaces - this is necessary to expose the server port to the host machine). You can run the server with different options by explicitly passing -l [options]. It's also possible to pass an IpQualityScore, ipinfo.io and/or Cloudflare API token (both client and server runs) by setting, respectively, the IQS_TOKEN, IPINFO_TOKEN and CLOUDFLARE_TOKEN environment variables (examples below) in the container.
Usage examples:

Start server: docker run -it -p 49200:49200 nitefood/asn
Client mode: docker run -it nitefood/asn 1.1.1.1
Supply an IQS token: docker run -it -e IQS_TOKEN=\"xxx\" nitefood/asn [...]
Supply multiple tokens: docker run -it -e IQS_TOKEN=\"xxx\" -e IPINFO_TOKEN=\"yyy\" -e CLOUDFLARE_TOKEN=\"zzz\" nitefood/asn [...]

"
url: "https://github.com/33Fraise33"
category: "Miscellaneous"
---
