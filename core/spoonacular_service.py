import requests

SPOONACULAR_API_KEY = 'your_api_key_here'
BASE_URL = 'https://api.spoonacular.com/recipes'

def get_recipes_by_ingredients(ingredients):
    url = f"{BASE_URL}/findByIngredients"
    params = {
        'apiKey': SPOONACULAR_API_KEY,
        'ingredients': ','.join(ingredients),
        'number': 10
    }
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else []
