# If your script has a name other than frequency.py, replace "frequency" on
# line 4 with the name of your script (without the .py).

import frequency as frq
import pytest

def test_get_pitch():
    # test (near) canonical pitches with A4=440
    assert frq.get_pitch(440.0) == "A"
    assert frq.get_pitch(932.33) == "A#"
    assert frq.get_pitch(61.74) == "B"
    assert frq.get_pitch(2093.0) == "C"
    assert frq.get_pitch(17.32) == "C#"
    assert frq.get_pitch(4978.03) == "D#"
    assert frq.get_pitch(1318.51) == "E"
    assert frq.get_pitch(174.61) == "F"
    assert frq.get_pitch(369.99) == "F#"
    assert frq.get_pitch(98.0) == "G"
    assert frq.get_pitch(3322.44) == "G#"
    
    # test some flat pitches
    assert frq.get_pitch(1920) == "B"
    assert frq.get_pitch(193) == "G"
    
    # test some sharp pitches
    assert frq.get_pitch(352) == "F"
    assert frq.get_pitch(18.7) == "D"
    
    # run some tests with other values of A4
    assert frq.get_pitch(407.75, 432) == "G#"
    assert frq.get_pitch(12, 48) == "A"
    
def test_get_octave():
    # test canonical pitches with A4=440
    assert frq.get_octave(440.0) == 4
    assert frq.get_octave(261.63) == 4
    assert frq.get_octave(16.35) == 0
    assert frq.get_octave(30.87) == 0
    assert frq.get_octave(2093) == 7
    
    # test some edge cases
    assert frq.get_octave(4065) == 7
    assert frq.get_octave(4068) == 8
    
    # test other values of A4
    assert frq.get_octave(32.11, 432) == 1
    assert frq.get_octave(30.31, 432) == 0
    assert frq.get_octave(200, 100) == 5

def test_check_intonation():
    assert frq.check_intonation(293.66) == 0
    assert frq.check_intonation(783.99) == 0
    assert frq.check_intonation(438.2245) == -7
    assert frq.check_intonation(1783.5382) == 23
    assert frq.check_intonation(266.3525) == 31
    assert frq.check_intonation(761.7748, 432) == -18

def test_who_can_hear():
    assert frq.who_can_hear(300) == "human"
    assert frq.who_can_hear(20) == "human"
    assert frq.who_can_hear(20_000) == "human"
    assert frq.who_can_hear(19.9) == "pigeon"
    assert frq.who_can_hear(0.5) == "pigeon"
    assert frq.who_can_hear(20_000.1) == "dog"
    assert frq.who_can_hear(44_000) == "dog"
    assert frq.who_can_hear(44_000.1) == "cat"
    assert frq.who_can_hear(77_000) == "cat"
    assert frq.who_can_hear(77_000.1) == "porpoise"
    assert frq.who_can_hear(150_000) == "porpoise"
    assert frq.who_can_hear(150_000.1) == "greater wax moth"
    assert frq.who_can_hear(300_000) == "greater wax moth"
    assert frq.who_can_hear(300_000.1) == None
    assert frq.who_can_hear(0.4) == None

def test_main(capsys):
    frq.main(440.0)
    captured = capsys.readouterr()
    assert captured.out == ("440.0 Hz is A4.\n"
                            "It is in tune if A4=440.0 Hz.\n"
                            "It is within the hearing range of a human.\n")
    frq.main(25600.0)
    captured = capsys.readouterr()
    assert captured.out == ("25600.0 Hz is G10.\n"
                            "It is 35 cents sharp if A4=440.0 Hz.\n"
                            "It is within the hearing range of a dog.\n")
    frq.main(0.17)
    captured = capsys.readouterr()
    assert captured.out == ("0.17 Hz is F-7.\n"
                            "It is 5 cents flat if A4=440.0 Hz.\n"
                            "I don't know of a species that can hear"
                            " this frequency.\n")
