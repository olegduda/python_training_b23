from faker import Faker

fake = Faker()
fake_ru = Faker('ru_RU')


class Contact:

    all_none = False

    def __init__(self, first_name=None, last_name=None, middle_name=None, group=None, id_contact=None, all_none=False):

        self.all_none = all_none

        self.id = id_contact
        self.first_name = self.field_fill_value(field_value=first_name, gen_value=fake_ru.first_name())
        self.last_name = self.field_fill_value(field_value=last_name, gen_value=fake_ru.last_name())
        self.middle_name = self.field_fill_value(field_value=middle_name, gen_value=fake_ru.middle_name())

        self.nickname = self.field_fill_value(gen_value=fake.user_name())
        self.title = self.field_fill_value(gen_value=fake.job())
        self.company = self.field_fill_value(gen_value=fake.company())
        self.address = self.field_fill_value(gen_value=fake.address())
        self.phone_home = self.field_fill_value(gen_value=fake.phone_number())
        self.phone_mobile = self.field_fill_value(gen_value=fake.phone_number())
        self.phone_work = self.field_fill_value(gen_value=fake.phone_number())
        self.phone_fax = self.field_fill_value(gen_value=fake.phone_number())
        self.email_one = self.field_fill_value(gen_value=fake.email())
        self.email_two = self.field_fill_value(gen_value=fake.company_email())
        self.email_three = self.field_fill_value(gen_value=fake.company_email())
        self.home_page = self.field_fill_value(gen_value=fake.hostname(2))
        self.b_day = self.field_fill_value(gen_value=str(fake.date_time().day))
        self.b_month = self.field_fill_value(gen_value=fake.month_name())
        self.b_year = self.field_fill_value(gen_value=fake.year())
        self.a_day = self.field_fill_value(gen_value=str(fake.date_time().day))
        self.a_month = self.field_fill_value(gen_value=fake.month_name())
        self.a_year = self.field_fill_value(gen_value=fake.year())
        self.group = self.field_fill_value(field_value=group)
        self.address_two = self.field_fill_value(gen_value=fake.address())
        self.phone_address_two = self.field_fill_value(gen_value=fake.phone_number())
        self.notes = self.field_fill_value(gen_value=fake.paragraph(nb_sentences=5))

    def field_fill_value(self, field_value=None, gen_value=None):
        if field_value is not None:
            first_name = field_value
        elif self.all_none is True:
            first_name = None
        else:
            first_name = gen_value
        return first_name

