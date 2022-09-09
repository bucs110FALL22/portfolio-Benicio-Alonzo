import random
#Part A
weeks = 16
print(weeks, type(weeks))

classes = 5
print(classes, type(classes))

tuition = 6000
print(tuition, type(tuition))

classes_per_week = 3
print(classes_per_week, type(classes_per_week))

cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week, type(cost_per_week))

cost_per_class = (cost_per_week / classes_per_week)
print("The cost per class: ", cost_per_class, type(cost_per_class))
print(
    " Give a man a fish, and feed him for a day. Teach him to fish, and feed him for life. - Lao Tzu"
)

#Part B

Fruit = [
    "mango", "kiwi", "guava", "coconut", "dragonfruit", "pineapple",
    "strawberries", "starfruit", "bananas", "pomegranate", "grapes", "durian",
    "blueberries"
]

Selection = random.choice(Fruit)
print("I guess I will be eating", Selection, "today")
