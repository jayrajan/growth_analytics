from core import post_time,fname,CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET, js, item
from fuse_image import fuse_logo, hc_logo
import unittest

class TestCoreApp(unittest.TestCase):
    '''
    Unit Tests for Core App
    '''

    def test_SchedulerTime(self):
        '''
        Testing that the correct scheduler time value is used in variable
        '''
        a = 5
        self.assertEqual(post_time,a,'Should be 5')

    def test_ExcelInput(self):
        '''
        Testing that the correct excel file is captured
        '''
        filename = 'GrowthAnalytics_python test_final.xlsx'
        self.assertEqual(fname,filename,'Should be GrowthAnalytics_python test_final.xlsx')

    def test_tweet_consKey(self):
        '''
        Testing the Twitter Consumer Key Token
        '''
        consumer_key = 'oBiIhg7ZF5wefAihCCm1rl1Wj'
        self.assertEqual(CONSUMER_KEY,consumer_key,'incorrect consumer key detected')

    def test_tweet_consSec(self):
        '''
        Testing the Twitter Consumer Secret Token
        '''
        consumer_sec = 'bG6DjIFrIaqsrIFv5pafCXRbGtpC6nYz8HIcMJxocHQ6sQGkes'
        self.assertEqual(CONSUMER_SECRET,consumer_sec,'incorrect consumer secret detected')

    def test_tweet_accessToken(self):
        '''
        Testing the Twitter Access Token
        '''
        access_token = '290090813-XSgGWVmRde2FT3o4DgBoRMkyxqSqHCXUMD5in5Vt'
        self.assertEqual(ACCESS_TOKEN,access_token,'incorrect access token detected')

    def test_tweet_access_sec_Token(self):
        '''
        Testing the Twitter Access Secret Token
        '''
        access_sec_token = 'sPUVX7l1sXgUkxf25nw1PCdS55Os3caTmOA3IE6RPOI7s'
        self.assertEqual(ACCESS_TOKEN_SECRET,access_sec_token,'incorrect access secret token detected')

    def test_fuseLogo(self):
        '''
        Testing the output response of the fuse logo function
        '''
        url = 'https://upload.wikimedia.org/wikipedia/commons/5/5d/Kamchatka_Brown_Bear_near_Dvuhyurtochnoe_on_2015-07-23.jpg'
        id = 55
        result = fuse_logo(url,id)
        expected = './fusion/55.jpg'
        self.assertEqual(result,expected, 'Incorrect filename')

    def test_logo(self):
        '''
        Testing if the correct HPC logo link is used on the images.
        '''
        expected_url = 'http://cityread.london/wp-content/uploads/2016/02/HarperCollins-logo.png'
        self.assertEqual(hc_logo,expected_url, 'Incorrect logo')

    def test_json_postID(self):
        '''
        Testing if the Json contains the item - post_ID
        '''
        self.assertIn('post_id',item, 'incorrect datasource')

    def test_json_posttext(self):
        '''
        Testing if the Json contains the item - post_text
        '''
        self.assertIn('post_text',item, 'incorrect datasource')

    def test_json_postImg(self):
        '''
        Testing if the Json contains the item - post_img
        '''
        self.assertIn('post_img',item, 'incorrect datasource')

    # FileNotFoundError: [Errno 2] No such file or directory: 'GrowthAnalytics'

if __name__ == '__main__':
    unittest.main()
