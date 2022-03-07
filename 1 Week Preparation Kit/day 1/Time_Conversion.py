"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
"""

def timeConversion(s):
	# Write your code here
	hour = s[:-2]
	am_pm = s[-2:]
	hour, minute, sec = hour.split(':')

	if am_pm == 'PM' and hour != '12':
		hour = str(int(hour) + 12)
	if am_pm == 'PM' and hour == '12':
		hour = '12'
	if am_pm == 'AM' and hour == '12':
		hour = '00'

	return ('%s:%s:%s' % (hour, minute, sec))