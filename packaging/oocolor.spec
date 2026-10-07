Name:           oocolor
Version:        0.1.0
Release:        1%{?dist}
Summary:        Converts between HEX, RGB, HSL, CMYK, and ANSI 256 color representations.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oocolor
Source0:        oocolor-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oocolor is a sovereign, capability-bounded COLOR CONVERTER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oocolor
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oocolor-uninstall

%files
/usr/bin/oocolor
/usr/bin/oocolor-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
