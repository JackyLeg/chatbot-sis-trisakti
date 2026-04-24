from re import match
from typing import Any, Dict, List, Text
import requests

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
        dispatcher.utter_message(json_message={"context": "cuti"})
        
        id_login = tracker.get_slot("npm")
        
        def fetch_peraturan_api(context_name: str) -> bool:
            try:
                payload = {
                    "IdLogin": id_login or "",
                    "context": context_name
                }
                response = requests.post(
                    "https://sismob.trisakti.ac.id/api/get-peraturan",
                    json=payload,
                    timeout=10
                )
                if response.status_code == 200:
                    data = response.json()
                    if data.get("status") == 200 and "body" in data and "data" in data["body"] and data["body"]["data"]:
                        aturan = data["body"]["data"].get("aturan")
                        if aturan:
                            dispatcher.utter_message(text=aturan)
                            return True
            except Exception as e:
                print(f"Failed to fetch from get-peraturan API: {e}")
            return False

        
        match pilihan_menu:
            case "Prosedur Tugas Akhir":
                if fetch_peraturan_api("cuti_prosedur"):
                    return []
                return [SlotSet("return_value", "Prosedur Tugas Akhir")]
            case "Persyaratan Tugas Akhir":
                if fetch_peraturan_api("cuti_persyaratan"):
                    return []
                return [SlotSet("return_value", "Persyaratan Tugas Akhir")]
            case "Transaksi Tugas Akhir":
                return [SlotSet("return_value", "Transaksi Tugas Akhir")]
            case "Hasil Tugas Akhir":
                return [SlotSet("return_value", "Hasil Tugas Akhir")]
            case _:
                return []
