#!/bin/bash

set -e

./scripts/gen.sh
CC=clang CXX=clang++ cmake --build build $@

