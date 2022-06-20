import hmac
import base64
import hashlib
from datetime import datetime
from urllib.parse import urljoin
import requests
import json
import time
from requests.adapters import HTTPAdapter


class Client:
    """
    basic API
    """

    def __init__(self, api_key, secret_key, passphrase, simulated_trade=False, server_time=False) -> None:
        self._api_key = api_key
        self._secret_key = secret_key
        self._passphrase = passphrase
        self._simulated_trade = simulated_trade
        self._server_time = server_time
        self._server = "https://www.okx.com/"
        self._session = self._create_session()

    def _create_session(self):
        session = requests.session()
        session.keep_alive = False
        return session

    def _request(self, method: str, endpoint: str, params=None) -> requests.Response:
        response = None
        method = method.upper()
        self._timestamp = self.get_timestamp()
        if params is None or method == "GET":
            body = ""
            endpoint = endpoint + self._parse_params(params)
        else:
            body = json.dumps(params)
        url = urljoin(self._server, endpoint)
        try:
            self._sign = self._generage_sign(self._timestamp, method, endpoint, body, self._secret_key)
            header = self.generate_header()
            response = self._session.request(method, url, headers=header, data=body)
        except Exception as e:
            print(f"request failed with error: {e}")
        return response.json() if response else {}

    def _generage_sign(self, timestamp, method, request_path, body, secret_key):
        message = timestamp + method + request_path + body
        mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod=hashlib.sha256)
        d = mac.digest()
        return base64.b64encode(d)
    
    def generate_header(self):
        header = dict()
        header['Content-Type'] = 'application/json'
        header['OK-ACCESS-KEY'] = self._api_key
        header['OK-ACCESS-SIGN'] = self._sign
        header['OK-ACCESS-TIMESTAMP'] = self._timestamp
        header['OK-ACCESS-PASSPHRASE'] = self._passphrase
        header['x-simulated-trading'] = '1' if self._simulated_trade else '0'
        return header

    def get_timestamp(self):
        if self._server_time is True:
            resp = self._session.get("https://www.okex.com/api/v5/public/time")
            if resp.status_code == 200:
                return resp.json()['ts']
        now = datetime.utcnow()
        t = now.isoformat("T", "milliseconds") + "Z"
        return t

    def _parse_params(self, params: dict) -> str:
        res = "?"
        for k, v in params.items():
            if v is not None:
                res += f"{k}={v}&"
        return res[:-1]
