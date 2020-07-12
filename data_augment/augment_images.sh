#!/bin/bash

#ROOT_IMG_DIR="/mnt/c/Users/Vincent/Desktop/APS360Project/weather_dataset/train/"
ROOT_IMG_DIR=$1

classes=("cloudy" "foggy" "rain" "snow" "sunny")


for i in "${classes[@]}"
do
	printf "Augmenting Images in $i"
	python3 ./data_augment.py ${ROOT_IMG_DIR}$i/
done
