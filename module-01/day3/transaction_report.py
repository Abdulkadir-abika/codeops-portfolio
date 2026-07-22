trans = {}
try:
    with open ("transactions.txt" , "r") as f:
        for line in f:
            name,amount = line.strip().split(",")
            amount = float(amount)
            trans[name] = trans.get(name,0) + amount
    print(trans)
    trans_sorted = sorted(trans.items(), key=lambda x: x[1], reverse = True )
    print(trans_sorted)
    print("the telebirr report follows as :-")
    with open("report.txt", "w") as report:
        for name, total in trans_sorted:
            line = f"{name}: {total} ETB\n"
           
            print(line.strip())     
            report.write(line)
except FileNotFoundError:
    print("Error:file transaction.txt not found! or the file is not in the current directory.")
finally:
    print("Done.")
    