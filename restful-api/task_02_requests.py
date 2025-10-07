#!/usr/bin/env python3
"""
this module define two function for learn requests
"""
import requests
import csv


def fetch_and_print_posts():
    """
    fetches all post from JSONPlaceholder
    """
    JSON = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(JSON.status_code))

    if JSON.status_code == 200:
        data = JSON.json()
        for t in data:
            print(t["title"])


def fetch_and_save_posts():
    """
    fetches all post from JSONPlaceholder.
    """
    JSON = requests.get("https://jsonplaceholder.typicode.com/posts")

    if JSON.status_code == 200:
        data = JSON.json()

        data_list = [{"id": p["id"], "title": p["title"],
                      "body": p["body"]} for p in data]

        with open("posts.csv", "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data_list)
