contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

AliceNumber = contacts["Alice"]
print(f"Alice's number: {AliceNumber}")

contacts["Diana"] = "555-4321"
print(f"Contacts after adding diana: {contacts}" )
del contacts["Charlie"]
print(f"Contacts after deleting charlie: {contacts}")
print(f"All names: {contacts.keys()}")
print(f"All numbers: {contacts.values()}")
print(f"Total contacts: {len(contacts)}")


