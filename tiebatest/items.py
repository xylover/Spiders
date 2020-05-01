# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field,Item

class TiebaItem(Item):

    collection = 'tiezis'
    title = Field()
    writer = Field()
    time = Field()
    text = Field()
    replies = Field()
    replier = Field()