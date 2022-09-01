from sakuraParisAPI import sakura

for en in sakura.tryQuery()[0]:
    print(en.getHeading())
    print(en.getDefinition())