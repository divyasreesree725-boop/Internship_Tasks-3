from solutions import (
    q1_word_frequency,
    q2_char_frequency,
    q3_First_non_repeating_char,
    Q4_anagrams,
    q5_First_Repeating_Character,
    q6_All_Zeros,
    q7_Second_Highest,
    q8_Duplicates,
    q9_Missing_Number,
    q10_two_sum,
    q11_Number_Closest,
    q12_commom_elements,
    q13_K_Positions,
    q14_max_sum_of_consecutive,
    q15_all_pairs

)

def run_tests():
    print("--- Running Q1: Word Frequency ---")
    print(q1_word_frequency("python is easy and python is powerful"))
    

    print("--- Running Q2: char Frequency ---")
    print(q1_word_frequency("Banana"))


    print("--- Running Q3:  First Non-Repeating Character ---")
    print(q3_First_non_repeating_char('swiss'))


    print("--- Running Q4: Anagram ---")
    print(Q4_anagrams('listen','silent'))


    print("--- Running Q5: First_Repeating_Character ---")
    print(q5_First_Repeating_Character('Programming'))
  

    print("--- q6_All_Zeros ---")  
    print(q6_All_Zeros([0, 3, 0, 1, 2, 0, 4]))


    print("--- q7_Second_Highest ---")
    print(q7_Second_Highest([10, 20, 40, 30, 40, 20]))


    print("---q8_Duplicates ---")
    print(q8_Duplicates([4, 2, 4, 5, 2, 7, 5]))


    print("---q9_Missing_Number---")
    print(q9_Missing_Number([1,2,4,5,6],6))


    print("---q10_two_sum---")
    print(q10_two_sum([2, 7, 11, 15],9))


    print("---q11_Number_Closest---")
    print(q11_Number_Closest([-8, -3, 2, 5, -2]))


    print("---q12_commom_elements---")
    print(q12_commom_elements([1, 2, 3, 4, 5],[3, 4, 5, 6, 7]))


    print("---q13_K_Positions---")
    print(q13_K_Positions( [1, 2, 3, 4, 5],2))


    print("---q14_max_sum_of_consecutive---")
    print(q14_max_sum_of_consecutive([4, 7, 2, 9,5]))


    print("---q15_all_pairs---")
    print(q15_all_pairs( [2, 4, 3, 5, 7, 8, 1],9))

run_tests()