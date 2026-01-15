from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuKartuHasilStudi(Action):
    def name(self) -> Text:
        return "action_menu_kartuHasilStudi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response = "utter_menu_kartuHasilStudi_ok")
        pilihan_menu = tracker.get_slot("menu_kartuHasilStudi")

        match pilihan_menu:
            case "Prosedur KHS":
                return [SlotSet("return_value", "Prosedur KHS")]
            case "Persyaratan KHS":
                return [SlotSet("return_value", "Persyaratan KHS")]
            case "Transaksi KHS":
                return [SlotSet("return_value", "Transaksi KHS")]
            case "Hasil KHS":
                return [SlotSet("return_value", "Hasil KHS")]
            case _:
                return []

        if tracker.get_slot("menu_kartuHasilStudi_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_kartuHasilStudi_confirmation", True)]
        else:
            return [SlotSet("menu_kartuHasilStudi_confirmation", False)]