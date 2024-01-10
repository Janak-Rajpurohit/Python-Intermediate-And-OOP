import requests
r=requests.get("https://hdhub4u.app/category/south-hindi-movies/")
print(r.text)       ## source code
#print(r.status_code)       ## status code 

url="https://hdhub4u.app/category/south-hindi-movies/"
data={1:"one",2:"two"}

r2=requests.post(url=url,data=data)
print(r2)


