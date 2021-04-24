from flaskAppServer import create_app
    
def test_greeting(self):
    assert self.get('/query/greeting').status_code == 200
    response = self.get('/query/greeting')
    assert response.data == b'Hello this message is coming from query Blueprint.'
