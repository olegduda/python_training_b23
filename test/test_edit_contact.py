# -*- coding: utf-8 -

from model.dto_contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() < 1:
        app.contact.add_contact(Contact())
    old_contacts = app.contact.get_contact_list()
    new_contact = Contact(first_name="New F_Name Edit", last_name="New L_Name Edit")
    new_contact.id = old_contacts[0].id
    app.contact.edit_first(new_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_last_first_name(app):
    current_contact = Contact()
    app.contact.add_contact(current_contact)
    old_contacts = app.contact.get_contact_list()
    new_contact = Contact(first_name="F_Name Edit", last_name="L_Name Edit")
    new_contact.id = Contact.found_by_name_in_list(first_name=current_contact.first_name,
                                                   last_name=current_contact.last_name,
                                                   list_contacts=old_contacts).id
    app.contact.search(f"{current_contact.last_name} {current_contact.first_name}")
    app.contact.edit_first(new_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts = Contact.update_list_by_id(new_contact, old_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
