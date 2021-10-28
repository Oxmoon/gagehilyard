/* Program 4 
 * Logic Puzzle with Prolog
 */

/* The Puzzle:
 * Hunter, Laura, Addiley , Ramey, and Arnie all live in the same dorm
 * with five adjacent bedrooms. Hunter doesn’t sleep in the 5th
 * bedroom and Laura doesn’t sleep in the first bedroom.
 * Arnie doesn’t sleep in the first or last bedroom,
 * and he is not in an bedroomadjacent to Addiley or Laura.
 * Ramey sleeps in some bedroom higher than Laura’s.
 * Who sleeps in which bedrooms?
 */

adj(X,Y) :- Y =:= X-1 ; Y =:= X+1.

hallway([bedroom(_,1), bedroom(_,2), bedroom(_,3), bedroom(_,4), bedroom(_,5)]).

answer(X) :- hallway(X),
	member(bedroom(hunter,A),X), A \= 5,
	member(bedroom(laura,B),X), B \= 1,
	member(bedroom(addily,C),X),
	member(bedroom(ramey,D),X), D > B,
	member(bedroom(arnie,E),X), E \= 1 , E \= 5, \+ (adj(E,B)), \+ (adj(E,C)).
 
