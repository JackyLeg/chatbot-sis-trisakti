from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuTAskripsi(Action):
    def name(self) -> Text:
        return "action_menu_TAskripsi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_TAskripsi_ok")
        pilihan_menu = tracker.get_slot("menu_TAskripsi")
        
        match pilihan_menu:
            case "Prosedur TAskripsi":
                return [SlotSet("return_value", "Prosedur TAskripsi")]
            case "Persyaratan TAskripsi":
                return [SlotSet("return_value", "Persyaratan TAskripsi")]
            case "Transaksi TAskripsi":
                return [SlotSet("return_value", "Transaksi TAskripsi")]
            case "Hasil TAskripsi":
                return [SlotSet("return_value", "Hasil TAskripsi")]
            case "Batal":
                return [SlotSet("return_value", "Batal")]
            case _:
                return []
            
        if tracker.get_slot("menu_TAskripsi_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_TAskripsi_confirmation", True)]
        else:
            return [SlotSet("menu_TAskripsi_confirmation", False)]
        