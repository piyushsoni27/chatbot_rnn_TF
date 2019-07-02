#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:04:13 2019

@author: piyush
"""

import tensorflow as tf

import chatbot as cb

#params = cb.params
#print(params)

inp = "Hi"
reply = cb.output(inp, cb.states, cb.net, cb.sess, cb.chars, cb.vocab, **cb.params)

print(reply)