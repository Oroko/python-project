# A program to prompt the user for hours and rate per hour to compute gross pay

hours = input('Enter Hours:')
hourly_rate = input('Enter Hourly Rate:')
overtime_hrs = input('Enter Overtime hours:')
regular_pay = float(hours) * float(hourly_rate)

if float(overtime_hrs)==0:
	print(regular_pay)
elif float(overtime_hrs)>0:
	print(regular_pay + (float(hourly_rate)*1.5*float(overtime_hrs) ))

print("Thank you for your work!")


