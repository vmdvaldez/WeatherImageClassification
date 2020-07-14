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


		xclasses = ["foggy", "rain", "snow"]

		for clss in xclasses:
			rename_img = glob.glob("./pinterest_images/{}/*".format(clss))
			for i in rename_img:
				x = int(random.uniform(0,1000000))

				if str(x) in img_ids:
					continue
				path = splitext(i)[0].rsplit('/', 1)[0]
				os.rename(i, path + '/{}'.format(x) + ".jpg")


		# print(len(img_ids))
		# print(len(set(img_ids)))
		# print(class_idxs)

		# features = ["hum", "tempm", "dewptm", "vism", "pressurem", "windchillm", "wgustm"]

		# ### Load Metadata
		# with open('metadata.json') as f:
		# 	metadata = json.load(f)

		# self.n_metadata = {}
		# for data in metadata:
		# 	try:	
		# 		idx = img_ids.index(data['id']) # check whether image has a metadata if not skip
		# 		clss = get_class(idx, class_idxs) # check which class image belongs to
		# 		# print(idx, clss)
		# 		feat_list = []
		# 		for key, val in data['weather'].items():
		# 			if key in features:
		# 				feat_list.append({key : val}) #put all relevant features in list
		# # 				# print(key, val)
		# 		# if(data['id'] == "12381129"):
		# 		# 	print(feat_list)
		# 		self.n_metadata[data['id']] = (feat_list, clss) # <id : weatherfeat[]> mapping
		# 		# print(self.n_metadata)
		# 	except Exception as e:
				# print("{} img id NOT FOUND".format(data['id'])) #lots of images not found because we are using subset of original dataset
				# x = 0
				# print(x)
		
		# print(len(img_ids)) # total of 8408 images 
		# print(len(self.n_metadata)) ## 6509 images with metadata
		# for key,val in self.n_metadata.items():
			# print(key, val)
			# break
		
		# the 8408 - 6509 = 1899 (which is the number of images we got online)
		




# wgust, windhcill, vism (lots of missing or -999 values)
# auto encoder on missing data instead of doing the regeneration?


##TODO need to do for data augmenting (change data augment python script to rename to ID.<>.jpg to easily split)

if __name__ == "__main__":
	m = metadata_map()
	# feat = m.get_features("12381129")
	# print(feat)

# weather_feats = ['hum', 'tempm', 'dewptm', 'vism', 'pressurem', 'windchillm', 'wgustm']
# for data in metadata:
# 	print('id: ', data['id'])
# 	for feats in weather_feats:
# 		print(feats, data['weather'][feats])


