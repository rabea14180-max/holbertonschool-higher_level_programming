#!/usr/bin/python3
"""
task_02_requests.py
Consuming and processing data from an API using Python
"""

import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print their titles
    """
    response = requests.get(URL)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # Check if request was successful
    if response.status_code == 200:
        posts = response.json()  # Parse JSON data

        # Iterate and print titles
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch posts and save selected fields to posts.csv
    """
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        # Prepare structured data
        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(structured_posts)
