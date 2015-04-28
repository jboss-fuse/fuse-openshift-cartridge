%global product_build_number 110

%global cartridgedir %{_libexecdir}/openshift/cartridges/fuse-builder
%global frameworkdir %{_libexecdir}/openshift/cartridges/fuse-builder
%global github_tag openshift-enterprise-fuse-builder-rpm-6.2

Name: openshift-origin-cartridge-fuse-builder
Version: 6.2.0.redhat.%{product_build_number}
Release: 1%{?dist}
Summary: Fuse Builder cartridge
Group: Development/Languages
License: ASL 2.0
URL: https://www.openshift.com
Source0: https://github.com/jboss-fuse/fuse-openshift-cartridge/archive/%{github_tag}.zip
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Requires:      java-1.7.0-openjdk
Requires:      java-1.7.0-openjdk-devel
Requires:      httpd
Requires:      maven3

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Fuse cartridge for openshift.

%prep
%setup -q -n fuse-openshift-cartridge-%{github_tag}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{cartridgedir}
cp -r * %{buildroot}%{cartridgedir}/

%clean
rm -rf %{buildroot}

%post

%files
%defattr(-,root,root,-)
%dir %{cartridgedir}
%dir %{cartridgedir}/bin
%dir %{cartridgedir}/metadata
%dir %{cartridgedir}/run
%dir %{cartridgedir}/template
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{frameworkdir}
%{cartridgedir}/metadata/manifest.yml
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE


%changelog
