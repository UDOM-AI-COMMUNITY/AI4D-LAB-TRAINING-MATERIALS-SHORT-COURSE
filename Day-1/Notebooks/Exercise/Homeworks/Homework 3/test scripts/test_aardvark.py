from pytest import approx, fixture
import random
import re

import aardvarks as aard


RANDOM_SEED = 1


@fixture
def aardvark1():
    return aard.Aardvark("Vincent", "Purple", 200.0, 75.0)

@fixture
def aardvark2():
    return aard.Aardvark("Lenny", "Orange", 300.0, 66.0)

@fixture
def aardvark3():
    return aard.Aardvark("Gina", "Green", 180.0, 120.0)


@fixture
def pseudorandom_sequence():
    random.seed(RANDOM_SEED)
    sequence = []
    while sequence.count(0) < 2 or sequence.count(1) < 2:
        sequence.append(random.randint(0, 1))
    return sequence


class BattleAardvark:
        def __init__(self, name, hp):
            self.name = name
            self.hp = hp
        
        def attack(self, other):
            other.hp -= 1


def test_aardvark_name(aardvark1):
    """Is the Aardvark's name attribute assigned as expected?"""
    assert hasattr(aardvark1, "name"), "Aardvark has no 'name' attribute"
    assert aardvark1.name == "Vincent", \
        f"name attribute has unexpected value {aardvark1.name}"

def test_aardvark_clan(aardvark1):
    """Is the Aardvark's clan attribute assigned as expected?"""
    assert hasattr(aardvark1, "clan"), "Aardvark has no 'clan' attribute"
    assert aardvark1.clan == "Purple", \
        f"clan attribute has unexpected value {aardvark1.clan}"

def test_aardvark_hp(aardvark1):
    """Is the Aardvark's hp attribute assigned as expected?"""
    assert hasattr(aardvark1, "hp"), "Aardvark has no 'hp' attribute"
    assert aardvark1.hp == approx(200.0), \
        f"hp attribute has unexpected value {aardvark1.hp}"

def test_aardvark_power(aardvark1):
    """Is the Aardvark's power attribute assigned as expected?"""
    assert hasattr(aardvark1, "power"), "Aardvark has no 'power' attribute"
    assert aardvark1.power == approx(75.0), \
        f"power attribute has unexpected value {aardvark1.power}"


def test_advantage1(aardvark1, aardvark2, aardvark3):
    """Does advantage() correctly recognize an advantage?"""
    assert aardvark1.advantage(aardvark2) == approx(1.25)
    assert aardvark2.advantage(aardvark3) == approx(1.25)
    assert aardvark3.advantage(aardvark1) == approx(1.25)

def test_advantage2(aardvark1, aardvark2, aardvark3):
    """Does advantage() correctly recognize a disadvantage?"""
    assert aardvark2.advantage(aardvark1) == approx(0.8)
    assert aardvark3.advantage(aardvark2) == approx(0.8)
    assert aardvark1.advantage(aardvark3) == approx(0.8)

def test_advantage3(aardvark1, aardvark2, aardvark3):
    """Does advantage() correctly handle two aardvarks of the same clan?"""
    assert aardvark1.advantage(aardvark1) == approx(1.0)
    assert aardvark2.advantage(aardvark2) == approx(1.0)
    assert aardvark3.advantage(aardvark3) == approx(1.0)


def test_attack1(aardvark1, aardvark2, monkeypatch, pseudorandom_sequence):
    """Does attack() inflict damage correctly when there is no advantage?"""
    advantage = 1
    def mock_advantage(*args, **kwargs):
        return advantage
    monkeypatch.setattr(aardvark1, "advantage", mock_advantage)
    hp = aardvark2.hp
    damage = aardvark1.power * advantage
    random.seed(RANDOM_SEED)
    for value in pseudorandom_sequence:
        aardvark1.attack(aardvark2)
        if value == 0:
            msg = ("attack() method is inflicting damage when an attack fails,"
                   " OR attack() method is not generating random numbers as"
                   " expected")
            assert aardvark2.hp == hp, msg
        else:
            msg = ("attack() method is not inflicting the correct amount of"
                   " damage when there is no advantage, OR attack()"
                   " method is not generating random numbers as expected")
            assert aardvark2.hp == hp - damage, msg
            hp -= damage

def test_attack2(aardvark1, aardvark2, monkeypatch, pseudorandom_sequence):
    """Does attack() inflict damage correctly when aardvark has advantage?"""
    advantage = 1.25
    def mock_advantage(*args, **kwargs):
        return advantage
    monkeypatch.setattr(aardvark1, "advantage", mock_advantage)
    hp = aardvark2.hp
    damage = aardvark1.power * advantage
    random.seed(RANDOM_SEED)
    for value in pseudorandom_sequence:
        aardvark1.attack(aardvark2)
        if value == 0:
            msg = ("attack() method is inflicting damage when an attack fails,"
                   " OR attack() method is not generating random numbers as"
                   " expected")
            assert aardvark2.hp == hp, msg
        else:
            msg = ("attack() method is not inflicting the correct amount of"
                   " damage when aardvark has an advantage, OR attack()"
                   " method is not generating random numbers as expected")
            assert aardvark2.hp == hp - damage, msg
            hp -= damage

def test_attack3(aardvark1, aardvark2, monkeypatch, pseudorandom_sequence):
    """Does attack() inflict damage correctly when opponent has advantage?"""
    advantage = 0.8
    def mock_advantage(*args, **kwargs):
        return advantage
    monkeypatch.setattr(aardvark1, "advantage", mock_advantage)
    hp = aardvark2.hp
    damage = aardvark1.power * advantage
    random.seed(RANDOM_SEED)
    for value in pseudorandom_sequence:
        aardvark1.attack(aardvark2)
        if value == 0:
            msg = ("attack() method is inflicting damage when an attack fails,"
                   " OR attack() method is not generating random numbers as"
                   " expected")
            assert aardvark2.hp == hp, msg
        else:
            msg = ("attack() method is not inflicting the correct amount of"
                   " damage when opponent has an advantage, OR attack()"
                   " method is not generating random numbers as expected")
            assert aardvark2.hp == hp - damage, msg
            hp -= damage

def test_attack4(aardvark1, aardvark2, monkeypatch, pseudorandom_sequence,
                 capsys):
    """Are attack() print statements correct?"""
    advantage = 1.25
    def mock_advantage(*args, **kwargs):
        return advantage
    monkeypatch.setattr(aardvark1, "advantage", mock_advantage)
    hp = aardvark2.hp
    damage = aardvark1.power * advantage
    random.seed(RANDOM_SEED)
    for value in pseudorandom_sequence:
        aardvark1.attack(aardvark2)
        captured = capsys.readouterr()
        out = captured.out.rstrip()
        if value == 0:
            expr = r"^\s*Vincent\s+fails to do damage to\s+Lenny"
            msg = ("unexpected string printed by attack() when attack fails; "
                   f" expected 'Vincent fails to do damage to Lenny.'; got"
                   f" '{out}'")
            assert re.search(expr, out), msg
        else:
            expr = r"^\s*Vincent\s+does\s+(\d+(?:\.\d+)?)\s+damage to Lenny"
            match = re.search(expr, out)
            msg1 = ("unexpected string printed by attack() when attack"
                    f" succeeds; expected 'Vincent does {damage}"
                    f" damage to Lenny.'; got '{out}'")
            assert match, msg1
            msg2 = ("unexpected amount of damage reported by attack() when"
                    f" attack succeeds; expected {damage}; got"
                    f" {match.group(1)}")
            assert float(match.group(1)) == approx(damage), msg2
            hp -= damage


def test_aardvark_docstring_exists():
    """Does Aardvark class have a class docstring?"""
    docstr = aard.Aardvark.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "Aardvark class has no class docstring"

def test_aardvark_docstring_contents():
    """Does Aardvark class docstring have an Attributes: section?"""
    assert "Attributes:" in aard.Aardvark.__doc__, \
        "Aardvark class docstring has no 'Attributes:' section"

def test_advantage_docstring_exists():
    """Does advantage() have a docstring?"""
    docstr = aard.Aardvark.advantage.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "advantage() method has no docstring"

def test_advantage_docstring_contents():
    """Does advantage() docstring have the correct sections?"""
    docstr = aard.Aardvark.advantage.__doc__
    assert "Args:" in docstr, \
        "advantage() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "advantage() method docstring has no 'Returns:' section"

def test_attack_docstring_exists():
    """Does attack() have a docstring?"""
    docstr = aard.Aardvark.attack.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "attack() method has no docstring"

def test_attack_docstring_contents():
    """Does attack() docstring have the correct sections?"""
    docstr = aard.Aardvark.attack.__doc__
    assert "Args:" in docstr, \
        "attack() method docstring has no 'Args:' section"
    assert "Side effects:" in docstr, \
        "attack() method docstring has no 'Side effects:' section"
