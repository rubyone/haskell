# cabal2spec-0.25
# https://fedoraproject.org/wiki/Packaging:Haskell
# https://fedoraproject.org/wiki/PackagingDrafts/Haskell

%global pkg_name yaml
%global common_summary Haskell %{pkg_name} library
%global common_description A %{pkg_name} library for Haskell to provides support for parsing and emitting Yaml documents. 

Name:           ghc-%{pkg_name}
Version:        0.7.0.3
# Not yet as conduit >= 0.5.x is not available in Fedora yet:
#Version:        0.8.0
Release:        1%{?dist}
Summary:        %{common_summary}
Group:          System Environment/Libraries
License:        BSD
# BEGIN cabal2spec
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz
ExclusiveArch:  %{ghc_arches}
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros %{!?without_hscolour:hscolour}
# END cabal2spec
BuildRequires:  ghc-aeson-devel >= 0.5
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel >= 0.9.1.4
BuildRequires:  ghc-conduit-devel >= 0.4.0
# Not available in Fedora yet:
#BuildRequires:  ghc-conduit-devel >= 0.5.0
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-resourcet-devel >= 0.3.0
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel


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

%ghc_files LICENSE


%changelog
* Mon Jul  9 2012 Satoru SATOH <ssato@redhat.com> - 0.8.0-1
- Added build-time dependencies

* Mon Jul  9 2012 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.5
