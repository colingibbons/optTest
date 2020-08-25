import time

class TimerError(Exception):
    """Oops!"""

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        if self._start_time is not None:
            raise TimerError("Timer is running. Stop it before starting a new one!")
        # starts new timer
        self._start_time = time.perf_counter()

    def stop(self):
        if self._start_time is None:
            raise TimerError("Timer is not running. Start it first!")
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print("Elapsed time: " + str(elapsed_time) + " seconds")