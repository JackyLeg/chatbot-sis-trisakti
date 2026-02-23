from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuGraduationProcess(Action):
    def name(self) -> Text:
        return "action_menu_graduationProcess"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_graduationProcess_ok")
        pilihan_menu = tracker.get_slot("menu_graduationProcess")
        
        match pilihan_menu:
            case "Prosedur Graduation Process":
                return [SlotSet("return_value", "Prosedur Graduation Process")]
            case "Persyaratan Graduation Process":
                return [SlotSet("return_value", "Persyaratan Graduation Process")]
            case "Transaksi Graduation Process":
                return [SlotSet("return_value", "Transaksi Graduation Process")]
            case "Hasil Graduation Process":
                return [SlotSet("return_value", "Hasil Graduation Process")]
            case "Batal":
                return [SlotSet("return_value", "Batal")]
            case _:
                return []
            
        if tracker.get_slot("menu_graduationProcess_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_graduationProcess_confirmation", True)]
        else:
            return [SlotSet("menu_graduationProcess_confirmation", False)]
        