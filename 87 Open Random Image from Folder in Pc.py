import random, os
from PIL import Image


# path = r"C:\Users\Gero Zayas\Downloads\Images\PinDown__Quotes"

path = input("Insert your path here: ")


random_filename = random.choice(
    [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
)

print(random_filename)


# read the image
im = Image.open(f"{path}/{random_filename}")

# show image
im.show()
