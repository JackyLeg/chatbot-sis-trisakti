from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuCuti(Action):
    def name(self) -> Text:
        return "menu_cuti"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        if tracker.get_slot("menu_cuti") == "Pengajuan Cuti Akademik":
            dispatcher.utter_message("Pengajuan Cuti Akademik *goToLink*")

        elif tracker.get_slot("menu_cuti") == "Status Pengajuan Cuti Akademik":
            dispatcher.utter_message("Status Pengajuan Cuti Akademik *checkStatus*")

        elif tracker.get_slot("menu_cuti") == "Kendala Pengajuan Cuti Akademik":
            dispatcher.utter_message("""Kendala Pengajuan Cuti Akademik
                                    Jika pengajuan cuti tidak dapat dilakukan atau status belum diperbarui, silakan periksa hal berikut:
                                    - Pastikan tidak memiliki kewajiban administrasi yang belum diselesaikan
                                    - Pastikan pengajuan dilakukan pada periode cuti yang ditentukan
                                    Jika kendala masih terjadi, silakan hubungi Contact Help Desk.""")
        
        else:
            dispatcher.utter_message("Maaf, menu tidak ditemukan.")

        return []