import json
import os
from os import listdir
from os.path import isfile, join, splitext
import glob
import random
import pandas as pd


class metadata_map():

	# id
		# weather
			# hum
			# tempm
			# dewptm
			# vism
			# pressurem
			# windchillm
			# wgustm

	# Get Image Names to match the image id with metadata


	def get_features(self, img_id, dset="train"):
		x = -1
		if dset == "train":
			x = 0
		elif dset == "val":
			x = 1
		elif sdet == "test":
			x=2
		else :
			assert 0
		return self.datasets[x][img_id]

	def get_available_metadata(self, dset="train"):
		x = -1
		if dset == "train":
			x = 0
		elif dset == "val":
			x = 1
		elif dset == "test":
			x=2
		else :
			assert 0
		return self.datasets[x]

	def __init__(self):

		def get_class(im_id):
			for clss, img_ids in self.class_imgs.items():
				try:
					x = img_ids.index(im_id)
					return clss
				except:
					continue

				return None


		self.datasets =[]
		classes = ["cloudy", "foggy", "rain", "snow", "sunny"]
		dataset = ["train", "val", "test"]

		
		for dset in dataset:
			self.class_imgs = {}
			num_img_ids = 0
			# Get Image Names (id)
			for clss in classes:
				img_ids = []
				# IMAGE_PATH="./weather/{}".format(clss) #path to image class
				IMAGE_PATH="./weather_dataset/{}/{}".format(dset, clss)
				imgs =  [im.split('.')[0] for im in listdir(IMAGE_PATH) if isfile(join(IMAGE_PATH, im))] #get all images names
				img_ids += imgs
				img_ids = list(set(img_ids))
				num_img_ids += len(img_ids)
				if clss not in self.class_imgs.keys():
					self.class_imgs[clss] = img_ids
				else:
					self.class_imgs[clss] += img_ids
				

			# features = ["hum", "tempm", "dewptm", "vism", "pressurem", "windchillm", "wgustm"]
			features = ["hum", "tempm", "dewptm", "pressurem"]

			### Load Metadata
			metadata = 0
			with open('metadata.json') as f:
				metadata = json.load(f)


			n_metadata = {}
			for data in metadata:
				clss = get_class(data['id']) # check which class image belongs to
				if clss is None:
					continue

				feat_list = []
				for key, val in data['weather'].items():
					if key in features:
						if val == '' or val == 'N/A':
							val = -9999 
						feat_list.append({key : val}) #put all relevant features in list
				# if(data['id'] == "3414285633"):
				# 	print(feat_list)
				n_metadata[data['id']] = (feat_list, clss) # <id : weatherfeat[]> mapping
				# print(self.n_metadata)
			
			print("Number of Image Ids: ", num_img_ids)
			print("Number of Image Ids with metadata: ", len(n_metadata))
			self.datasets.append(n_metadata)
		# print(len(self.datasets))




# # wgust, windhcill, vism (lots of missing or -999 values)
# # auto encoder on missing data instead of doing the regeneration?


# ##TODO need to do for data augmenting (change data augment python script to rename to ID.<>.jpg to easily split)

if __name__ == "__main__":
	m = metadata_map()
	# feat = m.get_features("3414285633")
	# avail_metadata = m.get_available_metadata()
	# print(len(avail_metadata))
	# print(feat)



