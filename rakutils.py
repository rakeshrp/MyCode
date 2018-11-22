'''Round integers , both negative and positive
'''
def roundd(a):
   if a < 0:
     sign= -1
   else:
     sign = 1
   a = abs(a)
   temp = a + 0.5
   if temp > int(a) + 1.0:
      return sign * int(temp)
   else:
      return sign* int(a)

'''Sum of digits in a number
'''

def sum_digits(num):
   sum = 0
   while num > 1:
      num = num / 10
      quo = int(num)
      rem = roundd((num - quo)*10)
      sum = sum + rem
      num = quo
   sum = sum + num
   return sum


'''Sort a input list of numbers
   input : unsorted list of numbers
   output : sorted list
'''

def sorted_list(l):
   for k in (range(len(l))):
     for i in range(len(l) -1):
        if l[i] > l[i+1]:
           l[i] , l[i+1] = l[i+1] , l[i]
   return(l)


'''median element in a list of numbers
'''
def mediann(l):
   if len(l)/2 > int(len(l)/2):
      # odd
      return (l[int(len(l)/2)])
   else:
      return (l[int(len(l)/2)] + l[int(len(l)/2)-1])/2
