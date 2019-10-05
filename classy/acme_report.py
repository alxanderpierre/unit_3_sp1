from acme import Product
import random
from collections import Counter


adjective = random.sample(['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved'], 1)

noun = random.sample(['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Hangers'], 1)

# Concatenate the adjectives  and the nouns into one single product name"""

name = adjective[0] + " " + noun[0]

# Now setting values price, weight, flammability"""

flammability = random.uniform(0, 2.5)
price = random.randint(5, 100)
weight = random.randint(5,100)

def generate_products(name, flammability, price, weight, num_products=30):
    prod = []   # want to return a list
    for i in range(num_products):
        prod.append(Product(name, flammability, price, weight))
    return prod

def inventory_report(prod_list):
    name=[]
    flame_mean=[]
    price_mean=[]
    weight_mean=[]

    for prod in prod_list:
        names.append(prod.name)
        flame_mean.append(prod.flamability)
        price_mean.append(prod.price)
        weight_mean.append(prod.weight)

    fq = list(Counter(names). values())

    unique=[]

    for i in range(len(fq)):
        if fq[i]==1:
            unique.append(names[i])

    # ok so now we have to get the average of each. sum/len

    flame_average = sum(flame_mean)/len(flame_mean)
    price_average = sum(price_mean)/len(price_mean)
    weight_average = sum(weight_mean)/len(weight_mean)
    num_unique_prod = len(unique)

    print(f"Number of unique product names are {num_unique_prod}.")
    print(f"Flammability's average is {flame_average}.")
    print(f"Price's average is{price_average}.")
    print(f"Weight's average is {weight_average}.")



prod = generate_products(name,flammability,price,weight)
inventory_report(prod)
