import requests
import csv
import operator

field_names = ["label", "url", "calories"]

def recipe_search(ingredient, meal_choice, max_cals):
        app_id = 'f718d00c'
        app_key = '2491806462d45a75519e4418ce425121'
        result = requests.get(f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}&calories{max_cals}&mealType={meal_choice}')
        data = result.json()
        return data['hits']


def run():
    print("Welcome to the Recipe Finder! Let us know your main ingredient, your meal, and your results will show in order of how calorific (and yummy) they are!")
    ingredient = input("What's your main ingredient? ")
    meal_choice = input("What type of meal do you want to cook? Breakfast/Lunch/Dinner? ")
    max_cals = input("Whats the maximum number of calories you want for the meal? ")

    results = recipe_search(ingredient, meal_choice, max_cals)
    newList =[]
    for result in results:
        if result['recipe']['calories'] <= int(max_cals):
            newList.append({'label': result['recipe']['label'], 'url': result['recipe']['url'], 'calories': result['recipe']['calories']})
        newList.sort(key=operator.itemgetter('calories'))
    return newList

data = run()

with open("recipeList.csv", "w+") as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames= field_names)
    spreadsheet.writerows(data)
