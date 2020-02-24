import SlackAPI
import os
import sqlite3


if __name__ == '__main__':
    slack_token = ''
    #os.getenv('SLACK_TOKEN')
    proxy = 'MY_PROXY'
    slackClient = SlackAPI.SlackClient(slack_token)#, proxy)
    users = slackClient.list_up_users()

    id_table = {}
    for user_info in users:
        if not user_info['deleted']:
            id_table[user_info['name']] = user_info['id']

    print(id_table)
