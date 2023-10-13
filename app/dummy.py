import os
import time

redis_host = os.environ.get('REDIS_HOST')
redis_port = os.environ.get('REDIS_PORT')
redis_queue_name = os.environ.get('REDIS_QUEUE_NAME')

if __name__ == '__main__':
    while True:
        print(f'redis url: {redis_host}:{redis_port}/{redis_queue_name} | timestamp: {time.time()}')
        time.sleep(1.5)