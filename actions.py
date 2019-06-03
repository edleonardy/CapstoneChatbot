# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionDetails(Action):
    def name(self) -> Text:
        return "action_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        import directory_loader as dl
        d = dl.Directory()
        input_type = tracker.latest_message['entities'][0]['entity']
        value = tracker.latest_message['entities'][0]['value']
        if not value:
            dispatcher.utter_template('utter_fallback', tracker)
            return []
        if input_type == 'name':
            results = d.search(value)
            if len(results) == 0:
                dispatcher.utter_name_does_not_exist("utter_default", tracker, name=value)
                return []
            elif len(results) > 1:
                dispatcher.utter_message('There are multiple results for {}:'.format(value))
                for r in results:
                    i = d[r[0]]
                    dispatcher.utter_message('{} {}'.format(i.code(), i.get_name()))
                dispatcher.utter_message('Please reply with the correct code.')
                return []
            else:
                result = d[results[0][0]]
        elif input_type == 'code':
            try:
                result = d[value]
            except KeyError:
                dispatcher.utter_code_does_not_exist("utter_default", tracker, code=value)
                return []
        else:
            dispatcher.utter_template('utter_fallback', tracker)
            return []
        dispatcher.utter_message('{} {} is a {} at UTS. For more info, visit {}'.format(result.code(),
                                                                                        result.get_name(),
                                                                                        result.get_type(),
                                                                                        result.url()))
        return [SlotSet("code", result.just_code())]
