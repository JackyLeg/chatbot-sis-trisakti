from re import match
from typing import Any, Dict, List, Text
import requests

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuMajoringApplication(Action):
    def name(self) -> Text:
        return "action_menu_majoringApplication"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_majoringApplication_ok")
        pilihan_menu = tracker.get_slot("menu_majoringApplication")
        dispatcher.utter_message(json_message={"context": "majoringApplication"})
        
        # id_login = tracker.get_slot("npm")
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
            case "Prosedur Majoring Application":
                if fetch_peraturan_api(tracker.sender_id, "majoringApplication_prosedur"):
                    return []
                return [SlotSet("return_value", "Prosedur Majoring Application")]
            case "Persyaratan Majoring Application":
                if fetch_peraturan_api(tracker.sender_id, "majoringApplication_persyaratan"):
                    return []
                return [SlotSet("return_value", "Persyaratan Majoring Application")]
            case "Transaksi Majoring Application":
                return [SlotSet("return_value", "Transaksi Majoring Application")]
            case "Hasil Majoring Application":
                return [SlotSet("return_value", "Hasil Majoring Application")]
            case _:
                return []
