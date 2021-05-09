# -*- coding: utf-8 -

from model.dto_contact import Contact


def test_edit_first_contact(app):
    app.contact.add_contact(Contact())
    new_contact = Contact(first_name="New F_Name Edit", last_name="New L_Name Edit")
    app.contact.edit_first(new_contact)


def test_edit_last_first_name(app):
    current_contact = Contact()
    app.contact.add_contact(current_contact)
    new_contact = Contact(first_name="F_Name Edit", last_name="L_Name Edit")
    app.contact.search(f"{current_contact.last_name} {current_contact.first_name}")
    app.contact.edit_first(new_contact)
