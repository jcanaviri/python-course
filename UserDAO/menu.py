from UserDAO import UserDAO
from logger_file import log
from User import User

while True:
    print("""What do you want to do?
    1.- See all the users
    2.- Add a new user
    3.- Update a user
    4.- Delete a user
    5.- Exit""")
    option = int(input('> '))

    if option == 1:
        users = UserDAO.select()
        for user in users:
            log.debug(user)
    elif option == 2:
        username = input('Username: ')
        password = input('Password: ')

        new_user = User(username=username, password=password)
        result = UserDAO.insert(new_user)
        log.debug(f'Users inserted: {result}')
    elif option == 3:
        update_id = input('Update id: ')
        username = input('New username: ')
        password = input('New password: ')

        update_user = User(user_id=update_id, username=username, password=password)

        result = UserDAO.update(update_user)
        log.debug(f'Users update: {result}')
    elif option == 4:
        delete_id  = input('Delete id: ')
        delete_user = User(user_id=delete_id)
        deleted = UserDAO.delete(delete_user)
        log.debug(f'People deleted: {deleted}')
    elif option == 5:
        break
print('Goodbye')
