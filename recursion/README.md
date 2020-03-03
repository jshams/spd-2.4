# [Recursion Problems](README.md)

## [Problem 1:](fizz_buzz.py) **Fizz Buzz**
You’re asked to write recursive FizzBuzz. Your function takes 2 integers: start and end, which are the first and last number in the sequence of integers to return in a list (array). However, if the number is a multiple of 3, put “Fizz” in the list instead of the number. If it’s a multiple of 5 put “Buzz” in the list. If it’s a multiple of 3 and 5, put “FizzBuzz” in the list.  
Example: `fizzbuzz(1, 20)`  
returns `[1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz]`

---

## [Problem 2:](t9_letters.py) **T9 Letters**
Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, return a list of all letter combinations they could have been trying to type on the keypad.  
Example execution 1:  `t9_letters("23")`  
returns `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])`  
Example execution 2:  `t9_letters("4663")`  
returns `["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]`
