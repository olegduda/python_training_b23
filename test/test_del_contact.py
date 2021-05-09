# -*- coding: utf-8 -

from model.dto_contact import Contact


def test_delete_first_contact(app):
    app.contact.add_contact(Contact())
    app.contact.delete_first()


def test_delete_all_contacts(app):
    app.contact.preparation_several_contacts(4)
    app.contact.delete_all()
