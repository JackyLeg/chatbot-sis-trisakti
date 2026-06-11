from re import match
from typing import Any, Dict, List, Text
import requests

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuBimbinganDiktisaintekBerdampak(Action):
    def name(self) -> Text:
        return "action_menu_bimbinganDiktisaintekBerdampak"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_bimbinganDiktisaintekBerdampak_ok")
        pilihan_menu = tracker.get_slot("menu_bimbinganDiktisaintekBerdampak")
        dispatcher.utter_message(json_message={"context": "bimbinganDiktisaintekBerdampak"})
        
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
            case "Prosedur Bimbingan Diktisaintek Berdampak":
                if fetch_peraturan_api(tracker.sender_id, "bimbinganDiktisaintekBerdampak_prosedur"):
                    return [SlotSet("return_value", "api_success")]
                return [SlotSet("return_value", "Prosedur Bimbingan Diktisaintek Berdampak")]
            case "Persyaratan Bimbingan Diktisaintek Berdampak":
                if fetch_peraturan_api(tracker.sender_id, "bimbinganDiktisaintekBerdampak_persyaratan"):
                    return [SlotSet("return_value", "api_success")]
                return [SlotSet("return_value", "Persyaratan Bimbingan Diktisaintek Berdampak")]
            case "Transaksi Bimbingan Diktisaintek Berdampak":
                return [SlotSet("return_value", "Transaksi Bimbingan Diktisaintek Berdampak")]
            case "Hasil Bimbingan Diktisaintek Berdampak":
                return [SlotSet("return_value", "Hasil Bimbingan Diktisaintek Berdampak")]
            case _:
                return []
