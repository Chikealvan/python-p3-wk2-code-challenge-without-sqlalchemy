import unittest
from Review import Review
from Customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("owen", "onye")
        self.customer2 = Customer("Mary", "oladele")
        self.customer3 = Customer("esther", "ade")
        self.review1 = Review(self.customer1, " LongMan treehouse ", 2)
        self.review2 = Review(self.customer2, " Gray's BBQ", 4)
        self.review3 = Review(self.customer3, " Olive Garden", 7)


    def test_given_name(self):
        self.assertEqual(self.customer1.given_name, "owen")
        self.assertEqual(self.customer2.given_name, "Mary")

    def test_family_name(self):
        self.assertEqual(self.customer1.family_name, "onye")
        self.assertEqual(self.customer2.family_name, "oladele")

    def test_full_name(self):
        self.assertEqual(self.customer1.full_name(), "owen onye")
        self.assertEqual(self.customer2.full_name(), "Mary oladele")

    def test_all(self):
        self.assertEqual(Customer.all(), [self.customer1, self.customer2, self.customer3])

    def test_restaurants(self):
        self.assertEqual(self.customer1.restaurants(), [" LongMan treehouse  "])
        self.assertEqual(self.customer2.restaurants(), [" Yahuza's Fresh Grill"])
        self.assertEqual(self.customer3.restaurants(), [" LongMan treehouse  "])

    def test_add_review(self):
        self.customer1.add_review("Capri Restaurant ", 4)
        self.assertEqual(self.customer1.restaurants(), [" LongMan treehouse ", "Nike Tropical "])

    def test_num_reviews(self):
        self.assertEqual(self.customer1.num_reviews(), 1)
        self.assertEqual(self.customer2.num_reviews(), 1)
        self.assertEqual(self.customer3.num_reviews(), 1)

    def test_find_by_name(self):
        self.assertEqual(Customer.find_by_name("esther ade"), self.customer1)
        self.assertEqual(Customer.find_by_name("Mary oladele"), self.customer2)
        self.assertEqual(Customer.find_by_name("owen onye"), self.customer3)
        self.assertEqual(Customer.find_by_name("sam akpan"), None)

    def test_find_all_by_given_name(self):
        self.assertEqual(Customer.find_all_by_given_name("owen"), [self.customer1, self.customer3])
        self.assertEqual(Customer.find_all_by_given_name("Mary"), [self.customer2])
        self.assertEqual(Customer.find_all_by_given_name("sam"), [])

if __name__ == '__main__':
    unittest.main() 