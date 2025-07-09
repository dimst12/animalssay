from animalssay import cat_says

def test_cat_says():
    output = cat_says("Hello!")
    assert "Hello!" in output
    assert "/\\_/\\ " in output
