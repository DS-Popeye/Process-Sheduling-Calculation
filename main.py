

import func

gData = {'P1': [2,4], 'P2': [2,5], 'P3': [1,6], 'P4':[3,7], 'P5': [6,5], 'P6':[3,4]}
gQuant = 4
gContSwitch = 0.4

fcfsScheduling,fcfsLine = func.fcfs(gData)
sjfScheduling,sjfLine = func.sjf(gData)
srtfScheduling,srtfLine = func.srtf(gData)
rrobinScheduling,rrLine = func.rrobin(gData,gQuant)
func.printData(gData,fcfsScheduling,fcfsLine,'First Come First Serve')
func.printData(gData,sjfScheduling,sjfLine,'Shortest Job First')
func.printData(gData,srtfScheduling,srtfLine,'Shortest Remaning Time First')
func.printData(gData,rrobinScheduling,rrLine,'Round Robin QT={}'.format(gQuant))
#sum([len(x) for x in my_dict.values()]) summing to make avg answer


