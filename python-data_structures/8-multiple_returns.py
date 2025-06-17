#!/usr/bin/python3
def multiple_returns(sentence):
    s = 0
    for i in sentence:
        s += 1
    if s == 0:
        return ("length: 0 - First character: None")
    else:
        return (f"Length: {s} - First character: {sentence[0]}")
