#!/usr/bin/python3
def multiple_returns(sentence):
    s = 0
    for i in sentence:
        s += 1
    if s == 0:
        return (0, None)
    else:
        return (s, sentence[0])

