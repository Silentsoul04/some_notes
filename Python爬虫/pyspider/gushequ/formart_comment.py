#-*- coding:utf-8 -*-

import re

rep = {"base_resp":{"ret":0,"errmsg":"ok"},"enabled":1,"is_fans":1,"nick_name":"招财龙猫","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q745gYawziaE195jF27DPub1A4L4jQq59DO3Wyypz5Lw\/132","my_comment":[],"elected_comment":[{"id":213,"my_id":40,"nick_name":"郑仲庭","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/eTBFF2uBxbAfs8UOeUI1eCLrXtDPH6Dibicj9gxHTXicricMeeJzCHicvoQ\/132","content":"你今天心情不好吗？很少见到这么没干货的夜报\/阴险\/阴险","create_time":1481208917,"content_id":"6884563113534816296","like_id":10003,"like_num":61,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"我今天出去参加活动，但为了晚上写夜报，8点钟不到，饭都没吃几口就匆匆忙忙赶回家。坐在电脑前复了好一会盘，确定没有亮点可写，那也只能这样了。态度是很认真的，奈何无米下炊。我也希望来个贾跃亭宣布出家，或者姚振华和许家印联手出柜之类的劲爆新闻。","uin":2392015180,"create_time":1481209183,"reply_id":1,"to_uin":1602937261,"reply_like_num":274}]},"is_from_me":0},{"id":49,"my_id":3,"nick_name":"Mr王","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM6fXtK3zyoCSjV9icaDQhbB1BibZvYogD188cL4RicdqiaOTg\/132","content":"你故意说的，救盘失败！明天如愿大阴棒\/呲牙","create_time":1481208682,"content_id":"9775375286869688323","like_id":10001,"like_num":95,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"我最近刚发了几个基金产品，还在审批阶段，没有建仓，你觉得我现在内心世界会真心盼着大盘好起来嘛。别怪我阴暗，人都是屁股决定脑袋的。\/阴险","uin":2392015180,"create_time":1481208784,"reply_id":1,"to_uin":2276006920,"reply_like_num":115}]},"is_from_me":0},{"id":195,"my_id":6,"nick_name":"тюрьмы кролик","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/iae4XYQUopMZUUeMPQcwSqFsrN3sl1OPY7gic7CZlDLkw\/132","content":"希望你能救世成功，还有股大提过的票票不管说了啥都会大涨\/偷笑昨晚的老神奇了\/偷笑","create_time":1481208892,"content_id":"2419670242536980486","like_id":10005,"like_num":36,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"我也很尴尬，我其实是想给大家警示温州帮凶残，劝大家远离投机炒作股，结果时机就是这么巧，今天突然集体大涨。这就好像妈妈教育孩子，不好好读书就和小区当门卫的张叔叔一样挣不到大钱，然后第二天张叔叔彩票中了500万。","uin":2392015180,"create_time":1481209433,"reply_id":1,"to_uin":563373380,"reply_like_num":98}]},"is_from_me":0},{"id":187,"my_id":19,"nick_name":"莱昂纳多张","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/PiajxSqBRaEIUXRxokTOdxsiajm93316Os7hjuPJVKPLhyw6dlicw6Wfw\/132","content":"现在好些领导都是屁股决定脑袋，为什么这种人也能做到“领导”，尤其是国企里，靠关系拉帮结派上来，然后就大肆胡来的人多了去了","create_time":1481208885,"content_id":"882693239063183379","like_id":10006,"like_num":27,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"我觉得领导想睡漂亮女下属，这是人之常情，可以理解，但潜规则之所以是潜规则，关键在于点到即止。稍微暗示一下，女下属如果拒绝就算了，这关小虎穷追不舍缠了两年多，最后以辞职相威胁，心里变态。","uin":2392015180,"create_time":1481209578,"reply_id":1,"to_uin":205518035,"reply_like_num":93}]},"is_from_me":0},{"id":210,"my_id":14,"nick_name":"杨旭然go","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM7mDhpZrXicdsxIgic2J1k3AN9Y2M35sMVVtET3WANrov4g\/132","content":"如果这次创业板下去了，这一年多横盘过程里得沉淀多少筹码，这平台可能真的几年内都回不去。想想都心酸","create_time":1481208914,"content_id":"11782396856997249038","like_id":10004,"like_num":79,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"你这句话说到我心里了，这次创业板在2050-2150这个区间横了10个月，如果最后的方向是向下，但就意味着创业板未来很长一段时间都没有牛市了。","uin":2392015180,"create_time":1481209257,"reply_id":1,"to_uin":2743303044,"reply_like_num":84}]},"is_from_me":0},{"id":514,"my_id":31,"nick_name":"芷郡","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/PiajxSqBRaEKZWX92rrEzumrFGmATypryptqJ5tqvutkF3OA9cuFHhA\/132","content":"请问社区君是如何暗示女下属？","create_time":1481209674,"content_id":"950639363987865631","like_id":10012,"like_num":63,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"我是民营企业，工作岗位的稀缺度怎么和民生银行相比？我欺负女下属人拍拍屁股就走了，那个烈女之所以能在性骚扰下坚持两年，说到底还是舍不得民生银行的工作，所以这种事也就只能发生在体制内，体制外自由度太高，潜规则是没有的。","uin":2392015180,"create_time":1481210275,"reply_id":1,"to_uin":221337975,"reply_like_num":25}]},"is_from_me":0},{"id":522,"my_id":6,"nick_name":"Vincent","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM4PYzzt9LZAD5FqJqWvmjwibzk8c0MdT5ULVG2wiavYbsmQ\/132","content":"好想知道烈女长什么样，值得民生银行的高管这么执着？","create_time":1481209716,"content_id":"11904253480140806","like_id":10009,"like_num":40,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"银行挑女职员也是有一条看不见的底线的，长太丑是进不去的，保底70分肯定有。","uin":2392015180,"create_time":1481210013,"reply_id":1,"to_uin":2771675,"reply_like_num":39}]},"is_from_me":0},{"id":171,"my_id":19,"nick_name":"Jason","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/G1wwQRibLukTNuURzeMWVO5B7q9kgEdzzcGQk2D8k0JE\/132","content":"给预测一下乐视网的停牌时间吧。","create_time":1481208865,"content_id":"3137617087405490195","like_id":10007,"like_num":29,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"短时间内肯定不愿意出来，本来创业板就风雨飘摇，正好借着这次停牌躲进去，肯定要等创业板回暖，或者乐视出个大利好再放出来，也给自己赢得一个喘息的时间。明年1月3日发布电动车很关键，如果搞砸了乐视网真要去深渊，我很乐意到时候去捡带血的筹码。","uin":2392015180,"create_time":1481209729,"reply_id":1,"to_uin":730533406,"reply_like_num":36}]},"is_from_me":0},{"id":515,"my_id":27,"nick_name":"秋色浪涛","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/nBcYE97sU45iaUX74n1Vh3ILLXicw9Y7JGZnecYVYvI7ic8WngiaPUMQfg\/132","content":"请问，死鱼的任期到啥时候","create_time":1481209684,"content_id":"9226870214702923803","like_id":10011,"like_num":25,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"周小川退休，尚福林接任，然后刘主席就可以去顶替银监会主席的位置，所以周小川退休那天就是刘主席升职挪窝的时候。","uin":2392015180,"create_time":1481210141,"reply_id":1,"to_uin":2148298131,"reply_like_num":30}]},"is_from_me":0},{"id":528,"my_id":1,"nick_name":"SleepingSnoopy","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM6ibO3kGROlyx05er4exW0qOHkPe7Qkm9Fe3F1lKFopC7w\/132","content":"步步高是002251，不要谢我，我是雷锋\/微笑","create_time":1481209729,"content_id":"6769657443988275201","like_id":10010,"like_num":23,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"无所谓的，因为我本来也没有推荐步步高的意思，只是强调一下这个是A股的公司，不是段永平那个步步高。","uin":2392015180,"create_time":1481209923,"reply_id":1,"to_uin":1576183700,"reply_like_num":26}]},"is_from_me":0},{"id":532,"my_id":35,"nick_name":"thomas👣","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM7NDTVfhsDcswSkXIib5QeINRrw2MLULaT6U6HWdUce4PQ\/132","content":"昨天说大盘的缺口大概率回补，但大盘连续几天缩量了，向上也难了，看来要见好就收了","create_time":1481209766,"content_id":"7323644659656294435","like_id":10008,"like_num":16,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"不是我嘴硬，我说回补缺口说的是主板，比如上证指数或者沪深300指数，没说创业板，因为创业板没缺口。以前大家根本不敢想象创业板下跌，主板上涨的情况发生，但最近几个月就是这样的。","uin":2392015180,"create_time":1481209871,"reply_id":1,"to_uin":1705168900,"reply_like_num":20}]},"is_from_me":0},{"id":590,"my_id":3,"nick_name":"毅","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/Q3auHgzwzM6tMVXq8gaMc1VPEiaCeyibmwARwZ0w86Libwt4ox1snvuqQ\/132","content":"一直只看不写，一看看上了瘾。很亲切的感觉，字里行间信息量很大，看的时间久了，谈资也有了，有米有？晚安","create_time":1481210132,"content_id":"5116047820452790275","like_id":10014,"like_num":12,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"股市无情人有情，9-10万人每天都来我这里消遣一小会，我自然也想好好写，有机会就带大家挣点钱，没机会也帮大家读读财经新闻，长长知识。今晚内容的确有点水，但也是精心拼凑的，就到这了，大家睡吧。\/再见","uin":2392015180,"create_time":1481210677,"reply_id":1,"to_uin":1191172707,"reply_like_num":15}]},"is_from_me":0},{"id":609,"my_id":19,"nick_name":"风香玉","logo_url":"http:\/\/wx.qlogo.cn\/mmhead\/tGoXwuibdlibiaDuy2nQ61KRk81Kcd7e260T1JFWzD2aYA\/132","content":"能说说阳光私募的阳光两个字的涵义嘛？另外，搜索网站可以把评论及回复也加上嘛，感觉那里面也有不少有用的信息。谢谢社区君。","create_time":1481210214,"content_id":"1479028510147215379","like_id":10013,"like_num":12,"like_status":0,"is_from_friend":0,"reply":{"reply_list":[{"content":"阳光主要是两层含义，1个是三方托管，就是钱存在券商或者银行那里，私募公司只负责交易，不能转账或者取现。2个是私募正式受政府监管，我们现在每个月都要给基金业协会提交报告，发产品都要他们审批，拿到备案号才能上车。","uin":2392015180,"create_time":1481210448,"reply_id":1,"to_uin":344363160,"reply_like_num":10}]},"is_from_me":0}],"friend_comment":[],"elected_comment_total_cnt":13}


commands = rep["elected_comment"]
count = 1

print ('<h2 style="color: #ff4c00;">精选留言:</h2>')
print ("<ul>")
for command in commands:
    try:
        reply_content = re.sub(r"\\","",command["reply"]["reply_list"][0]["content"])
    except IndexError as e:
        reply_content = ""
    command_content = re.sub(r"\\","",command["content"])
    print "<li>" + str(count) + ".\n<blockquote>" + command_content + "</blockquote>"
    print '<span style="color: #ff4c00;">回复：</span>'
    print reply_content +"</li>\n"
    count  += 1

print ("</ul>")