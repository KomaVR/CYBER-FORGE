---
description: "Version 2.0 (21/02/2016) :

A new module (privesc) for using system privileges of an Oracle user (e.g. CREATE ANY PROCEDURE) in order to gain privileged access (i.e. DBA). System privileges that can be used by ODAT in this version:

CREATE ANY PROCEDURE: execution of arbitrary requests with APEX_040200's privileges (e.g. modification of Oracle users' passwords)
CREATE PROCEDURE and EXECUTE ANY PROCEDURE: execution of arbitrary requests as SYS (e.g. gives DBA role to a user)
CREATE ANY TRIGER (and CREATE PROCEDURE): execution of arbitrary requests as SYS (e.g. gives DBA role to a user)
ANALYZE ANY (and CREATE PROCEDURE): execution of arbitrary requests as SYS (e.g. gives DBA role to a user)
CREATE ANY INDEX (and CREATE PROCEDURE): execution of arbitrary requests as SYS (e.g. gives DBA role to a user)


The module privesc can be used to get all system privileges and roles granted. It shows system privileges that can be used to gain privileged access.
new option (-vvv) for showing SQL requests sent by ODAT in debugs
standalone version moved to releases ()

"
external_category: "Reverse Engineering"
---
[Visit Website](https://github.com/quentinhardy/odat/releases/)

[Visit Website](https://github.com/quentinhardy/odat/releases/)

