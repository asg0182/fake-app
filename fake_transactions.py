import csv
import datetime
import random
from faker import Faker


fake = Faker()


def generate_info(url):
    return [
        fake.name(),
        fake.date_of_birth(),
        fake.job(),
        fake.company() + ' ' + fake.company_suffix(),
        fake.country(),
        fake.city(),
        fake.address(),
        fake.zipcode(),
        fake.phone_number(),
        fake.email(),
        fake.credit_card_number(),
        fake.credit_card_expire(),
        fake.credit_card_security_code(),
        url
    ]


def main():
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d-%H-%M-%S")
    url = fake.url()
    count = random.randint(5221, 198765)
    columns = [
        "name", "birth", "job", "company", "country", "city", 
        "address", "zip_code", "phone", "email", "card_number", 
        "card_expire", "security_code", "url"
        ]
    with open(f"data-{now_str}.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        writer.writerow(columns)
        for _ in range(count):
            writer.writerow(generate_info(url=url))


if __name__=="__main__":
    main()
