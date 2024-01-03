current_number = 2
num = 2
process = 0
stopwatch = eval(input('What is your limit?\t'))
limiter = 0
while process <= 30000 and limiter == 0:
      if num >= stopwatch:
         limiter = 1
      process += 1
      if current_number % 2 == 0:
         even_div = current_number/2
         current_number = current_number/2
         if even_div == 1:
            num += 1
            current_number = num
            process = 0
            print(f"Currently working on {current_number}")
      else:
          current_number = (current_number*3) + 1
if limiter == 0:
   print(f'Number {num} has been in 3x+1 cycle for more than 30000 times, there is a high chance it might string to infinity')

