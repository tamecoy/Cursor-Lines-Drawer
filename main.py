import win32gui
import win32api
import win32con
from pynput.mouse import Listener


def draw_cursor_lines(x, y):
    desktop_hwnd = win32gui.GetDesktopWindow()
    desktop_dc = win32gui.GetWindowDC(desktop_hwnd)
    pen = win32gui.CreatePen(win32con.PS_SOLID, 1, win32api.RGB(255, 0, 0))
    win32gui.SelectObject(desktop_dc, pen)
    win32gui.MoveToEx(desktop_dc, x, 0)
    win32gui.LineTo(
        desktop_dc, x, win32api.GetSystemMetrics(win32con.SM_CYSCREEN))
    win32gui.MoveToEx(desktop_dc, 0, y)
    win32gui.LineTo(desktop_dc, win32api.GetSystemMetrics(
        win32con.SM_CXSCREEN), y)
    win32gui.DeleteObject(pen)
    win32gui.ReleaseDC(desktop_hwnd, desktop_dc)


def erase_cursor_lines():
    desktop_hwnd = win32gui.GetDesktopWindow()
    desktop_dc = win32gui.GetWindowDC(desktop_hwnd)
    win32gui.InvalidateRect(desktop_hwnd, None, True)
    win32gui.ReleaseDC(desktop_hwnd, desktop_dc)


def on_click(x, y, button, pressed):
    if pressed:
        draw_cursor_lines(x, y)
    else:
        erase_cursor_lines()


if __name__ == "__main__":
    with Listener(on_click=on_click) as listener:
        listener.join()
