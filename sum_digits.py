def sum_digits(l):
      l = input()
      sum = 0 
      for digit in str(l):
           sum += int(digit)
      return sum 
print(sum_digits(sum))