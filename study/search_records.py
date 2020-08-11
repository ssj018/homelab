import re
import sys
# 2014

# %book%
# %title%abc%title%
# %publish%2011%publish%
# %author%qwer%author%
# %book%

# %book%
# %title%def%title%
# %publish%2012%publish%
# %author%asdf%author%
# %book%

# %book%
# %title%ghi%title%
# %publish%2014%publish%
# %author%zxcv%author%
# %book%

# %book%
# %title%back to 2014%title%
# %publish%1999%publish%
# %author%poiu%author%
# %book%



class book:
    def __init__(self, title, publish, author):
        self.title = title
        self.publish = publish
        self.author = author
    
    def search(self, key):
        found = False
        if self.title == None:
            pass
        else:
            if re.search(r'{}'.format(key), self.title):
                found = True
                return found

        if self.publish == None:
            pass 
        else:        
            if re.search(r'{}'.format(key), self.publish):
                found = True
                return found

        if self.author == None:
            pass
        else:
            if re.search(r'{}'.format(key), self.author):
                found = True
                return found
        
        return found


def main():
    print('type your input, stop with \'...\'')
    key = input()
    book_tags = 0
    title = publish = author = None
    booklist = []
    while True:
        line = input()
        if line == '...':
            if book_tags % 2 != 0:
                print('book_tags are not double')
                sys.exit(1)
            break
        elif re.match(r'^\s*$',line):
            continue
        elif re.match(r'%book%$', line) and book_tags % 2 == 0:
            book_tags += 1
        elif re.match(r'%book%$', line) and book_tags % 2 != 0:
            tbook = book(title, publish, author)
            booklist.append(tbook)
            book_tags +=1   
        elif re.search(r'%title%', line) and book_tags % 2 != 0:
            title = re.findall(r'''%title%(.*)%title%''', line)[0]
        elif re.search(r'publish', line) and book_tags % 2 != 0:
            publish = re.findall(r'''%publish%(.*)%publish%''', line)[0]
        elif re.search(r'author', line) and book_tags % 2 != 0:
            author = re.findall(r'''%author%(.*)%author%''', line)[0]
        else:
            print('wrong Input')
            sys.exit(1)

    for i  in booklist:
        if i.search(key):
            print('title: {}, publish: {} , author: {}'.format(i.title, i.publish, i.author))

if __name__ == "__main__":
     main()
    # line = input()
    # book_tag = 0
    #  if re.search(r'%book%', line) and book_tag % 2 == 0:
    #      print('book')




        

        
