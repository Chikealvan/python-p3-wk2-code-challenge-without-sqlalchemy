class Review:
    # Create a class variable to store all reviews
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        # Initialize the Review object with a customer, restaurant, and rating
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        # Return the rating of the review
        return self.rating

    @classmethod
    def all(cls):
        # Return a list of all reviews
        return cls.all_reviews

    def customer(self):
        # Return the customer of the review
        return self.customer

    def restaurant(self):
        # Return the restaurant of the review
        return self.restaurant