import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'teams'
PACKAGE_BINARY = '/usr/bin/teams'
DEBIAN_REPO_FILE = '/etc/apt/sources.list.d/teams.list'
EL_REPO_FILE = '/etc/yum.repos.d/teams.repo'


def test_teams_package_installed(host):
    """
    Tests if teams is installed.
    """
    assert host.package("teams").is_installed


def test_teams_binary_exists(host):
    """
    Tests if teams binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_teams_binary_file(host):
    """
    Tests if teams binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_teams_binary_which(host):
    """
    Tests the output to confirm teams's binary location.
    """
    assert host.check_output('which teams') == PACKAGE_BINARY


def test_teams_repo_exists(host):
    """
    Tests if teams repo exists on DEBIAN/EL Systems.
    """
    assert host.file(DEBIAN_REPO_FILE).exists or \
        host.file(EL_REPO_FILE).exists


def test_teams_repo_file(host):
    """
    Tests if teams repo is a file type on DEBIAN/EL Systems.
    """
    assert host.file(DEBIAN_REPO_FILE).is_file or \
        host.file(EL_REPO_FILE).is_file
