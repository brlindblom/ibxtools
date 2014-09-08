Name:     ibxtools
Version:	0.1
Release:	1%{?dist}
Summary:	Backup tools for InnoDB-backed databases

Group:		MySQL Database server
License:	GPL
URL:		  https://github.com/brlindblom/ibxtools
Source0:	https://github.com/brlindblom/ibxtools/archive/master.zip
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	percona-xtrabackup /usr/bin/mysql /usr/bin/mysqldump /usr/bin/mysqladmin

%description
ibxtools provides backup and restore scripts for managing backups on InnoDB-based
MySQL/Percona/MariaDB database servers

%prep
%setup -n ibxtools-master

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}%{_docdir}
cp ibxbackup %{buildroot}/usr/bin/
cp ibxrestore %{buildroot}/usr/bin/
cp README.md %{buildroot}%{_docdir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %_docdir/README.md
%_bindir/ibxbackup
%_bindir/ibxrestore

%changelog
* Mon Sep 9  2014 - lindblom (at) ornl.gov
- Initial spec file creation
