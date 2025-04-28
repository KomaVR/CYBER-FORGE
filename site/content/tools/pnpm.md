---
title: "pnpm"
description: "To build the web UI:

. If you have Node.js installed, run corepack enable  to make  available.
If you prefer not to install/use , but have docker available, you can run make docker-ui instead.
The Rust and Cargo version in build.assets/Makefile (search for RUST_VERSION) are required.
The wasm-pack version in build.assets/Makefile (search for WASM_PACK_VERSION) is required.
binaryen (which contains wasm-opt) is required to be installed manually
on linux aarch64 (64-bit ARM). You can check if it's already installed on your system by running which wasm-opt. If not you can install it like apt-get install binaryen (for Debian-based Linux). wasm-pack will install this automatically on other platforms.

"
url: "https://pnpm.io/installation#using-corepack"
category: "Reverse Engineering"
---
