from add import calc_add
def test_positive_no():
    assert calc_add(20,40)==60
def test__zero___no():
    assert calc_add(0,50)==50
def test_negative_no():
    assert calc_add(-50,10)==-40