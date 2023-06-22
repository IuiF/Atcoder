#!/bin/bash

for i in {1..306}
do
    number=$(printf "%03d" $i)
    acc new abc$number
    sleep 2
done
