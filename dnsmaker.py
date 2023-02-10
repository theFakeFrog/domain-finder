import random
import socket
import string

def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None

def generate_domain(length=1):
    domain = "".join(random.choices(string.ascii_lowercase, k=length))
    domain += random.choice([".com", ".org", ".net", ".int", ".edu", ".gov", ".mil", ".arpa", ".aero", ".asia", ".biz", ".cat", ".coop", ".info", ".jobs", ".mobi", ".museum", ".name", ".pro", ".tel", ".travel", ".cn", ".tk", ".de", ".uk", ".ru", ".eu", ".au", ".br", ".in", ".us"])

    return domain

generated_domains = set()
while len(generated_domains) < 100:
    domain = generate_domain(length=random.randint(1, 63))
    if domain not in generated_domains:
        generated_domains.add(domain)
        ip = get_ip(domain)
        if ip:
            print(f"{ip} {domain}")

