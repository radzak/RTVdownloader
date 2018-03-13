from rtv.extractor.rmf24 import Rmf24

from ..test_extractors import ExtractorTester


class TestRmf24Extractor(ExtractorTester):
    extractor_class = Rmf24
    urls = [
        'http://www.rmf24.pl/tylko-w-rmf24/rozmowa/news-abp-gadecki-o-rozancu-do-granic-przygotowane-nie-przez-ksiez,nId,2449655'
    ]
