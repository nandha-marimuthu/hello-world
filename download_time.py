
t=int(input('Enter the size: '))
s=str(input('KB or MB '))
i=int(input('Enter the internet speed in Kb/s: '))
if s=='MB' :
    t=t*1024
    time_taken=t/i
    mins=time_taken/60
    print('time_taken= ',mins,'mins')
else:
    time_taken=t/i
    if time_taken>60:
        mins=time_taken/60
        print('time_taken= ',mins,'mins')
    else:
        print('time_taken= ',time_taken,'secs')