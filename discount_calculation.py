import math
class Discount():
    def discount(mid_json,total_medicines,count):
        discount = math.log(total_medicines / count, 10)
        if discount < 0:
            discount = 0
        if discount > 30:
            discount = 30
        return discount