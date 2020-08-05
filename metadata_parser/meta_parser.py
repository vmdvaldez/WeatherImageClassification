import json
import os
from os import listdir
from os.path import isfile, join, splitext
import glob
import random
<<<<<<< HEAD
=======
import pandas as pd
>>>>>>> CNN_ANN_WeatherClass


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

<<<<<<< HEAD
	def __init__(self):

		def get_class(index,class_idxs):

			if index < class_idxs[0]:
				return"cloudy"
			elif index >= class_idxs[0] and index < class_idxs[1]:
				return"foggy"
			elif index >= class_idxs[1] and index < class_idxs[2]:
				return "rain"
			elif index >= class_idxs[2] and index < class_idxs[3]:
				return "snow"
			elif index >= class_idxs[3]:
				return "sunny"
			else:
				print("asserted")
				assert 0
=======


	def __init__(self):

		# features = ["hum", "tempm", "dewptm", "vism", "pressurem", "windchillm", "wgustm"]
		features = ["hum", "tempm", "dewptm", "pressurem", "vism"]
		# features = ["hum", "tempm", "dewptm", "pressurem"]

		def normalize_data():
			# feat_max = [-9999999.0] * len(features)
			# feat_min = [99999999.0] * len(features)
			feat_max = {i : -9999999.0 for i in features}
			feat_min = {i : 99999999.0 for i in features}

			for i in self.datasets:
				for key, val in i.items():
					# print(key, val[0]['hum'])
					for fkey, fval in val[0].items():
						# tmp = float(fval)
						# if tmp == '' or tmp == 'N/A' or tmp <= -999.0:
						# 	continue
						feat_max[fkey] = max(feat_max[fkey], float(fval))
						feat_min[fkey] = min(feat_min[fkey], float(fval))
					# for index in range(len(features)):
						# feat_max[index] = max(float(val[0][features[index]]), feat_max[index])
						# feat_min[index] = min(float(val[0][features[index]]), feat_max[index])
			print("Max Values: ", feat_max)
			print("Minx Values: ", feat_min)
			
			for i in self.datasets:
				for key, val in i.items():
					# print(key, val[0]['hum'])
					feats = {}
					for fkey, fval in val[0].items():
						feats[fkey] = (float(fval) + abs(feat_min[fkey]))/(feat_max[fkey] + abs(feat_min[fkey]))
												
					i[key] =  (feats , val[1])

			# print(self.datasets[0])

		def get_class(im_id):
			for clss, img_ids in self.class_imgs.items():
				try:
					x = img_ids.index(im_id)
					return clss
				except:
					continue

				return None


>>>>>>> CNN_ANN_WeatherClass
		self.datasets =[]
		classes = ["cloudy", "foggy", "rain", "snow", "sunny"]
		dataset = ["train", "val", "test"]

<<<<<<< HEAD
		for dset in dataset:
			# Get Image Names (id)
			class_idxs = []
			img_ids = []
			for clss in classes:
				# IMAGE_PATH="./weather/{}".format(clss) #path to image class
				IMAGE_PATH="./weather_dataset/{}/{}".format(dset, clss)
				imgs =  [im.split('.')[0] for im in listdir(IMAGE_PATH) if isfile(join(IMAGE_PATH, im))] #get all images names
				if class_idxs != []:
					class_idxs.append(class_idxs[-1] + len(imgs))
				else:
					class_idxs.append(len(imgs))
				img_ids += imgs



			print("imgs_ids * 4 is equal to set(img_ids): ", len(img_ids) / 4 == len(set(img_ids)))
			img_ids = list(set(img_ids))
			# print(type(img_ids[0]))

			# print(class_idxs)

			features = ["hum", "tempm", "dewptm", "vism", "pressurem", "windchillm", "wgustm"]

			### Load Metadata
			with open('metadata.json') as f:
				metadata = json.load(f)

			n_metadata = {}
			for data in metadata:
				try:
					idx = img_ids.index(data['id']) # check whether image has a metadata if not skip
					clss = get_class(idx, class_idxs) # check which class image belongs to
					# print(idx, clss)
					feat_list = []
					for key, val in data['weather'].items():
						if key in features:
							if val == '' or val == 'N/A':
								val = -9999 
							feat_list.append({key : val}) #put all relevant features in list
			# 				# print(key, val)
					# if(data['id'] == "3414285633"):
					# 	print(feat_list)
					n_metadata[data['id']] = (feat_list, clss) # <id : weatherfeat[]> mapping
					# print(self.n_metadata)
				except Exception as e:
					x = 0		
					# print("{} img id NOT FOUND".format(data['id'])) #lots of images not found because we are using subset of original dataset
					# print(x)
			
			print("Number of Image Ids: ", len(img_ids)) 
			print("Number of Image Ids with metadata: ", len(n_metadata))
			# for key,val in self.n_metadata.items():
				# print(key, val)
				# break
			self.datasets.append(n_metadata)
			# the 8408 - 6509 = 1899 (which is the number of images we got online)
		print(len(self.datasets))
=======
		
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
				



			### Load Metadata
			metadata = 0
			with open('metadata.json') as f:
				metadata = json.load(f)


			n_metadata = {}
			for data in metadata:
				clss = get_class(data['id']) # check which class image belongs to
				if clss is None:
					continue

				feat_list = {}
				for key, val in data['weather'].items():
					if key in features:
						if val == '' or val == 'N/A' or float(val) <= -999.0:
							val = -9999 
							feat_list = {}
							break
						# feat_list.append({key : val}) #put all relevant features in list
						feat_list[key] = val
				# if(data['id'] == "3414285633"):
				# 	print(feat_list)
				if len(feat_list) > 0:
					n_metadata[data['id']] = (feat_list, clss) # <id : (weatherfeat:{'hum':0, ...}, class)> mapping
				# print(self.n_metadata)
			
			print("Number of Image Ids: ", num_img_ids)
			print("Number of Image Ids with metadata: ", len(n_metadata))
			self.datasets.append(n_metadata)
		# print(len(self.datasets))
		
		normalize_data()

>>>>>>> CNN_ANN_WeatherClass




<<<<<<< HEAD
# wgust, windhcill, vism (lots of missing or -999 values)
# auto encoder on missing data instead of doing the regeneration?


##TODO need to do for data augmenting (change data augment python script to rename to ID.<>.jpg to easily split)

if __name__ == "__main__":
	m = metadata_map()
	feat = m.get_features("3414285633")
	avail_metadata = m.get_available_metadata()
	print(len(avail_metadata))
	print(feat)

# weather_feats = ['hum', 'tempm', 'dewptm', 'vism', 'pressurem', 'windchillm', 'wgustm']
# for data in metadata:
# 	print('id: ', data['id'])
# 	for feats in weather_feats:
# 		print(feats, data['weather'][feats])
=======

# # wgust, windhcill, vism (lots of missing or -999 values)
# # auto encoder on missing data instead of doing the regeneration?


# ##TODO need to do for data augmenting (change data augment python script to rename to ID.<>.jpg to easily split)

if __name__ == "__main__":
	m = metadata_map()
	# feat = m.get_features("3414285633")
	# avail_metadata = m.get_available_metadata()
	# print(len(avail_metadata))
	# print(feat)

>>>>>>> CNN_ANN_WeatherClass


