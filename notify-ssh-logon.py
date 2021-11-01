import requests
import sys
import re
import subprocess

# Change this:
discord_role_id = "827339782199836682"

args = sys.argv[1:]

url = args[0]

split_ip = args[1].split(".")
ip = f"{split_ip[0]}.{split_ip[1]}.\*\*\*.\*\*\*"

hostname = subprocess.check_output(["hostname"]).decode().splitlines()[0]

country_data_url = f"https://ipapi.co/{args[1]}/json"
country_data = requests.get(country_data_url).json()

country = ""
country_code = ""

if "country_name" in country_data:
    country = country_data["country_name"]
else:
    country = f"Unknown"
    ip = args[1]

if "country_code" in country_data:
    code = country_data["country_code"]
    country_code = f"flag_{code.lower()}"
else:
    country_code = f"pirate_flag"

payload = {
    "content": f"<@&{discord_role_id}> :shield: New logon to \`{hostname}\` from :{country_code}: {country} ({ip})"
}

x = requests.post(url, json=payload)
