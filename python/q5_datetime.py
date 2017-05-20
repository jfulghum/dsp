# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

d0 = date(2013, 1, 2)
d1 = date(2013, 7, 28)
delta = d0 - d1
print (delta.days)
-207

####b)  
date_start = '12312013'  
date_stop = '05282015'  
d0 = date(2013, 12, 31)
d1 = date(2015, 5, 28)
delta = d0 - d1
print(delta.days)
-513
####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
d1 = date(1994, 1, 15)
d2 = date(2015, 7, 14)
delta = d1 - d2
print(delta.days)
-7850
