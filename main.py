import os
import networkx as nx
from CCA_DAG import *
from txt_parser import *
from smt_parser import *
from timeit import default_timer as timer

def main():

    print( "\n*****************************************************************************************" )
    print( "*  Congruence closure algorithm with DAG for the satisfiability of a set of equalities  *" )
    print( "*     and disequalities in the quantifier-free fragment of the theory of equality.      *" ) 
    print( "*****************************************************************************************" )
    
    #f(a, b) = a & f(f(a, b), b) != a or f(f(f(a))) = a & f(f(f(f(f(a))))) = a & f(a) != a or f(f(f(a))) = a
    # f(a)=f(b) & a!=b SAT
    # a=b & f(a)!=f(b) UNSAT
    # f(f(f(a))) = a & f(f(f(f(f(a))))) = a & f(a) != a UNSAT
    # f(f(f(a))) = f(a) & f(f(a)) = a & f(a) != a SAT
    # f(a, b) = a & f(f(a, b), b) != a UNSAT
    #a=b & b!=a unsat -> forbidden list


    file_test = open('input/input.txt', 'r')
    filename = file_test.readlines()
    flag=True

    #filename = "input/or.smt2"
    #filename = "input/input1.smt2"
    #filename = "input/input2.smt2"
    #filename = "input/input4.smt2"
    #filename = "input/input6.smt2"
    #filename = "input/input7.smt2"
    #filename = "input/input8.smt2"
    #filename = "input/input10.smt2"
    #filename = "input/input11.smt2"
    #filename = "input/input12.smt2"
    #filename = "input/input13.smt2"
    #filename = "input/input14.smt2"
    
    # script = SmtLibParser().get_script_fname(filename)
    # f = script.get_strict_formula().serialize().__str__()[1:-1]
    # f = f.replace(' ', '')
    # flag = False

    if flag:
        for line in filename:
            if "or" in line:
                merge = 0
                print(f"Checking formula: {line.strip()}")
                start = timer()
                linesOR = split_or(line)
                l_sat = []
                sat_unsat = "0"
                for clause in linesOR:
                    merge += OR(clause, l_sat)
                    for i in range(len(l_sat)):
                        if l_sat[i] == "SAT":   sat_unsat = "SAT"
                    if sat_unsat == "0":    sat_unsat = "UNSAT"
                end = timer()
                print(f"The formula is: {sat_unsat}")
                print(f'time = {end-start}')
                print(f'number of merge = {merge}')
                print('-'*100)
            
            else:
                print(f"Checking formula: {line.strip()}")
                merge = 0
                start = timer()
                merge = AND(line)
                end = timer()
                print(f'time = {end-start}')
                print(f'number of merge = {merge}')

                print('-'*100)

    
    else:
        start = timer()
        parser_smt = Txt_parser()
        res, input, list_sat, merge  = SMT(filename, parser_smt)
        end = timer()
        
        print(f"Checking formula: {input}")
        print(f'time = {end-start}')
        print(f'number of merge = {merge}')
        print(f"The formula is: {res}")
        print('-'*100)

if __name__ == '__main__':
    main()