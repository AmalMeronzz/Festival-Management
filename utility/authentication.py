from AdminMainApp.models import UserMaster
from django.http import HttpResponseRedirect

def authenticate(func):
    def wrapper(*args, **kwargs):
        request = kwargs['request']
        user = request.session.get('AdminId')
        is_authenticated = UserMaster.objects.filter(login_id=user).exists ()
        if is_authenticated:
            return  func(*args, **kwargs)
        else:
            return HttpResponseRedirect('/login')
    return wrapper


def customauthenticate(*args, **kwargs):
    def authenticate(func):

        print('reached 11111111')
        def wrapper(request,*args, **kwargs):
            print(request)
            print('reached 2222222222')
            print(args)
            print(kwargs)
            print('---------------------')


            user = request.session.get('AdminId')
            print(user)
            print('dddddd')
            if user is not None:
                print('sksksksksskskskskksks')
                is_authenticated = UserMaster.objects.filter(login_id=user).exists()
                print(is_authenticated)
                print('reeeeeeeeeeee')
                if is_authenticated:
                    print('dddddddddddddddddddddddddwwwwwwwwwww')
                    return func(*args, **kwargs)

            return HttpResponseRedirect('/login')

        return wrapper

    return authenticate