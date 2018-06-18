import pytest
from are_you_sure import are_you_sure
import builtins

class TestAreYouSure():
    def test_are_you_sure_not_y(self, monkeypatch, capsys):
        monkeypatch.setattr('builtins.input', lambda x: 'lol')

        @are_you_sure
        def dangerous_function(*args, **kwargs):
            print(f'Running {__name__} with {args,kwargs}')
        dangerous_function()
        captured = capsys.readouterr()
        assert captured.out == 'Aborted without running\n'

    def test_are_you_sure_y(self, monkeypatch, capsys):
        monkeypatch.setattr('builtins.input', lambda x: 'y')

        @are_you_sure
        def dangerous_function(*args, **kwargs):
            print(f'Running {dangerous_function.__name__} with {args,kwargs}')
        dangerous_function()
        captured = capsys.readouterr()
        assert captured.out == "Running dangerous_function with ((), {})\n"
