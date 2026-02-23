from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuWisuda(Action):
    def name(self) -> Text:
        return "action_menu_wisuda"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_wisuda_ok")
        pilihan_menu = tracker.get_slot("menu_wisuda")
        
        match pilihan_menu:
            case "Prosedur Wisuda":
                return [SlotSet("return_value", "Prosedur Wisuda")]
            case "Persyaratan Wisuda":
                return [SlotSet("return_value", "Persyaratan Wisuda")]
            case "Transaksi Wisuda":
                return [SlotSet("return_value", "Transaksi Wisuda")]
            case "Hasil Wisuda":
                return [SlotSet("return_value", "Hasil Wisuda")]
            case "Batal":
                return [SlotSet("return_value", "Batal")]
            case _:
                return []
            
        if tracker.get_slot("menu_wisuda_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_wisuda_confirmation", True)]
        else:
            return [SlotSet("menu_wisuda_confirmation", False)]
        