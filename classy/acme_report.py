from acme import Product
import random
from collections import Counter

adjective = random.sample(['Awesome', 'Shiny', 'Impressive',
  'Portable', 'Improved'],1)

noun = random.sample(['Anvil', 'Catapult' ,'Disguise' ,'Mousetrap', 'Hanger'],1)


name = adjective[0] + " " + noun[0]


flammability = random.uniform(0,2.5)
price = random.randint(5,100)
weight = random.randint(5,100)


def generate_products(name,price,weight,flamability,num_products= 30):

    prod = []

    for i in range(num_products):
        prod.append(Product(name,price,weight,flamability))

    return prod

def inventory_report(prod_list):

    names = []
    mean_price = []
    mean_weight = []
    mean_flame = []

    for prod in prod_list:
        names.append(prod.name)
        mean_price.append(prod.price)
        mean_weight.append(prod.weight)
        mean_flame.append(prod.flammability)


    freq = list(Counter(names).values())
    unique = []

    # get unique names
    for i in range(len(freq)):
        if freq[i] == 1:
            unique.append(names[i])

# ok so now we have to get the average of each. sum/len
    flame_average = sum(flame_mean)/len(flame_mean)
    avg_price = sum(mean_price) / len(mean_price)
    avg_weight = sum(mean_weight) / len(mean_weight)
    avg_flame = sum(mean_flame) / len(mean_flame)

    # report
    print(f"Number of unique product names are {num_unique_prod}.")
    print(f"Flammability's average is {flame_average}.")
    print(f"Price's average is{price_average}.")
    print(f"Weight's average is {weight_average}.")
