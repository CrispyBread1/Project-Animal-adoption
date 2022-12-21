import pdb
from models.animal import Animal
from models.shelter import Shelter

import repositories.animal_repository as animal_repository
import repositories.shelter_repository as shelter_repository



animal_repository.delete_all()
shelter_repository.delete_all()



shelter1 = Shelter("Furys", "Edinburgh", "furys@gmail.com")
shelter_repository.save(shelter1)
shelter2 = Shelter("4 Paws", "Edinburgh", "4paws@gmail.com")
shelter_repository.save(shelter2)

animal1 = Animal("Jam Roll", "19/6/20", "Shetland Pony", "This is a very good boy, who loves grass", "https://cdn.images.express.co.uk/img/dynamic/1/590x/secondary/155675.jpg", shelter1)
animal_repository.save(animal1)
animal2 = Animal("Poopy", "12/11/19", "Gecko", "Likes warmth", "https://i.imgflip.com/1wez9h.jpg", shelter2)
animal_repository.save(animal2)
animal3 = Animal("Big Bird", "3/7/18", "Penguin", "Biggest bird", "https://media.glamour.com/photos/56959e35d9dab9ff41b308a0/master/pass/inspired-2015-02-gentoo-penguin-main.jpg", shelter1)
animal_repository.save(animal3)
animal4 = Animal("Furball", "7/12/22", "Brown Bear", "Favourite thing is cuddles", "https://img.freepik.com/premium-photo/funny-bear-cub-sits-ground-forest_265142-3241.jpg?w=2000", shelter1)
animal_repository.save(animal4)



