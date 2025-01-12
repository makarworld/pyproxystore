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
proxystore.get_balance()
proxystore.get_category(nokey)
proxystore.get_price(count, period, category, country)
proxystore.get_count(country, category)
proxystore.get_country(category)
proxystore.get_proxy(state, order_id, comment, nokey)
proxystore.set_ip_auth(ids, ips)
proxystore.set_type(ids, proxy_type)
proxystore.set_descr(ids, comment, old_comment)
proxystore.buy(category, count, period, country, proxy_type, comment, username, password, generate_auth, coupon, nokey)
proxystore.prolong(period, ids, coupon, nokey)
proxystore.autoprolong(ids, enabled, coupon, nokey)
proxystore.delete(ids)
proxystore.check(ids)
```

# Main part of code was generated with [DuckDuckGo AI](https://duckduckgo.com/?q=DuckDuckGo+AI+Chat&ia=chat&duckai=1)