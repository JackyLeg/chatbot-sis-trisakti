from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuMajoringApplication(Action):
    def name(self) -> Text:
        return "action_menu_majoringApplication"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_majoringApplication_ok")
        pilihan_menu = tracker.get_slot("menu_majoringApplication")
        
        match pilihan_menu:
            case "Prosedur Majoring Application":
                return [SlotSet("return_value", "Prosedur Majoring Application")]
            case "Persyaratan Majoring Application":
                return [SlotSet("return_value", "Persyaratan Majoring Application")]
            case "Transaksi Majoring Application":
                return [SlotSet("return_value", "Transaksi Majoring Application")]
            case "Hasil Majoring Application":
                return [SlotSet("return_value", "Hasil Majoring Application")]
            case "Batal":
                return [SlotSet("return_value", "Batal")]
            case _:
                return []
            
        if tracker.get_slot("menu_majoringApplication_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_majoringApplication_confirmation", True)]
        else:
            return [SlotSet("menu_majoringApplication_confirmation", False)]
        