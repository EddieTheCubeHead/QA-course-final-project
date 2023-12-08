import datetime


class Timer:

    def __init__(self):
        self._start_time: datetime.datetime | None = None
        self._stopwatch: datetime.timedelta | None = None

    def __enter__(self):
        self._start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._stop()

    def _start(self):
        self._start_time = datetime.datetime.now()

    def _stop(self):
        if self._start_time is None:
            raise Exception("Cannot stop a timer that has not been started!")
        self._stopwatch = datetime.datetime.now() - self._start_time
        self._start_time = None

    def __lt__(self, other: datetime.timedelta):
        self._assert_used()
        return self._stopwatch < other

    def __le__(self, other: datetime.timedelta):
        self._assert_used()
        return self._stopwatch <= other

    def __eq__(self, other: datetime.timedelta):
        self._assert_used()
        return self._stopwatch == other

    def _assert_used(self):
        if self._stopwatch is None:
            raise Exception("Tried to get timer time before using the timer!")
