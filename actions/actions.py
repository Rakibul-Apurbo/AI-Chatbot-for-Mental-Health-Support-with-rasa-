# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from database_utils import insert_chat, create_table
from datetime import datetime

create_table()

class ActionLogUserMessage(Action):
    def name(self) -> Text:
        return "action_log_user_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_message = tracker.latest_message.get("text")
        conversation_id = tracker.sender_id
        
        # Log user message
        insert_chat(conversation_id, "user", user_message)
        
        return []

class ActionLogBotResponse(Action):
    def name(self) -> Text:
        return "action_log_bot_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        last_bot_event = None
        for e in reversed(tracker.events):
            if e.get("event") == "bot":
                last_bot_event = e
                break

        if last_bot_event:
            bot_response = last_bot_event.get("text")
            insert_chat(tracker.sender_id, "bot", bot_response)
            return [SlotSet("last_bot_response", bot_response)]

        return []

# class ActionRespondGreeting(Action):
#     def name(self) -> Text:
#         return "action_respond_greeting"
    
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         response = "Hey! How can I help you today?"   # Example bot response
        
#         # Send the response to the user
#         dispatcher.utter_message(text=response)
        
#         # Save the response in the slot for logging
#         return [SlotSet("last_bot_response", response)]
        