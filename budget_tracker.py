class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0

    def check_funds(self, amount):
        if self.balance >= amount: #and self.balance > amount:
            return True
        else:
            return False

    def get_balance(self):
        return self.balance
        #print('total:', self.balance)
        
    def deposit(self, amount, description = ''):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})
        #print('total:', self.balance)

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True
        else:
            return False
        #print('total:', self.balance)
    
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination.category}')
            destination.deposit(amount, f'Transfer from {self.category}')
            return True
        return False
            #{'amount': -amount, 'description': f'Transfer to {destination.category}'})
    
    def __str__(self):
        output = f"{self.category.center(30, '*')}\n"
        for line in self.ledger:
            desc = line['description'][:23]
            amount = f"{line['amount']:.2f}"
            output += f'{desc:<23}{amount:>7}\n'
        output += f'Total: {self.balance:.2f}\n'
        return output
    
def create_spend_chart(categories):
    # calculate total spent per category (withdrawals only)
    spent_amounts = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item ['amount'] < 0: #check if withdrawals are negative digits
                total += abs(item['amount'])
        spent_amounts.append(total)
        
    # calculate total spent across all categories
    total_spent = sum(spent_amounts)

    # calculate percentages and round down to nearest 10
    percentages = []
    for amount in spent_amounts:
        if total_spent == 0:
            percentage = 0
        else:
            percentage = (amount / total_spent) * 100
        percentages.append(int(percentage // 10) * 10)

    # build the chart
    chart = 'Percentage spent by category\n'

    # create bars from 100 to 0
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    
    # add horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1 ) + "\n"

    # add category names vertically
    max_length = max(len(category.category) for category in categories)

    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n"
            
    return chart



            

#Test code... Doesn't work fine
#def create_spend_chart(categories):
#    header = 'Percentage spent by category'
#    total = sum(sum(-e['amount'] for e in c.ledger if e['amount'] < 0) for c in categories)
#    ps = [round(sum(-e['amount'] for e in c.ledger if e ['amount'] < 0) / total * 100 / 100) * 10 for c in categories]
#    for i in range(10, -1, -1):
#       header += f"{i*10:3d}| {'  '.join('o' if p >= i*10 else ' ' for p in ps)}\n"
#        header += "   " + "-" * (len(categories) * 3 + 1) + "\n"
#        names = [c.category for c in categories]
#        for i in range(max(map(len, names))):
#            header += "    " + "  ".join(n[i] if i < len(n) else ' ' for n in names) + "\n"
#        return header.strip() 
    

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(30, 'Lois Vulton')
print(food, clothing)
print(create_spend_chart([food, clothing]))