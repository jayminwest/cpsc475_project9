"""
Jaymin West
CPSC 475
Fall, 2022
Project 9

Description:
    A very simple program that computes cosine similarities between
    two words given their contexts in the form of a table

Output: 
********
    Computing Cosine Similarities: 
    Word 1 - Word 2:  0.141
    Word 2 - Word 3:  0.998
    Word 1 - Word 3:  0.095
********
Word 1 is likely "woman"
Word 2 is likely "queen"
Word 3 is likely "king"

Woman and Queen are slightly related in gender, however, are rarley used in the same context as they both refer
    to individuals so saying something like "she was a woman queen" is redundant. 
    
Queen and King are often used in the same context. "They were the king and queen". Because of this they are highly related

King and woman are very rarley used together. They do not share a gender or a royal status. 
"""
import math # used for square root

def compute_cosine_similarity(word1, word2):
    """Driver function of the program
    args:
        word1, word2: rows from co-occurence matrix representing word context values
    returns:
        the cosine similarity of these two words
    """
    sum_xx = sum_xy = sum_yy = 0

    for i in range(len(word1)):
        x, y = word1[i], word2[i]

        sum_xx += x * x # denominator
        sum_yy += y * y # denominator
        sum_xy += x * y # numerator

    # full equation (rounded to 3 decimal points):   
    return round(sum_xy / math.sqrt(sum_xx*sum_yy), 3)

# Matrix representing word-word co-occurence matrix given in assignment sheet:
matrix = [
        [10, 82, 0, 4, 275], # word 1
        [85, 5, 4, 0, 8], # word 2
        [237, 20, 4, 1, 9] # word 3
        ]
# Printing the results:
print("Computing Cosine Similarities: ")
print("Word 1 - Word 2: ", compute_cosine_similarity(matrix[0], matrix[1]))
print("Word 2 - Word 3: ", compute_cosine_similarity(matrix[1], matrix[2]))
print("Word 1 - Word 3: ", compute_cosine_similarity(matrix[0], matrix[2]))
