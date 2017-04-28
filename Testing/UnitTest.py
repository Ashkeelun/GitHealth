import requests
import unittest

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:8000/health/api/'
        self.payload = {"url":"https://github.com/celalgorgun/TestFile"}


    def testResponse(self):
        r = requests.post(self.url, self.payload)
        #Test Request
        self.assertEqual(r.status_code, 200)

        self.assertEquals(r.json()["root"]["total_doc_info"]["slcSize"], 93)
        self.assertEquals(r.json()["root"]["total_doc_info"]["mlcNum"], 3)
        self.assertEquals(r.json()["root"]["total_doc_info"]["mlcSize"], 271)
        self.assertEquals(r.json()["root"]["total_doc_info"]["codeSize"], 551)
        self.assertEquals(r.json()["root"]["total_doc_info"]["comtSize"], 364)
        self.assertEquals(r.json()["root"]["total_doc_info"]["slcNum"], 6)
        
        #Test 1 file
        self.assertEquals(r.json()["root"]["sub_files"][0]["mlc_size"], 72)
        self.assertEquals(r.json()["root"]["sub_files"][0]["mlc_num"], 1)
        self.assertEquals(r.json()["root"]["sub_files"][0]["slc_size"], 16)
        self.assertEquals(r.json()["root"]["sub_files"][0]["slc_num"], 1)
        self.assertEquals(r.json()["root"]["sub_files"][0]["comt_size"], 88)
        self.assertEquals(r.json()["root"]["sub_files"][0]["code_size"], 125)
        #Test 2 file
        self.assertEquals(r.json()["root"]["sub_files"][1]["mlc_size"], 97)
        self.assertEquals(r.json()["root"]["sub_files"][1]["mlc_num"], 1)
        self.assertEquals(r.json()["root"]["sub_files"][1]["slc_size"], 27)
        self.assertEquals(r.json()["root"]["sub_files"][1]["slc_num"], 2)
        self.assertEquals(r.json()["root"]["sub_files"][1]["comt_size"], 124)
        self.assertEquals(r.json()["root"]["sub_files"][1]["code_size"], 148)
        #Test 3 file
        self.assertEquals(r.json()["root"]["sub_files"][2]["mlc_size"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][2]["mlc_num"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][2]["slc_size"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][2]["slc_num"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][2]["comt_size"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][2]["code_size"], 0)
        #Test 4 file
        self.assertEquals(r.json()["root"]["sub_files"][3]["mlc_size"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][3]["mlc_num"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][3]["slc_size"], 50)
        self.assertEquals(r.json()["root"]["sub_files"][3]["slc_num"], 3)
        self.assertEquals(r.json()["root"]["sub_files"][3]["comt_size"], 50)
        self.assertEquals(r.json()["root"]["sub_files"][3]["code_size"], 2)
        #Test 5 file
        self.assertEquals(r.json()["root"]["sub_files"][4]["mlc_size"], 102)
        self.assertEquals(r.json()["root"]["sub_files"][4]["mlc_num"], 1)
        self.assertEquals(r.json()["root"]["sub_files"][4]["slc_size"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][4]["slc_num"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][4]["comt_size"], 102)
        self.assertEquals(r.json()["root"]["sub_files"][4]["code_size"], 0)
        #Test 6 file
        self.assertEquals(r.json()["root"]["sub_files"][5]["mlc_size"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][5]["mlc_num"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][5]["slc_size"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][5]["slc_num"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][5]["comt_size"], 0)
        self.assertEquals(r.json()["root"]["sub_files"][5]["code_size"], 276)

if __name__ == '__main__':
    unittest.main()
