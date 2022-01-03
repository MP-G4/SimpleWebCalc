#!/bin/bash

cd ./database && ./build.sh

wait

cd ../midware && ./build-test.sh
