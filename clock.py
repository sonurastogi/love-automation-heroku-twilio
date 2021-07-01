from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from honey_love import send_love


#def job_function():
#    print("Hello World")

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
#sched.add_job(job_function, 'interval', hours=2)
#sched.add_job(job_function, 'interval', seconds=10)
#sched.add_job(send_love, 'interval', seconds=10)
sched.add_job(send_love, 'interval', seconds=60)

sched.start()