from faker import Faker

fake = Faker()


def get_last_users(count=10):
    return [ fake.name() for _ in range(count) ]
