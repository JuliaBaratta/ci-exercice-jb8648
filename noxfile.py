from __future__ import annotations

import nox


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
    session.run("python", "-m", "http.server", "8000", "-d", "docs/_build/html")


@nox.session
def test(session: nox.Session) -> None:
    """
    Run tests.
    """

    session.install(".[test]")
    session.run("pip", "list")
    session.run("pytest", "tests", env={"PYTHONPATH": "src"})
