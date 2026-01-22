import time
import os

# Oyun Verileri (Karakter Bilgileri)
can = 100
altin = 50
envanter = []

def temizle():
    # Ekranı temiz tutar (Siyah ekranda daha iyi görünür)
    os.system('cls' if os.name == 'nt' else 'clear')

def oyun_baslat():
    global can, altin, envanter
    
    while True:
        temizle()
        print(f"--- VENGEANCE CRAFT v1.0 ---")
        print(f"Can: {can} | Altın: {altin}")
        print(f"Envanter: {envanter}")
        print("----------------------------")
        print("1- Madene Git (Taş Topla)")
        print("2- Ormana Git (Odun Topla)")
        print("3- Markete Git (Eşya Sat/Al)")
        print("4- Dinlen (+20 Can)")
        print("5- Oyundan Çık")
        
        secim = input("\nNe yapmak istersin? (1-5): ")

        if secim == "1":
            print("\nMadende çalışıyorsun... ⛏️")
            time.sleep(2)
            envanter.append("Tas")
            can -= 10
            print("Bir 'Tas' kazandın! 10 Can gitti.")
            time.sleep(1)

        elif secim == "2":
            print("\nOrmanda ağaç kesiyorsun... 🪓")
            time.sleep(2)
            envanter.append("Odun")
            can -= 5
            print("Bir 'Odun' topladın! 5 Can gitti.")
            time.sleep(1)

        elif secim == "3":
            print("\nMarkete hoş geldin! 💰")
            if "Tas" in envanter:
                envanter.remove("Tas")
                altin += 20
                print("1 Tas sattın, 20 Altın kazandın!")
            else:
                print("Satacak bir şeyin yok!")
            time.sleep(2)

        elif secim == "4":
            print("\nDinleniyorsun... 💤")
            can += 20
            if can > 100: can = 100
            time.sleep(2)

        elif secim == "5":
            print("Kaptan, VengeanceCraft'tan ayrılıyor...")
            break
        
        if can <= 0:
            print("\nÖldün! Oyun bitti.")
            break

# Oyunu çalıştıran komut
oyun_baslat()
