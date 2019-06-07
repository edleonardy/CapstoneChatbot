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

def init_code(dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        import directory_loader as dl
        d = dl.Directory()

        try:
            input_type = tracker.latest_message['entities'][0]['entity']
            value = tracker.latest_message['entities'][0]['value']
        except:
            input_type = 'code'
            value = tracker.get_slot('code')

        if not value:
            dispatcher.utter_template('utter_fallback', tracker)
            return None

        if input_type == 'name':
            results = d.search(value)
            if len(results) == 0:
                dispatcher.utter_template("utter_code_does_not_exist", tracker, name=value)
                return None
            elif len(results) > 1:
                dispatcher.utter_message('There are multiple results for {}:'.format(value))
                for r in results:
                    i = d[r[0]]
                    dispatcher.utter_message('{} {}'.format(i.code(), i.get_name()))
                dispatcher.utter_message('Please reply with the correct code.')
                return None
            else:
                result = d[results[0][0]]

        elif input_type == 'code':
            try:
                result = d[value]
            except KeyError:
                dispatcher.utter_template("utter_code_does_not_exist", tracker, code=value)
                return None
        else:
            dispatcher.utter_template('utter_fallback', tracker)
            return None

        return result


class ActionDetails(Action):
    def name(self) -> Text:
        return "action_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        if result is None:
            return []

        dispatcher.utter_message('{} {} is a {} at UTS. For more info, visit {}'.format(result.code(),
                                                                                        result.get_name(),
                                                                                        result.get_type(),
                                                                                        result.url()))
        return [SlotSet("code", result.just_code())]

class ActionChildren(Action):
    def name(self) -> Text:
        return "action_children"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        if result is None:
            return []

        if not result.is_type(''):
            dispatcher.utter_message('{} {} is a {} at UTS. It contains:'.format(result.code(),
                                                                                 result.get_name(),
                                                                                 result.get_type()))
            for c in result.get_children():
                dispatcher.utter_message('{} {}'.format(c.code(), c.get_name()))
            else:
                dispatcher.utter_message('For more info, visit {}'.format(result.url()))
        else:
            dispatcher.utter_message('{} {} is a {} at UTS. For more info, visit {}'.format(result.code(),
                                                                                            result.get_name(),
                                                                                            result.get_type(),
                                                                                            result.url()))
        return [SlotSet("code", result.just_code())]

class ActionChildren(Action):
    def name(self) -> Text:
        return "action_children"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        if result is None:
            return []

        if not result.is_type(''):
            dispatcher.utter_message('{} {} is a {} at UTS. It contains:'.format(result.code(),
                                                                                 result.get_name(),
                                                                                 result.get_type()))
            for c in result.get_children():
                if c.is_type('xbk'):
                    s = 'Select {} credit points from '.format(c.cp())
                    c_children = c.get_children()
                    if len(c_children) > 1:
                        for c_ in c_children[0:-1]:
                            s += c_.code() + ' ' + c_.get_name() + ', '
                        s += 'and '
                    if c_children[-1] is not None:
                        s += c_children[-1] .code() + ' ' + c_children[-1].get_name()
                    s += '.'
                    dispatcher.utter_message(s)
                else:
                    dispatcher.utter_message('{} {}'.format(c.code(), c.get_name()))
            else:
                dispatcher.utter_message('For more info, visit {}'.format(result.url()))
        else:
            dispatcher.utter_message('{} {} is a {} at UTS. For more info, visit {}'.format(result.code(),
                                                                                            result.get_name(),
                                                                                            result.get_type(),
                                                                                            result.url()))
        return [SlotSet("code", result.just_code())]


class ActionHonours(Action):
    def name(self) -> Text:
        return "action_hons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        if result is None:
            return []

        elif result.is_type('c'):
            if result.is_hons():
                dispatcher.utter_message('{} {} is a honours degree.'.format(result.code(), result.get_name()))
            else:
                dispatcher.utter_message('{} {} is not a honours degree.'.format(result.code(), result.get_name()))

        else:
            dispatcher.utter_message('{} {} is not a course at UTS. It is a a {} at UTS. It contains:'.format(
                result.code(), result.get_name(), result.get_type()))
        return [SlotSet("code", result.just_code())]


class ActionProfPrac(Action):
    def name(self) -> Text:
        return "action_prof_prac"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        if result is None:
            return []

        elif result.is_type('c'):
            if result.is_prof_prac():
                dispatcher.utter_message('{} {} comes with a Diploma in Professional Practice.'.format(result.code(),
                                                                                                       result.get_name()))
            else:
                dispatcher.utter_message('{} {} does not come with a Diploma in Professional Practice.'.format(
                    result.code(), result.get_name()))

        else:
            dispatcher.utter_message('{} {} is not a course at UTS. It is a a {} at UTS. It contains:'.format(
                result.code(), result.get_name(), result.get_type()))
        return [SlotSet("code", result.just_code())]


class ActionCombined(Action):
    def name(self) -> Text:
        return "action_combined"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        if result is None:
            return []

        elif result.is_type('c'):
            if result.is_combined():
                dispatcher.utter_message(
                    '{} {} is a combined degree.'.format(result.code(), result.get_name()))
            else:
                dispatcher.utter_message(
                    '{} {} is not a combined degree.'.format(result.code(), result.get_name()))

        else:
            dispatcher.utter_message('{} {} is not a course at UTS. It is a a {} at UTS. It contains:'.format(
                result.code(), result.get_name(), result.get_type()))
        return [SlotSet("code", result.just_code())]
