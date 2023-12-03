#!/usr/bin/env python3
"""
This script contains fixtures for the client module
"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from requests import HTTPError
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Test fixtures for testing methods in GitHubOrgClient class
    """
    @parameterized.expand([
        ('google', {'name': 'Google'}),
        ('abc', {'name': 'abc'}),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """
        Test the method org and patch get_json method to prevent external call
        """
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """testing public repos url"""
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mocked_fxn:
            url = "https://api.github.com/orgs/google/repos"
            mocked_fxn.return_value = {
                'repos_url': url,
            }
            self.assertEqual(
                GithubOrgClient('google')._public_repos_url, url)
    
    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """testing public repos"""
        test_payload = [
            {'name': 'Swizz'},
            {'name': '6ix'}
        ]
        rtn_obj = {'repos_url': test_payload}
        mock_get_json.return_value = rtn_obj["repos_url"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload
            new_obj = GitHubOrgClient('github').public_repos()
            self.assertEqual(new_obj, [ "swizz6ix", '6ix'])
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """testing if license exists"""
        gh_org_client = GithubOrgClient('google')
        client_has_license = gh_org_client.has_license(repo, key)
        self.assertEqual(client_has_license, expected)

@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repo_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration Testing: Mock code that sends external requests only
    """
    @classmethod
    def setUpClass(cls) -> None:
        """Start up method before the rest fixture"""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            """get the payload value"""
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError
        
        cls.get_patcher = patch('request.get', side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Test the public repos"""
        self.assertEqual(
            GithubOrgClient('google').public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """test the public repo with license"""
        self.assertEqual(
            GithubOrgClient('google').public_repos(license='apache-2.0'),
            self.apache2_repos,
        )
    
    @classmethod
    def tearDownClass(cls) -> None:
        """cleanup after testing"""
        cls.get_patcher.stop()
