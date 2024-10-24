import nox
import sys  # Add this import
from pathlib import Path

@nox.session
def docs(session: nox.Session) -> None:
    """
    Build the docs. Pass "--serve" to serve.
    """

    session.install(".[docs]")
    session.chdir("docs")
    session.run("sphinx-build", "-M", "html", ".", "build")

@nox.session
def serve(session: nox.Session) -> None:
    """
    Serve the built documentation.
    """
    docs(session)  # Build the docs first
    print("Launching docs at http://localhost:8000/ - use Ctrl-C to quit")
    session.run("python", "-m", "http.server", "8000", "-d", "docs/_build/html")

@nox.session
def test(session: nox.Session) -> None:
    """
    Run tests.
    """

    session.install(".[test]")
    session.run("pytest")
