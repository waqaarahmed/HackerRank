"""
Company Logo:
A newly opened multinational brand has decided to base their company logo on the 
three most common characters in the company name. They are now trying out various 
combinations of company names and logos based on this condition. Given a string s, 
which is the company name in lowercase letters, your task is to find the top three 
most common characters in the string.

    -Print the three most common characters along with their occurrence count.
    -Sort in descending order of occurrence count.
    -If the occurrence count is the same, sort the characters in alphabetical order.

Input Format
A single line of input containing the string s. 

Output Format
Print the three most common characters along with their occurrence count each on a 
separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0
aabbbccde

Sample Output 0
b 3
a 2
c 2

"""
import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
   
    s = sorted(input())
    sc = Counter(s)
    most_com = sc.most_common(3)
    for element, count in most_com:
        print(element, count)
