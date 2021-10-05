;;;; Assignment 2
;;;; Gage Hilyard

(setq *print-case* :downcase)
;; To match the output in the assignment

;; The recursive palindrome function
;; Prints the result to terminal
(defun palindromep (rlist)
	(cond	
		;;base case, when there is one element remaining, or the list is empty
		((atom rlist) (format t "t~%"))
		((null rlist) (format t "t~%"))

		;;tests first and last elements in list, and executes recursion
		;;in the format (test action) where test is the equal function, and action is the recursion
		(
			(equal (first rlist) (first (reverse rlist)))
			(palindromep (rest (reverse (rest rlist))))
		)
		
		;;failure
		(t (format t "nil~%"))
	)
)

(palindromep '(a b b a))
(palindromep '(a b c b a))
(palindromep '(a b c))
(palindromep '(a (d e) b (d e) a))
(palindromep '(a (d e) b (e d) a))
