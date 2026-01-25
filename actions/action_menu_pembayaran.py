from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuPembayaran(Action):
    def name(self) -> Text:
        return "action_menu_pembayaran"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response = "utter_menu_pembayaran_ok")
        pilihan_menu = tracker.get_slot("menu_pembayaran")
        
        match pilihan_menu:
            case "Prosedur Pembayaran":
                return [SlotSet("return_value", "Prosedur Pembayaran")]
            case "Persyaratan Pembayaran":
                return [SlotSet("return_value", "Persyaratan Pembayaran")]
            case "Transaksi Pembayaran":
                return [SlotSet("return_value", "Transaksi Pembayaran")]
            case "Hasil Pembayaran":
                return [SlotSet("return_value", "Hasil Pembayaran")]
            case _:
                return []

        if tracker.get_slot("menu_pembayaran_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_pembayaran_confirmation", True)]
        else:
            return [SlotSet("menu_pembayaran_confirmation", False)]