from PIL import Image, ImageOps, ImageEnhance
import glob
import os
import random


def mirror_img(img_name, img, ext):
	img_name = img_name + "mir"
	mirror = ImageOps.mirror(img)
	mirror.save(img_name + ext)
	return img_name

def contrast_img(img_name, img, ext):
	img_name = img_name + "cont"
	n_img = ImageEnhance.Contrast(img)

	x = round(random.uniform(0.8, 1.5),2)
	while x == 1.0:
		x = round(random.uniform(0.8, 1.5),2)

	enhanced_img = n_img.enhance(x)
	# enhanced_img.save(img_name + ext)
	return img_name, enhanced_img, ext


def brighten_img(img_name, img, ext):
	img_name = img_name + "brght"
	n_img = ImageEnhance.Brightness(img)

	x = round(random.uniform(0.8, 1.2),2)
	while x == 1.0:
		x = round(random.uniform(0.8, 1.2),2)

	enhanced_img = n_img.enhance(x)
	# enhanced_img.save(img_name + ext)
	return img_name, enhanced_img, ext


def sharpen_img(img_name, img, ext):
	img_name = img_name + "shrp"
	n_img = ImageEnhance.Sharpness(img)

	x = round(random.uniform(0.1, 1.5),2)
	while x == 1.0:
		x = round(random.uniform(0.1, 1.5),2)

	enhanced_img = n_img.enhance(x)
	# enhanced_img.save(img_name + ext)
	return img_name, enhanced_img, ext


def save_image(img_name, img, ext):
	img.save(img_name + ext)


if __name__  == "__main__":

	image_list = glob.glob("./images/*")

	# create mirrored images
	for im in image_list:
		img_name, ext = os.path.splitext(im)
		img = Image.open(img_name + ext)
		mirror_img(img_name, img, ext)


	image_list = glob.glob("./images/*")

	# apply random augmentation to all images
	for i in image_list:
		img_name, ext = os.path.splitext(i)
		img = Image.open(img_name + ext)

		img_name, img, ext = sharpen_img(img_name, img, ext)
		img_name, img, ext = brighten_img(img_name, img, ext)
		img_name, img, ext = contrast_img(img_name, img, ext)

		save_image(img_name, img, ext)

	
