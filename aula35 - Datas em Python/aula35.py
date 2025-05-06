import datetime

data = datetime.datetime.now()
nasc = datetime.datetime(1978, 3, 7)

print(str(data.day) + "/" + str(data.month) + "/" + str(data.year))

print(nasc.strftime("%A"))
# %a - dia da semana reduzido
# %A - dia da semana
# %w - numero do dia da semana
# %d - numero do dia do mes
# %b - nome do mes reduzido
# %B - nome do mes
# %m - numero do mes
# %y - ano com dois digitos
# %Y - ano com 4 digitos
# %H - 00 - 23 horas
# %I - 00 - 12 horas
# %p - AM / PM
# %M - minutos
# %S - segundos
# %f - microsegundos
# %j - dia do ano 001 ate 365
# %W - numero da semana do ano
