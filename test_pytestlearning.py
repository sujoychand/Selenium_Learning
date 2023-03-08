""" The file contains the examples which were done when learning pytest
    Thanks to accidental tester who is producing awesome content
"""
import pytest


@pytest.fixture()  # Run the fixture associated with the function which represent the common portion of the application
@pytest.mark.cra
def test_setup():
    print("This is test setup")
    yield  # To be used at the end of the test
    print("this is end of test")


def test_case_1(test_setup):  # Represents running the corresponding set-up
    print("Test Case Result -1 :Pass")


@pytest.mark.cra  # Use of the cra pytest marker
def test_case_2():
    print("Test Case Result -2 :Pass")


def test_case_method_1(test_setup):
    print("Test Case Method Result -1 :Pass")

