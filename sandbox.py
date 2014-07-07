#! usr/bin/env python
periods = 2
days = 31

if periods==1:
    print '1 Period'
    for i in range(1,days+1):
        print 'Day '+str(i)
else:
    print '2 Periods'
    p1=days/periods
    p2=days-p1
    print 'period 1'
    for i in range(1,p1+1):
        print 'Day '+str(i)
    print 'period 2'
    for i in range(1,p2+1):
        print 'Day '+str(i)