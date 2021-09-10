from Product import Product

class Order:
    counter = 0
    def __init__(self, products):
        Order.counter += 1
        self.order_id = Order.counter
        self.products = list(products)

    def add_order(self, product):
        self.products.append(product)

    def total_order(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        products = [product.__str__() for product in self.products]
        return f'<Order {self.order_id} {products}>'

if __name__ == '__main__':
    # Some products
    product1 = Product('T-Shirt', 100)
    product2 = Product('Shorts', 200)
    product3 = Product('socks', 40)
    product4 = Product('blouse', 70)

    # Product list
    product_list1 = [product1, product2]
    product_list2 = [product3, product4]

    # Orders
    orden1 = Order(product_list1)
    orden2 = Order(product_list2)

    orden2.add_order(product1)

    print(orden1.total_order())
    print(orden2.total_order())
