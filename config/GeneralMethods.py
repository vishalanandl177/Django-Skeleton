import re
import base64
from django.http import JsonResponse
from rest_framework.status import HTTP_400_BAD_REQUEST, \
    HTTP_405_METHOD_NOT_ALLOWED, HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR


class GeneralMethods:

    def isValidEmail(self, email):
        if re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", email) is None:
            return False
        return True

    def encode(self, key, clear):
        enc = []
        for i in range(len(clear)):
            key_c = key[i % len(key)]
            enc_c = (ord(clear[i]) + ord(key_c)) % 256
            enc.append(enc_c)
        return base64.urlsafe_b64encode(bytes(enc)).decode('utf-8')

    def decode(self, key, enc):
        dec = []
        enc = base64.urlsafe_b64decode(enc)
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + enc[i] - ord(key_c)) % 256)
            dec.append(dec_c)
        return "".join(dec)

    def clientError(self, message):
        response = dict()
        response['status'] = 'error'
        response['description'] = message
        return JsonResponse(response, status=HTTP_400_BAD_REQUEST)

    def generateResponse(self, data):
        response = dict()
        response['status'] = 'success'
        response['result'] = data
        return JsonResponse(response, status=HTTP_200_OK)

    def errorResponse(self):
        response = dict()
        response['status'] = 'error'
        response['description'] = 'Server Exception'
        return JsonResponse(response, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def noDataFound(self):
        response = dict()
        response['status'] = 'success'
        response['description'] = 'No Data Found'
        return JsonResponse(response, status=HTTP_200_OK)

    def paramMissing(self):
        response = dict()
        response['status'] = 'error'
        response['description'] = 'Required params missing/incorrect(Bad request)'
        return JsonResponse(response, status=HTTP_400_BAD_REQUEST)

    def unAuthorized(self):
        response = dict()
        response['status'] = 'error'
        response['description'] = 'Unauthorized'
        return JsonResponse(response, status=HTTP_401_UNAUTHORIZED)

    def methodNotAllowed(self):
        response = dict()
        response['status'] = 'error'
        response['description'] = 'Method Not Allowed'
        return JsonResponse(response, status=HTTP_405_METHOD_NOT_ALLOWED)
