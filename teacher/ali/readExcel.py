
import pandas as pd

data=pd.read_excel("data/训练.xlsx",sheetname=0)
label=data.columns[-1]
feature=list(data.columns[1:-1])

X_all = data[feature]
y_all = data[label]

def preprocess_features(X):
    ''' Preprocesses the student data and converts non-numeric binary variables into
        binary (0/1) variables. Converts categorical variables into dummy variables. '''

    # Initialize new output DataFrame
    output = pd.DataFrame(index=X.index)

    # Investigate each feature column for the data
    for col, col_data in X.iteritems():

        # If data type is non-numeric, replace all yes/no values with 1/0
        if col_data.dtype == object:
            col_data = col_data.replace(['yes', 'no'], [1, 0])

        # If data type is categorical, convert to dummy variables
        if col_data.dtype == object:
            # Example: 'school' => 'school_GP' and 'school_MS'
            col_data = pd.get_dummies(col_data, prefix=col)

            # Collect the revised columns
        output = output.join(col_data)

    return output


X_all = preprocess_features(X_all)
for i in range(len(X_all.columns)):
    col=X_all.columns[i]
    dic={}
    for v in col:
        dic[str(v)]=1
    if len(dic)<=1:
        print(X_all.columns[i])
print(X_all.head())
print("Processed feature columns ({} total features):\n{}".format(len(X_all.columns), list(X_all.columns)))