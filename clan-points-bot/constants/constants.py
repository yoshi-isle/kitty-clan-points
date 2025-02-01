class Constants:
    # Ansi tables
    INCOMPLETE_STATUS="""
[2;31m[2;41m[2;43m[2;40mIncomplete[0m[2;31m[2;43m[0m[2;31m[2;41m[0m[2;31m[0m
"""
    READY_FOR_APPROVAL="""
[2;40m[2;32mReady for approval[0m[2;40m[0m
"""

    # Channel IDs
    CATEGORY_ID_NEW_MEMBER_REQUESTS=1327810678513340508
    CHANNEL_ID_PVM_HIGHSCORES=1327471885826392087
    CHANNEL_ID_HIGHEST_KCS=1327471885826392087
    CHANNEL_ID_EVENT_WINNERS=1327471885826392087
    CHANNEL_ID_CLAN_PHOTOS=1327471885826392087
    CHANNEL_ID_UPCOMING_EVENTS=1327471885826392087
    CHANNEL_ID_GIVEAWAYS=1327471885826392087
    CHANNEL_ID_SUBMIT_CLAN_POINTS=1331481576105709568
    CHANNEL_ID_APPROVALS=1334331881591803964
    
    # Links
    WISE_OLD_MAN_GROUP="https://wiseoldman.net/groups/1165"
    
    # Role names
    ROLE_NAME_MODERATOR="Moderator"
    ROLE_NAME_CATNIP="Catnip"
    
    # Button names
    BUTTON_CLOSE_TICKET="Close this channel"
    BUTTON_NO="No, keep it open"

    BUTTON_WELCOME_PVM_HIGHSCORES="⚔️ PvM Highscores"
    BUTTON_HIGHEST_KCS="📈 Highest KCs"
    BUTTON_EVENT_SHOWCASE="🏆 Event Showcase"
    BUTTON_CLAN_PHOTOS="📷 Clan Photos"
    BUTTON_UPCOMING_EVENTS="📅 Upcoming Events"
    BUTTON_GIVEAWAYS="🎉 Giveaways"
    BUTTON_WISE_OLD_MAN="📊 WiseOldMan Group"

    BUTTON_APPLY_TO_JOIN="✅ Accept Rules & Apply to Join"
    
    BUTTON_ANSWER_EDIT_QUESTIONS="📝 Click here to answer the questions"
    
    BUTTON_ADMIN_PANEL_APPROVE="Approve✅"
    BUTTON_ADMIN_PANEL_CLOSE="Close❌"
    BUTTON_ADMIN_PANEL_ADD_LEGACY_POINTS="Legacy Points🗓️"
    
    # Admin panel
    APPLICATION_STATUS_HEADER="Application Status"
    LEGACY_POINTS_HEADER="Legacy Points"
    
    # Application questions
    APPLICATION_QUESTION1="Runescape name(s)"
    APPLICATION_QUESTION1_PLACEHOLDER="Enter names separated by commas (Zezima, Zezima2, ...)"
    APPLICATION_QUESTION2="How did you find out about us / referral?"
    APPLICATION_QUESTION3="What content do you like to do in-game?"
    APPLICATION_QUESTION4="Why do you want to join our clan?"
    
    # Info messages
    INFO_FILL_APPLICATION="Please fill out your application here: "
    
    # Success messages
    SUCCESS_APPLICATION_UPDATED="Your application has been updated!"
    SUCCESS_MEMBER_APPROVED="Member's application approved!"
    
    TICKET_WELCOME_MESSAGE="# <:application:1331487726075252759> __Clan Member Application__\nWelcome! We're excited that you're interested in joining our growing community.\n\nPlease take a moment to answer the questions below so we can get to know you better.\n\n*Already part of the clan?* If you're an existing member looking to claim legacy points, please let us know your join date, and an admin will assist you shortly."

    # Error messages
    ERROR_APPLICANT_FORM_INCOMPLETE="Applicant did not finish their questionnaire."
    ERROR_APPLICANT_NOT_FOUND="Applicant not found. (Already approved?)"
    ERROR_INVALID_DATE_FORMAT="Invalid date format. Please use MM/DD/YYYY."
    ERROR_DATE_IN_FUTURE="You provided a date in the future. Try again"
    ERROR_MODERATOR_ACCESS_ONLY="This button is for moderators only."
    ERROR_WRONG_USER_EDITING_QUESTIONS="You are not the applicant. This is for them to fill out. If you believe this is an error, contact an admin."
    ERROR_TICKET_MANUALLY_REMOVED="It looks like you had an application that has been removed. Please contact an admin"
    ERROR_ALREADY_IN_CLAN="You're already in the clan!"
    ERROR_ALREADY_OPEN_APPLICATION="You already have an open application here: "
    # Regex
    DATE_FORMAT="%m/%d/%Y"