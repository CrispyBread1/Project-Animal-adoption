import random

def random_image_generator(images):
    num = random.randrange(0, len(images))
    image_of_the_day = images[int(num)]
    for link in image_of_the_day:
        image_of_the_day = link
        return image_of_the_day
