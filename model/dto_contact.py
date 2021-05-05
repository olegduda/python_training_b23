from faker import Faker

fake = Faker()
fake_ru = Faker('ru_RU')


class Contact:

    def __init__(self, first_name="", last_name="", group=None):
        if first_name != "":
            self.first_name = first_name
        else:
            self.first_name = fake_ru.first_name()
        if last_name != "":
            self.last_name = last_name
        else:
            self.last_name = fake_ru.last_name()

        self.middle_name = fake_ru.middle_name()
        self.nickname = fake.user_name()
        self.title = fake.job()
        self.company = fake.company()
        self.address = fake.address()
        self.phone_home = fake.phone_number()
        self.phone_mobile = fake.phone_number()
        self.phone_work = fake.phone_number()
        self.phone_fax = fake.phone_number()
        self.email_one = fake.email()
        self.email_two = fake.company_email()
        self.email_three = fake.company_email()
        self.home_page = fake.hostname(2)
        self.b_day = str(fake.date_time().day)
        self.b_month = fake.month_name()
        self.b_year = fake.year()
        self.a_day = str(fake.date_time().day)
        self.a_month = fake.month_name()
        self.a_year = fake.year()
        self.group = group
        self.address_two = fake.address()
        self.phone_address_two = fake.phone_number()
        self.notes = fake.paragraph(nb_sentences=5)




