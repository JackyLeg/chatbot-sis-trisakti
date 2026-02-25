from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuSKPI(Action):
    def name(self) -> Text:
        return "action_menu_skpi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response = "utter_menu_skpi_ok")
        pilihan_menu = tracker.get_slot("menu_skpi")
        
        match pilihan_menu:
            case "Prosedur SKPI":
                return [SlotSet("return_value", "Prosedur SKPI")]
            case "Persyaratan SKPI":
                return [SlotSet("return_value", "Persyaratan SKPI")]
            case "Transaksi SKPI":
                return [SlotSet("return_value", "Transaksi SKPI")]
            case "Hasil SKPI":
                return [SlotSet("return_value", "Hasil SKPI")]
            case _:
                return []

        if tracker.get_slot("menu_skpi_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_skpi_confirmation", True)]
        else:
            return [SlotSet("menu_skpi_confirmation", False)]