# Restaurant Extraction Script
# This script extracts restaurant names and cuisine types from API responses.

import re

# Define a regular expression pattern for restaurant names and cuisines
restaurant_pattern = r'(.+?) - (.+?)'

# Sample API response containing restaurant information
api_response = "Welcome to Jean Paul's Dish - Rwanda's Cuisine. Enjoy our delicious potato dishes!"

# Extract restaurant names and cuisine types using regex

# Use the findall() method to extract matches
matches = re.findall(restaurant_pattern, api_response)

# Iterate over matches and print restaurant names and cuisines
for match in matches:
    restaurant_name, cuisine_type = match
    print(f"Restaurant Name: {restaurant_name.strip()}")
    print(f"Cuisine Type: {cuisine_type.strip()}")

# Usage: Run this script with a sample API response to extract restaurant information.
# Replace the 'api_response' variable with your own data.

# Author: Rohaenat Mustapha
# Date: 0ctober 4

# Note: This script assumes that the restaurant names and cuisine types
# follow the "Name - Cuisine" pattern. It may not handle all variations.