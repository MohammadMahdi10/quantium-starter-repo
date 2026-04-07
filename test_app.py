import pytest
from dash import Dash
from dash.testing.application_runners import import_app

# Fixture to load the Dash app
@pytest.fixture
def dash_app():
    app = import_app("app")  # 'app' is the name of your app.py file without '.py'
    return app

# Test 1: Header exists
def test_header(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert "Pink Morsel Sales Dashboard" in header.text

# Test 2: Line chart exists
def test_graph(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

# Test 3: Region picker exists
def test_region_picker(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    radio = dash_duo.find_element("#region-filter")
    assert radio is not None