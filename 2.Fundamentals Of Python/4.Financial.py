revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

#Total profit
profit = list([])

for i in range (0 ,len(revenue)):
    profit.append(revenue[i] - expenses[-i])

print(profit)

#get total tax
tax = [round(i * 0.3 , 2) for i in profit]

print("\n\n\n\n\n")
print(tax)

# profit after Tax
print("\n\n\n")

profit_after_tax = list([])

for i in range(0, len(profit)):
    profit_after_tax.append(profit[i] - tax[i])

print(profit_after_tax)

#profit margin after tax

print("\n\n\n\n")

pro_margin = list([])

for i in range(0, len(profit)):
    pro_margin.append(profit_after_tax[i]/revenue[i])

print(pro_margin)

print("\n\n\n")
#after profite margin

pro_margin = [round((i * 100),2) for i in pro_margin]
print(pro_margin)

# profite after tax mean
print("\n\n")
mean_pat = sum(profit_after_tax) / len(profit_after_tax)
print(mean_pat)

# good month
print("\n\n\n")

good_month =list([])

for i in range(0, len(profit)):
    good_month.append(profit_after_tax[i] > mean_pat)

print(good_month)

# bad month
print("\n\n\n")

bad_month = ([])
for i in range(0, len(profit)):
    bad_month.append(profit_after_tax[i] < mean_pat)

print(bad_month)


# best month = list([])

print("\n\n")
best_month = list([])

for i in range(0,len(profit)):
    best_month.append(profit_after_tax[i] == max(profit_after_tax))

print(best_month)

# worst month

print("\n\n")

worst_month = list([])

for i in range(0,len(profit)):
    worst_month.append(profit_after_tax[i] == min(profit_after_tax))

print(worst_month)


#convert all calculations to units of one Thousand Dollars

revenue_1000 = [round(i/1000, 2) for i in revenue]

expenses_1000 = [round(i/1000, 2) for i in expenses]

profit_1000 = [round(i/1000,2) for i in profit]

profit_after_tax_1000 = [round(i/1000, 2) for i in profit_after_tax]


revenue_1000 = [int(i) for i in revenue_1000]

expenses_1000 = [int(i) for i in expenses_1000]

profit_1000 = [int(i) for i in profit_1000]

profit_after_tax_1000 = [int(i) for i in profit_after_tax_1000]

########print every thing

print("\n\n\n")

##

print("\nRevenue :")
print(revenue_1000)

print("\nExpenses :")
print(expenses_1000)

print("\nprofit :")
print(profit_1000)

print("\nprofit after tax :")
print(profit_after_tax_1000)

print("\nprofit margin :")
print(pro_margin)

print("\nGood Months :")
print(good_month)

print("\nBad Months :")
print(bad_month)

print("\nWorst Month :")
print(worst_month)




























