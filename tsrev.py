#!/usr/bin/env python
import datetime
now = datetime.datetime.now()
name = raw_input('What name do you want to give your text file: ')
file = open(name+".txt", "a+")
print ' -- Name of File: ', name+'.txt -- '
def calculate():
    # values collected from user
    h = int(raw_input('How many ttl hours in calculation ( eg. 95): '))
    m = int(raw_input('How many ttl minutes in calculation ( eg. 56): '))
    np = int(raw_input('How many periods in calculation ( eg. 1 or 2): '))
    d = int(raw_input('How many days in calculation ( eg. 15, 28, 31): '))

    for i in range(1,np+1):
        if np<1 or np>2:
            print "Please choose 1 or 2 periods."
            calculate()
        elif np==1:
            #calculated / assumed values
            p1 = d
            totalMinutes = h*60 + m
            minutesPerDay = totalMinutes/p1
            hpd = minutesPerDay/60
            mpd = minutesPerDay%60
            minutesInPeriod = totalMinutes

            print ' --- '
            print 'Days in Period: ', p1
            print 'Minutes in Period: ', totalMinutes
            print ' '
            for i in range(1,p1+1):
                if minutesInPeriod>(2*(minutesPerDay)):
                    minutesInPeriod = minutesInPeriod-(hpd*60)-mpd
                    print 'Day '+str(i)+' - '+str(hpd)+':'+str({'%.2f'}.format(mpd))
                    print ' '
                else:
                    minutesInPeriod = minutesInPeriod-(hpd*60)-mpd
                    last_min=mpd+minutesInPeriod
                    if last_min>60:
                        hpd+=1
                        last_min=last_min-60
                    print 'Day '+str(i)+' - '+str(hpd)+':'+str(last_min)
                    print ' '
        else:
            # 2 periods -- calculated / assumed values
            p1=15
            p2 = d-p1
            if d<16:
                p1=d/2
                p2=d-p1

            print 'p1: ', p1
            print 'p2: ', p2
            totalMinutes = h*60 + m
            print 'totalMinutes: ', totalMinutes
            minutesInPeriod_p1 = totalMinutes/2
            minutesInPeriod_p2 = totalMinutes/2
            minutesPerDay_p1 = minutesInPeriod_p1/p1
            minutesPerDay_p2 = minutesInPeriod_p2/p2
            hpd_p1 = minutesPerDay_p1/60
            mpd_p1 = minutesPerDay_p1%60
            hpd_p2 = minutesPerDay_p2/60
            mpd_p2 = minutesPerDay_p2%60

            print ' --- '
            print 'Days in Period 1: ', p1
            print 'Minutes in Period 1: ', minutesInPeriod_p1
            print ' '
            for i in range(1,p1+1):
                if minutesInPeriod_p1>(2*(minutesPerDay_p1)):
                    minutesInPeriod_p1 = minutesInPeriod_p1-(hpd_p1*60)-mpd_p1
                    print 'Day '+str(i)+' - '+str(hpd_p1)+':'+str(mpd_p1)
                    print ' '
                else:
                    minutesInPeriod_p1 = minutesInPeriod_p1-(hpd_p1*60)-mpd_p1
                    last_min=mpd_p1+minutesInPeriod_p1
                    if last_min>60:
                        hpd_p1+=1
                        last_min=last_min-60
                    print 'Day '+str(i)+' - '+str(hpd_p1)+':'+str(last_min)
                    print ' '
            print ' --- '
            print 'Days in Period 2: ', p2
            print 'Minutes in Period 2: ', minutesInPeriod_p2
            print ' '
            for i in range(1,p2+1):
                if minutesInPeriod_p2>(1.5*(minutesPerDay_p2)):
                    minutesInPeriod_p2 = minutesInPeriod_p2-(hpd_p2*60)-mpd_p2
                    print 'Day '+str(i)+' - '+str(hpd_p2)+':'+str(mpd_p2)
                    print 'Subtracting', minutesPerDay_p2, ' leaves', minutesInPeriod_p2, ' min left in p2'
                    print 'hpd_p2: ', hpd_p2
                    print 'mpd_pd: ', mpd_p2
                    print ' '
                else:
                    minutesInPeriod_p2 = minutesInPeriod_p2-(hpd_p2*60)-mpd_p2
                    last_min=mpd_p2+minutesInPeriod_p2
                    if last_min>60:
                        hpd_p2+=1
                        last_min=last_min-60
                    print 'Day '+str(i)+' - '+str(hpd_p2)+':'+str(last_min)
                    print ' '
    print 'the end'

calculate()

file.close()

'-----------------------------------'
def main():
    pass
if __name__ == '__main__':
    main()


    #  import py_compile
    #  py_compile.compile('timesheet.py') to create pyc