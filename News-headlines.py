# News headline Script
# This script Extracts News Headlines from API responses.

import re


api_response = [
    "Breaking News: Major Earthquake Strikes City.",
    "Sports Update: Team Wins Championship Game!",
    "Technology News: New Iphone 15 Smartphone Released",
    "Entertainment Buzz: Actor Wins Award",
]


headlines = []

pattern = r"^(.*?): (.*?)$"

for response in api_response:
    match = re.match(pattern, response)
    if match:
        headline = match.group(1)
        subheader = match.group(2)
        headlines.append({"headline": headline, "subheader": subheader})


for headline in headlines:
    print(f"Headline: {headline['headline']}")
    print(f"Subheader: {headline['subheader']}")
    print("\n")


