# Q1 Find the Frequency of Each Word in a Sentence

def q1_word_frequency(s):
    w = s.split(' ')
    d = {}
    for i in w:
        d[i]=w.count(i)
    return d


#print(q1_word_frequency("python is easy and python is powerful"))

# Q2. Find the Frequency of Each Character in a Word

def q2_char_frequency(s):
    d = {}
    for i in s:
        d[i]=s.count(i)
    return d

#print(q2_char_frequency('banana'))


# Q3. Find the First Non-Repeating Character in a Word
def q3_First_non_repeating_char(s):
    d = {}
    for i in s:
        d[i]=s.count(i)
    for i in d:
        if d[i] == 1:
            return i
    
#print(q3_First_non_repeating_char('swiss'))

#Q4. Check Whether Two Strings Are Anagrams

def Q4_anagrams(s1,s2):
    return sorted(s1) == sorted(s2)



#print(Q4_anagrams('listen','silent'))

# Q5. Find the First Repeating Character in a String
def q5_First_Repeating_Character(s):
    d={}
    for i in s:
        d[i] = s.count(i)
    for i in d:
        if d[i]>1:
            return i

#print(q5_First_Repeating_Character('Programming'))

def q6_All_Zeros(l):
    l1 = []
    for i in l:
        if i != 0:
            l1.append(i)
    n = l.count(0)
    return l1+[0]*n

#print(q6_All_Zeros([0, 3, 0, 1, 2, 0, 4]))

def q7_Second_Highest(l):
    l1 = []
    for i in l:
        if i not in l1:
            l1.append(i)
    l1.sort()
    return l1[-2]


#print(q7_Second_Highest([10, 20, 40, 30, 40, 20]))

#Q8. Remove Duplicates Without Changing the Original Order
def q8_Duplicates(l):
    l1 = []
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1

#print(q8_Duplicates([4, 2, 4, 5, 2, 7, 5]))

#Q9. Find the Missing Number from 1 to N
def q9_Missing_Number(l,n):
    l1 = []
    for i in range(1,n+1):
        l1.append(i)
    for i in l1:
        if i not in l:
            return i

#print(q9_Missing_Number([1,2,4,5,6],6))

#Q10. Find Two Numbers Whose Sum Equals a Target

def q10_two_sum(nums, target):
    seen = {}
    for num in nums:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen[num] = True
    return []


#print(q10_two_sum([2, 7, 11, 15],9))

#Q11. Find the Number Closest to Zero
def q11_Number_Closest(l):
    l1 = []
    l2 = []
    for i in l:
        if i >= 0:
            l1.append(i)
        else:
            l2.append(i)
    l1.sort()
    l2.sort()
    if l2[0]*-1 >= l1[0]:
        return l1[0]
    else:
        return l2[0]
        
#print(q11_Number_Closest([-8, -3, 2, 5, -2]))

#Q12. Find Common Elements Between Two Lists
def q12_commom_elements(l1,l2):
    l3=[x for x in l1 if x in l2]
    return l3

#print(q12_commom_elements([1, 2, 3, 4, 5],[3, 4, 5, 6, 7]))

#Q13. Rotate a List to the Right by K Positions
def q13_K_Positions(l,k):
    l1 = []
    for i in range(1,k+1):
        l1.append(l[i*-1])
    l1 = l1[::-1]
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1

# print(q13_K_Positions( [1, 2, 3, 4, 5],2))


#Q14. Find the Maximum Sum of Two Consecutive Elements
def q14_max_sum_of_consecutive(l):
    l1= []
    for i in range(len(l)-1):
        l1.append(l[i]+l[i+1])
    return(max(l1))
#print(q14_max_sum_of_consecutive([4, 7, 2, 9,5]))

#Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def q15_all_pairs(nums,target):
    l1 = []
    s = set(nums)
    for i in s:
        t = target-i
        if t in s and i < t:
            l1.append([i,t])
    return l1
#print(q15_all_pairs( [2, 4, 3, 5, 7, 8, 1],9))

