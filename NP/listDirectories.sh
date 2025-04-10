#!/bin/bash

for item in "$1"/*; do
	if [ -d "$item" ]; then
		echo "$item"
	fi
done
