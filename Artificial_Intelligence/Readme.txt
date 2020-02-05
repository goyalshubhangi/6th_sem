Program 1: Write a prolog program to calculate the sum of two numbers.

Program 2: Write a Prolog program to implement max(X, Y, M) so that M is the maximum of two numbers X and Y.

Program 3: Write a program in PROLOG to implement factorial (N, F) where F represents the factorial of a number N.

Program 4: Write a program in PROLOG to implement generate_fib(N,T) where T represents the Nth term of the fibonacci series.

Program 5: Write a Prolog program to implement GCD of two numbers.

Program 6: Write a Prolog program to implement power (Num,Pow, Ans) : where Num is raised to the power Pow to get Ans.

Program 7: Prolog program to implement multi (N1, N2, R) : where N1 and N2 denotes the numbers to be multiplied and R represents the result.

Program 8: Write a program in PROLOG to implement towerofhanoi (N) where N represents the number of discs.

Program 9: Consider a cyclic directed graph [edge (p, q), edge (q, r), edge (q, r), edge (q, s), edge (s,t)] where edge (A,B) is a predicate indicating directed edge in a graph from a node A to a node B. Write a program to check whether there is a route from one node to another node.

Program 10: Write a Prolog program to implement memb(X, L): to check whether X is a member of L or not.

Program 11: Write a Prolog program to implement conc (L1, L2, L3) where L2 is the list to be appended with L1 to get the resulted list L3.

Program 12: Write a Prolog program to implement reverse (L, R) where List L is original and List R is reversed list.

Program 13: Write a program in PROLOG to implement palindrome (L) which checks whether a list L is a palindrome or not.

Program 14: Write a Prolog program to implement sumlist(L, S) so that S is the sum of a given list L.

Program 15: Write a Prolog program to implement two predicates evenlength(List) and oddlength(List) so that they are true if their argument is a list of even or odd length respectively.

Program 16: Write a Prolog program to implement nth_element (N, L, X) where N is the desired position, L is a list and X represents the Nth element of L.

Program 17: Write a program in PROLOG to implement remove_dup (L, R) where L denotes the list with some duplicates and the list R denotes the list with duplicates removed.

Program 18: Write a Prolog program to implement maxlist(L, M) so that M is the maximum number in the list.

Program 19: Write a prolog program to implement insert_nth(I, N, L, R) that inserts an item I into Nth position of list L to generate a list R.

Program 20: Write a Program in PROLOG to implement sublist(S, L) that checks whether the list S is the sublist of list L or not. (Check for sequence or the part in the same order).

Program 21: Write a Prolog program to implement delete_nth (N, L, R) that removes the element on Nth position from a list L to generate a list R.

Program 22: Write a program in PROLOG to implement delete_all (X, L, R) where X denotes the element whose all occurrences has to be deleted from list L to obtain list R.

Program 23: Write a program in PROLOG to implement merge (L1, L2, L3) where L1 is first ordered list and L2 is second ordered list and L3 represents the merged list.

Program 24: Write a PROLOG program that will take grammar rules in the following format:
          NT -> (NT | T)*
Where NT is any nonterminal, T is any terminal and Kleene star (*) signifies any number of repetitions, and generate the corresponding top-down parser, that is:
        sentence -> noun-phrase, verb-phrase
        determiner -> [the]
will generate the following:
        sentence (I, O) :- noun-phrase(I,R), verb-phrase (R,O).
        determiner ([the|X], X) :- !.