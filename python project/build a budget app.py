class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount, "description": desc})
    
    def withdraw(self, amount, desc=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": desc})
        return True
    
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    
    def transfer(self, amount, other):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {other.name}")
        other.deposit(amount, f"Transfer from {self.name}")
        return True
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    spendings = []
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spendings.append(spent)
    
    total = sum(spendings)
    percents = [int(s/total*100) if total != 0 else 0 for s in spendings]
    
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for p in percents:
            chart += "o  " if p >= i else "   "
        chart += "\n"
    
    chart += "    " + "-" * (3*len(categories)+1) + "\n"
    
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)
    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += name[i] + "  " if i < len(name) else "   "
        if i < max_len-1:
            chart += "\n"
    
    return chart


# TEST CODE - ADD THIS TO SEE OUTPUT
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing]))