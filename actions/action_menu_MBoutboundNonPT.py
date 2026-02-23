from re import match
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuMBOutboundNonPT(Action):
    def name(self) -> Text:
        return "action_menu_MBOutboundNonPT"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response = "utter_menu_MBOutboundNonPT_ok")
        pilihan_menu = tracker.get_slot("menu_MBOutboundNonPT")
        
        match pilihan_menu:
            case "Prosedur MBOutboundNonPT":
                return [SlotSet("return_value", "Prosedur MBOutboundNonPT")]
            case "Persyaratan MBOutboundNonPT":
                return [SlotSet("return_value", "Persyaratan MBOutboundNonPT")]
            case "Transaksi MBOutboundNonPT":
                return [SlotSet("return_value", "Transaksi MBOutboundNonPT")]
            case "Hasil MBOutboundNonPT":
                return [SlotSet("return_value", "Hasil MBOutboundNonPT")]
            case "Batal":
                return [SlotSet("return_value", "Batal")]
            case _:
                return []
            
        if tracker.get_slot("menu_MBOutboundNonPT_confirmation") == "Yes, that's correct":
            return [SlotSet("menu_MBOutboundNonPT_confirmation", True)]
        else:
            return [SlotSet("menu_MBOutboundNonPT_confirmation", False)]
        