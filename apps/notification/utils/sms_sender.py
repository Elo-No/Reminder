import base64
import hashlib
import hmac
import time
import urllib.parse
from abc import ABC, abstractmethod
import requests
from decouple import config
import http.client


class AbstractSMSHandler(ABC):

    @abstractmethod
    def header_maker(self):
        pass

    @abstractmethod
    def secret_revealed(self):
        pass

    @abstractmethod
    def url_maker(self):
        pass

    @abstractmethod
    def signature_generator(self):
        pass

    @abstractmethod
    def passphrase_generator(self):
        pass

    @abstractmethod
    def dispatcher(self):
        pass


class SMSHandler(AbstractSMSHandler):
    user_secrets = None

    def __init__(self, data):
        # user, provider_api, message, receptor, line_number, send_date, check_id,endpoint: str, method: str, params: dict = None, sandbox: bool = False):
        """

        :param user: a user instance to get phone's user
        :param endpoint: used for calling the endpoint of sms's ghasedak
        :param method: The method we want to use to send request . also needed for creating api sign
        :param params: take any accepted parameter by the ghasedak endpoint and sends with the request
        :param sandbox: to get the main url
        """
        self.user = data['user']
        self.method = data['method']
        self.provider_api = data['provider_api']
        self.messages = data['messages']
        self.line_number = data['line_number']
        self.send_date = data['send_date']
        self.check_id = data['check_id']

    def header_maker(self) -> dict:
        """
        according to the docs of ghasedak , this whole header is needed to be sent with request to authenticate
        :return:
        """
        return {
            'content-type': "application/x-www-form-urlencoded",
            'apikey': config('GHASEDAK_APIKEY'),
            'cache-control': "no-cache",
        }

    def url_maker(self) -> str:
        """
        provides the url we need to send request
        :return:
        """
        url = self.provider_api
        payload = {
            'message': self.message,
            'receptor': self.user.phone_number,
            'linenumber': self.line_number,
            'senddate': self.send_date,
            'checkid': self.check_id
        }
        return payload, url

    def dispatcher(self) -> dict:
        """
        we dispatch the request with the generated credentials
        we use method variable to determine the method
        generate url by calling url_maker method
        add headers and params that we generated above
        :return:
        """
        payload, url = self.url_maker()
        res = requests.request(
            method=self.method, url=url, payload=payload, headers=self.header_maker())
        result = {}
        if res.status_code != 200:
            result = {'Error': True , 'data' : res}
        result = {'Error': False , 'data' : res}
        return result
       