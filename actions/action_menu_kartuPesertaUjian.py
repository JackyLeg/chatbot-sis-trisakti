from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuKartuPesertaUjian(Action):
    def name(self) -> Text:
        return "action_menu_kartuPesertaUjian"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_kartuPesertaUjian_ok")
        pilihan_menu = tracker.get_slot("menu_kartuPesertaUjian")
        
        match pilihan_menu:
            case "Prosedur Kartu Peserta Ujian":
                return [SlotSet("return_value", "Prosedur Kartu Peserta Ujian")]
            case "Persyaratan Kartu Peserta Ujian":
                return [SlotSet("return_value", "Persyaratan Kartu Peserta Ujian")]
            case "Transaksi Kartu Peserta Ujian":
                return [SlotSet("return_value", "Transaksi Kartu Peserta Ujian")]
            case "Hasil Kartu Peserta Ujian":
                return [SlotSet("return_value", "Hasil Kartu Peserta Ujian")]
            case _:
                return []
            
        if tracker.get_slot("menu_kartuPesertaUjian_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_kartuPesertaUjian_confirmation", True)]
        else:
            return [SlotSet("menu_kartuPesertaUjian_confirmation", False)]
        