import vt 
from csvv import sha256
import time
a = sha256()
client = vt.Client("0c3129508a0774cade273706af8fb9491ea77612bd8e478c8e10daf30a44c1e3")
print('Hangisiyle islem yapmak istiyorusunuz.\n1-Sigcheck csv\n2-Dosya ismi')
tur = int(input())

if(tur==1):
    print("sigcheckten Aldiginiz csv dosyasini ismini ya da pathini yaziniz =")
    o=input()
    hashs=a.withcsv(o)
    size = []
    for hash in hashs :
        vtt="/files/{}".format(hash)
        print(vtt)
        file = client.get_object(vtt)
        for anahtar, deger in file.last_analysis_stats.items():
          print(f'{anahtar}: {deger}')
        time.sleep(5)
    print(size)    
else:
   print("Hash kodu cikarilip taramasi yapilmasini istediginiz dosyayi giriniz =")
   p=input()
   hashcode=a.withfile(p)
   vtt="/files/{}".format(hashcode)
   file = client.get_object(vtt)
   for anahtar, deger in file.last_analysis_stats.items():
     print(f'{anahtar}: {deger}')
   time.sleep(5)
   

   

   
   
   



"""print(vtt)
file = client.get_object("vtt")
print(file.size)
print("kljalskj")
print(file.type_tag)
print("vvvvvvvvvvvvvv")
print(file.last_analysis_stats)
print("vvvvvvvvvvvvvv")
#a = sha256("snrtt.csv")
"""