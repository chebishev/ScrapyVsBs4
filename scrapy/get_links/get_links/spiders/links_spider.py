import scrapy
import re


class LinksSpider(scrapy.Spider):
    name = 'links'
    start_urls = ['https://bdz.bg']

    def parse(self, response):
        found_links = response.css('a').getall()
        counter = 1

        for link in found_links:
            current_link = link.split('href="')[1].split('"')[0],
            current_link = current_link[0]
            if "http" not in current_link:
                continue
            found_name = ''
            for ch in link:
                if re.search('[а-яА-Я]', ch) or ch == ' ':
                    found_name += ch
            found_name = found_name.split()
            final_name = ''
            for word in found_name:
                if word:
                    final_name += word + ' '
            yield {
                'id': counter,
                'link': current_link,
                'name': final_name.strip(),
            }
            counter += 1