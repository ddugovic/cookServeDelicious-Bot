from recipe_renamer import renamer


def test_renamer():
    assert "Hot Dog Ketchup" == renamer("Hot Dog (Ketchup)")
