#-*- coding:utf-8 -*-

import re

commands = [{
        "id": 461,
        "my_id": 7,
        "nick_name": "玢玢",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM5lYZ5OBibeOtHq3H4FJoOMml4ZPY38iazicPu6GoDL3TyibA\/132",
        "content": "不要老提这种放大头像的事好不？一个专业的金融公司老说这些low不low?反正你这次互联网公司也做不成了，就别丢金融公司的脸了",
        "create_time": 1479999640,
        "content_id": "5935951206038896647",
        "like_id": 10011,
        "like_num": 240,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "看看头像怎么了....姑娘照片有看一看我不觉得low啊.....你看金融行业的妹子基本上不会有特别难看的，金融大概是最看脸的行业之一。",
                "uin": 2392015180,
                "create_time": 1479999882,
                "reply_id": 1,
                "to_uin": 1382071340,
                "reply_like_num": 958
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 335,
        "my_id": 150,
        "nick_name": "琥珀",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM57Q26zMO65DEia47OfrXIzjq0PO8oLibpvKSdr4QFFzgCw\/132",
        "content": "聊聊深港通。",
        "create_time": 1479999092,
        "content_id": "5328297944510627990",
        "like_id": 10008,
        "like_num": 105,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "应该是12月初，下周一的概率小。给你们说一个逗逼的事，富途港股开户想在我这里做广告，说好了挑深港通开通那天，他们几个星期前就以为深港通要开了，信心十足就提前支付了，结果拖了一星期又一星期，我先说好了，如果深港通不开我也不会退钱的。\/再见",
                "uin": 2392015180,
                "create_time": 1479999338,
                "reply_id": 1,
                "to_uin": 1240591040,
                "reply_like_num": 281
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 327,
        "my_id": 31,
        "nick_name": "AK前 行 ²⁰¹⁶",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/juI7hYgmtnqtjEqhib3Vv41Cyfeuw8iayB9icYyuhsJZ7U\/132",
        "content": "创业板会一直死下去吗？估计不会吧。",
        "create_time": 1479999076,
        "content_id": "4193530304591298591",
        "like_id": 0,
        "like_num": 93,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "创业板权重比较大的温氏股份、乐视网、网宿科技都是下降趋势，这样就很难玩的好。话说我也不明白为什么温氏股份一养猪场，市值这么大，怎么就去创业板上市，直接把整个指数都给污了。",
                "uin": 2392015180,
                "create_time": 1479999483,
                "reply_id": 1,
                "to_uin": 976382360,
                "reply_like_num": 206
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 112,
        "my_id": 1,
        "nick_name": "金天一",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/FcIe7cV2DMpiawZO2hPibQPSfbgXskTlvExnAbUXPwEJM\/132",
        "content": "网页打不开",
        "create_time": 1479998623,
        "content_id": "782768436919926785",
        "like_id": 10002,
        "like_num": 127,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "棒棒哒，我们小公司的网站还从来没有过那么多访客，已经被冲垮了....等明天看看找同事增加服务器，其实也就是现在一下子涌过去的人比较多，平时用网页看或者查资料的毕竟是少数人。",
                "uin": 2392015180,
                "create_time": 1479998756,
                "reply_id": 1,
                "to_uin": 182252479,
                "reply_like_num": 175
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 97,
        "my_id": 341,
        "nick_name": "面粉",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/hNWCQ9bibbzESft6ZJAJKyfpsPFMUBTvBBDsibP0eLrV2qY2zeVH0Xbw\/132",
        "content": "乳汁奶盒?不懂，虽然我知道这不是好事",
        "create_time": 1479998585,
        "content_id": "12600250619765195093",
        "like_id": 10003,
        "like_num": 112,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "如之奈何，同理还有师母已呆。",
                "uin": 2392015180,
                "create_time": 1479998841,
                "reply_id": 1,
                "to_uin": 2933724462,
                "reply_like_num": 170
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 82,
        "my_id": 20,
        "nick_name": "水心",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/LwRiasmDqqJ1ok574kqRDhkcCau4iaPamemPQX5DvzRgY\/132",
        "content": "网站挂了。。还没一睹到底多简陋",
        "create_time": 1479998559,
        "content_id": "11978556414361620",
        "like_id": 10004,
        "like_num": 165,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "我们毕竟是一家私募公司，不是互联网公司\/尴尬",
                "uin": 2392015180,
                "create_time": 1479998947,
                "reply_id": 1,
                "to_uin": 2788975,
                "reply_like_num": 149
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 379,
        "my_id": 90,
        "nick_name": "🦄楠妹儿。",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM5fOXOD5lOhaT6g0Cmng2qYXEbFOgcicdNmUoeB2bWO6bQ\/132",
        "content": "为了让股大大翻我，特意换了个头像~~~好想加入贵司为广大网友服务！！！看我看我~~~",
        "create_time": 1479999278,
        "content_id": "4347048417323647066",
        "like_id": 10012,
        "like_num": 141,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "你们看，还有主动让大家看照片的，这事我觉得挺好，正好当调剂了~",
                "uin": 2392015180,
                "create_time": 1480000196,
                "reply_id": 1,
                "to_uin": 1012126081,
                "reply_like_num": 158
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 63,
        "my_id": 20,
        "nick_name": "名•可🏀",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM6fXGMicxNlKXNs2Uibd4XJCIqGTky7g740vjPs8CkvyMnw\/132",
        "content": "今天看见的早。还没开始翻牌呢。长城电脑今天果然放巨量下跌，早盘只能眼睁睁看着，也卖不出去。哈哈。信息也不知道还得几天。一次成功的套利。感谢任小姐。今天没看内容先留言了。这就去看内容",
        "create_time": 1479998522,
        "content_id": "9107360387459710996",
        "like_id": 10001,
        "like_num": 127,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "要有正确的预期，这么巨量的套利是绝对不可能有15%的盈利的，最后有5-8%就不错了，我因为早就想透了，所以看它涨了跌了也没什么起伏。但我觉得当套利党退出后，长城电脑是很有机会到13+的。",
                "uin": 2392015180,
                "create_time": 1479998639,
                "reply_id": 1,
                "to_uin": 2120472581,
                "reply_like_num": 149
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 326,
        "my_id": 23,
        "nick_name": "火龙果",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/yYI4pIsF7XGhficI4WoI6GfibicStEAR2GhuFLdY2yHE6V7ulGAlveIzQ\/132",
        "content": "St这几天不好，是否跟最近网络热议注册制即将推出有关",
        "create_time": 1479999075,
        "content_id": "8071341935530344471",
        "like_id": 10010,
        "like_num": 60,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "注册制还早，排队的企业不少，ST之前太强了，合理调整正常，种马配种也得喘口气...",
                "uin": 2392015180,
                "create_time": 1479999556,
                "reply_id": 1,
                "to_uin": 1879255738,
                "reply_like_num": 143
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 553,
        "my_id": 7,
        "nick_name": "快乐（福康安)",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/PiajxSqBRaEKEMjNt679bMWxdNtzC8cNwWzqia0GwCmsczdI269YaxWQ\/132",
        "content": "种马都出来了，太有生活了\/呲牙\/呲牙。金融行业看脸，还是出乎我意料。一直以为靠脑",
        "create_time": 1480000097,
        "content_id": "2946963218553110535",
        "like_id": 10014,
        "like_num": 73,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "金融行业的本质是资本中介，其实和链家的中介工作性质是一样的，只不过服务的人群更高大上一些罢了。但凡服务业，脸就不会太难看，比如银行揽存款的妹子，如果长的太挫你根本没聊天的欲望。",
                "uin": 2392015180,
                "create_time": 1480000391,
                "reply_id": 1,
                "to_uin": 686143343,
                "reply_like_num": 137
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 536,
        "my_id": 1,
        "nick_name": "黄翔",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM5COauChvcE1gMN6z3p1l3QjrFspUUa1VfwQH6xT6jG8Q\/132",
        "content": "第一次留言：网站打不开……",
        "create_time": 1479999976,
        "content_id": "11537363372123095041",
        "like_id": 10015,
        "like_num": 70,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "明天一定会修好的，今晚只能暂时这样了。今不翻了，我得抓紧时间去处理一些客户的回复，大家早些休息吧，我最近累成狗了，就没2点之前睡过觉。私募装逼互联网公司的代价太惨重了....\/可怜",
                "uin": 2392015180,
                "create_time": 1480000524,
                "reply_id": 1,
                "to_uin": 2686251740,
                "reply_like_num": 136
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 79,
        "my_id": 1,
        "nick_name": "LiNG",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/FUAB7rj8u00xoatznibKiaxAy9TOqHXMfQib0w6dWKIhlQ\/132",
        "content": "我觉得今晚肯定很多人会问，董小姐一抬手全员加了1000月钱，格力一年增支8亿多，这公司是不是以后不准备当奶牛了",
        "create_time": 1479998557,
        "content_id": "373429303100047361",
        "like_id": 10005,
        "like_num": 91,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "其实董明珠一年拿8亿收买员工，对格力影响不是很大，要知道格力一年的利润将近200亿。这种阳光普照的加薪并不科学，因为对于月薪3000的人和月薪10000的人来说，加1000的意义不一样，总觉得是对之前股东大会挫折的一种回应",
                "uin": 2392015180,
                "create_time": 1479999040,
                "reply_id": 1,
                "to_uin": 86945785,
                "reply_like_num": 133
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 68,
        "my_id": 9,
        "nick_name": "大宝小宝妈",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM67lEH2LND9UQ2jbTGyBmbJqiaTqv8FkiarzFJbuOpCJbOw\/132",
        "content": "装修贷划算吗？买房了，准备攒钱装修，男人吵着要买车代步。纠结。",
        "create_time": 1479998541,
        "content_id": "7701175046638665737",
        "like_id": 10006,
        "like_num": 71,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "目前社会，利率低于7%的贷款都还可以，高于8%就一般，高于10%就是耍流氓。",
                "uin": 2392015180,
                "create_time": 1479999101,
                "reply_id": 1,
                "to_uin": 1793069543,
                "reply_like_num": 133
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 563,
        "my_id": 99,
        "nick_name": "肥杨",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/SCug0ESSOHicdtpq0Nibu7H1bsDUtkZukQw6TjHMibGzlyPV0TcX90bAg\/132",
        "content": "大大对浴盆和中小创失去信心了\/发呆\/冷汗\/惊讶\/睡",
        "create_time": 1480000152,
        "content_id": "8835158017507852387",
        "like_id": 10013,
        "like_num": 80,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "长期肯定还是中小创的趋势更明显，但短期你也不能和大势较劲，今年创业板这走的真特么.....一坨屎\/便便",
                "uin": 2392015180,
                "create_time": 1480000277,
                "reply_id": 1,
                "to_uin": 2057095528,
                "reply_like_num": 98
            }]
        },
        "is_from_me": 0
    },
    {
        "id": 340,
        "my_id": 23,
        "nick_name": "高宇",
        "logo_url": "http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM4d1pnF73ZjicvDNssxsMm9keTibGdSIAk2b0IIAbUia748Q\/132",
        "content": "我没收到短息捏",
        "create_time": 1479999112,
        "content_id": "5464749399101931543",
        "like_id": 10007,
        "like_num": 83,
        "like_status": 0,
        "is_from_friend": 0,
        "reply": {
            "reply_list": [{
                "content": "邮件收到了嘛？如果短信和邮件一个都没收到的话请直接联系我。现在的社会垃圾信息太多，彼此都防贼似得，短信群发的到达率有问题，邮件群发各种被盾，也是见鬼。",
                "uin": 2392015180,
                "create_time": 1479999195,
                "reply_id": 1,
                "to_uin": 1272361120,
                "reply_like_num": 95
            }]
        },
        "is_from_me": 0
    }]

count = 1


print ('<h2 style="color: #ff4c00;">精选留言:</h2>')
print ("<ul>")
for command in commands:
    reply_content = re.sub(r"\\","",command["reply"]["reply_list"][0]["content"])
    command_content = re.sub(r"\\","",command["content"])
    print "<li>" + str(count) + "\n<blockquote>" + command_content + "</blockquote>"
    print '<span style="color: #ff4c00;">回复：</span>'
    print reply_content +"</li>\n"
    count  += 1

print ("</ul>")