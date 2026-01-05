import random

rastgele_sayi = random.randint(1,39)
tahmin_hakki= 7
print("Bil bakalım bende hangi sayı gizli , ipucu -->  1 ile 40 arasında bir sayı giriniz ,Dikkat 7 hakkın varrrrr:")
#print(rastgele_sayi)
tahmin=0
while True :
    giris = input("tahmin ettiginiz sayi nedir : ")
    try:
        tahmin = int(giris)
        # integer olduğunda döngüden çık

        if tahmin > 40 and tahmin_hakki != 0 :
            print("Sen MİLYARRR, senn üç milyar yedi yüz elli milyonnn milyarrr sen bu parayı ne yaptın,niy bu kadar buyuk sayi giriyorsunn ")
            tahmin_hakki -= 1
        elif tahmin < 0 and tahmin_hakki != 0 :
            print("istersen dünyanın ilk oluşum tarihinden başla sen bilirsin .")
            tahmin_hakki -= 1
        elif tahmin > rastgele_sayi and tahmin_hakki != 0 :
            if abs(rastgele_sayi - tahmin) <= 5:
                print("yaklastin  biraz daha kucuk gir")
                tahmin_hakki -= 1
            else:
                print("cok buyuk atma")
                tahmin_hakki -=1

            if  tahmin_hakki == 0:
                print("Oyundan atildiniz bi turlu dogru tahmine bulunamadiniz . defolun burdan ")
                break
        elif tahmin < rastgele_sayi and tahmin_hakki!=0 :
            if abs(rastgele_sayi - tahmin) <= 5:
                print("yaklastin biraz  daha buyuk  gir")
                tahmin_hakki -= 1
            else:
                print("çok küçük atma")
                tahmin_hakki -= 1

            if  tahmin_hakki == 0:
                print("Oyundan atildiniz bi turlu dogru tahminde bulunamadiniz . defolun burdan ")
                break
        elif tahmin == rastgele_sayi :
            if tahmin_hakki > 5:
                print("İşte cesaret, işte feraset, işte fazilet, işte fedakarlık, işte mertlik, işte adam gibi adamlık ,Dogru tahminnnn")
            if tahmin_hakki == 5:
                print("ohaaaa  daha 5 hakkında daha vardı ama sen buldunnnnn")
                print ("bravooo doğru tahmin , kedi olalı bir fare tuttun ")
            elif tahmin_hakki == 4:
                print("tebrikler doğru tahmin")
            elif tahmin_hakki <= 3 and tahmin_hakki > 1:
                print("doğru tahmin ama hiç bulmasaydın da olurdu, kendini niye yordunn ")
            elif tahmin_hakki == 1:
                print("Tırrekkk ,az daha bilmeseydin yanıyordunn. Doğru tahmin ")
            break
    except ValueError:
        print("Küfür mü ettin lan , ne söylediysen hepsi sana donsunn, tahmin hakkini 1 adet düşürdüm")
        tahmin_hakki -= 1
