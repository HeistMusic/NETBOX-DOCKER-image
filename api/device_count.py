
"""
NetBox API script to count devices by status.

Usage:
    python device_count.py --url http://localhost:8000 --token <API_TOKEN>
    python device_count.py --url http://localhost:8000 --token <API_TOKEN> --status active
"""

import argparse
import requests
import sys
from collections import Counter

# FUNCTION TO GET DEVICES FROM NETBOX API
def get_devices(netbox_url, token, status=None):

    # SET HEADERS
    headers = {
        "Authorization": f"Token {token}",
        "Accept": "application/json",
    }
    
    # BUILD QUERY PARAMETERS
    params = {}
    if status:
        params["status"] = status

    # PAGINATED REQUESTS
    url = f"{netbox_url.rstrip('/')}/api/dcim/devices/"

    # COLLECT DEVICES
    devices = []
    while url:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise RuntimeError(
                f"API request failed ({response.status_code}): {response.text}"
            )

        data = response.json()
        devices.extend(data["results"])
        url = data["next"]
        params = {}  # only for first request

    return devices

# MAIN FUNCTION
def main():

    # ARGUMENT PARSER
    parser = argparse.ArgumentParser(description="Count NetBox devices by status")
    parser.add_argument("--url", required=True, help="NetBox base URL (e.g. http://localhost:8000)")
    parser.add_argument("--token", required=True, help="NetBox API token")
    parser.add_argument("--status", help="Device status to filter (optional)")

    args = parser.parse_args()

    # GET DEVICES
    try:
        devices = get_devices(args.url, args.token, args.status)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
    # COUNT AND PRINT RESULTS
    if args.status:
        print(f"Devices with status '{args.status}': {len(devices)}")
    else:
        counter = Counter(device["status"]["value"] for device in devices)
        print("Device count by status:")
        for status, count in counter.items():
            print(f"  {status}: {count}")

# ENTRY POINT
if __name__ == "__main__":
    main()
