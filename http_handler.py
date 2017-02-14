import requests
import requests_mock
from db_schema import handle_db_operation




#requests_mock.Mocker.TEST_PREFIX = 'put'

def register_info_into_db(s,user_name,user_url):
    short_url = ""
    a_user = UserInfo(name=user_name)
    last_row_id = s.query(URLInfo).order_by(URLInfo.url_id.desc()).first()
    if last_row_id == None:
        short_url = base62encoder.toBase62(0)
    else:
        short_url = base62encoder.toBase62(last_row_id.url_id+1)
    a_url = URLInfo(original_URL=user_url,shortened_URL=short_url)
    s.add(a_user)
    s.add(a_url)
    s.commit()
    print('details registered for: ',user_name)
    print('Short-URL: ','mydomain.com/'+short_url)
    one_more = input('Do you want to enter one more long URL?')
    return one_more

#class Http_Mocks(object):
@requests_mock.Mocker()
def url_put_db(user_name,user_password,user_long_url,mock_object):
    mock_object.register_uri('POST','http://myservice.com',text="Success!! You're url has been shortened to {}".format())
    register_info_into_db(user_name,user_url)

    return requests.post('http://myservice.com').text

'''def url_get_db(self,user_name,user_password,user_long_url,mock_object):
    mock_object.register_uri('POST','http://myservice.com',text="Success!! You're url has been shortened to {}".format())
    handle_db_operation(user_name,user_password,user_long_url):
    return requests.post('http://myservice.com').text'''
