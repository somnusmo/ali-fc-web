from .sign import Sign
class PostgresqlSign(Sign):
    def __init__(self, func, *args, **kw):
        ''' 获取配置中心数据。
            需要有一个application.py文件，该文件配置了配置中心的url,pwd。
            配置中心配置名为：conf_center，无默认值，必须配置。
            sql配置文件名为：sql_name，默认值为'postgresql'
        '''
        super().__init__(func, *args, **kw)
    
    def replace(self):
        from AliFCWeb.constant import getConfByName, FC_ENVIRON, CONF_CENTER_NAME, POSTGRE_SQL_CONF_FILE_NAME
        confCenter = getConfByName(CONF_CENTER_NAME)

        from AliFCWeb.fcutils import getConfigFromConfCenter
        res = getConfigFromConfCenter(confCenter['url'], POSTGRE_SQL_CONF_FILE_NAME, confCenter['pwd'] )
        if res.status_code != 200:
            raise Exception('读取配置中心失败！')
        data = json.loads(res.text)
        
        import psycopg2
        conn = psycopg2.connect(**data)
        return conn
