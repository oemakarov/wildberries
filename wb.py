import requests
from .model import CardRequestModel

# https://card.wb.ru/cards/detail?nm=117647686;117647687;117647690;117647685;117647689;117647688


class WB():
    """docstring for WB."""

    CARDS_DETAIL = 'https://card.wb.ru/cards/detail?curr=rub&nm=' 

    def __init__(self):
        pass
    

    def get_products_data(self, ids: list[int]):
        return self.get_full_products_response_data(ids).data.products
        

    def get_full_products_response_data(self, ids: list[int]):
        resp = requests.get(self._compose_url(ids))
        return CardRequestModel.parse_raw(resp.text)
        
    
    def _compose_url(self, ids: list[int]):
        return self.CARDS_DETAIL + ';'.join([str(i) for i in ids])
    


# https://wbx-content-v2.wbstatic.net/ru/117647687.json
# https://wbx-content-v2.wbstatic.net/price-history/117647687.json

# URLS: {
#     MAIN_MENU: 'https://www.wildberries.ru/webapi/menu/main-menu-ru-ru.json',
#     PROMOS: 'https://www.wildberries.ru/webapi/settings/promo/get',
#     PRODUCT: {
#       CONTENT: 'https://wbx-content-v2.wbstatic.net/ru/{}.json',
#       CARD: 'https://basket-{0}.wb.ru/vol{1}/part{2}/{3}/info/ru/card.json',
#       SELLERS: 'https://basket-{0}.wb.ru/vol{1}/part{2}/{3}/info/sellers.json',
#       EXTRADATA: 'https://www.wildberries.ru/webapi/product/{}/data',
#       DETAILS: 'https://card.wb.ru/cards/detail',
#       FEEDBACKS:
#         'https://public-feedbacks.wildberries.ru/api/v1/feedbacks/site',
#       QUESTIONS: 'https://questions.wildberries.ru/api/v1/questions',
#       DELIVERYDATA: 'https://card.wb.ru/cards/list',
#     },
#     SEARCH: {
#       SIMILAR_BY_NM: 'https://in-similar.wildberries.ru/',
#       TOTALPRODUCTS: 'https://search.wb.ru/exactmatch/ru/common/v4/search',
#       EXACTMATCH: 'https://search.wb.ru/exactmatch/ru/common/v4/search',
#       CATALOG: 'https://wbxcatalog-ru.wildberries.ru/{}/catalog',
#       ADS: 'https://catalog-ads.wildberries.ru/api/v5/search',
#       CAROUSEL_ADS: 'https://carousel-ads.wildberries.ru/api/v4/carousel',
#       HINT: 'https://search.wb.ru/suggests/api/v2/hint',
#       LIST: 'https://card.wb.ru/cards/list',
#     },
#     IMAGES: {
#       TINY: 'https://basket-{0}.wb.ru/vol{1}/part{2}/{3}/images/tm/{4}.jpg', // 900x1200
#       BIG: 'https://basket-{0}.wb.ru/vol{1}/part{2}/{3}/images/big/{4}.jpg', // 900x1200
#       SMALL: 'https://basket-{0}.wb.ru/vol{1}/part{2}/{3}/images/c246x328/{4}.jpg', // 900x1200
#       MEDIUM: 'https://basket-{0}.wb.ru/vol{1}/part{2}/{3}/images/c516x688/{4}.jpg', // 900x1200
#       FEEDBACK_BASE: 'https://feedbackphotos.wbstatic.net/',
#     },
#   },