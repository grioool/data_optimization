from worker_scheduler import WorkerScheduler

scheduler = WorkerScheduler(2024)
min_workers_needed = scheduler.calculate_minimum_workers()
print(f"Minimum number of workers needed in {scheduler.year}: {min_workers_needed}")
