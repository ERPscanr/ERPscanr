"""Tests for the database classes and functions from erpsc.core."""

import os

from erpsc.core.db import ERPDB, check_db

##################################################################################
##################################################################################
##################################################################################

def test_erpdb():
    """Test the ERPDB object."""

    # Check that ERPDB returns properly.
    assert ERPDB(auto_gen=False)

def test_erpdb_gen_paths():
    """Check that gen_paths method of ERPDB."""

    db = ERPDB(auto_gen=False)
    db.gen_paths()

    assert db

def test_omdb_paths():
    """Test that all defined OMDB paths exist."""

    db = ERPDB()

    # Loops through all paths, checking they exist
    #  Skips vars with '_path' marker, and empty variables
    for key, val in vars(db).items():
        if '_path' in key and val:
            assert os.path.exists(val)

def test_check_db():
    """Test the check_db function."""

    # Check that it returns an ERPDB when given None
    db = check_db(None)
    assert isinstance(db, ERPDB)

    # Check that it returns an ERPDb object when given one
    db = ERPDB()
    db = check_db(db)
    assert isinstance(db, ERPDB)