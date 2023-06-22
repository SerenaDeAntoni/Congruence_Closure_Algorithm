import networkx as nx
from pyparsing import nestedExpr
from CCA_DAG import Node, Congruent_Closure_Algorithm_with_DAG
import itertools

class Parser:

    def __init__(self, graph):
        self.customParser = nestedExpr('(', ')')
        self.graph = graph
        self.ids = set()
        self.atoms_dict = dict()
    
    def parse(self, input):
        input = input.replace(' ', '')
        clauses = set(input.split('&'))
        variables = set()
        repeated = set()

        for c in clauses:
            c = c.replace('!', '')
            if c[0] == '(':
                c = c[1:-1]
            part1,part2 = c.split('=')
            variables.add(part1)
            variables.add(part2)

        for el1 in variables:
            for el2 in variables:
                if el1 != el2 and el1 in el2 and el2[el2.find(el1) + len(el1)] in ['=', '(', ')']:
                    repeated.add(el1)
                    break
                
        final = [var for var in variables if var not in repeated]
        final2 = ['0' if any(var1 in var2 for var2 in final if var1 != var2) else var1 for var1 in final]
        final2 = [var for var in final2 if var != '0']

        for atom in final2:
            atom_as_list = self.customParser.parseString('(' + atom + ')').asList()
            self.parse_clause(atom_as_list[0])
    
    def parse_clause(self, atom_as_list: list):
        clause = []
        children = []
        for term in atom_as_list:
            if isinstance(term, list):  clause.append(term)
            else:   clause.extend([t for t in term.split(',') if t != ''])

        atoms_dict = self.atoms_dict
        graph_add_node = self.graph.add_node
        node_string = self.graph.node_string

        for i, literal in enumerate(clause):
            if isinstance(literal, list):   continue
            id = self.newId()
            id_list = [arg.id for arg in self.parse_clause(clause[i + 1])] if i + 1 < len(clause) and isinstance(clause[i + 1], list) else []
            new_node = Node(id=id, fn=literal, args=id_list, find=id, ccpar=set())
            children.append(new_node)
            graph_add_node(new_node)
            atoms_dict[node_string(new_node.id).replace(' ', '')] = id

        return children

    def newId(self) -> str:
        id = next(i for i in itertools.count(1) if i not in self.ids)
        self.ids.add(id)
        return id

def split_or(input_string):
    split_list = input_string.split("or")
    split_list = [elem.strip() for elem in split_list]
    return split_list

def eq_ineq(equations, atoms_dict):
    eq = []
    ineq = []
    fl = set()

    equations = equations.split('&')

    for e in equations:
        if e[0] == '(':    e = e[1:-1]

        if '!=' in e:
            parts = e.split('!=')
            atom1 = parts[0].strip()
            atom2 = parts[1].strip()
            new_ineq = [atoms_dict[atom1], atoms_dict[atom2]]
            ineq.append(new_ineq)
            fl.add((atoms_dict[atom1], atoms_dict[atom2]))
        else:
            parts = e.split('=')
            atom1 = parts[0].strip()
            atom2 = parts[1].strip()
            new_eq = [atoms_dict[atom1], atoms_dict[atom2]]
            eq.append(new_eq)
    
    return eq, ineq, fl

def OR(clause, list_sat):
    s = Congruent_Closure_Algorithm_with_DAG()
    parser = Parser(s)
    clause = clause.replace(' ','')
    clause = clause.replace('\n','')
    parser.parse(clause.strip())
    eq, ineq, fl = eq_ineq(clause.strip(), parser.atoms_dict)
    s.add_forbidden_list(fl)
    s.add_eq(eq)
    s.add_ineq(ineq)
    s.complete_ccpar()
    s.visualize_dag()
    res, count = s.solve()
    print(f"The formula is: {res}")
    list_sat.append(res)
    return count

def AND(line):
    s = Congruent_Closure_Algorithm_with_DAG()
    parser = Parser(s)
    line = line.replace(' ','')
    line = line.replace('\n','')
    parser.parse(line.strip())
    eq, ineq, fl = eq_ineq(line.strip(), parser.atoms_dict)
    s.add_forbidden_list(fl)
    s.add_eq(eq)
    s.add_ineq(ineq)
    s.complete_ccpar()
    s.visualize_dag()
    res, count = s.solve()
    print(f"The formula is: {res}")
    return count

def SMT(filename, parser):
    s_smt = Congruent_Closure_Algorithm_with_DAG()
    parser_smt = parser
    my_parser = Parser(s_smt)
    f = parser_smt.parse(filename)
    string = f
    if "or" in f:
        linesOR = split_or(f)
        list_sat = []
        tot_merge = 0
        for line in linesOR:
            my_parser.parse(line)
            eq, ineq, fl = eq_ineq(line, my_parser.atoms_dict)
            s_smt.add_eq(eq)
            s_smt.add_ineq(ineq)
            s_smt.add_forbidden_list(fl)
            s_smt.complete_ccpar()
            s_smt.visualize_dag()
            res = s_smt.solve()
            tot_merge += res[1]
            if res[0] == "SAT": return "SAT", string, list_sat, tot_merge
            else: list_sat.append(res[0])
        res_f = "UNSAT"
    else:
        my_parser.parse(f)
        eq, ineq, fl = eq_ineq(f, my_parser.atoms_dict)
        s_smt.add_eq(eq)
        s_smt.add_ineq(ineq)
        s_smt.add_forbidden_list(fl)
        s_smt.complete_ccpar()
        res = s_smt.solve()
        tot_merge = res[1]
        list_sat = [res[0]]
        res_f = res[0]
    return res_f, string, list_sat, tot_merge






