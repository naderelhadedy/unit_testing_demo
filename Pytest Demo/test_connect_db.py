import dbm
from connect_db import StudentDB
import pytest


@pytest.fixture(scope='module')
def db ():
    db = StudentDB()
    db.connect("data.json")
    yield db # will run and stop here as a setup
    # will run as a teardown
    print()
    db.close("All tests are done!")


# Setup and Teardown methods

# db = None

# def setup_module(module):
#     print("--------------------SETUP--------------------", end=" ")
#     global db
#     db = StudentDB()
#     db.connect("data.json")


# def teardown_module(module):
#     print(" --------------------TEARDOWN--------------------")
#     print()
#     db.close("All tests are done!")


def test_ahmed_data(db):
    ahmed_data = db.get_data("Ahmed")
    
    assert ahmed_data["id"] == 1
    assert ahmed_data["name"] == "Ahmed"
    assert ahmed_data["result"] == "passed"


def test_heba_data(db):
    heba_data = db.get_data("Heba")
    
    assert heba_data["id"] == 3
    assert heba_data["name"] == "Heba"
    assert heba_data["result"] == "failed"
