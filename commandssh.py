import getpass
from pssh.clients import ParallelSSHClient

def go():
    command = 'uname -a'
    nodes = ['localhost']
    pw = getpass.getpass()
    client = ParallelSSHClient(nodes, password=pw, timeout=3)
    client.run_command(command)
    output = client.get_last_output()
    for node in output:
        for line in output[node]['stdout']:
            print('{0}  {1}'.format(node, line))


if __name__ == '__main__':
    go()
