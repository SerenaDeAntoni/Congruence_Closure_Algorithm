(set-info :smt-lib-version 2.6)
(set-logic QF_UF)
(set-info :category "crafted")
(set-info :status unsat)
(declare-sort S1 0)
(declare-fun f (S1) S1)
(declare-fun a () S1)
(declare-fun b () S1)
(declare-fun c0 () S1)
(declare-fun c1 () S1)
(declare-fun c2 () S1)
(declare-fun c3 () S1)
(declare-fun c4 () S1)
(assert (let ((t1 (f c0 )) (t2 (f c1 )) (t3 (f c3 )) (t4(f a))(t5(f b))(t6 (f t5))) (and (= a c0) (= t1 c2)(= t2 c3)(= b c1) (= t3 c4)(= c0 c1)(= c2 c4)(not (= t4 t6)))))
(check-sat)
(exit)