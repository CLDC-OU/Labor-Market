import urllib.request, urllib.parse, urllib.error
import base64
import json
import sys
import os
from dotenv import load_dotenv

class ONET_report:
  def __init__(self, codes): 
     self.codes = codes if codes is not None else sys.stdin.read().split("\n")

  def call(self):
    '''
    Takes in desired SOC codes, calls to ONET, and retrieves information for said SOC codes which is stored into a data dictionary.

    Input(s):
      - codes (list): List of the SOC code strings.

    Creates:
        - json file with SOC code as key.
    '''

    load_dotenv()
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')

    # read JSON input
    input = { "config": {
        "username": USERNAME,
        "password": PASSWORD,
        "max_results": 1
      }, "codes": self.codes}

    # initialize Web Services and results objects
    onet_ws = OnetWebService(input['config']['username'], input['config']['password'])
    max_results = max(1, input['config']['max_results'])
    output = {}

    # call search for each input query
    for code in input['codes']:
        coderesults = onet_ws.call('careers',
                                ('code', code),
                                'report',
                                ('end', max_results))
        
        if ('code' in coderesults) and (0 < len(coderesults['code'])):
            output[coderesults['code']] = { 'results': coderesults }

    json.dump(output, sys.stdout, indent=2, sort_keys=True)

class OnetWebService:
        
    def __init__(self, username, password):
        self._headers = {
            'User-Agent': 'python-OnetWebService/1.00 (bot)',
            'Authorization': 'Basic ' + base64.standard_b64encode((username + ':' + password).encode()).decode(),
            'Accept': 'application/json' }
        self.set_version()
    
    def set_version(self, version = None):
        if version is None:
            self._url_root = 'https://services.onetcenter.org/ws/mnm/'
        else:
            self._url_root = 'https://services.onetcenter.org/v' + version + '/ws/'
    
    def call(self, path, *query):
        url = self._url_root + path

        if len(query) > 0:
            url += '/' + query[0][1] + '.00/' + query[1]
        req = urllib.request.Request(url, None, self._headers)
        handle = None
        try:
            handle = urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            if e.code == 422:
                return json.load(e)
            else:
                return { 'error': 'Call to ' + url + ' failed with error code ' + str(e.code) }
        except urllib.error.URLError as e:
            return { 'error': 'Call to ' + url + ' failed with reason: ' + str(e.reason) }
        code = handle.getcode()
        if (code != 200) and (code != 422):
            return { 'error': 'Call to ' + url + ' failed with error code ' + str(code),
                     'urllib2_info': handle }
        return json.load(handle)

codes = sys.stdin.read().split("\n")
ONET_report(codes).call()
