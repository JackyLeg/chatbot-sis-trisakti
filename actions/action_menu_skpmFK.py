from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuSKPMFK(Action):
    def name(self) -> Text:
        return "action_menu_skpmFK"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response = "utter_menu_skpmFK_ok")
        pilihan_menu = tracker.get_slot("menu_skpmFK")
        
        match pilihan_menu:
            case "Prosedur SKPM FK":
                return [SlotSet("return_value", "Prosedur SKPM FK")]
            case "Persyaratan SKPM FK":
                return [SlotSet("return_value", "Persyaratan SKPM FK")]
            case "Transaksi SKPM FK":
                return [SlotSet("return_value", "Transaksi SKPM FK")]
            case "Hasil SKPM FK":
                return [SlotSet("return_value", "Hasil SKPM FK")]
            case "Batal":
                return [SlotSet("return_value", "Batal")]
            case _:
                return []

        if tracker.get_slot("menu_skpmFK_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_skpmFK_confirmation", True)]
        else:
            return [SlotSet("menu_skpmFK_confirmation", False)]