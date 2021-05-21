# -*- coding: utf-8 -

from model.dto_contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() < 1:
        app.contact.add_contact(Contact())
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)


def test_delete_all_contacts(app):
    app.contact.preparation_several_contacts(4)
    app.contact.delete_all()
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == 0
