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

        dispatcher.utter_message(template = "utter_menu_kartuHasilStudi_ok")
        pilihan_menu = tracker.get_slot("menu_kartuHasilStudi")

        match pilihan_menu:
            case "Prosedur KHS":
                dispatcher.utter_message("""Prosedur melihat nilai dilakukan melalui tahapan berikut:
                                            1. Mahasiswa telah mengikuti mata kuliah yang terdaftar pada KRS.
                                            2. Dosen pengampu menginput dan mempublikasikan nilai mata kuliah.
                                            3. Mahasiswa mengakses menu Nilai pada Sistem Informasi Akademik untuk melihat nilai mata kuliah dan Kartu Hasil Studi (KHS).""")
                return [SlotSet(pilihan_menu, "Prosedur KHS")]
            case "Persyaratan KHS":
                dispatcher.utter_message("""Prasyarat untuk melihat nilai adalah sebagai berikut:
                                            1. KRS mahasiswa telah disetujui.
                                            2. Mata kuliah telah selesai dilaksanakan.
                                            3. Nilai mata kuliah telah dipublikasikan oleh dosen pengampu.""")
                return [SlotSet(pilihan_menu, "Persyaratan KHS")]
            case "Transaksi KHS":
                dispatcher.utter_message("""Silakan pilih semester untuk melihat nilai mata kuliah yang telah kamu tempuh.""")
                return [SlotSet(pilihan_menu, "Transaksi KHS")]
            case "Hasil KHS":
                dispatcher.utter_message("""Berikut adalah nilai mata kuliah kamu pada semester yang dipilih.
                                            Kamu juga dapat melihat rekap nilai dalam bentuk Kartu Hasil Studi (KHS).""")
                return [SlotSet(pilihan_menu, "Hasil KHS")]
            case _:
                dispatcher.utter_message("Maaf, menu tidak ditemukan.")
                return []
            
        # pilihan_menu2 = tracker.get_slot("menu_kartuRencanaStudi2")
        # match pilihan_menu:
        #     case "Melihat Mata Kuliah Pada KRS":
        #         dispatcher.utter_message("Melihat Mata Kuliah Pada KRS *info*")
        #         return [SlotSet(pilihan_menu, "Melihat Mata Kuliah Pada KRS")]
        #     case "Mengisi Data Academic Advising":
        #         dispatcher.utter_message("Mengisi Data Academic Advising *info*")
        #         return [SlotSet(pilihan_menu, "Mengisi Data Academic Advising")]
        #     case "Mengisi KRS":
        #         dispatcher.utter_message("Mengisi KRS *info*")
        #         return [SlotSet(pilihan_menu, "Mengisi KRS")]
        #     case "Melihat Prasyarat Pengisian KRS":
        #         dispatcher.utter_message("Melihat Prasyarat Pengisian KRS *info*")
        #         return [SlotSet(pilihan_menu, "Melihat Prasyarat Pengisian KRS")]
        #     case "More":
        #         dispatcher.utter_message("Untuk menu KRS lainnya, silakan kunjungi laman")
        #         return [SlotSet(pilihan_menu, None)]
        #     case _:
        #         dispatcher.utter_message("Maaf, menu tidak ditemukan.")
        #         return []
            
        
        # match pilihan_menu2:
        #     case "Melihat Kurikulum":
        #         dispatcher.utter_message("Melihat Kurikulum *info*")
        #         return [SlotSet(pilihan_menu2, "Melihat Kurikulum")]
        #     case "Mengajukan Fast Track":
        #         dispatcher.utter_message("Mengajukan Fast Track *info*")
        #         return [SlotSet(pilihan_menu2, "Mengajukan Fast Track")]
        #     case "Melihat Data Conversion Plan":
        #         dispatcher.utter_message("Melihat Data Conversion Plan *info*")
        #         return [SlotSet(pilihan_menu2, "Melihat Data Conversion Plan")]
        #     # case "Back":
        #     #     dispatcher.utter_message("Kembali ke menu sebelumnya.")
        #     #     return [SlotSet(pilihan_menu2, "Back")]
        #     case _:
        #         dispatcher.utter_message("Maaf, menu tidak ditemukan.")
        #         return []

        if tracker.get_slot("menu_kartuRencanaStudi_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_kartuRencanaStudi_confirmation", True)]
        else:
            return [SlotSet("menu_kartuRencanaStudi_confirmation", False)]