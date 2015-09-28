fib1 =0
fib2 =1
counter = fib1 + fib2
total =0

while(counter < 4000000):
  if counter % 2 ==0:
    total += counter

  fib1 = fib2
  fib2 = counter
  counter = fib1 + fib2

print 'the sum of fibonacci even value up to 4 million is: ', total