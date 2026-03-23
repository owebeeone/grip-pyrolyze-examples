def test_import_demo_namespace() -> None:
    import grip_pyrolyze.examples.demo

    assert grip_pyrolyze.examples.demo.__name__ == "grip_pyrolyze.examples.demo"
