# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:23:19 2020

@author: joaom
"""

#Big_Dixxxxxxx

class big_dix:
     
    def __init__(self,**kwargs):
        dix={}
        for k,w in kwargs.items():
            dix[str(k)]=w
        self.size=len(dix)
        self.dix=dix
        
    def add_keys(self,**kwargs):
        for k,w in kwargs.items():
            self.dix[k]=w
            
    def add_keys_2(self,w1,w2):
        #w1 é uma lista com as keys e w2 uma lista com os valores correspondentes
        assert len(w1)==len(w2)
        for i in range(len(w1)):
            self.dix[w1[i]]=w2[i]
            
    def remove_keys(self,*args):
        for a in args:
            try:
                del self.dix[a]
            except:
                pass
            
    def keys(self):
        return list(self.dix.keys())
            
def go_get(dixx,count=0,mode=1,lista=None):
    if mode==1:
        if count==0:
            print(type(dixx))
        print(dixx.keys())
        new=input("Choose One of The Above: ")
        if new not in dixx.keys():
            print('ERRO na palavra!!!')
            return go_get(dixx,count,mode=1)
        dixx=dixx.dix[new]
        if type(dixx)==big_dix:
            count+=1
            return go_get(dixx,count,mode=1)
        else:
            return dixx
    else:
        while lista!=[]:
            dixx=dixx.dix[lista[0]]
            lista=lista[1:]
        return dixx


def get_return_money(repos,top=5):
    moneyz=100
    DF = go_get(repos,mode=2,lista=['OverAll'])
    method = list(DF['Method'])
    profit=[]
    for i in range(len(method)):
        tree,foret = method[i].split('_')
        listaz = ['Tree_Forest',tree,foret,'Predicted']
        df = go_get(repos,mode=2,lista=listaz)
        cash = round((100*(money(df,moneyz)/moneyz))-100,2)
        profit+=[[tree+'_'+foret,cash]]
    topz=[]
    for t in range(top):
        only_cash = np.array([profit[i][1] for i in range(len(profit))])
        ind_max=np.argmax(only_cash)
        topz+=[[profit[ind_max][0],profit[ind_max][1]]]
        del profit[ind_max]
    return topz
        