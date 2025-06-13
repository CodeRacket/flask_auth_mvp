def test_custom_commands(runner):
    result = runner().invoke(args=["test"])
    assert result.exit_code == 0
    assert "hello, world!" in result.output.lower()
