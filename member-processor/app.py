import os
import sys
import pika
import json
from dotenv import load_dotenv
from services.google_sheet_service import GoogleSheetsService
from models.clan_member import ClanMember

def main():
    load_dotenv()
    sheets_service = GoogleSheetsService() 
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    new_member_channel = connection.channel()
    new_member_channel.queue_declare(queue='new_member')
    
    # Handles google sheet generation for new members
    def callback(ch, method, properties, body):
        print(f" [x] Received sheet generation request: {body}")
        try:
            member: ClanMember = ClanMember.from_dict(json.loads(body.decode('utf-8')))
            url = sheets_service.create_sheet(member)
            print(f"Created sheet for {member.discord_display_name}: {url}")
        except Exception as e:
            print(f"Error getting clan member from request: {e}")
        
        
    new_member_channel.basic_consume(queue='new_member', auto_ack=True, on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    new_member_channel.start_consuming()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)