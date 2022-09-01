from sakuraParisAPI import sakura

a = sakura.tryQuery()

for en in a[0]:
    print(en.getHeading())