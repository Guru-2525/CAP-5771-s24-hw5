import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.008
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] =  False
    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    

    answers['(c) Weight update'] = "0.5 * math.log((1 - 0.3) / 0.3)"

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.5275
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"

    # type: explain_string
    answers['Explain'] = "Ensemble methods allow us to improve performance by combining various techniques, but it's crucial for each technique to be trained on relevant historical data. Unfortunately, Alan's random selection method ignores this important requirement."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = "iii"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = "i"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = "ii"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = "iv"
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] =  "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = "yes"

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "Both classifiers show results similar to random chance, as the True Positive Rate (TPR) is the same as the False Positive Rate (FPR). Increasing the likelihood of predicting the positive class doesn't improve the effectiveness of C2, as it raises both TPR and FPR proportionally, leading to performance similar to random chance."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = "precision/recall"

    # type: explain_string
    answers['(c) explain'] = "Precision and recall assess how well positive predictions impact overall performance in both categories. If C1 and C2 have the same True Positive Rates (TPR) and False Positive Rates (FPR), they show comparable performance compared to random guessing in an ROC curve. Nevertheless, precision and recall do not consider true negatives, making them less effective for evaluating classifiers that make random predictions for unevenly distributed classes."

    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = "C2"

    # type: explain_string
    answers['(i) Best classifier, explain'] = "C2 has a much higher rate of accurately identifying positive cases at 50% compared to C1 at only 10%, showing that it is better at detecting positive cases. Even though both classifiers have the same level of precision, C2 is more effective overall."


    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = "precision-recall-F1-Measure"

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "Having a high-quality classifier is crucial for effectively dealing with imbalanced datasets. Metrics such as precision, recall, and the F1-measure provide a thorough assessment of how well a classifier performs. They help determine the classifier's ability to accurately identify positive cases and avoid incorrectly classifying negative cases as positive."


    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = "C3" 

    # type: explain_string
    answers['(iii) best classifier, explain'] = "C3 strikes a balance between precision and recall, with its F1-measure reaching 50%, the highest among the classifiers. This shows that C3 is reliable in accurately identifying positive cases while also maintaining a good level of precision."
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = '0.1'

    # type: eval_float
    answers['(a) recall for C0'] = 'P'

    # type: eval_float
    answers['(b) F-measure of C0'] = '(0.2 * p) / (0.1 + p)'

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'no' 

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] =  {
    'recall': 0.5333,
    'precision': 0.6154,
    'F-measure': 0.5689,
    'accuracy': 0.8800
}

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure' #precision

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy' #accuracy

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = 'Accuracy is the best indicator since it accounts for all correct predictions (both true positives and true negatives) over the total number of samples. Precision is the worst in this context because it does not take into account the correct predictions of the majority class, which can be misleading for imbalanced datasets.'
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = "T1"

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = "T2"

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] ="In medical testing, the F1 score is preferred because it effectively balances precision and recall, making it essential for accurately identifying cases and reducing the danger of missed diagnoses, particularly in critical situations such as cancer detection." 

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "When the cost or impact of incorrect results is high, such as when further tests are risky or expensive, focusing on the ratio of true positives to false positives may be best. This method focuses on reducing false alarms while maintaining a satisfactory rate of correctly identified positives."
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
