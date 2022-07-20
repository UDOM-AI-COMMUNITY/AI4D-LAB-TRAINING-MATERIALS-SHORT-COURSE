from pytest import approx, raises as pytest_raises
import random

import aardvarks as aard


class BattleAardvark:
        def __init__(self, name, hp):
            self.name = name
            self.hp = hp
        
        def attack(self, other):
            other.hp -= 1


def test_catalog(tmp_path):
    """Does Catalog.__init__() read the specified file and build the right dict?"""
    # set up temp file
    p = tmp_path / "test_file.csv"
    random.seed()
    names = ["Helga", "Orson", "Ervin", "Dotty", "Gunther", "Eunice"]
    random.shuffle(names)
    clans = ["Orange", "Green", "Purple"]
    values = [(names.pop(), random.choice(clans),
               random.random()*800+200, random.random()*150+50)
              for i in range(2)]
    contents = [",".join(str(v) for v in t) for t in values]
    p.write_text("\n".join(contents)+"\n", encoding="utf-8")
    
    # run tests
    cat = aard.Catalog(str(p))
    assert hasattr(cat, "catalog"), "Catalog has no 'catalog' attribute"
    assert len(cat.catalog) == 2, \
        "Catalog.catalog has unexpected number of entries"
    assert set(cat.catalog) == set(v[0] for v in values), \
        f"keys in Catalog.catalog do not reflect the contents of the input file"
    name = values[1][0]
    assert isinstance(cat.catalog[name], tuple), \
        "values in Catalog.catalog should be tuples"
    assert isinstance(cat.catalog[name][1], float), \
        "health points stat should be stored in cat.catalog as a float"
    assert isinstance(cat.catalog[name][2], float), \
        "power stat should be stored in cat.catalog as a float"
    assert cat.catalog[name][0] == values[1][1], \
        "unexpected value for clan of aardvark in cat.catalog"
    assert cat.catalog[name][1] == approx(values[1][2]), \
        "unexpected value for health points stat of aardvark in cat.catalog"
    assert cat.catalog[name][2] == approx(values[1][3]), \
        "unexpected value for power stat of aardvark in cat.catalog"


def test_get_aardvark_unittest(monkeypatch):
    """Does get_aardvark() return an Aardvark object? (this test should work even if Aardvark is not defined)"""
    class FakeAardvark:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            
    def fake_init(self, filename):
        self.catalog = {"Betsy": ("Green", 850.0, 45.0)}
        
    monkeypatch.setattr(aard, "Aardvark", FakeAardvark)
    monkeypatch.setattr(aard.Catalog, "__init__", fake_init) 
    cat = aard.Catalog("fake_file.csv")
    aardvark = cat.get_aardvark("Betsy")
    assert len(aardvark.args) + len(aardvark.kwargs) == 4, \
        "Aardvark was instantiated with the wrong number of arguments"

def test_get_aardvark_error(monkeypatch):
    """Does get_aardvark() raise a KeyError? (this test should work even if Aardvark is not defined)"""
    class FakeAardvark:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            
    def fake_init(self, filename):
        self.catalog = {"Betsy": ("Green", 850.0, 45.0)}
        
    monkeypatch.setattr(aard, "Aardvark", FakeAardvark)
    monkeypatch.setattr(aard.Catalog, "__init__", fake_init)
    cat = aard.Catalog("fake_file.csv")
    with pytest_raises(KeyError):
        aardvark = cat.get_aardvark("Jurgen")

def test_get_aardvark_integrationtest(monkeypatch):
    """Does get_aardvark() return an Aardvark object? (this test requires Aardvark to be defined)"""
    def fake_init(self, filename):
        self.catalog = {"Betsy": ("Green", 850.0, 45.0)}
        
    monkeypatch.setattr(aard.Catalog, "__init__", fake_init)
    cat = aard.Catalog("fake_file.csv")
    a = cat.get_aardvark("Betsy")
    assert a.name == "Betsy", \
        ("Aardvark created by get_aardvark() has unexpected value for name"
         " attribute")
    assert a.clan == "Green", \
        ("Aardvark created by get_aardvark() has unexpected value for clan"
         " attribute")
    assert a.hp == approx(850.0), \
        ("Aardvark created by get_aardvark() has unexpected value for health"
         " points attribute")
    assert a.power == approx(45.0), \
        ("Aardvark created by get_aardvark() has unexpected value for power"
         " attribute")


def test_catalog_docstring_exists():
    """Does Catalog class have a class docstring?"""
    docstr = aard.Catalog.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "Catalog class has no class docstring"

def test_catalog_docstring_contents():
    """Does Catalog class docstring have an Attributes: section?"""
    assert "Attributes:" in aard.Catalog.__doc__, \
        "Catalog class docstring has no 'Attributes:' section"

def test_get_aardvark_docstring_exists():
    """Does get_aardvark() have a docstring?"""
    docstr = aard.Catalog.get_aardvark.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "get_aardvark() method has no docstring"

def test_get_aardvark_docstring_contents():
    """Does get_aardvark() docstring have the correct sections?"""
    docstr = aard.Catalog.get_aardvark.__doc__
    assert "Args:" in docstr, \
        "get_aardvark() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "get_aardvark() method docstring has no 'Returns:' section"
    assert "Raises:" in docstr, \
        "get_aardvark() method docstring has no 'Raises:' section"
