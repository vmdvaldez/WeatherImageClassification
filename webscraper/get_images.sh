#!/bin/bash

IMG_PATH="images/"

TEST=($(cat http_logs/Test.txt))

echo $TEST
x = 0

mkdir $IMG_PATH

for i in "${TEST[@]}"
do
	curl -o ${IMG_PATH}${x}.jpg $i
	((x = x + 1))
done
