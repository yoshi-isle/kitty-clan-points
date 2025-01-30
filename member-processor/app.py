import os
import sys
import pika
import json
import time
from dotenv import load_dotenv
from services.google_sheet_service import GoogleSheetsService
from models.clan_member import ClanMember
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

def main():
    load_dotenv()
    sheets_service = GoogleSheetsService() 
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='new_member')
    
    print(' [*] Starting batch processor. To exit press CTRL+C')
    
    while True:
        messages_processed = 0
        
        # Process messages
        while messages_processed < constants.BATCH_SIZE:
            method_frame, header_frame, body = channel.basic_get(queue='new_member', auto_ack=True)
            
            # No more messages in queue
            if not method_frame:
                break
                
            print(f" [x] Processing message: {body}")
            if process_message(sheets_service, body):
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