
import budget

class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses =[]
        self.sum_averages=0
        self.overages=[]

    def append(self, item):
        if self.sum_expenses + item < self.budget:
            append(self.expenses)
        else:
            append(self.overages)

    def __len__(self):
        return self.expenses+self.overages

def main():
    myBudgetList = BudgetList(1200)
