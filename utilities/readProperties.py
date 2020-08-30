import configparser
config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
class configure:
    @staticmethod
    def getUrl():
        baseUrl=config.get("common infor","baseUrl")
        return baseUrl
    @staticmethod
    def getCompany():
        company=config.get("common infor","company")
        return company
    @staticmethod
    def getUsername():
        userName=config.get("common infor","username")
        return userName

