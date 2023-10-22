from .Review import Review

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
# Initialize the Customer object with a given name and a family name
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def given_name(self):
# Return the given name of the customer
        return self.given_name

    def family_name(self):
# Return the family name of the customer
        return self.family_name

    def full_name(self):
# Return the full name of the customer by concatenating the given name and the family name
        return self.given_name + " " + self.family_name

    @classmethod
    def all(cls):
# Return a list of all customers
        return cls.all_customers

    def restaurants(self):
# Create an empty list to store reviewed restaurants
        reviewed_restaurants = []

# Iterate through each review in the list of all reviews
        for review in Review.all():
# Check if the customer of the review is the current customer
            if review.customer == self:
    # If yes, add the restaurant of the review to the list of reviewed restaurants
                reviewed_restaurants.append(review.restaurant)

    # Return a list of unique reviewed restaurants
        return list(set(reviewed_restaurants))

    def add_review(self, restaurant, rating):
        # Create a new review object with the current customer, the given restaurant, and the given rating
        Review(self, restaurant, rating)

    def num_reviews(self):
        # Initialize a count variable to store the number of reviews
        count = 0

        # Iterate through each review in the list of all reviews
        for review in Review.all():
            # Check if the customer of the review is the current customer
            if review.customer == self:
                # If yes, increment the count variable
                count += 1

        # Return the count of reviews
        return count

    @classmethod
    def find_by_name(cls, name):
        # Iterate through each customer in the list of all customers
        for customer in cls.all_customers:
            # Check if the full name of the customer matches the given name
            if customer.full_name() == name:
                # If yes, return the customer
                return customer

        # If no customer is found, return None
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        # Create an empty list to store customers with the given name
        customers_with_given_name = []

        # Iterate through each customer in the list of all customers
        for customer in cls.all_customers:
            # Check if the given name of the customer matches the given name
            if customer.given_name == name:
                # If yes, add the customer to the list of customers with the given name
                customers_with_given_name.append(customer)

        # Return the list of customers with the given name
        return customers_with_given_name