#This file holds all functions that can be called
from . import query

def tryQuery():
    return query.queryApi("元気", "広辞苑")