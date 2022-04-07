[[#YARA]]
[[#Flutter]]
[[#VirusTotal API]]
[[#Checklist]]

---
fadzilah.othman@utem.edu.my

#### YARA

- [My Repo](https://github.com/NovusIrez/Yara-APK-Demo)
- [YARA Docs](https://yara.readthedocs.io/en/latest/)
- [x]   [YarGen](https://github.com/Neo23x0/yarGen)
- [x] [Yet Another YARA Generator](https://github.com/jimmy-sonny/YaYaGen)
- [x] [Xen0ph0n YaraGenerator](https://github.com/Xen0ph0n/YaraGenerator)
- [YARA-CI](https://yara-ci.cloud.virustotal.com/)
- [x] [koodous.com find malware](https://blog.malwarebytes.com/security-world/technology/2017/09/explained-yara-rules/)
- [Awesome Yara (list of tools)](https://github.com/InQuest/awesome-yara)
- [x] [Koodous on YARA](https://docs.koodous.com/yara/getting-started/)
- https://github.com/Skotizo/VirusTotalBot
- [x] https://github.com/Koodous/androguard-yara
- [x] https://docs.koodous.com/
- https://github.com/Yara-Rules/yago
- https://github.com/VirusTotal/yara/issues/1145
- [Alternative to VirusTotal](https://www.maketecheasier.com/scan-apk-files-for-virus/)
- https://support.virustotal.com/hc/en-us/articles/360015658497-Crowdsourced-YARA-Rules

##### YarGen

> python3 yarGen.py --help

Extract UNICODE

> strings -el sample.exe > output

Extract ASCII

> strings -a sample.exe > output

**links**

- [Best Practice Rule Creation](https://github.com/Neo23x0/yarGen#best-practice) ^7f4108
- [CommandLine Parameter](https://github.com/Neo23x0/yarGen#best-practice)
- [Post-process Yara Rule](https://cyb3rops.medium.com/how-to-post-process-yara-rules-generated-by-yargen-121d29322282)
- [Examples](https://github.com/Neo23x0/yarGen#examples)
<br>

**Running YARA first time**

>echo "rule dummy { condition: true }" > my_first_rule
>yara my_first_rule my_first_rule

*YARA Location*

> /mnt/d/YARA/yara/yara

**Note**
- Storing YARA Rule on github

#### Flutter

- [Flutter doc](https://docs.flutter.dev/#new-to-flutter)
- [Expandable Floating action button](https://docs.flutter.dev/cookbook/effects/expandable-fab)
- [Scaffold class](https://api.flutter.dev/flutter/material/Scaffold-class.html)
- [File Picker](https://pub.dev/packages/file_picker)



**Note**
- RaisedButton
- upload icon
- Column
- [SizedBox](https://youtu.be/EHPu_DzRfqA)


Container

````dart
Container(
	 padding: EdgeInsets.all(30.0),
	 child: Text('click me'),
),
````

Row

````dart
 Row(
	 mainAxisAlignment: MainAxisAlignment.center,
	 children: <Widget>[
	 Text('hello, world'),
	 FlatButton(onPressed: (){},
	 child: Text('click me'),
	    ),
	  ],
	 ),
````

Empty space between

```dart
  Column(
  children:[
    MyButton(),
    SizedBox(height: 200),
    Otherbutton(),
    ],
  ),
```


```
mainAxisAlignment: MainAxisAlignment.
crossAxisAlignment: CrossAxisAlightment.
```


#### VirusTotal API

- [API](https://support.virustotal.com/hc/en-us/articles/115002100149-API)
- [API Scripts and client libraries](https://support.virustotal.com/hc/en-us/articles/360006819798)
- [VirusTotal Yara Doc](https://support.virustotal.com/hc/en-us/articles/115002178945-YARA)
- [API Upload File](https://developers.virustotal.com/reference/files-scan)
- [VT Hunting and Live Hunt](https://support.virustotal.com/hc/en-us/articles/360000363717-What-s-VT-Hunting-)

**Other method: Send APK and YARA to PC**


#### Koodous
- http://pavelsimecek.cz/custom-matching-of-koodous-yara-rules/
- 
#### Checklist

- **Yara**
- [x] how to use yarGen to scan apk (extract apk then scan files?)
- [x] what does Androguard-Yara dooo??
- [x] extract apk, use auto generate yara on dex file, use androguard-yara with yara
- [x] fix androguard fetch json report
- [ ] match apk file with community yara
- [ ] create yara from hybrid-analysis
- [ ] https://www.researchgate.net/publication/354701299_YARA-Signator_Automated_Generation_of_Code-based_YARA_Rules
- [x] [Write Yara Rule part 1](https://www.nextron-systems.com/2015/02/16/write-simple-sound-yara-rules/)
- [x] string.xml on yaragen
- [ ] read Koodous docs, try upload apk
- **Flutter**
- [ ] How to create new page
- [ ] how to create loading screen
- **Connection to PC**
- [ ] How to upload to PC
- [ ] how to run script on PC
- [ ] how to get result
- **Connection to VirusTotal**
- [ ] How to upload to API
- [ ] how to run scan
- [ ] how to get result


#### Issue

- APK file is an archive file, creating a YARA based on multiple parts in APK file "manifest , permissions, dex file" is not optimal/feaseable
- There is no Yara generator for dex file, analysts just write their own Yara for dex file
- Relying on Koodous API to convert APK into json report requires internet connection (the source code is not opensource)
- Koodous, biggest Yara static analysis site for apk has put a usage limits on analysis and subscription plans