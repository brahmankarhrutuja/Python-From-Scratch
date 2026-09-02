total_sales = 0

transactions = int(input("Enter value of transaction:"))

for i in range(1, transactions + 1):
    sale = float(input("Enter sales amount transaction{i}:"))
    
    total_sales += sale 
    
    if sale > 500:
        print("Good selling")
        
        average_sales = total_sales / transactions
        
        print("\n sales report")
        print("Total sales are here:", total_sales)
        print("Average Sales:", average_sales)
         