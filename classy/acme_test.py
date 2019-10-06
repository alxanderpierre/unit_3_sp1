import unittest
from acme import Product
from acme_report import generate_products, adjective, noun
import random

adjective = random.sample(['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved'], 1)
noun = random.sample(['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Hangers'], 1)
name = adjective[0] + " " + noun[0]


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_defaults(self):
        """Test Default values as shown"""
        prod=Product("Test Product")
        self.assertEqual(prod.flammability, 0.5)
        self.assertEqual(prod.weight, 20.0)
        self.assertEqual(prod.name, "Test prod")

    def test_stealability(self):
        """test stealability"""
        prod = generate_products(name,flammability,price,weight,num_products= 4)
        steal = ["Not so stealable.", "kinda stealable.", "Very stealable."]
        for x in prod:
            stealability = x.stealability()
            self.assertIn(stealability, steal)

class AcmeReportTest(unittest.TestCase):

    def test_legal_name(self):
        prod = generate_products(name,flammability, price, weight, num_products=1)
        self.assertIn(prod[0].name, name)

    def test_default_num_products(self):
        prod=generate_products(name, flammability, price, weight)
        self.assertEqual(len(prod), 30)

if __name__ == '__main__':
    unittest.main()

# What, in your opinion, is an important part of code reviews? That is, what is
#  something you pay attention to when you review code, and that you appreciate
#  when others do the same for your code?

# ANSWER: One thing that is very important to code review and something
# that i appreciate is when others show me how to make my code more DRY and less
# WET. Its important to have dry code because it important to repeat yourself
# too many time. Code is meant to be shared. If you have
# wet code it makes it harder for other to read and interpret your code.

# We have an awful lot of computers here, and it gets pretty confusing with
#  slightly different things running on all of them. How could containers help us
#  improve this situation?

# ANSWER: Containers can be very very very useful in situations like these. Using
# applications like docker allows a person to share their code with other and
# it will automatically import the correct dependencies based on the machine it
# is going
