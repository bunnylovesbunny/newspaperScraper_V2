from datetime import datetime
from scriptRun import runny

from apscheduler.schedulers.blocking import BlockingScheduler





sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(runny, 'interval', minutes = 15)

sched.start()

