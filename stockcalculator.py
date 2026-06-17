stocks={
    "AAPL":180,
    "TSLA":250,
    "GOOG":2800,
    "AMZN": 3300
}
total_investment=0
while True:
    stock_name=input("Enter Stock Name (or Type 'done' to finish):").upper()
    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity=int(input("Enter Quantity : "))
        price=stocks[stock_name]
        total=price*quantity
        total_investment+=total
        print("Added : ",total)
else:
    print("Stock Not Found")
print("\nTotal Investment: ",total_investment)
with open("portfolio.txt","w") as file:
    file.write(f"Total Investment:  {total_investment}")