%global cartridgedir %{_libexecdir}/openshift/cartridges/v2/fuse
%global frameworkdir %{_libexecdir}/openshift/cartridges/v2/fuse

Name: fuse-openshift-cartridge-openshift-enterprise-rpm
Version: 6.1.0.redhat.382
Release: 3%{?dist}
Summary: Fuse cartridge
Group: Development/Languages
License: ASL 2.0
URL: https://www.openshift.com
Source0: https://github.com/jboss-fuse/fuse-openshift-cartridge/archive/openshift-enterprise-rpm-6.1-6.1.0.redhat.382-3.tar.gz
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Fuse cartridge for openshift. (Cartridge Format V2)


%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{cartridgedir}
mkdir -p %{buildroot}/%{_sysconfdir}/openshift/cartridges/v2
cp -r * %{buildroot}%{cartridgedir}/
ln -s %{cartridgedir}/conf/ %{buildroot}/%{_sysconfdir}/openshift/cartridges/v2/%{name}


%clean
rm -rf %{buildroot}


%post
%{_sbindir}/oo-admin-cartridge --action install --offline --source /usr/libexec/openshift/cartridges/v2/fuse

%files
%defattr(-,root,root,-)
%dir %{cartridgedir}
%dir %{cartridgedir}/bin
%dir %{cartridgedir}/env
%dir %{cartridgedir}/metadata
%dir %{cartridgedir}/versions
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{frameworkdir}
%{_sysconfdir}/openshift/cartridges/v2/%{name}
%{cartridgedir}/metadata/manifest.yml
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE


%changelog
* Wed Jun 16 2014 Jon Anstey <janstey@gmail.com> 6.1.0.redhat.382-3
- Use 382 build no rather than 379
- Use redhat vendor name

* Wed Jun 11 2014 Jon Anstey <janstey@gmail.com> 6.1.0.redhat.382-1
- Fuse 6.1 rollup patch #1

* Wed Jun 11 2014 Jon Anstey <janstey@gmail.com> 6.1.0.redhat.379-1
- Fuse 6.1 GA cartridge
