#!/usr/bin/python3

def is_charshif_1(s1 :list, s2 :list):
    stillok=True
    if len(s1) != len(s2):
        stillok = False
        return stillok

    for  i  in s1:
        s2pos = 0
        found = False
        while s2pos < len(s2) and found == False:
            if i == s2[s2pos]:
                found = True
                s2.pop(s2pos)
            else:
                s2pos += 1

        if found == False:
            stillok = False
            break

    return stillok


def is_charshif_2(s1 :list, s2 :list):
    s1.sort()
    s2.sort()
    matches = True

    if len(s1) != len(s2):
        matches = False
        return matches
    
    pos = 0
    while pos < len(s1) and  matches == True:
        if s1[pos] != s2[pos]:
            matches = False
            break
        else:
            pos += 1
    
    return matches

def is_charshif_3(s1 :list, s2 :list):
    if len(s1) != len(s2):
        return False

    s1_counter = {}
    s2_counter = {}
    char_list = ['a', 'b', 'c', 'd', 
    'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'h', 'l', 'm',
    'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w',
    'x', 'y', 'z' 
    ]

    for  i in char_list:
        s1_counter[i] = 0
        s2_counter[i] = 0
    
    for  i in s1:
        s1_counter[i] += 1

    for  i  in  s2:
        s2_counter[i] += 1
    
    for  key  in s1_counter:
        if s1_counter[key] != s2_counter[key]:
            return False
        else:
            return True


    

if __name__ == "__main__":
    s1='earth'
    s2='heart'
    print(is_charshif_1(list(s1), list(s2)))
    print(is_charshif_2(list(s1), list(s2)))
    print(is_charshif_3(list(s1), list(s2)))
                
