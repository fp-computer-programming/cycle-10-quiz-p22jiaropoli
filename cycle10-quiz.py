# Author JRI 3/23/22

prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip','half-zip']]

# Question 1

def find_average(lst):
    

    price = 0 # set to add up all of the prices in the store
    num = len(lst) # holds the amount of different items in the store
    

    for x in lst: # adds each price to the total
        price += x
    
    average = price / num # stores the average price as a variable
# then returns the average
    return average
    
# Question 2

def price_minus_five(lst):
    for i,v in enumerate(lst): # enumerates, reduces the second piece by 5
        lst[i] = v - 5
    return lst # returns the modified list

print(price_minus_five(prices)) #prints newly modified list


# Question 3

def semester_sales(prices,sales):
    
    
    
    total = 0 # used to store the total sales on the semester
    
    for i,v in enumerate(prices): # for loop of the enumerated prices
        total += (prices[i] * sales[i]) # adds the price times the amount of sales to the variable total

    return total


# Question 4

def greater_than_40(prices, lower): # define function and set perameters
    
    
    for v in prices:
        
        i = 0 # index
        
        if v[i] <= 40: # if the price is less than 40 add v to the base index
            lower += v

        else:
            lower += v - 10 # subracting 10 from the price
            i += 1
            return lower

# Question 5

def format(price, items): # defining function that formats the prices and the different items

    for rows in items: 
        for i, v in enumerate(rows): # eneumerate list to access items seperately
            rows[i] = "{0} ${1}".format(v, price[0]) # adds the item and the price with a dollar sign in front

    return items

print(format([30, 40, 25, 55, 60, 80, 65],[['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip','half-zip']])) 