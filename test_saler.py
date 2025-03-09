import unittest
from saler import Saler
from product import Product

class TestSaler(unittest.TestCase):
    def setUp(self):
        Saler.names.clear()
        self.product1 = Product("Laptop", 1000.0, 10)
        self.product2 = Product("Phone", 500.0, 20)
        self.saler = Saler("TechStore0", 1000.0, self.product1, self.product2)
    
    def test_valid_saler_creation(self):
        self.assertEqual(self.saler.name, "TechStore0")
        self.assertEqual(self.saler.money, 1000.0)
        self.assertIn("Laptop", self.saler.products)
        self.assertIn("Phone", self.saler.products)
    
    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            Saler(123, 1000.0, self.product1)
    
    def test_invalid_money_type(self):
        with self.assertRaises(TypeError):
            Saler("TechStore1", "1000", self.product1)
    
    def test_negative_money(self):
        with self.assertRaises(ValueError):
            Saler("TechStore2", -500, self.product1)
    
    def test_invalid_products_type(self):
        with self.assertRaises(TypeError):
            Saler("TechStore3", 1000.0, "NotAProduct")
    
    def test_unique_saler_name(self):
        with self.assertRaises(ValueError):
            Saler("TechStore0", 500.0, self.product2)
    
    def test_setter_valid_money(self):
        self.saler.money = 2000.0
        self.assertEqual(self.saler.money, 2000.0)
    
    def test_setter_invalid_money_type(self):
        with self.assertRaises(TypeError):
            self.saler.money = "3000"
    
    def test_setter_negative_money(self):
        with self.assertRaises(ValueError):
            self.saler.money = -100
    
    def test_setter_valid_products(self):
        new_product = Product("Tablet", 700.0, 15)
        self.saler.products = new_product
        self.assertIn("Tablet", self.saler.products)
    
    def test_setter_invalid_products(self):
        with self.assertRaises(TypeError):
            self.saler.products = "NotAProduct"
    
    def test_repr(self):
        repr_str = repr(self.saler)
        self.assertIn("Saler: TechStore0", repr_str)
        self.assertIn("Laptop", repr_str)
        self.assertIn("Phone", repr_str)

if __name__ == "__main__":
    unittest.main()


