import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os


def politics():
    df_number_of_people_undernourished = pd.read_csv("number_of_people_undernourished.csv")
    df_political_stability_index = pd.read_csv("political_stability_index.csv")

    df_number_of_people_undernourished['Year'] = df_number_of_people_undernourished['Year'].str[:4]
    df_number_of_people_undernourished['Year'] = df_number_of_people_undernourished['Year'].astype('int64')

    columns = ["Year", "Value"]

    df_feature = df_number_of_people_undernourished.loc[:, columns]
    df_feature2 = df_political_stability_index.loc[:, columns]

    merged_df = pd.merge(df_feature, df_feature2, on='Year')

    print(merged_df)

    myplot = sns.scatterplot(x='Value_x', y='Value_y', data=merged_df.loc[:, ["Value_x", "Value_y"]])
    myplot.set_xlabel('number of people undernourished (millions)')
    myplot.set_ylabel('political stability index')

    # do regression and add it here

    myplot.figure.savefig('app\static\politics.png')
    print("File saved successfully")

def politics_find(indep_var):
    pass
    # to find the predicted y value for indep_var using the line of regression

# plt.show()




# def mergesort(array, byfunc=None):
#   mergesort_recursive(array, 0, len(array)-1, byfunc)

# def merge(array, p, q, r, byfunc):
#   ###
#   ### YOUR CODE HERE
#   ###
#   left_ar = array[p:q+1]
#   right_ar = array[q+1: r+1]
#   nl = len(left_ar)
#   rl = len(right_ar)
#   # init block
#   red = p
#   green = 0
#   yellow = 0
#   # while
#   if byfunc is None:
#       while green < nl and yellow < rl:
#           #block a
#           if left_ar[green] <= right_ar[yellow]:
#               # put from the left
#               array[red] = left_ar[green]
#               # block b
#               green += 1
#           else:
#               # put from the right
#               array[red] = right_ar[yellow]
#               # block b
#               yellow += 1
#           red += 1
          
#       # copy remaining elements
#       # left list
#       while green < nl:
#           array[red] = left_ar[green]
#           green += 1
#           red += 1
#       # right list
#       while yellow < rl:
#           array[red] = right_ar[yellow]
#           yellow += 1
#           red += 1
#       print(array)
#   # return array
#       pass
#   else:
#       while green < nl and yellow < rl:
#           #block a
#           if byfunc(left_ar[green]) <= byfunc(right_ar[yellow]):
#               # put from the left
#               array[red] = left_ar[green]
#               # block b
#               green += 1
#           else:
#               # put from the right
#               array[red] = right_ar[yellow]
#               # block b
#               yellow += 1
#           red += 1

#       while green < nl:
#           array[red] = left_ar[green]
#           green += 1
#           red += 1
#       # right list
#       while yellow < rl:
#           array[red] = right_ar[yellow]
#           yellow += 1
#           red += 1
#       print(array)
#       # return array
#       pass

# def mergesort_recursive(array, p, r, byfunc):
#   ###
#   ### YOUR CODE HERE
#   ###
#   if r > p:
#       # get mid point 
#       q = (p + r) // 2
#       # sort left list
#       mergesort_recursive(array, p, q, byfunc)
#       #sort right list
#       mergesort_recursive(array, q+1, r, byfunc)
#       merge(array, p, q, r, byfunc)

# class Stack:
#   def __init__(self):
#     self.__items = []

#   def push(self, item):
#     self.__items.append(item)

#   def pop(self):
#     if self.__items == []:
#       print("Stack len = 0")
#       return None
#     else:
#       return self.__items.pop()
  
#   def peek(self):
#     if self.__items == []:
#       print("Stack len = 0")
#     else:
#       return self.__items[-1]
    
#   @property
#   def is_empty(self):
#     return self.__items == []
  
#   @property
#   def size(self):
#     return len(self.__items)

# class EvaluateExpression:
#   # copy the other definitions
#   # from the previous parts

#   valid_char = '0123456789+-*/() '
#   def __init__(self, string=""):
#     self.expr = string

#   @property
#   def expression(self):
#     return self.expr
    

#   @expression.setter
#   def expression(self, new_expr):
#     string = ""
#     for character in new_expr:
#       if character in self.valid_char:
#         string += character
#     if string == new_expr:
#       self.expr = string
#     else:
#       self.expr = ""

#   def insert_space(self):
#     new_str = ""
#     for character in self.expr:
#       if character in "+-*/()":
#         new_str += " "
#         new_str += character
#         new_str += " "
#       else:
#         new_str += character
#     return new_str

#   def process_operator(self, operand_stack, operator_stack):
#     op1 = operand_stack.pop()
#     op2 = operand_stack.pop()
#     operator_1 = operator_stack.pop()
#     result = 0
#     print(f"op1 = {op1}, op2 = {op2}, operator 1 = {operator_1}")
    
#     if operator_1 == "+":
#       result = op2 + op1
#     elif operator_1 == "-":
#       result = op2 - op1
#     elif operator_1 == "*":
#       result = op2 * op1
#     elif operator_1 == "/":
#       result = op2 // op1
#     operand_stack.push(result)

#   def evaluate(self):
#     operand_stack = Stack()
#     operator_stack = Stack()
#     expression = self.insert_space()
#     tokens = expression.split()
#     print(tokens)
#     for token in tokens:
#       print(f"evaluating {token} token")
#       # if token in "0123456789":
#       #   token = int(token)
#       #   print(f"{token} pushed into operand stack")
#       #   operand_stack.push(token)
#       if token in "+-":
#         print(f"{token} is in +-")
#         if operator_stack.size != 0 and operator_stack.peek() not in "()":
#           print(f"operand_stack size = {operand_stack.size}, operator_stack size = {operator_stack.size}")
#           self.process_operator(operand_stack, operator_stack)
#         # else:
#         #   print("bye")
#         #   operator_stack.push(token)
#         operator_stack.push(token)
#       elif token in "*/":
#         print(f"{token} is in */")
#         if operator_stack.size != 0 and operator_stack.peek() not in "()+-":
#           self.process_operator(operand_stack, operator_stack)
#         operator_stack.push(token)
#         # else:
#         #   print("ok")
#         #   operator_stack.push(token)
#       elif token in "(":
#         print(f"pushing {token} in operator_stack")
#         operator_stack.push(token)
#       elif token in ")":
#         while operator_stack.peek() != "(":
#           print(f"operand_stack size = {operand_stack.size}, operator_stack size = {operator_stack.size}")
#           self.process_operator(operand_stack, operator_stack)
#           print(f"operand_stack size = {operand_stack.size}, operator_stack size = {operator_stack.size}")
        
#         print(operator_stack.pop()) # pops the starting paranthesis
#         print(f"operand_stack size = {operand_stack.size}, operator_stack size = {operator_stack.size}")
#       else:
#         token = int(token)
#         print(f"{token} pushed into operand stack")
#         operand_stack.push(token)

#     while operator_stack.size > 0:
#       self.process_operator(operand_stack, operator_stack)
    
#     return operand_stack.pop()
 

# def get_smallest_three(challenge):
#   records = challenge.records
#   times = [r for r in records]
#   mergesort(times, lambda x: x.elapsed_time)
#   return times[:3]





