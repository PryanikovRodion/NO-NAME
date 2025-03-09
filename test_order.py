import unittest
from order import Order
from saler import Saler
from buyer import Buyer
from product import Product

class TestOrder(unittest.TestCase):
    def setUp(self):
        Saler.names.clear()
        self.product = Product("Laptop", 1000.0, 10)
        self.saler = Saler("TechStore", 5000.0, self.product)
        self.buyer = Buyer("Alice", "123 Main St", 3000.0)
        self.order = Order(self.saler, self.product, 2, self.buyer)
    
    def test_valid_order_creation(self):
        self.assertEqual(self.order._Order__saler, self.saler)
        self.assertEqual(self.order._Order__product, self.product)
        self.assertEqual(self.order._Order__product_count, 2)
        self.assertEqual(self.order._Order__buyer, self.buyer)
    
    def test_invalid_saler_type(self):
        with self.assertRaises(TypeError):
            Order("NotASaler", self.product, 2, self.buyer)
    
    def test_invalid_product_type(self):
        with self.assertRaises(TypeError):
            Order(self.saler, "NotAProduct", 2, self.buyer)
    
    def test_invalid_product_count_type(self):
        with self.assertRaises(TypeError):
            Order(self.saler, self.product, "2", self.buyer)
    
    def test_invalid_buyer_type(self):
        with self.assertRaises(TypeError):
            Order(self.saler, self.product, 2, "NotABuyer")
    
    def test_repr(self):
        repr_str = repr(self.order)
        self.assertIn("Order:", repr_str)
        self.assertIn("Product name:Laptop", repr_str)
        self.assertIn("Count of Product:2", repr_str)
        self.assertIn("Saler:TechStore", repr_str)
        self.assertIn("Buyer:Alice", repr_str)
        self.assertIn("Buyer adress:123 Main St", repr_str)

if __name__ == "__main__":
    unittest.main()