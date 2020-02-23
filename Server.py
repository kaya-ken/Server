#!/usr/bin/env python3

import socket
import os
import SlackAPI
import json

import UserInfo
from PurchaseHistoryLogger import PurchaseHistoryLogger


if __name__ == '__main__':
    user2id = {}
    slack_token = os.getenv('SLACK_TOKEN')
    logger = PurchaseHistoryLogger()

    proxy = 'MY_PROXY'
    slackClient = SlackAPI.SlackClient(slack_token, proxy)
    # channels = slackClient.list_up_channels()
    # users = slackClient.list_up_users()

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

    decoded_team = UserInfo.ReceivedData(**json.loads(json_data))
    logger.log_purchase(decoded_team)
    logger.debug()

