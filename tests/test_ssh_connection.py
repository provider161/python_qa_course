"""
Test for ssh connection to docker container with opencart app. Test connects to container using ssh fixture,
makes dir and deletes that dir
"""


def test_ssh_connection(ssh_client):
    test_dir = 'test_dir'
    stdin_before, stdout_before, stderr_before = ssh_client.exec_command('ls -la')
    ssh_client.exec_command(f'mkdir {test_dir}')
    stdin_after, stdout_after, stderr_after = ssh_client.exec_command('ls -la')
    ssh_client.exec_command(f'rm -rf {test_dir}')
    stdin_finally, stdout_finally, stderr_finally = ssh_client.exec_command('ls -la')
    out_before = stdout_before.read().decode("utf-8")
    out_after = stdout_after.read().decode("utf-8")
    out_finally = stdout_finally.read().decode("utf-8")
    assert test_dir not in out_before
    assert test_dir in out_after
    assert test_dir not in out_finally
