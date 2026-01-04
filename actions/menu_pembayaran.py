from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuPembayaran(Action):
    def name(self) -> Text:
        return "menu_pembayaran"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        if tracker.get_slot("menu_pembayaran") == "Cek Status Pembayaran":
            dispatcher.utter_message("Cek Status Pembayaran *checkStatus*")

        elif tracker.get_slot("menu_pembayaran") == "Kendala Pembayaran":
            dispatcher.utter_message("Kendala Pembayaran *tellWhy*")

        else:
            dispatcher.utter_message("Maaf, menu tidak ditemukan.")

        return []