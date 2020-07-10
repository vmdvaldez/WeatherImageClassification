#!/bin/bash

ROOT_IMG_DIR="<PATH-TO-SPLIT-DATA>/weather_dataset/train/"

classes=("cloudy" "foggy" "rain" "snow" "sunny")


for i in "${classes[@]}"
do
	printf "Augmenting Images in $i"
	python3 ./data_augment.py ${ROOT_IMG_DIR}$i/
done
