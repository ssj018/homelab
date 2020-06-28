import random

def random_ip_section():
    section = random.randint(1, 254)
    return section

def random_ip():
    sections = [ random_ip_section() for i in range(4)]
    return '.'.join('%s'%section for  section  in sections)
    


if __name__ == "__main__":
    ip = random_ip()
    print(ip)