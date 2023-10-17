# Burası tabula ile değiştirelecek (opsiyonel)

import camelot
df = camelot.read_pdf("BM1.pdf")[0].df
df[4][0] = "Çarşamba"
df[5][0] = "Perşembe"

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
    
    for k in df[i]:
        list.append(k)

    for i in range(len(list)):
        if list[i] == "Pazartesi":
            list[i] = f"<b>{list[i]}:</b>\n"
        elif list[i] == "Salı\nÇarşamba\nPerşembe":
            list[i] = "<b>Salı:</b>\n"
        elif list[i] == "Cuma":
            list[i] = "<b>Cuma:</b>\n"
        elif list[i] == "Çarşamba":
            list[i] = "<b>Çarşamba:</b>\n"
        elif list[i] == "Perşembe":
            list[i] = "<b>Perşembe:</b>\n"
        

    program = "\n".join(list)

    return program