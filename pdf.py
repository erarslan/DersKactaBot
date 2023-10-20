import camelot

def createProgram (day, sınıf):

    if sınıf == "1":
        df = camelot.read_pdf("PDF\BM1.pdf")[0].df
        df = df.drop(10)
        df = df.drop(0, axis=1)
        df.columns = df.columns - 1
        df[0][0] = "Saatler"
        df[2][0] = "Salı"
        df[3][0] = "Çarşamba"
        df[4][0] = "Perşembe"

        for i in range(1, df.shape[1]):
            if i == 4:
                continue
            df[i][5] = "ÖĞLE ARASI"
    
    elif sınıf == "2":
        df = camelot.read_pdf("PDF\BM2.pdf")[0].df
        df = df.drop(10)
        df[0][0] = "Saatler"
        df[2][0] = "Salı"
        df[3][0] = "Çarşamba"

        for i in range(1, df.shape[1]):
            df[i][5] = "ÖĞLE ARASI"
    
    else:
        df = camelot.read_pdf("PDF\BM3.pdf")[0].df
        df = df.drop(10)
        df = df.drop(0, axis=1)
        df.columns = df.columns - 1
        df[1][0] = "Pazartesi"
        df[0][0] = "Saatler"
        df[2][0] = "Salı"
        df[3][0] = "Çarşamba"
        df[4][0] = "Perşembe"
        df[4][3] = 'MTH-MKK Dijital Dönüşüm Projelerinin \nYönetimi T, Bilgisayar Mühendisliği \n(Türkçe)  Şube 1, -Öğretim Üyesi \nBelirlenmemiş-, Yok'
        df[4][4] = 'MTH-MKK Dijital Dönüşüm Projelerinin \nYönetimi T, Bilgisayar Mühendisliği \n(Türkçe)  Şube 1, -Öğretim Üyesi \nBelirlenmemiş-, Yok'

        for i in range(1, df.shape[1]):
            df[i][5] = "ÖĞLE ARASI"
    
    list = []

    if day == "Pazartesi":
        i = 1
    elif day == "Sali":
        i = 2
    elif day == "Carsamba":
        i = 3
    elif day == "Persembe":
        i = 4
    elif day == "Cuma":
        i = 5
    
    for k in df[i][1:]:
        list.append(k)
    

    list = [i for i in list if i != '']

    liste = []
    baslik_df = df[i][0].upper()
    baslik = f"➡️➡️ {baslik_df} ⬅️⬅️"
    liste.append(baslik)

    for x in list:
        if x == "ÖĞLE ARASI":
            liste.append(f"🆓☕️ {x} ☕️🆓")
            continue
        x = x.replace("\n", "")
        parcalar = x.split(", ")
        output_string = f"""Ders📕 → {parcalar[0]}
Şube🔢 → {parcalar[1]}
Hoca🧑‍🏫 → {parcalar[2]}
Yer🚪 → {parcalar[3]}"""
        liste.append(output_string)
    son_program = "\n****************************\n".join(liste)

    return son_program