'''
Goal: code a program which prompts the user for a number of days
Then for each day, the user enters the temperature of that day
Finally, calcuates the average temperature and number of days which are above the average temp
'''

days = int(input('Enter number of days: '))

temperatures = []
for day in range(1,days+1):
    temperatures.append(int(input(f"Enter the highest temp for day {day}: ")))

avg = sum(temperatures)/len(temperatures)
print(f'Average {days} day temperature = {avg}')
print(f'Days above average = {sum([1 for i in temperatures if i > avg])}')    