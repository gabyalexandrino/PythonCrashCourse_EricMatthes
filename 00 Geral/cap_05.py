#cars = ['audi', 'bmw', 'subaru', 'toyota']
#for car in cars:
#    if car == 'bmw': 
#        print(car.upper()) 
#    else:
#        print(car.title())

#car = 'bmw'
#print(car == 'bmw')

#car = 'audi'
#print(car == 'bmw')

#car = 'Audi'
#print(car == 'audi')

#car = 'Audi'
#print(car.lower() == 'audi')

#car = 'Audi'
#print(car.lower() == 'audi')
#print(car)

#requested_topping = 'mushrooms'
#if requested_topping != 'anchovies':
#    print("Hold the anchovies!")

#age = 18
#print(age == 18)

#answer = 17
#if answer != 42:
#    print("That is not the correct answer. Please try again!")

#age = 19
#print(age < 21)
#print(age <= 21)
#print(age > 21)
#print(age >= 21)

#age_0 = 22
#age_1 = 18
#print(age_0 >= 21 and age_1 >= 21)
#age_1 = 22
#print(age_0 >= 21) and (age_1 >= 21)

#age_0 = 22
#age_1 = 18
#print(age_0 >= 21 or age_1 >= 21)
#age_0 = 18
#print(age_0 >= 21 or age_1 >= 21)

#requested_toppings = ['mushrooms', 'onions', 'pineapple']
#print('mushrooms' in requested_toppings)
#print('pepperoni' in requested_toppings)

#banned_users = ['andrew', 'carolina', 'david']
#user = 'marie'
#if user not in banned_users:
#    print(user.title() + ", you can post a response if you wish.")

#age = 19
#if age >=18:
#    print("You are old enough to vote!")
#    print("Have you registered to vote yet?")

#age = 17
#if age >= 18:
#    print("You are old enough to vote!")
#    print("Have you registered to vote yet?")
#else:
#    print("Sorry, you are too young to vote!")
#    print("Please register to vote soon as you turn 18!")

#age = 12
#if age < 4:
#    print("Your admisson cost is $0")
#elif age < 18:
#    print("Your admisson cost is $5")
#else:
#    print("Your admission cost is $10")

#age = 12
#if age < 4:
#    price = 0
#elif age < 18:
#    price = 5
#else:
#    price = 10
#print("Your admission cost is $" + str(price) + ".")

#age = 12
#if age <4:
#    price = 0
#elif age < 18:
#    price = 5
#elif age < 10:
#    price = 5
#elif age >= 65:
#    price = 5
#print("Your admission cost is $" + str(price) + ".")

#requested_toppings = ['mushrooms', 'extra cheese']
#if 'mushrooms' in requested_toppings:
#    print("Adding mushrooms.")
#if 'pepperoni' in requested_toppings:
#    print('Adding pepperoni.')
#if 'extra cheese' in requested_toppings:
#    print("Adding extra cheese.")
#print("\nFinished making your pizza!")

#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#for requested_topping in requested_toppings:
#    if requested_topping == 'green peppers':
#        print("Sorry, we are out of green peppers right now.")
#    else:
#        print("Adding " + requested_topping + ".")
#print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")