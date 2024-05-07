> :warning::rotating_light: This project is no longer maintained and has been archived.

[![build-test](https://github.com/darkwizard242/ansible-role-msteams/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-msteams/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-msteams/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-msteams/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/56469?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/56469?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/56469?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-msteams&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-msteams) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-msteams&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-msteams) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-msteams&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-msteams) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-msteams&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-msteams) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-msteams?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-msteams?color=orange&style=flat-square)

# Ansible Role: msteams

Role to install (_by default_) [Microsoft Teams](https://docs.microsoft.com/en-us/microsoftteams/teams-overview) package or uninstall (_if passed as var_) on Debian based systems and EL based systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
msteams_app: teams
msteams_app_desired_state: present

# Debian family based
msteams_repo_debian_gpg_key: https://packages.microsoft.com/keys/microsoft.asc
msteams_repo_debian: "deb [arch=amd64] https://packages.microsoft.com/repos/ms-teams stable main"
msteams_repo_debian_filename: "{{ msteams_app }}"
msteams_repo_debian_desired_state: present

# EL family based
msteams_repo_el: "https://packages.microsoft.com/yumrepos/ms-teams"
msteams_repo_el_name: teams
msteams_repo_el_description: teams
msteams_repo_el_gpgkey: https://packages.microsoft.com/keys/microsoft.asc
msteams_repo_el_gpgcheck: yes
msteams_repo_el_enabled: yes
msteams_repo_el_filename: "{{ msteams_app }}"
msteams_repo_el_desired_state: present
```

### Variables table:

Variable                          | Description
--------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
msteams_app                       | Name of Microsft Teams application package require to be installed i.e. `teams`
msteams_app_desired_state         | State of the Microsft Teams package. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
msteams_repo_debian_gpg_key       | Microsft Teams key required on Debian family systems.
msteams_repo_debian               | Microsft Teams repo URL for Debain family systems.
msteams_repo_debain_filename      | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems.
msteams_repo_debian_desired_state | `present` indicates creating the repository file if it doesn't exist on Debian based systems. Alternative is `absent` (not recommended as it will prevent from installation of **teams** package).
msteams_repo_el                   | Repository `baseurl` for Microsft Teams on EL based systems.
msteams_repo_el_name              | Repository name for Microsft Teams on EL based systems.
msteams_repo_el_description       | Description to be added in EL based repository file for Microsft Teams.
msteams_repo_el_gpgkey            | Microsft Teams GPG key required on EL family systems
msteams_repo_el_gpgcheck          | Boolean for whether to perform gpg check against Microsft Teams on EL based systems.
msteams_repo_el_enabled           | Boolean to set so that Microsft Teams repository is enabled on EL based systems.
msteams_repo_el_filename          | Name of the repository file that will be stored at `/yum/sources.list.d/teams.repo` on EL based systems.
msteams_repo_el_desired_state     | `present` indicates creating the repository file if it doesn't exist on EL based systems. Alternative is `absent` (not recommended as it will prevent from installation of **teams** package).

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **msteams** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.msteams
```

For customizing behavior of role (i.e. installing/upgrading to latest version of teams as an example) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.msteams
  vars:
    msteams_apps_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **msteams** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.msteams
  vars:
    msteams_apps_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-msteams/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
