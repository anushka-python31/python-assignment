#wap to enter p,t,r and calculate compount interest
p=int(input("Enter principal:"))
t=int(input("Enter time:"))
r=int(input("Enter rate:"))
#claculate compount interest
interest=(p*(t+r/100)**t)
print("compount interest:",interest)