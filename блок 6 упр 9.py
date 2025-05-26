class Actor:
    def __init__(self, text):
        self.text = text

    def line(self):
        return self.text

class Customer(Actor):
    def __init__(self):
      super().__init__("that's one ex-bird!")
    def line(self):
        return f"customer: {super().line()}"

class Clerk(Actor):
    def __init__(self):
      super().__init__("no it isn't...")
    def line(self):
        return f"clerk: {super().line()}"

class Parrot:
    def line(self):
        return "parrot: None"

class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        print(self.customer.line())
        print(self.clerk.line())
        print(self.parrot.line())


if __name__ == '__main__':
    import parrot
    parrot.Scene().action()
