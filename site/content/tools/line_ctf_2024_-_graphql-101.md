---
title: "Line CTF 2024 - graphql-101"
description: "Batch query

可以透過 Array-based query 一次送好幾個請求
Apollo GraphQL 預設不啟用 Array Batching
常見情境：Password brute-force, Rate limit bypass, DoS
[{ query: 'query { book(id: 1) { __typename } }' },{ query: 'query { book(id: 1) { __typename } }' }]
JSON list based batching 不能用時，可以嘗試 Query name based batching

{\"query\": \"query { kaibro: Query { meow } kaibro1: Query { meow } }\"}


Example:


corCTF 2023 - force



"
external_url: "https://adragos.ro/line-ctf-2024/#graphql-101"
category: "Grey Hat Tools"
---
