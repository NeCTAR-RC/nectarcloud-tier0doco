MonARCH supports a wide range of software  packages. The Linux environment module utility is used to load and unload different software packages. When a module is loaded, it sets specific environment variables (e.g., PATH, LD_LIBRARY_PATH, etc.) to the appropriate pathnames where the software is installed.

# Environment Modules

 There may be occasions where you need to use different compilers and/or libraries from those found in your usual environment, and you therefore need to adjust your environment variables accordingly. The module command makes this easy. Some examples of its use are:

| module avail | Shows what modules are available on the system |
| --- | --- |
| module whatis | Shows what they do |
| module load openmpi-intel | Makes Intel MPI libraries and Intel Fortran compiler available |
| module list | Shows which module are loaded |
| module purge | Unloads all of them |
| module unload openmpi-intel intel | Unloads Intel MPI and Intel Fortran modules |
| module display [modulefile]Software | Use this command to see exactly what a given modulefile will do to your environment, such as what will be added to the PATH, MANPATH, etc. environment variables. |

Here is an example of how to load the GNU C/C++ compiler.

```bash

$module load gcc/4.3.5
```

That's all! Now here we put some extra Linux commands to show that, by loading
the module, we override the default System compiler.

Load the gcc compiler, showing paths and versions:

```bash
#
# show that we have the default compiler
#
$which gcc
/usr/bin/gcc
$gcc -v
Using built-in specs.
Target: x86_64-redhat-linux
Configured with: ../configure --prefix=/usr --mandir=/usr/share/man
--infodir=/usr/share/info
--enable-shared --enable-threads=posix --enable-checking=release
--with-system-zlib --enable-__cxa_atexit
--disable-libunwind-exceptions --enable-libgcj-multifile
--enable-languages=c,c++,objc,obj-c++,java,fortran,ada
--enable-java-awt=gtk --disable-dssi --enable-plugin
--with-java-home=/usr/lib/jvm/java-1.4.2-gcj-1.4.2.0/jre
--with-cpu=generic --host=x86_64-redhat-linux
Thread model: posix
gcc version 4.1.2 20080704 (Red Hat 4.1.2-46)
#
# load a different compiler
#
$module load gcc/4.3.5
#
# check that we have a new version
#
$which gcc
/opt/sw/gcc-4.3.5/bin/gcc
$gcc -v
Using built-in specs.
Target: x86_64-unknown-linux-gnu
Configured with: ../gcc-4.3.5/configure --prefix=/opt/sw/gcc-4.3.5
Thread model: posix
gcc version 4.3.5 (GCC)
```

Suppose we wanted to know more about a module we wanted to load? That can be done via the 'show' command 'module show' example

```bash
module show gcc/4.3.5

-------------------------------------------------------------------
/opt/sw/Modules/modulefiles/gcc/4.3.5:
module-whatis    GNU Compiler Collection is ...
conflict     gcc/4.8.0
conflict     gcc/4.4.4
conflict     gcc/4.5.3
conflict     intel/10.0.025
conflict     intelC/10.0.025
prepend-path PATH /opt/sw/gcc-4.3.5/bin:/opt/sw/gcc-4.3.5/libexec/gcc/x86_64-unknown-linux-gnu/4.3.5
prepend-path     LD_LIBRARY_PATH /opt/sw/gcc-4.3.5/lib64:/opt/sw/gcc-4.3.5/lib
prepend-path     MANPATH /opt/sw/gcc-4.3.5/man
-------------------------------------------------------------------
```

Suppose we wanted to use the system compiler again. All you do is unload the module.
Unload the gcc compiler

```bash
module unload gcc/4.3.5

```

Here we unload the compiler, checking that we have the right versions when finished.

Check that we load the correct compiler:

```bash
#
# unload compiler
#
$ module unload gcc/4.3.5
#
# show that we have the default compiler
#
$which gcc
/usr/bin/gcc
$gcc -v
Using built-in specs.
Target: x86_64-redhat-linux
Configured with: ../configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-libgcj-multifile --enable-languages=c,c++,objc,obj-c++,java,fortran,ada --enable-java-awt=gtk --disable-dssi --enable-plugin --with-java-home=/usr/lib/jvm/java-1.4.2-gcj-1.4.2.0/jre --with-cpu=generic --host=x86_64-redhat-linux
Thread model: posix
gcc version 4.1.2 20080704 (Red Hat 4.1.2-46)
```

An advantage of using the module command is that it warns you about conflicting packages.  You can't load two different gcc compilers at the same time!

```bash
$ module load gcc/4.3.5
$ module load gcc/4.2.3
gcc/4.2.3(15):ERROR:150:    Module 'gcc/4.2.3' conflicts with the currently loaded module(s) 'gcc/4.3.5'
gcc/4.2.3(15):ERROR:102:    Tcl command execution failed: conflict gcc/4.3.5
```

Note. Some modules load other modules! Also, if the software is licensed,
loading a module does not mean you will be allowed access to it.  Please  email
mcc-help@monash.edu to gain access to proprietary software. Here, loading the
vasp module will not allow you access to it.

Example of 'module list':

```bash
module list
Currently Loaded Modulefiles:
  1) gcc/4.3.5               3) mpfr/2.4.2              5) openmpi/1.6-gcc-4.5.3   7) vasp/5.3.2-2D
  2) gmp/4.3.2               4) mpc/0.9                 6) fftw/3.2.2-openmp
```

If you do not explicitly give a version number, module will use the default module.

Example of 'module display'

```bash
module display gcc
-------------------------------------------------------------------
/opt/sw/Modules/modulefiles/gcc/4.4.4:


                module-whatis     GNU Compiler Collection is ...
                module         load gmp mpfr
                conflict     gcc/4.8.0
                conflict     gcc/4.3.5
                conflict     gcc/4.5.3
                conflict     intel/10.0.025
                conflict     intelC/10.0.025
                prepend-path    PATH/opt/sw/gcc-4.4.4/bin:/opt/sw/gcc-4.4.4/libexec/gcc/x86_64-unknown-linux-gnu/4.4.4
                prepend-path    LD_LIBRARY_PATH /opt/sw/gcc-4.4.4//lib64
                prepend-path    MANPATH /opt/sw/gcc-4.4.4//man
                -------------------------------------------------------------------
```

This is the output of 'module avail'.  You can interrogate any module with the commands listed above.
Output of 'module avail'

```bash
module avail
------------------------------ /usr/share/Modules/modulefiles -------------------------------
dot                    matlab-compiler/R2011a module-info            null
matlab/R2011a-local    module-cvs             modules                use.own

------------------------------ /opt/sw/Modules/modulefiles ----------------------------------
FEniCS/1.0                         fluent/proto                       libctl/3.0.3(default)
Mesa/7.0.1(default)                freeglut/2.6.0                     libctl/3.1
Mesa/7.0.2                         freeimage/3.13.1                   libctl/3.2.1
Mesa/7.2                           freesurfer/5.0.0                   libxc/2.0.2
OpenBUGS/3.1.1                     fsc/1.1.2                          libxml2/2.7.2
OpenCV/2.2.0                       fsl/4.0.2                          macmolplt/7.4.2
Qt/3.3.8b                          fsl/4.1.0-test                     mallet/2.0.7
Qt/4.2.3                           fsl/4.1.5                          ...
...
```
