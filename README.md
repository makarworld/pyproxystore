# pyproxystore - Unofficial python library for working with proxy-store.com

Site: https://proxy-store.com/

Docs: https://proxy-store.com/en/developers

> pip install pyproxystore

Example:
```python
from pyproxystore import ProxyStore

api_key = "YOUR_API_KEY"
proxystore = ProxyStore(api_key)

print(proxystore.get_balance())
```

Methods:
```python
# No Authorization needed
mobileproxy.change_ip(proxy_key, user_agent, format="json")

# Common methods
mobileproxy.get_balance()
mobileproxy.get_ipstat()
mobileproxy.get_geo_operator_list(equipments_back_list=None, operators_back_list=None, show_count_null=None)
mobileproxy.get_operators_list(proxy_id=None, geoid=None)
mobileproxy.get_id_country(lang)
mobileproxy.get_id_city(lang)
mobileproxy.get_geo_list(proxy_id=None, geoid=None)
mobileproxy.get_price(id_country)
mobileproxy.see_the_url_from_different_IPs(url, id_country=None)
mobileproxy.get_task_result(tasks_id)

# Proxy methods
mobileproxy.buy_proxy(operator, geoid, proxy_id, period, num, coupons_code=None, id_country=None, id_city=None, auto_renewal=None)
mobileproxy.edit_proxy(proxy_id, proxy_reboot_time=None, proxy_ipauth=None, proxy_comment=None)
mobileproxy.get_ip(proxy_id)
mobileproxy.get_black_list(proxy_id)
mobileproxy.add_operator_to_black_list(proxy_id, operator_id)
mobileproxy.remove_operator_from_black_list(proxy_id, operator_id)
mobileproxy.remove_black_list(proxy_id, black_list_id=None, eid=None)
mobileproxy.get_my_proxy(proxy_id)
mobileproxy.change_proxy_login_password(proxy_id, proxy_login, proxy_pass)
mobileproxy.reboot_proxy(proxy_id)
mobileproxy.change_equipment(operator, geoid, proxy_id, add_to_black_list, id_country, id_city, eid)
```

# Main part of code was generated with [DuckDuckGo AI](https://duckduckgo.com/?q=DuckDuckGo+AI+Chat&ia=chat&duckai=1)