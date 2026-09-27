import httpx 

URL = "https://api.wheretheiss.at/v1/satellites/25544" 

result = httpx.get(URL, timeout=10).json() 

print("===================================")
print(result)
print("===================================")

print(result["name"])

print(f"{result["latitude"]:1.2f}")

double = 90.11222
print(f"{double:90.1f}")

