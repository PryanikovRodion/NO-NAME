import unittest
from source.saler import Saler
from source.buyer import Buyer
from source.product import Product
from source.magazin import Magazin

class TestProduct(unittest.TestCase):
    def test_valid_product_creation(self):
        product = Product("Laptop", 1000.0, 5)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 1000.0)
        self.assertEqual(product.count, 5)

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            Product(123, 1000.0, 5)

    def test_invalid_price_type(self):
        with self.assertRaises(TypeError):
            Product("Laptop", "1000", 5)

    def test_invalid_count_type(self):
        with self.assertRaises(TypeError):
            Product("Laptop", 1000.0, "5")

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            Product("Laptop", -1000.0, 5)
    
    def test_zero_price(self):
        with self.assertRaises(ValueError):
            Product("Laptop", 0, 5)

    def test_negative_count(self):
        with self.assertRaises(ValueError):
            Product("Laptop", 1000.0, -5)

    def test_setter_valid_name(self):
        product = Product("Laptop", 1000.0, 5)
        product.name = "Tablet"
        self.assertEqual(product.name, "Tablet")

    def test_setter_invalid_name(self):
        product = Product("Laptop", 1000.0, 5)
        with self.assertRaises(TypeError):
            product.name = 123

    def test_setter_valid_price(self):
        product = Product("Laptop", 1000.0, 5)
        product.price = 1500.0
        self.assertEqual(product.price, 1500.0)

    def test_setter_invalid_price(self):
        product = Product("Laptop", 1000.0, 5)
        with self.assertRaises(TypeError):
            product.price = "2000"

    def test_setter_negative_price(self):
        product = Product("Laptop", 1000.0, 5)
        with self.assertRaises(ValueError):
            product.price = -500

    def test_setter_zero_price(self):
        product = Product("Laptop", 1000.0, 5)
        with self.assertRaises(ValueError):
            product.price = 0

    def test_setter_valid_count(self):
        product = Product("Laptop", 1000.0, 5)
        product.count = 10
        self.assertEqual(product.count, 10)

    def test_setter_invalid_count(self):
        product = Product("Laptop", 1000.0, 5)
        with self.assertRaises(TypeError):
            product.count = "10"

    def test_setter_negative_count(self):
        product = Product("Laptop", 1000.0, 5)
        with self.assertRaises(ValueError):
            product.count = -1

    def test_repr(self):
        product = Product("Laptop", 1000.0, 5)
        self.assertEqual(repr(product), "|Laptop|1000.0$|5|")
  

if __name__ == "__main__":
    unittest.main()

        
        




