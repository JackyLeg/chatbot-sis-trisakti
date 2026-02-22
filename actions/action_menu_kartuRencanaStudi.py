from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuKartuRencanaStudi(Action):
    def name(self) -> Text:
        return "action_menu_kartuRencanaStudi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response = "utter_menu_kartuRencanaStudi_ok")
        pilihan_menu = tracker.get_slot("menu_kartuRencanaStudi")
        
        match pilihan_menu:
            case "Prosedur KRS":
                return [SlotSet("return_value", "Prosedur KRS")]
            case "Persyaratan KRS":
                return [SlotSet("return_value", "Persyaratan KRS")]
            case "Transaksi KRS":
                return [SlotSet("return_value", "Transaksi KRS")]
            case "Hasil KRS":
                return [SlotSet("return_value", "Hasil KRS")]
            case "Batal":
                return [SlotSet("return_value", "Batal")]
            case _:
                return []
            
        if tracker.get_slot("menu_kartuRencanaStudi_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_kartuRencanaStudi_confirmation", True)]
        else:
            return [SlotSet("menu_kartuRencanaStudi_confirmation", False)]