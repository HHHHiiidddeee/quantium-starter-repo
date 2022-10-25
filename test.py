from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

from task4 import update1, update2

def test_header():
    output = update1(1,0)
    assert output == "button 1: 1 & button 2: 0"

def test_graph():
    output = update2(1,0)
    assert output == "button 1: 1 & button 2: 0"

test_header()
test_graph()