# Objective
# In this challenge, we practice using multiple linear regression to predict housing prices. Check out the Resources tab for helpful videos!
#
# Task
# Charlie wants to buy a house. He does a detailed survey of the area where he wants to live, in which he quantifies, normalizes, and maps the desirable features of houses to values on a scale of  to  so the data can be assembled into a table. If Charlie noted  features, each row contains  space-separated values followed by the house price in dollars per square foot (making for a total of  columns). If Charlie makes observations about  houses, his observation table has  rows. This means that the table has a total of  entries.
# 
# Unfortunately, he was only able to get the price per square foot for certain houses and thus needs your help estimating the prices of the rest! Given the feature and pricing data for a set of houses, help Charlie estimate the price per square foot of the houses for which he has compiled feature data but no pricing.
# 
# Important Observation: The prices per square foot form an approximately linear function for the features quantified in Charlie's table. For the purposes of prediction, you need to figure out this linear function.
#
# Recommended Technique: Use a regression-based technique. At this point, you are not expected to account for bias and variance trade-offs.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from sklearn.linear_model import LinearRegression
    
if __name__ == '__main__':
    [F,H] = [int(k) for k in input().strip().split(' ')]
    dtrain = []
    for i in range(H):
        dtrain.append([float(k) for k in input().strip().split(' ')])
    dtrain = np.asarray(dtrain)
    H2 = int(input().strip())
    dpred = []
    for i in range(H2):
        dpred.append([float(k) for k in input().strip().split(' ')])
    dpred = np.asarray(dpred)
    
    reg = LinearRegression().fit(dtrain[:,:-1],dtrain[:,-1])
    for k in reg.predict(dpred):
        print('{:.2f}'.format(k))
