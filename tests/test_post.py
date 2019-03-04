import unittest
from models import Post
Post = post.Post

class PostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Post class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post(id,title, description,user_id,comment)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

if __name__ == '__main__':
    unittest.main()


