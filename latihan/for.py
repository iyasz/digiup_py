# Iterating over a list
# foreach 
l = ["a", "b", "c"]
for a in l:
 print(a)

 
#continue
# for letter in 'abcdef':
#  if letter == 'b' or letter == 'd':
#   continue
#   print('Current Letter without b,d :', letter)

#break
 for letter in 'abcdef':
  if letter == 'd':
   break
 print('Current Letter before break :', letter)
 
#pass
 for letter in 'abcdef':
  pass
 print('last letter', letter)