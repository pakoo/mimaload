import pprint
mimi=open('tianya_1.txt','r')
data=mimi.readlines()
print 'data len:',len(data)
for p in data[151000:152000]:
    p=p[:-2]
    p=p.split(' ')
    p=[a for a in p if a]
    if len(p)==2:
        name=p[0]
        pwd=p[1]
        print name,pwd
    elif len(p)==3:
        name=p[0]
        pwd=p[1]
        email=p[2] 
        print name,pwd,email
    else:
        print name,pwd
    	print p
    #print p.decode('gbk')
    #print p.decode('utf-8').encode('gbk'),type(p)
