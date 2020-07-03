import random

# def random_mac_section():
#     hex_mac_list = [1,2,3,4,5,6,7,8,9,'a','b','c','e','f']
#     return '{}{}'.format(random.choice(hex_mac_list),random.choice(hex_mac_list))

def random_mac():
    hex_mac_list = [1,2,3,4,5,6,7,8,9,'a','b','c','e','f']
    x = lambda:'{}{}'.format(random.choice(hex_mac_list),random.choice(hex_mac_list))
    mac_sections=[ x() for i in range(6)]
    return ":".join(mac_sections)


if __name__ == "__main__":
    mac = random_mac()
    print(mac)