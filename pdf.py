import camelot
df = camelot.read_pdf("BM1.pdf")[0].df

# DataFrame Editing

df = df.drop(10)
df[3][0] = "Salı"
df[4][0] = "Çarşamba"
df[5][0] = "Perşembe"
df[1][0] = "Saatler"

for i in range(df.shape[1]):
    if i == 5:
        continue
    df[i][5] = "ÖĞLE ARASI"

df = df.drop(0, axis=1)

# Creating Program

def createProgram (day):
    list = []
    if day == "Pazartesi":
        i = 2
    elif day == "Sali":
        i = 3
    elif day == "Carsamba":
        i = 4
    elif day == "Persembe":
        i = 5
    elif day == "Cuma":
        i = 6
    
    for k in df[i][1:]:
        list.append(k)
    

    list = [i for i in list if i != '']

    liste = []
    baslik_df = df[i][0].upper()
    baslik = f"➡️➡️ <b>{baslik_df}</b> ⬅️⬅️"
    liste.append(baslik)

    for x in list:
        if x == "ÖĞLE ARASI":
            liste.append(f"🆓☕️ <b>{x}</b> ☕️🆓")
            continue
        parcalar = x.split(", ")
        output_string = f"""Ders📕 → {parcalar[0]}
Şube🔢 → {parcalar[1]}
Hoca🧑‍🏫 → {parcalar[2]}
Yer🚪 → {parcalar[3]}"""
        liste.append(output_string)
    bitti = "\n\n".join(liste)

    return bitti