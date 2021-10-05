	PROGRAM firstFortran
	IMPLICIT NONE
	  INTEGER :: code, digit1, digit2, answer

	  WRITE (*,*) "Hat size?"
	  READ (*,*) code
  	  CALL tensDigit(code)
	  CALL onesDigit(code)
!	turns the two digits from the  code into the locker number
	  answer = digit1*10 +digit2
	  WRITE (*,*) "Use ",answer
	CONTAINS

!	gets the second digit in the code, assigns it to digit1
	  SUBROUTINE tensDigit(num)
	    IMPLICIT NONE
	    INTEGER num
	    digit1 = MOD(num/10,10)
	  END SUBROUTINE tensDigit

!	gets the third digit in the code, assigns it to digit2
	  SUBROUTINE onesDigit(num)
	    IMPLICIT NONE
	    INTEGER num
	    digit2 = MOD(num/100,10)
	  END SUBROUTINE onesDigit
	END PROGRAM firstFortran
