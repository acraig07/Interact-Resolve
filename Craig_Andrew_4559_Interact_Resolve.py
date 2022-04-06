# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:45:35 2021

@author: Andrew
"""

CLS = [['notP', 'notQ','R'], ['P', 'R'], ['Q', 'R'], ['notR']]

CHEM = [['notCO2', 'notH2O', 'H2CO3'], ['notC', 'notO2', 'CO2'],\
        ['notMgO', 'notH2', 'Mg'], ['notMgO', 'notH2', 'H2O'], 
        ['MgO'], ['H2'], ['O2'], ['C'], ['notH2CO3']]

GOV = [['T', 'notE', 'D'], ['notT', 'C'], ['E', 'notD', 'I'],\
       ['notG', 'notD', 'I'], ['T', 'C', 'notD', 'G'], ['notC'], 
       ['notI', 'notG'], ['D'], ['E']]

def try_resolvent(count, c1, c2):
    res = None
    for lit1 in c1:
        for lit2 in c2:
            if is_complement(lit1, lit2):
                print ("\n[%d.] Resolving %s and %s ..." % (count, c1, c2))
                print ("... found compl lits (%s, %s)" % (lit1, lit2))
                res = c1[:]
                res.remove(lit1)
                for x in c2:
                    if not x in res and x != lit2:
                        if complement(x) in res:
                            return True
                        else:
                            res.append(x)
                return res
    print("No resolvent")
    return res

def is_complement(x, y):
    if len(x) >= 4 and x[:3] == 'not':
        return x[3:] == y
    elif len(y) >= 4 and y[:3] == 'not':
        return x == y[3:]
    else:
        return False

def complement(x):
    if len(x) >= 4 and x[:3] == 'not':
        return x[3:]
    else:
        return 'not' + x

def same_clause(c1, c2):
    if not len(c1) == len(c2):
        return False
    for x in c1:
        if not x in c2:
            return False
    return True

def interact_resolve(clause):
    count = 1
    
    while count < 10000:
        before = len(clause)
        
        for i in range(len(clause)):
            print ("[%s]" % (i + 1), clause[i])
        
        print('\nPick two clauses by their number ...', end='')
        first = int(input('First clause: '))
        second = int(input('Second clause: '))
        
        c3 = try_resolvent(count, clause[first-1], clause[second-1])       
        
        if c3 == []:
            print ("... new clause %s" %c3)
            print ("\nUNSATISFIABLE :-)")
            return 'UNSAT'
                
        if c3 != True:
            if not same_clause(clause, c3):
                clause.append(c3)
                count += 1
                print ("... new clause %s" %c3, "\n")
            else:
                print ("... clause NOT NEW")
                        
        if len(clause) == before:
            print ("\nNo Contradiction: Satisfiable :-(")
            return 'SAT'
        
    print ("\nExdeeding limit -- No answer :-|")
    for i in range(len(clause)):
        print ("[%s]" % (i + 1), clause[i])
    
if __name__ == '__main__':
    #interact_resolve(CHEM)
    #interact_resolve(CLS)
    interact_resolve(GOV)