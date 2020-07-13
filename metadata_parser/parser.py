import json
import os
from os import listdir
from os.path import isfile, join, splitext
import glob
import random


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


	def get_features(self, img_id):
		return self.n_metadata[img_id]

	def get_available_metadata(self):
		return self.n_metadata

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

		classes = ["cloudy", "foggy", "rain", "snow", "sunny"]

		# Get Image Names (id)
		class_idxs = []
		img_ids = []
		for clss in classes:
			# IMAGE_PATH="./weather/{}".format(clss) #path to image class
			IMAGE_PATH="./weather_dataset/train/{}".format(clss)
			imgs =  [im.split('.')[0] for im in listdir(IMAGE_PATH) if isfile(join(IMAGE_PATH, im))] #get all images names
			if class_idxs != []:
				class_idxs.append(class_idxs[-1] + len(imgs))
			else:
				class_idxs.append(len(imgs))
			img_ids += imgs



		print(len(img_ids) / 4 == len(set(img_ids)))
		img_ids = list(set(img_ids))
		# print(type(img_ids[0]))

		# print(class_idxs)

		features = ["hum", "tempm", "dewptm", "vism", "pressurem", "windchillm", "wgustm"]

		### Load Metadata
		with open('metadata.json') as f:
			metadata = json.load(f)

		self.n_metadata = {}
		for data in metadata:
			try:
				idx = img_ids.index(data['id']) # check whether image has a metadata if not skip
				clss = get_class(idx, class_idxs) # check which class image belongs to
				# print(idx, clss)
				feat_list = []
				for key, val in data['weather'].items():
					if key in features:
						feat_list.append({key : val}) #put all relevant features in list
		# 				# print(key, val)
				if(data['id'] == "3414285633"):
					print(feat_list)
				self.n_metadata[data['id']] = (feat_list, clss) # <id : weatherfeat[]> mapping
				# print(self.n_metadata)
			except Exception as e:
				x = 0		
				# print("{} img id NOT FOUND".format(data['id'])) #lots of images not found because we are using subset of original dataset
				# print(x)
		
		print(len(img_ids)) 
		print(len(self.n_metadata))
		# for key,val in self.n_metadata.items():
			# print(key, val)
			# break
		
		# the 8408 - 6509 = 1899 (which is the number of images we got online)
		




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


