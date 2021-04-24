from flaskAppServer import create_app
    
def test_greeting(self):
    assert self.get('/ingest/greeting').status_code == 200
    response = self.get('/ingest/greeting')
    assert response.data == b'Hello this message is coming from ingest Blueprint.'
