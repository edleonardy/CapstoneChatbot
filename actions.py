# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCode(Action):
    def name(self) -> Text:
        return "action_code"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        import directory_loader as dl
        d = dl.Directory()

        input_type = tracker.latest_message['entities'][0]['entity']
        value = tracker.latest_message['entities'][0]['value']
        if not value:
            dispatcher.utter_message('I did not recognise that input.')
            return []
        if input_type == 'name':
            results = d.search(value)
            if len(results) == 0:
                dispatcher.utter_message('Sorry, I could not find {} in the directory.'.format(value))
                return []
            elif len(results) > 1:
                dispatcher.utter_message('There are multiple results for {}'.format(value))
                return []
            else:
                result = d[results[0][0]]
        elif input_type == 'code':
            try:
                result = d[value]
            except KeyError:
                dispatcher.utter_message('Sorry, {} does not exist in the directory.'.format(value))
                return []
        else:
            dispatcher.utter_message('I did not recognise that input.')
            return []
        dispatcher.utter_message('{} {} is a {} at UTS. For more info, visit {}'.format(result.code(),
                                                                                        result.get_name(),
                                                                                        result.get_type(),
                                                                                        result.url()))
        return []
