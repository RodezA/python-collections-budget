
import budget
from . import Expense
import matplotlib.pyplot as plt

class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses =[]
        self.sum_overages=0
        self.overages=[]

    def append(self, item):
        if (self.sum_expenses+item < self.budget):
            self.expenses.append(item)
            self.sum_expenses+=item
        else:
            self.overages.append(item)
            self.sum_overages+=item

    def __len__(self):
        return len(self.expenses)+len(self.overages)

def main():
    myBudgetList = BudgetList(1200)
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    print('The count of all expenses: ' + str(len(myBudgetList)))

if __name__ == "__main__":
    main()
    fig, ax = plt.subplots()

def __iter__(self):
    self.iter()=self.expenses
    self.iter_o=self.overages
    return self

def __next__(self):
    try:
        return __next__()
    except:
        StopIteration
        return __next__(self.iter_o)


