#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Line Coding Encoder and Scrambler
@author: JameeBashir
"""


import numpy as np
import matplotlib.pyplot as plt

print("\t\t\tLine Coding Encoder and Scrambler\n")
print("Enter the bit stream to be encoded:\n")
s=input()

print("\n Choose the line coding scheme to be implemented: \n 1.NRZ-L\n 2.NRZ-I\n 3.Manchester\n 4.Differential Manchester\n 5.AMI\n")
n=int(input())
if(n==1):
    
    ls=list()
    for i in range(len(s)):
        if(s[i]=='0' or s[i]==0):
            ls.append(-1)
        else:
            ls.append(1)
    xs = np.repeat(range(len(s)), 2)
    ys = np.repeat(ls, 2)
    xs=xs[1:] 
    xs=np.append(xs,(xs[len(xs)-1]+1))
    ys=ys[:-1]
    ys=np.append(ys,(ys[len(ys)-1]))
    plt.step(xs,ys)
    plt.ylim(-2,2)
    plt.ylabel("Polar NRZ-L")
    plt.plot(xs,ys,color='blue',marker='>')
    
    
elif(n==2):
    
    Is=list()
    if(s[0]=='0' or s[0]==0):
        Is.append(-1)
    else:
        Is.append(1)
    k=len(s)
    i=1
    while(i<k):
        if(int(s[i])==0):
            Is.append(Is[i-1])
        else:
            Is.append(-Is[i-1])
        i=i+1
    xs = np.repeat(range(len(s)), 2)
    ys = np.repeat(Is, 2)
    xs=xs[1:]
    xs=np.append(xs,(xs[len(xs)-1]+1))
    ys=ys[:-1]
    ys=np.append(ys,(ys[len(ys)-1]))
    plt.step(xs,ys)
    plt.ylim(-2,2)
    plt.ylabel("Polar NRZ-I")
    plt.plot(xs,ys,color='blue',marker='>')
   
    
elif(n==3):
    
    pm=list()
    for j in range(len(s)):
        if(s[j]=='0' or s[j]==0):
            pm.append(1)
            pm.append(-1)
        else:
            pm.append(-1)
            pm.append(1)
    xs=[x*0.5 for x in range(0,(2*len(s)))]
    xs=np.repeat(xs,2)
    ys = np.repeat(pm, 2)
    xs=xs[1:]
    xs=np.append(xs,(xs[len(xs)-1]+0.5))
    ys=ys[:-1]
    ys=np.append(ys,(ys[len(ys)-1]))
    plt.step(xs,ys)
    plt.ylabel("Manchester")
    plt.ylim(-2,2)
    plt.plot(xs,ys,color='blue',marker='>')
    
elif(n==4):
   
    pdm=list()
    pdm.append(-1)
    pdm.append(1)
    i=1
    k=len(s)
    while(i<k):
        if(int(s[i])==1):
            pdm.append(pdm[len(pdm)-1])
            pdm.append(-pdm[len(pdm)-1])
        else:
            pdm.append(-pdm[len(pdm)-1])
            pdm.append(-pdm[len(pdm)-1])
        i=i+1
    print(pdm)
    xs=[x*0.5 for x in range(0,(2*len(s)))]
    xs=np.repeat(xs,2)
    ys = np.repeat(pdm, 2)
    xs=xs[1:]
    xs=np.append(xs,(xs[len(xs)-1]+0.5))
    ys=ys[:-1]
    ys=np.append(ys,(ys[len(ys)-1]))
    plt.step(xs,ys)
    plt.ylim(-2,2)
    plt.ylabel("Differantial Manchester")
    plt.plot(xs,ys,color='blue',marker='>')
else:
    print("Is Scrambling required? [y|n]")
    a=input().lower()
    if a=='n':
       
        am=list()
        m=1
        for i in range(len(s)):
            if(int(s[i])==0):
                am.append(0)
            else:
                if(m%2==1):
                    am.append(1)
                else:
                    am.append(-1)
                m=m+1
        xs = np.repeat(range(len(s)), 2)
        ys = np.repeat(am, 2)
        xs=xs[1:]
        xs=np.append(xs,(xs[len(xs)-1]+1))
        ys=ys[:-1]
        ys=np.append(ys,(ys[len(ys)-1]))
        plt.step(xs,ys)
        plt.ylim(-2,2)
        plt.ylabel("AMI")
        plt.plot(xs,ys,color='blue',marker='>')
        
    else:
        print("Choose type of scrambling: \n 1.B8ZS\n 2.HDB3")
        p=int(input())
        q=len(s)
        if(p==1):
           
            bz=list()
            m=1
            s1=s.replace("00000000","000vb0vb")
            for i in range(len(s1)):
                if(s1[i]=='0' or s1[i]==0):
                    bz.append(0)
                elif(s1[i]=='1'):
                    if(m%2==1):
                        bz.append(1)
                    else:
                        bz.append(-1)
                    m=m+1
                elif(s1[i]=='v'):
                    if(m%2==1):
                        bz.append(-1)
                    else:
                        bz.append(1)
                else:
                    if(m%2==1):
                        bz.append(1)
                    else:
                        bz.append(-1)
                    m=m+1
            xs = np.repeat(range(len(s)), 2)
            ys = np.repeat(bz, 2)
            xs=xs[1:]
            xs=np.append(xs,(xs[len(xs)-1]+1))
            ys=ys[:-1]
            ys=np.append(ys,(ys[len(ys)-1]))
            plt.step(xs,ys)
            plt.ylim(-2,2)
            
            plt.ylabel("B8ZS")
            plt.plot(xs,ys,color='blue',marker='>')
           
        else:
            
            m=0
            hd=list()
			  
            f=s.find("0000")
            if(f==-1):
                f=len(s)
            i=0
            k=len(s)
            d=-1
            p=0
            while(i<k):
                if(s[i]=='1' or s[i]==1):
                    m=m+1
                    p=p+1
                    if(m%2==1):
                        hd.append(-d)
                        d=-d
                    else:
                        hd.append(-d)
                        d=-d
                else:
                    if(i<f):
                        hd.append(0)
                    elif(i==f):
                        i=i+3
                        if(p==0):
                            hd.append(d)
                            hd.append(0)
                            hd.append(0)
                            hd.append(d)
                            
                            p=p+2
                            m=m+1
                        elif(p%2==0):
                            hd.append(-d)
                            hd.append(0)
                            hd.append(0)
                            hd.append(-d)
                            d=-d
                            p=p+2
                            m=m+1
                        else:
                            hd.append(0)
                            hd.append(0)
                            hd.append(0)
                            hd.append(d)
                            p=p+1
                        jk=s[i+1:(i+1)+(k-i-1)]
                        x=jk.find("0000")
                        if(x==-1):
                            f=k
                        else:
                            f=i+1+x
                i=i+1
            xs = np.repeat(range(len(s)), 2)
            ys = np.repeat(hd, 2)
            xs=xs[1:]
            xs=np.append(xs,(xs[len(xs)-1]+1))
            ys=ys[:-1]
            ys=np.append(ys,(ys[len(ys)-1]))
            plt.step(xs,ys)
            plt.ylim(-2,2)
            plt.ylabel("HDB3")
            plt.plot(xs,ys,color='blue',marker='>')
