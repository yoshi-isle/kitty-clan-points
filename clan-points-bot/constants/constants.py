class Constants:
    # Ansi tables
    INCOMPLETE_STATUS="""
[2;31m[2;41m[2;43m[2;40mIncomplete[0m[2;31m[2;43m[0m[2;31m[2;41m[0m[2;31m[0m
"""
    READY_FOR_APPROVAL="""
[2;40m[2;32mReady for approval[0m[2;40m[0m
"""

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
    
    BUTTON_APPLY_TO_JOIN="✅ Accept Rules & Apply to Join"
    
    BUTTON_ANSWER_EDIT_QUESTIONS="📝 Click here to answer the questions"
    
    BUTTON_ADMIN_PANEL_APPROVE="✅"
    BUTTON_ADMIN_PANEL_CLOSE="❌"
    BUTTON_ADMIN_PANEL_ADD_LEGACY_POINTS="🗓️"
    
    # Admin panel
    APPLICATION_STATUS_HEADER="Application Status"
    LEGACY_POINTS_HEADER="Legacy Points"
    
    # Application questions
    APPLICATION_QUESTION1="Runescape name(s)"
    APPLICATION_QUESTION1_PLACEHOLDER="Enter names separated by commas (Zezima, Zezima2, ...)"
    APPLICATION_QUESTION2="How did you find out about us / referral?"
    APPLICATION_QUESTION3="What content do you like to do in-game?"
    APPLICATION_QUESTION4="Why do you want to join our clan?"
    
    # Success messages
    SUCCESS_APPLICATION_UPDATED="Your application has been updated!"
    SUCCESS_MEMBER_APPROVED="Member's application approved!"

    # Error messages
    ERROR_APPLICANT_FORM_INCOMPLETE="Applicant did not finish their questionnaire. If you believe this is an error, contact an admin."
    ERROR_APPLICANT_NOT_FOUND="Applicant not found. Please contact an admin"
    ERROR_INVALID_DATE_FORMAT="Invalid date format. Please use MM/DD/YYYY."
    ERROR_DATE_IN_FUTURE="You provided a date in the future. Try again"
    ERROR_MODERATOR_ACCESS_ONLY="This button is for moderators only."
    ERROR_WRONG_USER_EDITING_QUESTIONS="You are not the applicant. This is for them to fill out. If you believe this is an error, contact an admin."
    
    # Regex
    DATE_FORMAT="%m/%d/%Y"