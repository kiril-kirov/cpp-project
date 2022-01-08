#!/bin/bash

set -e

print_usage() {
    echo "Usage: $0 release|debug|relwithdebinfo"
    exit 1
}

build_type=debug
if [[ $# -ge 1 ]]
then
    build_type=$1
    shift
fi

if [[ "$build_type" == "debug" ]]
then
    cmake_build_type="Debug"
elif [[ "$build_type" == "release" ]]
then
    cmake_build_type="Release"
elif [[ "$build_type" == "relwithdebinfo" ]]
then
    cmake_build_type="RelWithDebInfo"
else
    print_usage
fi

build_dir="build/$build_type"

CC=clang CXX=clang++ cmake -S . -B "$build_dir" -GNinja -DCMAKE_BUILD_TYPE=$cmake_build_type
cmake --build "$build_dir" $@
