# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from bot_stand.models import Models,db_connect,create_tables
from sqlalchemy.orm import sessionmaker
#from models import Models, db_connect,create_tables
class BotStandPipeline:
    def __init__(self):
        """ Initialize database connection and sessionmaker """
        engine = db_connect()
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)
    

    def process_item(self, item, spider):
        if isinstance(item, dict):
            pass
        else:
            session = self.Session()
            data = Models(item.get('content'),item.get('website_name'))
            try:
                session.add(data)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()

        return item

