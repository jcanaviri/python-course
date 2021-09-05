class Product:
    counter = 0
    def __init__(self, name, price):
        Product.counter += 1
        self._product_id = Product.counter
        self.name = name
        self.price = price

    def __str__(self):
        return f'<Product {self.name}>'

if __name__ == '__main__':
    product1 = Product('T-Shirt', 100)
    product2 = Product('Shorts', 200)

    print(product2)
