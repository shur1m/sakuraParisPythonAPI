from sakuraParisAPI.sakura import JpDict

a = JpDict()
a.setMax(10)
a.enableTags()

results = a.endsWith("元気")

for key in results:
    print("______", key, "______")
    for entry in results[key]:
        print(entry.getHeading())
        print(entry.getDefinition())

    print(len(results[key]))
    print()