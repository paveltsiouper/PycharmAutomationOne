import pytest

a=101
validateOne="ValidateOne"
validateTwo="HelloTwo"

@pytest.fixture(scope="module")
def fixture_code():
    print("")
    print("**************************************")
    print("This is the Fixture Code ExEcuted in testcase if the fixture name passed as an argument")
    print("**************************************")
    yield
    print("")
    print("/////////////////////////////////////////////////////////")
    print("This is the Fixture Code ExEcuted AFTER in testcase if the fixture name passed as an argument")
    print("/////////////////////////////////////////////////////////")


@pytest.mark.skipif(a>100,reason="Skipping as test case is not working")
def test_to_002_Login_logout_testLog():
    print("This is 2nd test cases code...")
    print("This is end of any testcase")


@pytest.mark.Smoke
@pytest.mark.Regression
def test_to_003_TheSameFile_testLog(fixture_code):
    print("SmokeTest:This is 3rd test cases code...")
    print("This is end of any testcase")
    assert validateOne == "HelloOne";

@pytest.mark.Sanity
@pytest.mark.Smoke
def test_to_004_Login_logout():
    print('helloclear')
    print("Sanity:This is 3rd test cases code...")
    print("This is end of any testcase")
    assert validateTwo != "HelloTwo", "This 2 messages must be not the same";


@pytest.mark.Regression
def test_to_005_Login_logout():
    print('helloclear')
    print("Sanity:This is 3rd test cases code...")
    print("This is end of any testcase")