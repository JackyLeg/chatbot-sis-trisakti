from re import match
from typing import Any, Dict, List, Text
import requests

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuWisuda(Action):
    def name(self) -> Text:
        return "action_menu_wisuda"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_wisuda_ok")
        pilihan_menu = tracker.get_slot("menu_wisuda")
        dispatcher.utter_message(json_message={"context": "wisuda"})
        
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
            case "Prosedur Wisuda":
                if fetch_peraturan_api("wisuda_prosedur"):
                    return []
                return [SlotSet("return_value", "Prosedur Wisuda")]
            case "Persyaratan Wisuda":
                if fetch_peraturan_api("wisuda_persyaratan"):
                    return []
                return [SlotSet("return_value", "Persyaratan Wisuda")]
            case "Transaksi Wisuda":
                return [SlotSet("return_value", "Transaksi Wisuda")]
            case "Hasil Wisuda":
                return [SlotSet("return_value", "Hasil Wisuda")]
            case _:
                return []
