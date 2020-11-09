#Exercise 2.2, problem 3 (extra credit) - Richa Bavadekar

#This program prints out the time at which it 5 miles at specific times will be done running, given a user inputted
#start time
starting_hour = eval(input("Enter starting hour: "))
starting_minute = eval(input("Enter starting minute: "))
total_minutes_ran = 7 * 3 + 8 * 2
total_seconds_ran = 12 * 3 + 15 * 2
ending_hour = starting_hour + (starting_minute + total_minutes_ran) / 60
ending_minute = (starting_minute + total_minutes_ran) % 60 + total_seconds_ran / 60
print("You will finish at", round(ending_hour),":",round(ending_minute))

#Recording of the output
'''
Enter starting hour: 7
Enter starting minute: 52
You will finish at  8 : 30
'''
