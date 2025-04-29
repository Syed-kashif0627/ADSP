#!/bin/bash

if [[ $# -lt 2 ]]; then
	echo "Less no.of Args provided"
	exit 1
fi

refFile=$1

#check if Refrence File Exists

if [[ ! -f $refFile ]]; then
	echo "Error : refrence doesn't exists"
	exit 1
fi

#collect all remaining files to count 
shift
otherFiles="$@"

for file in $otherFiles; do
	if [[ ! -f $file ]]; then
		echo "Provided file Doesn't Exists"
		exit 1
	fi
done

#create Temp file to hold word cnts
tempFile=$(mktemp)

while read -r word; do
	cnt=0

	for file in $otherFiles; do
		cnt=$((cnt + $(grep -o -w "$word" "$file" | wc -l)))
	done

	echo "$word : $cnt" >> "$tempFile"
done < <(tr ' ' '\n' < "$refFile" | sort |uniq)

cat "$tempFile"

#clean up the temporary file
rm "$tempFile"
