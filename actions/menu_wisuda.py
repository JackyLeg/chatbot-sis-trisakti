from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class MenuWisuda(Action):
    def name(self) -> Text:
        return "menu_wisuda"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        if tracker.get_slot("menu_wisuda") == "Graduation":
            dispatcher.utter_message("Yudisium dan Dokumen Kelulusan *giveInfo*")

        elif tracker.get_slot("menu_wisuda") == "Wisuda":
            dispatcher.utter_message("Pendaftaran dan Pelaksanaan Wisuda *giveInfo*")

        else:
            dispatcher.utter_message("Maaf, menu tidak ditemukan.")

        return []