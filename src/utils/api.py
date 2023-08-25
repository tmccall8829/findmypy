import logging
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
        project_urls_blob = payload.get("info", {}).get("project_urls", {})

        # some pypi projects have a "repository" key and some don't
        # also, sometimes these keys are capitalized in the payload
        search_keys = ["repository", "homepage"]

        url_blob_keys = list(project_urls_blob.keys())
        for key in search_keys:
            cap_key = key.capitalize()
            if key in url_blob_keys and "github.com" in project_urls_blob[key]:
                url = project_urls_blob[key]
                logging.info(f"Found repo url for {package_name} under {key}: {url}")
                return url
            elif (
                cap_key in url_blob_keys and "github.com" in project_urls_blob[cap_key]
            ):
                url = project_urls_blob[cap_key]
                logging.info(
                    f"Found repo url for {package_name} under {cap_key}: {url}"
                )
                return url

        logging.warning(f"Repo or homepage URL not found for {package_name}")
        return f"https://pypi.org/project/{package_name}"
