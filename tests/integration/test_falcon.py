from api_star import validators
from api_star.decorators import validate
from api_star.frameworks.falcon import App
from api_star.test import TestSession


app = App(__name__, title='Day of Week API')


@app.get('/day-of-week/')
@validate(date=validators.iso_date())
def day_of_week(date):
    """
    Returns the day of the week, for the given date.
    """
    return {'day': date.strftime('%A')}


@app.post('/day-of-week/')
@validate(date=validators.iso_date())
def day_of_week_post(date):
    """
    Returns the day of the week, for the given date.
    """
    return {'day': date.strftime('%A')}


# GET requests.

def test_success():
    session = TestSession(app)
    response = session.get('/day-of-week/', params={'date': '2001-01-01'})
    assert response.status_code == 200
    assert response.json() == {'day': 'Monday'}


def test_invalid_parameter():
    session = TestSession(app)
    response = session.get('/day-of-week/', params={'date': 'foo'})
    assert response.status_code == 400
    assert response.json() == {'date': 'Not a valid date value.'}


def test_invalid_blank_parameter():
    session = TestSession(app)
    response = session.get('/day-of-week/', params={'date': ''})
    assert response.status_code == 400
    assert response.json() == {'date': 'May not be blank.'}


def test_missing_parameter():
    session = TestSession(app)
    response = session.get('/day-of-week/')
    assert response.status_code == 400
    assert response.json() == {'date': 'This parameter is required.'}


# POST requests.

def test_success_post():
    session = TestSession(app)
    response = session.post('/day-of-week/', json={'date': '2001-01-01'})
    assert response.status_code == 200
    assert response.json() == {'day': 'Monday'}


def test_invalid_parameter_post():
    session = TestSession(app)
    response = session.post('/day-of-week/', json={'date': 'foo'})
    assert response.status_code == 400
    assert response.json() == {'date': 'Not a valid date value.'}


def test_invalid_blank_parameter_post():
    session = TestSession(app)
    response = session.post('/day-of-week/', json={'date': ''})
    assert response.status_code == 400
    assert response.json() == {'date': 'May not be blank.'}


def test_missing_parameter_post():
    session = TestSession(app)
    response = session.post('/day-of-week/')
    assert response.status_code == 400
    assert response.json() == {'date': 'This parameter is required.'}
