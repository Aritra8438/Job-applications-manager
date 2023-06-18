from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from Job_applications.utils import send_email

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    register_events(scheduler)
    
    
    @scheduler.scheduled_job('interval', seconds=3, name='auto_hello')
    def auto_hello():
        send_email()

    scheduler.start()