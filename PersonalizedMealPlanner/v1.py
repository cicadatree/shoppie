import random

# task: create a python program that creates a personalized meal plan for 1 week based on a user's inputs
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
meals = {
    "No Restrictions": {
        "Breakfast": ["Whole grain toast with scrambled eggs", "Omelette", "Yogurt with fruits", "Pancakes", "Smoothie bowl", "Breakfast burrito", "French toast", "Granola with milk", "Egg muffins", "Breakfast quesadilla", "Frittata", "Breakfast sandwich", "Waffles", "Cereal with milk", "Egg and cheese wrap"],
        "Lunch": ["Spaghetti Bolognese", "Chicken Caesar salad", "Turkey sandwich", "Grilled chicken with vegetables", "Caesar salad wrap", "BLT sandwich", "Chicken wrap", "Chicken stir-fry", "Chicken fajitas", "Chicken and rice", "Chicken and vegetable skewers", "Chicken and avocado salad", "Chicken and quinoa salad", "Chicken and broccoli stir-fry", "Chicken and mushroom risotto"],
        "Dinner": ["Grilled steak", "Salmon with roasted vegetables", "Pasta Alfredo", "Grilled chicken with mashed potatoes", "Steak with baked potato", "Fish tacos", "Beef stir-fry", "Beef and broccoli", "Beef and vegetable stir-fry", "Beef and mushroom stir-fry", "Beef and rice", "Beef and quinoa", "Beef and peppers", "Beef and sweet potato", "Beef and zucchini noodles"],
        "Snack": ["Greek yogurt with honey and nuts", "Hummus with veggies", "Mixed nuts", "Fruit salad", "Protein shake", "Cheese and crackers", "Trail mix", "Apple slices with peanut butter", "Cottage cheese with fruit", "Popcorn", "Energy bar", "Yogurt parfait", "Rice cakes with almond butter", "Vegetable sticks with dip", "Hard-boiled eggs"]
    },
    "Vegetarian": {
        "Breakfast": ["Vegetable stir-fry", "Smoothie bowl", "Avocado toast", "Vegetable omelette", "Vegetable frittata", "Vegetable scramble", "Vegetable breakfast burrito", "Vegetable hash", "Vegetable quiche", "Vegetable breakfast sandwich", "Vegetable pancakes", "Vegetable waffles", "Vegetable cereal", "Vegetable muffins", "Vegetable breakfast quesadilla"],
        "Lunch": ["Caprese salad", "Veggie wrap", "Quinoa and roasted vegetables", "Vegetable stir-fry", "Vegetable stir-fry noodles", "Vegetable stir-fry rice", "Vegetable stir-fry quinoa", "Vegetable stir-fry couscous", "Vegetable stir-fry bulgur", "Vegetable stir-fry millet", "Vegetable stir-fry barley", "Vegetable stir-fry farro", "Vegetable stir-fry buckwheat", "Vegetable stir-fry amaranth", "Vegetable stir-fry spelt"],
        "Dinner": ["Mushroom risotto", "Eggplant Parmesan", "Vegetable curry", "Vegetable lasagna", "Vegetable pasta", "Vegetable stir-fry", "Vegetable stir-fry noodles", "Vegetable stir-fry rice", "Vegetable stir-fry quinoa", "Vegetable stir-fry couscous", "Vegetable stir-fry bulgur", "Vegetable stir-fry millet", "Vegetable stir-fry barley", "Vegetable stir-fry farro", "Vegetable stir-fry buckwheat"],
        "Snack": ["Eggplant chips", "Guacamole with tortilla chips", "Vegetable spring rolls", "Vegetable sushi rolls", "Vegetable quesadilla", "Vegetable samosa", "Vegetable pakora", "Vegetable fritters", "Vegetable skewers", "Vegetable bruschetta", "Vegetable hummus wrap", "Vegetable pita pockets", "Vegetable empanadas", "Vegetable dumplings", "Vegetable sliders"]
    },
    "Vegan": {
        "Breakfast": ["Vegan oatmeal with fruits and nuts", "Chia pudding", "Fruit salad", "Vegan pancakes", "Vegan smoothie", "Vegan breakfast burrito", "Vegan granola with plant-based milk", "Vegan muffins", "Vegan breakfast sandwich", "Vegan waffles", "Vegan cereal", "Vegan energy balls", "Vegan breakfast cookies", "Vegan breakfast bars", "Vegan breakfast quesadilla"],
        "Lunch": ["Quinoa salad", "Vegan sushi rolls", "Sweet potato and black bean tacos", "Vegan stir-fry", "Vegan stir-fry noodles", "Vegan stir-fry rice", "Vegan stir-fry quinoa", "Vegan stir-fry couscous", "Vegan stir-fry bulgur", "Vegan stir-fry millet", "Vegan stir-fry barley", "Vegan stir-fry farro", "Vegan stir-fry buckwheat", "Vegan stir-fry amaranth", "Vegan stir-fry spelt"],
        "Dinner": ["Roasted vegetable wrap", "Vegan lasagna", "Chickpea curry", "Vegan pasta", "Vegan stir-fry", "Vegan stir-fry noodles", "Vegan stir-fry rice", "Vegan stir-fry quinoa", "Vegan stir-fry couscous", "Vegan stir-fry bulgur", "Vegan stir-fry millet", "Vegan stir-fry barley", "Vegan stir-fry farro", "Vegan stir-fry buckwheat", "Vegan stir-fry amaranth"],
        "Snack": ["Fruit and nut mix", "Vegan energy balls", "Roasted chickpeas", "Vegan fruit smoothie", "Vegan protein shake", "Vegan trail mix", "Vegan fruit salad", "Vegan granola bars", "Vegan popcorn", "Vegan energy bar", "Vegan yogurt with fruits", "Vegan rice cakes with almond butter", "Vegan vegetable sticks with dip", "Vegan hummus with veggies", "Vegan hard-boiled eggs"]
    },
    "Gluten-Free": {
        "Breakfast": ["Yogurt with gluten-free granola and berries", "Gluten-free pancakes", "Fruit smoothie", "Gluten-free toast with avocado", "Gluten-free smoothie bowl", "Gluten-free breakfast burrito", "Gluten-free granola with milk", "Gluten-free muffins", "Gluten-free breakfast sandwich", "Gluten-free waffles", "Gluten-free cereal", "Gluten-free energy balls", "Gluten-free breakfast cookies", "Gluten-free breakfast bars", "Gluten-free breakfast quesadilla"],
        "Lunch": ["Quinoa bowl", "Grilled chicken salad", "Stuffed bell peppers", "Gluten-free stir-fry", "Gluten-free stir-fry noodles", "Gluten-free stir-fry rice", "Gluten-free stir-fry quinoa", "Gluten-free stir-fry couscous", "Gluten-free stir-fry bulgur", "Gluten-free stir-fry millet", "Gluten-free stir-fry barley", "Gluten-free stir-fry farro", "Gluten-free stir-fry buckwheat", "Gluten-free stir-fry amaranth", "Gluten-free stir-fry spelt"],
        "Dinner": ["Greek salad", "Grilled shrimp with quinoa", "Zucchini noodles with pesto", "Gluten-free pasta", "Gluten-free stir-fry", "Gluten-free stir-fry noodles", "Gluten-free stir-fry rice", "Gluten-free stir-fry quinoa", "Gluten-free stir-fry couscous", "Gluten-free stir-fry bulgur", "Gluten-free stir-fry millet", "Gluten-free stir-fry barley", "Gluten-free stir-fry farro", "Gluten-free stir-fry buckwheat", "Gluten-free stir-fry amaranth"],
        "Snack": ["Gluten-free muffins", "Rice cakes with almond butter", "Gluten-free granola bars", "Gluten-free fruit smoothie", "Gluten-free protein shake", "Gluten-free trail mix", "Gluten-free fruit salad", "Gluten-free energy bars", "Gluten-free popcorn", "Gluten-free energy balls", "Gluten-free yogurt with fruits", "Gluten-free vegetable sticks with dip", "Gluten-free hummus with veggies", "Gluten-free hard-boiled eggs", "Gluten-free cheese and crackers"]
    },
    "Dairy-Free": {
        "Breakfast": ["Dairy-free yogurt parfai", "Smoothie with almond milk", "Oatmeal with berries", "Dairy-free pancakes", "Dairy-free smoothie bowl", "Dairy-free breakfast burrito", "Dairy-free granola with plant-based milk", "Dairy-free muffins", "Dairy-free breakfast sandwich", "Dairy-free waffles", "Dairy-free cereal", "Dairy-free energy balls", "Dairy-free breakfast cookies", "Dairy-free breakfast bars", "Dairy-free breakfast quesadilla"],
        "Lunch": ["Tofu stir-fry", "Dairy-free Caesar salad", "Turkey and avocado wrap", "Dairy-free stir-fry", "Dairy-free stir-fry noodles", "Dairy-free stir-fry rice", "Dairy-free stir-fry quinoa", "Dairy-free stir-fry couscous", "Dairy-free stir-fry bulgur", "Dairy-free stir-fry millet", "Dairy-free stir-fry barley", "Dairy-free stir-fry farro", "Dairy-free stir-fry buckwheat", "Dairy-free stir-fry amaranth", "Dairy-free stir-fry spelt"],
        "Dinner": ["Cobb salad", "Grilled fish with vegetables", "Stir-fried tofu with rice", "Dairy-free pasta", "Dairy-free stir-fry", "Dairy-free stir-fry noodles", "Dairy-free stir-fry rice", "Dairy-free stir-fry quinoa", "Dairy-free stir-fry couscous", "Dairy-free stir-fry bulgur", "Dairy-free stir-fry millet", "Dairy-free stir-fry barley", "Dairy-free stir-fry farro", "Dairy-free stir-fry buckwheat", "Dairy-free stir-fry amaranth"],
        "Snack": ["Dairy-free cheese and crackers", "Dairy-free yogurt with nuts", "Rice crackers with hummus", "Dairy-free fruit smoothie", "Dairy-free protein shake", "Dairy-free trail mix", "Dairy-free fruit salad", "Dairy-free energy bars", "Dairy-free popcorn", "Dairy-free energy balls", "Dairy-free yogurt with fruits", "Dairy-free vegetable sticks with dip", "Dairy-free hummus with veggies", "Dairy-free hard-boiled eggs", "Dairy-free cheese and cucumber slices"]
    },
    "Keto-Friendly": {
        "Breakfast": ["Bacon and eggs", "Keto smoothie", "Avocado with smoked salmon", "Keto pancakes", "Keto smoothie bowl", "Keto breakfast burrito", "Keto granola with almond milk", "Keto muffins", "Keto breakfast sandwich", "Keto waffles", "Keto cereal", "Keto energy balls", "Keto breakfast cookies", "Keto breakfast bars", "Keto breakfast quesadilla"],
        "Lunch": ["Steak with buttered asparagus", "Keto salad with chicken", "Cauliflower fried rice", "Keto stir-fry", "Keto stir-fry noodles", "Keto stir-fry rice", "Keto stir-fry quinoa", "Keto stir-fry couscous", "Keto stir-fry bulgur", "Keto stir-fry millet", "Keto stir-fry barley", "Keto stir-fry farro", "Keto stir-fry buckwheat", "Keto stir-fry amaranth", "Keto stir-fry spelt"],
        "Dinner": ["Salmon with cauliflower rice", "Grilled chicken with broccoli", "Zucchini noodles with pesto", "Keto pasta", "Keto stir-fry", "Keto stir-fry noodles", "Keto stir-fry rice", "Keto stir-fry quinoa", "Keto stir-fry couscous", "Keto stir-fry bulgur", "Keto stir-fry millet", "Keto stir-fry barley", "Keto stir-fry farro", "Keto stir-fry buckwheat", "Keto stir-fry amaranth"],
        "Snack": ["Avocado and shrimp salad", "Keto fat bombs", "Cheese and cucumber slices", "Keto fruit smoothie", "Keto protein shake", "Keto trail mix", "Keto fruit salad", "Keto energy bars", "Keto popcorn", "Keto energy balls", "Keto yogurt with fruits", "Keto vegetable sticks with dip", "Keto hummus with veggies", "Keto hard-boiled eggs", "Keto cheese and crackers"]
    }
}


class MealPlanner:
    def check_input(self):
        if self.user_input[1] == "No Restrictions":
            for day in weekdays:
                breakfast = random.choice(meals['No Restrictions']['Breakfast'])
                lunch = random.choice(meals['No Restrictions']['Lunch'])
                dinner = random.choice(meals['No Restrictions']['Dinner'])
                snack = random.choice(meals['No Restrictions']['Snack'])
                print(f"{day}: \n  Breakfast - {breakfast}, \n  Lunch - {lunch}, \n  Dinner - {dinner}, \n  Snack - {snack}\n")
        elif self.user_input[1] == "Vegetarian":
            for day in weekdays:
                breakfast = random.choice(meals['Vegetarian']['Breakfast'])
                lunch = random.choice(meals['Vegetarian']['Lunch'])
                dinner = random.choice(meals['Vegetarian']['Dinner'])
                snack = random.choice(meals['Vegetarian']['Snack'])
                print(f"{day}: \n  Breakfast - {breakfast}, \n  Lunch - {lunch}, \n  Dinner - {dinner}, \n  Snack - {snack}\n")
        elif self.user_input[1] == "Vegan":
            for day in weekdays:
                breakfast = random.choice(meals['Vegan']['Breakfast'])
                lunch = random.choice(meals['Vegan']['Lunch'])
                dinner = random.choice(meals['Vegan']['Dinner'])
                snack = random.choice(meals['Vegan']['Snack'])
                print(f"{day}: \n  Breakfast - {breakfast}, \n  Lunch - {lunch}, \n  Dinner - {dinner}, \n  Snack - {snack}\n")
        elif self.user_input[1] == "Gluten-Free":
            for day in weekdays:
                breakfast = random.choice(meals['Gluten-Free']['Breakfast'])
                lunch = random.choice(meals['Gluten-Free']['Lunch'])
                dinner = random.choice(meals['Gluten-Free']['Dinner'])
                snack = random.choice(meals['Gluten-Free']['Snack'])
                print(f"{day}: \n  Breakfast - {breakfast}, \n  Lunch - {lunch}, \n  Dinner - {dinner}, \n  Snack - {snack}\n")
        elif self.user_input[1] == "Dairy-Free":
            for day in weekdays:
                breakfast = random.choice(meals['Dairy-Free']['Breakfast'])
                lunch = random.choice(meals['Dairy-Free']['Lunch'])
                dinner = random.choice(meals['Dairy-Free']['Dinner'])
                snack = random.choice(meals['Dairy-Free']['Snack'])
                print(f"{day}: \n  Breakfast - {breakfast}, \n  Lunch - {lunch}, \n  Dinner - {dinner}, \n  Snack - {snack}\n")
        elif self.user_input[1] == "Keto-Friendly":
            print(f"\nHello {self.user_input[0]}, here is your meal plan for the week: \n")
            for day in weekdays:
                breakfast = random.choice(meals['Keto-Friendly']['Breakfast'])
                lunch = random.choice(meals['Keto-Friendly']['Lunch'])
                dinner = random.choice(meals['Keto-Friendly']['Dinner'])
                snack = random.choice(meals['Keto-Friendly']['Snack'])
                print(f" {day}: \n  Breakfast - {breakfast}, \n  Lunch - {lunch}, \n  Dinner - {dinner}, \n  Snack - {snack}\n")
        else:
            print("You have not provided a valid dietary restriction. Please try again (using one of the following options: No Restrictions, Vegetarian, Vegan, Gluten-Free, Dairy-Free, or Keto-Friendly) ")
            self.__init__()
            
    def __init__(self):
        self.user_input = [
            input("What is your name? "),
            input("What dietary restrictions do you have? ")
        ]
        self.check_input()

newMealPlan = MealPlanner()
newMealPlan.check_input()