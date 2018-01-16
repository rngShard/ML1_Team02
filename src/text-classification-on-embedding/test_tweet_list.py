#! /usr/bin/env python
'''
The Target Names:  [0:'csu', 1:'fdp', 2:'afd', 3:'gruene', 4:'die-linke', 5:'spd', 6:'cdu']
'''
import tensorflow as tf
import numpy as np
import os
import data_helpers
from tensorflow.contrib import learn
import csv
from sklearn import metrics
import yaml


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    if x.ndim == 1:
        x = x.reshape((1, -1))
    max_x = np.max(x, axis=1).reshape((-1, 1))
    exp_x = np.exp(x - max_x)
    return exp_x / np.sum(exp_x, axis=1).reshape((-1, 1))

def evaluateFile(read_file):
    x_raw = list(open(read_file, "r").readlines())
    print(x_raw)
    prob = evaluateList(x_raw)
    return prob

def evaluateList(tweet_list, batch_size=64,
                 checkpoint_dir="./runs/trained_model/checkpoints/"):
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    # CHANGE THIS: Load data. Load your own data here
    dataset_name = cfg["datasets"]["default"]
    print('dataset_name: ', dataset_name)
    x_raw = tweet_list
    # Map data into vocabulary
    vocab_path = os.path.join(checkpoint_dir, "..", "vocab")
    vocab_processor = learn.preprocessing.VocabularyProcessor.restore(
        vocab_path)
    x_test = np.array(list(vocab_processor.transform(x_raw)))
    print("Vocabulary Size: {:d}".format(len(vocab_processor.vocabulary_)))
    # print("Train/Dev split: {:d}/{:d}".format(len(y_train), len(y_dev)))
    print("size of x_test:", len(x_test))

    print("\nEvaluating...\n")

    # Evaluation
    # ==================================================
    checkpoint_file = tf.train.latest_checkpoint(checkpoint_dir)
    graph = tf.Graph()
    with graph.as_default():
        session_conf = tf.ConfigProto(
            allow_soft_placement=True,
            log_device_placement=False)
        sess = tf.Session(config=session_conf)
        with sess.as_default():
            # Load the saved meta graph and restore variables
            saver = tf.train.import_meta_graph("{}.meta".format(checkpoint_file))
            saver.restore(sess, checkpoint_file)
            # Get the placeholders from the graph by name
            input_x = graph.get_operation_by_name("input_x").outputs[0]
            # input_y = graph.get_operation_by_name("input_y").outputs[0]
            dropout_keep_prob = graph.get_operation_by_name(
                "dropout_keep_prob").outputs[0]
            # Tensors we want to evaluate
            scores = graph.get_operation_by_name("output/scores").outputs[0]
            # Tensors we want to evaluate
            predictions = graph.get_operation_by_name(
                "output/predictions").outputs[0]
            # Generate batches for one epoch
            batches = data_helpers.batch_iter(list(x_test),
                                              batch_size, 1, shuffle=False)
            # Collect the predictions here
            all_predictions = []
            all_probabilities = None
            for x_dev_batch in batches:
                batch_predictions_scores = sess.run([predictions, scores],
                                                    {input_x: x_dev_batch,
                                                     dropout_keep_prob: 1.0})
                all_predictions = np.concatenate([all_predictions,
                                                  batch_predictions_scores[0]])
                probabilities = softmax(batch_predictions_scores[1])
                if all_probabilities is not None:
                    all_probabilities = np.concatenate([all_probabilities,
                                                        probabilities])
                else:
                    all_probabilities = probabilities
    #print(all_predictions)
    #print(all_probabilities)
    #mean_prob = np.mean(all_probabilities, axis=0)
    #print(mean_prob)
    #print(np.argmax(mean_prob))
    #dict_voting={0:0,1:0,2:0,3:0,4:0,5:0,6:0}
    counts = np.bincount(all_predictions.astype(int))
    max_occur = np.argmax(counts)
    print("MaxVoting: Belongs to Party: ", max_occur)
    indices = [i for i, x in enumerate(all_predictions) if x == max_occur]
    good_probabilities = all_probabilities[indices]
    mean_prob = np.mean(good_probabilities, axis=0)
    print("Probability: Belongs to Party: ", np.argmax(mean_prob))
    print("Probability Distribution \n", mean_prob)
    return mean_prob
