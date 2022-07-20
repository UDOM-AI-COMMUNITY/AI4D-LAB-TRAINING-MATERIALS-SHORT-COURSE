from pytest import approx
import re
from unittest.mock import Mock

import aardvarks as aard


class BattleAardvark:
    """A mock Aardvark object used to test the battle() function."""
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def attack(self, other):
        other.hp -= 1


def test_battle_two_args():
    """Does battle() work with two arguments?"""
    a1 = BattleAardvark("A", 0)
    a2 = BattleAardvark("B", 0)
    aard.battle(a1, a2)

def test_battle_three_args():
    """Does battle() work with three arguments?"""
    a1 = BattleAardvark("A", 0)
    a2 = BattleAardvark("B", 0)
    aard.battle(a1, a2, 0)

def test_battle_draw_msg(capsys):
    """Does battle() print the correct message in case of a draw?"""
    a1 = BattleAardvark("A", 0)
    a2 = BattleAardvark("B", 0)
    aard.battle(a1, a2, 0)
    captured = capsys.readouterr()
    out = captured.out.strip()
    match = re.search(r"the battle ends in a draw", out.lower())
    assert match, f"expected: {'The battle ends in a draw!'} got: {out}"

def test_battle_skip_loop(capsys):
    """Does battle() skip attacks if both participants have zero HP?"""
    a1 = BattleAardvark("A", 0)
    a2 = BattleAardvark("B", 0)
    aard.battle(a1, a2, 0)
    captured = capsys.readouterr()
    out = captured.out.strip()
    match = re.search(r"^the battle ends in a draw", out.lower())
    assert "\n" not in out and match, \
        ("unexpected lines were printed when running a battle between two"
         " aardvarks with 0 health points each")

def test_battle_participant1_wins(capsys):
    """Does battle() produce the correct output if participant 1 wins?"""
    a1 = BattleAardvark("A", 1)
    a2 = BattleAardvark("B", 0)
    aard.battle(a1, a2, 0)
    captured = capsys.readouterr()
    out = captured.out.strip()
    assert "\n" not in out, \
        ("unexpected lines were printed when running a battle between an"
         " aardvark with 1 health point and another with 0 health points")
    match = re.search(r"^a\s+wins", out.lower())
    assert match, \
        ("unexpected message printed when first aardvark wins a battle:"
         f" {out}")

def test_battle_participant2_wins(capsys):
    """Does battle() produce the correct output if participant 2 wins?"""
    a1 = BattleAardvark("A", 0)
    a2 = BattleAardvark("B", 1)
    aard.battle(a1, a2, 0)
    captured = capsys.readouterr()
    out = captured.out.strip()
    assert "\n" not in out, \
        ("unexpected lines were printed when running a battle between an"
         " aardvark with 1 health point and another with 0 health points")
    match = re.search(r"^b\s+wins", out.lower())
    assert match, \
        ("unexpected message printed when second aardvark wins a battle:"
         f" {out}")

def test_battle_print_statements(capsys):
    """Does battle() produce the correct output during a battle?"""
    a1 = BattleAardvark("A", 3)
    a2 = BattleAardvark("B", 2)
    aard.battle(a1, a2, 0)
    captured = capsys.readouterr()
    out = captured.out.strip()
    out = re.sub(r"\n+", "\n", out)
    lines = out.splitlines()
    expr1 = r"^\s*a\s+has\s+(\d(?:\.\d+)?)\s+health points"
    expr2 = r"^\s*b\s+has\s+(\d(?:\.\d+)?)\s+health points"
    match1 = re.search(expr1, lines[0].lower())
    assert match1 and float(match1.group(1)) == approx(2), \
        (f"expected to see 'A has 2.0 health points.'; got '{lines[0]}'")
    match2 = re.search(expr2, lines[1].lower())
    assert match2 and float(match2.group(1)) == approx(1), \
        (f"expected to see 'B has 1.0 health points.'; got '{lines[1]}'")
    match1 = re.search(expr1, lines[2].lower())
    assert match1 and float(match1.group(1)) == approx(1), \
        (f"expected to see 'A has 1.0 health points.'; got '{lines[2]}'")
    match2 = re.search(expr2, lines[3].lower())
    assert match2 and float(match2.group(1)) == approx(0), \
        (f"expected to see 'B has 0.0 health points.'; got '{lines[3]}'")
    assert re.search(r"^\s*a\s+wins", lines[4].lower()), \
        (f"expected to see 'A wins!'; got '{lines[4]}'")

def test_battle_sleep(monkeypatch):
    """Does battle() use time.sleep() correctly?"""
    fake_sleep = Mock()
    monkeypatch.setattr(aard, "sleep", fake_sleep)
    a1 = BattleAardvark("A", 2)
    a2 = BattleAardvark("B", 2)
    aard.battle(a1, a2, 0.5)
    assert fake_sleep.called, "battle() did not call sleep()"
    assert fake_sleep.called_with(0.5), \
        "battle() did not pass the user-specified pause to sleep()"
    assert fake_sleep.call_count == 2, \
        "battle() did not call sleep() the correct number of times"


def test_battle_docstring_exists():
    """Does battle() have a docstring?"""
    docstr = aard.battle.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "battle() function has no docstring"

def test_battle_docstring_contents():
    """Does battle() docstring have the correct sections?"""
    docstr = aard.battle.__doc__
    assert "Args:" in docstr, \
        "battle() method docstring has no 'Args:' section"
    assert "Side effects:" in docstr, \
        "battle() method docstring has no 'Side effects:' section"