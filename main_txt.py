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
    
    file_test = open('input/input.txt', 'r')
    filename = file_test.readlines()
    flag=True

    
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

if __name__ == '__main__':
    main()