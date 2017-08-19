import os


class Measurement:
    def __init__(self, value, time=None):
        self.value = value
        self.time = time

    def get_time(self):
        return self.time[16:-9]


def get_samples(file='~/Desktop/temperature_log.txt'):
    file = os.path.expanduser(file)
    measurements = []
    m = None
    with open(file) as f:
        for line in f:
            line = line.strip()
            if m is None:
                m = Measurement(value=line)
            else:
                m.time = line
                measurements.append(m)
                m = None
    return measurements
