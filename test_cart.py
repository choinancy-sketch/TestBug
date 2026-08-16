import pytest
from cart import ShoppingCart

class TestShoppingCart:
    def setup_method(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Apple", 1.50, 3)
        assert len(self.cart.items) == 1
        assert self.cart.items[0]['name'] == "Apple"
        assert self.cart.items[0]['quantity'] == 3

    def test_add_duplicate_item_increases_quantity(self):
        self.cart.add_item("Apple", 1.50, 3)
        self.cart.add_item("Apple", 1.50, 2)
        assert len(self.cart.items) == 1
        assert self.cart.items[0]['quantity'] == 5

    def test_add_item_negative_price_raises_error(self):
        with pytest.raises(ValueError):
            self.cart.add_item("Bad Item", -5.00)

    def test_add_item_zero_quantity_raises_error(self):
        with pytest.raises(ValueError):
            self.cart.add_item("Bad Item", 5.00, 0)

    def test_remove_item(self):
        self.cart.add_item("Apple", 1.50)
        self.cart.remove_item("Apple")
        assert len(self.cart.items) == 0

    def test_remove_nonexistent_item_raises_error(self):
        with pytest.raises(ValueError, match="not found"):
            self.cart.remove_item("Ghost Item")

    def test_get_total_no_discount(self):
        self.cart.add_item("Apple", 2.00, 3)
        self.cart.add_item("Banana", 1.00, 2)
        assert self.cart.get_total() == 8.00

    def test_get_total_with_discount(self):
        self.cart.add_item("Apple", 10.00, 1)
        self.cart.apply_discount(20)  # 20% off
        assert self.cart.get_total() == 8.00

    def test_invalid_discount_raises_error(self):
        with pytest.raises(ValueError):
            self.cart.apply_discount(150)
        with pytest.raises(ValueError):
            self.cart.apply_discount(-10)

    def test_get_item_count(self):
        self.cart.add_item("Apple", 1.00, 3)
        self.cart.add_item("Banana", 0.50, 5)
        assert self.cart.get_item_count() == 8

    def test_clear_cart(self):
        self.cart.add_item("Apple", 1.00)
        self.cart.apply_discount(10)
        self.cart.clear()
        assert len(self.cart.items) == 0
        assert self.cart.discount == 0
        assert self.cart.get_total() == 0

    def test_empty_cart_total(self):
        assert self.cart.get_total() == 0
