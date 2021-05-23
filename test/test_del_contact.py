# -*- coding: utf-8 -
from model.dto_contact import Contact
from random import randrange


def test_delete_random_contact(app):
    if app.contact.count() < 1:
        app.contact.add_contact(Contact())
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.pop(index)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_delete_all_contacts(app):
    app.contact.preparation_several_contacts(4)
    app.contact.delete_all()
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == 0
