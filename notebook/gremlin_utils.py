### Utility Functions for GREMLIN-ML notebook
# imports
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import mean_squared_error

# Plotting 

def result_plot(true,preds):
    '''
    Small function to plot a jointplot in seaborn, comparing true values vs predictions
    '''
    sns.jointplot(x=true, y=preds, kind="hex", color="#4CB391")

    plt.xlabel('True Labels')
    plt.ylabel('Predictions')
    plt.xlim([-5,60])
    plt.ylim([-5,60])

    plt.tight_layout()

# Results

def rmse_results(test_true, val_true, test_preds, val_preds):
    '''
    Function to print RMSE values, and the difference for two sets,
    generally a test set and a validation set. 
    '''
    test_rmse = np.round(mean_squared_error(test_true, test_preds),2)
    print('test set RMSE:', test_rmse)
    val_rmse = np.round(mean_squared_error(val_true, val_preds), 2)
    print('val set RMSE:', val_rmse)
    print('difference:', np.round(np.abs(test_rmse-val_rmse),1))

# end