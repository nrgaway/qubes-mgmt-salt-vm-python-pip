%{!?version: %define version %(cat version)}

Name:      qubes-mgmt-salt-vm-python-pip
Version:   %{version}
Release:   1%{?dist}
Summary:   Installs python-pip package
License:   GPL 2.0
URL:	   http://www.qubes-os.org/

Group:     System administration tools
BuildArch: noarch
Requires:  qubes-mgmt-salt
Requires:  qubes-mgmt-salt-vm
Requires:  python-pip

%define _builddir %(pwd)

%description
Installs python-pip package

%prep
# we operate on the current directory, so no need to unpack anything
# symlink is to generate useful debuginfo packages
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D

%build

%install
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} BINDIR=%{_bindir} SBINDIR=%{_sbindir} SYSCONFDIR=%{_sysconfdir}

%post
# Update Salt Configuration
qubesctl state.sls config -l quiet --out quiet > /dev/null || true
qubesctl saltutil.clear_cache -l quiet --out quiet > /dev/null || true
qubesctl saltutil.sync_all refresh=true -l quiet --out quiet > /dev/null || true

# Enable States
qubesctl top.enable python-pip saltenv=vm -l quiet --out quiet > /dev/null || true

%files
%defattr(-,root,root)
%doc LICENSE README.rst
%attr(750, root, root) %dir /srv/formulas/vm/python-pip-formula

/srv/formulas/vm/python-pip-formula/LICENSE
/srv/formulas/vm/python-pip-formula/python-pip/init.sls
/srv/formulas/vm/python-pip-formula/python-pip/init.top
/srv/formulas/vm/python-pip-formula/python-pip/map.yaml
/srv/formulas/vm/python-pip-formula/README.rst

%changelog
