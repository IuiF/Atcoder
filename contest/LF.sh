#!/bin/bash

directory=$(pwd)

find "$directory" -type f \( -name "*.in" -o -name "*.out" \) -print0 | while IFS= read -r -d '' file; do
    sed -i 's/\r$//' "$file"
done
