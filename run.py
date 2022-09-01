from sakuraParisAPI.sakura import JpDict

a = JpDict()

a.addDict("大辞林")
results = a.search("元気")

for key in results:
    print("______", key, "______")
    for en in results[key]:
        print(en.getHeading())
        print(en.getDefinition())

    print()

print(a.getDict())