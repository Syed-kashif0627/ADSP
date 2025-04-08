#!/bin/bash

if [ $# -ne 3 ]; then
	echo Insufficient cmd line arguments provided!!
	exit 1
fi

fName=$1
start=$2
end=$3

if [ ! -f $fName ]; then
	echo file not Found
	exit 1
fi

sed -n "${start},${end}p" "$fName"

 
