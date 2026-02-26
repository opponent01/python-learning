#What Are Some Common Techniques to Loop Over a Dictionary?

products= {
    "laptop": 990,
    "smartphone": 600,
    "tablet": 250,
    "headphones": 70
}
#If we want to offer a 20% discount on all our products, we can loop over all the key-value pairs and modify the prices.
for product, price in products.items():
    products[product]= round(price * 0.8)
print(products)









