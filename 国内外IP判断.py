import geoip2.database

r1 = open('china.txt','a+')
r2 = open('foreign.txt','a+')


reader = geoip2.database.Reader('E:\Safe\脚本\Python脚本\Geoip\GeoLite2-Country.mmdb')  # mmdb文件路径

with open('url.txt','r') as f:
    for line in f.readlines():
        url = line.split(":")[0]
        print(url)
        c = reader.country(url)
        country = str(c.country.names)
        print(country)
        if "China" in country:
            r1.write(line)
        else:
            r2.write(line)








