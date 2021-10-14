import hashlib

def aurkitukodea():
    imagen="imagen"
    jpg=".jpg"
    i=1

    while (i<47):

        if(i==27):
            i=i+1

        j=str(i)
        arIzena=imagen+j+jpg
        
        with open(arIzena,"rb") as f:
            kodeOna="e5ed313192776744b9b93b1320b5e268"
            bytes=f.read()

            hasheatu=hashlib.md5(bytes).hexdigest()

            if(hasheatu==kodeOna):
                print("Aurkituta!!!")
                print(arIzena + ":")
                print(hasheatu)
            i= i +1
aurkitukodea()

