# AI Disclosure: I used ChatGPT to help identify and explain errors in my code, including logical errors and an IndexError.
# Reflection Question 1: The first bug that I has spotted was the missing colon, and i found it from the traceback. I think that is this because I often make this mistake within my own coding, so I am used to recognizing this error.
# Reflection Question 2:apply_discount(price, tier) shows the price of an item after the discount is applied, as well as the tier that the discount is placed in. A collauge could easily use this function without the need to read the body.
# Reflection Question 3: The AI helped build my understanding, since I would place the name of the errors into the AI rather than what specifically to fix. Although, when I had completed that but knew there was another error I was unsure of, I put the code into Chat GPT and asked for its help, while reading the explaination of what it did to fix it.
# #Exercise 1
# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# Exercise 2
def apply_discount (price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function with different tiers
original_price = 2000

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print(f"final_price(200, 0.07, 'gold'): ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4
orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (50, 'none')]

for price, tier in orders:
    total = final_price(price, 0.07, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# Exercise 5
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale #allows ability to add sales instead of completley replacing the total variable.
print(f"Total: ${total}")

count = 0
for sale in sales : #missing colon that prevents the for statement from running
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): #fixed the condition to prevent index out of bounds
    print(sales[i])
    i += 1

# Exercise 6

x = 100 # global x

def double_it():
    x = 999 # local x
    return x * 2

print(x)
print(double_it())
print(x)
