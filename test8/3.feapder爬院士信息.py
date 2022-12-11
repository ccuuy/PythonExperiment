import feapder


class TophubSpider(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://www.cae.cn/cae/html/main/col48/column_48_1.html")

    def parse(self, request, response):
        lists = response.xpath("//li[@class='name_list']")
        for list in lists:
            name = list.xpath("./a/text()").extract_first()
            link = list.xpath("./a/@href").extract_first()
            yield feapder.Request(link, callback=self.parse_detail, name=name)

    def parse_detail(self, request, response):
        name = request.name
        content = response.xpath(
            'string(//div[@class="intro"])').extract_first()
        print(name)
        print(content)
        f = open('./contents/'+name+'.txt', 'w', encoding='utf-8')
        f.write(content)
        f.close


if __name__ == "__main__":
    TophubSpider().start()
