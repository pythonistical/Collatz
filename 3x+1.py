odd = 0
even = 0
current_number = 2
process = 0
while process < 30000:
      process += 1
      if current_number % 2 == 0:
         even_div = current_number/2
         if even_div == 1:
            current_number += 1
            process = 0
            print(f"Currently working on {current_number}")
      else:
          odd_mul = (current_number*3) + 1
print(f'Number {current_number} has been in 3x+1 cycle for more than 30000 times, there is a high chance it might string to infinity')

