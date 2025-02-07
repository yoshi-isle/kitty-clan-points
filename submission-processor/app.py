from datetime import datetime
import os
import sys
import pika
import json
import time
from bson import ObjectId
from dotenv import load_dotenv
from models.submission import Submission
from models.task import Task
from constants import constants
from database import Database

def process_message(body, db: Database):
    try:
        submission: Submission = Submission.from_dict(json.loads(body.decode('utf-8')))
        print(f"Processing request for {submission}")
        
        # Soft-delete the submission record
        db.submissions_collection.find_one_and_update(
            {
                "_id": ObjectId(submission._id),
                "is_active": True
            },
            {
                "$set": {
                    "is_active": False
                }
            }
        )
        
        print(submission.task)
        
        # Convert the submission into a task
        completed_task = Task(
            is_active=True,
            task_name=submission.task["name"],
            task_id=submission.task["task_id"],
            point_value=submission.task["points_awarded"],
            image_url=submission.image_url,
            achieved_on=datetime.now(),
            approved_by=submission.approved_by
            )
        
        # Append the completed task
        member = db.members_collection.find_one_and_update(
            {
                "discord_id": submission.discord_id,
                "is_active": True
            },
            {
                "$push": {"task_history": completed_task.to_dict()}
            },
                return_document=True
        )
        
        # Send out request to update user's google sheet
        connection = pika.BlockingConnection(pika.ConnectionParameters(os.getenv('RABBITMQ_CONNECTION_STRING')))
        channel = connection.channel()
        channel.queue_declare(queue='add_task')
        channel.basic_publish(exchange='', routing_key='add_task', body=json.dumps(
            {
                "sheet_url": member["google_sheet_url"],
                "task": completed_task.to_dict()
            },
            default=str).encode("utf-8"))
        
        channel.close()
        return True
    
    except Exception as e:
        print(f"Error processing submission: {e}")
        return False

def main():
    load_dotenv()
    db = Database()
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
            if process_message(body, db):
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