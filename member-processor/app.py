import os
import sys
import pika
import json
from dotenv import load_dotenv
from services.google_sheet_service import GoogleSheetsService

def main():
    load_dotenv()
    sheets_service = GoogleSheetsService() 
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    new_member_channel = connection.channel()
    new_member_channel.queue_declare(queue='new_member')
    
    # Handles google sheet generation for new members
    def callback(ch, method, properties, body):
        print(f" [x] Received sheet generation request: {body}")
        message = json.loads(body.decode('utf-8'))
        member_discord_id = int(message["discord_id"])
        member_display_name = message["username"]
        sheets_service.create_sheet(member_discord_id, member_display_name)
        
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