import re

def extract_topics(text):

    lines = text.split("\n")

    topics = []

    for line in lines:

        line = line.strip()

        if len(line) > 3 and "unit" not in line.lower():
            topics.append(line)

    return topics