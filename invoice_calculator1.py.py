from logging import DEBUG

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('iv.log'),
        logging.StreamHandler()
    ]
)

def cal(price):
    logging.info("Calculation starts")
    total=0
    for item,rate in price:
        if rate<0:
            logging.warning(f"Negative value for price is an error {item}:{rate}")
        else:
            logging.debug(f"Adding {item} : Rs.{rate}")
            total+=max(rate,0)
    return total

price=[('TV',25000),('LIGHT',200),('FAN',3000),('TABLE',-6000),('STOVE',2000)]

tot=cal(price)
print(f"TOTAL : {tot}")