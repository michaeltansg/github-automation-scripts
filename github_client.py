# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=too-many-arguments, missing-timeout, line-too-long
import json
import requests

class GithubClient:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def get_all_gitignore_templates(self):
        """Gets all the available gitignore templates from GitHub."""
        response = requests.get("https://api.github.com/gitignore/templates", headers=self.headers)
        return response.json()

    def get_all_commonly_used_licenses(self):
        """Gets all the commonly used licenses from GitHub."""
        response = requests.get("https://api.github.com/licenses", headers=self.headers)
        return response.json()

    def create_repo(self, repo_name, repo_description, is_private, gitignore_template, license_template):
        data = {
            "name": repo_name,
            "description": repo_description,
            "private": is_private,
            "auto_init": True,
        }

        if gitignore_template != '':
            data["gitignore_template"] = gitignore_template

        if license_template != '':
            data["license_template"] = license_template

        response = requests.post(
            "https://api.github.com/user/repos",
            headers=self.headers,
            data=json.dumps(data))

        return response.json()
