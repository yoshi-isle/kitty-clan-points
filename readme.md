Local development

1. Navigate to clan-points-bot
2. Copy 'example.env' and create '.env' and fill in the values
3. You need a mongoDB database with the fields outlined in database.py
4. Get a sheets_config.json from google cloud API for google sheets and put in member-processor/services
5. Run `docker-compose up -d --build`