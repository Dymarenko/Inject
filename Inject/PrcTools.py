import psutil
import win32api, win32con
import ctypes

def getPid(PrName, pidlist):
    for i in psutil.process_iter():
        if i.name() == PrName:
            pidlist.append(i.pid)
def ReadMem(pid, Addr):
    prc = win32api.OpenProcess(0x10, False, pid)
    buff = 0
    res = ctypes.windll.kernel32.ReadProcessMemory(prc.handle, Addr, buff, 4, 0)
    print(res, buff.value)
    print(ctypes.windll.kernel32.GetLastError())