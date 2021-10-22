from re import T
from typing import Mapping
import wikipedia
from googlesearch import search

def a(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret

def addToMemory(head,info):
    info = a(info)
    rmemory = open("code\memory.txt",'r')
    content = rmemory.read()
    wmemory = open('code\memory.txt','w')
    wmemory.write(content+head+' : '+info+'\n')
    wmemory.close()
    rmemory.close()

def ishead(head,getheadinfo):
    rmemory = open("code\memory.txt",'r')
    head = head.split(' ')
    num_lines = sum(1 for line in open('code\memory.txt'))
    mlist = ''.join(rmemory.readlines()).split('\n')
    i =j=0
    result = False
    foundline = False
    while ((foundline==True and i<len(mlist))or (foundline == False and i<num_lines)) and j<len(head):
        if head[j] in mlist[i].split(' '):
            limit = mlist[i].index(':')
            inMlist = mlist[i].index(head[j])
            if inMlist < limit:
                if foundline == False:
                    t = i
                result = True
                foundline = True
                temp = mlist[i]
                mlist.clear()
                mlist.append(temp)
                j += 1
                i = -1
                if getheadinfo and j == len(head):
                    g = t
                    break
        elif foundline==True:
            result = False
            break

        i += 1 
    rmemory.close()
    if getheadinfo:
        return result,g
    return result
    

def getinfoFromMemory(data):
    rmemory = open("code\memory.txt",'r')
    mlist = ''.join(rmemory.readlines()).split('\n')
    if ishead(data,False):
        headlist = ishead(data,True)
        headline = mlist[headlist[1]].split(' ')
        j = 0
        while headline[j] != ':':
            headline.pop(j)
            j = 0
        headline.pop(0)
        return (' '.join(headline))
    try:    
        print(wikipedia.summary(data,sentences = 1))
        addToMemory(data,wikipedia.summary(data,sentences = 1,auto_suggest=True))
    except:
        print('data not found')

while True:
    order = input('What to do?')
    print(order)
    if 'add info' in order:
        head = input('TOPIC?')
        info = input('Discription')
        addToMemory(head,info)
        print('Feeded')
    elif 'get info' in order:
        head = input('About What?')
        print(getinfoFromMemory(head))
