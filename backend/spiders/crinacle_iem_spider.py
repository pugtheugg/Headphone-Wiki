import re
import scrapy
from pathlib import Path
from scrapy.exporters import JsonLinesItemExporter


class CrinacleIemSpider(scrapy.Spider):
    name = "iems"
    start_urls = [
        "https://crinacle.com/rankings/iems/",
    ]

    def parse(self, response):
        iems = response.css("tr")

        for iem in iems:
            # To retrieve all matches

            name = iem.css("td.column-3").getall()

            iem_name = []

            name = iem.css("td.column-3").getall()

            for n in name:
                matches = re.findall(r">([\w\d\s()-/]+)<", n)

                if matches:
                    iem_name.extend(matches)

            iem_name = ' '.join(iem_name).strip()

            iem_data = {
                "iem_name": iem_name,
                "rank": iem.css("td.column-1").re_first(r">([a-zA-Z][+-]?)<"),
                "value": iem.css("td.column-2::text").get(),
                "price": iem.css("td.column-4::text").get(),
                "sound_signature": iem.css("td.column-5::text").get(),
                "comments": iem.css("td.column-6::text").get(),
                "tone_grade": iem.css("td.column-7::text").get(),
                "technical_grade": iem.css("td.column-8::text").get(),
            }

            if iem_name:
                yield iem_data
