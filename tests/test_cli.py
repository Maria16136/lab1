import subprocess


def test_cli_calc_success():
    process = subprocess.run(
        ['python', '-m', 'toolkit', 'calc', '7+3'],
        capture_output=True,
        text=True,
        check=False,
    )

    assert process.stdout == '10.0\n'
    assert process.returncode == 0


def test_cli_convert_success():
    process = subprocess.run(
        ['python', '-m', 'toolkit', 'convert', '100', '--from', 'cm', '--to', 'm'],
        capture_output=True,
        text=True,
        check=False,
    )

    assert process.stdout == '1.0\n'
    assert process.returncode == 0


def test_cli_calc_error():
    process = subprocess.run(
        ['python', '-m', 'toolkit', 'calc', '7-5*2+'],
        capture_output=True,
        text=True,
        check=False,
    )

    assert process.stdout == 'Введено некорректное выражение\n'
    assert process.returncode == 2


def test_cli_convert_error():
    process = subprocess.run(
        ['python', '-m', 'toolkit', 'convert', '-300', '--from', 'c', '--to', 'k'],
        capture_output=True,
        text=True,
        check=False,
    )

    assert process.stdout == 'Введено некорректное выражение\n'
    assert process.returncode == 2


def test_cli_help():
    process = subprocess.run(
        ['python', '-m', 'toolkit', '--help'],
        capture_output=True,
        text=True,
        check=False,
    )

    assert process.returncode == 0
    assert 'calc' in process.stdout
    assert 'convert' in process.stdout