# Nutrition Facts
# The U.S. Food & Drug Administration (FDA) offers downloadable/printable posters that “show nutrition
# information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to
# download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods
# in the stores.”
#
# In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (
# case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for
# fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as
# written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
fruits = [
    {"name": "Apple", "Calories": "130"},
    {"name": "Avocado", "Calories": "50"},
    {"name": "Banana", "Calories": "110"},
    {"name": "Cantaloupe", "Calories": "50"},
    {"name": "Grapefruit", "Calories": "60"},
]

f = input("Item: ").strip().capitalize()
for fruit in fruits:
    if fruit["name"] == f:
        print("Calories:", fruit["Calories"],end="")