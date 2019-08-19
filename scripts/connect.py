#!/usr/bin/env python
# /etc/init.d/connect.py
### BEGIN INIT INFO
# Provides:          connect.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

import datetime
import time
import os
##from Hologram.HologramCloud import HologramCloud
time.sleep(10)

datetoday = datetime.datetime.now()

#open connection
##hologram = HologramCloud(dict(), network='cellular')
result = os.system("sudo hologram network connect")

file = open('/home/pi/Documents/connect.txt','w') 

file.write('Connect.')
file.write(' Today is:\n')
file.write(str(datetoday))
file.write('\n')
file.write(str(result))

file.close()
