from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuTranskrip(Action):
    def name(self) -> Text:
        return "action_menu_transkrip"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_transkrip_ok")
        pilihan_menu = tracker.get_slot("menu_transkrip")
        dispatcher.utter_message(json_message={"context": "transkrip"})
        fakultas = "Fakultas Teknologi Industri"
        
        match pilihan_menu:
            case "Prosedur Transkrip":
                return [SlotSet("return_value", "Prosedur Transkrip"),
                        SlotSet("fakultas", fakultas)]
            case "Persyaratan Transkrip":
                return [SlotSet("return_value", "Persyaratan Transkrip"),
                        SlotSet("fakultas", fakultas)]
            case "Transaksi Transkrip":
                return [SlotSet("return_value", "Transaksi Transkrip")]
            case "Hasil Transkrip":
                return [SlotSet("return_value", "Hasil Transkrip")]
            case _:
                return []
