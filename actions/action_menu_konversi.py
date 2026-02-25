from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuKonversi(Action):
    def name(self) -> Text:
        return "action_menu_konversi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_konversi_ok")
        pilihan_menu = tracker.get_slot("menu_konversi")
        
        match pilihan_menu:
            case "Prosedur Konversi":
                return [SlotSet("return_value", "Prosedur Konversi")]
            case "Persyaratan Konversi":
                return [SlotSet("return_value", "Persyaratan Konversi")]
            case "Transaksi Konversi":
                return [SlotSet("return_value", "Transaksi Konversi")]
            case "Hasil Konversi":
                return [SlotSet("return_value", "Hasil Konversi")]
            case _:
                return []
            
        if tracker.get_slot("menu_konversi_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_konversi_confirmation", True)]
        else:
            return [SlotSet("menu_konversi_confirmation", False)]
        