import requests

def fetch_logs_from_api():
    url = "https://your-api-endpoint.com/logs"   # 🔁 replace this
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        logs = []
        for item in data:
            logs.append({
                "file_name": item.get("id", "api_log"),
                "content": item.get("log", "")
            })

        return logs

    else:
        print("❌ Failed to fetch logs")
        return []