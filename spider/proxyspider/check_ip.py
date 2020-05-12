# -*- coding:utf-8 -*-
import requests,datetime,random,threading
# 爬取的ip存放在本地文档中 H:\codes\graduateProject\data\source\init_ip_proxies.txt
#多线程验证其可用性，结果输出到ip_proxies.txt

def dispatch(targetUrl,ip_list):
    for i in range(len(ip_list)):
        print("checking ip:" + ip_list[i])
        ip = ip_list[i].split(":")
        if check_ip(targetUrl,ip[0],ip[1]):
            f_out.write(ip[0]+":"+ip[1])


# 验证ip
def check_ip(targetUrl,ip,port):
    headers = getHeaders()
    proxies = {"http":"http://"+ip+":"+port,
               "https":"https://"+ip+":"+port
               }
    try:
        code = requests.get(url=targetUrl,proxies=proxies,headers=headers,timeout=5).status_code
        if code == 200:
            print("valid ip:"+ip+":"+port)
            return True
        else:
            return False
    except:
        return False
# 获取请求头
def getHeaders():
    user_agent_list = [ \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    UserAgent = random.choice(user_agent_list)
    headers = {'User-Agent':UserAgent}
    return headers
# 获取时间差
def gettimediff(startTime,endTime):
    seconds = (endTime-startTime).seconds
    m,s = divmod(seconds,60)
    h,m = divmod(m,60)
    diff = ('%02d:%02d:%02d' % (h,m,s))
    return diff

if __name__ == '__main__':
    path = "H:/codes/graduateProject/data/source/proxy/"
    targetUrl = "https://bj.lianjia.com/"
    # f_in = open(path+"init_ip_proxies_backup.txt",'r') 
    # ip_proxies不可用时的备用
    f_in = open(path+"init_ip_proxies.txt",'r')
    f_out = open(path+"ip_proxies.txt",'w')
    ip_list = f_in.readlines()
    num = len(ip_list)
    startTime = datetime.datetime.now()
    threads = []
    step = len(ip_list)//18
    # step = 32
    for i in range(18):
        t = threading.Thread(target=dispatch,args=(targetUrl,ip_list[i*step:(i+1)*step]))
        threads.append(t)
    print("开始验证,共有%d个待验证ip" % num)
    # 开启线程
    for s in threads:
        s.start()
    #     等待线程执行结束
    for e in threads:
        e.join()
    print("验证结束")
    endTime = datetime.datetime.now()
    diff = gettimediff(startTime,endTime)
    f_in.close()
    f_out.flush()
    f_out.close()
    f_out = open(path+"ip_proxies.txt",'r')
    valid_ip = len(f_out.readlines())
    print('一共耗时：%s 一共验证可用代理ip: %s' % (diff,valid_ip))
