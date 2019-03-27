import pandas as p

x = {'column1': p.Series(['A','B','C','D']),'column2': p.Series([1, 2.1, 3.2, 5.1]),'column3':p.Series([10,20,30,40])}

columns = p.DataFrame(x);

print(columns);
