class Restaurant:
    def __init__(self, name):
# Intializing the Restaurant object with a name and empty list of reviews 
        self._name = name
        self._reviews = []

    def name(self):
# Return the name of the restaurant
        return self._name

    def reviews(self):
# Return the list of reviews for the restaurant
        return self._reviews

    def customers(self):
# Creating an empty list to store special customers
        customers = []

# Iterate through a list of review for each review
        for review in self._reviews:
# Find the customer from review 
            customer = review.customer()

# Search if the customer is aleady in the list of customers
            if customer not in customers:
                # If not, add the customer to the list
                customers.append(customer)

        # Return the list of unique customers
        return customers

    def average_star_rating(self):
        # Initialize a variable to store the total rating
        total_rating = 0

        # Iterate through each review in the reviews list
        for review in self._reviews:
            # Add the star rating of the review to the total rating
            total_rating += review.star_rating()

        # Check if there are any reviews
        if len(self._reviews) > 0:
            # If there are, calculate and return the average star rating
            return total_rating / len(self._reviews)
        else:
            # If there are no reviews, return 0
            return 0


class Review:
    def __init__(self, customer, star_rating):
        # Initialize the Review object with a customer and a star rating
        self._customer = customer
        self._star_rating = star_rating

    def customer(self):
        # Return the customer of the review
        return self._customer

    def star_rating(self):
        # Return the star rating of the review
        return self._star_rating


