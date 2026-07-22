total=100
friend=5
def split_bill(total,friend,tip=0.10):
    total_with_tip = total + (total* tip)
    amount_per_person = total_with_tip / friend
    return amount_per_person
for i in range(1, friend+1):
    print(f"Friend {i} should pay: ${split_bill(total, friend):.2f}")

