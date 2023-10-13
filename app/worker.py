from redis import Redis
from rq import Worker, Queue
import os

redis_host = os.environ.get('REDIS_HOST')
redis_port = os.environ.get('REDIS_PORT')
redis_queue_name = os.environ.get('REDIS_QUEUE_NAME')

redis_conn = Redis(host=redis_host, port=int(redis_port))
tq = Queue(name=redis_queue_name, connection=redis_conn)


if __name__ == '__main__':
    w = Worker([tq], connection=redis_conn)
    w.work()
