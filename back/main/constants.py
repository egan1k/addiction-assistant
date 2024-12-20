from djchoices import ChoiceItem, DjangoChoices

class AccountType(DjangoChoices):
    admin = ChoiceItem('admin', 'Admin')
    stuff = ChoiceItem('stuff', 'Stuff')
    regular_user = ChoiceItem('regular_user', 'Regular User')