from re import match
from typing import Any, Dict, List, Text
import requests

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuCuti(Action):
    def name(self) -> Text:
        return "action_menu_cuti"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_cuti_ok")
        pilihan_menu = tracker.get_slot("menu_cuti")
        dispatcher.utter_message(json_message={"context": "cuti"})
        
        # Ambil identitas user untuk cek status login. 
        # (Silakan ubah "npm" menjadi nama slot yang sesuai di project ini jika berbeda)
        # id_login = tracker.get_slot("npm")
        # Jika ingin test dengan data dummy/hardcode "241150", jalankan line berikut:
        # id_login = tracker.get_slot("npm") or "241150"
        
        def fetch_peraturan_api(sender: str, context_name: str) -> bool:
            try:
                
                payload = {
                    "IdLogin": sender,
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
            case "Prosedur Cuti":
                # Panggil API dengan context_name "cuti_prosedur"
                # API akan selalu dipanggil walaupun belum login (id_login == ""). 
                if fetch_peraturan_api(tracker.sender_id, "cuti_prosedur"):
                    return [] 
                    
                # Fallback slot (jika API down / error / tidak ada keluaran teks)
                return [SlotSet("return_value", "Prosedur Cuti")]
            case "Persyaratan Cuti":
                if fetch_peraturan_api(tracker.sender_id, "cuti_persyaratan"):
                    return [] 
                    
                # Fallback slot (jika API down / error / tidak ada keluaran teks)
                return [SlotSet("return_value", "Persyaratan Cuti")]
            case "Transaksi Cuti":
                return [SlotSet("return_value", "Transaksi Cuti")]
            case "Hasil Cuti":
                return [SlotSet("return_value", "Hasil Cuti")]
            case _:
                return []
                