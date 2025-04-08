import unittest
from source.buyer import Buyer 

class TestBuyer(unittest.TestCase):
    def test_valid_buyer_creation(self):
        buyer = Buyer("Alice", "123 Main St", 100.0)
        self.assertEqual(buyer.name, "Alice")
        self.assertEqual(buyer.adress, "123 Main St")
        self.assertEqual(buyer.money, 100.0)

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            Buyer(123, "123 Main St", 100.0)

    def test_invalid_adress_type(self):
        with self.assertRaises(TypeError):
            Buyer("Alice", 123, 100.0)

    def test_invalid_money_type(self):
        with self.assertRaises(TypeError):
            Buyer("Alice", "123 Main St", "100.0")

    def test_setter_valid_name(self):
        buyer = Buyer("Alice", "123 Main St", 100.0)
        buyer.name = "Bob"
        self.assertEqual(buyer.name, "Bob")

    def test_setter_invalid_name(self):
        buyer = Buyer("Alice", "123 Main St", 100.0)
        with self.assertRaises(TypeError):
            buyer.name = 456

    def test_setter_valid_adress(self):
        buyer = Buyer("Alice", "123 Main St", 100.0)
        buyer.adress = "456 Elm St"
        self.assertEqual(buyer.adress, "456 Elm St")

    def test_setter_invalid_adress(self):
        buyer = Buyer("Alice", "123 Main St", 100.0)
        with self.assertRaises(TypeError):
            buyer.adress = 789

    def test_setter_valid_money(self):
        buyer = Buyer("Alice", "123 Main St", 100.0)
        buyer.money = 200.0
        self.assertEqual(buyer.money, 200.0)

    def test_setter_invalid_money_type(self):
        buyer = Buyer("Alice", "123 Main St", 100.0)
        with self.assertRaises(TypeError):
            buyer.money = "300"

    def test_setter_negative_money(self):
        buyer = Buyer("Alice", "123 Main St", 100.0)
        with self.assertRaises(ValueError):
            buyer.money = -50.0

    def test_repr(self):
        buyer = Buyer("Alice", "123 Main St", 100.0)
        expected_repr = "Buyer:Alice\nMoneys:100.0$\nAdress:123 Main St \n"
        self.assertEqual(repr(buyer), expected_repr)

if __name__ == "__main__":
    unittest.main()
