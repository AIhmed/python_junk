from requests_html import HTML,HTMLSession
session=HTMLSession()
r=session.get('https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas')
r.html.render(timeout=30)
print(r.html.html)
