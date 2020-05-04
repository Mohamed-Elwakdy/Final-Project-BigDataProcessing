import pandas as pd
import hdfdict
import h5py,time


# IN THIS CODE, DATAFRAMES CONTAINS MANY VARIABLES BASED ON THE NUMBER OF ROWS OF EACH VARIABLE.

dfd = {}

#{1:df1,5:df2,113:df3<-add col} # The dictionary contains many dataframes with different number
                                # rows.

def print_attrs(name, obj):

    print (name)    # "name" contains means all paths
    print (obj)     # "obj" contains the field names and the number of columns and
                    # rows for of columns of each field.
                    
    global dfd

    # '<class \'h5py._hl.dataset.Dataset\'>' indictes to the type of object
    # <class 'h5py._hl.dataset.Dataset'> indicates to the dataset
    # " <class 'h5py._hl.group.Group'>" indictes to the subgroup.
    
    if '<class \'h5py._hl.dataset.Dataset\'>' == str(type(obj)):
        k= str(len(obj))     # k indicates to the length of each object. The objects will have
                             # different number of rows
        #print (k)
        #print (type(obj))
                             
        if k not in dfd.keys():
            df = pd.DataFrame()
            #print(name,"Adding new key for len ", k)
        else:
            df = dfd[k]
        df[name] = obj      # "name" will be the name of the column. Take the object
                            # and make it a value.
                            # we get the key and turn out the data into a dataframe
                            # related to that key.

                            # split all columns, whcih have more than one item, to many columns with removing the parentheses and commas 
        df = pd.concat([pd.DataFrame(df[c].tolist()).add_prefix(c) for c in df.columns], axis=1)
        
        dfd[k] = df
        
        l = len(obj[0])
        
        #print (l)
        #print(dfd.keys())
        
        print(name,"Adding col to dfd index ", k)
        #print(dfd.keys())
    #for key, val in obj.attrs.items():
    #    print("    %s: %s" % (key, val),type(val))

f = h5py.File('walking5.h5', 'r') # Read h5 file
f.visititems(print_attrs) # visititems is for visit all objects in this group and subgroups
                          # In this case, object will be a Dataset instance

for name in f:
    print(name)
res = hdfdict.load("walking5.h5")
print(res.keys())

writer = pd.ExcelWriter('hd5excelout18.xlsx', engine = 'xlsxwriter')
for k, df in dfd.items():
    print(k,len(df)) # print the key number and the number of rows for each dataframe
    df.columns = df.columns.str.replace(r'\d+', '') # remove all number (Zeros) of columns which have the same name 
    df.to_excel(writer, sheet_name = 'sheet_len_'+k, index= False)
writer.save()
writer.close()
