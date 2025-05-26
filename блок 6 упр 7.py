class Food:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self):
        self.customer = None

    def set_customer(self, customer):
        self.customer = customer

    def takeOrder(self, foodName):
        food = Food(foodName)
        self.customer.receiveOrder(food) 
        return food 

class Customer:
    def __init__(self):
        self.food = None

    def placeOrder(self, foodName, employee):
        employee.takeOrder(foodName) 

    def receiveOrder(self, food):
        self.food = food

    def printFood(self):
        if self.food:
            print(self.food.name)
        else:
            print("No food ordered yet.")

class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()
        self.employee.set_customer(self.customer)  

    def order(self, foodName):
        self.customer.placeOrder(foodName, self.employee) 

    def result(self):
        self.customer.printFood()


if __name__ == '__main__':
    meal = Lunch()
    meal.order("Burger")
    meal.result()
