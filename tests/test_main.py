from unittest import TestCase
from mock import Mock, call
from blogger import blogger


class MainTests(TestCase):
    posts = {"items": [
            {
                "id": "100",
                "title": "title",
                "url": "url"
            }
            ]
            }

    def test_should_invoke_post(self):
        args = blogger.parse_args(['post', "-t", "t", "-c", "content"])
        blogObj = Mock()
        blogObj.post.return_value = {"id": "100"}

        exitStatus = blogger.runner(args, blogObj)

        blogObj.post.assert_called_with("t", "content", None, fmt="html")
        assert exitStatus == 0

    def test_should_invoke_delete(self):
        args = blogger.parse_args(['delete', '100', "200"])
        blogObj = Mock()

        blogger.runner(args, blogObj)

        assert blogObj.deletePost.call_count == 2
        expected = [call.deletePost('100'), call.deletePost('200')]
        assert blogObj.mock_calls == expected

    def test_should_invoke_update(self):
        args = blogger.parse_args(['update', "-t", "t", "-c", "content", "100"])
        blogObj = Mock()

        blogger.runner(args, blogObj)

        blogObj.updatePost.assert_called_with("100", "t", "content", None, fmt="html")

    def test_should_invoke_getbyid(self):
        args = blogger.parse_args(['get', "-p", "100"])
        blogObj = Mock()
        blogObj.getPosts.return_value = MainTests.posts

        blogger.runner(args, blogObj)

        blogObj.getPosts.assert_called_with(postId="100")

    def test_should_invoke_search(self):
        args = blogger.parse_args(['get', "-q", "query"])
        blogObj = Mock()
        blogObj.getPosts.return_value = MainTests.posts

        blogger.runner(args, blogObj)
        blogObj.getPosts.assert_called_with(query="query", maxResults=10)

    def test_empty_results_in_get(self):
        args = blogger.parse_args(['get', "-q", "query"])
        blogObj = Mock()
        blogObj.getPosts.return_value = {}

        blogger.runner(args, blogObj)
        blogObj.getPosts.assert_called_with(query="query", maxResults=10)

    def test_handle_non_existent_keys_in_fields(self):
        args = blogger.parse_args(['get', "-q", "query", "-f", "id,b"])
        blogObj = Mock()
        blogObj.getPosts.return_value = MainTests.posts

        blogger.runner(args, blogObj)
        blogObj.getPosts.assert_called_with(query="query", maxResults=10)
