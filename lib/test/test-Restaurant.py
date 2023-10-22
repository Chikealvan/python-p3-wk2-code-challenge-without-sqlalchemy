import unittest

from Review import Review
from Restaurant import Restaurant

class TestRestaurant(unittest.TestCase):

    def test_name(self):
        Restaurant = Restaurant("Test Restaurant")
        self.assertEqual(Restaurant.name(), "Test Restaurant")

    def test_reviews(self):
        restaurant = Restaurant("Test Restaurant")
        self.assertEqual(restaurant.reviews(), [])

    def test_customers(self):
        restaurant = Restaurant("Test Restaurant")
        review1 = Review("Customer esther", 4)
        review2 = Review("Customer damola", 5)
        restaurant._reviews = [review1, review2]
        self.assertEqual(restaurant.customers(), ["Customeresther", "Customer damola"])

    def test_average_star_rating(self):
        restaurant = Restaurant("Test Restaurant")
        review1 = Review("Customer esther", 4)
        review2 = Review("Customer damola", 5)
        restaurant._reviews = [review1, review2]
        self.assertEqual(restaurant.average_star_rating(), 4.5)

class TestReview(unittest.TestCase):

    def test_customer(self):
        review = Review("Customer esther", 4)
        self.assertEqual(review.customer(), "Customer esther")

    def test_star_rating(self):
        review = Review("Customer esther", 4)
        self.assertEqual(review.star_rating(), 4)

if __name__ == '__main__':
    unittest.main() 