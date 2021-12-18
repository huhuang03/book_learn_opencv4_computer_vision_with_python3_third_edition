import cv2

from .managers import WindowManager, CaptureManager


class Cameo:
    def __init__(self):
        self._windowManager = WindowManager()
        self._captureManager = CaptureManager(
            cv2.VideoCapture(0), self._windowManager, True
        )

        def run():
            self._windowManager.createWindow()
            while self._windowManager.isWindowCreated:
                self._captureManager.enterFrame()
                frame = self._captureManager.frame
                if frame is not None:
                    pass
                self._captureManager.exitFrame()
                self._windowManager.processEvent()