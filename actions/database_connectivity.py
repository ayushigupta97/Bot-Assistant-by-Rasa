from pymongo import MongoClient

def fetchData(emailId):

    client = MongoClient('localhost',27017)

    db=client['expert_details']
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

    collection.insert_many(mylist) '''

    #emailId="dbms@gmail.com"
    for x in collection.find(): 
        if emailId==x['technology']:
            print(x['email'])
            e=x['email']

    list_of_db = client.list_database_names() 
  
    if "expert_details" in list_of_db: 
        print("Exists !!") 
        
    return e

def main():
    e=fetchData("dbms@gmail.com")
    print(e)

if __name__=="__main__":
    main()
        
    