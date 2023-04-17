import plotting
import time
from datetime import datetime
import old_functions

pts = []
plc = []
dts = []

#for i in range(10):
while 1:
    d = old_functions.get_clan_output("KANHNI")#gets current clan stats
    pts.append(d[2])#points
    plc.append(d[0])#place
    dts.append(datetime.now().strftime("%d-%m-%y\n%H:%M"))#date and time
    plotting.plot(pts, plc, dts)
    if len(pts) > 10:
        del pts[0]
    if len(plc) > 10:
        del plc[0]
    if len(dts) > 10:
        del dts[0]
    time.sleep(1)