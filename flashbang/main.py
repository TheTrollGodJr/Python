import tkinter as tk
import ctypes

user = ctypes.windll.user32

class RECT(ctypes.Structure):
  _fields_ = [
    ('left', ctypes.c_long),
    ('top', ctypes.c_long),
    ('right', ctypes.c_long),
    ('bottom', ctypes.c_long)
    ]
  def dump(self):
    return [int(val) for val in (self.left, self.top, self.right, self.bottom)]

class MONITORINFO(ctypes.Structure):
  _fields_ = [
    ('cbSize', ctypes.c_ulong),
    ('rcMonitor', RECT),
    ('rcWork', RECT),
    ('dwFlags', ctypes.c_ulong)
    ]

def get_monitors():
  retval = []
  CBFUNC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(RECT), ctypes.c_double)
  def cb(hMonitor, hdcMonitor, lprcMonitor, dwData):
    r = lprcMonitor.contents
    #print("cb: %s %s %s %s %s %s %s %s" % (hMonitor, type(hMonitor), hdcMonitor, type(hdcMonitor), lprcMonitor, type(lprcMonitor), dwData, type(dwData)))
    data = [hMonitor]
    data.append(r.dump())
    retval.append(data)
    return 1
  cbfunc = CBFUNC(cb)
  temp = user.EnumDisplayMonitors(0, 0, cbfunc, 0)
  #print(temp)
  return retval

def monitor_areas():
  retval = []
  monitors = get_monitors()
  for hMonitor, extents in monitors:
    data = [hMonitor]
    mi = MONITORINFO()
    mi.cbSize = ctypes.sizeof(MONITORINFO)
    mi.rcMonitor = RECT()
    mi.rcWork = RECT()
    res = user.GetMonitorInfoA(hMonitor, ctypes.byref(mi))
    data = mi.rcMonitor.dump()
#    data.append(mi.rcWork.dump())
    retval.append(data)
  return retval

monitors = monitor_areas()
print(monitors)

alpha = 255  # Initial alpha value (255 for white)

def makeApp(xChange,yChange,width,height):
    def fade_to_black():
        global alpha
        if alpha > 0:
            alpha -= 1
            root.configure(bg=f'#{"%02x" % alpha}{"%02x" % alpha}{"%02x" % alpha}')
            root.after(10, fade_to_black)
        else:
            root.destroy()

    root = tk.Tk()
    root.title("Fading White to Black")

    root.configure(bg='white')

    # Start the fading effect after a delay
    root.after(10000, fade_to_black)
    #root.attributes("-fullscreen", True)
    if xChange >= 0 and yChange >= 0:
        root.geometry(f"{width}x{height}+{xChange}+{yChange}")
    elif xChange >= 0 and yChange < 0:
        root.geometry(f"{width}x{abs(height)}+{xChange}{yChange}")
    elif xChange < 0 and yChange >= 0:
        root.geometry(f"{width}x{height}{xChange}+{yChange}")
    else:
        root.geometry(f"{width}x{height}{xChange}{yChange}")
    
    return root

for i in range(len(monitors)):
    #makeApp(monitor.x, monitor.y, monitor.width, monitor.height)
    makeApp(monitors[i][0],monitors[i][1],monitors[i][2],monitors[i][3])

tk.mainloop()