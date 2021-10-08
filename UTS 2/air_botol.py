mliter = int(input())

if mliter >= 15000:
    print(22)
elif mliter > 0 and mliter <= 9000 :
    botolBsr = mliter//1500
    print(botolBsr)
elif mliter > 9000 and mliter <= 13200:
    botolBsr = 6
    botolSdg = (mliter-6*1500)//600
    total = botolBsr+botolSdg
    print(total)
elif mliter > 13200 and mliter < 15000:
    botolBsr = 6
    botolSdg = 7   
    botolKcl = (mliter-6*1500-7*600)//200
    total = botolBsr+botolSdg+botolKcl
    print(total)
