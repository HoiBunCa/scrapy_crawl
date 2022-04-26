import psycopg2


class CrawlDataPipeline:
    """Tweets pipeline for storing scraped items in the database"""

    # Define function to configure the connection to the database & connect to it
    def open_spider(self, spider):
        hostname = '172.16.30.245'
        port = 5435
        username = 'credit_score'
        password = 'upoo1huumahZuigh'
        database = 'credit_score'

        self.connection = psycopg2.connect(host=hostname, user=username, password=password,
                                           dbname=database, port=port)
        self.cur = self.connection.cursor()

    # Define function to disconnect from database
    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    # Define function to process each scraped item and insert it into    PostgreSQL table
    def process_item(self, item, spider):
        try:
            # Execute SQL command on database to insert data in table
            self.cur.execute(
                "insert into nhac_chuong_data(link_download, song_name, singer_name, num_download, category, size, lyric, link_source, source_craw, num_listens) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (item['link_download'], item['song_name'], item['singer_name'], item['num_download'], item['category'],
                 item['size'], item['lyric'], item['link_source'], item['source_craw'], item['num_listens']))
            self.connection.commit()
        except:
            self.connection.rollback()
            raise
        return item