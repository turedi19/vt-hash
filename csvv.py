import csv
import hashlib
class sha256:
      
  def withcsv(self,file_name):
    self.file_name = file_name
    print("Hangi hash turu ile islem yapmak istiyorsunuz?\n1-MD1\n2-SHA1\n5-SHA256")
    l=int(input())-1
    
    # initializing the titles and rows list
    fields = []
    m = []
    k = []
    with open(self.file_name, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # extracting field names through first row
        # sha is find.
        fields = next(csvreader)
        print(fields[l+10])
        print("asdasd")
        for row in csvreader:
            k.append(row[l+10].split(", "))
            u = '{}'.format(k)
            x = u.split("'")
           
            m.append(x[1])
    return m
        
    
  def withfile(self,file_kod):
      self.file_kod = file_kod
      



     # make a hash object
      h = hashlib.sha1()

   # open file for reading in binary mode
      with open(file_kod,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)
       print(h.hexdigest())
   # return the hex representation of digest
      return h.hexdigest()
     


  
"""a= sha256()
hash=a.withfile('snrtt.csv')"""





"""# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
 
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
 
# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')"""