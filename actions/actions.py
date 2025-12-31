from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionCheckWeather(Action):
    def name(self) -> Text:
        return "action_check_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        weather_info = "sunny and 25°C"  # Replace with real API call in production
        dispatcher.utter_message(text=f"The current weather in {location} is {weather_info}.")
        return [SlotSet("weather_info", weather_info)]