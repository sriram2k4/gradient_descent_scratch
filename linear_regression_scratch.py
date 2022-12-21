import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Student_Study_Hour.csv")
x = data.iloc[:,0].values
y = data.iloc[:,1].values



def finding_predicted_y(m=1, c=0.1):
    for i in range(6):
        total_mse = 0
        partial_derivative_c = 0
        partial_derivative_m = 0

        #Predicting Yp using own made m and c
        for i in range(len(x)):
            yp = m*x[i] + c

            # Mean Square Error
            total_mse += (y[i]-yp)**2

            # Partial differentiating m and c
            partial_derivative_c += (yp - y[i])*x[0]
            partial_derivative_m += (yp - y[i])

            # Mean Square Error
            total_mse += (y[i]-yp)**2

        # print("total_der_c = ",partial_derivative_c)
        # print("total_der_ m = ",partial_derivative_m)
        # print("total mean square error = ",total_mse)
        # print("old m is ",m)
        # print("old c is ",c)

        # Derive the New m and c
        print("new m is ",m-(0.001*partial_derivative_m))
        print("new c is ",c-(0.001*partial_derivative_c))
        print('-------------------')
        m = m-(0.001*partial_derivative_m)
        c = c-(0.001*partial_derivative_c)

def predict(x):
    y = 5.594670195724941*x + 11.586675489312357
    print(y)

predict(6)
finding_predicted_y(m=1, c=0.1)
