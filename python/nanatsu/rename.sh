#!/bin/bash

for file in *.jpg; do
    NAME=$(basename $file .jpg)
    EXT=$(exiftool $file | grep -P 'File Type\s+:\s+(.*)$' | cut -d ':' -f 2 | awk '{print $1}')
    $(mv $file $NAME.$EXT)
done
