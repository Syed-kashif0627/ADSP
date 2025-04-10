#!/bin/bash

if [ $# -eq 0 ]; then
	echo Insufficient args provided
	exit 1
fi


for item in $@; do
	if [ -f $item ]; then
		numLines=$(wc -l < $item)
		echo $item is a file with $numLines lines
	elif [ -d $item ]; then
		echo $item is a Directory
	else
		echo $item is neither a file nor Directory
	fi
done
