#!/usr/bin/python3
"""module top ten"""
import requests


def top_ten(subreddit):
    """querries Reddit API abd returns top ten posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {
        'User-Agent': 'My User Agent 5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()['data']
        top = (data['children'])
        for item in top[:10]:
            print(item['data']['title'])
    except Exception as e:
        print("None")
