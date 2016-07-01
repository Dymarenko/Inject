import PrcTools
import adresses

PIDLIST = []
PrcTools.getPid('elementclient.exe', PIDLIST)
print(PrcTools.ReadMem(PIDLIST[0], adresses.BaseAddr))