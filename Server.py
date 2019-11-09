#!/usr/bin/env python3

import socket
import os
import SlackAPI


if __name__ == '__main__':
    user2id = {}
    # slack_token = os.getenv('SLACK_TOKEN')
    slack_token = ''

    proxy = 'http://lab-12:Slpl-201@proxy.doshisha.ac.jp:8080'
    slackClient = SlackAPI.SlackClient(slack_token, proxy)
    channels = slackClient.list_channels()
    users = slackClient.list_users()

    if users:
        for u in users:
            if not u['deleted']:
                user2id[u['name']] = u['id']
    else:
        print("Unable to authenticate.")

    # img = open('QR/岸田 優輝.png', 'rb')
    slackClient.send_message(user2id['ctwc0162'], 'Images/logo.png')
    slackClient.send_image(user2id['ctwc0162'], 'Images/logo.png')

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.bind(('0.0.0.0', 8084))
    #
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
