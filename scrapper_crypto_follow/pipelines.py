# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#postgress
from sqlalchemy.orm import sessionmaker
from models import DataPrices, db_connect


class ScrapperCryptoFollowPipeline:
    """pipeline para guardar datos"""
        
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        #create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        data_price = DataPrices(**item)

        try:
            session.add(data_price)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item