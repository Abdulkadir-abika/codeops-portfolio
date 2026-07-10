total=100
friend=5
def split_bill(total,friend,tip_rate=0.10):
    tip_amount = total * tip_rate
    total_with_tip = total + tip_amount
    amount_per_person = total_with_tip / friend
    return amount_per_person
for i in range(5):
    print(split_bill(total,friend))

