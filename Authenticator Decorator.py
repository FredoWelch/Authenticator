user1 = {
    'name': 'Sorna',
    'valid': False
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            print('No access')

    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
