customers = [("Abebe", 1200),("Kebede", 800),("Alemu", 400),
             ("Mulu", 1500),("Tadesse", 600)]
def tier(balance) :
    if balance >= 1000 :
        return "premium"
    elif balance >=500:
        return "standard"
    else:
        return "basic"
for name,balance in customers:
    print(name,tier(balance),balance,"ETB")
  
