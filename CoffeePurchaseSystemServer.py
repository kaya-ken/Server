#!/usr/bin/env python3

import socket
import json
import sqlite3

import UserInfo
from PurchaseHistoryLogger import PurchaseHistoryLogger


# カラムを知るとき
# c.execute("PRAGMA TABLE_INFO(purchase_history)")
# print(c.fetchall())
def register_product(_product_id, _product_name, _price):
    connection = sqlite3.connect('purchase_history_db.sqlite3')
    c = connection.cursor()

    try:
        c.execute("INSERT INTO product VALUES (?, ?, ?)",
                  (_product_id, _product_name, _price))
    except sqlite3.Error as e:
        print('sqlite3 error:', e.args[0])

    connection.commit()
    connection.close()


if __name__ == '__main__':
    logger = PurchaseHistoryLogger()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 8084))

        print('listening...')
        s.listen(1)
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print('data : {}, addr: {}'.format(data, addr))
                    decoded_user_info = UserInfo.ReceivedData(**json.loads(data))
                    logger.log_purchase(decoded_user_info)
                    conn.sendall(b'Received: ' + data)
