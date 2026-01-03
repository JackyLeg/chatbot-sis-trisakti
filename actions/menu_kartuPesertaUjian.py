from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuKartuPesertaUjian(Action):
    def name(self) -> Text:
        return "menu_kartuPesertaUjian"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        if tracker.get_slot("menu_kartuPesertaUjian") == "Cek Kartu Peserta Ujian":
            dispatcher.utter_message("Cetak Kartu Peserta Ujian *goToLink*")

        elif tracker.get_slot("menu_kartuPesertaUjian") == "Kartu Peserta Ujian Tidak Dapat Diunduh":
            dispatcher.utter_message("Kartu Peserta Ujian Tidak Dapat Diunduh *tellWhy*")

        elif tracker.get_slot("menu_kartuPesertaUjian") == "Syarat mendapatkan Kartu Peserta Ujian":
            dispatcher.utter_message("Syarat mendapatkan Kartu Peserta Ujian *tellSyarat*")

        else:
            dispatcher.utter_message("Maaf, menu tidak ditemukan.")

        return []