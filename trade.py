import time
from iqoptionapi.stable_api import IQ_Option
iqEmail = "your iq options email"
iqPass = "your iq options pass"
iqo=IQ_Option(iqEmail,iqPass)
iqo.connect()#connect to iqoption
profit = 0.0
loss = 0
cntr = 0
mode = "PRACTICE"
#mode = "REAL"
iqo.change_balance(mode)
balance = (iqo.get_balance())
currency = (iqo.get_currency())
print("Balance : " + str(balance))
market = "EURUSD"
amount=1
dur = 1
act = "put"

while True:
	pps,ids = iqo.buy_digital_spot(market,amount,act,dur)
	print "trade started wait for 60 seconds"
	if ids!="error":
		while True:
			check,win = iqo.check_win_digital_v2(ids)
			if check == True:
				break
		if win<0:
			loss = loss + 1
			print("lost")
			if act == "put":
				act = "call"
			else:
				act = "put"
		else:
			print("win")
			profit = profit + win

		if cntr == 10:
			print("--------------")
			print("")
			print("")
			print("profit : "+ str(profit)+"      loss : "+str(loss))
			print("")
			print("")
			print("--------------")
			cntr = 0
		else:
			cntr = cntr + 1

		time.sleep(10)


