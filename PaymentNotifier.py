#!/usr/bin/env python3

import SlackAPI
import os
import sqlite3
import datetime


if __name__ == '__main__':
    slack_token = os.getenv('SLACK_TOKEN')
    proxy = 'MY_PROXY'
    slackClient = SlackAPI.SlackClient(slack_token, proxy)
    users = slackClient.list_up_users()

    # SlackIDとユーザIDの紐づけ
    id_table = {}
    for user_info in users:
        if not user_info['deleted']:
            id_table[user_info['name']] = user_info['id']

    conn = sqlite3.connect('purchase_history_db.sqlite3')
    c = conn.cursor()

    dt_now = datetime.datetime.now()
    str_time = dt_now.strftime('%Y-%m-%d %H:%M:%S')

    # 現在時刻から30日以内のユーザごとの合計金額を求めるためのクエリ
    c.execute("SELECT user_id, SUM(price) FROM purchase_history JOIN product ON purchase_history.product_id=product.product_id\
              WHERE datetime(?, '-30 days') < date", (str_time,))
    for record in c.fetchall():
        slack_id = id_table[record[0]]
        slackClient.send_message(slack_id, ':coffee: ネスカフェアンバサダーです :coffee:\n今月のコーヒー代は%d円です :+1: :+1: :+1:' %record[1])

    conn.close()
