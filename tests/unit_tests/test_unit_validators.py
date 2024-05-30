from sample.validators import validate_name


def test_validate_name__too_short__returns_false():
    # arrange
    too_short = 'Iv'

    # act
    actual = validate_name(too_short)

    # assert
    assert actual is False


def test_name_input__malformed__returns_false():
    # arrange
    malformed_name = 'Select *'

    # act
    actual = validate_name(malformed_name)

    # assert
    assert actual is False


def test_name_input__valid_input__returns_true():
    # arrange
    valid_name = 'Gary'

    # act
    actual = validate_name(valid_name)

    # assert
    assert actual is True