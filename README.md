# The Unofficial Sakura Paris Python API (TUSPPAPI)
✨ *Because one dictionary is never enough* ✨

### Table of Contents
* [More than just a wrapper (Intro)](https://github.com/shur1m/sakuraParisPythonAPI#more-than-just-a-wrapper)
* [Install the Package](https://github.com/shur1m/sakuraParisPythonAPI#install-the-package)
* [Documentation](https://github.com/shur1m/sakuraParisPythonAPI#documentation)

## More than just a wrapper
Have you ever wanted to search 40 different Japanese dictionaries at the same time? Well now you can anyways!

Introducing the wrapper that queries the [sakura-paris](https://sakura-paris.org/About/%E5%BA%83%E8%BE%9E%E8%8B%91%E7%84%A1%E6%96%99%E6%A4%9C%E7%B4%A2)'s free Koujien search API（広辞苑無料検索） for a lot of dictionaries. This includes Daijirin, Koujien, Daijisen, and even oddballs like a dictionary for psychological terms（心理学辞典）.

If that wasn't enough, this wrapper allows you to query selected dictionaries at the same time, and also allows searches over the 40 entry limit on sakura-paris! If you've ever been at a loss for which dictionary to pick, you're at the right place!

That's enough talk. Here's an example of how easy it is to use.

```python
#import the package!
from sakuraParisAPI.sakura import JpDict

#create JpDict object
a = JpDict()

#each dictionary will return at most 10 entries (default value is already 10)
a.setMax(10)

#add dictionary to be queries ("広辞苑" is added by default, so this will query 2 dictionaries)
a.addDict("大辞林")

#returns a dictionary where [key = dictionary_name, value = list of Entry]
results = a.search("元気")

#for every dictionary queried
for key in results:
    print("______", key, "______")
    
    #for every entry found in dictionary
    for entry in results[key]:
    
        #print out the word and its definition
        print(entry.getHeading())
        print(entry.getDefinition())
        
    print()

#print out all dictionaries used in this query
print(a.getDict())
```

Also, by adding a single line before calling `search(word)`, we can query all dictionaries at the same time.

```python
a.addAllDict()
```
and ***voila***. 40 dictionaries at your fingertips. Minus a couple cause the API returns empty jsons for them. :')

## Install the Package
This package can be downloaded using PIP! <br>
Here is the command for the latest version: `pip install sakuraParisAPI==0.1.1` <br>
SPPAPI has two dependencies: bs4 and requests, and both will also be installed by the above command

## Documentation
All public methods of the JpDict and Entry class are listed below. Supported Dictionaries are also listed. <br>
Please note that the API does not work with a few dictionaries (e.g. 学研古語辞典, NHK日本語発音アクセント辞典). I will be using bs4 or something similar to implement these features later. Especially for the NHK accent dictionary, I hope to return the links to the .wav files for each entry.

<br>

| JpDict Method | Parameter Types | Return Type | Description | 
|-|-|-|-|
| `search(word, searchType = 0)` | str, int (0 - 2) | dict[str, list[Entry]] | queries active dictionaries for `word` with search type `searchType`. `searchtype = 0` by default and searches for dictionary entries with prefixes matching `word`. `searchtype = 1` searches for suffixes matching `word` and `searchtype = 2` searches for exact matches only. <br> Returns a dictionary where keys are the name of the dictionary queried and value is a list of `Entry`|
| `startsWith(word)` | str | dict[str, list[Entry]] | Queries dictionary for entries that start with `word`. Same return type as `search`.|
| `endsWith(word)` | str | dict[str, list[Entry]] | Queries dictionary for entries that end with `word`. Same return type as `search`.|
| `completeMatch(word)` | str | dict[str, list[Entry]] | Queries dictionary for entries that are exact matches for `word`. Same return type as `search`.|
| `setMax(maxEntries)` | int | void | Sets the max number of entries (for each dictionary) returned by any of the above functions to `maxEntries` |
| `addDict(dictionaryName)` | str | void | adds `dictionaryName` to set of dictionaries to be queried if it exists. |
| `addAllDict()` | | void | adds all possible dictionaries to set of dictionaries to be queried.|
| `removeDict(dictionaryName)` | str | void | removes `dictionaryName` from the set of dictionaries to be queried if it exists. |
| `clearDict()` | | void | removes all dictionaries from set of dictionaries to be queried. |
| `getDict()` | | list(str) | returns a list of the names of all active dictionaries. |
| `getAllDict()` | | set(str) | returns a set of the names of all possible dictionaries that can be queried. |
| `enableTags()` | | void | prevents markdown tags from being removed from the `heading` and `definition` fields of `Entry`s returned in searches. |
| `disableTags()` | | void | ensures markdown tags are removed from the `heading` and `definition` fields of `Entry`s returned in searches. |

|Entry Method| Parameter Types | Return Type | Description |
|-|-|-|-|
|`getHeading()` | | str | returns heading listed in dictionary entry. |
|`getDefinition()` | | str | returns the definition listed in dictionary entry. |
|`getPage()` | | str | returns page number of dictionary entry |
|`getOffset()` | | str | returns the offset of the dictionary entry |

Note: `getPage()` and `getOffset()` do not currently have any use.

**List of Active Dictionaries:**
```
["広辞苑",
"大辞林",
"大辞泉",
"ハイブリッド新辞林",
"学研古語辞典",
"NHK日本語発音アクセント辞典",
"日本国語大辞典",
"学研国語大辞典",
"明鏡国語辞典",
"新明解国語辞典",
"学研漢和大字典",
"中日大辞典",
"講談社日中辞典",
"小学館中日・日中辞典",
"牛津英汉双解词典",
"漢英字典",
"英辞郎",
"斎藤和英大辞典",
"ジーニアス英和和英辞典",
"研究社新英和中辞典",
"ジーニアス英和大辞典",
"研究社新編英和活用大辞典",
"研究社リーダーズ英和辞典",
"ロイヤル英文法",
"Collins Cobuild English Dictionary",
"三省堂類語辞典","角川類語新辞典",
"日本語大シソーラス類語検索大辞典",
"三省堂慣用句辞典","学研慣用句辞典",
"学研故事ことわざ辞典","日本大百科",
"マグローヒル科学技術用語大辞典",
"日外35万語科学技術用語大辞典",
"南山堂医学大辞典",
"日外25万語医学用語大辞典"
,"岩波理化学辞典",
"自由国民社法律用語辞典",
"心理学辞典"]
```
