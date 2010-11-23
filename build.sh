#!/bin/sh

node-waf configure $*
node-waf build

# Copy build artifacts in lib folder for NPM install
mkdir -p ./lib
cp ./build/default/iconv.node ./lib
