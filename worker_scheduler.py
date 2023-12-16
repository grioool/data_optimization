import numpy as np


class WorkerScheduler:
    def __init__(self, year):
        self.year = year
        self.days_in_year = 366 if self.is_leap_year() else 365
        self.daily_staff = np.array([31, 45, 31, 45, 31, 45, 31])
        self.cycle_days = 18 + 10

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def calculate_minimum_workers(self):
        workers_per_day = np.zeros(self.days_in_year, dtype=int)

        worker_id = 0
        while True:
            for _ in range(3):
                for day in range(6):
                    workers_per_day[worker_id:worker_id + 6] += 1
                worker_id += 6

            worker_id += (self.cycle_days - 18)

            if np.all(np.bincount(np.arange(self.days_in_year) % 7, weights=workers_per_day) >= self.daily_staff):
                break

        return np.max(np.nonzero(workers_per_day)) + 1
