from database import get_db, SessionLocal, engine
from models import Base, Contact

Base.metadata.create_all(bind = engine)
db_gen = get_db()
db = next(db_gen)
def insert_contact(contact: int, username: str):
    new_contact = Contact(Contact = contact,Username= username)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)

def get_all_contacts():
    contacts = db.query(Contact).all()
    #print(contacts)
    #print(contacts.all())
    
    for c in contacts:
        print(f"Contact: {c.Contact}, Username:{c.Username}")

get_all_contacts()

    

