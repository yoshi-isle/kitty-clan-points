import os
import sys
import pika
import json
import time
from dotenv import load_dotenv
from models.submission import Submission
from constants import constants

def process_message(body):
    try:
        submission: Submission = Submission.from_dict(json.loads(body.decode('utf-8')))
        print(f"Processing request for {submission}")
        return True
    except Exception as e:
        print(f"Error processing submission: {e}")
        return False

def main():
    load_dotenv()
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='accept_submission')
    
    print(' [*] Starting batch submission processor. To exit press CTRL+C')
    
    while True:
        messages_processed = 0
        
        # Process messages
        while messages_processed < constants.BATCH_SIZE:
            method_frame, header_frame, body = channel.basic_get(queue='accept_submission', auto_ack=True)
            
            # No more messages in queue
            if not method_frame:
                break
                
            print(f" [x] Processing message: {body}")
            if process_message(body):
                messages_processed += 1
        
        print(f" [*] Processed {messages_processed} messages. Waiting for next interval...")
        time.sleep(constants.WAIT_TIME_SECONDS)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)