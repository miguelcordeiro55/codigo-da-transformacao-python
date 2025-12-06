from faker import Faker

fake = Faker()

print("=== Gerando dados falsos ===")
print("Nome:", fake.name())
print("Email:", fake.email())
print("Endereço:", fake.address())
print("Data de nascimento:", fake.date_of_birth())