#!/usr/bin/python3
def multiple_return(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
