#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Auther: @kumata0x (twitter)
@Date: 2022/5/5 20:20
"""

import re, requests, json, random, time

def testContext():
    context_list = [
    "gm fams!",
    "hello bro",
    "LLLFG guys",
    "gmgm!",
    "hi all",
    "have a good day",
    "hello everyone",
    ]
    text = random.choice(context_list)
    return text


def startChat(channalId, auth):
    header = {
        "Authorization": auth,
        "Content-Type":"application/json",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }
    print("auth-id: "+ auth, "channal-id: "+ channalId)
    time.sleep(10)
    msg = {
        "content": testContext(),
        "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
        "tts": False
    }
    print(msg)
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channalId)

    try:
        res = requests.post(url=url, headers=header, data=json.dumps(msg))
        print(res)

    except:
        pass

    time.sleep(random.randrange(30,50))


if __name__ == '__main__':
    while True:
        try:
            # 1. 获取channalID
            channalId = "963272583875264625"
            # 2. 获取用户authID
            auth = "OTU3OTk1NjQwMjQyMTkyNDA1.YnPUXQ._RNa7RgUwQd8U63p1KQ-uv_a5Qw"
            startChat(channalId, auth)
            sleeptime = random.randrange(120, 180)
            time.sleep(sleeptime)
        except:
            break
        continue
