import os
import sys
import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    new_member_channel = connection.channel()
    new_member_channel.queue_declare(queue='new_member')
    
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        
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