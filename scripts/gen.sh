#!/bin/bash

set -e

cmake -S . -B build -GNinja $@

