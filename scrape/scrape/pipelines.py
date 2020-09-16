# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapePipeline(object):

    # def __init__(self):
    #     pass

    # def create_connection(self):
    #     self.conn=sqlite3.connect("")

    def process_item(self, item, spider):
        return item
