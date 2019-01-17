from rest_framework import authentication
from config.is_development import is_development


class ValidateAuth(authentication.BaseAuthentication):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        path = request.get_full_path()

        '''
            For admin, don't check middleware.
            For development, don't check middleware.
        '''

        if 'admin' in path.split('/') or is_development:
            return self.get_response(request)

        '''
            Making sure middleware to run before View
            Write code here, will run before view.py
        '''
        response = self.get_response(request)

        '''
            Write code here, will run after view.py
        '''

        return response
