# ---
# cmd: ["python", "-m", "05_scheduling.schedule_simple"]
# ---
import time
from datetime import datetime

import modal

app = modal.App(
    "example-schedule-simple"
)  # Note: prior to April 2024, "app" was called "stub"


@app.function(schedule=modal.Period(seconds=5))
def print_time_1():
    print(
        f'Printing with period 5 seconds: {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}'
    )


@app.function(schedule=modal.Cron("* * * * *"))
def print_time_2():
    print(
        f'Printing with cron every minute: {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}'
    )


if __name__ == "__main__":
    with app.run():
        time.sleep(60)
