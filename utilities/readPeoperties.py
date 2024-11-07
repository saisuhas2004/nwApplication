import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getAppSpotURL():
        url = config.get('common info', 'appspotURL')
        return url


    @staticmethod
    def getUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info', 'password')
        return password

    @staticmethod
    def getKayakURL():
        url = config.get('common info', 'kayakURL')
        return url

