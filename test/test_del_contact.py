# -*- coding: utf-8 -

from model.dto_contact import Contact


def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_contact(Contact())
    app.contact.delete_first()
    app.session.logout()


def test_delete_all_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contact.preparation_several_contacts(4)
    app.contact.delete_all()
    app.session.logout()
