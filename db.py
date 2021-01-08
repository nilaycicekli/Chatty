# code snippets: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/41095eba777a94e2748a233fd5a2df826792086a/firestore/cloud-client/snippets.py#L273-L279
# firebase docs: https://firebase.google.com/docs/firestore/query-data/queries#python_3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import datetime

# Use the application default credentials
cred = credentials.Certificate('Chatty/chatty-y-firebase-adminsdk-zb1ow-7b79045fa0.json')
default_app = firebase_admin.initialize_app(cred)

# initialize firestore
db = firestore.client() 

# create a new document
def add(username, fname, lname, email, bio, streak=0,  tags=[], status='happy', location=(),city=''):
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
        'city':city

    })
# create a new user example
# add(username='john',
#     fname="john",
#     lname="doe",
#     tags=["dance","painting","photo","coding","hiking"],
#     email="jdoe@gmail.com",
#     bio="hello text me!",
#     status="online")


# get all the data in a collection
def get_all(collection="users"):
    collection_ref = db.collection(f'{collection}')
    docs = collection_ref.stream()
    arr = []
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
        arr.append(doc.to_dict())
    return arr



# get a document by id
def get_by_doc_id(docid):
    doc_ref = db.collection(u'users').document(docid)
    doc = doc_ref.get()
    print(f'{doc.id} => {doc.to_dict()}')
    dic = doc.to_dict()
    return dic

# get a document by username.
def get_by_username(username):
    doc = db.collection(u'users').where(u'username', u'==',username).stream()
    #print(f'{doc.id} => {doc.to_dict()}')
    for d in doc:
        print(f'{d.id} => {d.to_dict()}')
# update some fields. but not array fields. you can update multiple
def update(username,**kwargs):
    user_ref = db.collection(u'users').document(username)

    user_ref.update(kwargs)
    user_ref.update({
        u'timestamp': firestore.SERVER_TIMESTAMP
    })

# find the people with similar interests
def tag_match(tag=[]):
    collection_ref = db.collection(u'users')
    query = collection_ref.where(u'tags', u'array_contains_any', tag)
    result = query.stream()
    for r in result:
        print(f'{r.id} => {r.to_dict()}')


def tag_add(username,tags):
    user_ref = db.collection(u'users').document(username)

    # Atomically add a new tag to the 'tags' array field. you can add multiple.
    user_ref.update({u'tags': firestore.ArrayUnion(tags)})

    user_ref.update({
        u'timestamp': firestore.SERVER_TIMESTAMP
    })

def tag_remove(username,tags):
    user_ref = db.collection(u'users').document(username)

    #  remove a tag from the 'tags' array field.
    user_ref.update({u'tags': firestore.ArrayRemove(tags)})

    user_ref.update({
        u'timestamp': firestore.SERVER_TIMESTAMP
    })

# other functions we need:
# order results
# find people close by