import os
import csv

filename='contacts.csv'

if not os.path.exists(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id','name','contact'])
print("Welcome to Simple Contact Book app")



class ContactBook:




    def getId(self):

        new_id = 1
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row or row[0]=='id':
                    continue
                new_id = max(new_id, int(row[0])+1)

        return max(new_id,1)

    def simple_Contact_Book(self):

        k = int(input("Enter 1 to show all contacts, enter 2 to add contact, enter 3 to delete contact, enter 4 to search contact, enter 5 to exit: "))

        if k==1:
            with open(filename, mode='r', newline='') as file:

                reader = csv.reader(file)

                for row in reader:
                    if(not row or row[0]=='id'):
                        continue
                    print(f'id: {row[0]}, name: {row[1]}, contact: {row[2]}')

                return None
        elif k == 2:

            id = self.getId()

            name = input("Please enter name of the person:")

            contact = input("Please enter contact number:")
            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([id, name, contact])
                return None


        elif k == 3:

            id_to_remove =  int(input("Please enter id of the person to be removed: "))
            rows = []
            found = False
            with open(filename, mode='r', newline='') as file:

                reader = csv.reader(file)

                header = next(reader)  # Save header
                for row in reader:
                    if row and row[0] == str(id_to_remove):
                        found = True  # Found the contact to delete
                    else:
                        rows.append(row)
            if found:
                # Write back all rows except the deleted one
                with open(filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)  # Write header back
                    writer.writerows(rows)
                print(f"Contact with ID {id_to_remove} deleted.")
                return None
            else:
                print(f"No contact found with ID {id_to_remove}.")
                return None

        elif k == 4:
            search = input("Please enter search term: ")
            with open(filename, mode='r', newline='') as file:

                reader = csv.reader(file)
                header = next(reader)
                rows = []

                for row in reader:

                    i = 0

                    while i<len(search) and i<len(row[1]):

                        if search[i]==row[1][i]:
                            i+=1

                        else:
                            break

                    if(i == len(search)):
                        rows.append(row)


                print(rows)

        elif k == 5 :
            return True
        return None


cb = ContactBook()
wannaBreak = False
while not wannaBreak:

    wannaBreak = cb.simple_Contact_Book()