# -*- coding: utf-8 -

from model.dto_contact import Contact


def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_contact(Contact())
    app.contact.delete_first()
    app.session.logout()
