x = input('Enter a number')
try:
    y = int(x)
except:
    y= -1
if y > 0:
    print('nice work')
else :
    print('Not a number')
