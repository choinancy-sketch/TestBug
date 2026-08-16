class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount = 0

    def add_item(self, name, price, quantity=1):
        """Add item to cart"""
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        # Check if item already exists
        for item in self.items:
            if item['name'] == name:
                item['quantity'] += quantity
                return

        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    def remove_item(self, name):
        """Remove item from cart"""
        original_length = len(self.items)
        self.items = [item for item in self.items if item['name'] != name]
        if len(self.items) == original_length:
            raise ValueError(f"Item '{name}' not found in cart")

    def get_total(self):
        """Calculate total with discount"""
        subtotal = sum(item['price'] * item['quantity'] for item in self.items)
        if self.discount < 0 or self.discount > 100:
            raise ValueError("Discount must be between 0 and 100")
        discount_amount = subtotal * (self.discount / 100)
        return round(subtotal - discount_amount, 2)

    def apply_discount(self, percentage):
        """Apply discount percentage"""
        if percentage < 0 or percentage > 100:
            raise ValueError("Discount must be between 0 and 100")
        self.discount = percentage

    def get_item_count(self):
        """Get total number of items"""
        return sum(item['quantity'] for item in self.items)

    def clear(self):
        """Empty the cart"""
        self.items = []
        self.discount = 0
