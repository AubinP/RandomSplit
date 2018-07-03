import random, shutil, glob, os
from os.path import isfile, join
from os import listdir

# Setup paths variable
path = "" # Folder images path
target_folder_images = "" # Target folder images
target_folder = "" # Target sub folder images

# User insert the number he want
number_pictures_taken = int(input("Enter the number images to extract: "))

# Initializing
i = 0
j = 1
k = 0


filename = [f for f in listdir(path) if isfile(join(path, f))]
for x in range(number_pictures_taken):
	try:
		shutil.copyfile(path + '\\' + filename[x], target_folder_images + filename[x]) # Copy file from path to the target folder
	except:
		print('Cannot insert path in the array!')

random.shuffle(filename) # Put name in a random index in the array

for i in range(number_pictures_taken):
	target_folder_temp = target_folder + str(j) + '\\' # Loop the end number of the folder
	shutil.move(target_folder_images + filename[i], target_folder_temp) # Move images into sub folders
	# Alternate Folder1 to Folder5 in a loop
	if j == 5:
		j = 1
	else:
		j = j + 1