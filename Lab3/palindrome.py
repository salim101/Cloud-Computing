# take an input from the user
inp = raw_input('Enter something to check for palindrome: ')

#use the built in reversed function in python
rev=reversed (inp)

#if statement to check the input for palindrome
if list (inp) == list(rev):
  print 'true' #if it matches print true
else: # otherwise print false
  print 'false'


