import sys
def read_dna(dna_filename):
    a=open(dna_filename)
    b=a.read()
    return b

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
    a=True
    count=0
    while a:
        for i in range(len(dna_seq)):
            if dna_seq[i:i+4]==str_frag:
                count+=1
        a=False
    return count

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
    if (len(sys.argv[1]) == 0 or len(sys.argv[2]==0)):
        print('Usage: python dna.py STR_FILE DNA_FILE')
    else:
        print(dna_match(sys.argv[1],sys.argv[2]))

