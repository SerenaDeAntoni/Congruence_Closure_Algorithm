# Planning and Automated Reasoning – AUTOMATED REASONING-
## II term, Academic Year 2022-23
### Project: Implementation of the congruence closure algorithm
#### Author: Serena De Antoni VR487515

**Congruence Closure Algorithm with DAG**  
In this project I implement the congruence closure algorithm with DAG for the satisfiability of a
set of equalities and inequalities in the quantifier-free fragment of the theory of equality. 
The algorithm was explained in class and is described in Sect. 9.3 of the Bradley-Manna textbook, and I considered the variant of the forbidden list - when calling MERGE s t if s is in the forbidden list of t or vice versa, return ‘unsat’ – and of the non-arbitrary choice of the representative of the new class in the UNION function - pick the one with the largest ccpar set.
I chose Python as programming language and to test my program I considered sets of equalities and inequalities from the Bradley-Manna textbook and some benchmarks with “.smt2” extension.

**Running Test**
- https://colab.research.google.com/drive/1qfILMDw-UJeaZsxnxLntX8vnRkk6gLc7?usp=sharing

1. Run 'Clone + Requirements' cell that contains
    ``` bash
        !git clone https://github.com/SerenaDeAntoni/Congruence_Closure_Algorithm.git
        !pip install pysmt
        !pip install networkx
    ```
3. Run 'Open the correct directiory' cell that contains :
   ``` bash
        %cd Congruence_Closure_Algorithm
   ```

7. Run the 'TEST' cell that contains :
    ``` bash
        !python main_txt.py
    ```
8. Run the 'TEST' cell that contains :
     ``` bash
        !python main_smt.py
     ```
   
