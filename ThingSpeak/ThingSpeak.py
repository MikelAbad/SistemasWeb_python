import psutil

cpuPercent = psutil.cpu_percent(interval=15)
ramPercet = psutil.virtual_memory().percent
print " CPU = " + str(cpuPercent) + "   RAM = " + str(ramPercet)