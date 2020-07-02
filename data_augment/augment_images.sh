#!/bin/bash

ROOT_IMG_DIR="/######/Desktop/APS360Project/Image/"

classes=("cloudy" "foggy" "rain" "snow" "sunny")


for i in "${classes[@]}"
do
	printf "Augmenting Images in $i"
	python3 ./data_augment.py ${ROOT_IMG_DIR}$i/
done
