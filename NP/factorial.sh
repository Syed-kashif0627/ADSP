#!/bin/bash

echo "Enter a Positive Integer:"
read num

fact=1

for(( i=1; i<=num; i++))
do
	fact=$((fact*i))
done

echo "The Factorial of $num is $fact"
