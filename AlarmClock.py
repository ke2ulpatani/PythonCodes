import datetime as dt
import os

def getMinHour(datatime):
    hh = datatime[:2]
    mm = datatime[2:]
    return (hh,mm)

if __name__ == "__main__":
    time = raw_input("Enter the time(hhmm):\t")
    #choice = raw_input("Enter your OS:\n1.MacOS\n2.Linux")
    time = getMinHour(str(time))
    alarm = dt.datetime.now().replace(hour=int(float(time[0])), minute=int(float(time[1])), second=0, microsecond=0)


    while 1:
        now = dt.datetime.now()
        if (now <= alarm):
            if (now == alarm):
                while 1:
                    os.system("say 'Wake up its time to get up'")
