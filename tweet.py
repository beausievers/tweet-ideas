"""Tweet stimulator."""

import random


def tweet_ideas(config_path, n=1):
    """Return n tweet topics from config_path."""
    with open(config_path, 'r') as config:
        topics = config.readlines()
    selected_topics = [random.choice(topics) for _ in xrange(n)]
    print("You could tweet about...")
    for topic in selected_topics:
        print_topic(topic)


def print_topic(topic):
    """Print a single tweet idea."""
    print("    ..." + topic.strip())
