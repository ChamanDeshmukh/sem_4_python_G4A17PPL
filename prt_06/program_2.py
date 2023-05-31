#example_of_multiple_inheritance
class Brands:
    brand_name_1 = "Amazon"
    brand_name_2 = "Ebay"
    brand_name_3 = "OLX"
    
class Products:
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"

class Popularity(Brands,Products):
    prod_1_popularity = 100
    prod_2_popularity = 70
    prod_3_popularity = 60
    
obj_1 = Popularity()
print(obj_1.brand_name_1+" is an "+obj_1.prod_1)
print(obj_1.brand_name_2+" is an "+obj_1.prod_2)
print(obj_1.brand_name_3+" is an "+obj_1.prod_3)
