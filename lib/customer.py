from review import Review

class Customer:
    
    customers = []
    
    def __init__(self, first_name, last_name):
        # Customer should be initialized with a given name and family name, both strings (i.e., first and last name, like George Washington)"
        self._given_name = first_name
        self._family_name = last_name
        Customer.customers.append(self)
    
    @property
    def given_name(self):
        print('test')
        # returns the customer's given name
        # should be able to change after the customer is created
        return self._given_name
    
    @given_name.setter
    def given_name(self, given_name):
        self._given_name = given_name
    
    @property
    def family_name(self):
        # returns the customer's family name
        # should be able to change after the customer is created
        return self._family_name
    
    @family_name.setter
    def family_name(self, family_name):
        self._family_name = family_name
    
    def full_name(self):
        # returns the full name of the customer, with the given name and the family name concatenated, Western style
        return f'{self._given_name} {self._family_name}'
    
    @classmethod
    def all(cls):
        # returns **all** of the customer instances
        return cls.customers
    
    # object relationship
    
    def restaurants(self):
        # Returns a **unique** list of all restaurants a customer has reviewed
        return list({review.restaurant for review in Review.reviews if review.customer.full_name == self.full_name})
    
    def add_review(self, restaurant, rating):
        #  given a **restaurant object** and a star rating (as an integer), creates a new review and associates it with that customer and restaurant.
        Review(self, restaurant=restaurant, rating=rating)
    
    # aggregate and association
    
    def num_reviews(self):
        # Returns the total number of reviews that a customer has authored
        return len([review for review in Review.reviews if review.customer.full_name == self.full_name])
    
    @classmethod
    def find_by_name(cls, name):
        # given a string of a **full name**, returns the **first customer** whose full name matches
        for customer in cls.customers:
            if customer.full_name == name:
                return customer
    
    @classmethod
    def find_all_by_given_name(cls, name):
        # given a string of a given name, returns an **list** containing all customers with that given name
        return [customer.given_name for customer in cls.customers if customer.given_name == name]