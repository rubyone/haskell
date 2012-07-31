# cabal2spec-0.25.4
# https://fedoraproject.org/wiki/Packaging:Haskell
# https://fedoraproject.org/wiki/PackagingDrafts/Haskell

%global pkg_name system-fileio
%global common_summary Haskell %{pkg_name} library
%global common_description A %{pkg_name} library for Haskell.


Name:           ghc-%{pkg_name}
Version:        0.3.9
Release:        1%{?dist}
Summary:        %{common_summary}
Group:          System Environment/Libraries
License:        MIT
# BEGIN cabal2spec
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz
ExclusiveArch:  %{ghc_arches}
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros %{!?without_hscolour:hscolour}
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-system-filepath-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
# END cabal2spec

%description
%{common_description}


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


# devel subpackage
%ghc_devel_package

%ghc_devel_description

%ghc_devel_post_postun

%ghc_files


%changelog
* Tue Jul 22 2012 Satoru SATOH <ssato@redhat.com> - 0.3.9-1
- New upstream release

* Thu Mar 22 2012 Satoru SATOH <ssato@redhat.com> - 0.3.7-1
- Added build requires

* Thu Mar 22 2012 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.4
