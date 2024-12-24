import redis

# Set up Redis connection
r = redis.StrictRedis(host='localhost', port=6379, db=0)

def event_handler(message):
    print("Event received:", message['data'].decode())

# Subscribe to the event channel
p = r.pubsub()
p.subscribe(**{'yolo_event': event_handler})

# Listen for events
print("Waiting for events...")
p.run_in_thread(sleep_time=1)
