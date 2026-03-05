from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuKonseling(Action):
    def name(self) -> Text:
        return "action_menu_konseling"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_konseling_ok")
        pilihan_menu = tracker.get_slot("menu_konseling")
        dispatcher.utter_message(json_message={"context": "konseling"})
        fakultas = "Fakultas Teknologi Industri"
        
        match pilihan_menu:
            case "Prosedur Konseling":
                return [SlotSet("return_value", "Prosedur Konseling"),
                        SlotSet("fakultas", fakultas)]
            case "Persyaratan Konseling":
                return [
                    SlotSet("return_value", "Persyaratan Konseling"),
                    SlotSet("fakultas", fakultas)
                    ]
            case "Transaksi Konseling":
                return [SlotSet("return_value", "Transaksi Konseling")]
            case "Hasil Konseling":
                return [SlotSet("return_value", "Hasil Konseling")]
            case _:
                return []
