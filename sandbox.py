#! usr/bin/env python

h = 95
m = 55
d = 31
ttl_min = h * 60 + m
periods = 2.0

min_in_period = ttl_min/periods

d_p1=15
min_in_p1 = min_in_period
min_per_day_p1 = min_in_p1/d_p1


hpd_p1 = min_per_day_p1/60
mpd_p1 = min_per_day_p1%60

print 'Total Min: ' + str(ttl_min)
print 'Min in p1: ' + str(min_in_p1)

# print 'min_in_p1/d_p1: ' + str(int(min_in_p1/d_p1))
# print 'min_in_p1%d_p1: '+ str(int(min_in_p1%d_p1))

print 'Min per day p1: ' + str(min_per_day_p1)
print 'hpd_p1: ' + str(int(hpd_p1))
print 'mpd_p1: ' + str(int(mpd_p1))



# if periods==1:
#     print '1 Period'
#     for i in range(1,days+1):
#         print 'Day '+str(i)
# else:
#     print '2 Periods'
#     p1=days/periods
#     p2=days-p1
#     print 'period 1'
#     for i in range(1,p1+1):
#         print 'Day '+str(i)
#     print 'period 2'
#     for i in range(1,p2+1):
#         print 'Day '+str(i)