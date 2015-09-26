count = 0
total = 0

for i in range(0,1000):
  if i % 3 == 0 or i % 5 == 0:
      count += i
      print i

total = count
print 'The sum of multiple 3 and 5 is ',total