#!/bin/bash

factorial() {
	local num=$1
	local res=1

	for (( i=1;i<=num; i++))
	do
		res=$((res*i))
	done

	echo $res
}

echo "Enter a Positive Integer:"
read num

fact=$(factorial $num)
echo "The Factorial of $num is $fact"


