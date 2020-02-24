import datetime
import sqlite3


class PurchaseHistoryLogger(object):
    def log_purchase(self, _user_info):
        dt_now = datetime.datetime.now()
        str_time = dt_now.strftime('%Y/%m/%d %H:%M:%S')

        connection = sqlite3.connect('purchase_history_db.sqlite3')
        c = connection.cursor()

        try:
            c.execute("INSERT INTO purchase_history VALUES (? , ?, ?)",
                              (_user_info.slack_id, _user_info.product_id, str_time))
        except sqlite3.Error as e:
            print('sqlite3 error:', e.args[0])

        connection.commit()
        connection.close()
