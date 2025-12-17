#Implement a phone directory with add, search, update, and delete options.
class PhoneDirectory:
    def __init__(self):
        self.directory = {}

    def add_contact(self, name, phone_number):
        if name in self.directory:
            return f"Contact '{name}' already exists."
        self.directory[name] = phone_number
        return f"Contact '{name}' added successfully."

    def search_contact(self, name):
        return self.directory.get(name, f"Contact '{name}' not found.")

    def update_contact(self, name, new_phone_number):
        if name not in self.directory:
            return f"Contact '{name}' not found."
        self.directory[name] = new_phone_number
        return f"Contact '{name}' updated successfully."

    def delete_contact(self, name):
        if name not in self.directory:
            return f"Contact '{name}' not found."
        del self.directory[name]
        return f"Contact '{name}' deleted successfully."
# Example usage
if __name__ == "__main__":
    phone_directory = PhoneDirectory()
    
    # Add contacts
    print(phone_directory.add_contact("Alice", "123-456-7890"))
    print(phone_directory.add_contact("Bob", "987-654-3210"))
    
    # Search contacts
    print(phone_directory.search_contact("Alice"))
    print(phone_directory.search_contact("Charlie"))
    
    # Update contact
    print(phone_directory.update_contact("Bob", "111-222-3333"))
    print(phone_directory.update_contact("Charlie", "444-555-6666"))
    
    # Delete contact
    print(phone_directory.delete_contact("Alice"))
    print(phone_directory.delete_contact("Charlie"))
    
    # Final directory state
    print("Final Phone Directory:", phone_directory.directory)
    