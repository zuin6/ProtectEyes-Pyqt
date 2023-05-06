"""
Get and set the brightness of the monitor.
"""

import ctypes
from ctypes import wintypes

PHYSICAL_MONITOR_DESCRIPTION_SIZE = 128


class PHYSICAL_MONITOR(ctypes.Structure):
    _fields_ = [('hPhysicalMonitor', wintypes.HANDLE),
                ('szPhysicalMonitorDescription', ctypes.c_wchar * PHYSICAL_MONITOR_DESCRIPTION_SIZE)]
'''
原文：https://zhuanlan.zhihu.com/p/110146413
'''
def setBrightness(num: int):
    user32 = ctypes.windll.user32
    h_wnd = user32.GetDesktopWindow()
    MONITOR_DEFAULTTOPRIMARY = 1
    h_monitor = user32.MonitorFromWindow(h_wnd, MONITOR_DEFAULTTOPRIMARY)
    # print('Monitor Handle', h_monitor)

    dxva2 = ctypes.windll.Dxva2
    nummons = wintypes.DWORD()
    bres = dxva2.GetNumberOfPhysicalMonitorsFromHMONITOR(
        h_monitor, ctypes.byref(nummons))
    assert bres
    # print('Number of Monitors', nummons)

    physical_monitors = (PHYSICAL_MONITOR * nummons.value)()
    bres = dxva2.GetPhysicalMonitorsFromHMONITOR(
        h_monitor, nummons, physical_monitors)
    assert bres
    # print('Phyical Monitors', physical_monitors)
    physical_monitor = physical_monitors[0]
    # print('    first', physical_monitor.hPhysicalMonitor,
    #       physical_monitor.szPhysicalMonitorDescription)

    min_brightness = wintypes.DWORD()
    max_brightness = wintypes.DWORD()
    cur_brightness = wintypes.DWORD()

    bres = dxva2.GetMonitorBrightness(physical_monitor.hPhysicalMonitor, ctypes.byref(
        min_brightness), ctypes.byref(cur_brightness), ctypes.byref(max_brightness))
    assert bres
    # print('Brightness', min_brightness, 'min',
    #       cur_brightness, 'max', max_brightness)

    bres = dxva2.SetMonitorBrightness(physical_monitor.hPhysicalMonitor, num)
    assert bres

    kernel32 = ctypes.windll.kernel32
    err = kernel32.GetLastError()
