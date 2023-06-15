import requests

# API endpoint for recipe search
url = 'https://api.spoonacular.com/recipes/findByIngredients'

# API parameters
params = {
    'apiKey': '638a7c188b0d4915ab39070d29c0fc4e',
    'ingredients': 'apples,flour,sugar',
    'number': 5,
    'ranking': 2
}

# Make the GET request
response = requests.get(url, params=params)

# Get the JSON data from the response
data = response.json()

# Print the recipe information
for recipe in data:
    print(recipe['title'], recipe['id'])