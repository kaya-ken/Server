import pandas as pd
import datetime


class PurchaseHistoryLogger(object):
    def __init__(self):
        self.purchase_history_df = pd.DataFrame(columns=['UserID', 'ProductID', 'PurchaseDate'])

    def update_purchase_history(self, _user_info):
        dt_now = datetime.datetime.now()
        str_time = dt_now.strftime('%Y/%m/%d %H:%M:%S')
        tmp_series = pd.Series([_user_info.slack_id, _user_info.product_id, str_time],
                               index=self.purchase_history_df.columns)
        self.purchase_history_df = self.purchase_history_df.append(tmp_series, ignore_index=True)

    def debug(self):
        print(self.purchase_history_df.head())
