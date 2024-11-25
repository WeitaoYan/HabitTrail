import httpx
import json

task_list = []


def post_task():
    url = "http://127.0.0.1:8000/api/activities/"
    data = [
        {
            "name": "预留项",
            "content": "预留项",
            "score": 0,
        },
        {
            "name": "独立完成作业",
            "content": "放学后回家自觉独立完成作业，家长到家只需要检查签字，包含家长布置作业。",
            "score": 10,
        },
        {
            "name": "按时吃饭不拖沓",
            "content": "上学时早晚饭，周末三餐不拖沓。饭做好立即吃，每次2分。",
            "score": 2,
        },
        {
            "name": "围棋对弈",
            "content": "新博少儿围棋对弈平台，对战超过120手，或者对手认输。战胜高一级对手额外再得10分。",
            "score": 10,
        },
        {
            "name": "火花思维",
            "content": "火花思维课堂纪律良好，上课时间全程坐在电脑前，不做小动作，不吃东西。",
            "score": 5,
        },
        {
            "name": "环球英语阅读",
            "content": "每本1分，每天5本。",
            "score": 5,
        },
        {
            "name": "看投影",
            "content": "10分钟一个单位，周末1：1，平时1：8",
            "score": -10,
        },
        {
            "name": "玩游戏",
            "content": "10分钟一个单位，周末1：3，平时1：20",
            "score": -30,
        },
        {
            "name": "买玩具",
            "content": "家长同意买的玩具，可以用积分兑换。每分抵1元。家长不同意的每10分抵1元。",
            "score": -10,
        },
    ]
    headers = {"Content-Type": "application/json"}
    for item in data:
        resp = httpx.post(url, json=item, headers=headers)
    print(resp.json())


if __name__ == "__main__":
    post_task()
