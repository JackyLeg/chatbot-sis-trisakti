from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckUserRole(Action):
    def name(self) -> Text:
        return "action_check_user_role"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # 1. Cek apakah role sudah ada di slot (supaya tidak hit API berulang kali)
        role = tracker.get_slot("user_role")
        
        # 2. Jika belum ada, panggil API get-role
        if not role:
            try:
                role_response = requests.post(
                    "https://sismob.trisakti.ac.id/api/get-role",
                    json={"IdLogin": tracker.sender_id},
                    timeout=10
                )
                if role_response.status_code == 200:
                    role = role_response.json().get("role")
                    if not role or role == "No Role":
                        role = "DSNWALI"
                else:
                    print(f"API Error: Status {role_response.status_code}")
                    role = "DSNWALI"
            except Exception as e:
                print(f"Failed to fetch get-role API: {e}")
                role = "DSNWALI"

        #print(f"DEBUG: Sender ID: {tracker.sender_id} | Final Role yang didapat: {role}")

        return [SlotSet("user_role", role)]
