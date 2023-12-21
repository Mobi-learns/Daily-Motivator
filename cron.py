# from apscheduler.schedulers.background import BackgroundScheduler
# from motivator import send_whatsapp_text, client, data_dict
# import pytz
# import time
# scheduler= BackgroundScheduler(timezone=pytz.timezone("Asia/Kolkata"))
# scheduler.start()
# job = scheduler.add_job(send_whatsapp_text, 'cron',[client,data_dict['content']], hour="18",minute="54")
# print(job)

# while True:
#     time.sleep(1)

# from apscheduler.schedulers.background import BackgroundScheduler
# from motivator import send_whatsapp_text, client, data_dict
# import pytz
# import time

# scheduler = BackgroundScheduler(timezone=pytz.timezone("Asia/Kolkata"))
# scheduler.start()
# job = scheduler.add_job(send_whatsapp_text, 'interval', [client, data_dict['content']], minutes=1)
# print(job)

# while True:

#     time.sleep(1)
#modified code by shadab
from apscheduler.schedulers.background import BackgroundScheduler
from motivator import send_whatsapp_text, client, get_random_quote
import pytz
import time

scheduler = BackgroundScheduler(timezone=pytz.timezone("Asia/Kolkata"))
scheduler.start()

def scheduled_job():
    quote = get_random_quote()
    send_whatsapp_text(client, quote)

# Schedule the job to run every 1 minute
scheduler.add_job(scheduled_job, 'cron', hour=22, minute=00)

while True:
    time.sleep(1)

