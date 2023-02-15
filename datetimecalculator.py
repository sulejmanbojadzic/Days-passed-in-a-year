date=input("Input a date after 15.10.1582 in dd.mm.yyyy format :")
isleap=False
year=int(date[-4:])
month=int(date[3:5])
day=int(date[0:2])
dateordinalnumbercounter=0

if year%100==0 and year%400==0: #We check if year is a leap year
    isleap=True
elif year%4==0:
    isleap=True
else:
    isleap=False

for i in range(1,month+1): #We loop trough the amount of months
    j=0
    if i==month:
        j=day
    elif i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
        j=31
    elif i==2 and isleap :
        j=29
    elif i==2:
        j=28
    else:
        j=30
    for days in range(1,j+1): #And then trough amount of days in each month and last month
        dateordinalnumbercounter+=1
print(dateordinalnumbercounter)


