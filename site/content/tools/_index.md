---
title: "Tools"
description: "A collection of hacking tools, utilities, and resources."
---

# Tools

Welcome to the Tools section!  
Here you’ll find a living arsenal of cybersecurity tools, dork lists, recon utilities, and more.

Explore freely:

{{ range (where .Site.RegularPages "Section" "tools").ByTitle }}
<div class="tool-item">
  <h2><a href="{{ .RelPermalink }}">{{ .Title }}</a></h2>
  <p>{{ .Params.description }}</p>
</div>
{{ end }}
