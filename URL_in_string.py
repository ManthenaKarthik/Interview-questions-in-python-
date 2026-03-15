from urllib.parse import urlparse

s = 'My Profile: https://www.geeksforgeeks.org/404.html/ in the portal of https://www.geeksforgeeks.org/'
s1= s.split()

urls = []
for word in s1:
    parsed = urlparse(word)
    if parsed.scheme and parsed.netloc:
        urls.append(word)
print("URLs:", urls)