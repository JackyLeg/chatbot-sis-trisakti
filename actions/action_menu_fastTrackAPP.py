from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuFastTrackAPP(Action):
    def name(self) -> Text:
        return "action_menu_fastTrackAPP"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_fastTrackAPP_ok")
        pilihan_menu = tracker.get_slot("menu_fastTrackAPP")
        
        match pilihan_menu:
            case "Prosedur FastTrackAPP":
                return [SlotSet("return_value", "Prosedur FastTrackAPP")]
            case "Persyaratan FastTrackAPP":
                return [SlotSet("return_value", "Persyaratan FastTrackAPP")]
            case "Transaksi FastTrackAPP":
                return [SlotSet("return_value", "Transaksi FastTrackAPP")]
            case "Hasil FastTrackAPP":
                return [SlotSet("return_value", "Hasil FastTrackAPP")]
            case "Batal":
                return [SlotSet("return_value", "Batal")]
            case _:
                return []
            
        if tracker.get_slot("menu_fastTrackAPP_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_fastTrackAPP_confirmation", True)]
        else:
            return [SlotSet("menu_fastTrackAPP_confirmation", False)]
        