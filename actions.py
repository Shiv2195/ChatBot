import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class GetTodayHoroscope(Action):

    def name(self):
        return "get_todays_horoscope"

    def run(self,dispatchcer,tracker,domain):
        user_horoscope_sign = tracker.get_slot('horoscope_sign')
        base_url = "http://horoscope-api.herokuapp.com/horoscope/{day}/{sign}"
        url = base_url.format(**{'day': "today",'sign' : user_horoscope_sign})
        res = requests.get(url)
        todays_horoscope = res.json()['horoscope']
        response = "Your today's horoscope:/n{}".format(todays_horoscope)
        dispatchcer.utter_message(response)
        return [SlotSet("horoscope_sign",user_horoscope_sign)]

class SubscribeUser(Action):
    def name(self):
        return "subscribe_user"

    def run(self, dispatchcer, tracker, domain):
        subscribe = tracker.get_slot('subscribe')
        if subscribe == 'True':
            response = "You're successfully subscribed"
        if subscribe=='False':
            response = "You're successfully unsubscribed"
            dispatchcer.utter_message(response)
        return [SlotSet("subscribe", subscribe)]

