import re

ingredient_pattern = r'([\w\s]+(?:,\s*[\w\s]+)*)'

api_response = "Ingredients: flour, sugar, butter, eggs, potato, chicken, curry, rice"

matches = re.findall(ingredient_pattern, api_response)

ingredient_lists = [match.split(', ') for match in matches]

for index, ingredients in enumerate(ingredient_lists, start=1):
    print(f"Ingredient List {index}:")
    for ingredient in ingredients:
        print(f" - {ingredient}")
