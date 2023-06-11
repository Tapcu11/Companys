class Company:
    def __init__(self, name, warranty, delivery_time, payment_term, delivery_term, vat):
        self.name = name
        self.warranty = warranty
        self.delivery_time = delivery_time
        self.payment_term = payment_term
        self.delivery_term = delivery_term
        self.vat = vat

    def introduce_self(self):
        print("Company name : " + self.name)
        print("Warranty : " + self.warranty)
        print("Delivery time :" + self.delivery_time)
        print("Payment term :" + self.payment_term)
        print("Delivery term :" + self.delivery_term)
        print("VAT : " + self.vat)


class Product:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def calculate_total_price(self):
        return self.quantity * self.unit_price

    def introduce_product(self):
        print("Product: " + (product.name))
        print("Quantity: " + str(product.quantity))
        print("Unit Price: " + str(product.unit_price))
        print("Total Price: " + str(product.calculate_total_price()))


num_companies = int(input("How many companies do you want to add? : "))

companies = []

for i in range(num_companies):
    print(f"\nEnter details for Company {i + 1}:")
    name = input("Enter the name: ")
    warranty = input("Enter the time of warranty: ")
    delivery_time = input("Enter the time of delivery: ")
    payment_term = input("Enter the payment term: ")
    delivery_term = input("Enter the delivery term: ")
    vat = input("Include VAT or exclude VAT: ").lower()

    company = Company(name, warranty, delivery_time, payment_term, delivery_term, vat)

    num_products = int(input("How many products do you want to add for this company? : "))
    products = []
    for j in range(num_products):
        print(f"\nEnter details for Product {j + 1}:")
        product_name = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        unit_price = float(input("Enter the unit price: "))
        if vat == "include":
            unit_price = unit_price / 1.18

        product = Product(product_name, quantity, unit_price)
        products.append(product)

    company.products = products
    companies.append(company)

print("\nCompany details:")
for i, company in enumerate(companies):
    print(f"\nCompany {i + 1}")
    company.introduce_self()

    print("\nProduct details")
    for j, product in enumerate(company.products):
        print(f"\nProduct {i + 1}")
        product.introduce_product()
