from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuCuti(Action):
    def name(self) -> Text:
        return "action_menu_cuti"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_cuti_ok")
        pilihan_menu = tracker.get_slot("menu_cuti")
        
        match pilihan_menu:
            case "Prosedur Cuti":
                return [SlotSet("return_value", "Prosedur Cuti")]
            case "Persyaratan Cuti":
                return [SlotSet("return_value", "Persyaratan Cuti")]
            case "Transaksi Cuti":
                return [SlotSet("return_value", "Transaksi Cuti")]
            case "Hasil Cuti":
                return [SlotSet("return_value", "Hasil Cuti")]
            case "Batal":
                return [SlotSet("return_value", "Batal")]
            case _:
                return []
            
        if tracker.get_slot("menu_cuti_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_cuti_confirmation", True)]
        else:
            return [SlotSet("menu_cuti_confirmation", False)]
        