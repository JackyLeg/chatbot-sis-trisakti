from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuTugasAkhir(Action):
    def name(self) -> Text:
        return "action_menu_tugasAkhir"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_tugasAkhir_ok")
        pilihan_menu = tracker.get_slot("menu_tugasAkhir")
        
        match pilihan_menu:
            case "Prosedur Tugas Akhir":
                return [SlotSet("return_value", "Prosedur Tugas Akhir")]
            case "Persyaratan Tugas Akhir":
                return [SlotSet("return_value", "Persyaratan Tugas Akhir")]
            case "Transaksi Tugas Akhir":
                return [SlotSet("return_value", "Transaksi Tugas Akhir")]
            case "Hasil Tugas Akhir":
                return [SlotSet("return_value", "Hasil Tugas Akhir")]
            case _:
                return []
            
        if tracker.get_slot("menu_tugasAkhir_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_tugasAkhir_confirmation", True)]
        else:
            return [SlotSet("menu_tugasAkhir_confirmation", False)]
        