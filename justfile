build_emscripten:
    # Make sure to install/activate and source emsdk_env.fish/.sh
    cargo build --target wasm32-unknown-emscripten
serve_emscripten:
    python3 server.py
build_side:
    emcc cpp-side-module/side_module.cpp \
        -o side_module.wasm \
        -s SIDE_MODULE=1 \
        -O2
