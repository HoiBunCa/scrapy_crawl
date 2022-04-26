
from scrapy.exceptions import DropItem


class CrawlDataPipeline:
    def __init__(self):
        _engine = create_engine("sqlite:///data.db")
        _connection = _engine.connect()
        _metadata = MetaData()
        _stack_items = Table("questions", _metadata,
                             Column("id", Integer, primary_key=True),
                             Column("url", Text),
                             Column("title", Text))
        _metadata.create_all(_engine)
        self.connection = _connection
        self.stack_items = _stack_items

    def process_item(self, item, spider):
        return item
