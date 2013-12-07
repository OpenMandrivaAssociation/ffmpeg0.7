%define oname	ffmpeg
%define version	0.7.13
%define release  5
%define major	52

%define libname %mklibname %oname %major
%define develname %mklibname %name -d
%define staticname %mklibname %name -s -d

%define avfmajor 52
%define avflibname %mklibname avformats %avfmajor
%define postprocmajor 51
%define postproclibname %mklibname postproc %postprocmajor

%define avumajor 50
%define avulibname %mklibname avutil %avumajor
%define swsmajor 0
%define swslibname %mklibname swscaler %swsmajor

%define filtermajor 1
%define filterlibname %mklibname avfilter %filtermajor

%define build_swscaler 1
%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define distsuffix plf
%if %mdvver >= 201100
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif
%endif
%define build_faac	0
%{?_with_faac: %{expand: %%global build_faac 1}}
%{?_without_faac: %{expand: %%global build_faac 0}}
Name: 	 	%{oname}0.7
Version: 	%{version}
Release: 	%{release}%{?extrarelsuffix}
Summary: 	Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder
Source0: 	http://ffmpeg.org/releases/%{oname}-%version.tar.bz2
%if %build_plf
License: 	GPLv3+
%else
License: 	GPLv2+
%endif
Group: 	 	Video
BuildRequires:  texi2html
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	jackit-devel
BuildRequires:	pkgconfig(libdc1394-2)
BuildRequires:	pkgconfig(schroedinger-1.0)
BuildRequires:	pkgconfig(vpx)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	bzip2-devel
BuildRequires:	rtmp-devel
BuildRequires:	yasm
%if %{mdkversion} >= 200900
BuildRequires:	vdpau-devel
%endif
%if %{mdkversion} >= 200910
BuildRequires:	pkgconfig(libva)
%endif
URL:		http://ffmpeg.org/
%if %build_plf
BuildRequires: x264-devel >= 0.115
BuildRequires: liblame-devel
BuildRequires: opencore-amr-devel
%endif
%if %build_faac
BuildRequires: faac-devel = 1:1.28-6
%endif
Requires:	%postproclibname >= %version-%release
Requires:	%libname = %version-%release
Requires:	%avflibname = %version-%release
Requires:	%avulibname = %version-%release
%if %build_swscaler
Requires:       %{swslibname} = %{version}-%release
%endif

%description
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

%if %build_plf
This package is in PLF as it violates several patents.
%endif

%package -n %{libname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg
Provides:       libffmpeg = %{version}-%{release}

%description -n %{libname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n %{postproclibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg
Conflicts: %mklibname ffmpeg 51

%description -n %{postproclibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.


%package -n %{avflibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg

%description -n %{avflibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n %{avulibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg

%description -n %{avulibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n %{swslibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg
Requires:	%{avulibname} = %{version}-%release

%description -n %{swslibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n %{filterlibname}
Group:          System/Libraries
Summary:        Shared library part of ffmpeg

%description -n %{filterlibname}
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg if you want to encode multimedia streams.

%package -n %develname
Group:          Development/C
Summary:        Header files for the ffmpeg codec library
Requires:       %{libname} = %{version}-%release
Requires:       %{avflibname} = %{version}-%release
Requires:       %{avulibname} = %{version}-%release
Requires:       %{postproclibname} >= %{version}-%release
%if %build_swscaler
Requires:       %{swslibname} = %{version}-%release
%endif
Requires:	%{filterlibname} = %{version}-%release
Provides:	ffmpeg0.7-devel = %{version}-%{release}
Obsoletes: %mklibname -d %oname 51
Conflicts: %mklibname -d %oname

%description -n %develname
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg-devel if you want to compile apps with ffmpeg support.

%package -n %staticname
Group:          Development/C
Summary:        Static library for the ffmpeg codec library
Requires:       %develname = %{version}-%release
Provides:       ffmpeg0.7-static-devel = %{version}-%{release}
Obsoletes: %mklibname -s -d %oname 51
Conflicts: %mklibname -s -d %oname

%description -n %staticname
ffmpeg is a hyper fast realtime audio/video encoder, a streaming  server
and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it into
several file formats based on DCT/motion compensation encoding. Sound is
compressed in MPEG audio layer 2 or using an AC3 compatible stream.

Install libffmpeg-devel if you want to compile apps with ffmpeg support.

%prep

%setup -q -n %{oname}-%version

%build
%define Werror_cflags %nil
export CFLAGS="%optflags -FPIC"
export LDFLAGS="%{ldflags}"

./configure --prefix=%_prefix \
	--enable-shared \
	--libdir=%{_libdir} \
	--shlibdir=%{_libdir} \
	--incdir=%{_includedir} \
	--disable-stripping \
	--enable-postproc \
	--enable-gpl \
	--enable-pthreads \
	--enable-libtheora \
	--enable-libvorbis --disable-encoder=vorbis \
	--enable-libvpx \
	--enable-x11grab \
	--enable-runtime-cpudetect \
	--enable-libdc1394 \
	--enable-libschroedinger \
	--enable-librtmp \
%if %build_plf
	--enable-libmp3lame \
	--enable-libopencore-amrnb \
	--enable-libopencore-amrwb \
	--enable-version3 \
	--enable-libx264 \
%else
	--disable-decoder=aac --disable-encoder=aac \
%endif
%if %build_faac
	--enable-nonfree --enable-libfaac
%endif

%make

%install
rm -rf %{buildroot}

%makeinstall_std SRC_PATH=`pwd`

# compat symlink
install -d %buildroot/%_libdir/libavcodec
pushd %buildroot/%_libdir/libavcodec && ln -sf ../libavcodec.a && popd
install -d %buildroot/%_libdir/libavformat
pushd %buildroot/%_libdir/libavformat && ln -sf ../libavformat.a && popd

#gw don't package these:
rm -rf %buildroot{%_bindir,%_mandir/man1,%_datadir/%oname}
#gw same major as in ffmpeg 0.8.x, use that one instead
#rm -f %buildroot%{_libdir}/libpostproc.so.%{postprocmajor}*

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libavcodec.so.%{major}*

%files -n %postproclibname
%defattr(-,root,root)
%{_libdir}/libpostproc.so.%{postprocmajor}*

%files -n %{avflibname}
%defattr(-,root,root)
%{_libdir}/libavformat.so.%{avfmajor}*
%{_libdir}/libavdevice.so.%{avfmajor}*

%files -n %{avulibname}
%defattr(-,root,root)
%{_libdir}/libavutil.so.%{avumajor}*

%if %build_swscaler
%files -n %{swslibname}
%defattr(-,root,root)
%{_libdir}/libswscale.so.%{swsmajor}*
%endif

%files -n %{filterlibname}
%defattr(-,root,root)
%{_libdir}/libavfilter.so.%{filtermajor}*

%files -n %develname
%defattr(-,root,root)
%doc INSTALL README doc/*.html doc/*.txt doc/TODO doc/*.conf
%{_includedir}/libavcodec
%{_includedir}/libavdevice
%{_includedir}/libavformat
%{_includedir}/libavutil
%{_includedir}/libpostproc
%{_includedir}/libavfilter
%{_libdir}/libavcodec.so
%{_libdir}/libavdevice.so
%{_libdir}/libavformat.so
%{_libdir}/libavutil.so
%{_libdir}/libpostproc.so
%{_libdir}/libavfilter.so
%if %build_swscaler
%{_libdir}/libswscale.so
%{_includedir}/libswscale
%_libdir/pkgconfig/libswscale.pc
%endif
%_libdir/pkgconfig/libavcodec.pc
%_libdir/pkgconfig/libavdevice.pc
%_libdir/pkgconfig/libavformat.pc
%_libdir/pkgconfig/libavutil.pc
%_libdir/pkgconfig/libpostproc.pc
%_libdir/pkgconfig/libavfilter.pc

%files -n %staticname
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/libavformat/*a
%{_libdir}/libavcodec/*a


%changelog
* Thu Jul 19 2012 Götz Waschk <waschk@mandriva.org> 0.7.13-1mdv2012.0
+ Revision: 810241
- update build deps for jack
- update to new version 0.7.13

* Tue Nov 22 2011 Götz Waschk <waschk@mandriva.org> 0.7.8-1
+ Revision: 732681
- new version

* Sun Nov 06 2011 Götz Waschk <waschk@mandriva.org> 0.7.7-2
+ Revision: 722686
- make devel package installable

* Sun Nov 06 2011 Götz Waschk <waschk@mandriva.org> 0.7.7-1
+ Revision: 722588
- new version
- fork ffmpeg 0.7 API version
- branch 0.7.x
- update to new version 0.7.5
- bump x264 dep
- remove obsolete faad option
- rebuild
- build with librtmp (bug #60225)
- rebuild for new libva
- new version 0.6
- drop patch 2
- build with vp8 support
- disable internal vorbis encoder (bug #59797)
- disable AAC decoder and encoder
- rebuild
- new snapshot
- drop patch 2
- bump x264 dep
- add more deps to the main package (gc)
- new snapshot
- fix x264 build
- bump x264 dep
- new snapshot
- drop imgresample patch, the old API is now gone
- new major
- replace amr by openamr
- disable faac support
- update build deps
- update license
- fix source URL
- new version
- new snapshot
- rediff patch 0
- new snapshot
- rediff patch 0
- drop patch 2
- disable parallel build
- rediff the patch again
- new snapshot
- fix format strings
- update file list
- new snapshot
- explicit dep on libpostproc to fix upgrades
- spec cleanup
- bump x264 dep
- new snapshot
- add conflict with old ffmpeg package to libpostproc
- new snapshot
- new major
- split out libpostproc
- changes recommended upstream:
 * disable external libnut support
 * drop liba52dec, xvid
- new snapshot
- remove mpegaudio.h again
- new snapshot
- update patch 0
- add missing headers requested in bug #41949
- new snapshot
- reenable deprecated libavcodec image scaler for vlc
- bump for build system trouble
- new snapshot
- reenable swscaler
- fix header file conflict
- new version
- drop dirac support
- fix build
- update file list
- update license tag
- disable amr_nb and amr_wb in PLF, it would make the build undistributable
- enable vorbis and theora
- new version
- update dirac deps
- update dirac patch
- fix pkgconfig file generated by dirac patch
- new version
- fix versioned deps between the packages, the important part is the release
- new version
- bump avformat major
- add libavdevice
- rediff patch 3
- new version
- drop patch 0
- fix dirac patch to correctly generate the pkgconfig files
- new devel name
- fix configure options
- new version
- patch0: build fix
- update dirac patch
- update deps
- new version
- patch for dirac support
- fix buildrequires
- drop merged patch 2
- drop amr source, support using external libamrnb instead

  + mandrake <mandrake@mandriva.com>
    - %repsys markrelease
      version: 0.7.5
      release: 1
      revision: 701925
      Copying 0.7.5-1 to releases/ directory.

  + Funda Wang <fwang@mandriva.org>
    - br yasm
    - new versinon 0.7.1
    - new version 0.6.3
    - update br
    - rebuild
    - new version 0.6.1
    - add BR for more encoders

  + Anssi Hannula <anssi@mandriva.org>
    - plf: append "plf" to Release on cooker to make plf build have higher EVR
      again with the rpm5-style mkrel now in use
    - build with vaapi support
    - fix debug packages (stripping happened too early)
    - fix a regression causing wrong fourcc selection for VP6F remuxing
      (ffmpeg-move-vp6f-up.patch)
    - build with vdpau support on 2009.0+ (BR vdpau-devel)
    - build_amr option (disabled by default) needs --enable-nonfree
    - update reenable-imgresample.patch so that duplicate sws_ symbols are
      omitted from libavcodec (from Debian adaptation of the patch)
    - drop now unneeded ffplay-uses-xlib.patch (ffplay only uses SDL)
    - set --incdir explicitely so that pkg-config files get generated
      correctly
    - use --shlibdir instead of move hack for lib64
    - fix pkgconfig requires for dirac

  + Emmanuel Andry <eandry@mandriva.org>
    - enable cpu detection at run time
    - enable schroedinger and firewire support
    - New svn snapshot
    - New svn snapshot
    - New svn snapshot

  + Oden Eriksson <oeriksson@mandriva.com>
    - new url
    - rediffed one fuzzy patch
    - use %%ldflags and fix linkage (P1)

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - build with -fPIC (#35955)
    - kill re-definition of %%buildroot on Pixel's request

