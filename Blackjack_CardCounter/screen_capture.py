"""Screen capture utilities."""
import mss
import mss.tools


def capture_screen(monitor_number: int = 1) -> bytes:
    """Capture a screenshot of the selected monitor and return PNG bytes."""
    with mss.mss() as sct:
        monitor = sct.monitors[monitor_number]
        img = sct.grab(monitor)
        return mss.tools.to_png(img.rgb, img.size)
