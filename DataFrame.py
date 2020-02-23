import pandas as pd


class DataFrame():
    purchase_history_df = pd.DataFrame(columns=['UserID', 'ProductID', 'PurchaseDate'])
    product_info_df = pd.DataFrame(columns=['ProductID', 'ProductName', 'Price'])
