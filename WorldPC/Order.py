class Order:
    counter = 0

    def __init__(self, computers):
        Order.counter += 1
        self.order_id = Order.counter
        self.computers = computers

    def add_computer(self, computer):
        self.computers.append(computer)

    def __str__(self):
        computers_str = [comp.__str__() for comp in self.computers]
        return f'<Order {computers_str}>'
