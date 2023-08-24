import requests


class FindMyPy:
    @staticmethod
    def get_github_url(package_name: str) -> str | None:
        """
        Given a PyPI package name, call the pypi.org api and return
        the package's Github URL.

        Params
        ------
        package_name (str): the name of the pypi package

        Returns
        -------
        github_url (str): the url of the github repo for the pypi package
        """
        url = f"https://www.pypi.org/pypi/{package_name}/json"
        resp = requests.get(url)

        if not resp.ok:
            return None

        payload = resp.json()
        package_urls_blob = payload.get("info", {}).get("project_urls", {})

        homepage_url = package_urls_blob.get("Homepage")

        return homepage_url
