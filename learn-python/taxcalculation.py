print ("\n")
print ("--------------Tax Calculation---------------")
print ("\n")

meal = 44.50
tax = 0.0675
tip = 0.15

tax = meal * tax	# Calculate Tax
meal = meal + tax	
tip = meal * tip	# Calculate Tip

total = meal + tip	# Calculate Total =

#print("meal price:", total)
print("meal price:", "%.2f" % total)
#print("%.2f" % total)

