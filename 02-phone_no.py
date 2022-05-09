# after installing phonenumbers module

import phonenumbers
from phonenumbers import timezone,geocoder,carrier
n=input('Enter the number with country code : ')
p=phonenumbers.parse(n) # parse is a command for dividing the given program code 
# into a small piece of code for analyzing the correct syntax
t=timezone.time_zones_for_number(p)
g=geocoder.description_for_number(p,'en')
c=carrier.name_for_number(p,'en')
print(p,t,g,c)


