#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:42:16 2019

@author: piyush
"""

from flask import Flask, render_template, request, jsonify

import chatbot as cb

app = Flask(__name__)


@app.route('/prediction_in/<input_str>', methods=['GET', 'POST'])
def prediction_in(input_str):
    print("method : {}".format(request.method))
    input_string = str(input_str)
    print("Input: {}\n".format(input_string))
    prediction = str(pred(input_string))
    print("prediction: {}\n".format(prediction))
    return jsonify(prediction)


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    #print(request.get_json(force=True))
    if request.method == "POST":
        input_string = str(request.form.get('message'))
        print("Input: {}\n".format(input_string))
        prediction =cb.output(input_string, cb.states, cb.net, cb.sess, cb.chars, cb.vocab, **cb.params)
        print("prediction: {}\n".format(prediction))
        return jsonify(prediction)
    else:
        return render_template('index.html')

@app.route('/')         #root directory(homepage)
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)

