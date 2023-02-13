from datetime import date 

def calculaIdade(dia, mes, ano):
    diaAtual = int(format(date.today(), "%d"))
    mesAtual = int(format(date.today(), "%m"))
    anoAtual = int(format(date.today(), "%Y"))
    diferencaAno = anoAtual - ano
    diferencaMes = mesAtual - mes
    diferencaDia = diaAtual - dia 
    if(diferencaAno >= 18):
        if(diferencaMes == 0 ):
            if(diferencaDia == 0):
                return True
    return False

print(calculaIdade(13, 2, 2005))