inp = raw_input('Enter something to check for palindrome: ')

rev=reversed (inp)

if list (inp) == list(rev):
  print 'true'
else:
  print 'false'


