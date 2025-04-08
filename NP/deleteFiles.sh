#!/bin/bash

if [ $# -lt 2 ]; then
	echo Less No.of aruguments provided
	exit 1
fi

word=$1
shift # shift the aruguments so files remain

for file in $@; do
	if [ -f $file ]; then
		sed -i "/$word/d" "$file"
		echo "Processed: $file"
	else
		echo "$file is not a valid file"
	fi
done
