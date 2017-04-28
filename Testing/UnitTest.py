import requests
import unittest

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:8000/health/api/'
        self.payload = {"url":"https://github.com/celalgorgun/TestFile"}


    def testResponse(self):
        r = requests.post(self.url, self.payload)
        self.assertEqual(r.status_code, 200)

        self.assertEquals(r.json()["root"]["total_doc_info"]["slcSize"], 93)
        self.assertEquals(r.json()["root"]["total_doc_info"]["mlcNum"], 3)
        self.assertEquals(r.json()["root"]["total_doc_info"]["mlcSize"], 271)
        self.assertEquals(r.json()["root"]["total_doc_info"]["codeSize"], 551)
        self.assertEquals(r.json()["root"]["total_doc_info"]["comtSize"], 364)
        self.assertEquals(r.json()["root"]["total_doc_info"]["slcNum"], 6)
        self.assertEquals(r.json()["root"]["sub_files"][0]["mlc_size"], 72)

if __name__ == '__main__':
    unittest.main()
