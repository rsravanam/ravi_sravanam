words = ['cat', 'window', 'defenestrate']
for w in words:
  print (w, len(w), w.upper(), w.lower())

print ("...........................")
for w in words[:]:
  if len(w) > 6:
    words.insert(0, w)
    print (words)

print (".............The range() Function.............")
for i in range(5):
  print (i)
print ("...........................")  
for i in range(0, 5):
  print (i)
print ("...........................")  
for i in range(0, 115, 13): # table 13, between 0  and 115
  print (i)
print ("...........................") 
for i in range(-10, -100, -20):
  print (i)
  
print (".............combine range() and len().............")
in_names = ['Mary', 'had', 'a', 'little', 'lamb']
for name in range(len(in_names)):
  print (name, in_names[name],"\n")

print(range(10))
print ( list(range(10)) ) 

print("---break and continue Statements, and else Clauses on Loops---")

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		# loop fell through without finding a factor
		print(n, 'is a prime number')
		
print ("----------find even number----------")

for en in range(0, 10):
	if en % 2 == 0:
		print ("Found", en , "as even")
	else:
		print ("Found", en)