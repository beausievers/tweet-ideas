"""Tweet stimulator."""

import random


def lines_from_file(path, n=1):
    """Return n lines from file at path."""
    with open(path, 'r') as f:
        topics = f.readlines()
    lines = [random.choice(topics) for _ in range(n)]
    return lines


def tweet_ideas(config_path, n=1):
    """Return n tweet topics from config_path."""
    selected_topics = lines_from_file(config_path, n)
    print("You could tweet...")
    for topic in selected_topics:
        print_topic(topic)


def fortune(fortune_path, n=1):
    """Return n fortunes from fortune_path."""
    fortunes = lines_from_file(fortune_path, n)
    print("Sound advice for quality tweets:")
    for fortune in fortunes:
        print_fortune(fortune)


def print_topic(topic):
    """Print a single tweet idea."""
    print("    ..." + topic.strip())


def print_fortune(fortune):
    """Print a single fortune."""
    print(fortune)


if __name__ == '__main__':
    print(' ')
    tweet_ideas('topics.txt', n=1)
    print(' ')
    fortune('fortunes.txt', n=1)
