'''Given a string a, find longest substring without repeating characters.
Examples:
Input: "ATTRIBUTE"
Output: "RIBUTE"

Input: "PALINDROME"
Output: "PALINDROME"

Input: "BAILLEY"
Output: "BAIL"'''

def longest_substring(string):
   substr=''
   strlist = []
   for i in range(0,len(string)-1):
       if string[i + 1] != string[i] :
           substr += string[i]
           if i >= len(string)-2:
               substr += string[i+1]
       if string[i + 1] == string[i] :
               substr = ""
       strlist.append(substr)
   print "strlist-->", strlist
   print(max(strlist, key=len))

longest_substring("ATTRIBUTE")