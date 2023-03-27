# yaml-cpp for RACE

This repo provides scripts to custom-build the
[yaml-cpp library](https://github.com/jbeder/yaml-cpp) for RACE.

## License

The yaml-cpp library is licensed under the MIT license.

Only the build scripts in this repo are licensed under Apache 2.0.

## Dependencies

yaml-cpp has no dependencies on any custom-built libraries.

## How To Build

The [ext-builder](https://github.com/tst-race/ext-builder) image is used to
build yaml-cpp.

```
git clone https://github.com/tst-race/ext-builder.git
git clone https://github.com/tst-race/ext-yaml-cpp.git
./ext-builder/build.py \
    --target linux-x86_64 \
    ./ext-yaml-cpp
```

## Platforms

yaml-cpp is built for the following platforms:

* `linux-x86_64`
* `linux-arm64-v8a`
* `android-x86_64`
* `android-arm64-v8a`

## How It Is Used

yaml-cpp is used directly by the RACE core.
