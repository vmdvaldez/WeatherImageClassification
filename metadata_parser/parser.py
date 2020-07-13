import json
from os import listdir
from os.path import isfile, join, splitext


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
		for i in self.n_metadata:
			key, val = list(i[0].items())[0]
			# print(key, type(key))
			if key == str(img_id):
				print(i[0][img_id])
				return(img_id, i[0][img_id], i[1])
			# if i[0][img_id]:
				# return i[0][img_id]

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
			IMAGE_PATH="./Image/{}".format(clss)
			imgs =  [splitext(im)[0] for im in listdir(IMAGE_PATH) if isfile(join(IMAGE_PATH, im))]
			if class_idxs != []:
				class_idxs.append(class_idxs[-1] + len(imgs))
			else:
				class_idxs.append(len(imgs))
			img_ids += imgs

		# print(img_ids)
		# print(class_idxs)

		features = ["hum", "tempm", "dewptm", "vism", "pressurem", "windchillm", "wgustm"]

		# # # Get Relevant Metadata
		with open('metadata.json') as f:
			metadata = json.load(f)

		self.n_metadata = []

		for data in metadata:

			try:
				
				idx = img_ids.index(data['id'])
				clss = get_class(idx, class_idxs)
				# print(idx, clss)
				
				# print("FOUND")
				feat_list = []

				for key, val in data['weather'].items():
					if key in features:
						feat_list.append({key : val})
		# 				# print(key, val)
				self.n_metadata.append( ({data['id'] : feat_list}, clss ))
				# print(self.n_metadata[-1])
				# print(idx)
			except Exception as e:
				l = 0
				# print("NOT FOUND")
		
		print(len(img_ids)) # total of 8408 images 
		print(len(self.n_metadata)) ## 6509 images with metadata
		# the 8408 - 6509 = 1899 (which is the number of images we got online)
		




# wgust, windhcill, vism (lots of missing or -999 values)
# auto encoder on missing data instead of doing the regeneration?


##TODO need to do for data augmenting (change data augment python script to rename to ID.<>.jpg to easily split)

if __name__ == "__main__":
	m = metadata_map()
	feat = m.get_features("12381129")
	print(feat)

# weather_feats = ['hum', 'tempm', 'dewptm', 'vism', 'pressurem', 'windchillm', 'wgustm']
# for data in metadata:
# 	print('id: ', data['id'])
# 	for feats in weather_feats:
# 		print(feats, data['weather'][feats])


