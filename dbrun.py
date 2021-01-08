import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

cred = credentials.Certificate('Chatty/chatty-y-firebase-adminsdk-zb1ow-7b79045fa0.json')
default_app = firebase_admin.initialize_app(cred)

# initialize firestore
db = firestore.client() 

def add(username, email,fname='', lname='',  bio='I am new here!', streak=0,  tags=[], status='happy', location=()):
    # with specified document id.
    doc_ref = db.collection(u'users').document(f'{username}') 
    doc_ref.set({ # if you uncommented the line above, then chanhe this line to doc_ref.set({, default = db.collection(u'users').add({
        'username':username,
        'fname':fname,
        'lname':lname,
        'email':email,
        'streak':streak,
        'bio':bio,
        'tags':tags,
        'status': status,
        'location': location,
        'created': datetime.datetime.now(),

    })