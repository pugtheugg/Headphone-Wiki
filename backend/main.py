from duckduckgo_search import DDGS
from scrapy.crawler import CrawlerProcess

from backend.spiders.crinacle_iem_spider import CrinacleIemSpider
from crinacleController import app
from databaseHandler import DatabaseHandler


def get_reddit_data(headphones):
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(f"{headphones} site:reddit.com", max_results=5)]
        print(results)


def get_crinicle_data():
    process = CrawlerProcess(settings={
        'FEEDS': {
            'iems.jsonl': {
                'format': 'jsonlines',
                'overwrite': True,
            },
        },
    })


if __name__ == '__main__':
    # process.crawl(CrinacleIemSpider)

    app.run(debug=True)

    # get_crinicle_data()

    with open('iems.jsonl', 'r') as json_file:
        json_list = list(json_file)

    iem_table = DatabaseHandler("iems")

    # iem_table.execute_query("""DROP TABLE IF EXISTS iem""")
    #
    # iem_table.execute_query(f"""
    # CREATE TABLE IF NOT EXISTS iem
    #   (
    #      name              TEXT PRIMARY KEY,
    #      rank              TEXT,
    #      value             TEXT,
    #      price             TEXT,
    #      signature         TEXT,
    #      comments          TEXT,
    #      tone_grade        TEXT,
    #      technical_grade   TEXT
    #   );  """)

    # for json_str in json_list:
    #     result = json.loads(json_str)
    #
    #     query = """
    #         INSERT INTO iem
    #         (
    #             name,
    #             rank,
    #             value,
    #             price,
    #             signature,
    #             comments,
    #             tone_grade,
    #             technical_grade
    #         )
    #         VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    #         """

    # values = [
    #     result["iem_name"],
    #     result["rank"],
    #     result["value"],
    #     result["price"],
    #     result["sound_signature"],
    #     result["comments"],
    #     result["tone_grade"],
    #     result["technical_grade"]]
    #
    # print(values)
    #
    # iem_table.execute_query(query, values)

    # get_reddit_data("Moondrop Blessing 2")
