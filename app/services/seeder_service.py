import string
from random import randint

from app import db
from app.models import User, Group


def seed_data():
    hafsah = random_user()
    musab = random_user()
    mama = random_user()
    group = random_group()
    db.session.add(hafsah)
    db.session.add(musab)
    db.session.add(mama)
    db.session.commit()
    group.creator_phone_number = hafsah.phone_number
    db.session.add(group)
    db.session.commit()


def random_phone_number():
    return str(randint(1000000000, 99999999999))


def random_string(length=15):
    import random
    return ''.join(random.choice(string.lowercase) for x in range(length))


def random_email():
    return random_string() + "@" + random_string() + ".com"


def random_user():
    return User(
        phone_number=random_phone_number(),
        first_name=random_string(),
        last_name=random_string(),
        email=random_email(),
        username=random_string()
    )


def random_group():
    return Group(
        group_name=random_string()
    )
