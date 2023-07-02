# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long
import os
from dotenv import load_dotenv
from github_client import GithubClient

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

def main():
    github_client = GithubClient(TOKEN)

    valid_gitignore_templates = github_client.get_all_gitignore_templates()
    valid_licenses = github_client.get_all_commonly_used_licenses()
    valid_license_keys = [item["key"] for item in valid_licenses]

    while True:
        repo_name = input("Name of the repository: ")
        if repo_name != '':
            break
        print("Repository name cannot be empty.")

    repo_description = input("Description for the repository: ")
    private_response = input("Should the repository be private? (Y/n): ")
    is_private = not private_response.lower().startswith('n')

    while True:
        gitignore_template = input("Type of .gitignore template ('?' for list): ")
        if gitignore_template == '' or gitignore_template in valid_gitignore_templates:
            break
        print(f"Possible options: {', '.join(valid_gitignore_templates)}")

    while True:
        license_template = input("Type of license ('?' for list): ")
        if license_template == '' or license_template in valid_license_keys:
            break
        print(f"Possible options: {', '.join(valid_license_keys)}")

    response = github_client.create_repo(
        repo_name,
        repo_description,
        is_private,
        gitignore_template,
        license_template)

    # TODO: Handle errors and exceptions - e.g. token invalid, repo name already exists, etc.
    print(response["html_url"])


if __name__ == "__main__":
    main()
