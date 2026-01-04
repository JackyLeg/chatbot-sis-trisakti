from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuTugasAkhir(Action):
    def name(self) -> Text:
        return "menu_tugasAkhir"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        if tracker.get_slot("menu_tugasAkhir") == "Pendaftaran Tugas Akhir":
            dispatcher.utter_message("Pendaftaran Tugas Akhir *goToLink*")

        elif tracker.get_slot("menu_tugasAkhir") == "Judul Tugas Akhir":
            dispatcher.utter_message("Judul Tugas Akhir *giveInfo*")

        elif tracker.get_slot("menu_tugasAkhir") == "Dosen Pembimbing":
            dispatcher.utter_message("Dosen Pembimbing *giveInfo*")

        elif tracker.get_slot("menu_tugasAkhir") == "Proposal dan Bimbingan":
            dispatcher.utter_message("Proposal dan Bimbingan *giveInfo*")

        elif tracker.get_slot("menu_tugasAkhir") == "Seminar Proposal dan Sidang":
            dispatcher.utter_message("Seminar Proposal dan Sidang *giveInfo*")

        elif tracker.get_slot("menu_kartuRe") == "Nilai, Revisi, dan Kelulusan":
            dispatcher.utter_message("Nilai, Revisi, dan Kelulusan *giveInfo*")

        else:
            dispatcher.utter_message("Maaf, menu tidak ditemukan.")

        return []