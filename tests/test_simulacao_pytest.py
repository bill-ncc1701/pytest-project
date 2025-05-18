import pytest

class TestSimulacao():

    @pytest.mark.simulacao
    @pytest.mark.skip
    def test_sumulacao_1(self):
        assert 1 == 1

    @pytest.mark.simulacao
    @pytest.mark.skip
    def test_sumulacao_2(self):
        assert 2 > 1


    @pytest.mark.teste2
    @pytest.mark.skip
    def test_sumulacao_3(self):
        assert 20 < 50