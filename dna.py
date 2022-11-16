def read_dna(dna_filename):
    a=open(dna_filename)
    b=a.read()
    return b

def dna_length(dna_filename):
    a=len(read_dna(dna_filename))
    return a

def get_strs(str_profile):
    b=['0','1','2','3','4','5','6','7','8','9']
    c=[]
    for key in str_profile:
        c.append(key)
        if str_profile[key] in b:
            c.append(int(str_profile[key]))
        else:
            c.append(str_profile[key])
    d=[c[2],c[3]]
    e=[c[4],c[5]]
    f=[c[6],c[7]]
    g=[tuple(d),tuple(e),tuple(f)]
    return g

def read_strs(str_filename):
    a=open(str_filename)
    b=a.read()
    c=b.split()
    d=c[0].split(',')
    e=c[1].split(',')
    f=c[2].split(',')
    g=c[3].split(',')
    dict_a={}
    dict_b={}
    dict_c={}
    for i in range(len(d)):
        dict_a[d[i]]=e[i]
        dict_b[d[i]]=f[i]
        dict_c[d[i]]=g[i]
    h=[dict_a,dict_b,dict_c]
    return h

def longest_str_repeat_count(str_frag, dna_seq):
    list_count=[]
    count = 0
    i=0
    while i<len(dna_seq):
        if i==len(dna_seq)-4:
            break
        if dna_seq[i:i+4]==str_frag:
            count+=1
            i+=4
        else:
            list_count.append(count)
            count=0
            i+=1
    for a in range(len(list_count)):
        if list_count[a]==list_count[a+1] and list_count[a]!=0:
            count=list_count[a]
            break
    
    mx = 0
    for a in list_count:
        if mx<a:
            mx = a
    return mx

def find_match(str_profile, dna_seq):
    a=str_profile[0]
    b=str_profile[1]
    c=str_profile[2]
    d=longest_str_repeat_count(a[0],dna_seq)
    e=longest_str_repeat_count(b[0],dna_seq)
    f=longest_str_repeat_count(c[0],dna_seq)
    if d==a[1] and e==b[1] and f==c[1]:
        return True
    else:
        return False


def dna_match(str_filename, dna_filename):
    dna=read_dna(dna_filename)
    stats=read_strs(str_filename)
    alice=get_strs(stats[0])
    bob=get_strs(stats[1])
    charlie=get_strs(stats[2])
    ans=''
    if find_match(alice, dna):
        ans="Alice"
    elif find_match(bob,dna):
        ans="Bob"
    elif find_match(charlie,dna):
        ans="Charlie"
    else:
        ans="No match"
    return ans

if __name__ == '__main__':
    arg=[]
    count=0
    while count!=-1:
        if count>2:
            break
        else:
            arg.append(input())
            count+=1

    if len(arg)==2:
        print(dna_match(arg[0],arg[1]))
    else:
        print('Usage: python dna.py STR_FILE DNA_FILE')
