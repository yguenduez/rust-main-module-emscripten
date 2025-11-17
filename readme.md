# Dynamic Linking with Rust as main Module

This example uses emcc 4.0.19

```sh
emsdk install 4.0.19
emsdk activate 4.0.19
source emsdk_env.sh
```

## Build the side module first

```sh
emcc cpp-side-module/side_module.cpp \
    -o side_module.wasm \
    -s SIDE_MODULE=1 \
    -O2
```

## Then build the main module

```sh
cargo +nightly build --target wasm32-unknown-emscripten
```

## Then serve the main module

```sh
python3 server.py
```

Open a browser and navigate to http://localhost:8000
