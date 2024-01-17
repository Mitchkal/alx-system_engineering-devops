#!/usr/bin/python3
"""module hot """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """recursively querries Reddit API abd returns hot posts"""

    if not hot_list:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json?".format(subreddit)

    headers = {
        'User-Agent': 'My User Agent 5.0'}
    params = {
            'after': after
            }
    try:
        response = requests.get(url, params=params, headers=headers,
                                allow_redirects=False)
        data = response.json()['data']['children']
        if not data:
            return hot_list

        hot_list.extend(item['data']['title'] for item in data)

        after = data[-1]['data']['name']

        if not after:
            return hot_list

        return (hot_list + recurse(subreddit, hot_list=hot_list, after=after))
    except Exception as e:
        return (None)
