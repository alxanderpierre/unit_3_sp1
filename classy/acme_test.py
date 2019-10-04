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
