

def test_status_code(api):
    status = api.get().status_code
    assert status == 200