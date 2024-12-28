import re

users_list = [
    {
        "id": "user1",
        "nombre": "jose",
        "correo": "jose@example.com",
        "años": 30,
        "sexo": "masculino",
        "telefono": "+123456789",
    },
    {
        "id": "user2",
        "nombre": "Alicia",
        "correo": "alicia@example.com",
        "años": 28,
        "sexo": "femenino",
        "telefono": "+987654321",
    },
    {
        "id": "user3",
        "nombre": "Bruno",
        "correo": "bruno@example.com",
        "años": 35,
        "sexo": "masculino",
        "telefono": "+192837465",
    },
]

# Find a pattern inside users' emails
pattern = r"example.com"
matched_users = []

# Loop through users and check if their email matches the pattern
for user in users_list:
    if "correo" in user and re.search(pattern, user["correo"]):
        matched_users.append(user)

# Create a dictionary to track the count of each domain
domain_count = {}

# Extract domains from matched users
for user in matched_users:
    domain = re.search(r"@(.+)", user["correo"]).group(1).upper()

    # Update the domain count in the dictionary
    if domain in domain_count:
        domain_count[domain] += 1
    else:
        domain_count[domain] = 1

# Print email addresses and the count of domains
for user in matched_users:
    correoUpper = user["correo"].upper()  # Convert only the email to uppercase
    print(correoUpper)

    # Extract domain
    domain = re.search(r"@(.+)", user["correo"]).group(1).upper()

    # Get the count of this domain from the dictionary
    countDomain = domain_count[domain]
    print(
        f"Domain: {domain} | Total number of occurrences of this domain: {countDomain}"
    )

# set creates a new list reming  duplicated items from a list

newUsers = ["jose", "jose", "jose", "Alicia", "bruno"]
removeDuplicated = set(newUsers)
print(f"New users are {removeDuplicated}")
