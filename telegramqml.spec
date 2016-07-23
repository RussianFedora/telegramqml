%global origname TelegramQML

%if 0%{?fedora} <= 24
%global _qt5_qmldir %{_qt5_archdatadir}/qml
%endif

Name:           telegramqml
Version:        2.0.0
Release:        1%{?dist}
Summary:        Telegram API tools for QtQml and Qml

License:        GPLv3+
URL:            https://github.com/Aseman-Land/TelegramQML
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
# Only compile-time
BuildRequires:  openssl-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  libqtelegram-ae-devel

%description
%{summary}.

%prep
%autosetup -n %{origname}-%{version}
mkdir %{_target_platform}

%build
pushd %{_target_platform}
  %qmake_qt5 QMAKE_CFLAGS_ISYSTEM= ..
popd
%make_build -C %{_target_platform}

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

%files
%license LICENSE
%{_qt5_qmldir}/TelegramQml/

%changelog
* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.0.0-1
- Initial package
