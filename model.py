
from pydantic import BaseModel, Field, validator


class ProductExtendedModel(BaseModel):
    basic_sale: int = Field(default=None, alias="basicSale")
    basic_price_u: int = Field(default=None, alias="basicPriceU")


class ProductSizesModel(BaseModel):
    name: str
    origName : str = Field(default=None, alias="origName")
    rank: int
    option_id : int = Field(default=None, alias="optionId")
    stocks: list


class ProductModel(BaseModel):
    id: int
    root: int
    kind_id : int = Field(default=None, alias="kindId")
    subject_id : int = Field(default=None, alias="subjectId")
    subject_parent_id : int = Field(default=None, alias="subjectParentId")
    name: str
    brand: str
    brand_id : int = Field(default=None, alias="brandId")
    site_brand_id : int = Field(default=None, alias="siteBrandId")
    price_u : int = Field(default=None, alias="priceU")
    sale_price_u : int = Field(default=None, alias="salePriceU")
    logistics_cost : int = Field(default=None, alias="logisticsCost")
    sale: int
    extended: ProductExtendedModel
    sale_conditions : int = Field(default=None, alias="saleConditions")
    pics: int
    rating: int
    review_rating : float = Field(default=None, alias="reviewRating")
    feedbacks: int
    volume: int
    colors: list
    promotions: list
    diff_price : bool = Field(default=None, alias="diffPrice")
    sizes: list[ProductSizesModel]

    @property
    def price(self) -> float:
        return self.sale_price_u / 100


class ProductParamsModel(BaseModel):
    version: int
    curr: str


class ProductsListModel(BaseModel):
    products: list[ProductModel]


class CardRequestModel(BaseModel):
    state: int
    params: ProductParamsModel
    data: ProductsListModel



