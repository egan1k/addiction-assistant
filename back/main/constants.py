from djchoices import ChoiceItem, DjangoChoices

class AccountType(DjangoChoices):
    admin = ChoiceItem('admin', 'Admin')
    stuff = ChoiceItem('stuff', 'Stuff')
    regular_user = ChoiceItem('regular_user', 'Regular User')

DASHBOARD_ONLY_ACCESS_ACCOUNT_TYPES = [AccountType.admin, AccountType.stuff]
