import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_explosiveness(self):
        """ Test default explosivenenss"""
        prod = Product('Test Product')
        self.assertLess(prod.flammability, 10)

    def test_default_stealability(self):
        """test default stealability"""
        prod = Product('Test Product')
        self.assertLessEqual(prod.stealability, .05)

class AcmeReportTest(unittest.TestCase):


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
# is going to.
