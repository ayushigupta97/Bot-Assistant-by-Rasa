# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from pymongo import MongoClient

#import database_connectivity
#from __init__ import fetchData

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

def fetchData(tech):

    client = MongoClient('localhost',27017)

    db=client['exprt_details']
    print("Database created")

    collection = db["details"]
    print("Collection created")

    '''mylist = [ 
    {"name":"phpexpert", "technology":"PHP", "email":"php@gmail.com", "phone":"1234567891"}, 
    {"name":"pearlexpert", "technology":"Pearl", "email":"pearl@gmail.com", "phone":"1234567891"}, 
    {"name":"rubyexpert", "technology":"Ruby", "email":"ruby@gmail.com", "phone":"1234567891"}, 
    {"name":"javascriptexpert", "technology":"Javascript", "email":"js@gmail.com", "phone":"1234567891"}, 
    {"name":"angularexpert", "technology":"Angular", "email":"angular@gmail.com", "phone":"1234567891"}, 
    {"name":"dbexpert", "technology":"Database", "email":"dbms@gmail.com", "phone":"1234567891"}, 
    {"name":"mlexpert", "technology":"machine learning algorithms", "email":"ml@gmail.com", "phone":"1234567891"}, 
    ]

    collection.insert_many(mylist)''' 

    #emailId="dbms@gmail.com"
    for x in collection.find(): 
        if tech==x['technology']:
            n = x['name']
            e=x['email']
            p = x['phone']

    list_of_db = client.list_database_names() 
  
    if "exprt_details" in list_of_db: 
        print("Exists !!") 
        
    return n, e, p


class ActionAskTechnology(Action):

	def name(self) -> Text:
		return "action_ask_technology"

	def run(self, dispatcher, tracker, domain):

		technology = tracker.get_slot("technology_type")
		dispatcher.utter_message(template="utter_technology")
		return[]

class ActionGiveExpert(Action):

	def name(self) -> Text:
		return "action_give_expert"

	def run(self, dispatcher, tracker, domain):

		technology = tracker.get_slot("technology_type")
		name, email, phone = fetchData(technology)
		#fetchData(technology)
		#name = "Ayushi"
		#email = "abc@gmail.com"
		#phone = "945035"
		dispatcher.utter_message("Here is the name, email and phone no of {0} expert:{1}, {2} and {3}".format(technology, name, email, phone))
		return[]

class ActionGiveTutorial(Action):

	def name(self) -> Text:
		return "action_give_tutorial"

	def run(self, dispatcher, tracker, domain):

		technology = tracker.get_slot("technology_type")
		print(technology)
		if technology=="Database" or technology=="database":
			t = "https://www.javatpoint.com/dbms-tutorial"
		elif technology=="Php" : 
			t = "https://www.w3schools.com/php/"
		elif technology=="JavaScript" or technology=="CSS" or technology=="HTML" :
			t = "https://www.w3schools.com/html/html_scripts.asp"
		elif technology=="machine learning algorithms" : 
			t = "https://www.javatpoint.com/machine-learning"
		elif technology=="Angular" or technology=="Node" : 
			t = "https://medium.com/swlh/node-js-express-angular-mongodb-stack-3dcc5087b6d4"
		elif technology=="Perl" : 
			t = "https://www.tutorialspoint.com/perl/index.htm"
		elif technology=="Ruby" : 
			t = "https://www.tutorialspoint.com/ruby/index.htm"
		else :
			t = "Oops!!!! Please choose any of the above options" 
		'''if technology=="Php" : 
			t = "PHP"
		if technology=="JavaScript" or technology=="CSS" or technology=="HTML" :
			t = "JavaScript"
		if technology=="machine learning algorithms" : 
			t = "ML"
		if technology=="Angular" or technology=="Node" : 
			t = "Angular"
		if technology=="Pearl" : 
			t = "Pearl"
		if technology=="Ruby" : 
			t = "Ruby"
		if technology=="Other" :
			t = "Other" '''
		dispatcher.utter_message(t)
		return[]
