#!/usr/bin/env python3

import socket
import os
import json
import sqlite3

import UserInfo
from PurchaseHistoryLogger import PurchaseHistoryLogger


if __name__ == '__main__':
    logger = PurchaseHistoryLogger()


    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.bind(('0.0.0.0', 8084))
    #
    #     print('listening...')
    #     s.listen(1)
    #     while True:
    #         conn, addr = s.accept()
    #         with conn:
    #             while True:
    #                 data = conn.recv(1024)
    #                 if not data:
    #                     break
    #                 print('data : {}, addr: {}'.format(data, addr))
    #                 conn.sendall(b'Received: ' + data)

    # ダミーデータ
    receivedUserInfo = UserInfo.ReceivedData(slack_id='ctwc0162', product_id='hOgEpRoDuCt')
    json_data = json.dumps(receivedUserInfo, default=lambda o: o.__dict__, indent=4)

    decoded_user_info = UserInfo.ReceivedData(**json.loads(json_data))
    logger.log_purchase(decoded_user_info)

    conn = sqlite3.connect('purchase_history_db.sqlite3')
    c = conn.cursor()
    c.execute('SELECT * FROM purchase_history')
    print(c.fetchone())
    c.execute('SELECT * FROM product')
    print(c.fetchone())
    conn.close()
