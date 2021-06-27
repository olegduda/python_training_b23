from faker import Faker
from sys import maxsize


fake = Faker()
fake_ru = Faker('ru_RU')


class Contact:

    all_none = False

    def __init__(self, first_name=None, last_name=None, middle_name=None,
                 group=None, id_contact=None, address=None,
                 all_phones_from_home_page=None,
                 phone_home=None, phone_mobile=None, phone_work=None, phone_fax=None,
                 all_emails_from_home_page=None,
                 email_one=None, email_two=None, email_three=None,
                 phone_2=None,
                 all_none=False):

        self.all_none = all_none

        self.id = id_contact
        self.first_name = self.field_fill_value(field_value=first_name, gen_value=fake_ru.first_name())
        self.last_name = self.field_fill_value(field_value=last_name, gen_value=fake_ru.last_name())
        self.middle_name = self.field_fill_value(field_value=middle_name, gen_value=fake_ru.middle_name())

        self.nickname = self.field_fill_value(gen_value=fake.user_name())
        self.title = self.field_fill_value(gen_value=fake.job())
        self.company = self.field_fill_value(gen_value=fake.company())
        self.address = self.field_fill_value(field_value=address, gen_value=fake.address())

        self.all_phones_from_home_page = all_phones_from_home_page
        self.phone_home = self.field_fill_value(field_value=phone_home, gen_value=fake.phone_number())
        self.phone_mobile = self.field_fill_value(field_value=phone_mobile, gen_value=fake.phone_number())
        self.phone_work = self.field_fill_value(field_value=phone_work, gen_value=fake.phone_number())
        self.phone_fax = self.field_fill_value(field_value=phone_fax, gen_value=fake.phone_number())

        self.all_emails_from_home_page = all_emails_from_home_page
        self.email_one = self.field_fill_value(field_value=email_one, gen_value=fake.email())
        self.email_two = self.field_fill_value(field_value=email_two, gen_value=fake.company_email())
        self.email_three = self.field_fill_value(field_value=email_three, gen_value=fake.company_email())
        self.home_page = self.field_fill_value(gen_value=fake.hostname(2))
        self.b_day = self.field_fill_value(gen_value=str(fake.date_time().day))
        self.b_month = self.field_fill_value(gen_value=fake.month_name())
        self.b_year = self.field_fill_value(gen_value=fake.year())
        self.a_day = self.field_fill_value(gen_value=str(fake.date_time().day))
        self.a_month = self.field_fill_value(gen_value=fake.month_name())
        self.a_year = self.field_fill_value(gen_value=fake.year())
        self.group = self.field_fill_value(field_value=group)
        self.address_two = self.field_fill_value(gen_value=fake.address())
        self.phone_2 = self.field_fill_value(field_value=phone_2, gen_value=fake.phone_number())
        self.notes = self.field_fill_value(gen_value=fake.paragraph(nb_sentences=5))

    def __repr__(self):
        return f"{self.id}:{self.first_name}:{self.last_name}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def field_fill_value(self, field_value=None, gen_value=None):
        if field_value is not None:
            first_name = field_value
        elif self.all_none is True:
            first_name = None
        else:
            first_name = gen_value
        return first_name

    @staticmethod
    def found_by_name_in_list(first_name, last_name, list_contacts):
        for contact in list_contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None

    @staticmethod
    def update_list_by_id(contact, list_contacts):
        new_list = []
        for old_contact in list_contacts:
            if old_contact.id == contact.id:
                old_contact = contact
            new_list.append(old_contact)
        return new_list

