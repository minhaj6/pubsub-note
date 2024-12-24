import redis
import time

# Set up Redis connection
r = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
    detected = True  # Replace with actual detection logic
    if detected:
        r.publish('yolo_event', "Object detected at {}".format(time.time()))
        print("Event published to Redis.")
    
    time.sleep(1)

