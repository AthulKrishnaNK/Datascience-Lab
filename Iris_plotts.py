#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("iris_csv.csv")
print(data.head(100))
print(data.describe())
print(data.info())


# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("iris_csv.csv")
plt.plot(data["sepallength"],"r-")
plt.show()


# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("iris_csv.csv")
data.plot(kind="scatter",x="sepallength",y="petallength")
plt.grid()
plt.show


# In[16]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("iris_csv.csv")
plt.figure(figsize=(10,7))
x=data["sepallength"]
plt.hist(x,bins=20,color="violet")
plt.title("SEPAL LENGTH in cm")
plt.xlabel("sepal_length_cm")
plt.ylabel("count")
plt.show


# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("iris_csv.csv")
plt.figure(figsize=(10,7))
data.boxplot()


# In[ ]:




