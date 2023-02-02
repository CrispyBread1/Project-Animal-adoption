from repositories.animal_repository import animal_repository
import unittest

class TestPetShop(unittest.TestCase):

    def test_animals_added_to_sql(self):
            animals = animal_repository.select_all()
            sum = len(animals)
            self.assertEqual(5, sum)

if __name__ == '__main__':
    unittest.main()