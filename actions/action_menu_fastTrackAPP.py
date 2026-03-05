from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuFastTrackApp(Action):
    def name(self) -> Text:
        return "action_menu_fastTrackApp"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_fastTrackApp_ok")
        pilihan_menu = tracker.get_slot("menu_fastTrackApp")
        dispatcher.utter_message(json_message={"context": "fastTrackApp"})
        fakultas = "Fakultas Teknologi Industri" #default value= ""
        
        match pilihan_menu:
            case "Prosedur FastTrackApp":
                
                return [SlotSet("return_value", "Prosedur FastTrackApp"),
                        SlotSet("fakultas", fakultas)]
            case "Persyaratan FastTrackApp":
                return [SlotSet("return_value", "Persyaratan FastTrackApp"),
                        SlotSet("fakultas", fakultas)]
            case "Transaksi FastTrackApp":
                return [SlotSet("return_value", "Transaksi FastTrackApp")]
            case "Hasil FastTrackApp":
                return [SlotSet("return_value", "Hasil FastTrackApp")]
            case _:
                return []