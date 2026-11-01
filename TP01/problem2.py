#Problem 2. Time Converter

total_seconds = 9875
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
sec = total_seconds % 60

print("\n",total_seconds, "seconds = ", hours, 'h', minutes, 'min', sec, ' s')
#check
print("Check: ", 2*3600 + 44 * 60 + 35 == total_seconds) # == check boolean value`

#Test your code with 3600, 59 and 86399 seconds. 

total_seconds = 3600
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
sec = total_seconds % 60

print("\n",total_seconds, "seconds = ", hours, 'h', minutes, 'min', sec, ' s')
#check
print("Check: ", 1*3600 + 0 * 60 + 0 == total_seconds) # == check boolean value`

total_seconds = 59
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
sec = total_seconds % 60

print("\n",total_seconds, "seconds = ", hours, 'h', minutes, 'min', sec, ' s')
#check

print("Check: ", 0*3600 + 0 * 60 + 59 == total_seconds) # == check boolean value`
total_seconds = 86399
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
sec = total_seconds % 60

print("\n",total_seconds, "seconds = ", hours, 'h', minutes, 'min', sec, ' s')
#check
print("Check: ", 24*3600 - 1 == total_seconds) # == check boolean value`