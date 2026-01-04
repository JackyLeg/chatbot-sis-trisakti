from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuKartuRencanaStudi(Action):
    def name(self) -> Text:
        return "menu_kartuRencanaStudi"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        if tracker.get_slot("menu_kartuRencanaStudi") == "Cara Mengisi KRS":
            dispatcher.utter_message("Cara Mengisi KRS *tellHow*")

        elif tracker.get_slot("menu_kartuRencanaStudi") == "Periode Pengisian KRS":
            dispatcher.utter_message("Periode Pengisian KRS *tellWhen*")

        elif tracker.get_slot("menu_kartuRencanaStudi") == "Tidak Bisa Mengisi KRS":
            dispatcher.utter_message("Syarat Tidak Bisa Mengisi KRS *tellWhy*")

        elif tracker.get_slot("menu_kartuRencanaStudi") == "Ubah/Batalkan KRS":
            dispatcher.utter_message("Ubah/Batalkan KRS *tellHow*")

        elif tracker.get_slot("menu_kartuRencanaStudi") == "Cetak/Unduh KRS":
            dispatcher.utter_message("Cetak/Unduh KRS *tellHow*")

        elif tracker.get_slot("menu_kartuRencanaStudi") == "Masalah KRS":
            dispatcher.utter_message("Masalah KRS *tellWhy*")

        else:
            dispatcher.utter_message("Maaf, menu tidak ditemukan.")

        return []