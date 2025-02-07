import os
import sys
import pika
import json
import time
from dotenv import load_dotenv
from services.google_sheet_service import GoogleSheetsService
from models.clan_member import ClanMember
from models.task import Task
from constants import constants

def process_message(sheets_service, body):
    try:
        member: ClanMember = ClanMember.from_dict(json.loads(body.decode('utf-8')))
        url = sheets_service.create_sheet(member)
        print(f"Created sheet for {member.discord_display_name}: {url}")
        return True
    except Exception as e:
        print(f"Error processing clan member: {e}")
        return False

def process_task(sheets_service, body):
    try:
        data = json.loads(body.decode('utf-8'))
        sheet_url = data["sheet_url"]
        task_data = data["task"]
        task: Task = Task.from_dict(task_data)
        print(sheet_url, task_data)
        sheets_service.add_task(sheet_url, task)
        print(f" [x] Processing task: {body}")
        return True
    except Exception as e:
        print(f"Error processing task: {e}")
        return False

def main():
    load_dotenv()
    sheets_service = GoogleSheetsService() 
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='new_member')
    channel.queue_declare(queue='add_task')

    print(' [*] Starting batch processor. To exit press CTRL+C')
    
    while True:
        new_members_processed = 0
        task_processed = 0
        
        # Process new_member messages
        while new_members_processed < constants.BATCH_SIZE:
            method_frame, header_frame, body = channel.basic_get(queue='new_member', auto_ack=True)
            
            # No more messages in queue
            if not method_frame:
                break
                
            print(f" [x] Processing message: {body}")
            if process_message(sheets_service, body):
                new_members_processed += 1

        # Process add_task messages
        while task_processed < constants.BATCH_SIZE:
            method_frame, header_frame, body = channel.basic_get(queue='add_task', auto_ack=True)

            # No more messages in queue
            if not method_frame:
                break

            if process_task(sheets_service, body):
                task_processed += 1
        
        print(f" [*] Processed {new_members_processed} new_member messages.")
        print(f" [*] Processed {task_processed} add_task messages.")
        print(f" [*] Waiting for next interval...")
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