import requests

url = "https://api.weather.gov/alerts"

# so i dont get blocked by the API
headers = {"User-Agent": "NoaaAlertFetcher/1.0 (https://github.com/myproject)"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    # extract and list the alerts
    alerts = data.get("features", [])
    for alert in alerts:
        properties = alert.get("properties", {})
        print(f"Title: {properties.get('headline', 'No Title')}")
        print(f"Description: {properties.get('description', 'No Description')}")
        print(f"Severity: {properties.get('severity', 'Unknown')}")
        print(f"Effective: {properties.get('effective', 'Unknown')}")
        print(f"Expires: {properties.get('expires', 'Unknown')}")
        print("-" * 40)
else:
    print(f"Failed to retrieve alerts: {response.status_code}")
