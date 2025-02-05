import pandas as pd
import numpy as np
import argparse

# first value is the symmetry, the second is the average intensity, and the third is the label.
train_df = pd.read_csv('data/1/train_1_5.csv', header=None)
test_df = pd.read_csv('data/1/test_1_5.csv', header=None)


def perceptron_update(df, iterations):
    # Initialize the weight
    weight_array = []
    offset_array = []
    weight_details = {}
    weight = np.array([0, 0], dtype=float)
    weight_array.append(weight)
    offset = 0.0
    offset_array.append(offset)
    for i in range(iterations):
        print('This is iteration {}'.format(i))
        for rows in df.iterrows():
            #print('This is row {}'.format(rows[0]))
            x = np.array([rows[1][0], rows[1][1]])
            y = rows[1][2]
            weight_dot_x = np.inner(weight, x)
            condition = y * (weight_dot_x + offset)
            if condition <= 0:
                weight = weight + y * x
                weight_array.append(weight)
                offset += y
                offset_array.append(offset)
    weight_details['weight'] = weight
    weight_details['weight_array'] = weight_array
    weight_details['offset'] = offset
    weight_details['offset_array'] = offset_array
    return weight_details


def predict_test(df, weight_details):
    weight = weight_details['weight']
    print(weight)
    offset = weight_details['offset']
    print(offset)
    predict_list = []
    total_tests = len(df)
    # print(total_tests)
    correct = 0
    for rows in df.iterrows():
        label = rows[1][2]
        x = np.array([rows[1][0], rows[1][1]])
        predict_label = np.inner(weight, x) + offset
        if predict_label > 0:
            predict_label = 1.0
        elif predict_label < 0:
            predict_label = -1.0
        else:
            print('ZOMG')
        predict_list.append(predict_label)
        if predict_label == label:
            correct += 1
    accuracy_score = correct/total_tests
    return accuracy_score


if __name__ == "__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', dest='mode', help='Enter a for 1(a), b for 1(b) or f for All')

    # parse our arguments
    args = parser.parse_args()
    mode = args.mode

    valid_mode = ['a', 'b', 'f']
    if mode and mode not in valid_mode:
        mode = 'f'
    elif mode not in valid_mode:
        mode = 'f'

    question_a_weight = perceptron_update(train_df, 5)
    score_a = predict_test(test_df, question_a_weight)

    question_b_weight = perceptron_update(train_df, 10)
    score_b = predict_test(test_df, question_b_weight)

    switcher = {
        'a': "The accuracy for question 1(a) - 5 iterations is: {}".format(score_a),
        'b': "The accuracy for question 1(b) - 10 iterations is: {}".format(score_b),
        'f': "The accuracy for question 1(a) - 5 iterations is: {}\n"
             "The accuracy for question 1(b) - 10 iterations is: {}".format(score_a, score_b),
    }
    print(switcher.get(mode, "Invalid mode"))


# question_a_weight = perceptron_update(train_df, 5)
# score_a = predict_test(test_df, question_a_weight)
#
# question_b_weight = perceptron_update(train_df, 10)
# score_b = predict_test(test_df, question_b_weight)

# print('The accuracy for question 1(a) - 5 iterations is: {}'.format(score_a))
# print('The accuracy for question 1(b) - 10 iterations is: {}'.format(score_b))
