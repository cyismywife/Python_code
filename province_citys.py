import re
import requests

all_city_province = {}

def getCity(num):
    global all_city_province
    province = ''
    city = ''
    url = 'http://www.maps7.com/china_province.php'
    page = requests.get(url)
    file = page.text
    if (num == 33):
        one = re.findall('<a name="33"(.*)</a>', file)
    else:
        one = re.findall('<a name="' + str(num) + '" href=.*?>(.*?)<a name="' + str(num + 1) + '" href=.*?>', file)
    for i in one:
        if (num == 0):
            province = re.findall('(.*?)</a></h4>', i)
        else:
            province = re.findall('<h4>(.*?)</h4>', i)
        city = re.findall('<a href="/china/dianziditu.*?>(.*?)</a>', i)
    for i in province:
        if (len(city) != 0):
            for j in city:
                # return i + ' ' + j
                all_city_province[j] = i
        else:
            # return i + ' ' + i
            all_city_province[i] = i

if __name__ == '__main__':
    num = 34
    all_city_province = {}
    for i in range(0, num):
        getCity(i)

    print(all_city_province)
    #     dd = getCity(i)
    #     city = dd.split(' ')[1]
    #     province = dd.split(' ')[0]
    #     all_city_province[city] = province
    # print(all_city_province)