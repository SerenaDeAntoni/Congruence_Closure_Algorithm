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

    filename = "input/input1.smt2"
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
    
    script = SmtLibParser().get_script_fname(filename)
    f = script.get_strict_formula().serialize().__str__()[1:-1]
    f = f.replace(' ', '')

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