import requests
import json
import subprocess
import re

def fetch_subdomains(domain):
    print(f"[+] Fetching subdomains from crt.sh for: {domain}")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        subdomains = set()
        if response.status_code == 200:
            data = json.loads(response.text)
            for entry in data:
                name = entry['name_value']
                for sub in name.split('\n'):
                    if "*" not in sub:
                        subdomains.add(sub.strip())
        return list(subdomains)
    except Exception as e:
        print(f"[!] Error fetching from crt.sh: {e}")
        return []

def check_live(subdomain):
    try:
        response = requests.get(f"http://{subdomain}", timeout=3)
        return response.status_code
    except:
        return None

def categorize(subdomain):
    if "admin" in subdomain:
        return "Admin Panel"
    elif "api" in subdomain:
        return "API Endpoint"
    elif "shop" in subdomain or "store" in subdomain:
        return "E-Commerce"
    elif "blog" in subdomain:
        return "Blog"
    else:
        return "General"

def save_results(domain, results):
    filename = f"{domain.replace('.', '_')}_subdomains.txt"
    with open(filename, 'w') as f:
        f.write(f"{'Subdomain':<35} {'Status':<10} {'Category'}\n")
        f.write("-" * 60 + "\n")
        for sub, status, cat in results:
            f.write(f"{sub:<35} {str(status):<10} {cat}\n")
    print(f"[+] Results saved in: {filename}")

def run_subfinder(domain):
    print(f"[+] Running subfinder for: {domain}")
    try:
        result = subprocess.run(["subfinder", "-d", domain, "-silent"], capture_output=True, text=True)
        subs = result.stdout.strip().split("\n")
        return list(filter(lambda x: x.strip() != "", subs))
    except Exception as e:
        print(f"[!] subfinder error: {e}")
        return []

if __name__ == "__main__":
    domain = input("Enter domain (e.g., example.com): ").strip()
    crt_subs = fetch_subdomains(domain)
    subfinder_subs = run_subfinder(domain)

    all_subs = list(set(crt_subs + subfinder_subs))
    print(f"[+] Total unique subdomains found: {len(all_subs)}")

    results = []
    for sub in all_subs:
        status = check_live(sub)
        cat = categorize(sub)
        results.append((sub, status, cat))

    save_results(domain, results)
