import json, os
D = "cards_json"
os.makedirs(D, exist_ok=True)

def w(slug, data):
    with open(f"{D}/{slug}.json","w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  {slug}.json")

# ── COLLOCATION CARDS ─────────────────────────────────────────────────────────

w("01_dian", {"char":"电","tone":4,"pinyin":"diàn","meaning":"electricity",
  "type":"collocation","satellites":[
    {"word":[["电",4],["话",4]],"pinyin":"diànhuà","english":"phone call","breakdown":"电 + 话 speech"},
    {"word":[["电",4],["脑",3]],"pinyin":"diànnǎo","english":"computer","breakdown":"电 + 脑 brain"},
    {"word":[["电",4],["视",4]],"pinyin":"diànshì","english":"television","breakdown":"电 + 视 vision"},
    {"word":[["电",4],["影",3]],"pinyin":"diànyǐng","english":"movie","breakdown":"电 + 影 shadow"},
    {"word":[["充",1],["电",4]],"pinyin":"chōngdiàn","english":"charge (battery)","breakdown":"充 fill + 电"},
    {"word":[["电",4],["梯",1]],"pinyin":"diàntī","english":"elevator","breakdown":"电 + 梯 ladder"},
    {"word":[["电",4],["池",2]],"pinyin":"diànchí","english":"battery","breakdown":"电 + 池 pool"},
    {"word":[["电",4],["费",4]],"pinyin":"diànfèi","english":"electricity bill","breakdown":"电 + 费 fee"},
]})

w("02_shang", {"char":"上","tone":4,"pinyin":"shàng","meaning":"up / on / start",
  "type":"collocation","satellites":[
    {"word":[["上",4],["班",1]],"pinyin":"shàngbān","english":"go to work","breakdown":"上 + 班 shift"},
    {"word":[["上",4],["网",3]],"pinyin":"shàngwǎng","english":"go online","breakdown":"上 + 网 net"},
    {"word":[["上",4],["海",3]],"pinyin":"Shànghǎi","english":"Shanghai","breakdown":"上 + 海 sea"},
    {"word":[["上",4],["午",3]],"pinyin":"shàngwǔ","english":"morning (a.m.)","breakdown":"上 + 午 noon"},
    {"word":[["上",4],["课",4]],"pinyin":"shàngkè","english":"attend class","breakdown":"上 + 课 lesson"},
    {"word":[["上",4],["车",1]],"pinyin":"shàngchē","english":"board a vehicle","breakdown":"上 + 车 vehicle"},
    {"word":[["上",4],["学",2]],"pinyin":"shàngxué","english":"go to school","breakdown":"上 + 学 study"},
    {"word":[["上",4],["楼",2]],"pinyin":"shànglóu","english":"go upstairs","breakdown":"上 + 楼 floor"},
]})

w("03_xia", {"char":"下","tone":4,"pinyin":"xià","meaning":"down / off / under",
  "type":"collocation","satellites":[
    {"word":[["下",4],["班",1]],"pinyin":"xiàbān","english":"finish work","breakdown":"下 + 班 shift"},
    {"word":[["下",4],["午",3]],"pinyin":"xiàwǔ","english":"afternoon","breakdown":"下 + 午 noon"},
    {"word":[["下",4],["雨",3]],"pinyin":"xiàyǔ","english":"rain","breakdown":"下 + 雨 rain"},
    {"word":[["下",4],["雪",3]],"pinyin":"xiàxuě","english":"snow","breakdown":"下 + 雪 snow"},
    {"word":[["下",4],["课",4]],"pinyin":"xiàkè","english":"finish class","breakdown":"下 + 课 lesson"},
    {"word":[["下",4],["楼",2]],"pinyin":"xiàlóu","english":"go downstairs","breakdown":"下 + 楼 floor"},
    {"word":[["下",4],["载",4]],"pinyin":"xiàzài","english":"download","breakdown":"下 + 载 load"},
    {"word":[["下",4],["周",1]],"pinyin":"xiàzhōu","english":"next week","breakdown":"下 + 周 week"},
]})

w("04_you", {"char":"游","tone":2,"pinyin":"yóu","meaning":"swim / travel / play",
  "type":"collocation","satellites":[
    {"word":[["游",2],["戏",4]],"pinyin":"yóuxì","english":"game","breakdown":"游 + 戏 play"},
    {"word":[["游",2],["泳",3]],"pinyin":"yóuyǒng","english":"swim","breakdown":"游 + 泳 swim"},
    {"word":[["旅",3],["游",2]],"pinyin":"lǚyóu","english":"travel","breakdown":"旅 travel + 游"},
    {"word":[["电",4],["脑",3],["游",2],["戏",4]],"pinyin":"diànnǎo yóuxì","english":"computer game","breakdown":"电脑 computer + 游戏"},
    {"word":[["手",3],["机",1],["游",2],["戏",4]],"pinyin":"shǒujī yóuxì","english":"mobile game","breakdown":"手机 phone + 游戏"},
    {"word":[["游",2],["客",4]],"pinyin":"yóukè","english":"tourist","breakdown":"游 + 客 guest"},
    {"word":[["导",3],["游",2]],"pinyin":"dǎoyóu","english":"tour guide","breakdown":"导 guide + 游"},
]})

w("05_hao", {"char":"好","tone":3,"pinyin":"hǎo","meaning":"good / well",
  "type":"collocation","satellites":[
    {"word":[["好",3],["吃",1]],"pinyin":"hǎochī","english":"delicious","breakdown":"好 + 吃 eat"},
    {"word":[["好",3],["喝",1]],"pinyin":"hǎohē","english":"tasty (drink)","breakdown":"好 + 喝 drink"},
    {"word":[["好",3],["主",3],["意",4]],"pinyin":"hǎo zhǔyi","english":"good idea","breakdown":"好 + 主意 idea"},
    {"word":[["好",3],["看",4]],"pinyin":"hǎokàn","english":"good-looking","breakdown":"好 + 看 look"},
    {"word":[["好",3],["笑",4]],"pinyin":"hǎoxiào","english":"funny","breakdown":"好 + 笑 laugh"},
    {"word":[["好",3],["听",1]],"pinyin":"hǎotīng","english":"nice to hear","breakdown":"好 + 听 listen"},
    {"word":[["好",3],["用",4]],"pinyin":"hǎoyòng","english":"handy / useful","breakdown":"好 + 用 use"},
    {"word":[["好",3],["久",3]],"pinyin":"hǎojiǔ","english":"long time (no see)","breakdown":"好 + 久 long time"},
]})

w("06_da", {"char":"打","tone":3,"pinyin":"dǎ","meaning":"hit / play / do",
  "type":"collocation","satellites":[
    {"word":[["打",3],["网",3],["球",2]],"pinyin":"dǎ wǎngqiú","english":"play tennis","breakdown":"打 + 网球 tennis"},
    {"word":[["打",3],["篮",2],["球",2]],"pinyin":"dǎ lánqiú","english":"play basketball","breakdown":"打 + 篮球 basketball"},
    {"word":[["打",3],["电",4],["话",4]],"pinyin":"dǎ diànhuà","english":"make a phone call","breakdown":"打 + 电话 phone call"},
    {"word":[["打",3],["工",1]],"pinyin":"dǎgōng","english":"work for pay","breakdown":"打 + 工 work"},
    {"word":[["打",3],["扫",3]],"pinyin":"dǎsǎo","english":"clean / sweep","breakdown":"打 + 扫 sweep"},
    {"word":[["打",3],["算",4]],"pinyin":"dǎsuàn","english":"plan / intend","breakdown":"打 + 算 calculate"},
    {"word":[["打",3],["折",2]],"pinyin":"dǎzhé","english":"discount","breakdown":"打 + 折 fold"},
    {"word":[["打",3],["主",3],["意",4]],"pinyin":"dǎ zhǔyi","english":"think of a plan","breakdown":"打 + 主意 idea"},
]})

w("07_chi", {"char":"吃","tone":1,"pinyin":"chī","meaning":"eat",
  "type":"collocation","satellites":[
    {"word":[["吃",1],["饭",4]],"pinyin":"chīfàn","english":"eat a meal","breakdown":"吃 + 饭 rice/meal"},
    {"word":[["吃",1],["面",4]],"pinyin":"chī miàn","english":"eat noodles","breakdown":"吃 + 面 noodles"},
    {"word":[["吃",1],["素",4]],"pinyin":"chīsù","english":"be vegetarian","breakdown":"吃 + 素 plain"},
    {"word":[["好",3],["吃",1]],"pinyin":"hǎochī","english":"delicious","breakdown":"好 good + 吃"},
    {"word":[["吃",1],["惊",1]],"pinyin":"chījīng","english":"be surprised","breakdown":"吃 + 惊 shock"},
    {"word":[["吃",1],["力",4]],"pinyin":"chīlì","english":"struggle / strenuous","breakdown":"吃 + 力 effort"},
    {"word":[["吃",1],["亏",1]],"pinyin":"chīkuī","english":"suffer a loss","breakdown":"吃 + 亏 loss"},
]})

w("08_xue", {"char":"学","tone":2,"pinyin":"xué","meaning":"study / learn",
  "type":"collocation","satellites":[
    {"word":[["学",2],["习",2]],"pinyin":"xuéxí","english":"study / practise","breakdown":"学 + 习 practise"},
    {"word":[["学",2],["校",4]],"pinyin":"xuéxiào","english":"school","breakdown":"学 + 校 school"},
    {"word":[["大",4],["学",2]],"pinyin":"dàxué","english":"university","breakdown":"大 big + 学"},
    {"word":[["学",2],["汉",4],["字",4]],"pinyin":"xué hànzì","english":"study Chinese characters","breakdown":"学 + 汉字"},
    {"word":[["学",2],["生",1]],"pinyin":"xuésheng","english":"student","breakdown":"学 + 生 born/live"},
    {"word":[["留",2],["学",2]],"pinyin":"liúxué","english":"study abroad","breakdown":"留 stay + 学"},
    {"word":[["同",2],["学",2]],"pinyin":"tóngxué","english":"classmate","breakdown":"同 same + 学"},
    {"word":[["开",1],["学",2]],"pinyin":"kāixué","english":"start of term","breakdown":"开 open + 学"},
]})

w("09_shou", {"char":"手","tone":3,"pinyin":"shǒu","meaning":"hand",
  "type":"collocation","satellites":[
    {"word":[["手",3],["机",1]],"pinyin":"shǒujī","english":"mobile phone","breakdown":"手 + 机 machine"},
    {"word":[["洗",3],["手",3]],"pinyin":"xǐshǒu","english":"wash hands","breakdown":"洗 wash + 手"},
    {"word":[["洗",3],["手",3],["间",1]],"pinyin":"xǐshǒujiān","english":"restroom","breakdown":"洗手 + 间 room"},
    {"word":[["手",3],["机",1],["游",2],["戏",4]],"pinyin":"shǒujī yóuxì","english":"mobile game","breakdown":"手机 + 游戏 game"},
    {"word":[["手",3],["表",3]],"pinyin":"shǒubiǎo","english":"wristwatch","breakdown":"手 + 表 surface/watch"},
    {"word":[["握",4],["手",3]],"pinyin":"wòshǒu","english":"handshake","breakdown":"握 grasp + 手"},
    {"word":[["歌",1],["手",3]],"pinyin":"gēshǒu","english":"singer","breakdown":"歌 song + 手"},
]})

w("10_zuo", {"char":"坐","tone":4,"pinyin":"zuò","meaning":"sit / travel by",
  "type":"collocation","satellites":[
    {"word":[["坐",4],["火",3],["车",1]],"pinyin":"zuò huǒchē","english":"take a train","breakdown":"坐 + 火车 train"},
    {"word":[["坐",4],["飞",1],["机",1]],"pinyin":"zuò fēijī","english":"take a plane","breakdown":"坐 + 飞机 plane"},
    {"word":[["坐",4],["地",4],["铁",3]],"pinyin":"zuò dìtiě","english":"take the subway","breakdown":"坐 + 地铁 subway"},
    {"word":[["请",3],["坐",4]],"pinyin":"qǐng zuò","english":"please sit down","breakdown":"请 please + 坐"},
    {"word":[["坐",4],["下",4]],"pinyin":"zuòxià","english":"sit down","breakdown":"坐 + 下 down"},
    {"word":[["坐",4],["位",4]],"pinyin":"zuòwèi","english":"seat","breakdown":"坐 + 位 position"},
]})

w("11_huo", {"char":"火","tone":3,"pinyin":"huǒ","meaning":"fire",
  "type":"collocation","satellites":[
    {"word":[["火",3],["车",1]],"pinyin":"huǒchē","english":"train","breakdown":"火 fire + 车 vehicle"},
    {"word":[["火",3],["车",1],["站",4]],"pinyin":"huǒchē zhàn","english":"train station","breakdown":"火车 + 站 station"},
    {"word":[["火",3],["车",1],["票",4]],"pinyin":"huǒchē piào","english":"train ticket","breakdown":"火车 + 票 ticket"},
    {"word":[["火",3],["锅",1]],"pinyin":"huǒguō","english":"hot pot","breakdown":"火 fire + 锅 pot"},
    {"word":[["火",3],["山",1]],"pinyin":"huǒshān","english":"volcano","breakdown":"火 + 山 mountain"},
    {"word":[["发",1],["火",3]],"pinyin":"fāhuǒ","english":"lose one's temper","breakdown":"发 emit + 火"},
]})

w("12_kai", {"char":"开","tone":1,"pinyin":"kāi","meaning":"open / start / drive",
  "type":"collocation","satellites":[
    {"word":[["开",1],["车",1]],"pinyin":"kāichē","english":"drive a car","breakdown":"开 + 车 vehicle"},
    {"word":[["开",1],["会",4]],"pinyin":"kāihuì","english":"have a meeting","breakdown":"开 + 会 meeting"},
    {"word":[["开",1],["心",1]],"pinyin":"kāixīn","english":"happy","breakdown":"开 + 心 heart"},
    {"word":[["开",1],["始",3]],"pinyin":"kāishǐ","english":"begin","breakdown":"开 + 始 begin"},
    {"word":[["开",1],["门",2]],"pinyin":"kāimén","english":"open the door","breakdown":"开 + 门 door"},
    {"word":[["开",1],["学",2]],"pinyin":"kāixué","english":"start of term","breakdown":"开 + 学 study"},
    {"word":[["开",1],["玩",2],["笑",4]],"pinyin":"kāi wánxiào","english":"joke / kidding","breakdown":"开 + 玩笑 joke"},
]})

w("13_kan", {"char":"看","tone":4,"pinyin":"kàn","meaning":"look / watch / read",
  "type":"collocation","satellites":[
    {"word":[["看",4],["电",4],["影",3]],"pinyin":"kàn diànyǐng","english":"watch a movie","breakdown":"看 + 电影 movie"},
    {"word":[["看",4],["电",4],["视",4]],"pinyin":"kàn diànshì","english":"watch TV","breakdown":"看 + 电视 TV"},
    {"word":[["看",4],["见",4]],"pinyin":"kànjiàn","english":"see / catch sight of","breakdown":"看 + 见 see"},
    {"word":[["看",4],["起",3],["来",2]],"pinyin":"kàn qǐlai","english":"it seems / looks like","breakdown":"看 + 起来"},
    {"word":[["好",3],["看",4]],"pinyin":"hǎokàn","english":"good-looking","breakdown":"好 good + 看"},
    {"word":[["看",4],["书",1]],"pinyin":"kànshū","english":"read a book","breakdown":"看 + 书 book"},
    {"word":[["看",4],["病",4]],"pinyin":"kànbìng","english":"see a doctor","breakdown":"看 + 病 illness"},
    {"word":[["看",4],["望",4]],"pinyin":"kànwàng","english":"visit someone","breakdown":"看 + 望 hope/visit"},
]})

w("14_he", {"char":"喝","tone":1,"pinyin":"hē","meaning":"drink",
  "type":"collocation","satellites":[
    {"word":[["喝",1],["茶",2]],"pinyin":"hē chá","english":"drink tea","breakdown":"喝 + 茶 tea"},
    {"word":[["喝",1],["酒",3]],"pinyin":"hējiǔ","english":"drink alcohol","breakdown":"喝 + 酒 alcohol"},
    {"word":[["喝",1],["牛",2],["奶",3]],"pinyin":"hē niúnǎi","english":"drink milk","breakdown":"喝 + 牛奶 milk"},
    {"word":[["好",3],["喝",1]],"pinyin":"hǎohē","english":"tasty (drink)","breakdown":"好 good + 喝"},
    {"word":[["喝",1],["水",3]],"pinyin":"hēshuǐ","english":"drink water","breakdown":"喝 + 水 water"},
    {"word":[["喝",1],["汤",1]],"pinyin":"hē tāng","english":"drink soup","breakdown":"喝 + 汤 soup"},
    {"word":[["喝",1],["醉",4]],"pinyin":"hēzuì","english":"get drunk","breakdown":"喝 + 醉 drunk"},
]})

w("15_lao", {"char":"老","tone":3,"pinyin":"lǎo","meaning":"old / very",
  "type":"collocation","satellites":[
    {"word":[["老",3],["师",1]],"pinyin":"lǎoshī","english":"teacher","breakdown":"老 + 师 master"},
    {"word":[["老",3],["板",3]],"pinyin":"lǎobǎn","english":"boss","breakdown":"老 + 板 board"},
    {"word":[["老",3],["公",1]],"pinyin":"lǎogōng","english":"husband","breakdown":"老 + 公 public"},
    {"word":[["老",3],["婆",2]],"pinyin":"lǎopo","english":"wife","breakdown":"老 + 婆 woman"},
    {"word":[["老",3],["家",1]],"pinyin":"lǎojiā","english":"hometown","breakdown":"老 + 家 home"},
    {"word":[["老",3],["外",4]],"pinyin":"lǎowài","english":"foreigner","breakdown":"老 + 外 outside"},
    {"word":[["老",3],["朋",2],["友",3]],"pinyin":"lǎo péngyou","english":"old friend","breakdown":"老 + 朋友 friend"},
]})

w("16_di", {"char":"地","tone":4,"pinyin":"dì","meaning":"ground / earth / place",
  "type":"collocation","satellites":[
    {"word":[["地",4],["方",1]],"pinyin":"dìfāng","english":"place","breakdown":"地 + 方 direction"},
    {"word":[["地",4],["址",3]],"pinyin":"dìzhǐ","english":"address","breakdown":"地 + 址 site"},
    {"word":[["地",4],["铁",3]],"pinyin":"dìtiě","english":"subway / metro","breakdown":"地 + 铁 iron"},
    {"word":[["地",4],["球",2]],"pinyin":"dìqiú","english":"the Earth","breakdown":"地 + 球 ball"},
    {"word":[["地",4],["图",2]],"pinyin":"dìtú","english":"map","breakdown":"地 + 图 picture"},
    {"word":[["本",3],["地",4]],"pinyin":"běndì","english":"local","breakdown":"本 root + 地"},
    {"word":[["地",4],["道",4]],"pinyin":"dìdào","english":"authentic / tunnel","breakdown":"地 + 道 road"},
]})

w("17_shuo", {"char":"说","tone":1,"pinyin":"shuō","meaning":"speak / say",
  "type":"collocation","satellites":[
    {"word":[["说",1],["话",4]],"pinyin":"shuōhuà","english":"speak / talk","breakdown":"说 + 话 speech"},
    {"word":[["说",1],["谎",3]],"pinyin":"shuōhuǎng","english":"tell a lie","breakdown":"说 + 谎 lie"},
    {"word":[["说",1],["得",2],["对",4]],"pinyin":"shuō de duì","english":"you're right","breakdown":"说 + 得对"},
    {"word":[["难",2],["说",1]],"pinyin":"nán shuō","english":"hard to say","breakdown":"难 hard + 说"},
    {"word":[["小",3],["说",1]],"pinyin":"xiǎoshuō","english":"novel / fiction","breakdown":"小 small + 说"},
    {"word":[["说",1],["不",4],["定",4]],"pinyin":"shuō bu dìng","english":"maybe / perhaps","breakdown":"说不定"},
    {"word":[["不",4],["用",4],["说",1]],"pinyin":"bù yòng shuō","english":"needless to say","breakdown":"不用 + 说"},
]})

w("18_hui", {"char":"回","tone":2,"pinyin":"huí","meaning":"return / go back",
  "type":"collocation","satellites":[
    {"word":[["回",2],["家",1]],"pinyin":"huíjiā","english":"go home","breakdown":"回 + 家 home"},
    {"word":[["回",2],["来",2]],"pinyin":"huílai","english":"come back","breakdown":"回 + 来 come"},
    {"word":[["送",4],["回",2],["家",1]],"pinyin":"sòng huí jiā","english":"see someone home","breakdown":"送 + 回 + 家"},
    {"word":[["回",2],["答",2]],"pinyin":"huídá","english":"answer / reply","breakdown":"回 + 答 answer"},
    {"word":[["回",2],["头",2]],"pinyin":"huítóu","english":"look back / later","breakdown":"回 + 头 head"},
    {"word":[["回",2],["国",2]],"pinyin":"huíguó","english":"return to home country","breakdown":"回 + 国 country"},
]})

w("19_chu", {"char":"出","tone":1,"pinyin":"chū","meaning":"go out / emerge",
  "type":"collocation","satellites":[
    {"word":[["出",1],["去",4]],"pinyin":"chūqù","english":"go out","breakdown":"出 + 去 go"},
    {"word":[["出",1],["租",1],["车",1]],"pinyin":"chūzūchē","english":"taxi","breakdown":"出 + 租车 rent car"},
    {"word":[["出",1],["门",2]],"pinyin":"chūmén","english":"leave the house","breakdown":"出 + 门 door"},
    {"word":[["出",1],["发",1]],"pinyin":"chūfā","english":"set off","breakdown":"出 + 发 send"},
    {"word":[["出",1],["国",2]],"pinyin":"chūguó","english":"go abroad","breakdown":"出 + 国 country"},
    {"word":[["出",1],["差",1]],"pinyin":"chūchāi","english":"business trip","breakdown":"出 + 差 errand"},
]})

w("20_mai", {"char":"买","tone":3,"pinyin":"mǎi","meaning":"buy",
  "type":"collocation","satellites":[
    {"word":[["买",3],["单",1]],"pinyin":"mǎidān","english":"pay the bill","breakdown":"买 + 单 bill"},
    {"word":[["买",3],["票",4]],"pinyin":"mǎi piào","english":"buy a ticket","breakdown":"买 + 票 ticket"},
    {"word":[["买",3],["东",1],["西",1]],"pinyin":"mǎi dōngxi","english":"go shopping","breakdown":"买 + 东西 things"},
    {"word":[["买",3],["蛋",4],["糕",1]],"pinyin":"mǎi dàngāo","english":"buy a cake","breakdown":"买 + 蛋糕 cake"},
    {"word":[["买",3],["菜",4]],"pinyin":"mǎicài","english":"buy groceries","breakdown":"买 + 菜 vegetable"},
    {"word":[["超",1],["市",4]],"pinyin":"chāoshì","english":"supermarket","breakdown":"超 super + 市 market"},
]})

# ── PHONETIC / RADICAL FAMILY CARDS ──────────────────────────────────────────

w("21_ri", {"char":"日","tone":4,"pinyin":"rì","meaning":"sun / day",
  "type":"phonetic","satellites":[
    {"word":[["今",1],["天",1]],"pinyin":"jīntiān","english":"today","breakdown":"今 now + 天 sky"},
    {"word":[["明",2],["天",1]],"pinyin":"míngtiān","english":"tomorrow","breakdown":"明 bright + 天"},
    {"word":[["昨",2],["天",1]],"pinyin":"zuótiān","english":"yesterday","breakdown":"昨 previous + 天"},
    {"word":[["早",3],["上",4]],"pinyin":"zǎoshang","english":"morning","breakdown":"早 early + 上"},
    {"word":[["星",1],["期",1]],"pinyin":"xīngqī","english":"week","breakdown":"星 star + 期 period"},
    {"word":[["时",2],["间",1]],"pinyin":"shíjiān","english":"time","breakdown":"时 time + 间 between"},
    {"word":[["每",3],["天",1]],"pinyin":"měitiān","english":"every day","breakdown":"每 every + 天"},
    {"word":[["晚",3],["上",4]],"pinyin":"wǎnshang","english":"evening","breakdown":"晚 late + 上"},
    {"word":[["晴",2],["天",1]],"pinyin":"qíngtiān","english":"sunny day","breakdown":"晴 clear + 天"},
    {"word":[["日",4],["记",4]],"pinyin":"rìjì","english":"diary","breakdown":"日 day + 记 record"},
    {"word":[["假",4],["日",4]],"pinyin":"jiàrì","english":"holiday","breakdown":"假 false/break + 日"},
]})

w("22_ma", {"char":"马","tone":3,"pinyin":"mǎ","meaning":"horse (phonetic seed)",
  "type":"phonetic","satellites":[
    {"word":[["马",3]],"pinyin":"mǎ","english":"horse","breakdown":"the original"},
    {"word":[["妈",1]],"pinyin":"mā","english":"mum","breakdown":"女 woman + 马"},
    {"word":[["吗",0]],"pinyin":"ma","english":"question particle","breakdown":"口 mouth + 马"},
    {"word":[["骂",4]],"pinyin":"mà","english":"scold","breakdown":"口口 + 马"},
    {"word":[["码",3]],"pinyin":"mǎ","english":"code / number","breakdown":"石 stone + 马"},
]})

w("23_dan", {"char":"旦","tone":4,"pinyin":"dàn","meaning":"dawn (phonetic seed)",
  "type":"phonetic","satellites":[
    {"word":[["但",4]],"pinyin":"dàn","english":"but / however","breakdown":"亻person + 旦"},
    {"word":[["担",1]],"pinyin":"dān","english":"carry / worry","breakdown":"扌hand + 旦"},
    {"word":[["胆",3]],"pinyin":"dǎn","english":"gallbladder / guts","breakdown":"月 flesh + 旦"},
    {"word":[["坦",3]],"pinyin":"tǎn","english":"flat / frank","breakdown":"土 earth + 旦"},
    {"word":[["元",2],["旦",4]],"pinyin":"Yuándàn","english":"New Year's Day","breakdown":"元 first + 旦 dawn"},
    {"word":[["坦",3],["克",4]],"pinyin":"tǎnkè","english":"tank (vehicle!)","breakdown":"坦 + 克 overcome"},
]})

w("24_water", {"char":"氵","tone":0,"pinyin":"sān diǎn shuǐ","meaning":"water radical",
  "type":"phonetic","satellites":[
    {"word":[["游",2],["泳",3]],"pinyin":"yóuyǒng","english":"swim","breakdown":"氵in 游 + 泳"},
    {"word":[["海",3]],"pinyin":"hǎi","english":"sea","breakdown":"氵+ 每"},
    {"word":[["法",3]],"pinyin":"fǎ","english":"law / method","breakdown":"氵+ 去"},
    {"word":[["冰",1]],"pinyin":"bīng","english":"ice","breakdown":"氵frozen form"},
    {"word":[["洗",3]],"pinyin":"xǐ","english":"wash","breakdown":"氵+ 先"},
    {"word":[["酒",3]],"pinyin":"jiǔ","english":"alcohol","breakdown":"氵+ 酉"},
    {"word":[["汤",1]],"pinyin":"tāng","english":"soup","breakdown":"氵+ 易"},
    {"word":[["河",2]],"pinyin":"hé","english":"river","breakdown":"氵+ 可"},
    {"word":[["浪",4]],"pinyin":"làng","english":"wave","breakdown":"氵+ 良"},
    {"word":[["流",2]],"pinyin":"liú","english":"flow","breakdown":"氵+ 㐬"},
]})

w("25_kou", {"char":"口","tone":3,"pinyin":"kǒu","meaning":"mouth radical",
  "type":"phonetic","satellites":[
    {"word":[["叫",4]],"pinyin":"jiào","english":"call / be named","breakdown":"口 + 丩"},
    {"word":[["吃",1]],"pinyin":"chī","english":"eat","breakdown":"口 + 乞"},
    {"word":[["喝",1]],"pinyin":"hē","english":"drink","breakdown":"口 + 曷"},
    {"word":[["唱",4]],"pinyin":"chàng","english":"sing","breakdown":"口 + 昌"},
    {"word":[["问",4]],"pinyin":"wèn","english":"ask","breakdown":"口 + 门"},
    {"word":[["吗",0]],"pinyin":"ma","english":"question particle","breakdown":"口 + 马"},
    {"word":[["口",3],["语",3]],"pinyin":"kǒuyǔ","english":"spoken language","breakdown":"口 + 语 language"},
    {"word":[["出",1],["口",3]],"pinyin":"chūkǒu","english":"exit / export","breakdown":"出 + 口"},
]})

w("26_person", {"char":"亻","tone":0,"pinyin":"rén páng","meaning":"person radical",
  "type":"phonetic","satellites":[
    {"word":[["你",3]],"pinyin":"nǐ","english":"you","breakdown":"亻+ 尔"},
    {"word":[["他",1]],"pinyin":"tā","english":"he / him","breakdown":"亻+ 也"},
    {"word":[["她",1]],"pinyin":"tā","english":"she / her","breakdown":"女 + 也"},
    {"word":[["但",4]],"pinyin":"dàn","english":"but","breakdown":"亻+ 旦"},
    {"word":[["休",1],["息",0]],"pinyin":"xiūxi","english":"rest","breakdown":"亻+ 木 tree"},
    {"word":[["借",4]],"pinyin":"jiè","english":"borrow / lend","breakdown":"亻+ 昔"},
    {"word":[["作",4]],"pinyin":"zuò","english":"work / make","breakdown":"亻+ 乍"},
]})

w("27_ping", {"char":"平","tone":2,"pinyin":"píng","meaning":"flat / peaceful",
  "type":"phonetic","satellites":[
    {"word":[["评",2]],"pinyin":"píng","english":"comment / review","breakdown":"讠speech + 平"},
    {"word":[["苹",2]],"pinyin":"píng","english":"apple (苹果)","breakdown":"艹grass + 平"},
    {"word":[["坪",2]],"pinyin":"píng","english":"level ground","breakdown":"土 earth + 平"},
    {"word":[["萍",2]],"pinyin":"píng","english":"duckweed","breakdown":"艹+ 苹 (⊃平)"},
    {"word":[["平",2],["时",2]],"pinyin":"píngshí","english":"usually / normally","breakdown":"平 + 时 time"},
]})

print("All 27 JSON files written.")
