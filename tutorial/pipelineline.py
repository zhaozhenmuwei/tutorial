# from scrapy.exceptions import DropItem
#
# class PricePipeline(object):
#
#     vat_factor = 1.15
#
#     def process_item(self, item, spider):
#         if item['price']:
#             if item['price_excludes_vat']:
#                 item['price'] = item['price'] * self.vat_factor
#             return item
#         else:
#             raise DropItem("Missing price in %s" % item)



# import json
#
# class JsonWriterPipeline(object):
#
#     def __init__(self):
#         self.file = open('items.jl', 'wb')
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         return item



# from scrapy.exceptions import DropItem
#
# class DuplicatesPipeline(object):
#
#     def __init__(self):
#         self.ids_seen = set()
#
#     def process_item(self, item, spider):
#         if item['id'] in self.ids_seen:
#             raise DropItem("Duplicate item found: %s" % item)
#         else:
#             self.ids_seen.add(item['id'])
#             return item
#     def open_spider(spider)
#     def close_spider(spider)
