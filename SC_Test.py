from traitlets import signature_has_traits

import numpy as np 

import matplotlib.pyplot as plt 

import pandas as pd 


A = {"x1": 0.2, "x2": 0.7, "x3": 1.0, "x4": 0}
B = {"x1": 0.3, "x2": 0.6, "x3": 0, "x4": 0.2}
sum, product= {},{}

for a,b in zip(A, B):
  product[a] = round(A[a] * B[b], 1)

for a, b in zip(A, B):
   sum[a] = round((A[a] + B[b]) - (A[a] * B[b]), 1)
   
print("The Algebraic Product is ", product)



print("The Algebraic Sum is", sum)

