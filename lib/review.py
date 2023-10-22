class Review:
    
    reviews = []
    
    def __init__(self, customer, restaurant, rating):
        # - Reviews should be initialized with a customer, restaurant, and a rating (a number)
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.reviews.append(self)
    
    @property
    def rating(self):
        # returns the rating for a restaurant
        return self._rating
    
    @classmethod
    def all(cls):
        # returns all of the reviews
        return cls.reviews
    
    # object relationship
    
    @property
    def customer(self):
        # returns the customer object for that review
        # Once a review is created, should not be able to change the customer
        return self._customer
    
    @property
    def restaurant(self):
        # returns the restaurant object for that given review
        # Once a review is created, should not be able to change the restaurant
        return self._restaurant