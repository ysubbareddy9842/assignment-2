try:
	  hour = int (input("enter hour:"))
	  rate = int(input("enter rate"))
	  if hour <= 40:
	  	print(hour * rate)
	  elif hour > 40:
	  	print(hour * rate )+(hour - 40) * (rate * 0.5)
except:
	    print("something went wrong , kindly input numeric numbers")