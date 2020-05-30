import csv

print('Crearting CSV file')
with open('firts example.csv', 'w', newline='') as csvfile:
    fieldname = ['No','Firts Name','Last Name'] 
    writer = csv.DictWriter(csvfile,fieldname);
    writer.writerow({'No':1,'Firts Name':'John','Last Name':'Smith'})
    writer.writerow({'No':2,'Firts Name':'Piter','Last':'Smith'})
    writer.writerow({'No':3,'Firts Name':'Allan','Last': 'Smith'})
    writer.writerow({'No':4,'Firts Name':'John','Last': 'Poe'})
