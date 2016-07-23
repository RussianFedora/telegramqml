%global origname TelegramQML

Name:           telegramqml
Version:        2.0.0
Release:        1%{?dist}
Summary:        Telegram API tools for QtQml and Qml

License:        GPLv3+
URL:            https://github.com/Aseman-Land/TelegramQML
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtquick1-devel
# Only compile-time
BuildRequires:  openssl-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  libqtelegram-ae-devel

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       qt5-qtbase-devel%{?_isa}
Requires:       qt5-qtquick1-devel%{?_isa}

%description devel
%{summary}.

%prep
%autosetup -n %{origname}-%{version}
mkdir %{_target_platform}

%build
pushd %{_target_platform}
  %qmake_qt5 .. \
      BUILD_MODE+=lib \
      CONFIG+=typeobjects \
      QMAKE_CFLAGS_ISYSTEM= \
      PREFIX=%{_prefix} \
      INSTALL_LIBS_PREFIX=%{_libdir} \
      INSTALL_HEADERS_PREFIX=%{_includedir}
popd
%make_build -C %{_target_platform}

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%changelog
* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.0.0-1
- Initial package
