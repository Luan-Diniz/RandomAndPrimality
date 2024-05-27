carmichael_factors_list = [
                [3 , 11 , 17],
                [5 , 13 , 17],
                [5 , 17 , 29],
                [7 , 23 , 41],
                [7 , 19 , 67],
                [5 , 29 , 73],
                [43 , 433 , 643],
                [43 , 271 , 5827],
                [53 , 653 , 26479 , 1318579],
                [73 , 599 , 24989 , 546558263 , 1413470422229],
                [67 , 3677 , 5147 , 220523477 , 1306663196317481],
                [23 , 67 , 71 , 89 , 109 , 113 , 191 , 199 , 233 , 239 , 271 , 307 , 373,
                   419 , 521 , 911 , 929 , 1153 , 1217 , 1429 , 2089 , 2729 , 23561],
                [23 , 37 , 43 , 53 , 59 , 61 , 67 , 71 , 89 , 103 , 109 , 113 , 131 , 181 ,
                    191 , 199 , 239 , 271, 311 , 373 , 379 , 419 , 433 , 463 , 521 , 683 , 701 , 911 , 929 ,
                    991 , 1153 , 1429, 2089 , 2551 , 3191 , 4159 , 5279 , 11969 , 15809 , 23561 , 23869 , 244529],
            ]

def number_dividers_carmichael(list_factor):
    return (1 + 1)**len(list_factor)

for carmichael_factors in carmichael_factors_list:
    carmichael = 1
    for factor in carmichael_factors:
        carmichael *= factor

    number_dividers = number_dividers_carmichael(carmichael_factors)
    print(f"Number: {carmichael}")

    # number_dividers - 2 because we don't want 1 neither n.
    # ((carmichael - 2) - 2) is the number of numbers in randint(2, carmichael-2)
    print(f"Probability of not passing the test: {(number_dividers - 2)/((carmichael - 2) - 2)}", end = "")
    print(f"\t (Number of dividers: {number_dividers})")


