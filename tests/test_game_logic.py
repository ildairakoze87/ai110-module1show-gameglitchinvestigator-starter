from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_get_range_for_difficulty():
    # The hard difficulty range should be 1 to 50, not 1 to 100
    assert get_range_for_difficulty("Hard") == (1, 50)
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_parse_guess_empty_input():
    # Empty input should return an error and not treat it as zero
    ok, guess_int, err = parse_guess("")
    assert ok is False
    assert guess_int is None
    assert err == "Enter a guess."


def test_parse_guess_decimal_input():
    # Decimal input should convert to an integer and succeed
    ok, guess_int, err = parse_guess("42.0")
    assert ok is True
    assert guess_int == 42
    assert err is None


def test_parse_guess_non_numeric_input():
    # Non-numeric input should return a parse error instead of crashing or accepting it
    ok, guess_int, err = parse_guess("abc")
    assert ok is False
    assert guess_int is None
    assert err == "That is not a number."


def test_update_score_win_reward():
    # Win on first attempt (attempt 0) should give 90 points (100 - 10*1)
    score = update_score(0, "Win", attempt_number=0)
    assert score == 90
    
    # Win after multiple attempts should decrease reward but stay above minimum
    score = update_score(0, "Win", attempt_number=5)
    assert score == 40  # 100 - 10*6 = 40
    
    # Win after many attempts should be clamped at minimum 10 points
    score = update_score(0, "Win", attempt_number=10)
    assert score == 10  # 100 - 10*11 = -10, clamped to 10


def test_update_score_wrong_guess_penalty():
    # Normal case: wrong guess should deduct 5 points
    score = update_score(50, "Too High", attempt_number=0)
    assert score == 45
    
    # "Too Low" should also deduct 5 points
    score = update_score(50, "Too Low", attempt_number=0)
    assert score == 45
    
    # Edge case: score near zero should not go negative
    score = update_score(3, "Too High", attempt_number=0)
    assert score == 0  # max(0, 3 - 5) = 0, not -2
    
    # Edge case: score already at zero should stay at zero
    score = update_score(0, "Too Low", attempt_number=0)
    assert score == 0
    
    # Multiple wrong guesses accumulate penalties correctly
    score = 100
    score = update_score(score, "Too High", attempt_number=0)
    assert score == 95
    score = update_score(score, "Too Low", attempt_number=1)
    assert score == 90
    score = update_score(score, "Too High", attempt_number=2)
    assert score == 85


def test_update_score_prevents_negative_score():
    # Bug fix: Ensure score never goes negative due to penalties
    # Score of 2 with 5-point penalty should become 0, not -3
    score = update_score(2, "Too High", attempt_number=0)
    assert score == 0
    assert score >= 0
    
    # Score of 1 with 5-point penalty should become 0, not -4
    score = update_score(1, "Too Low", attempt_number=0)
    assert score == 0
    assert score >= 0
    
    # Score of 4 with 5-point penalty should become 0, not -1
    score = update_score(4, "Too High", attempt_number=0)
    assert score == 0
    assert score >= 0
    
    # Score of 5 with 5-point penalty should become exactly 0
    score = update_score(5, "Too Low", attempt_number=0)
    assert score == 0
    assert score >= 0



