from lib.review import Review

class Restaurant:
    def __init__(self, name):
        # Restaurants should be initialized with a name, as a string
        self._name = name
    
    @property
    def name(self):
        # returns the restaurant's name
        # should not be able to change after the restaurant is created
        return self._name
    
    # object relationship
    
    def reviews(self):
        # returns a list of all reviews for that restaurant
        return [review for review in Review.reviews if review.restaurant.name == self._name]
    
    def customers(self):
        # - Returns a **unique** list of all customers who have reviewed a particular restaurant
        return list({review.customer for review in Review.reviews if review.restaurant.name == self._name})
    
    # Aggregate and Association Methods
    
    def average_star_rating(self):
        # returns the average star rating for a restaurant based on its reviews
        # Reminder: you can calculate the average by adding up all the ratings and dividing by the number of ratings
        rating_sum = 0
        for review in Review.reviews:
            if review.restaurant.name == self._name:
                rating_sum += review.rating
        return (rating_sum / len(Review.reviews))