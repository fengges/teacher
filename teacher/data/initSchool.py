
from teacher.items import *
from teacher.util.mysql import *

import pandas as pd
import numpy as np

data=pd.read_csv("url2.csv",encoding='gbk')

x=np.array(data)
mysql=Mysql()
school = SchoolItem()

for l in x:

    school['school']=l[0].strip()

    school['adpart']=l[1].strip()
    school['url']=l[2].strip()
    mysql.insertSchool(school)