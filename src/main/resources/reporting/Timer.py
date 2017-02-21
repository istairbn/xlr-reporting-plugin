#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import time
now = time.time()

try:
    print(then)
    print("Time given")
except NameError:
    then = None

if then is not None:
    thenFloat = float(then)
    diffsecs = now - thenFloat
    roundSecs = int(round(diffsecs))
    totalTime = roundSecs
    hours = int(totalTime / 3600.0)
    minutes = int((totalTime - (hours * 3600.0)) / 60.0)
    seconds = int(((totalTime) - (hours * 3600) - (minutes * 60)))
    duration = "%d hours, %d minutes, and %d seconds." % (hours, minutes, seconds)
    secondsString = str(roundSecs)
    print(duration)
    print("Seconds="+secondsString)
else:
    print("No time given")
nowString = str(now)
print("Time="+nowString)
