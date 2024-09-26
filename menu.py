from peewee import *

"""
A menu - you need to add the database and fill in the functions.
"""

db = SqliteDatabase('menu.sqlite')
class Record(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name}, {self.country}, {self.country}'

db.connect()
db.create_tables([Record])

Record.delete().execute()


def main():
    janne = Record(name='Janne Mustonen', country='Finland', catches=98)
    janne.save()

    ian = Record(name='Ian Stewart', country='Canada', catches=94)
    ian.save()

    aaron = Record(name='Aaron Gregg', country='Canada', catches=88)
    aaron.save()

    chad = Record(name='Chad Taylor', country='USA', catches=78)
    chad.save()

    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    # print('todo display all records')
    records = Record.select()
    for record in records:
        print(record)


def search_by_name():
    # print('todo ask user for a name, and print the matching record if found. What should the program do if the name is not found?')
    name = input('Enter name: ')
    try:
        records = Record.select().where(Record.name == name).get()
        print(records)

    except DoesNotExist:
        print(f'{name} does not exist.')


def add_new_record():
    # print('todo add new record. What if user wants to add a record that already exists?')
    name = input('Enter name: ')
    country = input('Enter country: ')
    catches = input(int('Enter catches: '))

    Record.create(name=name, country=country, catches=catches).save()


def edit_existing_record():
    # print('todo edit existing record. What if user wants to edit record that does not exist?')
    display_all_records()
    name = input('Enter the name you\'d like to edit: ')
    catches = input('Enter catches: ')

    Record.update(catches=catches).where(Record.name == name).execute()


def delete_record():
    # print('todo delete existing record. What if user wants to delete record that does not exist?')
    name = input('Enter name to delete: ')

    Record.delete().where(Record.name == name).execute()


if __name__ == '__main__':
    main()