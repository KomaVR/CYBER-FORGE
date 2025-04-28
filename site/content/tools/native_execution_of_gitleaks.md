---
title: "native execution of GitLeaks"
description: "
Create a .pre-commit-config.yaml file at the root of your repository with the following content:
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.24.2
    hooks:
      - id: gitleaks

for a  or use the gitleaks-docker pre-commit ID for executing GitLeaks using the official Docker images
"
external_url: "https://github.com/gitleaks/gitleaks/releases"
category: "Miscellaneous"
---
