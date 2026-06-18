import pytest

@pytest.mark.skip(reason="фича в разработке")
def test_feature_in_development():
    ...


@pytest.mark.skip(reason="фича в разработке")
class TestSuitSkip:
    def test_feature_in_development_1(self):
        ...

    def test_feature_in_development_2(self):
        ...
