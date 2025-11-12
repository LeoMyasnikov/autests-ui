import pytest
import random

# если тест нестабилен, то можно поставить марикровку flaky, указав в параметрах кол-во перезапусков и задержка между ними
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_reruns():
    assert random.choice([True, False])


PLATFORM = 'Linux'
@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == "Windows")  # Перезапуск при выполнении условия
def test_rerun_with_condition():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_rerun_1(self):
        ...
    def test_rerun_2(self):
        ...

