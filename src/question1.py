class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_item(self, item_id, item_name, category, stock_quantity, price):
        item = {
            'Item_ID': item_id,
            'Item_Name': item_name,
            'Category': category,
            'Stock_Quantity': stock_quantity,
            'Price': price
        }
        self.inventory.append(item)

    def update_stock(self, item_id, stock_quantity):
        for item in self.inventory:
            if item['Item_ID'] == item_id:
                item['Stock_Quantity'] = stock_quantity
                return f"Stock updated for Item_ID: {item_id}"
        return "Item not found!"

    def remove_item(self, item_id):
        self.inventory = [item for item in self.inventory if item['Item_ID'] != item_id]

    def display_inventory(self):
        for item in self.inventory:
            print(item)
