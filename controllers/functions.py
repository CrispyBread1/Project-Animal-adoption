import random

def random_image_generator(images):
    num = random.randrange(0, len(images))
    
    animal = images[int(num)]
    animal_of_the_day = []
    animal_of_the_day.append(animal.name)
    animal_of_the_day.append(animal.img)
    
    return animal_of_the_day
    

    