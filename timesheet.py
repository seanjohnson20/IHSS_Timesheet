__author__ = 'QA'
import datetime
now = datetime.datetime.now()

# values collected from user
h = int(raw_input('How many hours(eg. 95): '))
m = int(raw_input('How many minutes(eg. 56): '))
d = int(raw_input('How many days in month(eg. 31): '))
name = raw_input('Name this file: ')

#calculated / assumed values
p1 = d/2
p2 = d-p1
tm = h*60 + 56
min_per_day_p1 = (tm/2)/p1
min_per_day_p2 = (tm/2)/p2

file = open( name+".txt", "a+")

print 'Created on: ', now.strftime("%Y-%m-%d %H:%M")
file.write('Created: '+ str(now.strftime("%Y-%m-%d %H:%M"))+'\n')

print 'Hours/Minutes in Month: '+str(h)+':'+str(m)
file.write('Hours/Minutes in Month: '+str(h)+':'+str(m)+'\n')

print 'Days in Month: '+str(d)
file.write('Days in Month: '+str(d)+'\n')
print ' '
file.write('\n')

# Period 1
hpd_p1 = min_per_day_p1/60
mpd_p1 = min_per_day_p1%60
p1m = tm/2
print ' '
print ' --- First Period --- '
file.write(' --- First Period --- \n')
print 'Days in First Period: ', p1
file.write('Days in First Period: '+str(p1)+'\n')
print 'Minutes in First Period: ', min_per_day_p1
file.write('Minutes in First Period: '+str(min_per_day_p1)+'\n')
print ' '
for i in range(1,p1+1):
    if p1m>(2*(min_per_day_p1)):
        p1m = p1m-(hpd_p1*60)-mpd_p1
        print 'Day '+str(i)+' - '+str(hpd_p1)+':'+str(mpd_p1)
        file.write('Day '+str(i)+' - '+str(hpd_p1)+':'+str(mpd_p1)+'\n')

    else:
        p1m = p1m-(hpd_p1*60)-mpd_p1
        last_min=mpd_p1+p1m
        if last_min>60:
            hpd_p1+=1
            last_min=last_min-60
        print 'Day '+str(i)+' - '+str(hpd_p1)+':'+str(last_min)
        file.write('Day '+str(i)+' - '+str(hpd_p1)+':'+str(last_min)+'\n')
        print ' '

# Period 2
hpd_p2 = min_per_day_p2/60
mpd_p2 = min_per_day_p2%60
p2m = tm/2
print ' '
file.write('\n')
print ' --- Second Period --- '
file.write(' --- Second Period --- \n')
print 'Days in Second Period: ', p2
file.write('Days in Second Period: '+str(p2)+'\n')
print 'Minutes in Second Period: ',min_per_day_p2
file.write('Minutes in Second Period: '+str(min_per_day_p2)+'\n')
print ' '
file.write('\n')
for i in range(1,p2+1):
    if p2m>(2*(min_per_day_p2)):
        p2m = p2m-(hpd_p2*60)-mpd_p2
        print 'Day '+str(i)+' - '+str(hpd_p2)+':'+str(mpd_p2)
        file.write('Day '+str(i)+' - '+str(hpd_p2)+':'+str(mpd_p2)+'\n')
    else:
        p2m = p2m-(hpd_p2*60)-mpd_p2
        last_min=mpd_p2+p2m
        if last_min>60:
            hpd_p2+=1
            last_min=last_min-60
        print 'Day '+str(i)+' - '+str(hpd_p2)+':'+str(last_min)
        file.write('Day '+str(i)+' - '+str(hpd_p2)+':'+str(last_min)+'\n')
        print ' '
        file.write('\n')

file.close()

'-----------------------------------'
def main():
    pass
if __name__ == '__main__':
    main()


    #  Use import py_compile
    #       py_compile.compile('timesheet.py') to create pyc