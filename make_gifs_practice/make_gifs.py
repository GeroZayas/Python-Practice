import imageio
import os


def create_gif(file_names, out_file="image.gif", duration=1.5):
    images = ['IMG_20210408_141755.jpg','IMG_20210408_141919.jpg', 'IMG_20210408_153019.jpg']
    for filename in file_names:
        images.append(imageio.imread(filename))
    imageio.mimsave(out_file, images, duration=duration)


images = []

folder_path = "./images/"

for filename in os.listdir(folder_path):
    print(filename)


create_gif(file_names=images)
