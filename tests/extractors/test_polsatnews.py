from rtv.extractors.polsatnews import PolsatNews

from ..test_extractors import ExtractorTester


class TestPolsatNewsExtractor(ExtractorTester):
    extractor_class = PolsatNews
    urls = [
        'http://www.polsatnews.pl/wideo/nie-zyje-chlopiec-pod-ktorym-zalamal-sie-lod-w-opolskiem_6550622/?ref=wideo_top_kraj',
        'http://www.polsatnews.pl/wideo-program/prezydenci-i-premierzy-prawo-i-sprawiedliwosc-rusza-w-polske_6710058/'
    ]
