from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckSufficientFunds(Action):
    def name(self) -> Text:
        return "action_check_sufficient_funds"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # hard-coded balance for tutorial purposes. in production this
        # would be retrieved from a database or an API
        balance = 1000
        transfer_amount = tracker.get_slot("amount")
        has_sufficient_funds = transfer_amount <= balance
        return [SlotSet("has_sufficient_funds", has_sufficient_funds)]

class ActionGreeetings(Action):
    def name(self) -> Text:
        return "action_greetings"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_greet", name=tracker.get_slot("name"))
        return []
###
class MenuCuti(Action):
    def name(self) -> Text:
        return "action_menu_cuti"

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

class MenuKartuPesertaUjian(Action):
    def name(self) -> Text:
        return "action_menu_kartuPesertaUjian"

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


# #CUTI
# class PengajuanCutiAkademik(Action):
#     def name(self) -> Text:
#         return "action_pengajuan_cuti_akademik"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message("Pengajuan Cuti Akademik *link*")
#         return []

# class StatusPengajuanCutiAkademik(Action):
#     def name(self) -> Text:
#         return "action_status_pengajuan_cuti_akademik"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message("Status Pengajuan Cuti Akademik *link*")
#         return []
    
# class KendalaPengajuanCuti(Action):
#     def name(self) -> Text:
#         return "action_kendala_pengajuan_cuti"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message("Kendala Pengajuan Cuti Akademik *link*")
#         return []