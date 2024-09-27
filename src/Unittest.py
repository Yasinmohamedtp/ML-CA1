import unittest
import pandas as pd

# Mock InventoryManager class for testing
class InventoryManager:
    def __init__(self):
        self.inventory = pd.read_csv('inventory_dataset_100.csv')

    def add_item(self, item_id, item_name, category, stock_quantity, price):
        new_item = pd.DataFrame([[item_id, item_name, category, stock_quantity, price]], 
                                columns=['Item_ID', 'Item_Name', 'Category', 'Stock_Quantity', 'Price'])
        self.inventory = pd.concat([self.inventory, new_item], ignore_index=True)

    def remove_item(self, item_id):
        self.inventory = self.inventory[self.inventory['Item_ID'] != item_id]

    def update_stock(self, item_id, stock_quantity):
        self.inventory.loc[self.inventory['Item_ID'] == item_id, 'Stock_Quantity'] = stock_quantity

    def low_stock_report(self, threshold=20):
        return self.inventory[self.inventory['Stock_Quantity'] < threshold]

    def display_inventory(self):
        print(self.inventory)

# Unit test cases
class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        self.manager = InventoryManager()

    def test_add_item(self):
        # Adding a new item
        self.manager.add_item(101, 'TestItem', 'TestCategory', 15, 1500)
        item = self.manager.inventory[self.manager.inventory['Item_ID'] == 101]
        self.assertEqual(len(item), 1)
        self.assertEqual(item['Item_Name'].values[0], 'TestItem')

    def test_remove_item(self):
        # Removing an existing item
        self.manager.remove_item(1)  # Remove item with Item_ID = 1
        item = self.manager.inventory[self.manager.inventory['Item_ID'] == 1]
        self.assertEqual(len(item), 0)

    def test_update_stock(self):
        # Updating stock quantity
        self.manager.update_stock(1, 300)
        updated_stock = self.manager.inventory[self.manager.inventory['Item_ID'] == 1]['Stock_Quantity'].values[0]
        self.assertEqual(updated_stock, 300)

    def test_low_stock_report(self):
        # Testing low stock report generation
        low_stock_items = self.manager.low_stock_report(threshold=20)
        self.assertTrue(all(low_stock_items['Stock_Quantity'] < 20))
        self.assertGreaterEqual(len(low_stock_items), 1)

if __name__ == '__main__':
    unittest.main()
