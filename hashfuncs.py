import requests
import hashlib
import sys
from bs4 import BeautifulSoup

def hash_string(hash_type, s):
    hashes = {'md5':hashlib.md5, 'sha1':hashlib.sha1, 'sha256':hashlib.sha256}
    if hash_type.lower() in hashes:
        return hashes[hash_type](s.encode()).hexdigest()
def populate(ls, hash_type, opt):
    hashes = {'md5':hashlib.md5, 'sha1':hashlib.sha1, 'sha256':hashlib.sha256}
    d = {}
    if hash_type.lower() in hashes:
        for word in ls:
            for option in opt:
                word = word+str(option)
                hsh = hashes[hash_type](word.encode())
                d.update({hsh.hexdigest():word})
    else:
        raise SystemExit(f"Unsupported hash type,\nSupported hash types are: [i for i in d.keys()]\nYou entered {hash_type}\n Exiting....")

    return d
def scrape_and_populate(url, hash_type, opt):
    """
    we need to increase the capabillity of this function or its' supporting functions
    to crawl through a website and get all words of interesing using scrapy probably
    TODO
    """

    with open("commonwords.txt", 'r') as f:
        common = [i.strip("\n") for i in f.readlines()]

    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    ls = [i for i in soup.body.text.split(" ") if i.isalpha() and i not in common]

    return populate(ls,hash_type, opt)
def populate_table_from_file(path,hash_type, opt):
    ls = open(path,'r').readlines() 
    return populate(ls,hash_type, opt)

def populate_table_from_link(link, hash_type, opt):
    ls = requests.get(link).text.split("\n")[:-1]
    return populate(ls,hash_type, opt)
