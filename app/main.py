import time
import os
import logging
from redis import Redis
from rq import Queue
from rq.registry import FinishedJobRegistry, FailedJobRegistry, CanceledJobRegistry, ScheduledJobRegistry, StartedJobRegistry
from rq.job import Job

from proccess import do_something, handle_ok, handle_fail, handle_stop

redis_host = os.environ.get('REDIS_HOST')
redis_port = os.environ.get('REDIS_PORT')
redis_queue_name = os.environ.get('REDIS_QUEUE_NAME')

log_name = '/tmp/app.log'

logging.basicConfig(filename=log_name, encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s')
logging.info("Staring the app...")

redis_conn = Redis(host=redis_host, port=redis_port)
tq = Queue(connection=redis_conn, name=redis_queue_name)

fail_registry = FailedJobRegistry(queue=tq)
ok_registry = FinishedJobRegistry(queue=tq)
cancel_registry = CanceledJobRegistry(queue=tq)
sched_registry = ScheduledJobRegistry(queue=tq)
start_registry = StartedJobRegistry(queue=tq)


def add_jobs():
    _jobs = [Queue.prepare_data(do_something,
                                (x,),
                                on_success=handle_ok,
                                on_failure=handle_fail,
                                on_stopped=handle_stop,
                                job_id=f'id-{x}') for x in range(5)]

    return tq.enqueue_many(_jobs)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # os.system('java Main')
    jobs = add_jobs()
    while True:
        # This simulated polling
        ts = time.time()
        print(f'heart beat: {ts}')

        for job_id in start_registry.get_job_ids():
            print(f'Scheduled job ID: {job_id} | ')

        for job_id in ok_registry.get_job_ids():
            job = Job.fetch(job_id, connection=redis_conn)
            print(f'OK\'d job ID: {job_id}')
            print(f'OK job value: {job.return_value()}')
            ok_registry.remove(job)
            print('=' * 80)
        time.sleep(1)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
