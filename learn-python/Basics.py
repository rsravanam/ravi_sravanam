
print ("-------------Variable declaration----------------")
print ("\n")
#!/usr/bin/python

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print ( "An integer assignment ; counter =", counter)
print ( "A floating point; miles =", miles)
print ( "A string; name =", name)

print ("\n")
print (">>>>>>>> Explicit String Conversion<<<<<<<<")
print ("The value of pi is around  str(3.14)", str(3.14) )

print ("\n")

print('C:\some\name') # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

 # 3 times 'un', followed by 'ium'
print ( 3 * '1_' + 'ium' )
#Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
print ('Py' 'thon')

text = ('Put several strings within parentheses '
        'to have them joined'
		'together.')
print (text)