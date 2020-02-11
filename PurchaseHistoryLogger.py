import pandas as pd
import datetime

from DataFrame import DataFrame


class PurchaseHistoryLogger(object):
    def log_purchase(self, _user_info):
        dt_now = datetime.datetime.now()
        str_time = dt_now.strftime('%Y/%m/%d %H:%M:%S')
        tmp_series = pd.Series([_user_info.slack_id, _user_info.product_id, str_time],
                               index=DataFrame.purchase_history_df.columns)
        DataFrame.purchase_history_df = DataFrame.purchase_history_df \
            .append(tmp_series, ignore_index=True)

    def debug(self):
        print(DataFrame.purchase_history_df.head())
