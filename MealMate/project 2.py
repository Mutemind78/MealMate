
#Welcome to MEAL MATE this will help you to generate your meal and its grocery list on the basis of your dietery preferences 

#importing necessary libraries 
import random
import os
import openpyxl

#using dictionary named recipes which contains lists dictionary is owing to too many list
#Dietitians can access this app and add or change recipes to the dictionary in the form of list
#which will be displayed to users...

recipes = {

    # Vegetrain recipes and grocery list 
    'vegetarian': [
        ['Vegetable Soup', ['carrots', 'celery', 'potatoes', 'vegetable broth']],
        ['Tofu Curry', ['tofu', 'curry paste', 'coconut milk', 'rice']],
        ['Pasta Primavera', ['pasta', 'olive oil', 'garlic', 'broccoli', 'carrots', 'peas']],
        ['Vegetable Stir Fry', ['broccoli', 'carrots', 'bell peppers', 'soy sauce', 'rice']],
        ['Margherita Pizza', ['pizza crust', 'tomato sauce', 'mozzarella cheese', 'basil']]
    ],

    # Vegan recipes and grocery list
    'vegan': [
        ['Vegan Chili', ['kidney beans', 'black beans', 'tomato sauce', 'onion', 'garlic']],
        ['Vegan Curry', ['chickpeas', 'curry paste', 'coconut milk', 'rice']],
        ['Vegan Tacos', ['tortillas', 'black beans', 'avocado', 'salsa']],
        ['Vegan Stir Fry', ['broccoli', 'carrots', 'bell peppers', 'soy sauce', 'rice']],
        ['Vegan Pasta Salad', ['pasta','olive oil','cherry tomatoes','cucumbers','red onion']]
    ],
    
    # gluten-free recipes and grocery list
    "gluten-free": [
        ["Gluten-free Spaghetti Carbonara", ["gluten-free spaghetti", "bacon", "eggs", "parmesan cheese"]],
        ["Gluten-free Chicken Alfredo", ["gluten-free fettuccine", "chicken breast", "butter", "heavy cream", "parmesan cheese"]],
        ["Gluten-free Vegetable Lasagna", ["gluten-free lasagna noodles", "ricotta cheese", "spinach", "tomato sauce"]],
        ["Gluten-free Quinoa Stuffed Peppers", ["quinoa", "bell peppers", "black beans", "corn", "cheddar cheese"]],
        ["Gluten-free Cauliflower Fried Rice", ["cauliflower rice", "carrots", "peas", "eggs", "soy sauce"]]
    ],
    
    # dairy-free recipes and grocery list
    "dairy-free": [
        ["Dairy-free Mac and Cheese", ["macaroni","dairy-free cheddar cheese","dairy-free milk","nutritional yeast"]],
        ["Dairy-free Cream of Mushroom Soup", ["mushrooms","dairy-free milk","vegetable broth","onion","garlic"]],
        ["Dairy-free Fettuccine Alfredo", ["fettuccine","dairy-free heavy cream","dairy-free parmesan cheese","garlic"]],
        ["Dairy-free Mashed Potatoes", ["potatoes","dairy-free butter","dairy-free milk"]],
        ["Dairy-free Chocolate Pudding", ["avocado","cocoa powder","maple syrup","vanilla extract"]]
    ]
}

#Function prompts the input and returns a valid choice from the list of choices
#Also it validates the user input to ensure that user input is valid among choices 
def getChoice(prompt, choices):
    choice = input(prompt).lower()
    while choice not in choices:
        print("Invalid choice. Please enter one of the following: " + ', '.join(choices))
        choice = input(prompt).lower()
    return choice


#this function asks the user to choose any of the prefrences listed below and
#it uses the above function to validate user input
#and the user can end their selection by entering 5 and the selection is stored as a list of strings 
def getDietaryPreferences():
    preferences = []
    for i in range(5):
        print("Please Select Your Dietary Preferences")
        print("After selecting when asked again and if you are sure then enter 5 to submit else choose other choice")
        print("===============================")
        print("1. Vegetarian")
        print("2. Vegan")
        print("3. Gluten-Free")
        print("4. Dairy-Free")
        print("5. Done")
        choice = getChoice("Enter your choice: ", ['1','2','3','4','5'])
        if choice == '1':
            preferences.append('vegetarian')
        elif choice == '2':
            preferences.append('vegan')
        elif choice == '3':
            preferences.append('gluten-free')
        elif choice == '4':
            preferences.append('dairy-free')
        elif choice == '5':
            break
    return preferences


#this function takes the above generated list of users preference and generate 7 day meal plan based on the user preference
#it also selects random meal rom availableRecipes and appends to meal plan and return as list of meals
def generateMealPlan(preferences):
    mealPlan = []
    for day in range(7):
        availableRecipes = []
        for preference in preferences:
            if preference in recipes:
                availableRecipes.extend(recipes[preference])
        meal, ingredients = random.choice(availableRecipes)
        mealPlan.append(meal)
    return mealPlan


#similarly to above function the below function generates grocery list for the above generated meal plan on the basis of user preferences
def generateGroceryList(mealPlan):
    groceryList = []
    for preference, preferenceRecipes in recipes.items():
        for meal, ingredients in preferenceRecipes:
            if meal in mealPlan:
                for ingredient in ingredients:
                    if ingredient not in groceryList:
                        groceryList.append(ingredient)
    return groceryList


#this function creates new excel workbook and woorksheet titled "Meal Plan"...
#and later it appends data from meanPlan and grocery lists with weekdays and save it to mealplan excel 
def saveData(mealPlan, groceryList):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Meal Plan"
    sheet.append(["Day", "Meal", "Item"])
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i in range(len(weekdays)):
        row = [weekdays[i]]
        if i < len(mealPlan):
            row.append(mealPlan[i])
        else:
            row.append("")
        if i < len(groceryList):
            row.append(groceryList[i])
        else:
            row.append("")
        sheet.append(row)
    wb.save('mealPlan.xlsx')
    print("Your MEAL PLAN and GROCERY LIST is being generated in Excel Sheet named mealPlan")
    print("Enjoy Your meals and STAY SAFE STAY HEALTHIER... :)")

#Based on the user's dietary preferences, a meal plan and grocery list are generated and saved to an Excel file.
#The code first executes the main function, which prints two lines of text.
def main():
    print("Welcome to your MEAl MATE ")
    print("==========================")
    preferences = getDietaryPreferences()
    mealPlan = generateMealPlan(preferences)
    groceryList = generateGroceryList(mealPlan)
    saveData(mealPlan, groceryList)

main()
