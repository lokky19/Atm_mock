class Budget: # this is a class Budget

    # instance attributes      
    def __init__(self, name):
       self.name = name
       self.balance = 0
    
    def deposit(self, amount):# for deposit
        self.balance = amount
        
        return f"You made a deposit of ${self.balance} in {self.name} budget \n "

    def withdraw(self, amount): # for withdraw
        self.amount = amount
        if self.balance < amount:
            return "***Insufficient Funds***\n"
        else:
            self.balance = self.balance - amount

            withdarw_statement = f"${self.amount} was deducted from your {self.name},\n "

            return withdarw_statement
    
    def get_balance(self):

        feedback = f"Your is balance for {self.name}: \n${self.balance}\n"
        return feedback

    def transfer(self, amount, category):# to transfer funds
        if self.balance < amount:
            return "***Insufficient Funds***\n"
        else:
            self.balance -= amount
            category.balance += amount
            transfer = f"***Transfer was successful***\nThe balance for {self.name} is ${self.balance}\n"
            transfer += f"The balancefor {category.name} is ${category.balance}\n"
            return transfer

#instantiating the Budget class
food = Budget("food")
clothing = Budget("clothing")
entertainment = Budget("entertainment")
# to access the instance attributes
print("#################################################################")
print(food.deposit (3500)) # to make deposit into the food budget
print(clothing.deposit (5300))# to make deposit into the food budget
print(entertainment.deposit (2400))# to make deposit into the food budget
print("#################################################################")
print(food.withdraw (4000))# to make withdrwal from the food budget
print(clothing.withdraw (1200))# to make withdrwal from the clothing budget
print(entertainment.withdraw (400))# to make withdrwal from the entertainment budget
print("#################################################################")
print(food.get_balance ())
print(clothing.get_balance())
print(entertainment.get_balance())
print("#################################################################")
# transfer between categories
print(food.transfer(2000, clothing))
print(clothing.transfer(1100, entertainment))
print(entertainment.transfer (3050, food))


