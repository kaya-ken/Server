#!/usr/bin/env python3

import socket
import os
# from slackclient import SlackClient
import slack


def list_channels(arg_client):
    channels_call = arg_client.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None


def list_users(arg_client):
    users_call = arg_client.api_call("users.list")
    if users_call.get('ok'):
        return users_call['members']
    return None


def send_message(arg_client, arg_id, arg_message):
    arg_client.api_call(
        "chat.postMessage",
        channel=arg_id,
        text=arg_message)


def send_image(arg_client, arg_id, arg_image, arg_comment):
    arg_client.api_call(
        "files.upload",
        channels=arg_id,
        file=arg_image,
        initial_comment=arg_comment
    )


if __name__ == '__main__':
    user2id = {}
    # slack_token = os.getenv('SLACK_TOKEN')
    slack_token = 'xoxp-367271599569-367715687027-828095310005-0ee6552a383ce30dbb262f0237c87af0'

    client_proxy = 'http://lab-12:Slpl-201@proxy.doshisha.ac.jp:8080'
    client = slack.WebClient(token=slack_token, proxy=client_proxy)
    channels = list_channels(client)
    users = list_users(client)

    if users:
        for u in users:
            if not u['deleted']:
                user2id[u['name']] = u['id']
            else:
                print(u['name'])
    else:
        print("Unable to authenticate.")

    # img = open('QR/岸田 優輝.png', 'rb')
    # send_image(client, user2id['bup0034'], img, 'QRコード')

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
