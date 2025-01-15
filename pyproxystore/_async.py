from curl_cffi import requests


class ProxyStore:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.base_uri = f"https://proxy-store.com/api/{api_key}/"

        self.session = requests.AsyncSession()

    async def request(
        self, command: str, params: dict = {}, data: dict = {}, method: str = "GET"
    ) -> dict:
        """
        Make a request to the MobileProxy API.

        :param params: Query parameters to send with the request.
        :param data: Data to send with the request.
        :param method: HTTP method to use for the request. Default is "GET".
        :return: The response from the API as a dictionary.
        """
        response = self.session.request(
            method=method, url=self.base_uri + command, params=params, data=data
        )
        try:
            return response.json()
        except Exception as e:
            print(f"Error: {e}. Response code: {response.status_code}")
            print(response.content)
            return {"error": str(e)}

    async def get_balance(self) -> dict:
        """
        Get info about an account balance.

        Response:
        {
            "status": "ok",
            "balance": "100",
            "currency": "USD"
        }

        :return: The response from the API as a dictionary.
        """
        return await self.request("getbalance")

    async def get_category(self, nokey: bool = False) -> dict:
        """
        Get the list of available categories

        Arguments:
            nokey - When this argument is included (nokey=1), the list will be returned without keys.

        Response:
        {
            "status": "ok",
            "list": [
                {
                    "id": "for_al",
                    "name": "List of all sites"
                }
            ]
        }

        :param nokey: When this argument is included (nokey=1), the list will be returned without keys.
        :type nokey: bool

        :return: The response from the API as a dictionary.
        """
        params = {"nokey": nokey}
        return await self.request("getcategory", params)

    async def get_price(self, count: int, period: int, category: str, country: str) -> dict:
        """
        Get info about the order amount depending on the period and number of proxies.

        Arguments:
            count (int): Number of proxies.
            period (int): Number of days.
            category (str): Purchase category (from getcategory attribute).
            country (str): ISO two-letter code for the country.

        Response:
        {
            "status": "ok",
            "price": 1800,
            "category": "for_all",
            "price_single": 0.6,
            "period": 30,
            "country": "us",
            "count": 100
        }

        :return: The response from the API as a dictionary.
        """
        params = {
            "count": count,
            "period": period,
            "category": category,
            "country": country,
        }
        return await self.request("getprice", params=params)

    async def get_count(self, country: str = None, category: str = None) -> dict:
        """
        Get the number of certain countries' proxies available for purchasing.

        Arguments:
            country (str): The two-letter ISO country code for the given country (optional).
            category (str): Purchase category (from getcategory attribute, optional).

        Response:
        {
            "status": "ok",
            "count": 971
        }

        :return: The response from the API as a dictionary.
        """
        params = {}
        if country:
            params["country"] = country
        if category:
            params["category"] = category

        return await self.request("getcount", params=params)

    async def get_country(self, category: str) -> dict:
        """
        Get info about available countries for purchase.

        Arguments:
            category (str): Purchase category (from getcategory attribute).

        Response:
        {
            "status": "ok",
            "list": ["ru", "ua", "us"]
        }

        :return: The response from the API as a dictionary.
        """
        params = {"category": category}
        return await self.request("getcountry", params=params)

    async def get_proxy(
        self,
        state: str = "all",
        order_id: str = None,
        comment: str = None,
        nokey: bool = False,
    ) -> dict:
        """
        Get the list of your proxies.

        Arguments:
            state (str): The state of the proxies returned. Available values: active, expiring, all (default).
            order_id (str): Internal order number (optional).
            comment (str): A comment specified for a proxy (optional).
            nokey (bool): When this argument is included (nokey=1), the list will be returned without keys.

        Response:
        {
            "status": "ok",
            "list_count": 4,
            "list": {
                "11": {
                    "id": 11,
                    "ip": "185.22.134.250",
                    "port": "7330",
                    "user": "5svBNZ",
                    "pass": "iagn2d",
                    "type": "http",
                    "country": "ru",
                    "date": "2016-06-19 16:32:39",
                    "date_end": "2016-07-12 11:50:41",
                    "unixtime": 1466379159,
                    "unixtime_end": 1468349441,
                    "comment": "",
                    "active": 1,
                    "category": "for_all"
                }
            }
        }

        :return: The response from the API as a dictionary.
        """
        params = {"state": state, "nokey": 1 if nokey else 0}
        if order_id:
            params["order_id"] = order_id
        if comment:
            params["comment"] = comment

        return await self.request("getproxy", params=params)

    async def set_ip_auth(self, ids: str, ips: str) -> dict:
        """
        Used to indicate IPs acceptable for proxy authorization (up to 3 pcs).

        Arguments:
            ids (str): Comma-separated list of internal IDs for the proxies in our system.
            ips (str): IP list separated by commas (up to 3 pcs).

        Response:
        {
            "status": "ok"
        }

        :return: The response from the API as a dictionary.
        """
        params = {"ids": ids, "ips": ips}
        return await self.request("setipauth", params=params)

    async def set_type(self, ids: str, proxy_type: str) -> dict:
        """
        Used to change the protocol of the proxies list.

        Arguments:
            ids (str): Comma-separated list of internal ID numbers for the proxies in our system.
            proxy_type (str): Set type (protocol): http - HTTPS, or socks - SOCKS5.

        Response:
        {
            "status": "ok"
        }

        :return: The response from the API as a dictionary.
        """
        params = {"ids": ids, "type": proxy_type}
        return await self.request("settype", params=params)

    async def set_descr(self, ids: str, comment: str, old_comment: str) -> dict:
        """
        Used to update the technical comment to the proxies list.

        Arguments:
            ids (str): Comma-separated list of internal ID numbers in our system.
            comment (str): New comment value (maximum length is 50 characters).
            old_comment (str): The comment that you wish to change.

        Response:
        {
            "status": "ok",
            "count": 4
        }

        :return: The response from the API as a dictionary.
        """
        params = {"old_comment": old_comment, "comment": comment, "ids": ids}
        return await self.request("setdescr", params=params)

    async def buy(
        self,
        category: str,
        count: int,
        period: int,
        country: str,
        proxy_type: str = "http",
        comment: str = None,
        username: str = None,
        password: str = None,
        generate_auth: int = 0,
        coupon: str = "h8B9bMDD", # support dev | 5% discount
        nokey: bool = False,
    ) -> dict:
        """
        Used to buy proxies.

        Arguments:
            category (str): Purchase category (from getcategory attribute).
            count (int): The number of proxies to purchase.
            period (int): The period, specified as the number of days, for which the proxies are being purchased.
            country (str): The country, represented by the ISO two-letter country code.
            proxy_type (str): Type of proxy (protocol): socks, or http (default).
            comment (str): Comment for the list of proxies (maximum length 50 characters).
            username (str): Login for authorization via a proxy (optional).
            password (str): Password for authorization via a proxy (optional).
            generate_auth (int): Login/password generation (1 - enable, 0 - disable).
            coupon (str): Promocode (optional).
            nokey (bool): When this argument is included (nokey=1), the list will be returned without keys.

        Response:
        {
            "status": "ok",
            "order_id": 100000,
            "count": 1,
            "price": 6.3,
            "price_single": 0.9,
            "period": 7,
            "country": "ru",
            "list": {
                "15": {
                    "id": 15,
                    "ip": "185.22.134.250",
                    "port": "7330",
                    "user": "5svBNZ",
                    "pass": "iagn2d",
                    "type": "http",
                    "country": "ru",
                    "date": "2016-06-19 16:32:39",
                    "date_end": "2016-07-12 11:50:41",
                    "unixtime": 1466379159,
                    "unixtime_end": 1468349441,
                    "comment": "",
                    "active": 1,
                    "category": "for_all"
                }
            }
        }

        :return: The response from the API as a dictionary.
        """
        params = {
            "category": category,
            "count": count,
            "period": period,
            "country": country,
            "type": proxy_type,
            "generate_auth": generate_auth,
            "nokey": 1 if nokey else 0,
        }

        if comment:
            params["comment"] = comment
        if username:
            params["username"] = username
        if password:
            params["password"] = password
        if coupon:
            params["coupon"] = coupon

        return await self.request("buy", params=params)

    async def prolong(
        self, period: int, ids: str, coupon: str = None, nokey: bool = False
    ) -> dict:
        """
        Used to renew current proxies.

        Arguments:
            period (int): Period for which you are extending the proxies, expressed as the number of days.
            ids (str): Comma-separated list of internal IDs for the proxies in our system.
            coupon (str): Promocode (optional).
            nokey (bool): When this argument is included (nokey=1), the list will be returned without keys.

        Response:
        {
            "status": "ok",
            "period": 30,
            "price": 12.6,
            "count": 2,
            "list": {
                "15": {
                    "id": 15,
                    "date_end": "2016-07-12 11:50:41",
                    "unixtime_end": 1468349441
                },
                "16": {
                    "id": 16,
                    "date_end": "2016-07-16 09:31:21",
                    "unixtime_end": 1466379261
                }
            }
        }

        :return: The response from the API as a dictionary.
        """
        params = {
            "period": period,
            "ids": ids,
            "coupon": coupon,
            "nokey": 1 if nokey else 0,
        }
        return await self.request("prolong", params=params)

    async def autoprolong(
        self, ids: str, enabled: int, coupon: str = None, nokey: bool = False
    ) -> dict:
        """
        Used to auto-renew current proxies.

        Arguments:
            ids (str): Comma-separated list of internal IDs for the proxies in our system.
            enabled (int): 1 to enable auto-renewal, 0 to disable.
            coupon (str): Promocode (optional).
            nokey (bool): When this argument is included (nokey=1), the list will be returned without keys.

        Response:
        {
            "code": 200,
            "data": {
                "15": {
                    "status": "success",
                    "enabled": true
                },
                "16": {
                    "status": "success",
                    "enabled": true
                }
            }
        }

        :return: The response from the API as a dictionary.
        """
        params = {
            "ids": ids,
            "enabled": enabled,
            "coupon": coupon,
            "nokey": 1 if nokey else 0,
        }
        return await self.request("autoprolong", params=params)

    async def delete(self, ids: str) -> dict:
        """
        Used to remove proxies.

        Arguments:
            ids (str): Comma-separated list of internal IDs for the proxies in our system.

        Response:
        {
            "status": "ok",
            "count": 2
        }

        :return: The response from the API as a dictionary.
        """
        params = {"ids": ids}
        return await self.request("delete", params=params)

    async def check(self, ids: str) -> dict:
        """
        Used to check the validity of the proxy.

        Arguments:
            ids (str): Internal ID for the proxy in our system.

        Response:
        {
            "status": "ok",
            "proxies": [
                {
                    "proxy_id": "15",
                    "proxy_status": true
                }
            ]
        }

        :return: The response from the API as a dictionary.
        """
        params = {"ids": ids}
        return await self.request("check", params=params)
