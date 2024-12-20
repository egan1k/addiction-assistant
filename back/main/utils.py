from django.utils import timezone

from dateutil.relativedelta import relativedelta


def smart_capitalize(string):
    words = string.split(" ")
    result = ["{}{}".format(word[0].upper(), word[1:]) for word in words if word]
    return " ".join(result)

def generate_username(user):
    first_name = smart_capitalize(user.first_name)
    last_name = smart_capitalize(user.last_name)
    simple_username = f"{first_name}{last_name}"
    if not simple_username:
        simple_username = smart_capitalize(user.email.split("@")[0])

    username = ""
    set_next_symbol_is_upper = False
    for symbol in simple_username:
        if symbol.isalpha():
            if set_next_symbol_is_upper:
                username += symbol.upper()
            else:
                username += symbol
            set_next_symbol_is_upper = False
        elif symbol.isdigit():
            username += symbol
        else:
            set_next_symbol_is_upper = True
    return username

def generate_unique_username(user, model):
    username = generate_username(user)
    qs = model.objects.all()
    if user.pk:
        qs = qs.exclude(pk=user.pk)
    for i in range(1000):
        postfix = str(i) if i else ""
        if not qs.filter(username=username + postfix).exists():
            return username + postfix

def block_user(user):
    user.is_locked = True
    user.locked_until = timezone.now() + relativedelta(days=1)
    user.save(update_fields=["is_locked", "locked_until"])

def get_client_ipv4(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip