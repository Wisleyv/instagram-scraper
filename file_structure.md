# Project Structure 
 
``` 
Listagem de caminhos de pasta para o volume Windows-SSD
O n�mero de s�rie do volume � E42D-6517
C:\DEV\LUANNY
|   .env
|   .env.example
|   .gitattributes
|   .gitignore
|   file_structure.md
|   get_tree.bat
|   investigate_alt.py
|   Luanny.code-workspace
|   Luanny.spec
|   Projeto Luanny - Implementa��o.md
|   Projeto Luanny - Implementa��o.pdf
|   Projeto Luanny(embri�o).pdf
|   pyproject.toml
|   README.md
|   storage_state.json
|   test_extractor.py
|   test_links.py
|   test_parents.py
|   test_scroll.py
|   
+---.pytest_cache
|   |   .gitignore
|   |   CACHEDIR.TAG
|   |   README.md
|   |   
|   \---v
|       \---cache
|               lastfailed
|               nodeids
|               
+---.venv
|   |   pyvenv.cfg
|   |   
|   +---Include
|   |   \---site
|   |       \---python3.10
|   |           \---greenlet
|   |                   greenlet.h
|   |                   
|   +---Lib
|   |   \---site-packages
|   |       |   a1_coverage.pth
|   |       |   distutils-precedence.pth
|   |       |   numpy-2.2.6-cp310-cp310-win_amd64.whl
|   |       |   py.py
|   |       |   six.py
|   |       |   typing_extensions.py
|   |       |   _editable_impl_luanny.pth
|   |       |   
|   |       +---annotated_doc
|   |       |   |   main.py
|   |       |   |   py.typed
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           main.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---annotated_doc-0.0.4.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---annotated_types
|   |       |   |   py.typed
|   |       |   |   test_cases.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           test_cases.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---annotated_types-0.7.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---backports
|   |       |   \---asyncio
|   |       |       \---runner
|   |       |           |   py.typed
|   |       |           |   runner.py
|   |       |           |   runner.pyi
|   |       |           |   tasks.py
|   |       |           |   _int_to_enum.py
|   |       |           |   _patch.py
|   |       |           |   __init__.py
|   |       |           |   
|   |       |           \---__pycache__
|   |       |                   runner.cpython-310.pyc
|   |       |                   tasks.cpython-310.pyc
|   |       |                   _int_to_enum.cpython-310.pyc
|   |       |                   _patch.cpython-310.pyc
|   |       |                   __init__.cpython-310.pyc
|   |       |                   
|   |       +---backports_asyncio_runner-1.2.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE.md
|   |       |           
|   |       +---click
|   |       |   |   core.py
|   |       |   |   decorators.py
|   |       |   |   exceptions.py
|   |       |   |   formatting.py
|   |       |   |   globals.py
|   |       |   |   parser.py
|   |       |   |   py.typed
|   |       |   |   shell_completion.py
|   |       |   |   termui.py
|   |       |   |   testing.py
|   |       |   |   types.py
|   |       |   |   utils.py
|   |       |   |   _compat.py
|   |       |   |   _termui_impl.py
|   |       |   |   _textwrap.py
|   |       |   |   _utils.py
|   |       |   |   _winconsole.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           core.cpython-310.pyc
|   |       |           decorators.cpython-310.pyc
|   |       |           exceptions.cpython-310.pyc
|   |       |           formatting.cpython-310.pyc
|   |       |           globals.cpython-310.pyc
|   |       |           parser.cpython-310.pyc
|   |       |           shell_completion.cpython-310.pyc
|   |       |           termui.cpython-310.pyc
|   |       |           testing.cpython-310.pyc
|   |       |           types.cpython-310.pyc
|   |       |           utils.cpython-310.pyc
|   |       |           _compat.cpython-310.pyc
|   |       |           _termui_impl.cpython-310.pyc
|   |       |           _textwrap.cpython-310.pyc
|   |       |           _utils.cpython-310.pyc
|   |       |           _winconsole.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---click-8.3.2.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE.txt
|   |       |           
|   |       +---colorama
|   |       |   |   ansi.py
|   |       |   |   ansitowin32.py
|   |       |   |   initialise.py
|   |       |   |   win32.py
|   |       |   |   winterm.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---tests
|   |       |   |   |   ansitowin32_test.py
|   |       |   |   |   ansi_test.py
|   |       |   |   |   initialise_test.py
|   |       |   |   |   isatty_test.py
|   |       |   |   |   utils.py
|   |       |   |   |   winterm_test.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           ansitowin32_test.cpython-310.pyc
|   |       |   |           ansi_test.cpython-310.pyc
|   |       |   |           initialise_test.cpython-310.pyc
|   |       |   |           isatty_test.cpython-310.pyc
|   |       |   |           utils.cpython-310.pyc
|   |       |   |           winterm_test.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           ansi.cpython-310.pyc
|   |       |           ansitowin32.cpython-310.pyc
|   |       |           initialise.cpython-310.pyc
|   |       |           win32.cpython-310.pyc
|   |       |           winterm.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---colorama-0.4.6.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE.txt
|   |       |           
|   |       +---coverage
|   |       |   |   annotate.py
|   |       |   |   bytecode.py
|   |       |   |   cmdline.py
|   |       |   |   collector.py
|   |       |   |   config.py
|   |       |   |   context.py
|   |       |   |   control.py
|   |       |   |   core.py
|   |       |   |   data.py
|   |       |   |   debug.py
|   |       |   |   disposition.py
|   |       |   |   env.py
|   |       |   |   exceptions.py
|   |       |   |   execfile.py
|   |       |   |   files.py
|   |       |   |   html.py
|   |       |   |   inorout.py
|   |       |   |   jsonreport.py
|   |       |   |   lcovreport.py
|   |       |   |   misc.py
|   |       |   |   multiproc.py
|   |       |   |   numbits.py
|   |       |   |   parser.py
|   |       |   |   patch.py
|   |       |   |   phystokens.py
|   |       |   |   plugin.py
|   |       |   |   plugin_support.py
|   |       |   |   pth_file.py
|   |       |   |   py.typed
|   |       |   |   python.py
|   |       |   |   pytracer.py
|   |       |   |   regions.py
|   |       |   |   report.py
|   |       |   |   report_core.py
|   |       |   |   results.py
|   |       |   |   sqldata.py
|   |       |   |   sqlitedb.py
|   |       |   |   sysmon.py
|   |       |   |   templite.py
|   |       |   |   tomlconfig.py
|   |       |   |   tracer.cp310-win_amd64.pyd
|   |       |   |   tracer.pyi
|   |       |   |   types.py
|   |       |   |   version.py
|   |       |   |   xmlreport.py
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   +---htmlfiles
|   |       |   |       coverage_html.js
|   |       |   |       favicon_32.png
|   |       |   |       index.html
|   |       |   |       keybd_closed.png
|   |       |   |       pyfile.html
|   |       |   |       style.css
|   |       |   |       style.scss
|   |       |   |       
|   |       |   \---__pycache__
|   |       |           annotate.cpython-310.pyc
|   |       |           bytecode.cpython-310.pyc
|   |       |           cmdline.cpython-310.pyc
|   |       |           collector.cpython-310.pyc
|   |       |           config.cpython-310.pyc
|   |       |           context.cpython-310.pyc
|   |       |           control.cpython-310.pyc
|   |       |           core.cpython-310.pyc
|   |       |           data.cpython-310.pyc
|   |       |           debug.cpython-310.pyc
|   |       |           disposition.cpython-310.pyc
|   |       |           env.cpython-310.pyc
|   |       |           exceptions.cpython-310.pyc
|   |       |           execfile.cpython-310.pyc
|   |       |           files.cpython-310.pyc
|   |       |           html.cpython-310.pyc
|   |       |           inorout.cpython-310.pyc
|   |       |           jsonreport.cpython-310.pyc
|   |       |           lcovreport.cpython-310.pyc
|   |       |           misc.cpython-310.pyc
|   |       |           multiproc.cpython-310.pyc
|   |       |           numbits.cpython-310.pyc
|   |       |           parser.cpython-310.pyc
|   |       |           patch.cpython-310.pyc
|   |       |           phystokens.cpython-310.pyc
|   |       |           plugin.cpython-310.pyc
|   |       |           plugin_support.cpython-310.pyc
|   |       |           pth_file.cpython-310.pyc
|   |       |           python.cpython-310.pyc
|   |       |           pytracer.cpython-310.pyc
|   |       |           regions.cpython-310.pyc
|   |       |           report.cpython-310.pyc
|   |       |           report_core.cpython-310.pyc
|   |       |           results.cpython-310.pyc
|   |       |           sqldata.cpython-310.pyc
|   |       |           sqlitedb.cpython-310.pyc
|   |       |           sysmon.cpython-310.pyc
|   |       |           templite.cpython-310.pyc
|   |       |           tomlconfig.cpython-310.pyc
|   |       |           types.cpython-310.pyc
|   |       |           version.cpython-310.pyc
|   |       |           xmlreport.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           __main__.cpython-310.pyc
|   |       |           
|   |       +---coverage-7.13.5.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE.txt
|   |       |           
|   |       +---dateutil
|   |       |   |   easter.py
|   |       |   |   relativedelta.py
|   |       |   |   rrule.py
|   |       |   |   tzwin.py
|   |       |   |   utils.py
|   |       |   |   _common.py
|   |       |   |   _version.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---parser
|   |       |   |   |   isoparser.py
|   |       |   |   |   _parser.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           isoparser.cpython-310.pyc
|   |       |   |           _parser.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---tz
|   |       |   |   |   tz.py
|   |       |   |   |   win.py
|   |       |   |   |   _common.py
|   |       |   |   |   _factories.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           tz.cpython-310.pyc
|   |       |   |           win.cpython-310.pyc
|   |       |   |           _common.cpython-310.pyc
|   |       |   |           _factories.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---zoneinfo
|   |       |   |   |   dateutil-zoneinfo.tar.gz
|   |       |   |   |   rebuild.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           rebuild.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           easter.cpython-310.pyc
|   |       |           relativedelta.cpython-310.pyc
|   |       |           rrule.cpython-310.pyc
|   |       |           tzwin.cpython-310.pyc
|   |       |           utils.cpython-310.pyc
|   |       |           _common.cpython-310.pyc
|   |       |           _version.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---dotenv
|   |       |   |   cli.py
|   |       |   |   ipython.py
|   |       |   |   main.py
|   |       |   |   parser.py
|   |       |   |   py.typed
|   |       |   |   variables.py
|   |       |   |   version.py
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           cli.cpython-310.pyc
|   |       |           ipython.cpython-310.pyc
|   |       |           main.cpython-310.pyc
|   |       |           parser.cpython-310.pyc
|   |       |           variables.cpython-310.pyc
|   |       |           version.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           __main__.cpython-310.pyc
|   |       |           
|   |       +---exceptiongroup
|   |       |   |   py.typed
|   |       |   |   _catch.py
|   |       |   |   _exceptions.py
|   |       |   |   _formatting.py
|   |       |   |   _suppress.py
|   |       |   |   _version.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           _catch.cpython-310.pyc
|   |       |           _exceptions.cpython-310.pyc
|   |       |           _formatting.cpython-310.pyc
|   |       |           _suppress.cpython-310.pyc
|   |       |           _version.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---exceptiongroup-1.3.1.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---greenlet
|   |       |   |   CObjects.cpp
|   |       |   |   greenlet.cpp
|   |       |   |   greenlet.h
|   |       |   |   greenlet_allocator.hpp
|   |       |   |   greenlet_compiler_compat.hpp
|   |       |   |   greenlet_cpython_compat.hpp
|   |       |   |   greenlet_exceptions.hpp
|   |       |   |   greenlet_internal.hpp
|   |       |   |   greenlet_msvc_compat.hpp
|   |       |   |   greenlet_refs.hpp
|   |       |   |   greenlet_slp_switch.hpp
|   |       |   |   greenlet_thread_support.hpp
|   |       |   |   PyGreenlet.cpp
|   |       |   |   PyGreenlet.hpp
|   |       |   |   PyGreenletUnswitchable.cpp
|   |       |   |   PyModule.cpp
|   |       |   |   slp_platformselect.h
|   |       |   |   TBrokenGreenlet.cpp
|   |       |   |   TExceptionState.cpp
|   |       |   |   TGreenlet.cpp
|   |       |   |   TGreenlet.hpp
|   |       |   |   TGreenletGlobals.cpp
|   |       |   |   TMainGreenlet.cpp
|   |       |   |   TPythonState.cpp
|   |       |   |   TStackState.cpp
|   |       |   |   TThreadState.hpp
|   |       |   |   TThreadStateCreator.hpp
|   |       |   |   TThreadStateDestroy.cpp
|   |       |   |   TUserGreenlet.cpp
|   |       |   |   _greenlet.cp310-win_amd64.pyd
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---platform
|   |       |   |   |   setup_switch_x64_masm.cmd
|   |       |   |   |   switch_aarch64_gcc.h
|   |       |   |   |   switch_alpha_unix.h
|   |       |   |   |   switch_amd64_unix.h
|   |       |   |   |   switch_arm32_gcc.h
|   |       |   |   |   switch_arm32_ios.h
|   |       |   |   |   switch_arm64_masm.asm
|   |       |   |   |   switch_arm64_masm.obj
|   |       |   |   |   switch_arm64_msvc.h
|   |       |   |   |   switch_csky_gcc.h
|   |       |   |   |   switch_loongarch64_linux.h
|   |       |   |   |   switch_m68k_gcc.h
|   |       |   |   |   switch_mips_unix.h
|   |       |   |   |   switch_ppc64_aix.h
|   |       |   |   |   switch_ppc64_linux.h
|   |       |   |   |   switch_ppc_aix.h
|   |       |   |   |   switch_ppc_linux.h
|   |       |   |   |   switch_ppc_macosx.h
|   |       |   |   |   switch_ppc_unix.h
|   |       |   |   |   switch_riscv_unix.h
|   |       |   |   |   switch_s390_unix.h
|   |       |   |   |   switch_sh_gcc.h
|   |       |   |   |   switch_sparc_sun_gcc.h
|   |       |   |   |   switch_x32_unix.h
|   |       |   |   |   switch_x64_masm.asm
|   |       |   |   |   switch_x64_masm.obj
|   |       |   |   |   switch_x64_msvc.h
|   |       |   |   |   switch_x86_msvc.h
|   |       |   |   |   switch_x86_unix.h
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---tests
|   |       |   |   |   fail_clearing_run_switches.py
|   |       |   |   |   fail_cpp_exception.py
|   |       |   |   |   fail_initialstub_already_started.py
|   |       |   |   |   fail_slp_switch.py
|   |       |   |   |   fail_switch_three_greenlets.py
|   |       |   |   |   fail_switch_three_greenlets2.py
|   |       |   |   |   fail_switch_two_greenlets.py
|   |       |   |   |   leakcheck.py
|   |       |   |   |   test_contextvars.py
|   |       |   |   |   test_cpp.py
|   |       |   |   |   test_extension_interface.py
|   |       |   |   |   test_gc.py
|   |       |   |   |   test_generator.py
|   |       |   |   |   test_generator_nested.py
|   |       |   |   |   test_greenlet.py
|   |       |   |   |   test_greenlet_trash.py
|   |       |   |   |   test_interpreter_shutdown.py
|   |       |   |   |   test_leaks.py
|   |       |   |   |   test_stack_saved.py
|   |       |   |   |   test_throw.py
|   |       |   |   |   test_tracing.py
|   |       |   |   |   test_version.py
|   |       |   |   |   test_weakref.py
|   |       |   |   |   _test_extension.c
|   |       |   |   |   _test_extension.cp310-win_amd64.pyd
|   |       |   |   |   _test_extension_cpp.cp310-win_amd64.pyd
|   |       |   |   |   _test_extension_cpp.cpp
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           fail_clearing_run_switches.cpython-310.pyc
|   |       |   |           fail_cpp_exception.cpython-310.pyc
|   |       |   |           fail_initialstub_already_started.cpython-310.pyc
|   |       |   |           fail_slp_switch.cpython-310.pyc
|   |       |   |           fail_switch_three_greenlets.cpython-310.pyc
|   |       |   |           fail_switch_three_greenlets2.cpython-310.pyc
|   |       |   |           fail_switch_two_greenlets.cpython-310.pyc
|   |       |   |           leakcheck.cpython-310.pyc
|   |       |   |           test_contextvars.cpython-310.pyc
|   |       |   |           test_cpp.cpython-310.pyc
|   |       |   |           test_extension_interface.cpython-310.pyc
|   |       |   |           test_gc.cpython-310.pyc
|   |       |   |           test_generator.cpython-310.pyc
|   |       |   |           test_generator_nested.cpython-310.pyc
|   |       |   |           test_greenlet.cpython-310.pyc
|   |       |   |           test_greenlet_trash.cpython-310.pyc
|   |       |   |           test_interpreter_shutdown.cpython-310.pyc
|   |       |   |           test_leaks.cpython-310.pyc
|   |       |   |           test_stack_saved.cpython-310.pyc
|   |       |   |           test_throw.cpython-310.pyc
|   |       |   |           test_tracing.cpython-310.pyc
|   |       |   |           test_version.cpython-310.pyc
|   |       |   |           test_weakref.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---greenlet-3.4.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           LICENSE.PSF
|   |       |           
|   |       +---iniconfig
|   |       |   |   exceptions.py
|   |       |   |   py.typed
|   |       |   |   _parse.py
|   |       |   |   _version.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           exceptions.cpython-310.pyc
|   |       |           _parse.cpython-310.pyc
|   |       |           _version.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---iniconfig-2.3.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---luanny-0.1.0.dist-info
|   |       |       direct_url.json
|   |       |       entry_points.txt
|   |       |       INSTALLER
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       WHEEL
|   |       |       
|   |       +---markdown_it
|   |       |   |   main.py
|   |       |   |   parser_block.py
|   |       |   |   parser_core.py
|   |       |   |   parser_inline.py
|   |       |   |   port.yaml
|   |       |   |   py.typed
|   |       |   |   renderer.py
|   |       |   |   ruler.py
|   |       |   |   token.py
|   |       |   |   tree.py
|   |       |   |   utils.py
|   |       |   |   _compat.py
|   |       |   |   _punycode.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---cli
|   |       |   |   |   parse.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           parse.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---common
|   |       |   |   |   entities.py
|   |       |   |   |   html_blocks.py
|   |       |   |   |   html_re.py
|   |       |   |   |   normalize_url.py
|   |       |   |   |   utils.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           entities.cpython-310.pyc
|   |       |   |           html_blocks.cpython-310.pyc
|   |       |   |           html_re.cpython-310.pyc
|   |       |   |           normalize_url.cpython-310.pyc
|   |       |   |           utils.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---helpers
|   |       |   |   |   parse_link_destination.py
|   |       |   |   |   parse_link_label.py
|   |       |   |   |   parse_link_title.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           parse_link_destination.cpython-310.pyc
|   |       |   |           parse_link_label.cpython-310.pyc
|   |       |   |           parse_link_title.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---presets
|   |       |   |   |   commonmark.py
|   |       |   |   |   default.py
|   |       |   |   |   zero.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           commonmark.cpython-310.pyc
|   |       |   |           default.cpython-310.pyc
|   |       |   |           zero.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---rules_block
|   |       |   |   |   blockquote.py
|   |       |   |   |   code.py
|   |       |   |   |   fence.py
|   |       |   |   |   heading.py
|   |       |   |   |   hr.py
|   |       |   |   |   html_block.py
|   |       |   |   |   lheading.py
|   |       |   |   |   list.py
|   |       |   |   |   paragraph.py
|   |       |   |   |   reference.py
|   |       |   |   |   state_block.py
|   |       |   |   |   table.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           blockquote.cpython-310.pyc
|   |       |   |           code.cpython-310.pyc
|   |       |   |           fence.cpython-310.pyc
|   |       |   |           heading.cpython-310.pyc
|   |       |   |           hr.cpython-310.pyc
|   |       |   |           html_block.cpython-310.pyc
|   |       |   |           lheading.cpython-310.pyc
|   |       |   |           list.cpython-310.pyc
|   |       |   |           paragraph.cpython-310.pyc
|   |       |   |           reference.cpython-310.pyc
|   |       |   |           state_block.cpython-310.pyc
|   |       |   |           table.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---rules_core
|   |       |   |   |   block.py
|   |       |   |   |   inline.py
|   |       |   |   |   linkify.py
|   |       |   |   |   normalize.py
|   |       |   |   |   replacements.py
|   |       |   |   |   smartquotes.py
|   |       |   |   |   state_core.py
|   |       |   |   |   text_join.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           block.cpython-310.pyc
|   |       |   |           inline.cpython-310.pyc
|   |       |   |           linkify.cpython-310.pyc
|   |       |   |           normalize.cpython-310.pyc
|   |       |   |           replacements.cpython-310.pyc
|   |       |   |           smartquotes.cpython-310.pyc
|   |       |   |           state_core.cpython-310.pyc
|   |       |   |           text_join.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---rules_inline
|   |       |   |   |   autolink.py
|   |       |   |   |   backticks.py
|   |       |   |   |   balance_pairs.py
|   |       |   |   |   emphasis.py
|   |       |   |   |   entity.py
|   |       |   |   |   escape.py
|   |       |   |   |   fragments_join.py
|   |       |   |   |   html_inline.py
|   |       |   |   |   image.py
|   |       |   |   |   link.py
|   |       |   |   |   linkify.py
|   |       |   |   |   newline.py
|   |       |   |   |   state_inline.py
|   |       |   |   |   strikethrough.py
|   |       |   |   |   text.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           autolink.cpython-310.pyc
|   |       |   |           backticks.cpython-310.pyc
|   |       |   |           balance_pairs.cpython-310.pyc
|   |       |   |           emphasis.cpython-310.pyc
|   |       |   |           entity.cpython-310.pyc
|   |       |   |           escape.cpython-310.pyc
|   |       |   |           fragments_join.cpython-310.pyc
|   |       |   |           html_inline.cpython-310.pyc
|   |       |   |           image.cpython-310.pyc
|   |       |   |           link.cpython-310.pyc
|   |       |   |           linkify.cpython-310.pyc
|   |       |   |           newline.cpython-310.pyc
|   |       |   |           state_inline.cpython-310.pyc
|   |       |   |           strikethrough.cpython-310.pyc
|   |       |   |           text.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           main.cpython-310.pyc
|   |       |           parser_block.cpython-310.pyc
|   |       |           parser_core.cpython-310.pyc
|   |       |           parser_inline.cpython-310.pyc
|   |       |           renderer.cpython-310.pyc
|   |       |           ruler.cpython-310.pyc
|   |       |           token.cpython-310.pyc
|   |       |           tree.cpython-310.pyc
|   |       |           utils.cpython-310.pyc
|   |       |           _compat.cpython-310.pyc
|   |       |           _punycode.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---markdown_it_py-4.0.0.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           LICENSE.markdown-it
|   |       |           
|   |       +---mdurl
|   |       |   |   py.typed
|   |       |   |   _decode.py
|   |       |   |   _encode.py
|   |       |   |   _format.py
|   |       |   |   _parse.py
|   |       |   |   _url.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           _decode.cpython-310.pyc
|   |       |           _encode.cpython-310.pyc
|   |       |           _format.cpython-310.pyc
|   |       |           _parse.cpython-310.pyc
|   |       |           _url.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---mdurl-0.1.2.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       WHEEL
|   |       |       
|   |       +---numpy
|   |       |   |   conftest.py
|   |       |   |   ctypeslib.py
|   |       |   |   ctypeslib.pyi
|   |       |   |   dtypes.py
|   |       |   |   dtypes.pyi
|   |       |   |   exceptions.py
|   |       |   |   exceptions.pyi
|   |       |   |   matlib.py
|   |       |   |   matlib.pyi
|   |       |   |   py.typed
|   |       |   |   version.py
|   |       |   |   version.pyi
|   |       |   |   _array_api_info.py
|   |       |   |   _array_api_info.pyi
|   |       |   |   _configtool.py
|   |       |   |   _configtool.pyi
|   |       |   |   _distributor_init.py
|   |       |   |   _distributor_init.pyi
|   |       |   |   _expired_attrs_2_0.py
|   |       |   |   _expired_attrs_2_0.pyi
|   |       |   |   _globals.py
|   |       |   |   _globals.pyi
|   |       |   |   _pytesttester.py
|   |       |   |   _pytesttester.pyi
|   |       |   |   __config__.py
|   |       |   |   __config__.pyi
|   |       |   |   __init__.cython-30.pxd
|   |       |   |   __init__.pxd
|   |       |   |   __init__.py
|   |       |   |   __init__.pyi
|   |       |   |   
|   |       |   +---char
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---compat
|   |       |   |   |   py3k.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           py3k.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---core
|   |       |   |   |   arrayprint.py
|   |       |   |   |   defchararray.py
|   |       |   |   |   einsumfunc.py
|   |       |   |   |   fromnumeric.py
|   |       |   |   |   function_base.py
|   |       |   |   |   getlimits.py
|   |       |   |   |   multiarray.py
|   |       |   |   |   numeric.py
|   |       |   |   |   numerictypes.py
|   |       |   |   |   overrides.py
|   |       |   |   |   overrides.pyi
|   |       |   |   |   records.py
|   |       |   |   |   shape_base.py
|   |       |   |   |   umath.py
|   |       |   |   |   _dtype.py
|   |       |   |   |   _dtype.pyi
|   |       |   |   |   _dtype_ctypes.py
|   |       |   |   |   _dtype_ctypes.pyi
|   |       |   |   |   _internal.py
|   |       |   |   |   _multiarray_umath.py
|   |       |   |   |   _utils.py
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           arrayprint.cpython-310.pyc
|   |       |   |           defchararray.cpython-310.pyc
|   |       |   |           einsumfunc.cpython-310.pyc
|   |       |   |           fromnumeric.cpython-310.pyc
|   |       |   |           function_base.cpython-310.pyc
|   |       |   |           getlimits.cpython-310.pyc
|   |       |   |           multiarray.cpython-310.pyc
|   |       |   |           numeric.cpython-310.pyc
|   |       |   |           numerictypes.cpython-310.pyc
|   |       |   |           overrides.cpython-310.pyc
|   |       |   |           records.cpython-310.pyc
|   |       |   |           shape_base.cpython-310.pyc
|   |       |   |           umath.cpython-310.pyc
|   |       |   |           _dtype.cpython-310.pyc
|   |       |   |           _dtype_ctypes.cpython-310.pyc
|   |       |   |           _internal.cpython-310.pyc
|   |       |   |           _multiarray_umath.cpython-310.pyc
|   |       |   |           _utils.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---distutils
|   |       |   |   |   armccompiler.py
|   |       |   |   |   ccompiler.py
|   |       |   |   |   ccompiler_opt.py
|   |       |   |   |   conv_template.py
|   |       |   |   |   core.py
|   |       |   |   |   cpuinfo.py
|   |       |   |   |   exec_command.py
|   |       |   |   |   extension.py
|   |       |   |   |   from_template.py
|   |       |   |   |   fujitsuccompiler.py
|   |       |   |   |   intelccompiler.py
|   |       |   |   |   lib2def.py
|   |       |   |   |   line_endings.py
|   |       |   |   |   log.py
|   |       |   |   |   mingw32ccompiler.py
|   |       |   |   |   misc_util.py
|   |       |   |   |   msvc9compiler.py
|   |       |   |   |   msvccompiler.py
|   |       |   |   |   npy_pkg_config.py
|   |       |   |   |   numpy_distribution.py
|   |       |   |   |   pathccompiler.py
|   |       |   |   |   system_info.py
|   |       |   |   |   unixccompiler.py
|   |       |   |   |   _shell_utils.py
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---checks
|   |       |   |   |       cpu_asimd.c
|   |       |   |   |       cpu_asimddp.c
|   |       |   |   |       cpu_asimdfhm.c
|   |       |   |   |       cpu_asimdhp.c
|   |       |   |   |       cpu_avx.c
|   |       |   |   |       cpu_avx2.c
|   |       |   |   |       cpu_avx512cd.c
|   |       |   |   |       cpu_avx512f.c
|   |       |   |   |       cpu_avx512_clx.c
|   |       |   |   |       cpu_avx512_cnl.c
|   |       |   |   |       cpu_avx512_icl.c
|   |       |   |   |       cpu_avx512_knl.c
|   |       |   |   |       cpu_avx512_knm.c
|   |       |   |   |       cpu_avx512_skx.c
|   |       |   |   |       cpu_avx512_spr.c
|   |       |   |   |       cpu_f16c.c
|   |       |   |   |       cpu_fma3.c
|   |       |   |   |       cpu_fma4.c
|   |       |   |   |       cpu_neon.c
|   |       |   |   |       cpu_neon_fp16.c
|   |       |   |   |       cpu_neon_vfpv4.c
|   |       |   |   |       cpu_popcnt.c
|   |       |   |   |       cpu_rvv.c
|   |       |   |   |       cpu_sse.c
|   |       |   |   |       cpu_sse2.c
|   |       |   |   |       cpu_sse3.c
|   |       |   |   |       cpu_sse41.c
|   |       |   |   |       cpu_sse42.c
|   |       |   |   |       cpu_ssse3.c
|   |       |   |   |       cpu_sve.c
|   |       |   |   |       cpu_vsx.c
|   |       |   |   |       cpu_vsx2.c
|   |       |   |   |       cpu_vsx3.c
|   |       |   |   |       cpu_vsx4.c
|   |       |   |   |       cpu_vx.c
|   |       |   |   |       cpu_vxe.c
|   |       |   |   |       cpu_vxe2.c
|   |       |   |   |       cpu_xop.c
|   |       |   |   |       extra_avx512bw_mask.c
|   |       |   |   |       extra_avx512dq_mask.c
|   |       |   |   |       extra_avx512f_reduce.c
|   |       |   |   |       extra_vsx3_half_double.c
|   |       |   |   |       extra_vsx4_mma.c
|   |       |   |   |       extra_vsx_asm.c
|   |       |   |   |       test_flags.c
|   |       |   |   |       
|   |       |   |   +---command
|   |       |   |   |   |   autodist.py
|   |       |   |   |   |   bdist_rpm.py
|   |       |   |   |   |   build.py
|   |       |   |   |   |   build_clib.py
|   |       |   |   |   |   build_ext.py
|   |       |   |   |   |   build_py.py
|   |       |   |   |   |   build_scripts.py
|   |       |   |   |   |   build_src.py
|   |       |   |   |   |   config.py
|   |       |   |   |   |   config_compiler.py
|   |       |   |   |   |   develop.py
|   |       |   |   |   |   egg_info.py
|   |       |   |   |   |   install.py
|   |       |   |   |   |   install_clib.py
|   |       |   |   |   |   install_data.py
|   |       |   |   |   |   install_headers.py
|   |       |   |   |   |   sdist.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           autodist.cpython-310.pyc
|   |       |   |   |           bdist_rpm.cpython-310.pyc
|   |       |   |   |           build.cpython-310.pyc
|   |       |   |   |           build_clib.cpython-310.pyc
|   |       |   |   |           build_ext.cpython-310.pyc
|   |       |   |   |           build_py.cpython-310.pyc
|   |       |   |   |           build_scripts.cpython-310.pyc
|   |       |   |   |           build_src.cpython-310.pyc
|   |       |   |   |           config.cpython-310.pyc
|   |       |   |   |           config_compiler.cpython-310.pyc
|   |       |   |   |           develop.cpython-310.pyc
|   |       |   |   |           egg_info.cpython-310.pyc
|   |       |   |   |           install.cpython-310.pyc
|   |       |   |   |           install_clib.cpython-310.pyc
|   |       |   |   |           install_data.cpython-310.pyc
|   |       |   |   |           install_headers.cpython-310.pyc
|   |       |   |   |           sdist.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---fcompiler
|   |       |   |   |   |   absoft.py
|   |       |   |   |   |   arm.py
|   |       |   |   |   |   compaq.py
|   |       |   |   |   |   environment.py
|   |       |   |   |   |   fujitsu.py
|   |       |   |   |   |   g95.py
|   |       |   |   |   |   gnu.py
|   |       |   |   |   |   hpux.py
|   |       |   |   |   |   ibm.py
|   |       |   |   |   |   intel.py
|   |       |   |   |   |   lahey.py
|   |       |   |   |   |   mips.py
|   |       |   |   |   |   nag.py
|   |       |   |   |   |   none.py
|   |       |   |   |   |   nv.py
|   |       |   |   |   |   pathf95.py
|   |       |   |   |   |   pg.py
|   |       |   |   |   |   sun.py
|   |       |   |   |   |   vast.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           absoft.cpython-310.pyc
|   |       |   |   |           arm.cpython-310.pyc
|   |       |   |   |           compaq.cpython-310.pyc
|   |       |   |   |           environment.cpython-310.pyc
|   |       |   |   |           fujitsu.cpython-310.pyc
|   |       |   |   |           g95.cpython-310.pyc
|   |       |   |   |           gnu.cpython-310.pyc
|   |       |   |   |           hpux.cpython-310.pyc
|   |       |   |   |           ibm.cpython-310.pyc
|   |       |   |   |           intel.cpython-310.pyc
|   |       |   |   |           lahey.cpython-310.pyc
|   |       |   |   |           mips.cpython-310.pyc
|   |       |   |   |           nag.cpython-310.pyc
|   |       |   |   |           none.cpython-310.pyc
|   |       |   |   |           nv.cpython-310.pyc
|   |       |   |   |           pathf95.cpython-310.pyc
|   |       |   |   |           pg.cpython-310.pyc
|   |       |   |   |           sun.cpython-310.pyc
|   |       |   |   |           vast.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---mingw
|   |       |   |   |       gfortran_vs2003_hack.c
|   |       |   |   |       
|   |       |   |   +---tests
|   |       |   |   |   |   test_build_ext.py
|   |       |   |   |   |   test_ccompiler_opt.py
|   |       |   |   |   |   test_ccompiler_opt_conf.py
|   |       |   |   |   |   test_exec_command.py
|   |       |   |   |   |   test_fcompiler.py
|   |       |   |   |   |   test_fcompiler_gnu.py
|   |       |   |   |   |   test_fcompiler_intel.py
|   |       |   |   |   |   test_fcompiler_nagfor.py
|   |       |   |   |   |   test_from_template.py
|   |       |   |   |   |   test_log.py
|   |       |   |   |   |   test_mingw32ccompiler.py
|   |       |   |   |   |   test_misc_util.py
|   |       |   |   |   |   test_npy_pkg_config.py
|   |       |   |   |   |   test_shell_utils.py
|   |       |   |   |   |   test_system_info.py
|   |       |   |   |   |   utilities.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_build_ext.cpython-310.pyc
|   |       |   |   |           test_ccompiler_opt.cpython-310.pyc
|   |       |   |   |           test_ccompiler_opt_conf.cpython-310.pyc
|   |       |   |   |           test_exec_command.cpython-310.pyc
|   |       |   |   |           test_fcompiler.cpython-310.pyc
|   |       |   |   |           test_fcompiler_gnu.cpython-310.pyc
|   |       |   |   |           test_fcompiler_intel.cpython-310.pyc
|   |       |   |   |           test_fcompiler_nagfor.cpython-310.pyc
|   |       |   |   |           test_from_template.cpython-310.pyc
|   |       |   |   |           test_log.cpython-310.pyc
|   |       |   |   |           test_mingw32ccompiler.cpython-310.pyc
|   |       |   |   |           test_misc_util.cpython-310.pyc
|   |       |   |   |           test_npy_pkg_config.cpython-310.pyc
|   |       |   |   |           test_shell_utils.cpython-310.pyc
|   |       |   |   |           test_system_info.cpython-310.pyc
|   |       |   |   |           utilities.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           armccompiler.cpython-310.pyc
|   |       |   |           ccompiler.cpython-310.pyc
|   |       |   |           ccompiler_opt.cpython-310.pyc
|   |       |   |           conv_template.cpython-310.pyc
|   |       |   |           core.cpython-310.pyc
|   |       |   |           cpuinfo.cpython-310.pyc
|   |       |   |           exec_command.cpython-310.pyc
|   |       |   |           extension.cpython-310.pyc
|   |       |   |           from_template.cpython-310.pyc
|   |       |   |           fujitsuccompiler.cpython-310.pyc
|   |       |   |           intelccompiler.cpython-310.pyc
|   |       |   |           lib2def.cpython-310.pyc
|   |       |   |           line_endings.cpython-310.pyc
|   |       |   |           log.cpython-310.pyc
|   |       |   |           mingw32ccompiler.cpython-310.pyc
|   |       |   |           misc_util.cpython-310.pyc
|   |       |   |           msvc9compiler.cpython-310.pyc
|   |       |   |           msvccompiler.cpython-310.pyc
|   |       |   |           npy_pkg_config.cpython-310.pyc
|   |       |   |           numpy_distribution.cpython-310.pyc
|   |       |   |           pathccompiler.cpython-310.pyc
|   |       |   |           system_info.cpython-310.pyc
|   |       |   |           unixccompiler.cpython-310.pyc
|   |       |   |           _shell_utils.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---doc
|   |       |   |   |   ufuncs.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           ufuncs.cpython-310.pyc
|   |       |   |           
|   |       |   +---f2py
|   |       |   |   |   auxfuncs.py
|   |       |   |   |   capi_maps.py
|   |       |   |   |   cb_rules.py
|   |       |   |   |   cfuncs.py
|   |       |   |   |   common_rules.py
|   |       |   |   |   crackfortran.py
|   |       |   |   |   diagnose.py
|   |       |   |   |   f2py2e.py
|   |       |   |   |   f90mod_rules.py
|   |       |   |   |   func2subr.py
|   |       |   |   |   rules.py
|   |       |   |   |   setup.cfg
|   |       |   |   |   symbolic.py
|   |       |   |   |   use_rules.py
|   |       |   |   |   _isocbind.py
|   |       |   |   |   _src_pyf.py
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   __main__.py
|   |       |   |   |   __version__.py
|   |       |   |   |   
|   |       |   |   +---src
|   |       |   |   |       fortranobject.c
|   |       |   |   |       fortranobject.h
|   |       |   |   |       
|   |       |   |   +---tests
|   |       |   |   |   |   test_abstract_interface.py
|   |       |   |   |   |   test_array_from_pyobj.py
|   |       |   |   |   |   test_assumed_shape.py
|   |       |   |   |   |   test_block_docstring.py
|   |       |   |   |   |   test_callback.py
|   |       |   |   |   |   test_character.py
|   |       |   |   |   |   test_common.py
|   |       |   |   |   |   test_crackfortran.py
|   |       |   |   |   |   test_data.py
|   |       |   |   |   |   test_docs.py
|   |       |   |   |   |   test_f2cmap.py
|   |       |   |   |   |   test_f2py2e.py
|   |       |   |   |   |   test_isoc.py
|   |       |   |   |   |   test_kind.py
|   |       |   |   |   |   test_mixed.py
|   |       |   |   |   |   test_modules.py
|   |       |   |   |   |   test_parameter.py
|   |       |   |   |   |   test_pyf_src.py
|   |       |   |   |   |   test_quoted_character.py
|   |       |   |   |   |   test_regression.py
|   |       |   |   |   |   test_return_character.py
|   |       |   |   |   |   test_return_complex.py
|   |       |   |   |   |   test_return_integer.py
|   |       |   |   |   |   test_return_logical.py
|   |       |   |   |   |   test_return_real.py
|   |       |   |   |   |   test_routines.py
|   |       |   |   |   |   test_semicolon_split.py
|   |       |   |   |   |   test_size.py
|   |       |   |   |   |   test_string.py
|   |       |   |   |   |   test_symbolic.py
|   |       |   |   |   |   test_value_attrspec.py
|   |       |   |   |   |   util.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---src
|   |       |   |   |   |   +---abstract_interface
|   |       |   |   |   |   |       foo.f90
|   |       |   |   |   |   |       gh18403_mod.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---array_from_pyobj
|   |       |   |   |   |   |       wrapmodule.c
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---assumed_shape
|   |       |   |   |   |   |       .f2py_f2cmap
|   |       |   |   |   |   |       foo_free.f90
|   |       |   |   |   |   |       foo_mod.f90
|   |       |   |   |   |   |       foo_use.f90
|   |       |   |   |   |   |       precision.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---block_docstring
|   |       |   |   |   |   |       foo.f
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---callback
|   |       |   |   |   |   |       foo.f
|   |       |   |   |   |   |       gh17797.f90
|   |       |   |   |   |   |       gh18335.f90
|   |       |   |   |   |   |       gh25211.f
|   |       |   |   |   |   |       gh25211.pyf
|   |       |   |   |   |   |       gh26681.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---cli
|   |       |   |   |   |   |       gh_22819.pyf
|   |       |   |   |   |   |       hi77.f
|   |       |   |   |   |   |       hiworld.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---common
|   |       |   |   |   |   |       block.f
|   |       |   |   |   |   |       gh19161.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---crackfortran
|   |       |   |   |   |   |       accesstype.f90
|   |       |   |   |   |   |       common_with_division.f
|   |       |   |   |   |   |       data_common.f
|   |       |   |   |   |   |       data_multiplier.f
|   |       |   |   |   |   |       data_stmts.f90
|   |       |   |   |   |   |       data_with_comments.f
|   |       |   |   |   |   |       foo_deps.f90
|   |       |   |   |   |   |       gh15035.f
|   |       |   |   |   |   |       gh17859.f
|   |       |   |   |   |   |       gh22648.pyf
|   |       |   |   |   |   |       gh23533.f
|   |       |   |   |   |   |       gh23598.f90
|   |       |   |   |   |   |       gh23598Warn.f90
|   |       |   |   |   |   |       gh23879.f90
|   |       |   |   |   |   |       gh27697.f90
|   |       |   |   |   |   |       gh2848.f90
|   |       |   |   |   |   |       operators.f90
|   |       |   |   |   |   |       privatemod.f90
|   |       |   |   |   |   |       publicmod.f90
|   |       |   |   |   |   |       pubprivmod.f90
|   |       |   |   |   |   |       unicode_comment.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---f2cmap
|   |       |   |   |   |   |       .f2py_f2cmap
|   |       |   |   |   |   |       isoFortranEnvMap.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---isocintrin
|   |       |   |   |   |   |       isoCtests.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---kind
|   |       |   |   |   |   |       foo.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---mixed
|   |       |   |   |   |   |       foo.f
|   |       |   |   |   |   |       foo_fixed.f90
|   |       |   |   |   |   |       foo_free.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---modules
|   |       |   |   |   |   |   |   module_data_docstring.f90
|   |       |   |   |   |   |   |   use_modules.f90
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   +---gh25337
|   |       |   |   |   |   |   |       data.f90
|   |       |   |   |   |   |   |       use_data.f90
|   |       |   |   |   |   |   |       
|   |       |   |   |   |   |   \---gh26920
|   |       |   |   |   |   |           two_mods_with_no_public_entities.f90
|   |       |   |   |   |   |           two_mods_with_one_public_routine.f90
|   |       |   |   |   |   |           
|   |       |   |   |   |   +---negative_bounds
|   |       |   |   |   |   |       issue_20853.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---parameter
|   |       |   |   |   |   |       constant_array.f90
|   |       |   |   |   |   |       constant_both.f90
|   |       |   |   |   |   |       constant_compound.f90
|   |       |   |   |   |   |       constant_integer.f90
|   |       |   |   |   |   |       constant_non_compound.f90
|   |       |   |   |   |   |       constant_real.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---quoted_character
|   |       |   |   |   |   |       foo.f
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---regression
|   |       |   |   |   |   |       AB.inc
|   |       |   |   |   |   |       assignOnlyModule.f90
|   |       |   |   |   |   |       datonly.f90
|   |       |   |   |   |   |       f77comments.f
|   |       |   |   |   |   |       f77fixedform.f95
|   |       |   |   |   |   |       f90continuation.f90
|   |       |   |   |   |   |       incfile.f90
|   |       |   |   |   |   |       inout.f90
|   |       |   |   |   |   |       lower_f2py_fortran.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---return_character
|   |       |   |   |   |   |       foo77.f
|   |       |   |   |   |   |       foo90.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---return_complex
|   |       |   |   |   |   |       foo77.f
|   |       |   |   |   |   |       foo90.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---return_integer
|   |       |   |   |   |   |       foo77.f
|   |       |   |   |   |   |       foo90.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---return_logical
|   |       |   |   |   |   |       foo77.f
|   |       |   |   |   |   |       foo90.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---return_real
|   |       |   |   |   |   |       foo77.f
|   |       |   |   |   |   |       foo90.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---routines
|   |       |   |   |   |   |       funcfortranname.f
|   |       |   |   |   |   |       funcfortranname.pyf
|   |       |   |   |   |   |       subrout.f
|   |       |   |   |   |   |       subrout.pyf
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---size
|   |       |   |   |   |   |       foo.f90
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---string
|   |       |   |   |   |   |       char.f90
|   |       |   |   |   |   |       fixed_string.f90
|   |       |   |   |   |   |       gh24008.f
|   |       |   |   |   |   |       gh24662.f90
|   |       |   |   |   |   |       gh25286.f90
|   |       |   |   |   |   |       gh25286.pyf
|   |       |   |   |   |   |       gh25286_bc.pyf
|   |       |   |   |   |   |       scalar_string.f90
|   |       |   |   |   |   |       string.f
|   |       |   |   |   |   |       
|   |       |   |   |   |   \---value_attrspec
|   |       |   |   |   |           gh21665.f90
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_abstract_interface.cpython-310.pyc
|   |       |   |   |           test_array_from_pyobj.cpython-310.pyc
|   |       |   |   |           test_assumed_shape.cpython-310.pyc
|   |       |   |   |           test_block_docstring.cpython-310.pyc
|   |       |   |   |           test_callback.cpython-310.pyc
|   |       |   |   |           test_character.cpython-310.pyc
|   |       |   |   |           test_common.cpython-310.pyc
|   |       |   |   |           test_crackfortran.cpython-310.pyc
|   |       |   |   |           test_data.cpython-310.pyc
|   |       |   |   |           test_docs.cpython-310.pyc
|   |       |   |   |           test_f2cmap.cpython-310.pyc
|   |       |   |   |           test_f2py2e.cpython-310.pyc
|   |       |   |   |           test_isoc.cpython-310.pyc
|   |       |   |   |           test_kind.cpython-310.pyc
|   |       |   |   |           test_mixed.cpython-310.pyc
|   |       |   |   |           test_modules.cpython-310.pyc
|   |       |   |   |           test_parameter.cpython-310.pyc
|   |       |   |   |           test_pyf_src.cpython-310.pyc
|   |       |   |   |           test_quoted_character.cpython-310.pyc
|   |       |   |   |           test_regression.cpython-310.pyc
|   |       |   |   |           test_return_character.cpython-310.pyc
|   |       |   |   |           test_return_complex.cpython-310.pyc
|   |       |   |   |           test_return_integer.cpython-310.pyc
|   |       |   |   |           test_return_logical.cpython-310.pyc
|   |       |   |   |           test_return_real.cpython-310.pyc
|   |       |   |   |           test_routines.cpython-310.pyc
|   |       |   |   |           test_semicolon_split.cpython-310.pyc
|   |       |   |   |           test_size.cpython-310.pyc
|   |       |   |   |           test_string.cpython-310.pyc
|   |       |   |   |           test_symbolic.cpython-310.pyc
|   |       |   |   |           test_value_attrspec.cpython-310.pyc
|   |       |   |   |           util.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---_backends
|   |       |   |   |   |   meson.build.template
|   |       |   |   |   |   _backend.py
|   |       |   |   |   |   _distutils.py
|   |       |   |   |   |   _meson.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _backend.cpython-310.pyc
|   |       |   |   |           _distutils.cpython-310.pyc
|   |       |   |   |           _meson.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           auxfuncs.cpython-310.pyc
|   |       |   |           capi_maps.cpython-310.pyc
|   |       |   |           cb_rules.cpython-310.pyc
|   |       |   |           cfuncs.cpython-310.pyc
|   |       |   |           common_rules.cpython-310.pyc
|   |       |   |           crackfortran.cpython-310.pyc
|   |       |   |           diagnose.cpython-310.pyc
|   |       |   |           f2py2e.cpython-310.pyc
|   |       |   |           f90mod_rules.cpython-310.pyc
|   |       |   |           func2subr.cpython-310.pyc
|   |       |   |           rules.cpython-310.pyc
|   |       |   |           symbolic.cpython-310.pyc
|   |       |   |           use_rules.cpython-310.pyc
|   |       |   |           _isocbind.cpython-310.pyc
|   |       |   |           _src_pyf.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           __main__.cpython-310.pyc
|   |       |   |           __version__.cpython-310.pyc
|   |       |   |           
|   |       |   +---fft
|   |       |   |   |   helper.py
|   |       |   |   |   helper.pyi
|   |       |   |   |   _helper.py
|   |       |   |   |   _helper.pyi
|   |       |   |   |   _pocketfft.py
|   |       |   |   |   _pocketfft.pyi
|   |       |   |   |   _pocketfft_umath.cp310-win_amd64.lib
|   |       |   |   |   _pocketfft_umath.cp310-win_amd64.pyd
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |   |   test_helper.py
|   |       |   |   |   |   test_pocketfft.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_helper.cpython-310.pyc
|   |       |   |   |           test_pocketfft.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           helper.cpython-310.pyc
|   |       |   |           _helper.cpython-310.pyc
|   |       |   |           _pocketfft.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---lib
|   |       |   |   |   array_utils.py
|   |       |   |   |   array_utils.pyi
|   |       |   |   |   format.py
|   |       |   |   |   format.pyi
|   |       |   |   |   introspect.py
|   |       |   |   |   introspect.pyi
|   |       |   |   |   mixins.py
|   |       |   |   |   mixins.pyi
|   |       |   |   |   npyio.py
|   |       |   |   |   npyio.pyi
|   |       |   |   |   recfunctions.py
|   |       |   |   |   recfunctions.pyi
|   |       |   |   |   scimath.py
|   |       |   |   |   scimath.pyi
|   |       |   |   |   stride_tricks.py
|   |       |   |   |   stride_tricks.pyi
|   |       |   |   |   user_array.py
|   |       |   |   |   user_array.pyi
|   |       |   |   |   _arraypad_impl.py
|   |       |   |   |   _arraypad_impl.pyi
|   |       |   |   |   _arraysetops_impl.py
|   |       |   |   |   _arraysetops_impl.pyi
|   |       |   |   |   _arrayterator_impl.py
|   |       |   |   |   _arrayterator_impl.pyi
|   |       |   |   |   _array_utils_impl.py
|   |       |   |   |   _array_utils_impl.pyi
|   |       |   |   |   _datasource.py
|   |       |   |   |   _datasource.pyi
|   |       |   |   |   _function_base_impl.py
|   |       |   |   |   _function_base_impl.pyi
|   |       |   |   |   _histograms_impl.py
|   |       |   |   |   _histograms_impl.pyi
|   |       |   |   |   _index_tricks_impl.py
|   |       |   |   |   _index_tricks_impl.pyi
|   |       |   |   |   _iotools.py
|   |       |   |   |   _iotools.pyi
|   |       |   |   |   _nanfunctions_impl.py
|   |       |   |   |   _nanfunctions_impl.pyi
|   |       |   |   |   _npyio_impl.py
|   |       |   |   |   _npyio_impl.pyi
|   |       |   |   |   _polynomial_impl.py
|   |       |   |   |   _polynomial_impl.pyi
|   |       |   |   |   _scimath_impl.py
|   |       |   |   |   _scimath_impl.pyi
|   |       |   |   |   _shape_base_impl.py
|   |       |   |   |   _shape_base_impl.pyi
|   |       |   |   |   _stride_tricks_impl.py
|   |       |   |   |   _stride_tricks_impl.pyi
|   |       |   |   |   _twodim_base_impl.py
|   |       |   |   |   _twodim_base_impl.pyi
|   |       |   |   |   _type_check_impl.py
|   |       |   |   |   _type_check_impl.pyi
|   |       |   |   |   _ufunclike_impl.py
|   |       |   |   |   _ufunclike_impl.pyi
|   |       |   |   |   _user_array_impl.py
|   |       |   |   |   _user_array_impl.pyi
|   |       |   |   |   _utils_impl.py
|   |       |   |   |   _utils_impl.pyi
|   |       |   |   |   _version.py
|   |       |   |   |   _version.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |   |   test_arraypad.py
|   |       |   |   |   |   test_arraysetops.py
|   |       |   |   |   |   test_arrayterator.py
|   |       |   |   |   |   test_array_utils.py
|   |       |   |   |   |   test_format.py
|   |       |   |   |   |   test_function_base.py
|   |       |   |   |   |   test_histograms.py
|   |       |   |   |   |   test_index_tricks.py
|   |       |   |   |   |   test_io.py
|   |       |   |   |   |   test_loadtxt.py
|   |       |   |   |   |   test_mixins.py
|   |       |   |   |   |   test_nanfunctions.py
|   |       |   |   |   |   test_packbits.py
|   |       |   |   |   |   test_polynomial.py
|   |       |   |   |   |   test_recfunctions.py
|   |       |   |   |   |   test_regression.py
|   |       |   |   |   |   test_shape_base.py
|   |       |   |   |   |   test_stride_tricks.py
|   |       |   |   |   |   test_twodim_base.py
|   |       |   |   |   |   test_type_check.py
|   |       |   |   |   |   test_ufunclike.py
|   |       |   |   |   |   test_utils.py
|   |       |   |   |   |   test__datasource.py
|   |       |   |   |   |   test__iotools.py
|   |       |   |   |   |   test__version.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---data
|   |       |   |   |   |       py2-np0-objarr.npy
|   |       |   |   |   |       py2-objarr.npy
|   |       |   |   |   |       py2-objarr.npz
|   |       |   |   |   |       py3-objarr.npy
|   |       |   |   |   |       py3-objarr.npz
|   |       |   |   |   |       python3.npy
|   |       |   |   |   |       win64python2.npy
|   |       |   |   |   |       
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_arraypad.cpython-310.pyc
|   |       |   |   |           test_arraysetops.cpython-310.pyc
|   |       |   |   |           test_arrayterator.cpython-310.pyc
|   |       |   |   |           test_array_utils.cpython-310.pyc
|   |       |   |   |           test_format.cpython-310.pyc
|   |       |   |   |           test_function_base.cpython-310.pyc
|   |       |   |   |           test_histograms.cpython-310.pyc
|   |       |   |   |           test_index_tricks.cpython-310.pyc
|   |       |   |   |           test_io.cpython-310.pyc
|   |       |   |   |           test_loadtxt.cpython-310.pyc
|   |       |   |   |           test_mixins.cpython-310.pyc
|   |       |   |   |           test_nanfunctions.cpython-310.pyc
|   |       |   |   |           test_packbits.cpython-310.pyc
|   |       |   |   |           test_polynomial.cpython-310.pyc
|   |       |   |   |           test_recfunctions.cpython-310.pyc
|   |       |   |   |           test_regression.cpython-310.pyc
|   |       |   |   |           test_shape_base.cpython-310.pyc
|   |       |   |   |           test_stride_tricks.cpython-310.pyc
|   |       |   |   |           test_twodim_base.cpython-310.pyc
|   |       |   |   |           test_type_check.cpython-310.pyc
|   |       |   |   |           test_ufunclike.cpython-310.pyc
|   |       |   |   |           test_utils.cpython-310.pyc
|   |       |   |   |           test__datasource.cpython-310.pyc
|   |       |   |   |           test__iotools.cpython-310.pyc
|   |       |   |   |           test__version.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           array_utils.cpython-310.pyc
|   |       |   |           format.cpython-310.pyc
|   |       |   |           introspect.cpython-310.pyc
|   |       |   |           mixins.cpython-310.pyc
|   |       |   |           npyio.cpython-310.pyc
|   |       |   |           recfunctions.cpython-310.pyc
|   |       |   |           scimath.cpython-310.pyc
|   |       |   |           stride_tricks.cpython-310.pyc
|   |       |   |           user_array.cpython-310.pyc
|   |       |   |           _arraypad_impl.cpython-310.pyc
|   |       |   |           _arraysetops_impl.cpython-310.pyc
|   |       |   |           _arrayterator_impl.cpython-310.pyc
|   |       |   |           _array_utils_impl.cpython-310.pyc
|   |       |   |           _datasource.cpython-310.pyc
|   |       |   |           _function_base_impl.cpython-310.pyc
|   |       |   |           _histograms_impl.cpython-310.pyc
|   |       |   |           _index_tricks_impl.cpython-310.pyc
|   |       |   |           _iotools.cpython-310.pyc
|   |       |   |           _nanfunctions_impl.cpython-310.pyc
|   |       |   |           _npyio_impl.cpython-310.pyc
|   |       |   |           _polynomial_impl.cpython-310.pyc
|   |       |   |           _scimath_impl.cpython-310.pyc
|   |       |   |           _shape_base_impl.cpython-310.pyc
|   |       |   |           _stride_tricks_impl.cpython-310.pyc
|   |       |   |           _twodim_base_impl.cpython-310.pyc
|   |       |   |           _type_check_impl.cpython-310.pyc
|   |       |   |           _ufunclike_impl.cpython-310.pyc
|   |       |   |           _user_array_impl.cpython-310.pyc
|   |       |   |           _utils_impl.cpython-310.pyc
|   |       |   |           _version.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---linalg
|   |       |   |   |   lapack_lite.cp310-win_amd64.lib
|   |       |   |   |   lapack_lite.cp310-win_amd64.pyd
|   |       |   |   |   lapack_lite.pyi
|   |       |   |   |   linalg.py
|   |       |   |   |   linalg.pyi
|   |       |   |   |   _linalg.py
|   |       |   |   |   _linalg.pyi
|   |       |   |   |   _umath_linalg.cp310-win_amd64.lib
|   |       |   |   |   _umath_linalg.cp310-win_amd64.pyd
|   |       |   |   |   _umath_linalg.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |   |   test_deprecations.py
|   |       |   |   |   |   test_linalg.py
|   |       |   |   |   |   test_regression.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_deprecations.cpython-310.pyc
|   |       |   |   |           test_linalg.cpython-310.pyc
|   |       |   |   |           test_regression.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           linalg.cpython-310.pyc
|   |       |   |           _linalg.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---ma
|   |       |   |   |   API_CHANGES.txt
|   |       |   |   |   core.py
|   |       |   |   |   core.pyi
|   |       |   |   |   extras.py
|   |       |   |   |   extras.pyi
|   |       |   |   |   LICENSE
|   |       |   |   |   mrecords.py
|   |       |   |   |   mrecords.pyi
|   |       |   |   |   README.rst
|   |       |   |   |   testutils.py
|   |       |   |   |   timer_comparison.py
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |   |   test_arrayobject.py
|   |       |   |   |   |   test_core.py
|   |       |   |   |   |   test_deprecations.py
|   |       |   |   |   |   test_extras.py
|   |       |   |   |   |   test_mrecords.py
|   |       |   |   |   |   test_old_ma.py
|   |       |   |   |   |   test_regression.py
|   |       |   |   |   |   test_subclassing.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_arrayobject.cpython-310.pyc
|   |       |   |   |           test_core.cpython-310.pyc
|   |       |   |   |           test_deprecations.cpython-310.pyc
|   |       |   |   |           test_extras.cpython-310.pyc
|   |       |   |   |           test_mrecords.cpython-310.pyc
|   |       |   |   |           test_old_ma.cpython-310.pyc
|   |       |   |   |           test_regression.cpython-310.pyc
|   |       |   |   |           test_subclassing.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           core.cpython-310.pyc
|   |       |   |           extras.cpython-310.pyc
|   |       |   |           mrecords.cpython-310.pyc
|   |       |   |           testutils.cpython-310.pyc
|   |       |   |           timer_comparison.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---matrixlib
|   |       |   |   |   defmatrix.py
|   |       |   |   |   defmatrix.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |   |   test_defmatrix.py
|   |       |   |   |   |   test_interaction.py
|   |       |   |   |   |   test_masked_matrix.py
|   |       |   |   |   |   test_matrix_linalg.py
|   |       |   |   |   |   test_multiarray.py
|   |       |   |   |   |   test_numeric.py
|   |       |   |   |   |   test_regression.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_defmatrix.cpython-310.pyc
|   |       |   |   |           test_interaction.cpython-310.pyc
|   |       |   |   |           test_masked_matrix.cpython-310.pyc
|   |       |   |   |           test_matrix_linalg.cpython-310.pyc
|   |       |   |   |           test_multiarray.cpython-310.pyc
|   |       |   |   |           test_numeric.cpython-310.pyc
|   |       |   |   |           test_regression.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           defmatrix.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---polynomial
|   |       |   |   |   chebyshev.py
|   |       |   |   |   chebyshev.pyi
|   |       |   |   |   hermite.py
|   |       |   |   |   hermite.pyi
|   |       |   |   |   hermite_e.py
|   |       |   |   |   hermite_e.pyi
|   |       |   |   |   laguerre.py
|   |       |   |   |   laguerre.pyi
|   |       |   |   |   legendre.py
|   |       |   |   |   legendre.pyi
|   |       |   |   |   polynomial.py
|   |       |   |   |   polynomial.pyi
|   |       |   |   |   polyutils.py
|   |       |   |   |   polyutils.pyi
|   |       |   |   |   _polybase.py
|   |       |   |   |   _polybase.pyi
|   |       |   |   |   _polytypes.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |   |   test_chebyshev.py
|   |       |   |   |   |   test_classes.py
|   |       |   |   |   |   test_hermite.py
|   |       |   |   |   |   test_hermite_e.py
|   |       |   |   |   |   test_laguerre.py
|   |       |   |   |   |   test_legendre.py
|   |       |   |   |   |   test_polynomial.py
|   |       |   |   |   |   test_polyutils.py
|   |       |   |   |   |   test_printing.py
|   |       |   |   |   |   test_symbol.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_chebyshev.cpython-310.pyc
|   |       |   |   |           test_classes.cpython-310.pyc
|   |       |   |   |           test_hermite.cpython-310.pyc
|   |       |   |   |           test_hermite_e.cpython-310.pyc
|   |       |   |   |           test_laguerre.cpython-310.pyc
|   |       |   |   |           test_legendre.cpython-310.pyc
|   |       |   |   |           test_polynomial.cpython-310.pyc
|   |       |   |   |           test_polyutils.cpython-310.pyc
|   |       |   |   |           test_printing.cpython-310.pyc
|   |       |   |   |           test_symbol.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           chebyshev.cpython-310.pyc
|   |       |   |           hermite.cpython-310.pyc
|   |       |   |           hermite_e.cpython-310.pyc
|   |       |   |           laguerre.cpython-310.pyc
|   |       |   |           legendre.cpython-310.pyc
|   |       |   |           polynomial.cpython-310.pyc
|   |       |   |           polyutils.cpython-310.pyc
|   |       |   |           _polybase.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---random
|   |       |   |   |   bit_generator.cp310-win_amd64.lib
|   |       |   |   |   bit_generator.cp310-win_amd64.pyd
|   |       |   |   |   bit_generator.pxd
|   |       |   |   |   bit_generator.pyi
|   |       |   |   |   c_distributions.pxd
|   |       |   |   |   LICENSE.md
|   |       |   |   |   mtrand.cp310-win_amd64.lib
|   |       |   |   |   mtrand.cp310-win_amd64.pyd
|   |       |   |   |   mtrand.pyi
|   |       |   |   |   _bounded_integers.cp310-win_amd64.lib
|   |       |   |   |   _bounded_integers.cp310-win_amd64.pyd
|   |       |   |   |   _bounded_integers.pxd
|   |       |   |   |   _common.cp310-win_amd64.lib
|   |       |   |   |   _common.cp310-win_amd64.pyd
|   |       |   |   |   _common.pxd
|   |       |   |   |   _generator.cp310-win_amd64.lib
|   |       |   |   |   _generator.cp310-win_amd64.pyd
|   |       |   |   |   _generator.pyi
|   |       |   |   |   _mt19937.cp310-win_amd64.lib
|   |       |   |   |   _mt19937.cp310-win_amd64.pyd
|   |       |   |   |   _mt19937.pyi
|   |       |   |   |   _pcg64.cp310-win_amd64.lib
|   |       |   |   |   _pcg64.cp310-win_amd64.pyd
|   |       |   |   |   _pcg64.pyi
|   |       |   |   |   _philox.cp310-win_amd64.lib
|   |       |   |   |   _philox.cp310-win_amd64.pyd
|   |       |   |   |   _philox.pyi
|   |       |   |   |   _pickle.py
|   |       |   |   |   _pickle.pyi
|   |       |   |   |   _sfc64.cp310-win_amd64.lib
|   |       |   |   |   _sfc64.cp310-win_amd64.pyd
|   |       |   |   |   _sfc64.pyi
|   |       |   |   |   __init__.pxd
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---lib
|   |       |   |   |       npyrandom.lib
|   |       |   |   |       
|   |       |   |   +---tests
|   |       |   |   |   |   test_direct.py
|   |       |   |   |   |   test_extending.py
|   |       |   |   |   |   test_generator_mt19937.py
|   |       |   |   |   |   test_generator_mt19937_regressions.py
|   |       |   |   |   |   test_random.py
|   |       |   |   |   |   test_randomstate.py
|   |       |   |   |   |   test_randomstate_regression.py
|   |       |   |   |   |   test_regression.py
|   |       |   |   |   |   test_seed_sequence.py
|   |       |   |   |   |   test_smoke.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---data
|   |       |   |   |   |   |   generator_pcg64_np121.pkl.gz
|   |       |   |   |   |   |   generator_pcg64_np126.pkl.gz
|   |       |   |   |   |   |   mt19937-testset-1.csv
|   |       |   |   |   |   |   mt19937-testset-2.csv
|   |       |   |   |   |   |   pcg64-testset-1.csv
|   |       |   |   |   |   |   pcg64-testset-2.csv
|   |       |   |   |   |   |   pcg64dxsm-testset-1.csv
|   |       |   |   |   |   |   pcg64dxsm-testset-2.csv
|   |       |   |   |   |   |   philox-testset-1.csv
|   |       |   |   |   |   |   philox-testset-2.csv
|   |       |   |   |   |   |   sfc64-testset-1.csv
|   |       |   |   |   |   |   sfc64-testset-2.csv
|   |       |   |   |   |   |   sfc64_np126.pkl.gz
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_direct.cpython-310.pyc
|   |       |   |   |           test_extending.cpython-310.pyc
|   |       |   |   |           test_generator_mt19937.cpython-310.pyc
|   |       |   |   |           test_generator_mt19937_regressions.cpython-310.pyc
|   |       |   |   |           test_random.cpython-310.pyc
|   |       |   |   |           test_randomstate.cpython-310.pyc
|   |       |   |   |           test_randomstate_regression.cpython-310.pyc
|   |       |   |   |           test_regression.cpython-310.pyc
|   |       |   |   |           test_seed_sequence.cpython-310.pyc
|   |       |   |   |           test_smoke.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---_examples
|   |       |   |   |   +---cffi
|   |       |   |   |   |   |   extending.py
|   |       |   |   |   |   |   parse.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           extending.cpython-310.pyc
|   |       |   |   |   |           parse.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---cython
|   |       |   |   |   |       extending.pyx
|   |       |   |   |   |       extending_distributions.pyx
|   |       |   |   |   |       meson.build
|   |       |   |   |   |       
|   |       |   |   |   \---numba
|   |       |   |   |       |   extending.py
|   |       |   |   |       |   extending_distributions.py
|   |       |   |   |       |   
|   |       |   |   |       \---__pycache__
|   |       |   |   |               extending.cpython-310.pyc
|   |       |   |   |               extending_distributions.cpython-310.pyc
|   |       |   |   |               
|   |       |   |   \---__pycache__
|   |       |   |           _pickle.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---rec
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---strings
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---testing
|   |       |   |   |   overrides.py
|   |       |   |   |   overrides.pyi
|   |       |   |   |   print_coercion_tables.py
|   |       |   |   |   print_coercion_tables.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |   |   test_utils.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_utils.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---_private
|   |       |   |   |   |   extbuild.py
|   |       |   |   |   |   extbuild.pyi
|   |       |   |   |   |   utils.py
|   |       |   |   |   |   utils.pyi
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __init__.pyi
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           extbuild.cpython-310.pyc
|   |       |   |   |           utils.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           overrides.cpython-310.pyc
|   |       |   |           print_coercion_tables.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---tests
|   |       |   |   |   test_configtool.py
|   |       |   |   |   test_ctypeslib.py
|   |       |   |   |   test_lazyloading.py
|   |       |   |   |   test_matlib.py
|   |       |   |   |   test_numpy_config.py
|   |       |   |   |   test_numpy_version.py
|   |       |   |   |   test_public_api.py
|   |       |   |   |   test_reloading.py
|   |       |   |   |   test_scripts.py
|   |       |   |   |   test_warnings.py
|   |       |   |   |   test__all__.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           test_configtool.cpython-310.pyc
|   |       |   |           test_ctypeslib.cpython-310.pyc
|   |       |   |           test_lazyloading.cpython-310.pyc
|   |       |   |           test_matlib.cpython-310.pyc
|   |       |   |           test_numpy_config.cpython-310.pyc
|   |       |   |           test_numpy_version.cpython-310.pyc
|   |       |   |           test_public_api.cpython-310.pyc
|   |       |   |           test_reloading.cpython-310.pyc
|   |       |   |           test_scripts.cpython-310.pyc
|   |       |   |           test_warnings.cpython-310.pyc
|   |       |   |           test__all__.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---typing
|   |       |   |   |   mypy_plugin.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |   |   test_isfile.py
|   |       |   |   |   |   test_runtime.py
|   |       |   |   |   |   test_typing.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---data
|   |       |   |   |   |   |   mypy.ini
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---fail
|   |       |   |   |   |   |       arithmetic.pyi
|   |       |   |   |   |   |       arrayprint.pyi
|   |       |   |   |   |   |       arrayterator.pyi
|   |       |   |   |   |   |       array_constructors.pyi
|   |       |   |   |   |   |       array_like.pyi
|   |       |   |   |   |   |       array_pad.pyi
|   |       |   |   |   |   |       bitwise_ops.pyi
|   |       |   |   |   |   |       char.pyi
|   |       |   |   |   |   |       chararray.pyi
|   |       |   |   |   |   |       comparisons.pyi
|   |       |   |   |   |   |       constants.pyi
|   |       |   |   |   |   |       datasource.pyi
|   |       |   |   |   |   |       dtype.pyi
|   |       |   |   |   |   |       einsumfunc.pyi
|   |       |   |   |   |   |       flatiter.pyi
|   |       |   |   |   |   |       fromnumeric.pyi
|   |       |   |   |   |   |       histograms.pyi
|   |       |   |   |   |   |       index_tricks.pyi
|   |       |   |   |   |   |       lib_function_base.pyi
|   |       |   |   |   |   |       lib_polynomial.pyi
|   |       |   |   |   |   |       lib_utils.pyi
|   |       |   |   |   |   |       lib_version.pyi
|   |       |   |   |   |   |       linalg.pyi
|   |       |   |   |   |   |       memmap.pyi
|   |       |   |   |   |   |       modules.pyi
|   |       |   |   |   |   |       multiarray.pyi
|   |       |   |   |   |   |       ndarray.pyi
|   |       |   |   |   |   |       ndarray_misc.pyi
|   |       |   |   |   |   |       nditer.pyi
|   |       |   |   |   |   |       nested_sequence.pyi
|   |       |   |   |   |   |       npyio.pyi
|   |       |   |   |   |   |       numerictypes.pyi
|   |       |   |   |   |   |       random.pyi
|   |       |   |   |   |   |       rec.pyi
|   |       |   |   |   |   |       scalars.pyi
|   |       |   |   |   |   |       shape.pyi
|   |       |   |   |   |   |       shape_base.pyi
|   |       |   |   |   |   |       stride_tricks.pyi
|   |       |   |   |   |   |       strings.pyi
|   |       |   |   |   |   |       testing.pyi
|   |       |   |   |   |   |       twodim_base.pyi
|   |       |   |   |   |   |       type_check.pyi
|   |       |   |   |   |   |       ufunclike.pyi
|   |       |   |   |   |   |       ufuncs.pyi
|   |       |   |   |   |   |       ufunc_config.pyi
|   |       |   |   |   |   |       warnings_and_errors.pyi
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---misc
|   |       |   |   |   |   |       extended_precision.pyi
|   |       |   |   |   |   |       
|   |       |   |   |   |   +---pass
|   |       |   |   |   |   |   |   arithmetic.py
|   |       |   |   |   |   |   |   arrayprint.py
|   |       |   |   |   |   |   |   arrayterator.py
|   |       |   |   |   |   |   |   array_constructors.py
|   |       |   |   |   |   |   |   array_like.py
|   |       |   |   |   |   |   |   bitwise_ops.py
|   |       |   |   |   |   |   |   comparisons.py
|   |       |   |   |   |   |   |   dtype.py
|   |       |   |   |   |   |   |   einsumfunc.py
|   |       |   |   |   |   |   |   flatiter.py
|   |       |   |   |   |   |   |   fromnumeric.py
|   |       |   |   |   |   |   |   index_tricks.py
|   |       |   |   |   |   |   |   lib_user_array.py
|   |       |   |   |   |   |   |   lib_utils.py
|   |       |   |   |   |   |   |   lib_version.py
|   |       |   |   |   |   |   |   literal.py
|   |       |   |   |   |   |   |   ma.py
|   |       |   |   |   |   |   |   mod.py
|   |       |   |   |   |   |   |   modules.py
|   |       |   |   |   |   |   |   multiarray.py
|   |       |   |   |   |   |   |   ndarray_conversion.py
|   |       |   |   |   |   |   |   ndarray_misc.py
|   |       |   |   |   |   |   |   ndarray_shape_manipulation.py
|   |       |   |   |   |   |   |   nditer.py
|   |       |   |   |   |   |   |   numeric.py
|   |       |   |   |   |   |   |   numerictypes.py
|   |       |   |   |   |   |   |   random.py
|   |       |   |   |   |   |   |   recfunctions.py
|   |       |   |   |   |   |   |   scalars.py
|   |       |   |   |   |   |   |   shape.py
|   |       |   |   |   |   |   |   simple.py
|   |       |   |   |   |   |   |   simple_py3.py
|   |       |   |   |   |   |   |   ufunclike.py
|   |       |   |   |   |   |   |   ufuncs.py
|   |       |   |   |   |   |   |   ufunc_config.py
|   |       |   |   |   |   |   |   warnings_and_errors.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           arithmetic.cpython-310.pyc
|   |       |   |   |   |   |           arrayprint.cpython-310.pyc
|   |       |   |   |   |   |           arrayterator.cpython-310.pyc
|   |       |   |   |   |   |           array_constructors.cpython-310.pyc
|   |       |   |   |   |   |           array_like.cpython-310.pyc
|   |       |   |   |   |   |           bitwise_ops.cpython-310.pyc
|   |       |   |   |   |   |           comparisons.cpython-310.pyc
|   |       |   |   |   |   |           dtype.cpython-310.pyc
|   |       |   |   |   |   |           einsumfunc.cpython-310.pyc
|   |       |   |   |   |   |           flatiter.cpython-310.pyc
|   |       |   |   |   |   |           fromnumeric.cpython-310.pyc
|   |       |   |   |   |   |           index_tricks.cpython-310.pyc
|   |       |   |   |   |   |           lib_user_array.cpython-310.pyc
|   |       |   |   |   |   |           lib_utils.cpython-310.pyc
|   |       |   |   |   |   |           lib_version.cpython-310.pyc
|   |       |   |   |   |   |           literal.cpython-310.pyc
|   |       |   |   |   |   |           ma.cpython-310.pyc
|   |       |   |   |   |   |           mod.cpython-310.pyc
|   |       |   |   |   |   |           modules.cpython-310.pyc
|   |       |   |   |   |   |           multiarray.cpython-310.pyc
|   |       |   |   |   |   |           ndarray_conversion.cpython-310.pyc
|   |       |   |   |   |   |           ndarray_misc.cpython-310.pyc
|   |       |   |   |   |   |           ndarray_shape_manipulation.cpython-310.pyc
|   |       |   |   |   |   |           nditer.cpython-310.pyc
|   |       |   |   |   |   |           numeric.cpython-310.pyc
|   |       |   |   |   |   |           numerictypes.cpython-310.pyc
|   |       |   |   |   |   |           random.cpython-310.pyc
|   |       |   |   |   |   |           recfunctions.cpython-310.pyc
|   |       |   |   |   |   |           scalars.cpython-310.pyc
|   |       |   |   |   |   |           shape.cpython-310.pyc
|   |       |   |   |   |   |           simple.cpython-310.pyc
|   |       |   |   |   |   |           simple_py3.cpython-310.pyc
|   |       |   |   |   |   |           ufunclike.cpython-310.pyc
|   |       |   |   |   |   |           ufuncs.cpython-310.pyc
|   |       |   |   |   |   |           ufunc_config.cpython-310.pyc
|   |       |   |   |   |   |           warnings_and_errors.cpython-310.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---reveal
|   |       |   |   |   |           arithmetic.pyi
|   |       |   |   |   |           arraypad.pyi
|   |       |   |   |   |           arrayprint.pyi
|   |       |   |   |   |           arraysetops.pyi
|   |       |   |   |   |           arrayterator.pyi
|   |       |   |   |   |           array_api_info.pyi
|   |       |   |   |   |           array_constructors.pyi
|   |       |   |   |   |           bitwise_ops.pyi
|   |       |   |   |   |           char.pyi
|   |       |   |   |   |           chararray.pyi
|   |       |   |   |   |           comparisons.pyi
|   |       |   |   |   |           constants.pyi
|   |       |   |   |   |           ctypeslib.pyi
|   |       |   |   |   |           datasource.pyi
|   |       |   |   |   |           dtype.pyi
|   |       |   |   |   |           einsumfunc.pyi
|   |       |   |   |   |           emath.pyi
|   |       |   |   |   |           fft.pyi
|   |       |   |   |   |           flatiter.pyi
|   |       |   |   |   |           fromnumeric.pyi
|   |       |   |   |   |           getlimits.pyi
|   |       |   |   |   |           histograms.pyi
|   |       |   |   |   |           index_tricks.pyi
|   |       |   |   |   |           lib_function_base.pyi
|   |       |   |   |   |           lib_polynomial.pyi
|   |       |   |   |   |           lib_utils.pyi
|   |       |   |   |   |           lib_version.pyi
|   |       |   |   |   |           linalg.pyi
|   |       |   |   |   |           matrix.pyi
|   |       |   |   |   |           memmap.pyi
|   |       |   |   |   |           mod.pyi
|   |       |   |   |   |           modules.pyi
|   |       |   |   |   |           multiarray.pyi
|   |       |   |   |   |           nbit_base_example.pyi
|   |       |   |   |   |           ndarray_assignability.pyi
|   |       |   |   |   |           ndarray_conversion.pyi
|   |       |   |   |   |           ndarray_misc.pyi
|   |       |   |   |   |           ndarray_shape_manipulation.pyi
|   |       |   |   |   |           nditer.pyi
|   |       |   |   |   |           nested_sequence.pyi
|   |       |   |   |   |           npyio.pyi
|   |       |   |   |   |           numeric.pyi
|   |       |   |   |   |           numerictypes.pyi
|   |       |   |   |   |           polynomial_polybase.pyi
|   |       |   |   |   |           polynomial_polyutils.pyi
|   |       |   |   |   |           polynomial_series.pyi
|   |       |   |   |   |           random.pyi
|   |       |   |   |   |           rec.pyi
|   |       |   |   |   |           scalars.pyi
|   |       |   |   |   |           shape.pyi
|   |       |   |   |   |           shape_base.pyi
|   |       |   |   |   |           stride_tricks.pyi
|   |       |   |   |   |           strings.pyi
|   |       |   |   |   |           testing.pyi
|   |       |   |   |   |           twodim_base.pyi
|   |       |   |   |   |           type_check.pyi
|   |       |   |   |   |           ufunclike.pyi
|   |       |   |   |   |           ufuncs.pyi
|   |       |   |   |   |           ufunc_config.pyi
|   |       |   |   |   |           warnings_and_errors.pyi
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_isfile.cpython-310.pyc
|   |       |   |   |           test_runtime.cpython-310.pyc
|   |       |   |   |           test_typing.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           mypy_plugin.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_core
|   |       |   |   |   arrayprint.py
|   |       |   |   |   arrayprint.pyi
|   |       |   |   |   cversions.py
|   |       |   |   |   defchararray.py
|   |       |   |   |   defchararray.pyi
|   |       |   |   |   einsumfunc.py
|   |       |   |   |   einsumfunc.pyi
|   |       |   |   |   fromnumeric.py
|   |       |   |   |   fromnumeric.pyi
|   |       |   |   |   function_base.py
|   |       |   |   |   function_base.pyi
|   |       |   |   |   getlimits.py
|   |       |   |   |   getlimits.pyi
|   |       |   |   |   memmap.py
|   |       |   |   |   memmap.pyi
|   |       |   |   |   multiarray.py
|   |       |   |   |   multiarray.pyi
|   |       |   |   |   numeric.py
|   |       |   |   |   numeric.pyi
|   |       |   |   |   numerictypes.py
|   |       |   |   |   numerictypes.pyi
|   |       |   |   |   overrides.py
|   |       |   |   |   overrides.pyi
|   |       |   |   |   printoptions.py
|   |       |   |   |   printoptions.pyi
|   |       |   |   |   records.py
|   |       |   |   |   records.pyi
|   |       |   |   |   shape_base.py
|   |       |   |   |   shape_base.pyi
|   |       |   |   |   strings.py
|   |       |   |   |   strings.pyi
|   |       |   |   |   umath.py
|   |       |   |   |   umath.pyi
|   |       |   |   |   _add_newdocs.py
|   |       |   |   |   _add_newdocs.pyi
|   |       |   |   |   _add_newdocs_scalars.py
|   |       |   |   |   _add_newdocs_scalars.pyi
|   |       |   |   |   _asarray.py
|   |       |   |   |   _asarray.pyi
|   |       |   |   |   _dtype.py
|   |       |   |   |   _dtype.pyi
|   |       |   |   |   _dtype_ctypes.py
|   |       |   |   |   _dtype_ctypes.pyi
|   |       |   |   |   _exceptions.py
|   |       |   |   |   _exceptions.pyi
|   |       |   |   |   _internal.py
|   |       |   |   |   _internal.pyi
|   |       |   |   |   _machar.py
|   |       |   |   |   _machar.pyi
|   |       |   |   |   _methods.py
|   |       |   |   |   _methods.pyi
|   |       |   |   |   _multiarray_tests.cp310-win_amd64.lib
|   |       |   |   |   _multiarray_tests.cp310-win_amd64.pyd
|   |       |   |   |   _multiarray_umath.cp310-win_amd64.lib
|   |       |   |   |   _multiarray_umath.cp310-win_amd64.pyd
|   |       |   |   |   _operand_flag_tests.cp310-win_amd64.lib
|   |       |   |   |   _operand_flag_tests.cp310-win_amd64.pyd
|   |       |   |   |   _rational_tests.cp310-win_amd64.lib
|   |       |   |   |   _rational_tests.cp310-win_amd64.pyd
|   |       |   |   |   _simd.cp310-win_amd64.lib
|   |       |   |   |   _simd.cp310-win_amd64.pyd
|   |       |   |   |   _simd.pyi
|   |       |   |   |   _string_helpers.py
|   |       |   |   |   _string_helpers.pyi
|   |       |   |   |   _struct_ufunc_tests.cp310-win_amd64.lib
|   |       |   |   |   _struct_ufunc_tests.cp310-win_amd64.pyd
|   |       |   |   |   _type_aliases.py
|   |       |   |   |   _type_aliases.pyi
|   |       |   |   |   _ufunc_config.py
|   |       |   |   |   _ufunc_config.pyi
|   |       |   |   |   _umath_tests.cp310-win_amd64.lib
|   |       |   |   |   _umath_tests.cp310-win_amd64.pyd
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---include
|   |       |   |   |   \---numpy
|   |       |   |   |       |   arrayobject.h
|   |       |   |   |       |   arrayscalars.h
|   |       |   |   |       |   dtype_api.h
|   |       |   |   |       |   halffloat.h
|   |       |   |   |       |   ndarrayobject.h
|   |       |   |   |       |   ndarraytypes.h
|   |       |   |   |       |   npy_1_7_deprecated_api.h
|   |       |   |   |       |   npy_2_compat.h
|   |       |   |   |       |   npy_2_complexcompat.h
|   |       |   |   |       |   npy_3kcompat.h
|   |       |   |   |       |   npy_common.h
|   |       |   |   |       |   npy_cpu.h
|   |       |   |   |       |   npy_endian.h
|   |       |   |   |       |   npy_math.h
|   |       |   |   |       |   npy_no_deprecated_api.h
|   |       |   |   |       |   npy_os.h
|   |       |   |   |       |   numpyconfig.h
|   |       |   |   |       |   ufuncobject.h
|   |       |   |   |       |   utils.h
|   |       |   |   |       |   _neighborhood_iterator_imp.h
|   |       |   |   |       |   _numpyconfig.h
|   |       |   |   |       |   _public_dtype_api_table.h
|   |       |   |   |       |   __multiarray_api.c
|   |       |   |   |       |   __multiarray_api.h
|   |       |   |   |       |   __ufunc_api.c
|   |       |   |   |       |   __ufunc_api.h
|   |       |   |   |       |   
|   |       |   |   |       \---random
|   |       |   |   |               bitgen.h
|   |       |   |   |               distributions.h
|   |       |   |   |               libdivide.h
|   |       |   |   |               LICENSE.txt
|   |       |   |   |               
|   |       |   |   +---lib
|   |       |   |   |   |   npymath.lib
|   |       |   |   |   |   
|   |       |   |   |   +---npy-pkg-config
|   |       |   |   |   |       mlib.ini
|   |       |   |   |   |       npymath.ini
|   |       |   |   |   |       
|   |       |   |   |   \---pkgconfig
|   |       |   |   |           numpy.pc
|   |       |   |   |           
|   |       |   |   +---tests
|   |       |   |   |   |   test_abc.py
|   |       |   |   |   |   test_api.py
|   |       |   |   |   |   test_argparse.py
|   |       |   |   |   |   test_arraymethod.py
|   |       |   |   |   |   test_arrayobject.py
|   |       |   |   |   |   test_arrayprint.py
|   |       |   |   |   |   test_array_api_info.py
|   |       |   |   |   |   test_array_coercion.py
|   |       |   |   |   |   test_array_interface.py
|   |       |   |   |   |   test_casting_floatingpoint_errors.py
|   |       |   |   |   |   test_casting_unittests.py
|   |       |   |   |   |   test_conversion_utils.py
|   |       |   |   |   |   test_cpu_dispatcher.py
|   |       |   |   |   |   test_cpu_features.py
|   |       |   |   |   |   test_custom_dtypes.py
|   |       |   |   |   |   test_cython.py
|   |       |   |   |   |   test_datetime.py
|   |       |   |   |   |   test_defchararray.py
|   |       |   |   |   |   test_deprecations.py
|   |       |   |   |   |   test_dlpack.py
|   |       |   |   |   |   test_dtype.py
|   |       |   |   |   |   test_einsum.py
|   |       |   |   |   |   test_errstate.py
|   |       |   |   |   |   test_extint128.py
|   |       |   |   |   |   test_function_base.py
|   |       |   |   |   |   test_getlimits.py
|   |       |   |   |   |   test_half.py
|   |       |   |   |   |   test_hashtable.py
|   |       |   |   |   |   test_indexerrors.py
|   |       |   |   |   |   test_indexing.py
|   |       |   |   |   |   test_item_selection.py
|   |       |   |   |   |   test_limited_api.py
|   |       |   |   |   |   test_longdouble.py
|   |       |   |   |   |   test_machar.py
|   |       |   |   |   |   test_memmap.py
|   |       |   |   |   |   test_mem_overlap.py
|   |       |   |   |   |   test_mem_policy.py
|   |       |   |   |   |   test_multiarray.py
|   |       |   |   |   |   test_multithreading.py
|   |       |   |   |   |   test_nditer.py
|   |       |   |   |   |   test_nep50_promotions.py
|   |       |   |   |   |   test_numeric.py
|   |       |   |   |   |   test_numerictypes.py
|   |       |   |   |   |   test_overrides.py
|   |       |   |   |   |   test_print.py
|   |       |   |   |   |   test_protocols.py
|   |       |   |   |   |   test_records.py
|   |       |   |   |   |   test_regression.py
|   |       |   |   |   |   test_scalarbuffer.py
|   |       |   |   |   |   test_scalarinherit.py
|   |       |   |   |   |   test_scalarmath.py
|   |       |   |   |   |   test_scalarprint.py
|   |       |   |   |   |   test_scalar_ctors.py
|   |       |   |   |   |   test_scalar_methods.py
|   |       |   |   |   |   test_shape_base.py
|   |       |   |   |   |   test_simd.py
|   |       |   |   |   |   test_simd_module.py
|   |       |   |   |   |   test_stringdtype.py
|   |       |   |   |   |   test_strings.py
|   |       |   |   |   |   test_ufunc.py
|   |       |   |   |   |   test_umath.py
|   |       |   |   |   |   test_umath_accuracy.py
|   |       |   |   |   |   test_umath_complex.py
|   |       |   |   |   |   test_unicode.py
|   |       |   |   |   |   test__exceptions.py
|   |       |   |   |   |   _locales.py
|   |       |   |   |   |   _natype.py
|   |       |   |   |   |   
|   |       |   |   |   +---data
|   |       |   |   |   |       astype_copy.pkl
|   |       |   |   |   |       generate_umath_validation_data.cpp
|   |       |   |   |   |       recarray_from_file.fits
|   |       |   |   |   |       umath-validation-set-arccos.csv
|   |       |   |   |   |       umath-validation-set-arccosh.csv
|   |       |   |   |   |       umath-validation-set-arcsin.csv
|   |       |   |   |   |       umath-validation-set-arcsinh.csv
|   |       |   |   |   |       umath-validation-set-arctan.csv
|   |       |   |   |   |       umath-validation-set-arctanh.csv
|   |       |   |   |   |       umath-validation-set-cbrt.csv
|   |       |   |   |   |       umath-validation-set-cos.csv
|   |       |   |   |   |       umath-validation-set-cosh.csv
|   |       |   |   |   |       umath-validation-set-exp.csv
|   |       |   |   |   |       umath-validation-set-exp2.csv
|   |       |   |   |   |       umath-validation-set-expm1.csv
|   |       |   |   |   |       umath-validation-set-log.csv
|   |       |   |   |   |       umath-validation-set-log10.csv
|   |       |   |   |   |       umath-validation-set-log1p.csv
|   |       |   |   |   |       umath-validation-set-log2.csv
|   |       |   |   |   |       umath-validation-set-README.txt
|   |       |   |   |   |       umath-validation-set-sin.csv
|   |       |   |   |   |       umath-validation-set-sinh.csv
|   |       |   |   |   |       umath-validation-set-tan.csv
|   |       |   |   |   |       umath-validation-set-tanh.csv
|   |       |   |   |   |       
|   |       |   |   |   +---examples
|   |       |   |   |   |   +---cython
|   |       |   |   |   |   |   |   checks.pyx
|   |       |   |   |   |   |   |   meson.build
|   |       |   |   |   |   |   |   setup.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           setup.cpython-310.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---limited_api
|   |       |   |   |   |       |   limited_api1.c
|   |       |   |   |   |       |   limited_api2.pyx
|   |       |   |   |   |       |   limited_api_latest.c
|   |       |   |   |   |       |   meson.build
|   |       |   |   |   |       |   setup.py
|   |       |   |   |   |       |   
|   |       |   |   |   |       \---__pycache__
|   |       |   |   |   |               setup.cpython-310.pyc
|   |       |   |   |   |               
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_abc.cpython-310.pyc
|   |       |   |   |           test_api.cpython-310.pyc
|   |       |   |   |           test_argparse.cpython-310.pyc
|   |       |   |   |           test_arraymethod.cpython-310.pyc
|   |       |   |   |           test_arrayobject.cpython-310.pyc
|   |       |   |   |           test_arrayprint.cpython-310.pyc
|   |       |   |   |           test_array_api_info.cpython-310.pyc
|   |       |   |   |           test_array_coercion.cpython-310.pyc
|   |       |   |   |           test_array_interface.cpython-310.pyc
|   |       |   |   |           test_casting_floatingpoint_errors.cpython-310.pyc
|   |       |   |   |           test_casting_unittests.cpython-310.pyc
|   |       |   |   |           test_conversion_utils.cpython-310.pyc
|   |       |   |   |           test_cpu_dispatcher.cpython-310.pyc
|   |       |   |   |           test_cpu_features.cpython-310.pyc
|   |       |   |   |           test_custom_dtypes.cpython-310.pyc
|   |       |   |   |           test_cython.cpython-310.pyc
|   |       |   |   |           test_datetime.cpython-310.pyc
|   |       |   |   |           test_defchararray.cpython-310.pyc
|   |       |   |   |           test_deprecations.cpython-310.pyc
|   |       |   |   |           test_dlpack.cpython-310.pyc
|   |       |   |   |           test_dtype.cpython-310.pyc
|   |       |   |   |           test_einsum.cpython-310.pyc
|   |       |   |   |           test_errstate.cpython-310.pyc
|   |       |   |   |           test_extint128.cpython-310.pyc
|   |       |   |   |           test_function_base.cpython-310.pyc
|   |       |   |   |           test_getlimits.cpython-310.pyc
|   |       |   |   |           test_half.cpython-310.pyc
|   |       |   |   |           test_hashtable.cpython-310.pyc
|   |       |   |   |           test_indexerrors.cpython-310.pyc
|   |       |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |           test_item_selection.cpython-310.pyc
|   |       |   |   |           test_limited_api.cpython-310.pyc
|   |       |   |   |           test_longdouble.cpython-310.pyc
|   |       |   |   |           test_machar.cpython-310.pyc
|   |       |   |   |           test_memmap.cpython-310.pyc
|   |       |   |   |           test_mem_overlap.cpython-310.pyc
|   |       |   |   |           test_mem_policy.cpython-310.pyc
|   |       |   |   |           test_multiarray.cpython-310.pyc
|   |       |   |   |           test_multithreading.cpython-310.pyc
|   |       |   |   |           test_nditer.cpython-310.pyc
|   |       |   |   |           test_nep50_promotions.cpython-310.pyc
|   |       |   |   |           test_numeric.cpython-310.pyc
|   |       |   |   |           test_numerictypes.cpython-310.pyc
|   |       |   |   |           test_overrides.cpython-310.pyc
|   |       |   |   |           test_print.cpython-310.pyc
|   |       |   |   |           test_protocols.cpython-310.pyc
|   |       |   |   |           test_records.cpython-310.pyc
|   |       |   |   |           test_regression.cpython-310.pyc
|   |       |   |   |           test_scalarbuffer.cpython-310.pyc
|   |       |   |   |           test_scalarinherit.cpython-310.pyc
|   |       |   |   |           test_scalarmath.cpython-310.pyc
|   |       |   |   |           test_scalarprint.cpython-310.pyc
|   |       |   |   |           test_scalar_ctors.cpython-310.pyc
|   |       |   |   |           test_scalar_methods.cpython-310.pyc
|   |       |   |   |           test_shape_base.cpython-310.pyc
|   |       |   |   |           test_simd.cpython-310.pyc
|   |       |   |   |           test_simd_module.cpython-310.pyc
|   |       |   |   |           test_stringdtype.cpython-310.pyc
|   |       |   |   |           test_strings.cpython-310.pyc
|   |       |   |   |           test_ufunc.cpython-310.pyc
|   |       |   |   |           test_umath.cpython-310.pyc
|   |       |   |   |           test_umath_accuracy.cpython-310.pyc
|   |       |   |   |           test_umath_complex.cpython-310.pyc
|   |       |   |   |           test_unicode.cpython-310.pyc
|   |       |   |   |           test__exceptions.cpython-310.pyc
|   |       |   |   |           _locales.cpython-310.pyc
|   |       |   |   |           _natype.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           arrayprint.cpython-310.pyc
|   |       |   |           cversions.cpython-310.pyc
|   |       |   |           defchararray.cpython-310.pyc
|   |       |   |           einsumfunc.cpython-310.pyc
|   |       |   |           fromnumeric.cpython-310.pyc
|   |       |   |           function_base.cpython-310.pyc
|   |       |   |           getlimits.cpython-310.pyc
|   |       |   |           memmap.cpython-310.pyc
|   |       |   |           multiarray.cpython-310.pyc
|   |       |   |           numeric.cpython-310.pyc
|   |       |   |           numerictypes.cpython-310.pyc
|   |       |   |           overrides.cpython-310.pyc
|   |       |   |           printoptions.cpython-310.pyc
|   |       |   |           records.cpython-310.pyc
|   |       |   |           shape_base.cpython-310.pyc
|   |       |   |           strings.cpython-310.pyc
|   |       |   |           umath.cpython-310.pyc
|   |       |   |           _add_newdocs.cpython-310.pyc
|   |       |   |           _add_newdocs_scalars.cpython-310.pyc
|   |       |   |           _asarray.cpython-310.pyc
|   |       |   |           _dtype.cpython-310.pyc
|   |       |   |           _dtype_ctypes.cpython-310.pyc
|   |       |   |           _exceptions.cpython-310.pyc
|   |       |   |           _internal.cpython-310.pyc
|   |       |   |           _machar.cpython-310.pyc
|   |       |   |           _methods.cpython-310.pyc
|   |       |   |           _string_helpers.cpython-310.pyc
|   |       |   |           _type_aliases.cpython-310.pyc
|   |       |   |           _ufunc_config.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_pyinstaller
|   |       |   |   |   hook-numpy.py
|   |       |   |   |   hook-numpy.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   +---tests
|   |       |   |   |   |   pyinstaller-smoke.py
|   |       |   |   |   |   test_pyinstaller.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           pyinstaller-smoke.cpython-310.pyc
|   |       |   |   |           test_pyinstaller.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           hook-numpy.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_typing
|   |       |   |   |   _add_docstring.py
|   |       |   |   |   _array_like.py
|   |       |   |   |   _callable.pyi
|   |       |   |   |   _char_codes.py
|   |       |   |   |   _dtype_like.py
|   |       |   |   |   _extended_precision.py
|   |       |   |   |   _nbit.py
|   |       |   |   |   _nbit_base.py
|   |       |   |   |   _nested_sequence.py
|   |       |   |   |   _scalars.py
|   |       |   |   |   _shape.py
|   |       |   |   |   _ufunc.py
|   |       |   |   |   _ufunc.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _add_docstring.cpython-310.pyc
|   |       |   |           _array_like.cpython-310.pyc
|   |       |   |           _char_codes.cpython-310.pyc
|   |       |   |           _dtype_like.cpython-310.pyc
|   |       |   |           _extended_precision.cpython-310.pyc
|   |       |   |           _nbit.cpython-310.pyc
|   |       |   |           _nbit_base.cpython-310.pyc
|   |       |   |           _nested_sequence.cpython-310.pyc
|   |       |   |           _scalars.cpython-310.pyc
|   |       |   |           _shape.cpython-310.pyc
|   |       |   |           _ufunc.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_utils
|   |       |   |   |   _convertions.py
|   |       |   |   |   _convertions.pyi
|   |       |   |   |   _inspect.py
|   |       |   |   |   _inspect.pyi
|   |       |   |   |   _pep440.py
|   |       |   |   |   _pep440.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   __init__.pyi
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _convertions.cpython-310.pyc
|   |       |   |           _inspect.cpython-310.pyc
|   |       |   |           _pep440.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           conftest.cpython-310.pyc
|   |       |           ctypeslib.cpython-310.pyc
|   |       |           dtypes.cpython-310.pyc
|   |       |           exceptions.cpython-310.pyc
|   |       |           matlib.cpython-310.pyc
|   |       |           version.cpython-310.pyc
|   |       |           _array_api_info.cpython-310.pyc
|   |       |           _configtool.cpython-310.pyc
|   |       |           _distributor_init.cpython-310.pyc
|   |       |           _expired_attrs_2_0.cpython-310.pyc
|   |       |           _globals.cpython-310.pyc
|   |       |           _pytesttester.cpython-310.pyc
|   |       |           __config__.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---numpy-2.2.6.dist-info
|   |       |       DELVEWHEEL
|   |       |       entry_points.txt
|   |       |       INSTALLER
|   |       |       LICENSE.txt
|   |       |       METADATA
|   |       |       RECORD
|   |       |       WHEEL
|   |       |       
|   |       +---numpy.libs
|   |       |       libscipy_openblas64_-13e2df515630b4a41f92893938845698.dll
|   |       |       msvcp140-263139962577ecda4cd9469ca360a746.dll
|   |       |       
|   |       +---packaging
|   |       |   |   dependency_groups.py
|   |       |   |   direct_url.py
|   |       |   |   errors.py
|   |       |   |   markers.py
|   |       |   |   metadata.py
|   |       |   |   py.typed
|   |       |   |   pylock.py
|   |       |   |   requirements.py
|   |       |   |   specifiers.py
|   |       |   |   tags.py
|   |       |   |   utils.py
|   |       |   |   version.py
|   |       |   |   _elffile.py
|   |       |   |   _manylinux.py
|   |       |   |   _musllinux.py
|   |       |   |   _parser.py
|   |       |   |   _tokenizer.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---licenses
|   |       |   |   |   _spdx.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _spdx.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           dependency_groups.cpython-310.pyc
|   |       |           direct_url.cpython-310.pyc
|   |       |           errors.cpython-310.pyc
|   |       |           markers.cpython-310.pyc
|   |       |           metadata.cpython-310.pyc
|   |       |           pylock.cpython-310.pyc
|   |       |           requirements.cpython-310.pyc
|   |       |           specifiers.cpython-310.pyc
|   |       |           tags.cpython-310.pyc
|   |       |           utils.cpython-310.pyc
|   |       |           version.cpython-310.pyc
|   |       |           _elffile.cpython-310.pyc
|   |       |           _manylinux.cpython-310.pyc
|   |       |           _musllinux.cpython-310.pyc
|   |       |           _parser.cpython-310.pyc
|   |       |           _tokenizer.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---packaging-26.1.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           LICENSE.APACHE
|   |       |           LICENSE.BSD
|   |       |           
|   |       +---pandas
|   |       |   |   conftest.py
|   |       |   |   pyproject.toml
|   |       |   |   testing.py
|   |       |   |   _typing.py
|   |       |   |   _version.py
|   |       |   |   _version_meson.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---api
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---extensions
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---indexers
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---interchange
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---types
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---typing
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---arrays
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---compat
|   |       |   |   |   compressors.py
|   |       |   |   |   pickle_compat.py
|   |       |   |   |   pyarrow.py
|   |       |   |   |   _constants.py
|   |       |   |   |   _optional.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---numpy
|   |       |   |   |   |   function.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           function.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           compressors.cpython-310.pyc
|   |       |   |           pickle_compat.cpython-310.pyc
|   |       |   |           pyarrow.cpython-310.pyc
|   |       |   |           _constants.cpython-310.pyc
|   |       |   |           _optional.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---core
|   |       |   |   |   accessor.py
|   |       |   |   |   algorithms.py
|   |       |   |   |   api.py
|   |       |   |   |   apply.py
|   |       |   |   |   arraylike.py
|   |       |   |   |   base.py
|   |       |   |   |   common.py
|   |       |   |   |   config_init.py
|   |       |   |   |   construction.py
|   |       |   |   |   flags.py
|   |       |   |   |   frame.py
|   |       |   |   |   generic.py
|   |       |   |   |   indexing.py
|   |       |   |   |   missing.py
|   |       |   |   |   nanops.py
|   |       |   |   |   resample.py
|   |       |   |   |   roperator.py
|   |       |   |   |   sample.py
|   |       |   |   |   series.py
|   |       |   |   |   shared_docs.py
|   |       |   |   |   sorting.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---arrays
|   |       |   |   |   |   base.py
|   |       |   |   |   |   boolean.py
|   |       |   |   |   |   categorical.py
|   |       |   |   |   |   datetimelike.py
|   |       |   |   |   |   datetimes.py
|   |       |   |   |   |   floating.py
|   |       |   |   |   |   integer.py
|   |       |   |   |   |   interval.py
|   |       |   |   |   |   masked.py
|   |       |   |   |   |   numeric.py
|   |       |   |   |   |   numpy_.py
|   |       |   |   |   |   period.py
|   |       |   |   |   |   string_.py
|   |       |   |   |   |   string_arrow.py
|   |       |   |   |   |   timedeltas.py
|   |       |   |   |   |   _arrow_string_mixins.py
|   |       |   |   |   |   _mixins.py
|   |       |   |   |   |   _ranges.py
|   |       |   |   |   |   _utils.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---arrow
|   |       |   |   |   |   |   accessors.py
|   |       |   |   |   |   |   array.py
|   |       |   |   |   |   |   extension_types.py
|   |       |   |   |   |   |   _arrow_utils.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           accessors.cpython-310.pyc
|   |       |   |   |   |           array.cpython-310.pyc
|   |       |   |   |   |           extension_types.cpython-310.pyc
|   |       |   |   |   |           _arrow_utils.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---sparse
|   |       |   |   |   |   |   accessor.py
|   |       |   |   |   |   |   array.py
|   |       |   |   |   |   |   scipy_sparse.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           accessor.cpython-310.pyc
|   |       |   |   |   |           array.cpython-310.pyc
|   |       |   |   |   |           scipy_sparse.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           base.cpython-310.pyc
|   |       |   |   |           boolean.cpython-310.pyc
|   |       |   |   |           categorical.cpython-310.pyc
|   |       |   |   |           datetimelike.cpython-310.pyc
|   |       |   |   |           datetimes.cpython-310.pyc
|   |       |   |   |           floating.cpython-310.pyc
|   |       |   |   |           integer.cpython-310.pyc
|   |       |   |   |           interval.cpython-310.pyc
|   |       |   |   |           masked.cpython-310.pyc
|   |       |   |   |           numeric.cpython-310.pyc
|   |       |   |   |           numpy_.cpython-310.pyc
|   |       |   |   |           period.cpython-310.pyc
|   |       |   |   |           string_.cpython-310.pyc
|   |       |   |   |           string_arrow.cpython-310.pyc
|   |       |   |   |           timedeltas.cpython-310.pyc
|   |       |   |   |           _arrow_string_mixins.cpython-310.pyc
|   |       |   |   |           _mixins.cpython-310.pyc
|   |       |   |   |           _ranges.cpython-310.pyc
|   |       |   |   |           _utils.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---array_algos
|   |       |   |   |   |   datetimelike_accumulations.py
|   |       |   |   |   |   masked_accumulations.py
|   |       |   |   |   |   masked_reductions.py
|   |       |   |   |   |   putmask.py
|   |       |   |   |   |   quantile.py
|   |       |   |   |   |   replace.py
|   |       |   |   |   |   take.py
|   |       |   |   |   |   transforms.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           datetimelike_accumulations.cpython-310.pyc
|   |       |   |   |           masked_accumulations.cpython-310.pyc
|   |       |   |   |           masked_reductions.cpython-310.pyc
|   |       |   |   |           putmask.cpython-310.pyc
|   |       |   |   |           quantile.cpython-310.pyc
|   |       |   |   |           replace.cpython-310.pyc
|   |       |   |   |           take.cpython-310.pyc
|   |       |   |   |           transforms.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---computation
|   |       |   |   |   |   align.py
|   |       |   |   |   |   api.py
|   |       |   |   |   |   check.py
|   |       |   |   |   |   common.py
|   |       |   |   |   |   engines.py
|   |       |   |   |   |   eval.py
|   |       |   |   |   |   expr.py
|   |       |   |   |   |   expressions.py
|   |       |   |   |   |   ops.py
|   |       |   |   |   |   parsing.py
|   |       |   |   |   |   pytables.py
|   |       |   |   |   |   scope.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           align.cpython-310.pyc
|   |       |   |   |           api.cpython-310.pyc
|   |       |   |   |           check.cpython-310.pyc
|   |       |   |   |           common.cpython-310.pyc
|   |       |   |   |           engines.cpython-310.pyc
|   |       |   |   |           eval.cpython-310.pyc
|   |       |   |   |           expr.cpython-310.pyc
|   |       |   |   |           expressions.cpython-310.pyc
|   |       |   |   |           ops.cpython-310.pyc
|   |       |   |   |           parsing.cpython-310.pyc
|   |       |   |   |           pytables.cpython-310.pyc
|   |       |   |   |           scope.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---dtypes
|   |       |   |   |   |   api.py
|   |       |   |   |   |   astype.py
|   |       |   |   |   |   base.py
|   |       |   |   |   |   cast.py
|   |       |   |   |   |   common.py
|   |       |   |   |   |   concat.py
|   |       |   |   |   |   dtypes.py
|   |       |   |   |   |   generic.py
|   |       |   |   |   |   inference.py
|   |       |   |   |   |   missing.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           api.cpython-310.pyc
|   |       |   |   |           astype.cpython-310.pyc
|   |       |   |   |           base.cpython-310.pyc
|   |       |   |   |           cast.cpython-310.pyc
|   |       |   |   |           common.cpython-310.pyc
|   |       |   |   |           concat.cpython-310.pyc
|   |       |   |   |           dtypes.cpython-310.pyc
|   |       |   |   |           generic.cpython-310.pyc
|   |       |   |   |           inference.cpython-310.pyc
|   |       |   |   |           missing.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---groupby
|   |       |   |   |   |   base.py
|   |       |   |   |   |   categorical.py
|   |       |   |   |   |   generic.py
|   |       |   |   |   |   groupby.py
|   |       |   |   |   |   grouper.py
|   |       |   |   |   |   indexing.py
|   |       |   |   |   |   numba_.py
|   |       |   |   |   |   ops.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           base.cpython-310.pyc
|   |       |   |   |           categorical.cpython-310.pyc
|   |       |   |   |           generic.cpython-310.pyc
|   |       |   |   |           groupby.cpython-310.pyc
|   |       |   |   |           grouper.cpython-310.pyc
|   |       |   |   |           indexing.cpython-310.pyc
|   |       |   |   |           numba_.cpython-310.pyc
|   |       |   |   |           ops.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---indexers
|   |       |   |   |   |   objects.py
|   |       |   |   |   |   utils.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           objects.cpython-310.pyc
|   |       |   |   |           utils.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---indexes
|   |       |   |   |   |   accessors.py
|   |       |   |   |   |   api.py
|   |       |   |   |   |   base.py
|   |       |   |   |   |   category.py
|   |       |   |   |   |   datetimelike.py
|   |       |   |   |   |   datetimes.py
|   |       |   |   |   |   extension.py
|   |       |   |   |   |   frozen.py
|   |       |   |   |   |   interval.py
|   |       |   |   |   |   multi.py
|   |       |   |   |   |   period.py
|   |       |   |   |   |   range.py
|   |       |   |   |   |   timedeltas.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           accessors.cpython-310.pyc
|   |       |   |   |           api.cpython-310.pyc
|   |       |   |   |           base.cpython-310.pyc
|   |       |   |   |           category.cpython-310.pyc
|   |       |   |   |           datetimelike.cpython-310.pyc
|   |       |   |   |           datetimes.cpython-310.pyc
|   |       |   |   |           extension.cpython-310.pyc
|   |       |   |   |           frozen.cpython-310.pyc
|   |       |   |   |           interval.cpython-310.pyc
|   |       |   |   |           multi.cpython-310.pyc
|   |       |   |   |           period.cpython-310.pyc
|   |       |   |   |           range.cpython-310.pyc
|   |       |   |   |           timedeltas.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---interchange
|   |       |   |   |   |   buffer.py
|   |       |   |   |   |   column.py
|   |       |   |   |   |   dataframe.py
|   |       |   |   |   |   dataframe_protocol.py
|   |       |   |   |   |   from_dataframe.py
|   |       |   |   |   |   utils.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           buffer.cpython-310.pyc
|   |       |   |   |           column.cpython-310.pyc
|   |       |   |   |           dataframe.cpython-310.pyc
|   |       |   |   |           dataframe_protocol.cpython-310.pyc
|   |       |   |   |           from_dataframe.cpython-310.pyc
|   |       |   |   |           utils.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---internals
|   |       |   |   |   |   api.py
|   |       |   |   |   |   array_manager.py
|   |       |   |   |   |   base.py
|   |       |   |   |   |   blocks.py
|   |       |   |   |   |   concat.py
|   |       |   |   |   |   construction.py
|   |       |   |   |   |   managers.py
|   |       |   |   |   |   ops.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           api.cpython-310.pyc
|   |       |   |   |           array_manager.cpython-310.pyc
|   |       |   |   |           base.cpython-310.pyc
|   |       |   |   |           blocks.cpython-310.pyc
|   |       |   |   |           concat.cpython-310.pyc
|   |       |   |   |           construction.cpython-310.pyc
|   |       |   |   |           managers.cpython-310.pyc
|   |       |   |   |           ops.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---methods
|   |       |   |   |   |   describe.py
|   |       |   |   |   |   selectn.py
|   |       |   |   |   |   to_dict.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           describe.cpython-310.pyc
|   |       |   |   |           selectn.cpython-310.pyc
|   |       |   |   |           to_dict.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---ops
|   |       |   |   |   |   array_ops.py
|   |       |   |   |   |   common.py
|   |       |   |   |   |   dispatch.py
|   |       |   |   |   |   docstrings.py
|   |       |   |   |   |   invalid.py
|   |       |   |   |   |   mask_ops.py
|   |       |   |   |   |   missing.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           array_ops.cpython-310.pyc
|   |       |   |   |           common.cpython-310.pyc
|   |       |   |   |           dispatch.cpython-310.pyc
|   |       |   |   |           docstrings.cpython-310.pyc
|   |       |   |   |           invalid.cpython-310.pyc
|   |       |   |   |           mask_ops.cpython-310.pyc
|   |       |   |   |           missing.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---reshape
|   |       |   |   |   |   api.py
|   |       |   |   |   |   concat.py
|   |       |   |   |   |   encoding.py
|   |       |   |   |   |   melt.py
|   |       |   |   |   |   merge.py
|   |       |   |   |   |   pivot.py
|   |       |   |   |   |   reshape.py
|   |       |   |   |   |   tile.py
|   |       |   |   |   |   util.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           api.cpython-310.pyc
|   |       |   |   |           concat.cpython-310.pyc
|   |       |   |   |           encoding.cpython-310.pyc
|   |       |   |   |           melt.cpython-310.pyc
|   |       |   |   |           merge.cpython-310.pyc
|   |       |   |   |           pivot.cpython-310.pyc
|   |       |   |   |           reshape.cpython-310.pyc
|   |       |   |   |           tile.cpython-310.pyc
|   |       |   |   |           util.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---sparse
|   |       |   |   |   |   api.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           api.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---strings
|   |       |   |   |   |   accessor.py
|   |       |   |   |   |   base.py
|   |       |   |   |   |   object_array.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           accessor.cpython-310.pyc
|   |       |   |   |           base.cpython-310.pyc
|   |       |   |   |           object_array.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---tools
|   |       |   |   |   |   datetimes.py
|   |       |   |   |   |   numeric.py
|   |       |   |   |   |   timedeltas.py
|   |       |   |   |   |   times.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           datetimes.cpython-310.pyc
|   |       |   |   |           numeric.cpython-310.pyc
|   |       |   |   |           timedeltas.cpython-310.pyc
|   |       |   |   |           times.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---util
|   |       |   |   |   |   hashing.py
|   |       |   |   |   |   numba_.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           hashing.cpython-310.pyc
|   |       |   |   |           numba_.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---window
|   |       |   |   |   |   common.py
|   |       |   |   |   |   doc.py
|   |       |   |   |   |   ewm.py
|   |       |   |   |   |   expanding.py
|   |       |   |   |   |   numba_.py
|   |       |   |   |   |   online.py
|   |       |   |   |   |   rolling.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           common.cpython-310.pyc
|   |       |   |   |           doc.cpython-310.pyc
|   |       |   |   |           ewm.cpython-310.pyc
|   |       |   |   |           expanding.cpython-310.pyc
|   |       |   |   |           numba_.cpython-310.pyc
|   |       |   |   |           online.cpython-310.pyc
|   |       |   |   |           rolling.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---_numba
|   |       |   |   |   |   executor.py
|   |       |   |   |   |   extensions.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---kernels
|   |       |   |   |   |   |   mean_.py
|   |       |   |   |   |   |   min_max_.py
|   |       |   |   |   |   |   shared.py
|   |       |   |   |   |   |   sum_.py
|   |       |   |   |   |   |   var_.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           mean_.cpython-310.pyc
|   |       |   |   |   |           min_max_.cpython-310.pyc
|   |       |   |   |   |           shared.cpython-310.pyc
|   |       |   |   |   |           sum_.cpython-310.pyc
|   |       |   |   |   |           var_.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           executor.cpython-310.pyc
|   |       |   |   |           extensions.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           accessor.cpython-310.pyc
|   |       |   |           algorithms.cpython-310.pyc
|   |       |   |           api.cpython-310.pyc
|   |       |   |           apply.cpython-310.pyc
|   |       |   |           arraylike.cpython-310.pyc
|   |       |   |           base.cpython-310.pyc
|   |       |   |           common.cpython-310.pyc
|   |       |   |           config_init.cpython-310.pyc
|   |       |   |           construction.cpython-310.pyc
|   |       |   |           flags.cpython-310.pyc
|   |       |   |           frame.cpython-310.pyc
|   |       |   |           generic.cpython-310.pyc
|   |       |   |           indexing.cpython-310.pyc
|   |       |   |           missing.cpython-310.pyc
|   |       |   |           nanops.cpython-310.pyc
|   |       |   |           resample.cpython-310.pyc
|   |       |   |           roperator.cpython-310.pyc
|   |       |   |           sample.cpython-310.pyc
|   |       |   |           series.cpython-310.pyc
|   |       |   |           shared_docs.cpython-310.pyc
|   |       |   |           sorting.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---errors
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---io
|   |       |   |   |   api.py
|   |       |   |   |   clipboards.py
|   |       |   |   |   common.py
|   |       |   |   |   feather_format.py
|   |       |   |   |   gbq.py
|   |       |   |   |   html.py
|   |       |   |   |   orc.py
|   |       |   |   |   parquet.py
|   |       |   |   |   pickle.py
|   |       |   |   |   pytables.py
|   |       |   |   |   spss.py
|   |       |   |   |   sql.py
|   |       |   |   |   stata.py
|   |       |   |   |   xml.py
|   |       |   |   |   _util.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---clipboard
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---excel
|   |       |   |   |   |   _base.py
|   |       |   |   |   |   _calamine.py
|   |       |   |   |   |   _odfreader.py
|   |       |   |   |   |   _odswriter.py
|   |       |   |   |   |   _openpyxl.py
|   |       |   |   |   |   _pyxlsb.py
|   |       |   |   |   |   _util.py
|   |       |   |   |   |   _xlrd.py
|   |       |   |   |   |   _xlsxwriter.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _base.cpython-310.pyc
|   |       |   |   |           _calamine.cpython-310.pyc
|   |       |   |   |           _odfreader.cpython-310.pyc
|   |       |   |   |           _odswriter.cpython-310.pyc
|   |       |   |   |           _openpyxl.cpython-310.pyc
|   |       |   |   |           _pyxlsb.cpython-310.pyc
|   |       |   |   |           _util.cpython-310.pyc
|   |       |   |   |           _xlrd.cpython-310.pyc
|   |       |   |   |           _xlsxwriter.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---formats
|   |       |   |   |   |   console.py
|   |       |   |   |   |   css.py
|   |       |   |   |   |   csvs.py
|   |       |   |   |   |   excel.py
|   |       |   |   |   |   format.py
|   |       |   |   |   |   html.py
|   |       |   |   |   |   info.py
|   |       |   |   |   |   printing.py
|   |       |   |   |   |   string.py
|   |       |   |   |   |   style.py
|   |       |   |   |   |   style_render.py
|   |       |   |   |   |   xml.py
|   |       |   |   |   |   _color_data.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---templates
|   |       |   |   |   |       html.tpl
|   |       |   |   |   |       html_style.tpl
|   |       |   |   |   |       html_table.tpl
|   |       |   |   |   |       latex.tpl
|   |       |   |   |   |       latex_longtable.tpl
|   |       |   |   |   |       latex_table.tpl
|   |       |   |   |   |       string.tpl
|   |       |   |   |   |       
|   |       |   |   |   \---__pycache__
|   |       |   |   |           console.cpython-310.pyc
|   |       |   |   |           css.cpython-310.pyc
|   |       |   |   |           csvs.cpython-310.pyc
|   |       |   |   |           excel.cpython-310.pyc
|   |       |   |   |           format.cpython-310.pyc
|   |       |   |   |           html.cpython-310.pyc
|   |       |   |   |           info.cpython-310.pyc
|   |       |   |   |           printing.cpython-310.pyc
|   |       |   |   |           string.cpython-310.pyc
|   |       |   |   |           style.cpython-310.pyc
|   |       |   |   |           style_render.cpython-310.pyc
|   |       |   |   |           xml.cpython-310.pyc
|   |       |   |   |           _color_data.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---json
|   |       |   |   |   |   _json.py
|   |       |   |   |   |   _normalize.py
|   |       |   |   |   |   _table_schema.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _json.cpython-310.pyc
|   |       |   |   |           _normalize.cpython-310.pyc
|   |       |   |   |           _table_schema.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---parsers
|   |       |   |   |   |   arrow_parser_wrapper.py
|   |       |   |   |   |   base_parser.py
|   |       |   |   |   |   c_parser_wrapper.py
|   |       |   |   |   |   python_parser.py
|   |       |   |   |   |   readers.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           arrow_parser_wrapper.cpython-310.pyc
|   |       |   |   |           base_parser.cpython-310.pyc
|   |       |   |   |           c_parser_wrapper.cpython-310.pyc
|   |       |   |   |           python_parser.cpython-310.pyc
|   |       |   |   |           readers.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---sas
|   |       |   |   |   |   sas7bdat.py
|   |       |   |   |   |   sasreader.py
|   |       |   |   |   |   sas_constants.py
|   |       |   |   |   |   sas_xport.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           sas7bdat.cpython-310.pyc
|   |       |   |   |           sasreader.cpython-310.pyc
|   |       |   |   |           sas_constants.cpython-310.pyc
|   |       |   |   |           sas_xport.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           api.cpython-310.pyc
|   |       |   |           clipboards.cpython-310.pyc
|   |       |   |           common.cpython-310.pyc
|   |       |   |           feather_format.cpython-310.pyc
|   |       |   |           gbq.cpython-310.pyc
|   |       |   |           html.cpython-310.pyc
|   |       |   |           orc.cpython-310.pyc
|   |       |   |           parquet.cpython-310.pyc
|   |       |   |           pickle.cpython-310.pyc
|   |       |   |           pytables.cpython-310.pyc
|   |       |   |           spss.cpython-310.pyc
|   |       |   |           sql.cpython-310.pyc
|   |       |   |           stata.cpython-310.pyc
|   |       |   |           xml.cpython-310.pyc
|   |       |   |           _util.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---plotting
|   |       |   |   |   _core.py
|   |       |   |   |   _misc.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---_matplotlib
|   |       |   |   |   |   boxplot.py
|   |       |   |   |   |   converter.py
|   |       |   |   |   |   core.py
|   |       |   |   |   |   groupby.py
|   |       |   |   |   |   hist.py
|   |       |   |   |   |   misc.py
|   |       |   |   |   |   style.py
|   |       |   |   |   |   timeseries.py
|   |       |   |   |   |   tools.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           boxplot.cpython-310.pyc
|   |       |   |   |           converter.cpython-310.pyc
|   |       |   |   |           core.cpython-310.pyc
|   |       |   |   |           groupby.cpython-310.pyc
|   |       |   |   |           hist.cpython-310.pyc
|   |       |   |   |           misc.cpython-310.pyc
|   |       |   |   |           style.cpython-310.pyc
|   |       |   |   |           timeseries.cpython-310.pyc
|   |       |   |   |           tools.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           _core.cpython-310.pyc
|   |       |   |           _misc.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---tests
|   |       |   |   |   test_aggregation.py
|   |       |   |   |   test_algos.py
|   |       |   |   |   test_common.py
|   |       |   |   |   test_downstream.py
|   |       |   |   |   test_errors.py
|   |       |   |   |   test_expressions.py
|   |       |   |   |   test_flags.py
|   |       |   |   |   test_multilevel.py
|   |       |   |   |   test_nanops.py
|   |       |   |   |   test_optional_dependency.py
|   |       |   |   |   test_register_accessor.py
|   |       |   |   |   test_sorting.py
|   |       |   |   |   test_take.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---api
|   |       |   |   |   |   test_api.py
|   |       |   |   |   |   test_types.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_api.cpython-310.pyc
|   |       |   |   |           test_types.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---apply
|   |       |   |   |   |   common.py
|   |       |   |   |   |   test_frame_apply.py
|   |       |   |   |   |   test_frame_apply_relabeling.py
|   |       |   |   |   |   test_frame_transform.py
|   |       |   |   |   |   test_invalid_arg.py
|   |       |   |   |   |   test_numba.py
|   |       |   |   |   |   test_series_apply.py
|   |       |   |   |   |   test_series_apply_relabeling.py
|   |       |   |   |   |   test_series_transform.py
|   |       |   |   |   |   test_str.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           common.cpython-310.pyc
|   |       |   |   |           test_frame_apply.cpython-310.pyc
|   |       |   |   |           test_frame_apply_relabeling.cpython-310.pyc
|   |       |   |   |           test_frame_transform.cpython-310.pyc
|   |       |   |   |           test_invalid_arg.cpython-310.pyc
|   |       |   |   |           test_numba.cpython-310.pyc
|   |       |   |   |           test_series_apply.cpython-310.pyc
|   |       |   |   |           test_series_apply_relabeling.cpython-310.pyc
|   |       |   |   |           test_series_transform.cpython-310.pyc
|   |       |   |   |           test_str.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---arithmetic
|   |       |   |   |   |   common.py
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_array_ops.py
|   |       |   |   |   |   test_categorical.py
|   |       |   |   |   |   test_datetime64.py
|   |       |   |   |   |   test_interval.py
|   |       |   |   |   |   test_numeric.py
|   |       |   |   |   |   test_object.py
|   |       |   |   |   |   test_period.py
|   |       |   |   |   |   test_timedelta64.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           common.cpython-310.pyc
|   |       |   |   |           conftest.cpython-310.pyc
|   |       |   |   |           test_array_ops.cpython-310.pyc
|   |       |   |   |           test_categorical.cpython-310.pyc
|   |       |   |   |           test_datetime64.cpython-310.pyc
|   |       |   |   |           test_interval.cpython-310.pyc
|   |       |   |   |           test_numeric.cpython-310.pyc
|   |       |   |   |           test_object.cpython-310.pyc
|   |       |   |   |           test_period.cpython-310.pyc
|   |       |   |   |           test_timedelta64.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---arrays
|   |       |   |   |   |   masked_shared.py
|   |       |   |   |   |   test_array.py
|   |       |   |   |   |   test_datetimelike.py
|   |       |   |   |   |   test_datetimes.py
|   |       |   |   |   |   test_ndarray_backed.py
|   |       |   |   |   |   test_period.py
|   |       |   |   |   |   test_timedeltas.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---boolean
|   |       |   |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_comparison.py
|   |       |   |   |   |   |   test_construction.py
|   |       |   |   |   |   |   test_function.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_logical.py
|   |       |   |   |   |   |   test_ops.py
|   |       |   |   |   |   |   test_reduction.py
|   |       |   |   |   |   |   test_repr.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_arithmetic.cpython-310.pyc
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_comparison.cpython-310.pyc
|   |       |   |   |   |           test_construction.cpython-310.pyc
|   |       |   |   |   |           test_function.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_logical.cpython-310.pyc
|   |       |   |   |   |           test_ops.cpython-310.pyc
|   |       |   |   |   |           test_reduction.cpython-310.pyc
|   |       |   |   |   |           test_repr.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---categorical
|   |       |   |   |   |   |   test_algos.py
|   |       |   |   |   |   |   test_analytics.py
|   |       |   |   |   |   |   test_api.py
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_dtypes.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_map.py
|   |       |   |   |   |   |   test_missing.py
|   |       |   |   |   |   |   test_operators.py
|   |       |   |   |   |   |   test_replace.py
|   |       |   |   |   |   |   test_repr.py
|   |       |   |   |   |   |   test_sorting.py
|   |       |   |   |   |   |   test_subclass.py
|   |       |   |   |   |   |   test_take.py
|   |       |   |   |   |   |   test_warnings.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_algos.cpython-310.pyc
|   |       |   |   |   |           test_analytics.cpython-310.pyc
|   |       |   |   |   |           test_api.cpython-310.pyc
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_dtypes.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_map.cpython-310.pyc
|   |       |   |   |   |           test_missing.cpython-310.pyc
|   |       |   |   |   |           test_operators.cpython-310.pyc
|   |       |   |   |   |           test_replace.cpython-310.pyc
|   |       |   |   |   |           test_repr.cpython-310.pyc
|   |       |   |   |   |           test_sorting.cpython-310.pyc
|   |       |   |   |   |           test_subclass.cpython-310.pyc
|   |       |   |   |   |           test_take.cpython-310.pyc
|   |       |   |   |   |           test_warnings.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---datetimes
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_cumulative.py
|   |       |   |   |   |   |   test_reductions.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_cumulative.cpython-310.pyc
|   |       |   |   |   |           test_reductions.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---floating
|   |       |   |   |   |   |   conftest.py
|   |       |   |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_comparison.py
|   |       |   |   |   |   |   test_concat.py
|   |       |   |   |   |   |   test_construction.py
|   |       |   |   |   |   |   test_contains.py
|   |       |   |   |   |   |   test_function.py
|   |       |   |   |   |   |   test_repr.py
|   |       |   |   |   |   |   test_to_numpy.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           conftest.cpython-310.pyc
|   |       |   |   |   |           test_arithmetic.cpython-310.pyc
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_comparison.cpython-310.pyc
|   |       |   |   |   |           test_concat.cpython-310.pyc
|   |       |   |   |   |           test_construction.cpython-310.pyc
|   |       |   |   |   |           test_contains.cpython-310.pyc
|   |       |   |   |   |           test_function.cpython-310.pyc
|   |       |   |   |   |           test_repr.cpython-310.pyc
|   |       |   |   |   |           test_to_numpy.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---integer
|   |       |   |   |   |   |   conftest.py
|   |       |   |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   |   test_comparison.py
|   |       |   |   |   |   |   test_concat.py
|   |       |   |   |   |   |   test_construction.py
|   |       |   |   |   |   |   test_dtypes.py
|   |       |   |   |   |   |   test_function.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_reduction.py
|   |       |   |   |   |   |   test_repr.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           conftest.cpython-310.pyc
|   |       |   |   |   |           test_arithmetic.cpython-310.pyc
|   |       |   |   |   |           test_comparison.cpython-310.pyc
|   |       |   |   |   |           test_concat.cpython-310.pyc
|   |       |   |   |   |           test_construction.cpython-310.pyc
|   |       |   |   |   |           test_dtypes.cpython-310.pyc
|   |       |   |   |   |           test_function.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_reduction.cpython-310.pyc
|   |       |   |   |   |           test_repr.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---interval
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_interval.py
|   |       |   |   |   |   |   test_interval_pyarrow.py
|   |       |   |   |   |   |   test_overlaps.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_formats.cpython-310.pyc
|   |       |   |   |   |           test_interval.cpython-310.pyc
|   |       |   |   |   |           test_interval_pyarrow.cpython-310.pyc
|   |       |   |   |   |           test_overlaps.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---masked
|   |       |   |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   |   test_arrow_compat.py
|   |       |   |   |   |   |   test_function.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_arithmetic.cpython-310.pyc
|   |       |   |   |   |           test_arrow_compat.cpython-310.pyc
|   |       |   |   |   |           test_function.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---numpy_
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_numpy.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_numpy.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---period
|   |       |   |   |   |   |   test_arrow_compat.py
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_reductions.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_arrow_compat.cpython-310.pyc
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_reductions.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---sparse
|   |       |   |   |   |   |   test_accessor.py
|   |       |   |   |   |   |   test_arithmetics.py
|   |       |   |   |   |   |   test_array.py
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_combine_concat.py
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_dtype.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_libsparse.py
|   |       |   |   |   |   |   test_reductions.py
|   |       |   |   |   |   |   test_unary.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_accessor.cpython-310.pyc
|   |       |   |   |   |           test_arithmetics.cpython-310.pyc
|   |       |   |   |   |           test_array.cpython-310.pyc
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_combine_concat.cpython-310.pyc
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_dtype.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_libsparse.cpython-310.pyc
|   |       |   |   |   |           test_reductions.cpython-310.pyc
|   |       |   |   |   |           test_unary.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---string_
|   |       |   |   |   |   |   test_concat.py
|   |       |   |   |   |   |   test_string.py
|   |       |   |   |   |   |   test_string_arrow.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_concat.cpython-310.pyc
|   |       |   |   |   |           test_string.cpython-310.pyc
|   |       |   |   |   |           test_string_arrow.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---timedeltas
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_cumulative.py
|   |       |   |   |   |   |   test_reductions.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_cumulative.cpython-310.pyc
|   |       |   |   |   |           test_reductions.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           masked_shared.cpython-310.pyc
|   |       |   |   |           test_array.cpython-310.pyc
|   |       |   |   |           test_datetimelike.cpython-310.pyc
|   |       |   |   |           test_datetimes.cpython-310.pyc
|   |       |   |   |           test_ndarray_backed.cpython-310.pyc
|   |       |   |   |           test_period.cpython-310.pyc
|   |       |   |   |           test_timedeltas.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---base
|   |       |   |   |   |   common.py
|   |       |   |   |   |   test_constructors.py
|   |       |   |   |   |   test_conversion.py
|   |       |   |   |   |   test_fillna.py
|   |       |   |   |   |   test_misc.py
|   |       |   |   |   |   test_transpose.py
|   |       |   |   |   |   test_unique.py
|   |       |   |   |   |   test_value_counts.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           common.cpython-310.pyc
|   |       |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |           test_conversion.cpython-310.pyc
|   |       |   |   |           test_fillna.cpython-310.pyc
|   |       |   |   |           test_misc.cpython-310.pyc
|   |       |   |   |           test_transpose.cpython-310.pyc
|   |       |   |   |           test_unique.cpython-310.pyc
|   |       |   |   |           test_value_counts.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---computation
|   |       |   |   |   |   test_compat.py
|   |       |   |   |   |   test_eval.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_compat.cpython-310.pyc
|   |       |   |   |           test_eval.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---config
|   |       |   |   |   |   test_config.py
|   |       |   |   |   |   test_localization.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_config.cpython-310.pyc
|   |       |   |   |           test_localization.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---construction
|   |       |   |   |   |   test_extract_array.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_extract_array.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---copy_view
|   |       |   |   |   |   test_array.py
|   |       |   |   |   |   test_astype.py
|   |       |   |   |   |   test_chained_assignment_deprecation.py
|   |       |   |   |   |   test_clip.py
|   |       |   |   |   |   test_constructors.py
|   |       |   |   |   |   test_core_functionalities.py
|   |       |   |   |   |   test_functions.py
|   |       |   |   |   |   test_indexing.py
|   |       |   |   |   |   test_internals.py
|   |       |   |   |   |   test_interp_fillna.py
|   |       |   |   |   |   test_methods.py
|   |       |   |   |   |   test_replace.py
|   |       |   |   |   |   test_setitem.py
|   |       |   |   |   |   test_util.py
|   |       |   |   |   |   util.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---index
|   |       |   |   |   |   |   test_datetimeindex.py
|   |       |   |   |   |   |   test_index.py
|   |       |   |   |   |   |   test_periodindex.py
|   |       |   |   |   |   |   test_timedeltaindex.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_datetimeindex.cpython-310.pyc
|   |       |   |   |   |           test_index.cpython-310.pyc
|   |       |   |   |   |           test_periodindex.cpython-310.pyc
|   |       |   |   |   |           test_timedeltaindex.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_array.cpython-310.pyc
|   |       |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |           test_chained_assignment_deprecation.cpython-310.pyc
|   |       |   |   |           test_clip.cpython-310.pyc
|   |       |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |           test_core_functionalities.cpython-310.pyc
|   |       |   |   |           test_functions.cpython-310.pyc
|   |       |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |           test_internals.cpython-310.pyc
|   |       |   |   |           test_interp_fillna.cpython-310.pyc
|   |       |   |   |           test_methods.cpython-310.pyc
|   |       |   |   |           test_replace.cpython-310.pyc
|   |       |   |   |           test_setitem.cpython-310.pyc
|   |       |   |   |           test_util.cpython-310.pyc
|   |       |   |   |           util.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---dtypes
|   |       |   |   |   |   test_common.py
|   |       |   |   |   |   test_concat.py
|   |       |   |   |   |   test_dtypes.py
|   |       |   |   |   |   test_generic.py
|   |       |   |   |   |   test_inference.py
|   |       |   |   |   |   test_missing.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---cast
|   |       |   |   |   |   |   test_can_hold_element.py
|   |       |   |   |   |   |   test_construct_from_scalar.py
|   |       |   |   |   |   |   test_construct_ndarray.py
|   |       |   |   |   |   |   test_construct_object_arr.py
|   |       |   |   |   |   |   test_dict_compat.py
|   |       |   |   |   |   |   test_downcast.py
|   |       |   |   |   |   |   test_find_common_type.py
|   |       |   |   |   |   |   test_infer_datetimelike.py
|   |       |   |   |   |   |   test_infer_dtype.py
|   |       |   |   |   |   |   test_maybe_box_native.py
|   |       |   |   |   |   |   test_promote.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_can_hold_element.cpython-310.pyc
|   |       |   |   |   |           test_construct_from_scalar.cpython-310.pyc
|   |       |   |   |   |           test_construct_ndarray.cpython-310.pyc
|   |       |   |   |   |           test_construct_object_arr.cpython-310.pyc
|   |       |   |   |   |           test_dict_compat.cpython-310.pyc
|   |       |   |   |   |           test_downcast.cpython-310.pyc
|   |       |   |   |   |           test_find_common_type.cpython-310.pyc
|   |       |   |   |   |           test_infer_datetimelike.cpython-310.pyc
|   |       |   |   |   |           test_infer_dtype.cpython-310.pyc
|   |       |   |   |   |           test_maybe_box_native.cpython-310.pyc
|   |       |   |   |   |           test_promote.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_common.cpython-310.pyc
|   |       |   |   |           test_concat.cpython-310.pyc
|   |       |   |   |           test_dtypes.cpython-310.pyc
|   |       |   |   |           test_generic.cpython-310.pyc
|   |       |   |   |           test_inference.cpython-310.pyc
|   |       |   |   |           test_missing.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---extension
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_arrow.py
|   |       |   |   |   |   test_categorical.py
|   |       |   |   |   |   test_common.py
|   |       |   |   |   |   test_datetime.py
|   |       |   |   |   |   test_extension.py
|   |       |   |   |   |   test_interval.py
|   |       |   |   |   |   test_masked.py
|   |       |   |   |   |   test_numpy.py
|   |       |   |   |   |   test_period.py
|   |       |   |   |   |   test_sparse.py
|   |       |   |   |   |   test_string.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---array_with_attr
|   |       |   |   |   |   |   array.py
|   |       |   |   |   |   |   test_array_with_attr.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           array.cpython-310.pyc
|   |       |   |   |   |           test_array_with_attr.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---base
|   |       |   |   |   |   |   accumulate.py
|   |       |   |   |   |   |   base.py
|   |       |   |   |   |   |   casting.py
|   |       |   |   |   |   |   constructors.py
|   |       |   |   |   |   |   dim2.py
|   |       |   |   |   |   |   dtype.py
|   |       |   |   |   |   |   getitem.py
|   |       |   |   |   |   |   groupby.py
|   |       |   |   |   |   |   index.py
|   |       |   |   |   |   |   interface.py
|   |       |   |   |   |   |   io.py
|   |       |   |   |   |   |   methods.py
|   |       |   |   |   |   |   missing.py
|   |       |   |   |   |   |   ops.py
|   |       |   |   |   |   |   printing.py
|   |       |   |   |   |   |   reduce.py
|   |       |   |   |   |   |   reshaping.py
|   |       |   |   |   |   |   setitem.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           accumulate.cpython-310.pyc
|   |       |   |   |   |           base.cpython-310.pyc
|   |       |   |   |   |           casting.cpython-310.pyc
|   |       |   |   |   |           constructors.cpython-310.pyc
|   |       |   |   |   |           dim2.cpython-310.pyc
|   |       |   |   |   |           dtype.cpython-310.pyc
|   |       |   |   |   |           getitem.cpython-310.pyc
|   |       |   |   |   |           groupby.cpython-310.pyc
|   |       |   |   |   |           index.cpython-310.pyc
|   |       |   |   |   |           interface.cpython-310.pyc
|   |       |   |   |   |           io.cpython-310.pyc
|   |       |   |   |   |           methods.cpython-310.pyc
|   |       |   |   |   |           missing.cpython-310.pyc
|   |       |   |   |   |           ops.cpython-310.pyc
|   |       |   |   |   |           printing.cpython-310.pyc
|   |       |   |   |   |           reduce.cpython-310.pyc
|   |       |   |   |   |           reshaping.cpython-310.pyc
|   |       |   |   |   |           setitem.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---date
|   |       |   |   |   |   |   array.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           array.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---decimal
|   |       |   |   |   |   |   array.py
|   |       |   |   |   |   |   test_decimal.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           array.cpython-310.pyc
|   |       |   |   |   |           test_decimal.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---json
|   |       |   |   |   |   |   array.py
|   |       |   |   |   |   |   test_json.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           array.cpython-310.pyc
|   |       |   |   |   |           test_json.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---list
|   |       |   |   |   |   |   array.py
|   |       |   |   |   |   |   test_list.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           array.cpython-310.pyc
|   |       |   |   |   |           test_list.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           conftest.cpython-310.pyc
|   |       |   |   |           test_arrow.cpython-310.pyc
|   |       |   |   |           test_categorical.cpython-310.pyc
|   |       |   |   |           test_common.cpython-310.pyc
|   |       |   |   |           test_datetime.cpython-310.pyc
|   |       |   |   |           test_extension.cpython-310.pyc
|   |       |   |   |           test_interval.cpython-310.pyc
|   |       |   |   |           test_masked.cpython-310.pyc
|   |       |   |   |           test_numpy.cpython-310.pyc
|   |       |   |   |           test_period.cpython-310.pyc
|   |       |   |   |           test_sparse.cpython-310.pyc
|   |       |   |   |           test_string.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---frame
|   |       |   |   |   |   common.py
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_alter_axes.py
|   |       |   |   |   |   test_api.py
|   |       |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   test_arrow_interface.py
|   |       |   |   |   |   test_block_internals.py
|   |       |   |   |   |   test_constructors.py
|   |       |   |   |   |   test_cumulative.py
|   |       |   |   |   |   test_iteration.py
|   |       |   |   |   |   test_logical_ops.py
|   |       |   |   |   |   test_nonunique_indexes.py
|   |       |   |   |   |   test_npfuncs.py
|   |       |   |   |   |   test_query_eval.py
|   |       |   |   |   |   test_reductions.py
|   |       |   |   |   |   test_repr.py
|   |       |   |   |   |   test_stack_unstack.py
|   |       |   |   |   |   test_subclass.py
|   |       |   |   |   |   test_ufunc.py
|   |       |   |   |   |   test_unary.py
|   |       |   |   |   |   test_validate.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---constructors
|   |       |   |   |   |   |   test_from_dict.py
|   |       |   |   |   |   |   test_from_records.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_from_dict.cpython-310.pyc
|   |       |   |   |   |           test_from_records.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---indexing
|   |       |   |   |   |   |   test_coercion.py
|   |       |   |   |   |   |   test_delitem.py
|   |       |   |   |   |   |   test_get.py
|   |       |   |   |   |   |   test_getitem.py
|   |       |   |   |   |   |   test_get_value.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_insert.py
|   |       |   |   |   |   |   test_mask.py
|   |       |   |   |   |   |   test_setitem.py
|   |       |   |   |   |   |   test_set_value.py
|   |       |   |   |   |   |   test_take.py
|   |       |   |   |   |   |   test_where.py
|   |       |   |   |   |   |   test_xs.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_coercion.cpython-310.pyc
|   |       |   |   |   |           test_delitem.cpython-310.pyc
|   |       |   |   |   |           test_get.cpython-310.pyc
|   |       |   |   |   |           test_getitem.cpython-310.pyc
|   |       |   |   |   |           test_get_value.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_insert.cpython-310.pyc
|   |       |   |   |   |           test_mask.cpython-310.pyc
|   |       |   |   |   |           test_setitem.cpython-310.pyc
|   |       |   |   |   |           test_set_value.cpython-310.pyc
|   |       |   |   |   |           test_take.cpython-310.pyc
|   |       |   |   |   |           test_where.cpython-310.pyc
|   |       |   |   |   |           test_xs.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---methods
|   |       |   |   |   |   |   test_add_prefix_suffix.py
|   |       |   |   |   |   |   test_align.py
|   |       |   |   |   |   |   test_asfreq.py
|   |       |   |   |   |   |   test_asof.py
|   |       |   |   |   |   |   test_assign.py
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_at_time.py
|   |       |   |   |   |   |   test_between_time.py
|   |       |   |   |   |   |   test_clip.py
|   |       |   |   |   |   |   test_combine.py
|   |       |   |   |   |   |   test_combine_first.py
|   |       |   |   |   |   |   test_compare.py
|   |       |   |   |   |   |   test_convert_dtypes.py
|   |       |   |   |   |   |   test_copy.py
|   |       |   |   |   |   |   test_count.py
|   |       |   |   |   |   |   test_cov_corr.py
|   |       |   |   |   |   |   test_describe.py
|   |       |   |   |   |   |   test_diff.py
|   |       |   |   |   |   |   test_dot.py
|   |       |   |   |   |   |   test_drop.py
|   |       |   |   |   |   |   test_droplevel.py
|   |       |   |   |   |   |   test_dropna.py
|   |       |   |   |   |   |   test_drop_duplicates.py
|   |       |   |   |   |   |   test_dtypes.py
|   |       |   |   |   |   |   test_duplicated.py
|   |       |   |   |   |   |   test_equals.py
|   |       |   |   |   |   |   test_explode.py
|   |       |   |   |   |   |   test_fillna.py
|   |       |   |   |   |   |   test_filter.py
|   |       |   |   |   |   |   test_first_and_last.py
|   |       |   |   |   |   |   test_first_valid_index.py
|   |       |   |   |   |   |   test_get_numeric_data.py
|   |       |   |   |   |   |   test_head_tail.py
|   |       |   |   |   |   |   test_infer_objects.py
|   |       |   |   |   |   |   test_info.py
|   |       |   |   |   |   |   test_interpolate.py
|   |       |   |   |   |   |   test_isetitem.py
|   |       |   |   |   |   |   test_isin.py
|   |       |   |   |   |   |   test_is_homogeneous_dtype.py
|   |       |   |   |   |   |   test_iterrows.py
|   |       |   |   |   |   |   test_join.py
|   |       |   |   |   |   |   test_map.py
|   |       |   |   |   |   |   test_matmul.py
|   |       |   |   |   |   |   test_nlargest.py
|   |       |   |   |   |   |   test_pct_change.py
|   |       |   |   |   |   |   test_pipe.py
|   |       |   |   |   |   |   test_pop.py
|   |       |   |   |   |   |   test_quantile.py
|   |       |   |   |   |   |   test_rank.py
|   |       |   |   |   |   |   test_reindex.py
|   |       |   |   |   |   |   test_reindex_like.py
|   |       |   |   |   |   |   test_rename.py
|   |       |   |   |   |   |   test_rename_axis.py
|   |       |   |   |   |   |   test_reorder_levels.py
|   |       |   |   |   |   |   test_replace.py
|   |       |   |   |   |   |   test_reset_index.py
|   |       |   |   |   |   |   test_round.py
|   |       |   |   |   |   |   test_sample.py
|   |       |   |   |   |   |   test_select_dtypes.py
|   |       |   |   |   |   |   test_set_axis.py
|   |       |   |   |   |   |   test_set_index.py
|   |       |   |   |   |   |   test_shift.py
|   |       |   |   |   |   |   test_size.py
|   |       |   |   |   |   |   test_sort_index.py
|   |       |   |   |   |   |   test_sort_values.py
|   |       |   |   |   |   |   test_swapaxes.py
|   |       |   |   |   |   |   test_swaplevel.py
|   |       |   |   |   |   |   test_to_csv.py
|   |       |   |   |   |   |   test_to_dict.py
|   |       |   |   |   |   |   test_to_dict_of_blocks.py
|   |       |   |   |   |   |   test_to_numpy.py
|   |       |   |   |   |   |   test_to_period.py
|   |       |   |   |   |   |   test_to_records.py
|   |       |   |   |   |   |   test_to_timestamp.py
|   |       |   |   |   |   |   test_transpose.py
|   |       |   |   |   |   |   test_truncate.py
|   |       |   |   |   |   |   test_tz_convert.py
|   |       |   |   |   |   |   test_tz_localize.py
|   |       |   |   |   |   |   test_update.py
|   |       |   |   |   |   |   test_values.py
|   |       |   |   |   |   |   test_value_counts.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_add_prefix_suffix.cpython-310.pyc
|   |       |   |   |   |           test_align.cpython-310.pyc
|   |       |   |   |   |           test_asfreq.cpython-310.pyc
|   |       |   |   |   |           test_asof.cpython-310.pyc
|   |       |   |   |   |           test_assign.cpython-310.pyc
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_at_time.cpython-310.pyc
|   |       |   |   |   |           test_between_time.cpython-310.pyc
|   |       |   |   |   |           test_clip.cpython-310.pyc
|   |       |   |   |   |           test_combine.cpython-310.pyc
|   |       |   |   |   |           test_combine_first.cpython-310.pyc
|   |       |   |   |   |           test_compare.cpython-310.pyc
|   |       |   |   |   |           test_convert_dtypes.cpython-310.pyc
|   |       |   |   |   |           test_copy.cpython-310.pyc
|   |       |   |   |   |           test_count.cpython-310.pyc
|   |       |   |   |   |           test_cov_corr.cpython-310.pyc
|   |       |   |   |   |           test_describe.cpython-310.pyc
|   |       |   |   |   |           test_diff.cpython-310.pyc
|   |       |   |   |   |           test_dot.cpython-310.pyc
|   |       |   |   |   |           test_drop.cpython-310.pyc
|   |       |   |   |   |           test_droplevel.cpython-310.pyc
|   |       |   |   |   |           test_dropna.cpython-310.pyc
|   |       |   |   |   |           test_drop_duplicates.cpython-310.pyc
|   |       |   |   |   |           test_dtypes.cpython-310.pyc
|   |       |   |   |   |           test_duplicated.cpython-310.pyc
|   |       |   |   |   |           test_equals.cpython-310.pyc
|   |       |   |   |   |           test_explode.cpython-310.pyc
|   |       |   |   |   |           test_fillna.cpython-310.pyc
|   |       |   |   |   |           test_filter.cpython-310.pyc
|   |       |   |   |   |           test_first_and_last.cpython-310.pyc
|   |       |   |   |   |           test_first_valid_index.cpython-310.pyc
|   |       |   |   |   |           test_get_numeric_data.cpython-310.pyc
|   |       |   |   |   |           test_head_tail.cpython-310.pyc
|   |       |   |   |   |           test_infer_objects.cpython-310.pyc
|   |       |   |   |   |           test_info.cpython-310.pyc
|   |       |   |   |   |           test_interpolate.cpython-310.pyc
|   |       |   |   |   |           test_isetitem.cpython-310.pyc
|   |       |   |   |   |           test_isin.cpython-310.pyc
|   |       |   |   |   |           test_is_homogeneous_dtype.cpython-310.pyc
|   |       |   |   |   |           test_iterrows.cpython-310.pyc
|   |       |   |   |   |           test_join.cpython-310.pyc
|   |       |   |   |   |           test_map.cpython-310.pyc
|   |       |   |   |   |           test_matmul.cpython-310.pyc
|   |       |   |   |   |           test_nlargest.cpython-310.pyc
|   |       |   |   |   |           test_pct_change.cpython-310.pyc
|   |       |   |   |   |           test_pipe.cpython-310.pyc
|   |       |   |   |   |           test_pop.cpython-310.pyc
|   |       |   |   |   |           test_quantile.cpython-310.pyc
|   |       |   |   |   |           test_rank.cpython-310.pyc
|   |       |   |   |   |           test_reindex.cpython-310.pyc
|   |       |   |   |   |           test_reindex_like.cpython-310.pyc
|   |       |   |   |   |           test_rename.cpython-310.pyc
|   |       |   |   |   |           test_rename_axis.cpython-310.pyc
|   |       |   |   |   |           test_reorder_levels.cpython-310.pyc
|   |       |   |   |   |           test_replace.cpython-310.pyc
|   |       |   |   |   |           test_reset_index.cpython-310.pyc
|   |       |   |   |   |           test_round.cpython-310.pyc
|   |       |   |   |   |           test_sample.cpython-310.pyc
|   |       |   |   |   |           test_select_dtypes.cpython-310.pyc
|   |       |   |   |   |           test_set_axis.cpython-310.pyc
|   |       |   |   |   |           test_set_index.cpython-310.pyc
|   |       |   |   |   |           test_shift.cpython-310.pyc
|   |       |   |   |   |           test_size.cpython-310.pyc
|   |       |   |   |   |           test_sort_index.cpython-310.pyc
|   |       |   |   |   |           test_sort_values.cpython-310.pyc
|   |       |   |   |   |           test_swapaxes.cpython-310.pyc
|   |       |   |   |   |           test_swaplevel.cpython-310.pyc
|   |       |   |   |   |           test_to_csv.cpython-310.pyc
|   |       |   |   |   |           test_to_dict.cpython-310.pyc
|   |       |   |   |   |           test_to_dict_of_blocks.cpython-310.pyc
|   |       |   |   |   |           test_to_numpy.cpython-310.pyc
|   |       |   |   |   |           test_to_period.cpython-310.pyc
|   |       |   |   |   |           test_to_records.cpython-310.pyc
|   |       |   |   |   |           test_to_timestamp.cpython-310.pyc
|   |       |   |   |   |           test_transpose.cpython-310.pyc
|   |       |   |   |   |           test_truncate.cpython-310.pyc
|   |       |   |   |   |           test_tz_convert.cpython-310.pyc
|   |       |   |   |   |           test_tz_localize.cpython-310.pyc
|   |       |   |   |   |           test_update.cpython-310.pyc
|   |       |   |   |   |           test_values.cpython-310.pyc
|   |       |   |   |   |           test_value_counts.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           common.cpython-310.pyc
|   |       |   |   |           conftest.cpython-310.pyc
|   |       |   |   |           test_alter_axes.cpython-310.pyc
|   |       |   |   |           test_api.cpython-310.pyc
|   |       |   |   |           test_arithmetic.cpython-310.pyc
|   |       |   |   |           test_arrow_interface.cpython-310.pyc
|   |       |   |   |           test_block_internals.cpython-310.pyc
|   |       |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |           test_cumulative.cpython-310.pyc
|   |       |   |   |           test_iteration.cpython-310.pyc
|   |       |   |   |           test_logical_ops.cpython-310.pyc
|   |       |   |   |           test_nonunique_indexes.cpython-310.pyc
|   |       |   |   |           test_npfuncs.cpython-310.pyc
|   |       |   |   |           test_query_eval.cpython-310.pyc
|   |       |   |   |           test_reductions.cpython-310.pyc
|   |       |   |   |           test_repr.cpython-310.pyc
|   |       |   |   |           test_stack_unstack.cpython-310.pyc
|   |       |   |   |           test_subclass.cpython-310.pyc
|   |       |   |   |           test_ufunc.cpython-310.pyc
|   |       |   |   |           test_unary.cpython-310.pyc
|   |       |   |   |           test_validate.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---generic
|   |       |   |   |   |   test_duplicate_labels.py
|   |       |   |   |   |   test_finalize.py
|   |       |   |   |   |   test_frame.py
|   |       |   |   |   |   test_generic.py
|   |       |   |   |   |   test_label_or_level_utils.py
|   |       |   |   |   |   test_series.py
|   |       |   |   |   |   test_to_xarray.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_duplicate_labels.cpython-310.pyc
|   |       |   |   |           test_finalize.cpython-310.pyc
|   |       |   |   |           test_frame.cpython-310.pyc
|   |       |   |   |           test_generic.cpython-310.pyc
|   |       |   |   |           test_label_or_level_utils.cpython-310.pyc
|   |       |   |   |           test_series.cpython-310.pyc
|   |       |   |   |           test_to_xarray.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---groupby
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_all_methods.py
|   |       |   |   |   |   test_api.py
|   |       |   |   |   |   test_apply.py
|   |       |   |   |   |   test_apply_mutate.py
|   |       |   |   |   |   test_bin_groupby.py
|   |       |   |   |   |   test_categorical.py
|   |       |   |   |   |   test_counting.py
|   |       |   |   |   |   test_cumulative.py
|   |       |   |   |   |   test_filters.py
|   |       |   |   |   |   test_groupby.py
|   |       |   |   |   |   test_groupby_dropna.py
|   |       |   |   |   |   test_groupby_subclass.py
|   |       |   |   |   |   test_grouping.py
|   |       |   |   |   |   test_indexing.py
|   |       |   |   |   |   test_index_as_string.py
|   |       |   |   |   |   test_libgroupby.py
|   |       |   |   |   |   test_missing.py
|   |       |   |   |   |   test_numba.py
|   |       |   |   |   |   test_numeric_only.py
|   |       |   |   |   |   test_pipe.py
|   |       |   |   |   |   test_raises.py
|   |       |   |   |   |   test_reductions.py
|   |       |   |   |   |   test_timegrouper.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---aggregate
|   |       |   |   |   |   |   test_aggregate.py
|   |       |   |   |   |   |   test_cython.py
|   |       |   |   |   |   |   test_numba.py
|   |       |   |   |   |   |   test_other.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_aggregate.cpython-310.pyc
|   |       |   |   |   |           test_cython.cpython-310.pyc
|   |       |   |   |   |           test_numba.cpython-310.pyc
|   |       |   |   |   |           test_other.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---methods
|   |       |   |   |   |   |   test_corrwith.py
|   |       |   |   |   |   |   test_describe.py
|   |       |   |   |   |   |   test_groupby_shift_diff.py
|   |       |   |   |   |   |   test_is_monotonic.py
|   |       |   |   |   |   |   test_nlargest_nsmallest.py
|   |       |   |   |   |   |   test_nth.py
|   |       |   |   |   |   |   test_quantile.py
|   |       |   |   |   |   |   test_rank.py
|   |       |   |   |   |   |   test_sample.py
|   |       |   |   |   |   |   test_size.py
|   |       |   |   |   |   |   test_skew.py
|   |       |   |   |   |   |   test_value_counts.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_corrwith.cpython-310.pyc
|   |       |   |   |   |           test_describe.cpython-310.pyc
|   |       |   |   |   |           test_groupby_shift_diff.cpython-310.pyc
|   |       |   |   |   |           test_is_monotonic.cpython-310.pyc
|   |       |   |   |   |           test_nlargest_nsmallest.cpython-310.pyc
|   |       |   |   |   |           test_nth.cpython-310.pyc
|   |       |   |   |   |           test_quantile.cpython-310.pyc
|   |       |   |   |   |           test_rank.cpython-310.pyc
|   |       |   |   |   |           test_sample.cpython-310.pyc
|   |       |   |   |   |           test_size.cpython-310.pyc
|   |       |   |   |   |           test_skew.cpython-310.pyc
|   |       |   |   |   |           test_value_counts.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---transform
|   |       |   |   |   |   |   test_numba.py
|   |       |   |   |   |   |   test_transform.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_numba.cpython-310.pyc
|   |       |   |   |   |           test_transform.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           conftest.cpython-310.pyc
|   |       |   |   |           test_all_methods.cpython-310.pyc
|   |       |   |   |           test_api.cpython-310.pyc
|   |       |   |   |           test_apply.cpython-310.pyc
|   |       |   |   |           test_apply_mutate.cpython-310.pyc
|   |       |   |   |           test_bin_groupby.cpython-310.pyc
|   |       |   |   |           test_categorical.cpython-310.pyc
|   |       |   |   |           test_counting.cpython-310.pyc
|   |       |   |   |           test_cumulative.cpython-310.pyc
|   |       |   |   |           test_filters.cpython-310.pyc
|   |       |   |   |           test_groupby.cpython-310.pyc
|   |       |   |   |           test_groupby_dropna.cpython-310.pyc
|   |       |   |   |           test_groupby_subclass.cpython-310.pyc
|   |       |   |   |           test_grouping.cpython-310.pyc
|   |       |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |           test_index_as_string.cpython-310.pyc
|   |       |   |   |           test_libgroupby.cpython-310.pyc
|   |       |   |   |           test_missing.cpython-310.pyc
|   |       |   |   |           test_numba.cpython-310.pyc
|   |       |   |   |           test_numeric_only.cpython-310.pyc
|   |       |   |   |           test_pipe.cpython-310.pyc
|   |       |   |   |           test_raises.cpython-310.pyc
|   |       |   |   |           test_reductions.cpython-310.pyc
|   |       |   |   |           test_timegrouper.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---indexes
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_any_index.py
|   |       |   |   |   |   test_base.py
|   |       |   |   |   |   test_common.py
|   |       |   |   |   |   test_datetimelike.py
|   |       |   |   |   |   test_engines.py
|   |       |   |   |   |   test_frozen.py
|   |       |   |   |   |   test_indexing.py
|   |       |   |   |   |   test_index_new.py
|   |       |   |   |   |   test_numpy_compat.py
|   |       |   |   |   |   test_old_base.py
|   |       |   |   |   |   test_setops.py
|   |       |   |   |   |   test_subclass.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---base_class
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_pickle.py
|   |       |   |   |   |   |   test_reshape.py
|   |       |   |   |   |   |   test_setops.py
|   |       |   |   |   |   |   test_where.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_formats.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_pickle.cpython-310.pyc
|   |       |   |   |   |           test_reshape.cpython-310.pyc
|   |       |   |   |   |           test_setops.cpython-310.pyc
|   |       |   |   |   |           test_where.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---categorical
|   |       |   |   |   |   |   test_append.py
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_category.py
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_equals.py
|   |       |   |   |   |   |   test_fillna.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_map.py
|   |       |   |   |   |   |   test_reindex.py
|   |       |   |   |   |   |   test_setops.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_append.cpython-310.pyc
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_category.cpython-310.pyc
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_equals.cpython-310.pyc
|   |       |   |   |   |           test_fillna.cpython-310.pyc
|   |       |   |   |   |           test_formats.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_map.cpython-310.pyc
|   |       |   |   |   |           test_reindex.cpython-310.pyc
|   |       |   |   |   |           test_setops.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---datetimelike_
|   |       |   |   |   |   |   test_drop_duplicates.py
|   |       |   |   |   |   |   test_equals.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_is_monotonic.py
|   |       |   |   |   |   |   test_nat.py
|   |       |   |   |   |   |   test_sort_values.py
|   |       |   |   |   |   |   test_value_counts.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_drop_duplicates.cpython-310.pyc
|   |       |   |   |   |           test_equals.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_is_monotonic.cpython-310.pyc
|   |       |   |   |   |           test_nat.cpython-310.pyc
|   |       |   |   |   |           test_sort_values.cpython-310.pyc
|   |       |   |   |   |           test_value_counts.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---datetimes
|   |       |   |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_datetime.py
|   |       |   |   |   |   |   test_date_range.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_freq_attr.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_iter.py
|   |       |   |   |   |   |   test_join.py
|   |       |   |   |   |   |   test_npfuncs.py
|   |       |   |   |   |   |   test_ops.py
|   |       |   |   |   |   |   test_partial_slicing.py
|   |       |   |   |   |   |   test_pickle.py
|   |       |   |   |   |   |   test_reindex.py
|   |       |   |   |   |   |   test_scalar_compat.py
|   |       |   |   |   |   |   test_setops.py
|   |       |   |   |   |   |   test_timezones.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---methods
|   |       |   |   |   |   |   |   test_asof.py
|   |       |   |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   |   test_delete.py
|   |       |   |   |   |   |   |   test_factorize.py
|   |       |   |   |   |   |   |   test_fillna.py
|   |       |   |   |   |   |   |   test_insert.py
|   |       |   |   |   |   |   |   test_isocalendar.py
|   |       |   |   |   |   |   |   test_map.py
|   |       |   |   |   |   |   |   test_normalize.py
|   |       |   |   |   |   |   |   test_repeat.py
|   |       |   |   |   |   |   |   test_resolution.py
|   |       |   |   |   |   |   |   test_round.py
|   |       |   |   |   |   |   |   test_shift.py
|   |       |   |   |   |   |   |   test_snap.py
|   |       |   |   |   |   |   |   test_to_frame.py
|   |       |   |   |   |   |   |   test_to_julian_date.py
|   |       |   |   |   |   |   |   test_to_period.py
|   |       |   |   |   |   |   |   test_to_pydatetime.py
|   |       |   |   |   |   |   |   test_to_series.py
|   |       |   |   |   |   |   |   test_tz_convert.py
|   |       |   |   |   |   |   |   test_tz_localize.py
|   |       |   |   |   |   |   |   test_unique.py
|   |       |   |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           test_asof.cpython-310.pyc
|   |       |   |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |   |           test_delete.cpython-310.pyc
|   |       |   |   |   |   |           test_factorize.cpython-310.pyc
|   |       |   |   |   |   |           test_fillna.cpython-310.pyc
|   |       |   |   |   |   |           test_insert.cpython-310.pyc
|   |       |   |   |   |   |           test_isocalendar.cpython-310.pyc
|   |       |   |   |   |   |           test_map.cpython-310.pyc
|   |       |   |   |   |   |           test_normalize.cpython-310.pyc
|   |       |   |   |   |   |           test_repeat.cpython-310.pyc
|   |       |   |   |   |   |           test_resolution.cpython-310.pyc
|   |       |   |   |   |   |           test_round.cpython-310.pyc
|   |       |   |   |   |   |           test_shift.cpython-310.pyc
|   |       |   |   |   |   |           test_snap.cpython-310.pyc
|   |       |   |   |   |   |           test_to_frame.cpython-310.pyc
|   |       |   |   |   |   |           test_to_julian_date.cpython-310.pyc
|   |       |   |   |   |   |           test_to_period.cpython-310.pyc
|   |       |   |   |   |   |           test_to_pydatetime.cpython-310.pyc
|   |       |   |   |   |   |           test_to_series.cpython-310.pyc
|   |       |   |   |   |   |           test_tz_convert.cpython-310.pyc
|   |       |   |   |   |   |           test_tz_localize.cpython-310.pyc
|   |       |   |   |   |   |           test_unique.cpython-310.pyc
|   |       |   |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_arithmetic.cpython-310.pyc
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_datetime.cpython-310.pyc
|   |       |   |   |   |           test_date_range.cpython-310.pyc
|   |       |   |   |   |           test_formats.cpython-310.pyc
|   |       |   |   |   |           test_freq_attr.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_iter.cpython-310.pyc
|   |       |   |   |   |           test_join.cpython-310.pyc
|   |       |   |   |   |           test_npfuncs.cpython-310.pyc
|   |       |   |   |   |           test_ops.cpython-310.pyc
|   |       |   |   |   |           test_partial_slicing.cpython-310.pyc
|   |       |   |   |   |           test_pickle.cpython-310.pyc
|   |       |   |   |   |           test_reindex.cpython-310.pyc
|   |       |   |   |   |           test_scalar_compat.cpython-310.pyc
|   |       |   |   |   |           test_setops.cpython-310.pyc
|   |       |   |   |   |           test_timezones.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---interval
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_equals.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_interval.py
|   |       |   |   |   |   |   test_interval_range.py
|   |       |   |   |   |   |   test_interval_tree.py
|   |       |   |   |   |   |   test_join.py
|   |       |   |   |   |   |   test_pickle.py
|   |       |   |   |   |   |   test_setops.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_equals.cpython-310.pyc
|   |       |   |   |   |           test_formats.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_interval.cpython-310.pyc
|   |       |   |   |   |           test_interval_range.cpython-310.pyc
|   |       |   |   |   |           test_interval_tree.cpython-310.pyc
|   |       |   |   |   |           test_join.cpython-310.pyc
|   |       |   |   |   |           test_pickle.cpython-310.pyc
|   |       |   |   |   |           test_setops.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---multi
|   |       |   |   |   |   |   conftest.py
|   |       |   |   |   |   |   test_analytics.py
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_compat.py
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_conversion.py
|   |       |   |   |   |   |   test_copy.py
|   |       |   |   |   |   |   test_drop.py
|   |       |   |   |   |   |   test_duplicates.py
|   |       |   |   |   |   |   test_equivalence.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_get_level_values.py
|   |       |   |   |   |   |   test_get_set.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_integrity.py
|   |       |   |   |   |   |   test_isin.py
|   |       |   |   |   |   |   test_join.py
|   |       |   |   |   |   |   test_lexsort.py
|   |       |   |   |   |   |   test_missing.py
|   |       |   |   |   |   |   test_monotonic.py
|   |       |   |   |   |   |   test_names.py
|   |       |   |   |   |   |   test_partial_indexing.py
|   |       |   |   |   |   |   test_pickle.py
|   |       |   |   |   |   |   test_reindex.py
|   |       |   |   |   |   |   test_reshape.py
|   |       |   |   |   |   |   test_setops.py
|   |       |   |   |   |   |   test_sorting.py
|   |       |   |   |   |   |   test_take.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           conftest.cpython-310.pyc
|   |       |   |   |   |           test_analytics.cpython-310.pyc
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_compat.cpython-310.pyc
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_conversion.cpython-310.pyc
|   |       |   |   |   |           test_copy.cpython-310.pyc
|   |       |   |   |   |           test_drop.cpython-310.pyc
|   |       |   |   |   |           test_duplicates.cpython-310.pyc
|   |       |   |   |   |           test_equivalence.cpython-310.pyc
|   |       |   |   |   |           test_formats.cpython-310.pyc
|   |       |   |   |   |           test_get_level_values.cpython-310.pyc
|   |       |   |   |   |           test_get_set.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_integrity.cpython-310.pyc
|   |       |   |   |   |           test_isin.cpython-310.pyc
|   |       |   |   |   |           test_join.cpython-310.pyc
|   |       |   |   |   |           test_lexsort.cpython-310.pyc
|   |       |   |   |   |           test_missing.cpython-310.pyc
|   |       |   |   |   |           test_monotonic.cpython-310.pyc
|   |       |   |   |   |           test_names.cpython-310.pyc
|   |       |   |   |   |           test_partial_indexing.cpython-310.pyc
|   |       |   |   |   |           test_pickle.cpython-310.pyc
|   |       |   |   |   |           test_reindex.cpython-310.pyc
|   |       |   |   |   |           test_reshape.cpython-310.pyc
|   |       |   |   |   |           test_setops.cpython-310.pyc
|   |       |   |   |   |           test_sorting.cpython-310.pyc
|   |       |   |   |   |           test_take.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---numeric
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_join.py
|   |       |   |   |   |   |   test_numeric.py
|   |       |   |   |   |   |   test_setops.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_join.cpython-310.pyc
|   |       |   |   |   |           test_numeric.cpython-310.pyc
|   |       |   |   |   |           test_setops.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---object
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---period
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_freq_attr.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_join.py
|   |       |   |   |   |   |   test_monotonic.py
|   |       |   |   |   |   |   test_partial_slicing.py
|   |       |   |   |   |   |   test_period.py
|   |       |   |   |   |   |   test_period_range.py
|   |       |   |   |   |   |   test_pickle.py
|   |       |   |   |   |   |   test_resolution.py
|   |       |   |   |   |   |   test_scalar_compat.py
|   |       |   |   |   |   |   test_searchsorted.py
|   |       |   |   |   |   |   test_setops.py
|   |       |   |   |   |   |   test_tools.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---methods
|   |       |   |   |   |   |   |   test_asfreq.py
|   |       |   |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   |   test_factorize.py
|   |       |   |   |   |   |   |   test_fillna.py
|   |       |   |   |   |   |   |   test_insert.py
|   |       |   |   |   |   |   |   test_is_full.py
|   |       |   |   |   |   |   |   test_repeat.py
|   |       |   |   |   |   |   |   test_shift.py
|   |       |   |   |   |   |   |   test_to_timestamp.py
|   |       |   |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           test_asfreq.cpython-310.pyc
|   |       |   |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |   |           test_factorize.cpython-310.pyc
|   |       |   |   |   |   |           test_fillna.cpython-310.pyc
|   |       |   |   |   |   |           test_insert.cpython-310.pyc
|   |       |   |   |   |   |           test_is_full.cpython-310.pyc
|   |       |   |   |   |   |           test_repeat.cpython-310.pyc
|   |       |   |   |   |   |           test_shift.cpython-310.pyc
|   |       |   |   |   |   |           test_to_timestamp.cpython-310.pyc
|   |       |   |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_formats.cpython-310.pyc
|   |       |   |   |   |           test_freq_attr.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_join.cpython-310.pyc
|   |       |   |   |   |           test_monotonic.cpython-310.pyc
|   |       |   |   |   |           test_partial_slicing.cpython-310.pyc
|   |       |   |   |   |           test_period.cpython-310.pyc
|   |       |   |   |   |           test_period_range.cpython-310.pyc
|   |       |   |   |   |           test_pickle.cpython-310.pyc
|   |       |   |   |   |           test_resolution.cpython-310.pyc
|   |       |   |   |   |           test_scalar_compat.cpython-310.pyc
|   |       |   |   |   |           test_searchsorted.cpython-310.pyc
|   |       |   |   |   |           test_setops.cpython-310.pyc
|   |       |   |   |   |           test_tools.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---ranges
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_join.py
|   |       |   |   |   |   |   test_range.py
|   |       |   |   |   |   |   test_setops.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_join.cpython-310.pyc
|   |       |   |   |   |           test_range.cpython-310.pyc
|   |       |   |   |   |           test_setops.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---string
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---timedeltas
|   |       |   |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_delete.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_freq_attr.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_join.py
|   |       |   |   |   |   |   test_ops.py
|   |       |   |   |   |   |   test_pickle.py
|   |       |   |   |   |   |   test_scalar_compat.py
|   |       |   |   |   |   |   test_searchsorted.py
|   |       |   |   |   |   |   test_setops.py
|   |       |   |   |   |   |   test_timedelta.py
|   |       |   |   |   |   |   test_timedelta_range.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---methods
|   |       |   |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   |   test_factorize.py
|   |       |   |   |   |   |   |   test_fillna.py
|   |       |   |   |   |   |   |   test_insert.py
|   |       |   |   |   |   |   |   test_repeat.py
|   |       |   |   |   |   |   |   test_shift.py
|   |       |   |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |   |           test_factorize.cpython-310.pyc
|   |       |   |   |   |   |           test_fillna.cpython-310.pyc
|   |       |   |   |   |   |           test_insert.cpython-310.pyc
|   |       |   |   |   |   |           test_repeat.cpython-310.pyc
|   |       |   |   |   |   |           test_shift.cpython-310.pyc
|   |       |   |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_arithmetic.cpython-310.pyc
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_delete.cpython-310.pyc
|   |       |   |   |   |           test_formats.cpython-310.pyc
|   |       |   |   |   |           test_freq_attr.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_join.cpython-310.pyc
|   |       |   |   |   |           test_ops.cpython-310.pyc
|   |       |   |   |   |           test_pickle.cpython-310.pyc
|   |       |   |   |   |           test_scalar_compat.cpython-310.pyc
|   |       |   |   |   |           test_searchsorted.cpython-310.pyc
|   |       |   |   |   |           test_setops.cpython-310.pyc
|   |       |   |   |   |           test_timedelta.cpython-310.pyc
|   |       |   |   |   |           test_timedelta_range.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           conftest.cpython-310.pyc
|   |       |   |   |           test_any_index.cpython-310.pyc
|   |       |   |   |           test_base.cpython-310.pyc
|   |       |   |   |           test_common.cpython-310.pyc
|   |       |   |   |           test_datetimelike.cpython-310.pyc
|   |       |   |   |           test_engines.cpython-310.pyc
|   |       |   |   |           test_frozen.cpython-310.pyc
|   |       |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |           test_index_new.cpython-310.pyc
|   |       |   |   |           test_numpy_compat.cpython-310.pyc
|   |       |   |   |           test_old_base.cpython-310.pyc
|   |       |   |   |           test_setops.cpython-310.pyc
|   |       |   |   |           test_subclass.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---indexing
|   |       |   |   |   |   common.py
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_at.py
|   |       |   |   |   |   test_categorical.py
|   |       |   |   |   |   test_chaining_and_caching.py
|   |       |   |   |   |   test_check_indexer.py
|   |       |   |   |   |   test_coercion.py
|   |       |   |   |   |   test_datetime.py
|   |       |   |   |   |   test_floats.py
|   |       |   |   |   |   test_iat.py
|   |       |   |   |   |   test_iloc.py
|   |       |   |   |   |   test_indexers.py
|   |       |   |   |   |   test_indexing.py
|   |       |   |   |   |   test_loc.py
|   |       |   |   |   |   test_na_indexing.py
|   |       |   |   |   |   test_partial.py
|   |       |   |   |   |   test_scalar.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---interval
|   |       |   |   |   |   |   test_interval.py
|   |       |   |   |   |   |   test_interval_new.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_interval.cpython-310.pyc
|   |       |   |   |   |           test_interval_new.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---multiindex
|   |       |   |   |   |   |   test_chaining_and_caching.py
|   |       |   |   |   |   |   test_datetime.py
|   |       |   |   |   |   |   test_getitem.py
|   |       |   |   |   |   |   test_iloc.py
|   |       |   |   |   |   |   test_indexing_slow.py
|   |       |   |   |   |   |   test_loc.py
|   |       |   |   |   |   |   test_multiindex.py
|   |       |   |   |   |   |   test_partial.py
|   |       |   |   |   |   |   test_setitem.py
|   |       |   |   |   |   |   test_slice.py
|   |       |   |   |   |   |   test_sorted.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_chaining_and_caching.cpython-310.pyc
|   |       |   |   |   |           test_datetime.cpython-310.pyc
|   |       |   |   |   |           test_getitem.cpython-310.pyc
|   |       |   |   |   |           test_iloc.cpython-310.pyc
|   |       |   |   |   |           test_indexing_slow.cpython-310.pyc
|   |       |   |   |   |           test_loc.cpython-310.pyc
|   |       |   |   |   |           test_multiindex.cpython-310.pyc
|   |       |   |   |   |           test_partial.cpython-310.pyc
|   |       |   |   |   |           test_setitem.cpython-310.pyc
|   |       |   |   |   |           test_slice.cpython-310.pyc
|   |       |   |   |   |           test_sorted.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           common.cpython-310.pyc
|   |       |   |   |           conftest.cpython-310.pyc
|   |       |   |   |           test_at.cpython-310.pyc
|   |       |   |   |           test_categorical.cpython-310.pyc
|   |       |   |   |           test_chaining_and_caching.cpython-310.pyc
|   |       |   |   |           test_check_indexer.cpython-310.pyc
|   |       |   |   |           test_coercion.cpython-310.pyc
|   |       |   |   |           test_datetime.cpython-310.pyc
|   |       |   |   |           test_floats.cpython-310.pyc
|   |       |   |   |           test_iat.cpython-310.pyc
|   |       |   |   |           test_iloc.cpython-310.pyc
|   |       |   |   |           test_indexers.cpython-310.pyc
|   |       |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |           test_loc.cpython-310.pyc
|   |       |   |   |           test_na_indexing.cpython-310.pyc
|   |       |   |   |           test_partial.cpython-310.pyc
|   |       |   |   |           test_scalar.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---interchange
|   |       |   |   |   |   test_impl.py
|   |       |   |   |   |   test_spec_conformance.py
|   |       |   |   |   |   test_utils.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_impl.cpython-310.pyc
|   |       |   |   |           test_spec_conformance.cpython-310.pyc
|   |       |   |   |           test_utils.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---internals
|   |       |   |   |   |   test_api.py
|   |       |   |   |   |   test_internals.py
|   |       |   |   |   |   test_managers.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_api.cpython-310.pyc
|   |       |   |   |           test_internals.cpython-310.pyc
|   |       |   |   |           test_managers.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---io
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   generate_legacy_storage_files.py
|   |       |   |   |   |   test_clipboard.py
|   |       |   |   |   |   test_common.py
|   |       |   |   |   |   test_compression.py
|   |       |   |   |   |   test_feather.py
|   |       |   |   |   |   test_fsspec.py
|   |       |   |   |   |   test_gbq.py
|   |       |   |   |   |   test_gcs.py
|   |       |   |   |   |   test_html.py
|   |       |   |   |   |   test_http_headers.py
|   |       |   |   |   |   test_orc.py
|   |       |   |   |   |   test_parquet.py
|   |       |   |   |   |   test_pickle.py
|   |       |   |   |   |   test_s3.py
|   |       |   |   |   |   test_spss.py
|   |       |   |   |   |   test_sql.py
|   |       |   |   |   |   test_stata.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---excel
|   |       |   |   |   |   |   test_odf.py
|   |       |   |   |   |   |   test_odswriter.py
|   |       |   |   |   |   |   test_openpyxl.py
|   |       |   |   |   |   |   test_readers.py
|   |       |   |   |   |   |   test_style.py
|   |       |   |   |   |   |   test_writers.py
|   |       |   |   |   |   |   test_xlrd.py
|   |       |   |   |   |   |   test_xlsxwriter.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_odf.cpython-310.pyc
|   |       |   |   |   |           test_odswriter.cpython-310.pyc
|   |       |   |   |   |           test_openpyxl.cpython-310.pyc
|   |       |   |   |   |           test_readers.cpython-310.pyc
|   |       |   |   |   |           test_style.cpython-310.pyc
|   |       |   |   |   |           test_writers.cpython-310.pyc
|   |       |   |   |   |           test_xlrd.cpython-310.pyc
|   |       |   |   |   |           test_xlsxwriter.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---formats
|   |       |   |   |   |   |   test_console.py
|   |       |   |   |   |   |   test_css.py
|   |       |   |   |   |   |   test_eng_formatting.py
|   |       |   |   |   |   |   test_format.py
|   |       |   |   |   |   |   test_ipython_compat.py
|   |       |   |   |   |   |   test_printing.py
|   |       |   |   |   |   |   test_to_csv.py
|   |       |   |   |   |   |   test_to_excel.py
|   |       |   |   |   |   |   test_to_html.py
|   |       |   |   |   |   |   test_to_latex.py
|   |       |   |   |   |   |   test_to_markdown.py
|   |       |   |   |   |   |   test_to_string.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---style
|   |       |   |   |   |   |   |   test_bar.py
|   |       |   |   |   |   |   |   test_exceptions.py
|   |       |   |   |   |   |   |   test_format.py
|   |       |   |   |   |   |   |   test_highlight.py
|   |       |   |   |   |   |   |   test_html.py
|   |       |   |   |   |   |   |   test_matplotlib.py
|   |       |   |   |   |   |   |   test_non_unique.py
|   |       |   |   |   |   |   |   test_style.py
|   |       |   |   |   |   |   |   test_tooltip.py
|   |       |   |   |   |   |   |   test_to_latex.py
|   |       |   |   |   |   |   |   test_to_string.py
|   |       |   |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           test_bar.cpython-310.pyc
|   |       |   |   |   |   |           test_exceptions.cpython-310.pyc
|   |       |   |   |   |   |           test_format.cpython-310.pyc
|   |       |   |   |   |   |           test_highlight.cpython-310.pyc
|   |       |   |   |   |   |           test_html.cpython-310.pyc
|   |       |   |   |   |   |           test_matplotlib.cpython-310.pyc
|   |       |   |   |   |   |           test_non_unique.cpython-310.pyc
|   |       |   |   |   |   |           test_style.cpython-310.pyc
|   |       |   |   |   |   |           test_tooltip.cpython-310.pyc
|   |       |   |   |   |   |           test_to_latex.cpython-310.pyc
|   |       |   |   |   |   |           test_to_string.cpython-310.pyc
|   |       |   |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_console.cpython-310.pyc
|   |       |   |   |   |           test_css.cpython-310.pyc
|   |       |   |   |   |           test_eng_formatting.cpython-310.pyc
|   |       |   |   |   |           test_format.cpython-310.pyc
|   |       |   |   |   |           test_ipython_compat.cpython-310.pyc
|   |       |   |   |   |           test_printing.cpython-310.pyc
|   |       |   |   |   |           test_to_csv.cpython-310.pyc
|   |       |   |   |   |           test_to_excel.cpython-310.pyc
|   |       |   |   |   |           test_to_html.cpython-310.pyc
|   |       |   |   |   |           test_to_latex.cpython-310.pyc
|   |       |   |   |   |           test_to_markdown.cpython-310.pyc
|   |       |   |   |   |           test_to_string.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---json
|   |       |   |   |   |   |   conftest.py
|   |       |   |   |   |   |   test_compression.py
|   |       |   |   |   |   |   test_deprecated_kwargs.py
|   |       |   |   |   |   |   test_json_table_schema.py
|   |       |   |   |   |   |   test_json_table_schema_ext_dtype.py
|   |       |   |   |   |   |   test_normalize.py
|   |       |   |   |   |   |   test_pandas.py
|   |       |   |   |   |   |   test_readlines.py
|   |       |   |   |   |   |   test_ujson.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           conftest.cpython-310.pyc
|   |       |   |   |   |           test_compression.cpython-310.pyc
|   |       |   |   |   |           test_deprecated_kwargs.cpython-310.pyc
|   |       |   |   |   |           test_json_table_schema.cpython-310.pyc
|   |       |   |   |   |           test_json_table_schema_ext_dtype.cpython-310.pyc
|   |       |   |   |   |           test_normalize.cpython-310.pyc
|   |       |   |   |   |           test_pandas.cpython-310.pyc
|   |       |   |   |   |           test_readlines.cpython-310.pyc
|   |       |   |   |   |           test_ujson.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---parser
|   |       |   |   |   |   |   conftest.py
|   |       |   |   |   |   |   test_comment.py
|   |       |   |   |   |   |   test_compression.py
|   |       |   |   |   |   |   test_concatenate_chunks.py
|   |       |   |   |   |   |   test_converters.py
|   |       |   |   |   |   |   test_c_parser_only.py
|   |       |   |   |   |   |   test_dialect.py
|   |       |   |   |   |   |   test_encoding.py
|   |       |   |   |   |   |   test_header.py
|   |       |   |   |   |   |   test_index_col.py
|   |       |   |   |   |   |   test_mangle_dupes.py
|   |       |   |   |   |   |   test_multi_thread.py
|   |       |   |   |   |   |   test_na_values.py
|   |       |   |   |   |   |   test_network.py
|   |       |   |   |   |   |   test_parse_dates.py
|   |       |   |   |   |   |   test_python_parser_only.py
|   |       |   |   |   |   |   test_quoting.py
|   |       |   |   |   |   |   test_read_fwf.py
|   |       |   |   |   |   |   test_skiprows.py
|   |       |   |   |   |   |   test_textreader.py
|   |       |   |   |   |   |   test_unsupported.py
|   |       |   |   |   |   |   test_upcast.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---common
|   |       |   |   |   |   |   |   test_chunksize.py
|   |       |   |   |   |   |   |   test_common_basic.py
|   |       |   |   |   |   |   |   test_data_list.py
|   |       |   |   |   |   |   |   test_decimal.py
|   |       |   |   |   |   |   |   test_file_buffer_url.py
|   |       |   |   |   |   |   |   test_float.py
|   |       |   |   |   |   |   |   test_index.py
|   |       |   |   |   |   |   |   test_inf.py
|   |       |   |   |   |   |   |   test_ints.py
|   |       |   |   |   |   |   |   test_iterator.py
|   |       |   |   |   |   |   |   test_read_errors.py
|   |       |   |   |   |   |   |   test_verbose.py
|   |       |   |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           test_chunksize.cpython-310.pyc
|   |       |   |   |   |   |           test_common_basic.cpython-310.pyc
|   |       |   |   |   |   |           test_data_list.cpython-310.pyc
|   |       |   |   |   |   |           test_decimal.cpython-310.pyc
|   |       |   |   |   |   |           test_file_buffer_url.cpython-310.pyc
|   |       |   |   |   |   |           test_float.cpython-310.pyc
|   |       |   |   |   |   |           test_index.cpython-310.pyc
|   |       |   |   |   |   |           test_inf.cpython-310.pyc
|   |       |   |   |   |   |           test_ints.cpython-310.pyc
|   |       |   |   |   |   |           test_iterator.cpython-310.pyc
|   |       |   |   |   |   |           test_read_errors.cpython-310.pyc
|   |       |   |   |   |   |           test_verbose.cpython-310.pyc
|   |       |   |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   +---dtypes
|   |       |   |   |   |   |   |   test_categorical.py
|   |       |   |   |   |   |   |   test_dtypes_basic.py
|   |       |   |   |   |   |   |   test_empty.py
|   |       |   |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           test_categorical.cpython-310.pyc
|   |       |   |   |   |   |           test_dtypes_basic.cpython-310.pyc
|   |       |   |   |   |   |           test_empty.cpython-310.pyc
|   |       |   |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   +---usecols
|   |       |   |   |   |   |   |   test_parse_dates.py
|   |       |   |   |   |   |   |   test_strings.py
|   |       |   |   |   |   |   |   test_usecols_basic.py
|   |       |   |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           test_parse_dates.cpython-310.pyc
|   |       |   |   |   |   |           test_strings.cpython-310.pyc
|   |       |   |   |   |   |           test_usecols_basic.cpython-310.pyc
|   |       |   |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           conftest.cpython-310.pyc
|   |       |   |   |   |           test_comment.cpython-310.pyc
|   |       |   |   |   |           test_compression.cpython-310.pyc
|   |       |   |   |   |           test_concatenate_chunks.cpython-310.pyc
|   |       |   |   |   |           test_converters.cpython-310.pyc
|   |       |   |   |   |           test_c_parser_only.cpython-310.pyc
|   |       |   |   |   |           test_dialect.cpython-310.pyc
|   |       |   |   |   |           test_encoding.cpython-310.pyc
|   |       |   |   |   |           test_header.cpython-310.pyc
|   |       |   |   |   |           test_index_col.cpython-310.pyc
|   |       |   |   |   |           test_mangle_dupes.cpython-310.pyc
|   |       |   |   |   |           test_multi_thread.cpython-310.pyc
|   |       |   |   |   |           test_na_values.cpython-310.pyc
|   |       |   |   |   |           test_network.cpython-310.pyc
|   |       |   |   |   |           test_parse_dates.cpython-310.pyc
|   |       |   |   |   |           test_python_parser_only.cpython-310.pyc
|   |       |   |   |   |           test_quoting.cpython-310.pyc
|   |       |   |   |   |           test_read_fwf.cpython-310.pyc
|   |       |   |   |   |           test_skiprows.cpython-310.pyc
|   |       |   |   |   |           test_textreader.cpython-310.pyc
|   |       |   |   |   |           test_unsupported.cpython-310.pyc
|   |       |   |   |   |           test_upcast.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---pytables
|   |       |   |   |   |   |   common.py
|   |       |   |   |   |   |   conftest.py
|   |       |   |   |   |   |   test_append.py
|   |       |   |   |   |   |   test_categorical.py
|   |       |   |   |   |   |   test_compat.py
|   |       |   |   |   |   |   test_complex.py
|   |       |   |   |   |   |   test_errors.py
|   |       |   |   |   |   |   test_file_handling.py
|   |       |   |   |   |   |   test_keys.py
|   |       |   |   |   |   |   test_put.py
|   |       |   |   |   |   |   test_pytables_missing.py
|   |       |   |   |   |   |   test_read.py
|   |       |   |   |   |   |   test_retain_attributes.py
|   |       |   |   |   |   |   test_round_trip.py
|   |       |   |   |   |   |   test_select.py
|   |       |   |   |   |   |   test_store.py
|   |       |   |   |   |   |   test_subclass.py
|   |       |   |   |   |   |   test_timezones.py
|   |       |   |   |   |   |   test_time_series.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           common.cpython-310.pyc
|   |       |   |   |   |           conftest.cpython-310.pyc
|   |       |   |   |   |           test_append.cpython-310.pyc
|   |       |   |   |   |           test_categorical.cpython-310.pyc
|   |       |   |   |   |           test_compat.cpython-310.pyc
|   |       |   |   |   |           test_complex.cpython-310.pyc
|   |       |   |   |   |           test_errors.cpython-310.pyc
|   |       |   |   |   |           test_file_handling.cpython-310.pyc
|   |       |   |   |   |           test_keys.cpython-310.pyc
|   |       |   |   |   |           test_put.cpython-310.pyc
|   |       |   |   |   |           test_pytables_missing.cpython-310.pyc
|   |       |   |   |   |           test_read.cpython-310.pyc
|   |       |   |   |   |           test_retain_attributes.cpython-310.pyc
|   |       |   |   |   |           test_round_trip.cpython-310.pyc
|   |       |   |   |   |           test_select.cpython-310.pyc
|   |       |   |   |   |           test_store.cpython-310.pyc
|   |       |   |   |   |           test_subclass.cpython-310.pyc
|   |       |   |   |   |           test_timezones.cpython-310.pyc
|   |       |   |   |   |           test_time_series.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---sas
|   |       |   |   |   |   |   test_byteswap.py
|   |       |   |   |   |   |   test_sas.py
|   |       |   |   |   |   |   test_sas7bdat.py
|   |       |   |   |   |   |   test_xport.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_byteswap.cpython-310.pyc
|   |       |   |   |   |           test_sas.cpython-310.pyc
|   |       |   |   |   |           test_sas7bdat.cpython-310.pyc
|   |       |   |   |   |           test_xport.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---xml
|   |       |   |   |   |   |   conftest.py
|   |       |   |   |   |   |   test_to_xml.py
|   |       |   |   |   |   |   test_xml.py
|   |       |   |   |   |   |   test_xml_dtypes.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           conftest.cpython-310.pyc
|   |       |   |   |   |           test_to_xml.cpython-310.pyc
|   |       |   |   |   |           test_xml.cpython-310.pyc
|   |       |   |   |   |           test_xml_dtypes.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           conftest.cpython-310.pyc
|   |       |   |   |           generate_legacy_storage_files.cpython-310.pyc
|   |       |   |   |           test_clipboard.cpython-310.pyc
|   |       |   |   |           test_common.cpython-310.pyc
|   |       |   |   |           test_compression.cpython-310.pyc
|   |       |   |   |           test_feather.cpython-310.pyc
|   |       |   |   |           test_fsspec.cpython-310.pyc
|   |       |   |   |           test_gbq.cpython-310.pyc
|   |       |   |   |           test_gcs.cpython-310.pyc
|   |       |   |   |           test_html.cpython-310.pyc
|   |       |   |   |           test_http_headers.cpython-310.pyc
|   |       |   |   |           test_orc.cpython-310.pyc
|   |       |   |   |           test_parquet.cpython-310.pyc
|   |       |   |   |           test_pickle.cpython-310.pyc
|   |       |   |   |           test_s3.cpython-310.pyc
|   |       |   |   |           test_spss.cpython-310.pyc
|   |       |   |   |           test_sql.cpython-310.pyc
|   |       |   |   |           test_stata.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---libs
|   |       |   |   |   |   test_hashtable.py
|   |       |   |   |   |   test_join.py
|   |       |   |   |   |   test_lib.py
|   |       |   |   |   |   test_libalgos.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_hashtable.cpython-310.pyc
|   |       |   |   |           test_join.cpython-310.pyc
|   |       |   |   |           test_lib.cpython-310.pyc
|   |       |   |   |           test_libalgos.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---plotting
|   |       |   |   |   |   common.py
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_backend.py
|   |       |   |   |   |   test_boxplot_method.py
|   |       |   |   |   |   test_common.py
|   |       |   |   |   |   test_converter.py
|   |       |   |   |   |   test_datetimelike.py
|   |       |   |   |   |   test_groupby.py
|   |       |   |   |   |   test_hist_method.py
|   |       |   |   |   |   test_misc.py
|   |       |   |   |   |   test_series.py
|   |       |   |   |   |   test_style.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---frame
|   |       |   |   |   |   |   test_frame.py
|   |       |   |   |   |   |   test_frame_color.py
|   |       |   |   |   |   |   test_frame_groupby.py
|   |       |   |   |   |   |   test_frame_legend.py
|   |       |   |   |   |   |   test_frame_subplots.py
|   |       |   |   |   |   |   test_hist_box_by.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_frame.cpython-310.pyc
|   |       |   |   |   |           test_frame_color.cpython-310.pyc
|   |       |   |   |   |           test_frame_groupby.cpython-310.pyc
|   |       |   |   |   |           test_frame_legend.cpython-310.pyc
|   |       |   |   |   |           test_frame_subplots.cpython-310.pyc
|   |       |   |   |   |           test_hist_box_by.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           common.cpython-310.pyc
|   |       |   |   |           conftest.cpython-310.pyc
|   |       |   |   |           test_backend.cpython-310.pyc
|   |       |   |   |           test_boxplot_method.cpython-310.pyc
|   |       |   |   |           test_common.cpython-310.pyc
|   |       |   |   |           test_converter.cpython-310.pyc
|   |       |   |   |           test_datetimelike.cpython-310.pyc
|   |       |   |   |           test_groupby.cpython-310.pyc
|   |       |   |   |           test_hist_method.cpython-310.pyc
|   |       |   |   |           test_misc.cpython-310.pyc
|   |       |   |   |           test_series.cpython-310.pyc
|   |       |   |   |           test_style.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---reductions
|   |       |   |   |   |   test_reductions.py
|   |       |   |   |   |   test_stat_reductions.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_reductions.cpython-310.pyc
|   |       |   |   |           test_stat_reductions.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---resample
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_base.py
|   |       |   |   |   |   test_datetime_index.py
|   |       |   |   |   |   test_period_index.py
|   |       |   |   |   |   test_resampler_grouper.py
|   |       |   |   |   |   test_resample_api.py
|   |       |   |   |   |   test_timedelta.py
|   |       |   |   |   |   test_time_grouper.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           conftest.cpython-310.pyc
|   |       |   |   |           test_base.cpython-310.pyc
|   |       |   |   |           test_datetime_index.cpython-310.pyc
|   |       |   |   |           test_period_index.cpython-310.pyc
|   |       |   |   |           test_resampler_grouper.cpython-310.pyc
|   |       |   |   |           test_resample_api.cpython-310.pyc
|   |       |   |   |           test_timedelta.cpython-310.pyc
|   |       |   |   |           test_time_grouper.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---reshape
|   |       |   |   |   |   test_crosstab.py
|   |       |   |   |   |   test_cut.py
|   |       |   |   |   |   test_from_dummies.py
|   |       |   |   |   |   test_get_dummies.py
|   |       |   |   |   |   test_melt.py
|   |       |   |   |   |   test_pivot.py
|   |       |   |   |   |   test_pivot_multilevel.py
|   |       |   |   |   |   test_qcut.py
|   |       |   |   |   |   test_union_categoricals.py
|   |       |   |   |   |   test_util.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---concat
|   |       |   |   |   |   |   conftest.py
|   |       |   |   |   |   |   test_append.py
|   |       |   |   |   |   |   test_append_common.py
|   |       |   |   |   |   |   test_categorical.py
|   |       |   |   |   |   |   test_concat.py
|   |       |   |   |   |   |   test_dataframe.py
|   |       |   |   |   |   |   test_datetimes.py
|   |       |   |   |   |   |   test_empty.py
|   |       |   |   |   |   |   test_index.py
|   |       |   |   |   |   |   test_invalid.py
|   |       |   |   |   |   |   test_series.py
|   |       |   |   |   |   |   test_sort.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           conftest.cpython-310.pyc
|   |       |   |   |   |           test_append.cpython-310.pyc
|   |       |   |   |   |           test_append_common.cpython-310.pyc
|   |       |   |   |   |           test_categorical.cpython-310.pyc
|   |       |   |   |   |           test_concat.cpython-310.pyc
|   |       |   |   |   |           test_dataframe.cpython-310.pyc
|   |       |   |   |   |           test_datetimes.cpython-310.pyc
|   |       |   |   |   |           test_empty.cpython-310.pyc
|   |       |   |   |   |           test_index.cpython-310.pyc
|   |       |   |   |   |           test_invalid.cpython-310.pyc
|   |       |   |   |   |           test_series.cpython-310.pyc
|   |       |   |   |   |           test_sort.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---merge
|   |       |   |   |   |   |   test_join.py
|   |       |   |   |   |   |   test_merge.py
|   |       |   |   |   |   |   test_merge_asof.py
|   |       |   |   |   |   |   test_merge_cross.py
|   |       |   |   |   |   |   test_merge_index_as_string.py
|   |       |   |   |   |   |   test_merge_ordered.py
|   |       |   |   |   |   |   test_multi.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_join.cpython-310.pyc
|   |       |   |   |   |           test_merge.cpython-310.pyc
|   |       |   |   |   |           test_merge_asof.cpython-310.pyc
|   |       |   |   |   |           test_merge_cross.cpython-310.pyc
|   |       |   |   |   |           test_merge_index_as_string.cpython-310.pyc
|   |       |   |   |   |           test_merge_ordered.cpython-310.pyc
|   |       |   |   |   |           test_multi.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_crosstab.cpython-310.pyc
|   |       |   |   |           test_cut.cpython-310.pyc
|   |       |   |   |           test_from_dummies.cpython-310.pyc
|   |       |   |   |           test_get_dummies.cpython-310.pyc
|   |       |   |   |           test_melt.cpython-310.pyc
|   |       |   |   |           test_pivot.cpython-310.pyc
|   |       |   |   |           test_pivot_multilevel.cpython-310.pyc
|   |       |   |   |           test_qcut.cpython-310.pyc
|   |       |   |   |           test_union_categoricals.cpython-310.pyc
|   |       |   |   |           test_util.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---scalar
|   |       |   |   |   |   test_nat.py
|   |       |   |   |   |   test_na_scalar.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---interval
|   |       |   |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_contains.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_interval.py
|   |       |   |   |   |   |   test_overlaps.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_arithmetic.cpython-310.pyc
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_contains.cpython-310.pyc
|   |       |   |   |   |           test_formats.cpython-310.pyc
|   |       |   |   |   |           test_interval.cpython-310.pyc
|   |       |   |   |   |           test_overlaps.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---period
|   |       |   |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   |   test_asfreq.py
|   |       |   |   |   |   |   test_period.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_arithmetic.cpython-310.pyc
|   |       |   |   |   |           test_asfreq.cpython-310.pyc
|   |       |   |   |   |           test_period.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---timedelta
|   |       |   |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_timedelta.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---methods
|   |       |   |   |   |   |   |   test_as_unit.py
|   |       |   |   |   |   |   |   test_round.py
|   |       |   |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           test_as_unit.cpython-310.pyc
|   |       |   |   |   |   |           test_round.cpython-310.pyc
|   |       |   |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_arithmetic.cpython-310.pyc
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_formats.cpython-310.pyc
|   |       |   |   |   |           test_timedelta.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---timestamp
|   |       |   |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   |   test_comparisons.py
|   |       |   |   |   |   |   test_constructors.py
|   |       |   |   |   |   |   test_formats.py
|   |       |   |   |   |   |   test_timestamp.py
|   |       |   |   |   |   |   test_timezones.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---methods
|   |       |   |   |   |   |   |   test_as_unit.py
|   |       |   |   |   |   |   |   test_normalize.py
|   |       |   |   |   |   |   |   test_replace.py
|   |       |   |   |   |   |   |   test_round.py
|   |       |   |   |   |   |   |   test_timestamp_method.py
|   |       |   |   |   |   |   |   test_to_julian_date.py
|   |       |   |   |   |   |   |   test_to_pydatetime.py
|   |       |   |   |   |   |   |   test_tz_convert.py
|   |       |   |   |   |   |   |   test_tz_localize.py
|   |       |   |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           test_as_unit.cpython-310.pyc
|   |       |   |   |   |   |           test_normalize.cpython-310.pyc
|   |       |   |   |   |   |           test_replace.cpython-310.pyc
|   |       |   |   |   |   |           test_round.cpython-310.pyc
|   |       |   |   |   |   |           test_timestamp_method.cpython-310.pyc
|   |       |   |   |   |   |           test_to_julian_date.cpython-310.pyc
|   |       |   |   |   |   |           test_to_pydatetime.cpython-310.pyc
|   |       |   |   |   |   |           test_tz_convert.cpython-310.pyc
|   |       |   |   |   |   |           test_tz_localize.cpython-310.pyc
|   |       |   |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_arithmetic.cpython-310.pyc
|   |       |   |   |   |           test_comparisons.cpython-310.pyc
|   |       |   |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |   |           test_formats.cpython-310.pyc
|   |       |   |   |   |           test_timestamp.cpython-310.pyc
|   |       |   |   |   |           test_timezones.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_nat.cpython-310.pyc
|   |       |   |   |           test_na_scalar.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---series
|   |       |   |   |   |   test_api.py
|   |       |   |   |   |   test_arithmetic.py
|   |       |   |   |   |   test_constructors.py
|   |       |   |   |   |   test_cumulative.py
|   |       |   |   |   |   test_formats.py
|   |       |   |   |   |   test_iteration.py
|   |       |   |   |   |   test_logical_ops.py
|   |       |   |   |   |   test_missing.py
|   |       |   |   |   |   test_npfuncs.py
|   |       |   |   |   |   test_reductions.py
|   |       |   |   |   |   test_subclass.py
|   |       |   |   |   |   test_ufunc.py
|   |       |   |   |   |   test_unary.py
|   |       |   |   |   |   test_validate.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---accessors
|   |       |   |   |   |   |   test_cat_accessor.py
|   |       |   |   |   |   |   test_dt_accessor.py
|   |       |   |   |   |   |   test_list_accessor.py
|   |       |   |   |   |   |   test_sparse_accessor.py
|   |       |   |   |   |   |   test_struct_accessor.py
|   |       |   |   |   |   |   test_str_accessor.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_cat_accessor.cpython-310.pyc
|   |       |   |   |   |           test_dt_accessor.cpython-310.pyc
|   |       |   |   |   |           test_list_accessor.cpython-310.pyc
|   |       |   |   |   |           test_sparse_accessor.cpython-310.pyc
|   |       |   |   |   |           test_struct_accessor.cpython-310.pyc
|   |       |   |   |   |           test_str_accessor.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---indexing
|   |       |   |   |   |   |   test_datetime.py
|   |       |   |   |   |   |   test_delitem.py
|   |       |   |   |   |   |   test_get.py
|   |       |   |   |   |   |   test_getitem.py
|   |       |   |   |   |   |   test_indexing.py
|   |       |   |   |   |   |   test_mask.py
|   |       |   |   |   |   |   test_setitem.py
|   |       |   |   |   |   |   test_set_value.py
|   |       |   |   |   |   |   test_take.py
|   |       |   |   |   |   |   test_where.py
|   |       |   |   |   |   |   test_xs.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_datetime.cpython-310.pyc
|   |       |   |   |   |           test_delitem.cpython-310.pyc
|   |       |   |   |   |           test_get.cpython-310.pyc
|   |       |   |   |   |           test_getitem.cpython-310.pyc
|   |       |   |   |   |           test_indexing.cpython-310.pyc
|   |       |   |   |   |           test_mask.cpython-310.pyc
|   |       |   |   |   |           test_setitem.cpython-310.pyc
|   |       |   |   |   |           test_set_value.cpython-310.pyc
|   |       |   |   |   |           test_take.cpython-310.pyc
|   |       |   |   |   |           test_where.cpython-310.pyc
|   |       |   |   |   |           test_xs.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---methods
|   |       |   |   |   |   |   test_add_prefix_suffix.py
|   |       |   |   |   |   |   test_align.py
|   |       |   |   |   |   |   test_argsort.py
|   |       |   |   |   |   |   test_asof.py
|   |       |   |   |   |   |   test_astype.py
|   |       |   |   |   |   |   test_autocorr.py
|   |       |   |   |   |   |   test_between.py
|   |       |   |   |   |   |   test_case_when.py
|   |       |   |   |   |   |   test_clip.py
|   |       |   |   |   |   |   test_combine.py
|   |       |   |   |   |   |   test_combine_first.py
|   |       |   |   |   |   |   test_compare.py
|   |       |   |   |   |   |   test_convert_dtypes.py
|   |       |   |   |   |   |   test_copy.py
|   |       |   |   |   |   |   test_count.py
|   |       |   |   |   |   |   test_cov_corr.py
|   |       |   |   |   |   |   test_describe.py
|   |       |   |   |   |   |   test_diff.py
|   |       |   |   |   |   |   test_drop.py
|   |       |   |   |   |   |   test_dropna.py
|   |       |   |   |   |   |   test_drop_duplicates.py
|   |       |   |   |   |   |   test_dtypes.py
|   |       |   |   |   |   |   test_duplicated.py
|   |       |   |   |   |   |   test_equals.py
|   |       |   |   |   |   |   test_explode.py
|   |       |   |   |   |   |   test_fillna.py
|   |       |   |   |   |   |   test_get_numeric_data.py
|   |       |   |   |   |   |   test_head_tail.py
|   |       |   |   |   |   |   test_infer_objects.py
|   |       |   |   |   |   |   test_info.py
|   |       |   |   |   |   |   test_interpolate.py
|   |       |   |   |   |   |   test_isin.py
|   |       |   |   |   |   |   test_isna.py
|   |       |   |   |   |   |   test_is_monotonic.py
|   |       |   |   |   |   |   test_is_unique.py
|   |       |   |   |   |   |   test_item.py
|   |       |   |   |   |   |   test_map.py
|   |       |   |   |   |   |   test_matmul.py
|   |       |   |   |   |   |   test_nlargest.py
|   |       |   |   |   |   |   test_nunique.py
|   |       |   |   |   |   |   test_pct_change.py
|   |       |   |   |   |   |   test_pop.py
|   |       |   |   |   |   |   test_quantile.py
|   |       |   |   |   |   |   test_rank.py
|   |       |   |   |   |   |   test_reindex.py
|   |       |   |   |   |   |   test_reindex_like.py
|   |       |   |   |   |   |   test_rename.py
|   |       |   |   |   |   |   test_rename_axis.py
|   |       |   |   |   |   |   test_repeat.py
|   |       |   |   |   |   |   test_replace.py
|   |       |   |   |   |   |   test_reset_index.py
|   |       |   |   |   |   |   test_round.py
|   |       |   |   |   |   |   test_searchsorted.py
|   |       |   |   |   |   |   test_set_name.py
|   |       |   |   |   |   |   test_size.py
|   |       |   |   |   |   |   test_sort_index.py
|   |       |   |   |   |   |   test_sort_values.py
|   |       |   |   |   |   |   test_tolist.py
|   |       |   |   |   |   |   test_to_csv.py
|   |       |   |   |   |   |   test_to_dict.py
|   |       |   |   |   |   |   test_to_frame.py
|   |       |   |   |   |   |   test_to_numpy.py
|   |       |   |   |   |   |   test_truncate.py
|   |       |   |   |   |   |   test_tz_localize.py
|   |       |   |   |   |   |   test_unique.py
|   |       |   |   |   |   |   test_unstack.py
|   |       |   |   |   |   |   test_update.py
|   |       |   |   |   |   |   test_values.py
|   |       |   |   |   |   |   test_value_counts.py
|   |       |   |   |   |   |   test_view.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_add_prefix_suffix.cpython-310.pyc
|   |       |   |   |   |           test_align.cpython-310.pyc
|   |       |   |   |   |           test_argsort.cpython-310.pyc
|   |       |   |   |   |           test_asof.cpython-310.pyc
|   |       |   |   |   |           test_astype.cpython-310.pyc
|   |       |   |   |   |           test_autocorr.cpython-310.pyc
|   |       |   |   |   |           test_between.cpython-310.pyc
|   |       |   |   |   |           test_case_when.cpython-310.pyc
|   |       |   |   |   |           test_clip.cpython-310.pyc
|   |       |   |   |   |           test_combine.cpython-310.pyc
|   |       |   |   |   |           test_combine_first.cpython-310.pyc
|   |       |   |   |   |           test_compare.cpython-310.pyc
|   |       |   |   |   |           test_convert_dtypes.cpython-310.pyc
|   |       |   |   |   |           test_copy.cpython-310.pyc
|   |       |   |   |   |           test_count.cpython-310.pyc
|   |       |   |   |   |           test_cov_corr.cpython-310.pyc
|   |       |   |   |   |           test_describe.cpython-310.pyc
|   |       |   |   |   |           test_diff.cpython-310.pyc
|   |       |   |   |   |           test_drop.cpython-310.pyc
|   |       |   |   |   |           test_dropna.cpython-310.pyc
|   |       |   |   |   |           test_drop_duplicates.cpython-310.pyc
|   |       |   |   |   |           test_dtypes.cpython-310.pyc
|   |       |   |   |   |           test_duplicated.cpython-310.pyc
|   |       |   |   |   |           test_equals.cpython-310.pyc
|   |       |   |   |   |           test_explode.cpython-310.pyc
|   |       |   |   |   |           test_fillna.cpython-310.pyc
|   |       |   |   |   |           test_get_numeric_data.cpython-310.pyc
|   |       |   |   |   |           test_head_tail.cpython-310.pyc
|   |       |   |   |   |           test_infer_objects.cpython-310.pyc
|   |       |   |   |   |           test_info.cpython-310.pyc
|   |       |   |   |   |           test_interpolate.cpython-310.pyc
|   |       |   |   |   |           test_isin.cpython-310.pyc
|   |       |   |   |   |           test_isna.cpython-310.pyc
|   |       |   |   |   |           test_is_monotonic.cpython-310.pyc
|   |       |   |   |   |           test_is_unique.cpython-310.pyc
|   |       |   |   |   |           test_item.cpython-310.pyc
|   |       |   |   |   |           test_map.cpython-310.pyc
|   |       |   |   |   |           test_matmul.cpython-310.pyc
|   |       |   |   |   |           test_nlargest.cpython-310.pyc
|   |       |   |   |   |           test_nunique.cpython-310.pyc
|   |       |   |   |   |           test_pct_change.cpython-310.pyc
|   |       |   |   |   |           test_pop.cpython-310.pyc
|   |       |   |   |   |           test_quantile.cpython-310.pyc
|   |       |   |   |   |           test_rank.cpython-310.pyc
|   |       |   |   |   |           test_reindex.cpython-310.pyc
|   |       |   |   |   |           test_reindex_like.cpython-310.pyc
|   |       |   |   |   |           test_rename.cpython-310.pyc
|   |       |   |   |   |           test_rename_axis.cpython-310.pyc
|   |       |   |   |   |           test_repeat.cpython-310.pyc
|   |       |   |   |   |           test_replace.cpython-310.pyc
|   |       |   |   |   |           test_reset_index.cpython-310.pyc
|   |       |   |   |   |           test_round.cpython-310.pyc
|   |       |   |   |   |           test_searchsorted.cpython-310.pyc
|   |       |   |   |   |           test_set_name.cpython-310.pyc
|   |       |   |   |   |           test_size.cpython-310.pyc
|   |       |   |   |   |           test_sort_index.cpython-310.pyc
|   |       |   |   |   |           test_sort_values.cpython-310.pyc
|   |       |   |   |   |           test_tolist.cpython-310.pyc
|   |       |   |   |   |           test_to_csv.cpython-310.pyc
|   |       |   |   |   |           test_to_dict.cpython-310.pyc
|   |       |   |   |   |           test_to_frame.cpython-310.pyc
|   |       |   |   |   |           test_to_numpy.cpython-310.pyc
|   |       |   |   |   |           test_truncate.cpython-310.pyc
|   |       |   |   |   |           test_tz_localize.cpython-310.pyc
|   |       |   |   |   |           test_unique.cpython-310.pyc
|   |       |   |   |   |           test_unstack.cpython-310.pyc
|   |       |   |   |   |           test_update.cpython-310.pyc
|   |       |   |   |   |           test_values.cpython-310.pyc
|   |       |   |   |   |           test_value_counts.cpython-310.pyc
|   |       |   |   |   |           test_view.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_api.cpython-310.pyc
|   |       |   |   |           test_arithmetic.cpython-310.pyc
|   |       |   |   |           test_constructors.cpython-310.pyc
|   |       |   |   |           test_cumulative.cpython-310.pyc
|   |       |   |   |           test_formats.cpython-310.pyc
|   |       |   |   |           test_iteration.cpython-310.pyc
|   |       |   |   |           test_logical_ops.cpython-310.pyc
|   |       |   |   |           test_missing.cpython-310.pyc
|   |       |   |   |           test_npfuncs.cpython-310.pyc
|   |       |   |   |           test_reductions.cpython-310.pyc
|   |       |   |   |           test_subclass.cpython-310.pyc
|   |       |   |   |           test_ufunc.cpython-310.pyc
|   |       |   |   |           test_unary.cpython-310.pyc
|   |       |   |   |           test_validate.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---strings
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_api.py
|   |       |   |   |   |   test_case_justify.py
|   |       |   |   |   |   test_cat.py
|   |       |   |   |   |   test_extract.py
|   |       |   |   |   |   test_find_replace.py
|   |       |   |   |   |   test_get_dummies.py
|   |       |   |   |   |   test_split_partition.py
|   |       |   |   |   |   test_strings.py
|   |       |   |   |   |   test_string_array.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           conftest.cpython-310.pyc
|   |       |   |   |           test_api.cpython-310.pyc
|   |       |   |   |           test_case_justify.cpython-310.pyc
|   |       |   |   |           test_cat.cpython-310.pyc
|   |       |   |   |           test_extract.cpython-310.pyc
|   |       |   |   |           test_find_replace.cpython-310.pyc
|   |       |   |   |           test_get_dummies.cpython-310.pyc
|   |       |   |   |           test_split_partition.cpython-310.pyc
|   |       |   |   |           test_strings.cpython-310.pyc
|   |       |   |   |           test_string_array.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---tools
|   |       |   |   |   |   test_to_datetime.py
|   |       |   |   |   |   test_to_numeric.py
|   |       |   |   |   |   test_to_time.py
|   |       |   |   |   |   test_to_timedelta.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_to_datetime.cpython-310.pyc
|   |       |   |   |           test_to_numeric.cpython-310.pyc
|   |       |   |   |           test_to_time.cpython-310.pyc
|   |       |   |   |           test_to_timedelta.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---tseries
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---frequencies
|   |       |   |   |   |   |   test_frequencies.py
|   |       |   |   |   |   |   test_freq_code.py
|   |       |   |   |   |   |   test_inference.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_frequencies.cpython-310.pyc
|   |       |   |   |   |           test_freq_code.cpython-310.pyc
|   |       |   |   |   |           test_inference.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---holiday
|   |       |   |   |   |   |   test_calendar.py
|   |       |   |   |   |   |   test_federal.py
|   |       |   |   |   |   |   test_holiday.py
|   |       |   |   |   |   |   test_observance.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           test_calendar.cpython-310.pyc
|   |       |   |   |   |           test_federal.cpython-310.pyc
|   |       |   |   |   |           test_holiday.cpython-310.pyc
|   |       |   |   |   |           test_observance.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---offsets
|   |       |   |   |   |   |   common.py
|   |       |   |   |   |   |   test_business_day.py
|   |       |   |   |   |   |   test_business_hour.py
|   |       |   |   |   |   |   test_business_month.py
|   |       |   |   |   |   |   test_business_quarter.py
|   |       |   |   |   |   |   test_business_year.py
|   |       |   |   |   |   |   test_common.py
|   |       |   |   |   |   |   test_custom_business_day.py
|   |       |   |   |   |   |   test_custom_business_hour.py
|   |       |   |   |   |   |   test_custom_business_month.py
|   |       |   |   |   |   |   test_dst.py
|   |       |   |   |   |   |   test_easter.py
|   |       |   |   |   |   |   test_fiscal.py
|   |       |   |   |   |   |   test_index.py
|   |       |   |   |   |   |   test_month.py
|   |       |   |   |   |   |   test_offsets.py
|   |       |   |   |   |   |   test_offsets_properties.py
|   |       |   |   |   |   |   test_quarter.py
|   |       |   |   |   |   |   test_ticks.py
|   |       |   |   |   |   |   test_week.py
|   |       |   |   |   |   |   test_year.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           common.cpython-310.pyc
|   |       |   |   |   |           test_business_day.cpython-310.pyc
|   |       |   |   |   |           test_business_hour.cpython-310.pyc
|   |       |   |   |   |           test_business_month.cpython-310.pyc
|   |       |   |   |   |           test_business_quarter.cpython-310.pyc
|   |       |   |   |   |           test_business_year.cpython-310.pyc
|   |       |   |   |   |           test_common.cpython-310.pyc
|   |       |   |   |   |           test_custom_business_day.cpython-310.pyc
|   |       |   |   |   |           test_custom_business_hour.cpython-310.pyc
|   |       |   |   |   |           test_custom_business_month.cpython-310.pyc
|   |       |   |   |   |           test_dst.cpython-310.pyc
|   |       |   |   |   |           test_easter.cpython-310.pyc
|   |       |   |   |   |           test_fiscal.cpython-310.pyc
|   |       |   |   |   |           test_index.cpython-310.pyc
|   |       |   |   |   |           test_month.cpython-310.pyc
|   |       |   |   |   |           test_offsets.cpython-310.pyc
|   |       |   |   |   |           test_offsets_properties.cpython-310.pyc
|   |       |   |   |   |           test_quarter.cpython-310.pyc
|   |       |   |   |   |           test_ticks.cpython-310.pyc
|   |       |   |   |   |           test_week.cpython-310.pyc
|   |       |   |   |   |           test_year.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---tslibs
|   |       |   |   |   |   test_api.py
|   |       |   |   |   |   test_array_to_datetime.py
|   |       |   |   |   |   test_ccalendar.py
|   |       |   |   |   |   test_conversion.py
|   |       |   |   |   |   test_fields.py
|   |       |   |   |   |   test_libfrequencies.py
|   |       |   |   |   |   test_liboffsets.py
|   |       |   |   |   |   test_npy_units.py
|   |       |   |   |   |   test_np_datetime.py
|   |       |   |   |   |   test_parse_iso8601.py
|   |       |   |   |   |   test_parsing.py
|   |       |   |   |   |   test_period.py
|   |       |   |   |   |   test_resolution.py
|   |       |   |   |   |   test_strptime.py
|   |       |   |   |   |   test_timedeltas.py
|   |       |   |   |   |   test_timezones.py
|   |       |   |   |   |   test_to_offset.py
|   |       |   |   |   |   test_tzconversion.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           test_api.cpython-310.pyc
|   |       |   |   |           test_array_to_datetime.cpython-310.pyc
|   |       |   |   |           test_ccalendar.cpython-310.pyc
|   |       |   |   |           test_conversion.cpython-310.pyc
|   |       |   |   |           test_fields.cpython-310.pyc
|   |       |   |   |           test_libfrequencies.cpython-310.pyc
|   |       |   |   |           test_liboffsets.cpython-310.pyc
|   |       |   |   |           test_npy_units.cpython-310.pyc
|   |       |   |   |           test_np_datetime.cpython-310.pyc
|   |       |   |   |           test_parse_iso8601.cpython-310.pyc
|   |       |   |   |           test_parsing.cpython-310.pyc
|   |       |   |   |           test_period.cpython-310.pyc
|   |       |   |   |           test_resolution.cpython-310.pyc
|   |       |   |   |           test_strptime.cpython-310.pyc
|   |       |   |   |           test_timedeltas.cpython-310.pyc
|   |       |   |   |           test_timezones.cpython-310.pyc
|   |       |   |   |           test_to_offset.cpython-310.pyc
|   |       |   |   |           test_tzconversion.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---util
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_assert_almost_equal.py
|   |       |   |   |   |   test_assert_attr_equal.py
|   |       |   |   |   |   test_assert_categorical_equal.py
|   |       |   |   |   |   test_assert_extension_array_equal.py
|   |       |   |   |   |   test_assert_frame_equal.py
|   |       |   |   |   |   test_assert_index_equal.py
|   |       |   |   |   |   test_assert_interval_array_equal.py
|   |       |   |   |   |   test_assert_numpy_array_equal.py
|   |       |   |   |   |   test_assert_produces_warning.py
|   |       |   |   |   |   test_assert_series_equal.py
|   |       |   |   |   |   test_deprecate.py
|   |       |   |   |   |   test_deprecate_kwarg.py
|   |       |   |   |   |   test_deprecate_nonkeyword_arguments.py
|   |       |   |   |   |   test_doc.py
|   |       |   |   |   |   test_hashing.py
|   |       |   |   |   |   test_numba.py
|   |       |   |   |   |   test_rewrite_warning.py
|   |       |   |   |   |   test_shares_memory.py
|   |       |   |   |   |   test_show_versions.py
|   |       |   |   |   |   test_util.py
|   |       |   |   |   |   test_validate_args.py
|   |       |   |   |   |   test_validate_args_and_kwargs.py
|   |       |   |   |   |   test_validate_inclusive.py
|   |       |   |   |   |   test_validate_kwargs.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           conftest.cpython-310.pyc
|   |       |   |   |           test_assert_almost_equal.cpython-310.pyc
|   |       |   |   |           test_assert_attr_equal.cpython-310.pyc
|   |       |   |   |           test_assert_categorical_equal.cpython-310.pyc
|   |       |   |   |           test_assert_extension_array_equal.cpython-310.pyc
|   |       |   |   |           test_assert_frame_equal.cpython-310.pyc
|   |       |   |   |           test_assert_index_equal.cpython-310.pyc
|   |       |   |   |           test_assert_interval_array_equal.cpython-310.pyc
|   |       |   |   |           test_assert_numpy_array_equal.cpython-310.pyc
|   |       |   |   |           test_assert_produces_warning.cpython-310.pyc
|   |       |   |   |           test_assert_series_equal.cpython-310.pyc
|   |       |   |   |           test_deprecate.cpython-310.pyc
|   |       |   |   |           test_deprecate_kwarg.cpython-310.pyc
|   |       |   |   |           test_deprecate_nonkeyword_arguments.cpython-310.pyc
|   |       |   |   |           test_doc.cpython-310.pyc
|   |       |   |   |           test_hashing.cpython-310.pyc
|   |       |   |   |           test_numba.cpython-310.pyc
|   |       |   |   |           test_rewrite_warning.cpython-310.pyc
|   |       |   |   |           test_shares_memory.cpython-310.pyc
|   |       |   |   |           test_show_versions.cpython-310.pyc
|   |       |   |   |           test_util.cpython-310.pyc
|   |       |   |   |           test_validate_args.cpython-310.pyc
|   |       |   |   |           test_validate_args_and_kwargs.cpython-310.pyc
|   |       |   |   |           test_validate_inclusive.cpython-310.pyc
|   |       |   |   |           test_validate_kwargs.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---window
|   |       |   |   |   |   conftest.py
|   |       |   |   |   |   test_api.py
|   |       |   |   |   |   test_apply.py
|   |       |   |   |   |   test_base_indexer.py
|   |       |   |   |   |   test_cython_aggregations.py
|   |       |   |   |   |   test_dtypes.py
|   |       |   |   |   |   test_ewm.py
|   |       |   |   |   |   test_expanding.py
|   |       |   |   |   |   test_groupby.py
|   |       |   |   |   |   test_numba.py
|   |       |   |   |   |   test_online.py
|   |       |   |   |   |   test_pairwise.py
|   |       |   |   |   |   test_rolling.py
|   |       |   |   |   |   test_rolling_functions.py
|   |       |   |   |   |   test_rolling_quantile.py
|   |       |   |   |   |   test_rolling_skew_kurt.py
|   |       |   |   |   |   test_timeseries_window.py
|   |       |   |   |   |   test_win_type.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---moments
|   |       |   |   |   |   |   conftest.py
|   |       |   |   |   |   |   test_moments_consistency_ewm.py
|   |       |   |   |   |   |   test_moments_consistency_expanding.py
|   |       |   |   |   |   |   test_moments_consistency_rolling.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           conftest.cpython-310.pyc
|   |       |   |   |   |           test_moments_consistency_ewm.cpython-310.pyc
|   |       |   |   |   |           test_moments_consistency_expanding.cpython-310.pyc
|   |       |   |   |   |           test_moments_consistency_rolling.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           conftest.cpython-310.pyc
|   |       |   |   |           test_api.cpython-310.pyc
|   |       |   |   |           test_apply.cpython-310.pyc
|   |       |   |   |           test_base_indexer.cpython-310.pyc
|   |       |   |   |           test_cython_aggregations.cpython-310.pyc
|   |       |   |   |           test_dtypes.cpython-310.pyc
|   |       |   |   |           test_ewm.cpython-310.pyc
|   |       |   |   |           test_expanding.cpython-310.pyc
|   |       |   |   |           test_groupby.cpython-310.pyc
|   |       |   |   |           test_numba.cpython-310.pyc
|   |       |   |   |           test_online.cpython-310.pyc
|   |       |   |   |           test_pairwise.cpython-310.pyc
|   |       |   |   |           test_rolling.cpython-310.pyc
|   |       |   |   |           test_rolling_functions.cpython-310.pyc
|   |       |   |   |           test_rolling_quantile.cpython-310.pyc
|   |       |   |   |           test_rolling_skew_kurt.cpython-310.pyc
|   |       |   |   |           test_timeseries_window.cpython-310.pyc
|   |       |   |   |           test_win_type.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           test_aggregation.cpython-310.pyc
|   |       |   |           test_algos.cpython-310.pyc
|   |       |   |           test_common.cpython-310.pyc
|   |       |   |           test_downstream.cpython-310.pyc
|   |       |   |           test_errors.cpython-310.pyc
|   |       |   |           test_expressions.cpython-310.pyc
|   |       |   |           test_flags.cpython-310.pyc
|   |       |   |           test_multilevel.cpython-310.pyc
|   |       |   |           test_nanops.cpython-310.pyc
|   |       |   |           test_optional_dependency.cpython-310.pyc
|   |       |   |           test_register_accessor.cpython-310.pyc
|   |       |   |           test_sorting.cpython-310.pyc
|   |       |   |           test_take.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---tseries
|   |       |   |   |   api.py
|   |       |   |   |   frequencies.py
|   |       |   |   |   holiday.py
|   |       |   |   |   offsets.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           api.cpython-310.pyc
|   |       |   |           frequencies.cpython-310.pyc
|   |       |   |           holiday.cpython-310.pyc
|   |       |   |           offsets.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---util
|   |       |   |   |   _decorators.py
|   |       |   |   |   _doctools.py
|   |       |   |   |   _exceptions.py
|   |       |   |   |   _print_versions.py
|   |       |   |   |   _tester.py
|   |       |   |   |   _test_decorators.py
|   |       |   |   |   _validators.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---version
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           _decorators.cpython-310.pyc
|   |       |   |           _doctools.cpython-310.pyc
|   |       |   |           _exceptions.cpython-310.pyc
|   |       |   |           _print_versions.cpython-310.pyc
|   |       |   |           _tester.cpython-310.pyc
|   |       |   |           _test_decorators.cpython-310.pyc
|   |       |   |           _validators.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_config
|   |       |   |   |   config.py
|   |       |   |   |   dates.py
|   |       |   |   |   display.py
|   |       |   |   |   localization.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           config.cpython-310.pyc
|   |       |   |           dates.cpython-310.pyc
|   |       |   |           display.cpython-310.pyc
|   |       |   |           localization.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_libs
|   |       |   |   |   algos.cp310-win_amd64.lib
|   |       |   |   |   algos.cp310-win_amd64.pyd
|   |       |   |   |   algos.pyi
|   |       |   |   |   arrays.cp310-win_amd64.lib
|   |       |   |   |   arrays.cp310-win_amd64.pyd
|   |       |   |   |   arrays.pyi
|   |       |   |   |   byteswap.cp310-win_amd64.lib
|   |       |   |   |   byteswap.cp310-win_amd64.pyd
|   |       |   |   |   byteswap.pyi
|   |       |   |   |   groupby.cp310-win_amd64.lib
|   |       |   |   |   groupby.cp310-win_amd64.pyd
|   |       |   |   |   groupby.pyi
|   |       |   |   |   hashing.cp310-win_amd64.lib
|   |       |   |   |   hashing.cp310-win_amd64.pyd
|   |       |   |   |   hashing.pyi
|   |       |   |   |   hashtable.cp310-win_amd64.lib
|   |       |   |   |   hashtable.cp310-win_amd64.pyd
|   |       |   |   |   hashtable.pyi
|   |       |   |   |   index.cp310-win_amd64.lib
|   |       |   |   |   index.cp310-win_amd64.pyd
|   |       |   |   |   index.pyi
|   |       |   |   |   indexing.cp310-win_amd64.lib
|   |       |   |   |   indexing.cp310-win_amd64.pyd
|   |       |   |   |   indexing.pyi
|   |       |   |   |   internals.cp310-win_amd64.lib
|   |       |   |   |   internals.cp310-win_amd64.pyd
|   |       |   |   |   internals.pyi
|   |       |   |   |   interval.cp310-win_amd64.lib
|   |       |   |   |   interval.cp310-win_amd64.pyd
|   |       |   |   |   interval.pyi
|   |       |   |   |   join.cp310-win_amd64.lib
|   |       |   |   |   join.cp310-win_amd64.pyd
|   |       |   |   |   join.pyi
|   |       |   |   |   json.cp310-win_amd64.lib
|   |       |   |   |   json.cp310-win_amd64.pyd
|   |       |   |   |   json.pyi
|   |       |   |   |   lib.cp310-win_amd64.lib
|   |       |   |   |   lib.cp310-win_amd64.pyd
|   |       |   |   |   lib.pyi
|   |       |   |   |   missing.cp310-win_amd64.lib
|   |       |   |   |   missing.cp310-win_amd64.pyd
|   |       |   |   |   missing.pyi
|   |       |   |   |   ops.cp310-win_amd64.lib
|   |       |   |   |   ops.cp310-win_amd64.pyd
|   |       |   |   |   ops.pyi
|   |       |   |   |   ops_dispatch.cp310-win_amd64.lib
|   |       |   |   |   ops_dispatch.cp310-win_amd64.pyd
|   |       |   |   |   ops_dispatch.pyi
|   |       |   |   |   pandas_datetime.cp310-win_amd64.lib
|   |       |   |   |   pandas_datetime.cp310-win_amd64.pyd
|   |       |   |   |   pandas_parser.cp310-win_amd64.lib
|   |       |   |   |   pandas_parser.cp310-win_amd64.pyd
|   |       |   |   |   parsers.cp310-win_amd64.lib
|   |       |   |   |   parsers.cp310-win_amd64.pyd
|   |       |   |   |   parsers.pyi
|   |       |   |   |   properties.cp310-win_amd64.lib
|   |       |   |   |   properties.cp310-win_amd64.pyd
|   |       |   |   |   properties.pyi
|   |       |   |   |   reshape.cp310-win_amd64.lib
|   |       |   |   |   reshape.cp310-win_amd64.pyd
|   |       |   |   |   reshape.pyi
|   |       |   |   |   sas.cp310-win_amd64.lib
|   |       |   |   |   sas.cp310-win_amd64.pyd
|   |       |   |   |   sas.pyi
|   |       |   |   |   sparse.cp310-win_amd64.lib
|   |       |   |   |   sparse.cp310-win_amd64.pyd
|   |       |   |   |   sparse.pyi
|   |       |   |   |   testing.cp310-win_amd64.lib
|   |       |   |   |   testing.cp310-win_amd64.pyd
|   |       |   |   |   testing.pyi
|   |       |   |   |   tslib.cp310-win_amd64.lib
|   |       |   |   |   tslib.cp310-win_amd64.pyd
|   |       |   |   |   tslib.pyi
|   |       |   |   |   writers.cp310-win_amd64.lib
|   |       |   |   |   writers.cp310-win_amd64.pyd
|   |       |   |   |   writers.pyi
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---tslibs
|   |       |   |   |   |   base.cp310-win_amd64.lib
|   |       |   |   |   |   base.cp310-win_amd64.pyd
|   |       |   |   |   |   ccalendar.cp310-win_amd64.lib
|   |       |   |   |   |   ccalendar.cp310-win_amd64.pyd
|   |       |   |   |   |   ccalendar.pyi
|   |       |   |   |   |   conversion.cp310-win_amd64.lib
|   |       |   |   |   |   conversion.cp310-win_amd64.pyd
|   |       |   |   |   |   conversion.pyi
|   |       |   |   |   |   dtypes.cp310-win_amd64.lib
|   |       |   |   |   |   dtypes.cp310-win_amd64.pyd
|   |       |   |   |   |   dtypes.pyi
|   |       |   |   |   |   fields.cp310-win_amd64.lib
|   |       |   |   |   |   fields.cp310-win_amd64.pyd
|   |       |   |   |   |   fields.pyi
|   |       |   |   |   |   nattype.cp310-win_amd64.lib
|   |       |   |   |   |   nattype.cp310-win_amd64.pyd
|   |       |   |   |   |   nattype.pyi
|   |       |   |   |   |   np_datetime.cp310-win_amd64.lib
|   |       |   |   |   |   np_datetime.cp310-win_amd64.pyd
|   |       |   |   |   |   np_datetime.pyi
|   |       |   |   |   |   offsets.cp310-win_amd64.lib
|   |       |   |   |   |   offsets.cp310-win_amd64.pyd
|   |       |   |   |   |   offsets.pyi
|   |       |   |   |   |   parsing.cp310-win_amd64.lib
|   |       |   |   |   |   parsing.cp310-win_amd64.pyd
|   |       |   |   |   |   parsing.pyi
|   |       |   |   |   |   period.cp310-win_amd64.lib
|   |       |   |   |   |   period.cp310-win_amd64.pyd
|   |       |   |   |   |   period.pyi
|   |       |   |   |   |   strptime.cp310-win_amd64.lib
|   |       |   |   |   |   strptime.cp310-win_amd64.pyd
|   |       |   |   |   |   strptime.pyi
|   |       |   |   |   |   timedeltas.cp310-win_amd64.lib
|   |       |   |   |   |   timedeltas.cp310-win_amd64.pyd
|   |       |   |   |   |   timedeltas.pyi
|   |       |   |   |   |   timestamps.cp310-win_amd64.lib
|   |       |   |   |   |   timestamps.cp310-win_amd64.pyd
|   |       |   |   |   |   timestamps.pyi
|   |       |   |   |   |   timezones.cp310-win_amd64.lib
|   |       |   |   |   |   timezones.cp310-win_amd64.pyd
|   |       |   |   |   |   timezones.pyi
|   |       |   |   |   |   tzconversion.cp310-win_amd64.lib
|   |       |   |   |   |   tzconversion.cp310-win_amd64.pyd
|   |       |   |   |   |   tzconversion.pyi
|   |       |   |   |   |   vectorized.cp310-win_amd64.lib
|   |       |   |   |   |   vectorized.cp310-win_amd64.pyd
|   |       |   |   |   |   vectorized.pyi
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---window
|   |       |   |   |   |   aggregations.cp310-win_amd64.lib
|   |       |   |   |   |   aggregations.cp310-win_amd64.pyd
|   |       |   |   |   |   aggregations.pyi
|   |       |   |   |   |   indexers.cp310-win_amd64.lib
|   |       |   |   |   |   indexers.cp310-win_amd64.pyd
|   |       |   |   |   |   indexers.pyi
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_testing
|   |       |   |   |   asserters.py
|   |       |   |   |   compat.py
|   |       |   |   |   contexts.py
|   |       |   |   |   _hypothesis.py
|   |       |   |   |   _io.py
|   |       |   |   |   _warnings.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           asserters.cpython-310.pyc
|   |       |   |           compat.cpython-310.pyc
|   |       |   |           contexts.cpython-310.pyc
|   |       |   |           _hypothesis.cpython-310.pyc
|   |       |   |           _io.cpython-310.pyc
|   |       |   |           _warnings.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           conftest.cpython-310.pyc
|   |       |           testing.cpython-310.pyc
|   |       |           _typing.cpython-310.pyc
|   |       |           _version.cpython-310.pyc
|   |       |           _version_meson.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---pandas-2.3.3.dist-info
|   |       |       DELVEWHEEL
|   |       |       entry_points.txt
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       WHEEL
|   |       |       
|   |       +---pandas.libs
|   |       |       msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
|   |       |       
|   |       +---pip
|   |       |   |   py.typed
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   __pip-runner__.py
|   |       |   |   
|   |       |   +---_internal
|   |       |   |   |   build_env.py
|   |       |   |   |   cache.py
|   |       |   |   |   configuration.py
|   |       |   |   |   exceptions.py
|   |       |   |   |   main.py
|   |       |   |   |   pyproject.py
|   |       |   |   |   self_outdated_check.py
|   |       |   |   |   wheel_builder.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---cli
|   |       |   |   |   |   autocompletion.py
|   |       |   |   |   |   base_command.py
|   |       |   |   |   |   cmdoptions.py
|   |       |   |   |   |   command_context.py
|   |       |   |   |   |   main.py
|   |       |   |   |   |   main_parser.py
|   |       |   |   |   |   parser.py
|   |       |   |   |   |   progress_bars.py
|   |       |   |   |   |   req_command.py
|   |       |   |   |   |   spinners.py
|   |       |   |   |   |   status_codes.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           autocompletion.cpython-310.pyc
|   |       |   |   |           base_command.cpython-310.pyc
|   |       |   |   |           cmdoptions.cpython-310.pyc
|   |       |   |   |           command_context.cpython-310.pyc
|   |       |   |   |           main.cpython-310.pyc
|   |       |   |   |           main_parser.cpython-310.pyc
|   |       |   |   |           parser.cpython-310.pyc
|   |       |   |   |           progress_bars.cpython-310.pyc
|   |       |   |   |           req_command.cpython-310.pyc
|   |       |   |   |           spinners.cpython-310.pyc
|   |       |   |   |           status_codes.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---commands
|   |       |   |   |   |   cache.py
|   |       |   |   |   |   check.py
|   |       |   |   |   |   completion.py
|   |       |   |   |   |   configuration.py
|   |       |   |   |   |   debug.py
|   |       |   |   |   |   download.py
|   |       |   |   |   |   freeze.py
|   |       |   |   |   |   hash.py
|   |       |   |   |   |   help.py
|   |       |   |   |   |   index.py
|   |       |   |   |   |   inspect.py
|   |       |   |   |   |   install.py
|   |       |   |   |   |   list.py
|   |       |   |   |   |   search.py
|   |       |   |   |   |   show.py
|   |       |   |   |   |   uninstall.py
|   |       |   |   |   |   wheel.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           cache.cpython-310.pyc
|   |       |   |   |           check.cpython-310.pyc
|   |       |   |   |           completion.cpython-310.pyc
|   |       |   |   |           configuration.cpython-310.pyc
|   |       |   |   |           debug.cpython-310.pyc
|   |       |   |   |           download.cpython-310.pyc
|   |       |   |   |           freeze.cpython-310.pyc
|   |       |   |   |           hash.cpython-310.pyc
|   |       |   |   |           help.cpython-310.pyc
|   |       |   |   |           index.cpython-310.pyc
|   |       |   |   |           inspect.cpython-310.pyc
|   |       |   |   |           install.cpython-310.pyc
|   |       |   |   |           list.cpython-310.pyc
|   |       |   |   |           search.cpython-310.pyc
|   |       |   |   |           show.cpython-310.pyc
|   |       |   |   |           uninstall.cpython-310.pyc
|   |       |   |   |           wheel.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---distributions
|   |       |   |   |   |   base.py
|   |       |   |   |   |   installed.py
|   |       |   |   |   |   sdist.py
|   |       |   |   |   |   wheel.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           base.cpython-310.pyc
|   |       |   |   |           installed.cpython-310.pyc
|   |       |   |   |           sdist.cpython-310.pyc
|   |       |   |   |           wheel.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---index
|   |       |   |   |   |   collector.py
|   |       |   |   |   |   package_finder.py
|   |       |   |   |   |   sources.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           collector.cpython-310.pyc
|   |       |   |   |           package_finder.cpython-310.pyc
|   |       |   |   |           sources.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---locations
|   |       |   |   |   |   base.py
|   |       |   |   |   |   _distutils.py
|   |       |   |   |   |   _sysconfig.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           base.cpython-310.pyc
|   |       |   |   |           _distutils.cpython-310.pyc
|   |       |   |   |           _sysconfig.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---metadata
|   |       |   |   |   |   base.py
|   |       |   |   |   |   pkg_resources.py
|   |       |   |   |   |   _json.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---importlib
|   |       |   |   |   |   |   _compat.py
|   |       |   |   |   |   |   _dists.py
|   |       |   |   |   |   |   _envs.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           _compat.cpython-310.pyc
|   |       |   |   |   |           _dists.cpython-310.pyc
|   |       |   |   |   |           _envs.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           base.cpython-310.pyc
|   |       |   |   |           pkg_resources.cpython-310.pyc
|   |       |   |   |           _json.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---models
|   |       |   |   |   |   candidate.py
|   |       |   |   |   |   direct_url.py
|   |       |   |   |   |   format_control.py
|   |       |   |   |   |   index.py
|   |       |   |   |   |   installation_report.py
|   |       |   |   |   |   link.py
|   |       |   |   |   |   scheme.py
|   |       |   |   |   |   search_scope.py
|   |       |   |   |   |   selection_prefs.py
|   |       |   |   |   |   target_python.py
|   |       |   |   |   |   wheel.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           candidate.cpython-310.pyc
|   |       |   |   |           direct_url.cpython-310.pyc
|   |       |   |   |           format_control.cpython-310.pyc
|   |       |   |   |           index.cpython-310.pyc
|   |       |   |   |           installation_report.cpython-310.pyc
|   |       |   |   |           link.cpython-310.pyc
|   |       |   |   |           scheme.cpython-310.pyc
|   |       |   |   |           search_scope.cpython-310.pyc
|   |       |   |   |           selection_prefs.cpython-310.pyc
|   |       |   |   |           target_python.cpython-310.pyc
|   |       |   |   |           wheel.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---network
|   |       |   |   |   |   auth.py
|   |       |   |   |   |   cache.py
|   |       |   |   |   |   download.py
|   |       |   |   |   |   lazy_wheel.py
|   |       |   |   |   |   session.py
|   |       |   |   |   |   utils.py
|   |       |   |   |   |   xmlrpc.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           auth.cpython-310.pyc
|   |       |   |   |           cache.cpython-310.pyc
|   |       |   |   |           download.cpython-310.pyc
|   |       |   |   |           lazy_wheel.cpython-310.pyc
|   |       |   |   |           session.cpython-310.pyc
|   |       |   |   |           utils.cpython-310.pyc
|   |       |   |   |           xmlrpc.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---operations
|   |       |   |   |   |   check.py
|   |       |   |   |   |   freeze.py
|   |       |   |   |   |   prepare.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---build
|   |       |   |   |   |   |   build_tracker.py
|   |       |   |   |   |   |   metadata.py
|   |       |   |   |   |   |   metadata_editable.py
|   |       |   |   |   |   |   metadata_legacy.py
|   |       |   |   |   |   |   wheel.py
|   |       |   |   |   |   |   wheel_editable.py
|   |       |   |   |   |   |   wheel_legacy.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           build_tracker.cpython-310.pyc
|   |       |   |   |   |           metadata.cpython-310.pyc
|   |       |   |   |   |           metadata_editable.cpython-310.pyc
|   |       |   |   |   |           metadata_legacy.cpython-310.pyc
|   |       |   |   |   |           wheel.cpython-310.pyc
|   |       |   |   |   |           wheel_editable.cpython-310.pyc
|   |       |   |   |   |           wheel_legacy.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---install
|   |       |   |   |   |   |   editable_legacy.py
|   |       |   |   |   |   |   legacy.py
|   |       |   |   |   |   |   wheel.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           editable_legacy.cpython-310.pyc
|   |       |   |   |   |           legacy.cpython-310.pyc
|   |       |   |   |   |           wheel.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           check.cpython-310.pyc
|   |       |   |   |           freeze.cpython-310.pyc
|   |       |   |   |           prepare.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---req
|   |       |   |   |   |   constructors.py
|   |       |   |   |   |   req_file.py
|   |       |   |   |   |   req_install.py
|   |       |   |   |   |   req_set.py
|   |       |   |   |   |   req_uninstall.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           constructors.cpython-310.pyc
|   |       |   |   |           req_file.cpython-310.pyc
|   |       |   |   |           req_install.cpython-310.pyc
|   |       |   |   |           req_set.cpython-310.pyc
|   |       |   |   |           req_uninstall.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---resolution
|   |       |   |   |   |   base.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---legacy
|   |       |   |   |   |   |   resolver.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           resolver.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---resolvelib
|   |       |   |   |   |   |   base.py
|   |       |   |   |   |   |   candidates.py
|   |       |   |   |   |   |   factory.py
|   |       |   |   |   |   |   found_candidates.py
|   |       |   |   |   |   |   provider.py
|   |       |   |   |   |   |   reporter.py
|   |       |   |   |   |   |   requirements.py
|   |       |   |   |   |   |   resolver.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           base.cpython-310.pyc
|   |       |   |   |   |           candidates.cpython-310.pyc
|   |       |   |   |   |           factory.cpython-310.pyc
|   |       |   |   |   |           found_candidates.cpython-310.pyc
|   |       |   |   |   |           provider.cpython-310.pyc
|   |       |   |   |   |           reporter.cpython-310.pyc
|   |       |   |   |   |           requirements.cpython-310.pyc
|   |       |   |   |   |           resolver.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           base.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---utils
|   |       |   |   |   |   appdirs.py
|   |       |   |   |   |   compat.py
|   |       |   |   |   |   compatibility_tags.py
|   |       |   |   |   |   datetime.py
|   |       |   |   |   |   deprecation.py
|   |       |   |   |   |   direct_url_helpers.py
|   |       |   |   |   |   distutils_args.py
|   |       |   |   |   |   egg_link.py
|   |       |   |   |   |   encoding.py
|   |       |   |   |   |   entrypoints.py
|   |       |   |   |   |   filesystem.py
|   |       |   |   |   |   filetypes.py
|   |       |   |   |   |   glibc.py
|   |       |   |   |   |   hashes.py
|   |       |   |   |   |   inject_securetransport.py
|   |       |   |   |   |   logging.py
|   |       |   |   |   |   misc.py
|   |       |   |   |   |   models.py
|   |       |   |   |   |   packaging.py
|   |       |   |   |   |   setuptools_build.py
|   |       |   |   |   |   subprocess.py
|   |       |   |   |   |   temp_dir.py
|   |       |   |   |   |   unpacking.py
|   |       |   |   |   |   urls.py
|   |       |   |   |   |   virtualenv.py
|   |       |   |   |   |   wheel.py
|   |       |   |   |   |   _log.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           appdirs.cpython-310.pyc
|   |       |   |   |           compat.cpython-310.pyc
|   |       |   |   |           compatibility_tags.cpython-310.pyc
|   |       |   |   |           datetime.cpython-310.pyc
|   |       |   |   |           deprecation.cpython-310.pyc
|   |       |   |   |           direct_url_helpers.cpython-310.pyc
|   |       |   |   |           distutils_args.cpython-310.pyc
|   |       |   |   |           egg_link.cpython-310.pyc
|   |       |   |   |           encoding.cpython-310.pyc
|   |       |   |   |           entrypoints.cpython-310.pyc
|   |       |   |   |           filesystem.cpython-310.pyc
|   |       |   |   |           filetypes.cpython-310.pyc
|   |       |   |   |           glibc.cpython-310.pyc
|   |       |   |   |           hashes.cpython-310.pyc
|   |       |   |   |           inject_securetransport.cpython-310.pyc
|   |       |   |   |           logging.cpython-310.pyc
|   |       |   |   |           misc.cpython-310.pyc
|   |       |   |   |           models.cpython-310.pyc
|   |       |   |   |           packaging.cpython-310.pyc
|   |       |   |   |           setuptools_build.cpython-310.pyc
|   |       |   |   |           subprocess.cpython-310.pyc
|   |       |   |   |           temp_dir.cpython-310.pyc
|   |       |   |   |           unpacking.cpython-310.pyc
|   |       |   |   |           urls.cpython-310.pyc
|   |       |   |   |           virtualenv.cpython-310.pyc
|   |       |   |   |           wheel.cpython-310.pyc
|   |       |   |   |           _log.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---vcs
|   |       |   |   |   |   bazaar.py
|   |       |   |   |   |   git.py
|   |       |   |   |   |   mercurial.py
|   |       |   |   |   |   subversion.py
|   |       |   |   |   |   versioncontrol.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           bazaar.cpython-310.pyc
|   |       |   |   |           git.cpython-310.pyc
|   |       |   |   |           mercurial.cpython-310.pyc
|   |       |   |   |           subversion.cpython-310.pyc
|   |       |   |   |           versioncontrol.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           build_env.cpython-310.pyc
|   |       |   |           cache.cpython-310.pyc
|   |       |   |           configuration.cpython-310.pyc
|   |       |   |           exceptions.cpython-310.pyc
|   |       |   |           main.cpython-310.pyc
|   |       |   |           pyproject.cpython-310.pyc
|   |       |   |           self_outdated_check.cpython-310.pyc
|   |       |   |           wheel_builder.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_vendor
|   |       |   |   |   six.py
|   |       |   |   |   typing_extensions.py
|   |       |   |   |   vendor.txt
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---cachecontrol
|   |       |   |   |   |   adapter.py
|   |       |   |   |   |   cache.py
|   |       |   |   |   |   compat.py
|   |       |   |   |   |   controller.py
|   |       |   |   |   |   filewrapper.py
|   |       |   |   |   |   heuristics.py
|   |       |   |   |   |   serialize.py
|   |       |   |   |   |   wrapper.py
|   |       |   |   |   |   _cmd.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---caches
|   |       |   |   |   |   |   file_cache.py
|   |       |   |   |   |   |   redis_cache.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           file_cache.cpython-310.pyc
|   |       |   |   |   |           redis_cache.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           adapter.cpython-310.pyc
|   |       |   |   |           cache.cpython-310.pyc
|   |       |   |   |           compat.cpython-310.pyc
|   |       |   |   |           controller.cpython-310.pyc
|   |       |   |   |           filewrapper.cpython-310.pyc
|   |       |   |   |           heuristics.cpython-310.pyc
|   |       |   |   |           serialize.cpython-310.pyc
|   |       |   |   |           wrapper.cpython-310.pyc
|   |       |   |   |           _cmd.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---certifi
|   |       |   |   |   |   cacert.pem
|   |       |   |   |   |   core.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __main__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           core.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           __main__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---chardet
|   |       |   |   |   |   big5freq.py
|   |       |   |   |   |   big5prober.py
|   |       |   |   |   |   chardistribution.py
|   |       |   |   |   |   charsetgroupprober.py
|   |       |   |   |   |   charsetprober.py
|   |       |   |   |   |   codingstatemachine.py
|   |       |   |   |   |   codingstatemachinedict.py
|   |       |   |   |   |   cp949prober.py
|   |       |   |   |   |   enums.py
|   |       |   |   |   |   escprober.py
|   |       |   |   |   |   escsm.py
|   |       |   |   |   |   eucjpprober.py
|   |       |   |   |   |   euckrfreq.py
|   |       |   |   |   |   euckrprober.py
|   |       |   |   |   |   euctwfreq.py
|   |       |   |   |   |   euctwprober.py
|   |       |   |   |   |   gb2312freq.py
|   |       |   |   |   |   gb2312prober.py
|   |       |   |   |   |   hebrewprober.py
|   |       |   |   |   |   jisfreq.py
|   |       |   |   |   |   johabfreq.py
|   |       |   |   |   |   johabprober.py
|   |       |   |   |   |   jpcntx.py
|   |       |   |   |   |   langbulgarianmodel.py
|   |       |   |   |   |   langgreekmodel.py
|   |       |   |   |   |   langhebrewmodel.py
|   |       |   |   |   |   langhungarianmodel.py
|   |       |   |   |   |   langrussianmodel.py
|   |       |   |   |   |   langthaimodel.py
|   |       |   |   |   |   langturkishmodel.py
|   |       |   |   |   |   latin1prober.py
|   |       |   |   |   |   macromanprober.py
|   |       |   |   |   |   mbcharsetprober.py
|   |       |   |   |   |   mbcsgroupprober.py
|   |       |   |   |   |   mbcssm.py
|   |       |   |   |   |   resultdict.py
|   |       |   |   |   |   sbcharsetprober.py
|   |       |   |   |   |   sbcsgroupprober.py
|   |       |   |   |   |   sjisprober.py
|   |       |   |   |   |   universaldetector.py
|   |       |   |   |   |   utf1632prober.py
|   |       |   |   |   |   utf8prober.py
|   |       |   |   |   |   version.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---cli
|   |       |   |   |   |   |   chardetect.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           chardetect.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---metadata
|   |       |   |   |   |   |   languages.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           languages.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           big5freq.cpython-310.pyc
|   |       |   |   |           big5prober.cpython-310.pyc
|   |       |   |   |           chardistribution.cpython-310.pyc
|   |       |   |   |           charsetgroupprober.cpython-310.pyc
|   |       |   |   |           charsetprober.cpython-310.pyc
|   |       |   |   |           codingstatemachine.cpython-310.pyc
|   |       |   |   |           codingstatemachinedict.cpython-310.pyc
|   |       |   |   |           cp949prober.cpython-310.pyc
|   |       |   |   |           enums.cpython-310.pyc
|   |       |   |   |           escprober.cpython-310.pyc
|   |       |   |   |           escsm.cpython-310.pyc
|   |       |   |   |           eucjpprober.cpython-310.pyc
|   |       |   |   |           euckrfreq.cpython-310.pyc
|   |       |   |   |           euckrprober.cpython-310.pyc
|   |       |   |   |           euctwfreq.cpython-310.pyc
|   |       |   |   |           euctwprober.cpython-310.pyc
|   |       |   |   |           gb2312freq.cpython-310.pyc
|   |       |   |   |           gb2312prober.cpython-310.pyc
|   |       |   |   |           hebrewprober.cpython-310.pyc
|   |       |   |   |           jisfreq.cpython-310.pyc
|   |       |   |   |           johabfreq.cpython-310.pyc
|   |       |   |   |           johabprober.cpython-310.pyc
|   |       |   |   |           jpcntx.cpython-310.pyc
|   |       |   |   |           langbulgarianmodel.cpython-310.pyc
|   |       |   |   |           langgreekmodel.cpython-310.pyc
|   |       |   |   |           langhebrewmodel.cpython-310.pyc
|   |       |   |   |           langhungarianmodel.cpython-310.pyc
|   |       |   |   |           langrussianmodel.cpython-310.pyc
|   |       |   |   |           langthaimodel.cpython-310.pyc
|   |       |   |   |           langturkishmodel.cpython-310.pyc
|   |       |   |   |           latin1prober.cpython-310.pyc
|   |       |   |   |           macromanprober.cpython-310.pyc
|   |       |   |   |           mbcharsetprober.cpython-310.pyc
|   |       |   |   |           mbcsgroupprober.cpython-310.pyc
|   |       |   |   |           mbcssm.cpython-310.pyc
|   |       |   |   |           resultdict.cpython-310.pyc
|   |       |   |   |           sbcharsetprober.cpython-310.pyc
|   |       |   |   |           sbcsgroupprober.cpython-310.pyc
|   |       |   |   |           sjisprober.cpython-310.pyc
|   |       |   |   |           universaldetector.cpython-310.pyc
|   |       |   |   |           utf1632prober.cpython-310.pyc
|   |       |   |   |           utf8prober.cpython-310.pyc
|   |       |   |   |           version.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---colorama
|   |       |   |   |   |   ansi.py
|   |       |   |   |   |   ansitowin32.py
|   |       |   |   |   |   initialise.py
|   |       |   |   |   |   win32.py
|   |       |   |   |   |   winterm.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---tests
|   |       |   |   |   |   |   ansitowin32_test.py
|   |       |   |   |   |   |   ansi_test.py
|   |       |   |   |   |   |   initialise_test.py
|   |       |   |   |   |   |   isatty_test.py
|   |       |   |   |   |   |   utils.py
|   |       |   |   |   |   |   winterm_test.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           ansitowin32_test.cpython-310.pyc
|   |       |   |   |   |           ansi_test.cpython-310.pyc
|   |       |   |   |   |           initialise_test.cpython-310.pyc
|   |       |   |   |   |           isatty_test.cpython-310.pyc
|   |       |   |   |   |           utils.cpython-310.pyc
|   |       |   |   |   |           winterm_test.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           ansi.cpython-310.pyc
|   |       |   |   |           ansitowin32.cpython-310.pyc
|   |       |   |   |           initialise.cpython-310.pyc
|   |       |   |   |           win32.cpython-310.pyc
|   |       |   |   |           winterm.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---distlib
|   |       |   |   |   |   compat.py
|   |       |   |   |   |   database.py
|   |       |   |   |   |   index.py
|   |       |   |   |   |   locators.py
|   |       |   |   |   |   manifest.py
|   |       |   |   |   |   markers.py
|   |       |   |   |   |   metadata.py
|   |       |   |   |   |   resources.py
|   |       |   |   |   |   scripts.py
|   |       |   |   |   |   t32.exe
|   |       |   |   |   |   t64-arm.exe
|   |       |   |   |   |   t64.exe
|   |       |   |   |   |   util.py
|   |       |   |   |   |   version.py
|   |       |   |   |   |   w32.exe
|   |       |   |   |   |   w64-arm.exe
|   |       |   |   |   |   w64.exe
|   |       |   |   |   |   wheel.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           compat.cpython-310.pyc
|   |       |   |   |           database.cpython-310.pyc
|   |       |   |   |           index.cpython-310.pyc
|   |       |   |   |           locators.cpython-310.pyc
|   |       |   |   |           manifest.cpython-310.pyc
|   |       |   |   |           markers.cpython-310.pyc
|   |       |   |   |           metadata.cpython-310.pyc
|   |       |   |   |           resources.cpython-310.pyc
|   |       |   |   |           scripts.cpython-310.pyc
|   |       |   |   |           util.cpython-310.pyc
|   |       |   |   |           version.cpython-310.pyc
|   |       |   |   |           wheel.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---distro
|   |       |   |   |   |   distro.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __main__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           distro.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           __main__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---idna
|   |       |   |   |   |   codec.py
|   |       |   |   |   |   compat.py
|   |       |   |   |   |   core.py
|   |       |   |   |   |   idnadata.py
|   |       |   |   |   |   intranges.py
|   |       |   |   |   |   package_data.py
|   |       |   |   |   |   uts46data.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           codec.cpython-310.pyc
|   |       |   |   |           compat.cpython-310.pyc
|   |       |   |   |           core.cpython-310.pyc
|   |       |   |   |           idnadata.cpython-310.pyc
|   |       |   |   |           intranges.cpython-310.pyc
|   |       |   |   |           package_data.cpython-310.pyc
|   |       |   |   |           uts46data.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---msgpack
|   |       |   |   |   |   exceptions.py
|   |       |   |   |   |   ext.py
|   |       |   |   |   |   fallback.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           exceptions.cpython-310.pyc
|   |       |   |   |           ext.cpython-310.pyc
|   |       |   |   |           fallback.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---packaging
|   |       |   |   |   |   markers.py
|   |       |   |   |   |   requirements.py
|   |       |   |   |   |   specifiers.py
|   |       |   |   |   |   tags.py
|   |       |   |   |   |   utils.py
|   |       |   |   |   |   version.py
|   |       |   |   |   |   _manylinux.py
|   |       |   |   |   |   _musllinux.py
|   |       |   |   |   |   _structures.py
|   |       |   |   |   |   __about__.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           markers.cpython-310.pyc
|   |       |   |   |           requirements.cpython-310.pyc
|   |       |   |   |           specifiers.cpython-310.pyc
|   |       |   |   |           tags.cpython-310.pyc
|   |       |   |   |           utils.cpython-310.pyc
|   |       |   |   |           version.cpython-310.pyc
|   |       |   |   |           _manylinux.cpython-310.pyc
|   |       |   |   |           _musllinux.cpython-310.pyc
|   |       |   |   |           _structures.cpython-310.pyc
|   |       |   |   |           __about__.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---pkg_resources
|   |       |   |   |   |   py31compat.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           py31compat.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---platformdirs
|   |       |   |   |   |   android.py
|   |       |   |   |   |   api.py
|   |       |   |   |   |   macos.py
|   |       |   |   |   |   unix.py
|   |       |   |   |   |   version.py
|   |       |   |   |   |   windows.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __main__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           android.cpython-310.pyc
|   |       |   |   |           api.cpython-310.pyc
|   |       |   |   |           macos.cpython-310.pyc
|   |       |   |   |           unix.cpython-310.pyc
|   |       |   |   |           version.cpython-310.pyc
|   |       |   |   |           windows.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           __main__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---pygments
|   |       |   |   |   |   cmdline.py
|   |       |   |   |   |   console.py
|   |       |   |   |   |   filter.py
|   |       |   |   |   |   formatter.py
|   |       |   |   |   |   lexer.py
|   |       |   |   |   |   modeline.py
|   |       |   |   |   |   plugin.py
|   |       |   |   |   |   regexopt.py
|   |       |   |   |   |   scanner.py
|   |       |   |   |   |   sphinxext.py
|   |       |   |   |   |   style.py
|   |       |   |   |   |   token.py
|   |       |   |   |   |   unistring.py
|   |       |   |   |   |   util.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __main__.py
|   |       |   |   |   |   
|   |       |   |   |   +---filters
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---formatters
|   |       |   |   |   |   |   bbcode.py
|   |       |   |   |   |   |   groff.py
|   |       |   |   |   |   |   html.py
|   |       |   |   |   |   |   img.py
|   |       |   |   |   |   |   irc.py
|   |       |   |   |   |   |   latex.py
|   |       |   |   |   |   |   other.py
|   |       |   |   |   |   |   pangomarkup.py
|   |       |   |   |   |   |   rtf.py
|   |       |   |   |   |   |   svg.py
|   |       |   |   |   |   |   terminal.py
|   |       |   |   |   |   |   terminal256.py
|   |       |   |   |   |   |   _mapping.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           bbcode.cpython-310.pyc
|   |       |   |   |   |           groff.cpython-310.pyc
|   |       |   |   |   |           html.cpython-310.pyc
|   |       |   |   |   |           img.cpython-310.pyc
|   |       |   |   |   |           irc.cpython-310.pyc
|   |       |   |   |   |           latex.cpython-310.pyc
|   |       |   |   |   |           other.cpython-310.pyc
|   |       |   |   |   |           pangomarkup.cpython-310.pyc
|   |       |   |   |   |           rtf.cpython-310.pyc
|   |       |   |   |   |           svg.cpython-310.pyc
|   |       |   |   |   |           terminal.cpython-310.pyc
|   |       |   |   |   |           terminal256.cpython-310.pyc
|   |       |   |   |   |           _mapping.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---lexers
|   |       |   |   |   |   |   python.py
|   |       |   |   |   |   |   _mapping.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           python.cpython-310.pyc
|   |       |   |   |   |           _mapping.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---styles
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           cmdline.cpython-310.pyc
|   |       |   |   |           console.cpython-310.pyc
|   |       |   |   |           filter.cpython-310.pyc
|   |       |   |   |           formatter.cpython-310.pyc
|   |       |   |   |           lexer.cpython-310.pyc
|   |       |   |   |           modeline.cpython-310.pyc
|   |       |   |   |           plugin.cpython-310.pyc
|   |       |   |   |           regexopt.cpython-310.pyc
|   |       |   |   |           scanner.cpython-310.pyc
|   |       |   |   |           sphinxext.cpython-310.pyc
|   |       |   |   |           style.cpython-310.pyc
|   |       |   |   |           token.cpython-310.pyc
|   |       |   |   |           unistring.cpython-310.pyc
|   |       |   |   |           util.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           __main__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---pyparsing
|   |       |   |   |   |   actions.py
|   |       |   |   |   |   common.py
|   |       |   |   |   |   core.py
|   |       |   |   |   |   exceptions.py
|   |       |   |   |   |   helpers.py
|   |       |   |   |   |   results.py
|   |       |   |   |   |   testing.py
|   |       |   |   |   |   unicode.py
|   |       |   |   |   |   util.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---diagram
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           actions.cpython-310.pyc
|   |       |   |   |           common.cpython-310.pyc
|   |       |   |   |           core.cpython-310.pyc
|   |       |   |   |           exceptions.cpython-310.pyc
|   |       |   |   |           helpers.cpython-310.pyc
|   |       |   |   |           results.cpython-310.pyc
|   |       |   |   |           testing.cpython-310.pyc
|   |       |   |   |           unicode.cpython-310.pyc
|   |       |   |   |           util.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---pyproject_hooks
|   |       |   |   |   |   _compat.py
|   |       |   |   |   |   _impl.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---_in_process
|   |       |   |   |   |   |   _in_process.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           _in_process.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _compat.cpython-310.pyc
|   |       |   |   |           _impl.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---requests
|   |       |   |   |   |   adapters.py
|   |       |   |   |   |   api.py
|   |       |   |   |   |   auth.py
|   |       |   |   |   |   certs.py
|   |       |   |   |   |   compat.py
|   |       |   |   |   |   cookies.py
|   |       |   |   |   |   exceptions.py
|   |       |   |   |   |   help.py
|   |       |   |   |   |   hooks.py
|   |       |   |   |   |   models.py
|   |       |   |   |   |   packages.py
|   |       |   |   |   |   sessions.py
|   |       |   |   |   |   status_codes.py
|   |       |   |   |   |   structures.py
|   |       |   |   |   |   utils.py
|   |       |   |   |   |   _internal_utils.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __version__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           adapters.cpython-310.pyc
|   |       |   |   |           api.cpython-310.pyc
|   |       |   |   |           auth.cpython-310.pyc
|   |       |   |   |           certs.cpython-310.pyc
|   |       |   |   |           compat.cpython-310.pyc
|   |       |   |   |           cookies.cpython-310.pyc
|   |       |   |   |           exceptions.cpython-310.pyc
|   |       |   |   |           help.cpython-310.pyc
|   |       |   |   |           hooks.cpython-310.pyc
|   |       |   |   |           models.cpython-310.pyc
|   |       |   |   |           packages.cpython-310.pyc
|   |       |   |   |           sessions.cpython-310.pyc
|   |       |   |   |           status_codes.cpython-310.pyc
|   |       |   |   |           structures.cpython-310.pyc
|   |       |   |   |           utils.cpython-310.pyc
|   |       |   |   |           _internal_utils.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           __version__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---resolvelib
|   |       |   |   |   |   providers.py
|   |       |   |   |   |   reporters.py
|   |       |   |   |   |   resolvers.py
|   |       |   |   |   |   structs.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---compat
|   |       |   |   |   |   |   collections_abc.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           collections_abc.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           providers.cpython-310.pyc
|   |       |   |   |           reporters.cpython-310.pyc
|   |       |   |   |           resolvers.cpython-310.pyc
|   |       |   |   |           structs.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---rich
|   |       |   |   |   |   abc.py
|   |       |   |   |   |   align.py
|   |       |   |   |   |   ansi.py
|   |       |   |   |   |   bar.py
|   |       |   |   |   |   box.py
|   |       |   |   |   |   cells.py
|   |       |   |   |   |   color.py
|   |       |   |   |   |   color_triplet.py
|   |       |   |   |   |   columns.py
|   |       |   |   |   |   console.py
|   |       |   |   |   |   constrain.py
|   |       |   |   |   |   containers.py
|   |       |   |   |   |   control.py
|   |       |   |   |   |   default_styles.py
|   |       |   |   |   |   diagnose.py
|   |       |   |   |   |   emoji.py
|   |       |   |   |   |   errors.py
|   |       |   |   |   |   filesize.py
|   |       |   |   |   |   file_proxy.py
|   |       |   |   |   |   highlighter.py
|   |       |   |   |   |   json.py
|   |       |   |   |   |   jupyter.py
|   |       |   |   |   |   layout.py
|   |       |   |   |   |   live.py
|   |       |   |   |   |   live_render.py
|   |       |   |   |   |   logging.py
|   |       |   |   |   |   markup.py
|   |       |   |   |   |   measure.py
|   |       |   |   |   |   padding.py
|   |       |   |   |   |   pager.py
|   |       |   |   |   |   palette.py
|   |       |   |   |   |   panel.py
|   |       |   |   |   |   pretty.py
|   |       |   |   |   |   progress.py
|   |       |   |   |   |   progress_bar.py
|   |       |   |   |   |   prompt.py
|   |       |   |   |   |   protocol.py
|   |       |   |   |   |   region.py
|   |       |   |   |   |   repr.py
|   |       |   |   |   |   rule.py
|   |       |   |   |   |   scope.py
|   |       |   |   |   |   screen.py
|   |       |   |   |   |   segment.py
|   |       |   |   |   |   spinner.py
|   |       |   |   |   |   status.py
|   |       |   |   |   |   style.py
|   |       |   |   |   |   styled.py
|   |       |   |   |   |   syntax.py
|   |       |   |   |   |   table.py
|   |       |   |   |   |   terminal_theme.py
|   |       |   |   |   |   text.py
|   |       |   |   |   |   theme.py
|   |       |   |   |   |   themes.py
|   |       |   |   |   |   traceback.py
|   |       |   |   |   |   tree.py
|   |       |   |   |   |   _cell_widths.py
|   |       |   |   |   |   _emoji_codes.py
|   |       |   |   |   |   _emoji_replace.py
|   |       |   |   |   |   _export_format.py
|   |       |   |   |   |   _extension.py
|   |       |   |   |   |   _inspect.py
|   |       |   |   |   |   _log_render.py
|   |       |   |   |   |   _loop.py
|   |       |   |   |   |   _null_file.py
|   |       |   |   |   |   _palettes.py
|   |       |   |   |   |   _pick.py
|   |       |   |   |   |   _ratio.py
|   |       |   |   |   |   _spinners.py
|   |       |   |   |   |   _stack.py
|   |       |   |   |   |   _timer.py
|   |       |   |   |   |   _win32_console.py
|   |       |   |   |   |   _windows.py
|   |       |   |   |   |   _windows_renderer.py
|   |       |   |   |   |   _wrap.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __main__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           abc.cpython-310.pyc
|   |       |   |   |           align.cpython-310.pyc
|   |       |   |   |           ansi.cpython-310.pyc
|   |       |   |   |           bar.cpython-310.pyc
|   |       |   |   |           box.cpython-310.pyc
|   |       |   |   |           cells.cpython-310.pyc
|   |       |   |   |           color.cpython-310.pyc
|   |       |   |   |           color_triplet.cpython-310.pyc
|   |       |   |   |           columns.cpython-310.pyc
|   |       |   |   |           console.cpython-310.pyc
|   |       |   |   |           constrain.cpython-310.pyc
|   |       |   |   |           containers.cpython-310.pyc
|   |       |   |   |           control.cpython-310.pyc
|   |       |   |   |           default_styles.cpython-310.pyc
|   |       |   |   |           diagnose.cpython-310.pyc
|   |       |   |   |           emoji.cpython-310.pyc
|   |       |   |   |           errors.cpython-310.pyc
|   |       |   |   |           filesize.cpython-310.pyc
|   |       |   |   |           file_proxy.cpython-310.pyc
|   |       |   |   |           highlighter.cpython-310.pyc
|   |       |   |   |           json.cpython-310.pyc
|   |       |   |   |           jupyter.cpython-310.pyc
|   |       |   |   |           layout.cpython-310.pyc
|   |       |   |   |           live.cpython-310.pyc
|   |       |   |   |           live_render.cpython-310.pyc
|   |       |   |   |           logging.cpython-310.pyc
|   |       |   |   |           markup.cpython-310.pyc
|   |       |   |   |           measure.cpython-310.pyc
|   |       |   |   |           padding.cpython-310.pyc
|   |       |   |   |           pager.cpython-310.pyc
|   |       |   |   |           palette.cpython-310.pyc
|   |       |   |   |           panel.cpython-310.pyc
|   |       |   |   |           pretty.cpython-310.pyc
|   |       |   |   |           progress.cpython-310.pyc
|   |       |   |   |           progress_bar.cpython-310.pyc
|   |       |   |   |           prompt.cpython-310.pyc
|   |       |   |   |           protocol.cpython-310.pyc
|   |       |   |   |           region.cpython-310.pyc
|   |       |   |   |           repr.cpython-310.pyc
|   |       |   |   |           rule.cpython-310.pyc
|   |       |   |   |           scope.cpython-310.pyc
|   |       |   |   |           screen.cpython-310.pyc
|   |       |   |   |           segment.cpython-310.pyc
|   |       |   |   |           spinner.cpython-310.pyc
|   |       |   |   |           status.cpython-310.pyc
|   |       |   |   |           style.cpython-310.pyc
|   |       |   |   |           styled.cpython-310.pyc
|   |       |   |   |           syntax.cpython-310.pyc
|   |       |   |   |           table.cpython-310.pyc
|   |       |   |   |           terminal_theme.cpython-310.pyc
|   |       |   |   |           text.cpython-310.pyc
|   |       |   |   |           theme.cpython-310.pyc
|   |       |   |   |           themes.cpython-310.pyc
|   |       |   |   |           traceback.cpython-310.pyc
|   |       |   |   |           tree.cpython-310.pyc
|   |       |   |   |           _cell_widths.cpython-310.pyc
|   |       |   |   |           _emoji_codes.cpython-310.pyc
|   |       |   |   |           _emoji_replace.cpython-310.pyc
|   |       |   |   |           _export_format.cpython-310.pyc
|   |       |   |   |           _extension.cpython-310.pyc
|   |       |   |   |           _inspect.cpython-310.pyc
|   |       |   |   |           _log_render.cpython-310.pyc
|   |       |   |   |           _loop.cpython-310.pyc
|   |       |   |   |           _null_file.cpython-310.pyc
|   |       |   |   |           _palettes.cpython-310.pyc
|   |       |   |   |           _pick.cpython-310.pyc
|   |       |   |   |           _ratio.cpython-310.pyc
|   |       |   |   |           _spinners.cpython-310.pyc
|   |       |   |   |           _stack.cpython-310.pyc
|   |       |   |   |           _timer.cpython-310.pyc
|   |       |   |   |           _win32_console.cpython-310.pyc
|   |       |   |   |           _windows.cpython-310.pyc
|   |       |   |   |           _windows_renderer.cpython-310.pyc
|   |       |   |   |           _wrap.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           __main__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---tenacity
|   |       |   |   |   |   after.py
|   |       |   |   |   |   before.py
|   |       |   |   |   |   before_sleep.py
|   |       |   |   |   |   nap.py
|   |       |   |   |   |   retry.py
|   |       |   |   |   |   stop.py
|   |       |   |   |   |   tornadoweb.py
|   |       |   |   |   |   wait.py
|   |       |   |   |   |   _asyncio.py
|   |       |   |   |   |   _utils.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           after.cpython-310.pyc
|   |       |   |   |           before.cpython-310.pyc
|   |       |   |   |           before_sleep.cpython-310.pyc
|   |       |   |   |           nap.cpython-310.pyc
|   |       |   |   |           retry.cpython-310.pyc
|   |       |   |   |           stop.cpython-310.pyc
|   |       |   |   |           tornadoweb.cpython-310.pyc
|   |       |   |   |           wait.cpython-310.pyc
|   |       |   |   |           _asyncio.cpython-310.pyc
|   |       |   |   |           _utils.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---tomli
|   |       |   |   |   |   _parser.py
|   |       |   |   |   |   _re.py
|   |       |   |   |   |   _types.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _parser.cpython-310.pyc
|   |       |   |   |           _re.cpython-310.pyc
|   |       |   |   |           _types.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---urllib3
|   |       |   |   |   |   connection.py
|   |       |   |   |   |   connectionpool.py
|   |       |   |   |   |   exceptions.py
|   |       |   |   |   |   fields.py
|   |       |   |   |   |   filepost.py
|   |       |   |   |   |   poolmanager.py
|   |       |   |   |   |   request.py
|   |       |   |   |   |   response.py
|   |       |   |   |   |   _collections.py
|   |       |   |   |   |   _version.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---contrib
|   |       |   |   |   |   |   appengine.py
|   |       |   |   |   |   |   ntlmpool.py
|   |       |   |   |   |   |   pyopenssl.py
|   |       |   |   |   |   |   securetransport.py
|   |       |   |   |   |   |   socks.py
|   |       |   |   |   |   |   _appengine_environ.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---_securetransport
|   |       |   |   |   |   |   |   bindings.py
|   |       |   |   |   |   |   |   low_level.py
|   |       |   |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           bindings.cpython-310.pyc
|   |       |   |   |   |   |           low_level.cpython-310.pyc
|   |       |   |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           appengine.cpython-310.pyc
|   |       |   |   |   |           ntlmpool.cpython-310.pyc
|   |       |   |   |   |           pyopenssl.cpython-310.pyc
|   |       |   |   |   |           securetransport.cpython-310.pyc
|   |       |   |   |   |           socks.cpython-310.pyc
|   |       |   |   |   |           _appengine_environ.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---packages
|   |       |   |   |   |   |   six.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---backports
|   |       |   |   |   |   |   |   makefile.py
|   |       |   |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           makefile.cpython-310.pyc
|   |       |   |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           six.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---util
|   |       |   |   |   |   |   connection.py
|   |       |   |   |   |   |   proxy.py
|   |       |   |   |   |   |   queue.py
|   |       |   |   |   |   |   request.py
|   |       |   |   |   |   |   response.py
|   |       |   |   |   |   |   retry.py
|   |       |   |   |   |   |   ssltransport.py
|   |       |   |   |   |   |   ssl_.py
|   |       |   |   |   |   |   ssl_match_hostname.py
|   |       |   |   |   |   |   timeout.py
|   |       |   |   |   |   |   url.py
|   |       |   |   |   |   |   wait.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           connection.cpython-310.pyc
|   |       |   |   |   |           proxy.cpython-310.pyc
|   |       |   |   |   |           queue.cpython-310.pyc
|   |       |   |   |   |           request.cpython-310.pyc
|   |       |   |   |   |           response.cpython-310.pyc
|   |       |   |   |   |           retry.cpython-310.pyc
|   |       |   |   |   |           ssltransport.cpython-310.pyc
|   |       |   |   |   |           ssl_.cpython-310.pyc
|   |       |   |   |   |           ssl_match_hostname.cpython-310.pyc
|   |       |   |   |   |           timeout.cpython-310.pyc
|   |       |   |   |   |           url.cpython-310.pyc
|   |       |   |   |   |           wait.cpython-310.pyc
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           connection.cpython-310.pyc
|   |       |   |   |           connectionpool.cpython-310.pyc
|   |       |   |   |           exceptions.cpython-310.pyc
|   |       |   |   |           fields.cpython-310.pyc
|   |       |   |   |           filepost.cpython-310.pyc
|   |       |   |   |           poolmanager.cpython-310.pyc
|   |       |   |   |           request.cpython-310.pyc
|   |       |   |   |           response.cpython-310.pyc
|   |       |   |   |           _collections.cpython-310.pyc
|   |       |   |   |           _version.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---webencodings
|   |       |   |   |   |   labels.py
|   |       |   |   |   |   mklabels.py
|   |       |   |   |   |   tests.py
|   |       |   |   |   |   x_user_defined.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           labels.cpython-310.pyc
|   |       |   |   |           mklabels.cpython-310.pyc
|   |       |   |   |           tests.cpython-310.pyc
|   |       |   |   |           x_user_defined.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           six.cpython-310.pyc
|   |       |   |           typing_extensions.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           __init__.cpython-310.pyc
|   |       |           __main__.cpython-310.pyc
|   |       |           __pip-runner__.cpython-310.pyc
|   |       |           
|   |       +---pip-23.0.1.dist-info
|   |       |       entry_points.txt
|   |       |       INSTALLER
|   |       |       LICENSE.txt
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       top_level.txt
|   |       |       WHEEL
|   |       |       
|   |       +---pkg_resources
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---extern
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_vendor
|   |       |   |   |   appdirs.py
|   |       |   |   |   zipp.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---importlib_resources
|   |       |   |   |   |   abc.py
|   |       |   |   |   |   readers.py
|   |       |   |   |   |   simple.py
|   |       |   |   |   |   _adapters.py
|   |       |   |   |   |   _common.py
|   |       |   |   |   |   _compat.py
|   |       |   |   |   |   _itertools.py
|   |       |   |   |   |   _legacy.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           abc.cpython-310.pyc
|   |       |   |   |           readers.cpython-310.pyc
|   |       |   |   |           simple.cpython-310.pyc
|   |       |   |   |           _adapters.cpython-310.pyc
|   |       |   |   |           _common.cpython-310.pyc
|   |       |   |   |           _compat.cpython-310.pyc
|   |       |   |   |           _itertools.cpython-310.pyc
|   |       |   |   |           _legacy.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---jaraco
|   |       |   |   |   |   context.py
|   |       |   |   |   |   functools.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---text
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           context.cpython-310.pyc
|   |       |   |   |           functools.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---more_itertools
|   |       |   |   |   |   more.py
|   |       |   |   |   |   recipes.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           more.cpython-310.pyc
|   |       |   |   |           recipes.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---packaging
|   |       |   |   |   |   markers.py
|   |       |   |   |   |   requirements.py
|   |       |   |   |   |   specifiers.py
|   |       |   |   |   |   tags.py
|   |       |   |   |   |   utils.py
|   |       |   |   |   |   version.py
|   |       |   |   |   |   _manylinux.py
|   |       |   |   |   |   _musllinux.py
|   |       |   |   |   |   _structures.py
|   |       |   |   |   |   __about__.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           markers.cpython-310.pyc
|   |       |   |   |           requirements.cpython-310.pyc
|   |       |   |   |           specifiers.cpython-310.pyc
|   |       |   |   |           tags.cpython-310.pyc
|   |       |   |   |           utils.cpython-310.pyc
|   |       |   |   |           version.cpython-310.pyc
|   |       |   |   |           _manylinux.cpython-310.pyc
|   |       |   |   |           _musllinux.cpython-310.pyc
|   |       |   |   |           _structures.cpython-310.pyc
|   |       |   |   |           __about__.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---pyparsing
|   |       |   |   |   |   actions.py
|   |       |   |   |   |   common.py
|   |       |   |   |   |   core.py
|   |       |   |   |   |   exceptions.py
|   |       |   |   |   |   helpers.py
|   |       |   |   |   |   results.py
|   |       |   |   |   |   testing.py
|   |       |   |   |   |   unicode.py
|   |       |   |   |   |   util.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---diagram
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           actions.cpython-310.pyc
|   |       |   |   |           common.cpython-310.pyc
|   |       |   |   |           core.cpython-310.pyc
|   |       |   |   |           exceptions.cpython-310.pyc
|   |       |   |   |           helpers.cpython-310.pyc
|   |       |   |   |           results.cpython-310.pyc
|   |       |   |   |           testing.cpython-310.pyc
|   |       |   |   |           unicode.cpython-310.pyc
|   |       |   |   |           util.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           appdirs.cpython-310.pyc
|   |       |   |           zipp.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---playwright
|   |       |   |   py.typed
|   |       |   |   _repo_version.py
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   +---async_api
|   |       |   |   |   _context_manager.py
|   |       |   |   |   _generated.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _context_manager.cpython-310.pyc
|   |       |   |           _generated.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---driver
|   |       |   |   |   LICENSE
|   |       |   |   |   node.exe
|   |       |   |   |   README.md
|   |       |   |   |   
|   |       |   |   \---package
|   |       |   |       |   api.json
|   |       |   |       |   browsers.json
|   |       |   |       |   cli.js
|   |       |   |       |   index.d.ts
|   |       |   |       |   index.js
|   |       |   |       |   index.mjs
|   |       |   |       |   LICENSE
|   |       |   |       |   NOTICE
|   |       |   |       |   package.json
|   |       |   |       |   protocol.yml
|   |       |   |       |   README.md
|   |       |   |       |   ThirdPartyNotices.txt
|   |       |   |       |   
|   |       |   |       +---bin
|   |       |   |       |       install_media_pack.ps1
|   |       |   |       |       install_webkit_wsl.ps1
|   |       |   |       |       reinstall_chrome_beta_linux.sh
|   |       |   |       |       reinstall_chrome_beta_mac.sh
|   |       |   |       |       reinstall_chrome_beta_win.ps1
|   |       |   |       |       reinstall_chrome_stable_linux.sh
|   |       |   |       |       reinstall_chrome_stable_mac.sh
|   |       |   |       |       reinstall_chrome_stable_win.ps1
|   |       |   |       |       reinstall_msedge_beta_linux.sh
|   |       |   |       |       reinstall_msedge_beta_mac.sh
|   |       |   |       |       reinstall_msedge_beta_win.ps1
|   |       |   |       |       reinstall_msedge_dev_linux.sh
|   |       |   |       |       reinstall_msedge_dev_mac.sh
|   |       |   |       |       reinstall_msedge_dev_win.ps1
|   |       |   |       |       reinstall_msedge_stable_linux.sh
|   |       |   |       |       reinstall_msedge_stable_mac.sh
|   |       |   |       |       reinstall_msedge_stable_win.ps1
|   |       |   |       |       
|   |       |   |       +---lib
|   |       |   |       |   |   androidServerImpl.js
|   |       |   |       |   |   browserServerImpl.js
|   |       |   |       |   |   inprocess.js
|   |       |   |       |   |   inProcessFactory.js
|   |       |   |       |   |   mcpBundle.js
|   |       |   |       |   |   outofprocess.js
|   |       |   |       |   |   utils.js
|   |       |   |       |   |   utilsBundle.js
|   |       |   |       |   |   zipBundle.js
|   |       |   |       |   |   zipBundleImpl.js
|   |       |   |       |   |   
|   |       |   |       |   +---cli
|   |       |   |       |   |       driver.js
|   |       |   |       |   |       program.js
|   |       |   |       |   |       programWithTestStub.js
|   |       |   |       |   |       
|   |       |   |       |   +---client
|   |       |   |       |   |       android.js
|   |       |   |       |   |       api.js
|   |       |   |       |   |       artifact.js
|   |       |   |       |   |       browser.js
|   |       |   |       |   |       browserContext.js
|   |       |   |       |   |       browserType.js
|   |       |   |       |   |       cdpSession.js
|   |       |   |       |   |       channelOwner.js
|   |       |   |       |   |       clientHelper.js
|   |       |   |       |   |       clientInstrumentation.js
|   |       |   |       |   |       clientStackTrace.js
|   |       |   |       |   |       clock.js
|   |       |   |       |   |       connection.js
|   |       |   |       |   |       consoleMessage.js
|   |       |   |       |   |       coverage.js
|   |       |   |       |   |       dialog.js
|   |       |   |       |   |       download.js
|   |       |   |       |   |       electron.js
|   |       |   |       |   |       elementHandle.js
|   |       |   |       |   |       errors.js
|   |       |   |       |   |       eventEmitter.js
|   |       |   |       |   |       events.js
|   |       |   |       |   |       fetch.js
|   |       |   |       |   |       fileChooser.js
|   |       |   |       |   |       fileUtils.js
|   |       |   |       |   |       frame.js
|   |       |   |       |   |       harRouter.js
|   |       |   |       |   |       input.js
|   |       |   |       |   |       jsHandle.js
|   |       |   |       |   |       jsonPipe.js
|   |       |   |       |   |       localUtils.js
|   |       |   |       |   |       locator.js
|   |       |   |       |   |       network.js
|   |       |   |       |   |       page.js
|   |       |   |       |   |       pageAgent.js
|   |       |   |       |   |       platform.js
|   |       |   |       |   |       playwright.js
|   |       |   |       |   |       selectors.js
|   |       |   |       |   |       stream.js
|   |       |   |       |   |       timeoutSettings.js
|   |       |   |       |   |       tracing.js
|   |       |   |       |   |       types.js
|   |       |   |       |   |       video.js
|   |       |   |       |   |       waiter.js
|   |       |   |       |   |       webError.js
|   |       |   |       |   |       webSocket.js
|   |       |   |       |   |       worker.js
|   |       |   |       |   |       writableStream.js
|   |       |   |       |   |       
|   |       |   |       |   +---generated
|   |       |   |       |   |       bindingsControllerSource.js
|   |       |   |       |   |       clockSource.js
|   |       |   |       |   |       injectedScriptSource.js
|   |       |   |       |   |       pollingRecorderSource.js
|   |       |   |       |   |       storageScriptSource.js
|   |       |   |       |   |       utilityScriptSource.js
|   |       |   |       |   |       webSocketMockSource.js
|   |       |   |       |   |       
|   |       |   |       |   +---mcpBundleImpl
|   |       |   |       |   |       index.js
|   |       |   |       |   |       
|   |       |   |       |   +---protocol
|   |       |   |       |   |       serializers.js
|   |       |   |       |   |       validator.js
|   |       |   |       |   |       validatorPrimitives.js
|   |       |   |       |   |       
|   |       |   |       |   +---remote
|   |       |   |       |   |       playwrightConnection.js
|   |       |   |       |   |       playwrightServer.js
|   |       |   |       |   |       
|   |       |   |       |   +---server
|   |       |   |       |   |   |   artifact.js
|   |       |   |       |   |   |   browser.js
|   |       |   |       |   |   |   browserContext.js
|   |       |   |       |   |   |   browserType.js
|   |       |   |       |   |   |   callLog.js
|   |       |   |       |   |   |   clock.js
|   |       |   |       |   |   |   console.js
|   |       |   |       |   |   |   cookieStore.js
|   |       |   |       |   |   |   debugController.js
|   |       |   |       |   |   |   debugger.js
|   |       |   |       |   |   |   deviceDescriptors.js
|   |       |   |       |   |   |   deviceDescriptorsSource.json
|   |       |   |       |   |   |   dialog.js
|   |       |   |       |   |   |   dom.js
|   |       |   |       |   |   |   download.js
|   |       |   |       |   |   |   errors.js
|   |       |   |       |   |   |   fetch.js
|   |       |   |       |   |   |   fileChooser.js
|   |       |   |       |   |   |   fileUploadUtils.js
|   |       |   |       |   |   |   formData.js
|   |       |   |       |   |   |   frames.js
|   |       |   |       |   |   |   frameSelectors.js
|   |       |   |       |   |   |   harBackend.js
|   |       |   |       |   |   |   helper.js
|   |       |   |       |   |   |   index.js
|   |       |   |       |   |   |   input.js
|   |       |   |       |   |   |   instrumentation.js
|   |       |   |       |   |   |   javascript.js
|   |       |   |       |   |   |   launchApp.js
|   |       |   |       |   |   |   localUtils.js
|   |       |   |       |   |   |   macEditingCommands.js
|   |       |   |       |   |   |   network.js
|   |       |   |       |   |   |   page.js
|   |       |   |       |   |   |   pipeTransport.js
|   |       |   |       |   |   |   playwright.js
|   |       |   |       |   |   |   progress.js
|   |       |   |       |   |   |   protocolError.js
|   |       |   |       |   |   |   recorder.js
|   |       |   |       |   |   |   screencast.js
|   |       |   |       |   |   |   screenshotter.js
|   |       |   |       |   |   |   selectors.js
|   |       |   |       |   |   |   socksClientCertificatesInterceptor.js
|   |       |   |       |   |   |   socksInterceptor.js
|   |       |   |       |   |   |   transport.js
|   |       |   |       |   |   |   types.js
|   |       |   |       |   |   |   usKeyboardLayout.js
|   |       |   |       |   |   |   videoRecorder.js
|   |       |   |       |   |   |   
|   |       |   |       |   |   +---agent
|   |       |   |       |   |   |       actionRunner.js
|   |       |   |       |   |   |       actions.js
|   |       |   |       |   |   |       codegen.js
|   |       |   |       |   |   |       context.js
|   |       |   |       |   |   |       expectTools.js
|   |       |   |       |   |   |       pageAgent.js
|   |       |   |       |   |   |       performTools.js
|   |       |   |       |   |   |       tool.js
|   |       |   |       |   |   |       
|   |       |   |       |   |   +---android
|   |       |   |       |   |   |       android.js
|   |       |   |       |   |   |       backendAdb.js
|   |       |   |       |   |   |       
|   |       |   |       |   |   +---bidi
|   |       |   |       |   |   |   |   bidiBrowser.js
|   |       |   |       |   |   |   |   bidiChromium.js
|   |       |   |       |   |   |   |   bidiConnection.js
|   |       |   |       |   |   |   |   bidiDeserializer.js
|   |       |   |       |   |   |   |   bidiExecutionContext.js
|   |       |   |       |   |   |   |   bidiFirefox.js
|   |       |   |       |   |   |   |   bidiInput.js
|   |       |   |       |   |   |   |   bidiNetworkManager.js
|   |       |   |       |   |   |   |   bidiOverCdp.js
|   |       |   |       |   |   |   |   bidiPage.js
|   |       |   |       |   |   |   |   bidiPdf.js
|   |       |   |       |   |   |   |   
|   |       |   |       |   |   |   \---third_party
|   |       |   |       |   |   |           bidiCommands.d.js
|   |       |   |       |   |   |           bidiKeyboard.js
|   |       |   |       |   |   |           bidiProtocol.js
|   |       |   |       |   |   |           bidiProtocolCore.js
|   |       |   |       |   |   |           bidiProtocolPermissions.js
|   |       |   |       |   |   |           bidiSerializer.js
|   |       |   |       |   |   |           firefoxPrefs.js
|   |       |   |       |   |   |           
|   |       |   |       |   |   +---chromium
|   |       |   |       |   |   |       appIcon.png
|   |       |   |       |   |   |       chromium.js
|   |       |   |       |   |   |       chromiumSwitches.js
|   |       |   |       |   |   |       crBrowser.js
|   |       |   |       |   |   |       crConnection.js
|   |       |   |       |   |   |       crCoverage.js
|   |       |   |       |   |   |       crDevTools.js
|   |       |   |       |   |   |       crDragDrop.js
|   |       |   |       |   |   |       crExecutionContext.js
|   |       |   |       |   |   |       crInput.js
|   |       |   |       |   |   |       crNetworkManager.js
|   |       |   |       |   |   |       crPage.js
|   |       |   |       |   |   |       crPdf.js
|   |       |   |       |   |   |       crProtocolHelper.js
|   |       |   |       |   |   |       crServiceWorker.js
|   |       |   |       |   |   |       defaultFontFamilies.js
|   |       |   |       |   |   |       protocol.d.js
|   |       |   |       |   |   |       
|   |       |   |       |   |   +---codegen
|   |       |   |       |   |   |       csharp.js
|   |       |   |       |   |   |       java.js
|   |       |   |       |   |   |       javascript.js
|   |       |   |       |   |   |       jsonl.js
|   |       |   |       |   |   |       language.js
|   |       |   |       |   |   |       languages.js
|   |       |   |       |   |   |       python.js
|   |       |   |       |   |   |       types.js
|   |       |   |       |   |   |       
|   |       |   |       |   |   +---dispatchers
|   |       |   |       |   |   |       androidDispatcher.js
|   |       |   |       |   |   |       artifactDispatcher.js
|   |       |   |       |   |   |       browserContextDispatcher.js
|   |       |   |       |   |   |       browserDispatcher.js
|   |       |   |       |   |   |       browserTypeDispatcher.js
|   |       |   |       |   |   |       cdpSessionDispatcher.js
|   |       |   |       |   |   |       debugControllerDispatcher.js
|   |       |   |       |   |   |       dialogDispatcher.js
|   |       |   |       |   |   |       dispatcher.js
|   |       |   |       |   |   |       electronDispatcher.js
|   |       |   |       |   |   |       elementHandlerDispatcher.js
|   |       |   |       |   |   |       frameDispatcher.js
|   |       |   |       |   |   |       jsHandleDispatcher.js
|   |       |   |       |   |   |       jsonPipeDispatcher.js
|   |       |   |       |   |   |       localUtilsDispatcher.js
|   |       |   |       |   |   |       networkDispatchers.js
|   |       |   |       |   |   |       pageAgentDispatcher.js
|   |       |   |       |   |   |       pageDispatcher.js
|   |       |   |       |   |   |       playwrightDispatcher.js
|   |       |   |       |   |   |       streamDispatcher.js
|   |       |   |       |   |   |       tracingDispatcher.js
|   |       |   |       |   |   |       webSocketRouteDispatcher.js
|   |       |   |       |   |   |       writableStreamDispatcher.js
|   |       |   |       |   |   |       
|   |       |   |       |   |   +---electron
|   |       |   |       |   |   |       electron.js
|   |       |   |       |   |   |       loader.js
|   |       |   |       |   |   |       
|   |       |   |       |   |   +---firefox
|   |       |   |       |   |   |       ffBrowser.js
|   |       |   |       |   |   |       ffConnection.js
|   |       |   |       |   |   |       ffExecutionContext.js
|   |       |   |       |   |   |       ffInput.js
|   |       |   |       |   |   |       ffNetworkManager.js
|   |       |   |       |   |   |       ffPage.js
|   |       |   |       |   |   |       firefox.js
|   |       |   |       |   |   |       protocol.d.js
|   |       |   |       |   |   |       
|   |       |   |       |   |   +---har
|   |       |   |       |   |   |       harRecorder.js
|   |       |   |       |   |   |       harTracer.js
|   |       |   |       |   |   |       
|   |       |   |       |   |   +---recorder
|   |       |   |       |   |   |       chat.js
|   |       |   |       |   |   |       recorderApp.js
|   |       |   |       |   |   |       recorderRunner.js
|   |       |   |       |   |   |       recorderSignalProcessor.js
|   |       |   |       |   |   |       recorderUtils.js
|   |       |   |       |   |   |       throttledFile.js
|   |       |   |       |   |   |       
|   |       |   |       |   |   +---registry
|   |       |   |       |   |   |       browserFetcher.js
|   |       |   |       |   |   |       dependencies.js
|   |       |   |       |   |   |       index.js
|   |       |   |       |   |   |       nativeDeps.js
|   |       |   |       |   |   |       oopDownloadBrowserMain.js
|   |       |   |       |   |   |       
|   |       |   |       |   |   +---trace
|   |       |   |       |   |   |   +---recorder
|   |       |   |       |   |   |   |       snapshotter.js
|   |       |   |       |   |   |   |       snapshotterInjected.js
|   |       |   |       |   |   |   |       tracing.js
|   |       |   |       |   |   |   |       
|   |       |   |       |   |   |   \---viewer
|   |       |   |       |   |   |           traceParser.js
|   |       |   |       |   |   |           traceViewer.js
|   |       |   |       |   |   |           
|   |       |   |       |   |   +---utils
|   |       |   |       |   |   |   |   ascii.js
|   |       |   |       |   |   |   |   comparators.js
|   |       |   |       |   |   |   |   crypto.js
|   |       |   |       |   |   |   |   debug.js
|   |       |   |       |   |   |   |   debugLogger.js
|   |       |   |       |   |   |   |   env.js
|   |       |   |       |   |   |   |   eventsHelper.js
|   |       |   |       |   |   |   |   expectUtils.js
|   |       |   |       |   |   |   |   fileUtils.js
|   |       |   |       |   |   |   |   happyEyeballs.js
|   |       |   |       |   |   |   |   hostPlatform.js
|   |       |   |       |   |   |   |   httpServer.js
|   |       |   |       |   |   |   |   imageUtils.js
|   |       |   |       |   |   |   |   linuxUtils.js
|   |       |   |       |   |   |   |   network.js
|   |       |   |       |   |   |   |   nodePlatform.js
|   |       |   |       |   |   |   |   pipeTransport.js
|   |       |   |       |   |   |   |   processLauncher.js
|   |       |   |       |   |   |   |   profiler.js
|   |       |   |       |   |   |   |   socksProxy.js
|   |       |   |       |   |   |   |   spawnAsync.js
|   |       |   |       |   |   |   |   task.js
|   |       |   |       |   |   |   |   userAgent.js
|   |       |   |       |   |   |   |   wsServer.js
|   |       |   |       |   |   |   |   zipFile.js
|   |       |   |       |   |   |   |   zones.js
|   |       |   |       |   |   |   |   
|   |       |   |       |   |   |   \---image_tools
|   |       |   |       |   |   |           colorUtils.js
|   |       |   |       |   |   |           compare.js
|   |       |   |       |   |   |           imageChannel.js
|   |       |   |       |   |   |           stats.js
|   |       |   |       |   |   |           
|   |       |   |       |   |   \---webkit
|   |       |   |       |   |           protocol.d.js
|   |       |   |       |   |           webkit.js
|   |       |   |       |   |           wkBrowser.js
|   |       |   |       |   |           wkConnection.js
|   |       |   |       |   |           wkExecutionContext.js
|   |       |   |       |   |           wkInput.js
|   |       |   |       |   |           wkInterceptableRequest.js
|   |       |   |       |   |           wkPage.js
|   |       |   |       |   |           wkProvisionalPage.js
|   |       |   |       |   |           wkWorkers.js
|   |       |   |       |   |           
|   |       |   |       |   +---third_party
|   |       |   |       |   |       pixelmatch.js
|   |       |   |       |   |       
|   |       |   |       |   +---utils
|   |       |   |       |   |   \---isomorphic
|   |       |   |       |   |       |   ariaSnapshot.js
|   |       |   |       |   |       |   assert.js
|   |       |   |       |   |       |   colors.js
|   |       |   |       |   |       |   cssParser.js
|   |       |   |       |   |       |   cssTokenizer.js
|   |       |   |       |   |       |   headers.js
|   |       |   |       |   |       |   locatorGenerators.js
|   |       |   |       |   |       |   locatorParser.js
|   |       |   |       |   |       |   locatorUtils.js
|   |       |   |       |   |       |   lruCache.js
|   |       |   |       |   |       |   manualPromise.js
|   |       |   |       |   |       |   mimeType.js
|   |       |   |       |   |       |   multimap.js
|   |       |   |       |   |       |   protocolFormatter.js
|   |       |   |       |   |       |   protocolMetainfo.js
|   |       |   |       |   |       |   rtti.js
|   |       |   |       |   |       |   selectorParser.js
|   |       |   |       |   |       |   semaphore.js
|   |       |   |       |   |       |   stackTrace.js
|   |       |   |       |   |       |   stringUtils.js
|   |       |   |       |   |       |   time.js
|   |       |   |       |   |       |   timeoutRunner.js
|   |       |   |       |   |       |   traceUtils.js
|   |       |   |       |   |       |   types.js
|   |       |   |       |   |       |   urlMatch.js
|   |       |   |       |   |       |   utilityScriptSerializers.js
|   |       |   |       |   |       |   yaml.js
|   |       |   |       |   |       |   
|   |       |   |       |   |       \---trace
|   |       |   |       |   |           |   entries.js
|   |       |   |       |   |           |   snapshotRenderer.js
|   |       |   |       |   |           |   snapshotServer.js
|   |       |   |       |   |           |   snapshotStorage.js
|   |       |   |       |   |           |   traceLoader.js
|   |       |   |       |   |           |   traceModel.js
|   |       |   |       |   |           |   traceModernizer.js
|   |       |   |       |   |           |   
|   |       |   |       |   |           \---versions
|   |       |   |       |   |                   traceV3.js
|   |       |   |       |   |                   traceV4.js
|   |       |   |       |   |                   traceV5.js
|   |       |   |       |   |                   traceV6.js
|   |       |   |       |   |                   traceV7.js
|   |       |   |       |   |                   traceV8.js
|   |       |   |       |   |                   
|   |       |   |       |   +---utilsBundleImpl
|   |       |   |       |   |       index.js
|   |       |   |       |   |       xdg-open
|   |       |   |       |   |       
|   |       |   |       |   \---vite
|   |       |   |       |       +---htmlReport
|   |       |   |       |       |       index.html
|   |       |   |       |       |       
|   |       |   |       |       +---recorder
|   |       |   |       |       |   |   index.html
|   |       |   |       |       |   |   playwright-logo.svg
|   |       |   |       |       |   |   
|   |       |   |       |       |   \---assets
|   |       |   |       |       |           codeMirrorModule-DadYNm1I.js
|   |       |   |       |       |           codeMirrorModule-DYBRYzYX.css
|   |       |   |       |       |           codicon-DCmgc-ay.ttf
|   |       |   |       |       |           index-BhTWtUlo.js
|   |       |   |       |       |           index-BSjZa4pk.css
|   |       |   |       |       |           
|   |       |   |       |       \---traceViewer
|   |       |   |       |           |   codeMirrorModule.DYBRYzYX.css
|   |       |   |       |           |   codicon.DCmgc-ay.ttf
|   |       |   |       |           |   defaultSettingsView.7ch9cixO.css
|   |       |   |       |           |   index.Bk2uYQRV.js
|   |       |   |       |           |   index.BVu7tZDe.css
|   |       |   |       |           |   index.html
|   |       |   |       |           |   manifest.webmanifest
|   |       |   |       |           |   playwright-logo.svg
|   |       |   |       |           |   snapshot.html
|   |       |   |       |           |   sw.bundle.js
|   |       |   |       |           |   uiMode.Btcz36p_.css
|   |       |   |       |           |   uiMode.CQJ9SCIQ.js
|   |       |   |       |           |   uiMode.html
|   |       |   |       |           |   xtermModule.DYP7pi_n.css
|   |       |   |       |           |   
|   |       |   |       |           \---assets
|   |       |   |       |                   codeMirrorModule-a5XoALAZ.js
|   |       |   |       |                   defaultSettingsView-CJSZINFr.js
|   |       |   |       |                   xtermModule-CsJ4vdCR.js
|   |       |   |       |                   
|   |       |   |       \---types
|   |       |   |               protocol.d.ts
|   |       |   |               structs.d.ts
|   |       |   |               types.d.ts
|   |       |   |               
|   |       |   +---sync_api
|   |       |   |   |   _context_manager.py
|   |       |   |   |   _generated.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _context_manager.cpython-310.pyc
|   |       |   |           _generated.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_impl
|   |       |   |   |   _api_structures.py
|   |       |   |   |   _artifact.py
|   |       |   |   |   _assertions.py
|   |       |   |   |   _async_base.py
|   |       |   |   |   _browser.py
|   |       |   |   |   _browser_context.py
|   |       |   |   |   _browser_type.py
|   |       |   |   |   _cdp_session.py
|   |       |   |   |   _clock.py
|   |       |   |   |   _connection.py
|   |       |   |   |   _console_message.py
|   |       |   |   |   _dialog.py
|   |       |   |   |   _download.py
|   |       |   |   |   _driver.py
|   |       |   |   |   _element_handle.py
|   |       |   |   |   _errors.py
|   |       |   |   |   _event_context_manager.py
|   |       |   |   |   _fetch.py
|   |       |   |   |   _file_chooser.py
|   |       |   |   |   _frame.py
|   |       |   |   |   _glob.py
|   |       |   |   |   _greenlets.py
|   |       |   |   |   _har_router.py
|   |       |   |   |   _helper.py
|   |       |   |   |   _impl_to_api_mapping.py
|   |       |   |   |   _input.py
|   |       |   |   |   _json_pipe.py
|   |       |   |   |   _js_handle.py
|   |       |   |   |   _local_utils.py
|   |       |   |   |   _locator.py
|   |       |   |   |   _map.py
|   |       |   |   |   _network.py
|   |       |   |   |   _object_factory.py
|   |       |   |   |   _page.py
|   |       |   |   |   _path_utils.py
|   |       |   |   |   _playwright.py
|   |       |   |   |   _selectors.py
|   |       |   |   |   _set_input_files_helpers.py
|   |       |   |   |   _stream.py
|   |       |   |   |   _str_utils.py
|   |       |   |   |   _sync_base.py
|   |       |   |   |   _tracing.py
|   |       |   |   |   _transport.py
|   |       |   |   |   _video.py
|   |       |   |   |   _waiter.py
|   |       |   |   |   _web_error.py
|   |       |   |   |   _writable_stream.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---__pycache__
|   |       |   |   |       _api_structures.cpython-310.pyc
|   |       |   |   |       _artifact.cpython-310.pyc
|   |       |   |   |       _assertions.cpython-310.pyc
|   |       |   |   |       _async_base.cpython-310.pyc
|   |       |   |   |       _browser.cpython-310.pyc
|   |       |   |   |       _browser_context.cpython-310.pyc
|   |       |   |   |       _browser_type.cpython-310.pyc
|   |       |   |   |       _cdp_session.cpython-310.pyc
|   |       |   |   |       _clock.cpython-310.pyc
|   |       |   |   |       _connection.cpython-310.pyc
|   |       |   |   |       _console_message.cpython-310.pyc
|   |       |   |   |       _dialog.cpython-310.pyc
|   |       |   |   |       _download.cpython-310.pyc
|   |       |   |   |       _driver.cpython-310.pyc
|   |       |   |   |       _element_handle.cpython-310.pyc
|   |       |   |   |       _errors.cpython-310.pyc
|   |       |   |   |       _event_context_manager.cpython-310.pyc
|   |       |   |   |       _fetch.cpython-310.pyc
|   |       |   |   |       _file_chooser.cpython-310.pyc
|   |       |   |   |       _frame.cpython-310.pyc
|   |       |   |   |       _glob.cpython-310.pyc
|   |       |   |   |       _greenlets.cpython-310.pyc
|   |       |   |   |       _har_router.cpython-310.pyc
|   |       |   |   |       _helper.cpython-310.pyc
|   |       |   |   |       _impl_to_api_mapping.cpython-310.pyc
|   |       |   |   |       _input.cpython-310.pyc
|   |       |   |   |       _json_pipe.cpython-310.pyc
|   |       |   |   |       _js_handle.cpython-310.pyc
|   |       |   |   |       _local_utils.cpython-310.pyc
|   |       |   |   |       _locator.cpython-310.pyc
|   |       |   |   |       _map.cpython-310.pyc
|   |       |   |   |       _network.cpython-310.pyc
|   |       |   |   |       _object_factory.cpython-310.pyc
|   |       |   |   |       _page.cpython-310.pyc
|   |       |   |   |       _path_utils.cpython-310.pyc
|   |       |   |   |       _playwright.cpython-310.pyc
|   |       |   |   |       _selectors.cpython-310.pyc
|   |       |   |   |       _set_input_files_helpers.cpython-310.pyc
|   |       |   |   |       _stream.cpython-310.pyc
|   |       |   |   |       _str_utils.cpython-310.pyc
|   |       |   |   |       _sync_base.cpython-310.pyc
|   |       |   |   |       _tracing.cpython-310.pyc
|   |       |   |   |       _transport.cpython-310.pyc
|   |       |   |   |       _video.cpython-310.pyc
|   |       |   |   |       _waiter.cpython-310.pyc
|   |       |   |   |       _web_error.cpython-310.pyc
|   |       |   |   |       _writable_stream.cpython-310.pyc
|   |       |   |   |       __init__.cpython-310.pyc
|   |       |   |   |       
|   |       |   |   \---__pyinstaller
|   |       |   |       |   hook-playwright.async_api.py
|   |       |   |       |   hook-playwright.sync_api.py
|   |       |   |       |   __init__.py
|   |       |   |       |   
|   |       |   |       \---__pycache__
|   |       |   |               hook-playwright.async_api.cpython-310.pyc
|   |       |   |               hook-playwright.sync_api.cpython-310.pyc
|   |       |   |               __init__.cpython-310.pyc
|   |       |   |               
|   |       |   \---__pycache__
|   |       |           _repo_version.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           __main__.cpython-310.pyc
|   |       |           
|   |       +---playwright-1.58.0.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---pluggy
|   |       |   |   py.typed
|   |       |   |   _callers.py
|   |       |   |   _hooks.py
|   |       |   |   _manager.py
|   |       |   |   _result.py
|   |       |   |   _tracing.py
|   |       |   |   _version.py
|   |       |   |   _warnings.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           _callers.cpython-310.pyc
|   |       |           _hooks.cpython-310.pyc
|   |       |           _manager.cpython-310.pyc
|   |       |           _result.cpython-310.pyc
|   |       |           _tracing.cpython-310.pyc
|   |       |           _version.cpython-310.pyc
|   |       |           _warnings.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---pluggy-1.6.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---pydantic
|   |       |   |   aliases.py
|   |       |   |   alias_generators.py
|   |       |   |   annotated_handlers.py
|   |       |   |   class_validators.py
|   |       |   |   color.py
|   |       |   |   config.py
|   |       |   |   dataclasses.py
|   |       |   |   datetime_parse.py
|   |       |   |   decorator.py
|   |       |   |   env_settings.py
|   |       |   |   errors.py
|   |       |   |   error_wrappers.py
|   |       |   |   fields.py
|   |       |   |   functional_serializers.py
|   |       |   |   functional_validators.py
|   |       |   |   generics.py
|   |       |   |   json.py
|   |       |   |   json_schema.py
|   |       |   |   main.py
|   |       |   |   mypy.py
|   |       |   |   networks.py
|   |       |   |   parse.py
|   |       |   |   py.typed
|   |       |   |   root_model.py
|   |       |   |   schema.py
|   |       |   |   tools.py
|   |       |   |   types.py
|   |       |   |   type_adapter.py
|   |       |   |   typing.py
|   |       |   |   utils.py
|   |       |   |   validate_call_decorator.py
|   |       |   |   validators.py
|   |       |   |   version.py
|   |       |   |   warnings.py
|   |       |   |   _migration.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---deprecated
|   |       |   |   |   class_validators.py
|   |       |   |   |   config.py
|   |       |   |   |   copy_internals.py
|   |       |   |   |   decorator.py
|   |       |   |   |   json.py
|   |       |   |   |   parse.py
|   |       |   |   |   tools.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           class_validators.cpython-310.pyc
|   |       |   |           config.cpython-310.pyc
|   |       |   |           copy_internals.cpython-310.pyc
|   |       |   |           decorator.cpython-310.pyc
|   |       |   |           json.cpython-310.pyc
|   |       |   |           parse.cpython-310.pyc
|   |       |   |           tools.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---experimental
|   |       |   |   |   arguments_schema.py
|   |       |   |   |   missing_sentinel.py
|   |       |   |   |   pipeline.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           arguments_schema.cpython-310.pyc
|   |       |   |           missing_sentinel.cpython-310.pyc
|   |       |   |           pipeline.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---plugin
|   |       |   |   |   _loader.py
|   |       |   |   |   _schema_validator.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _loader.cpython-310.pyc
|   |       |   |           _schema_validator.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---v1
|   |       |   |   |   annotated_types.py
|   |       |   |   |   class_validators.py
|   |       |   |   |   color.py
|   |       |   |   |   config.py
|   |       |   |   |   dataclasses.py
|   |       |   |   |   datetime_parse.py
|   |       |   |   |   decorator.py
|   |       |   |   |   env_settings.py
|   |       |   |   |   errors.py
|   |       |   |   |   error_wrappers.py
|   |       |   |   |   fields.py
|   |       |   |   |   generics.py
|   |       |   |   |   json.py
|   |       |   |   |   main.py
|   |       |   |   |   mypy.py
|   |       |   |   |   networks.py
|   |       |   |   |   parse.py
|   |       |   |   |   py.typed
|   |       |   |   |   schema.py
|   |       |   |   |   tools.py
|   |       |   |   |   types.py
|   |       |   |   |   typing.py
|   |       |   |   |   utils.py
|   |       |   |   |   validators.py
|   |       |   |   |   version.py
|   |       |   |   |   _hypothesis_plugin.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           annotated_types.cpython-310.pyc
|   |       |   |           class_validators.cpython-310.pyc
|   |       |   |           color.cpython-310.pyc
|   |       |   |           config.cpython-310.pyc
|   |       |   |           dataclasses.cpython-310.pyc
|   |       |   |           datetime_parse.cpython-310.pyc
|   |       |   |           decorator.cpython-310.pyc
|   |       |   |           env_settings.cpython-310.pyc
|   |       |   |           errors.cpython-310.pyc
|   |       |   |           error_wrappers.cpython-310.pyc
|   |       |   |           fields.cpython-310.pyc
|   |       |   |           generics.cpython-310.pyc
|   |       |   |           json.cpython-310.pyc
|   |       |   |           main.cpython-310.pyc
|   |       |   |           mypy.cpython-310.pyc
|   |       |   |           networks.cpython-310.pyc
|   |       |   |           parse.cpython-310.pyc
|   |       |   |           schema.cpython-310.pyc
|   |       |   |           tools.cpython-310.pyc
|   |       |   |           types.cpython-310.pyc
|   |       |   |           typing.cpython-310.pyc
|   |       |   |           utils.cpython-310.pyc
|   |       |   |           validators.cpython-310.pyc
|   |       |   |           version.cpython-310.pyc
|   |       |   |           _hypothesis_plugin.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_internal
|   |       |   |   |   _config.py
|   |       |   |   |   _core_metadata.py
|   |       |   |   |   _core_utils.py
|   |       |   |   |   _dataclasses.py
|   |       |   |   |   _decorators.py
|   |       |   |   |   _decorators_v1.py
|   |       |   |   |   _discriminated_union.py
|   |       |   |   |   _docs_extraction.py
|   |       |   |   |   _fields.py
|   |       |   |   |   _forward_ref.py
|   |       |   |   |   _generate_schema.py
|   |       |   |   |   _generics.py
|   |       |   |   |   _git.py
|   |       |   |   |   _import_utils.py
|   |       |   |   |   _internal_dataclass.py
|   |       |   |   |   _known_annotated_metadata.py
|   |       |   |   |   _mock_val_ser.py
|   |       |   |   |   _model_construction.py
|   |       |   |   |   _namespace_utils.py
|   |       |   |   |   _repr.py
|   |       |   |   |   _schema_gather.py
|   |       |   |   |   _schema_generation_shared.py
|   |       |   |   |   _serializers.py
|   |       |   |   |   _signature.py
|   |       |   |   |   _typing_extra.py
|   |       |   |   |   _utils.py
|   |       |   |   |   _validate_call.py
|   |       |   |   |   _validators.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _config.cpython-310.pyc
|   |       |   |           _core_metadata.cpython-310.pyc
|   |       |   |           _core_utils.cpython-310.pyc
|   |       |   |           _dataclasses.cpython-310.pyc
|   |       |   |           _decorators.cpython-310.pyc
|   |       |   |           _decorators_v1.cpython-310.pyc
|   |       |   |           _discriminated_union.cpython-310.pyc
|   |       |   |           _docs_extraction.cpython-310.pyc
|   |       |   |           _fields.cpython-310.pyc
|   |       |   |           _forward_ref.cpython-310.pyc
|   |       |   |           _generate_schema.cpython-310.pyc
|   |       |   |           _generics.cpython-310.pyc
|   |       |   |           _git.cpython-310.pyc
|   |       |   |           _import_utils.cpython-310.pyc
|   |       |   |           _internal_dataclass.cpython-310.pyc
|   |       |   |           _known_annotated_metadata.cpython-310.pyc
|   |       |   |           _mock_val_ser.cpython-310.pyc
|   |       |   |           _model_construction.cpython-310.pyc
|   |       |   |           _namespace_utils.cpython-310.pyc
|   |       |   |           _repr.cpython-310.pyc
|   |       |   |           _schema_gather.cpython-310.pyc
|   |       |   |           _schema_generation_shared.cpython-310.pyc
|   |       |   |           _serializers.cpython-310.pyc
|   |       |   |           _signature.cpython-310.pyc
|   |       |   |           _typing_extra.cpython-310.pyc
|   |       |   |           _utils.cpython-310.pyc
|   |       |   |           _validate_call.cpython-310.pyc
|   |       |   |           _validators.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           aliases.cpython-310.pyc
|   |       |           alias_generators.cpython-310.pyc
|   |       |           annotated_handlers.cpython-310.pyc
|   |       |           class_validators.cpython-310.pyc
|   |       |           color.cpython-310.pyc
|   |       |           config.cpython-310.pyc
|   |       |           dataclasses.cpython-310.pyc
|   |       |           datetime_parse.cpython-310.pyc
|   |       |           decorator.cpython-310.pyc
|   |       |           env_settings.cpython-310.pyc
|   |       |           errors.cpython-310.pyc
|   |       |           error_wrappers.cpython-310.pyc
|   |       |           fields.cpython-310.pyc
|   |       |           functional_serializers.cpython-310.pyc
|   |       |           functional_validators.cpython-310.pyc
|   |       |           generics.cpython-310.pyc
|   |       |           json.cpython-310.pyc
|   |       |           json_schema.cpython-310.pyc
|   |       |           main.cpython-310.pyc
|   |       |           mypy.cpython-310.pyc
|   |       |           networks.cpython-310.pyc
|   |       |           parse.cpython-310.pyc
|   |       |           root_model.cpython-310.pyc
|   |       |           schema.cpython-310.pyc
|   |       |           tools.cpython-310.pyc
|   |       |           types.cpython-310.pyc
|   |       |           type_adapter.cpython-310.pyc
|   |       |           typing.cpython-310.pyc
|   |       |           utils.cpython-310.pyc
|   |       |           validate_call_decorator.cpython-310.pyc
|   |       |           validators.cpython-310.pyc
|   |       |           version.cpython-310.pyc
|   |       |           warnings.cpython-310.pyc
|   |       |           _migration.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---pydantic-2.13.1.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---pydantic_core
|   |       |   |   core_schema.py
|   |       |   |   py.typed
|   |       |   |   _pydantic_core.cp310-win_amd64.pyd
|   |       |   |   _pydantic_core.pyi
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           core_schema.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---pydantic_core-2.46.1.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   +---licenses
|   |       |   |       LICENSE
|   |       |   |       
|   |       |   \---sboms
|   |       |           pydantic-core.cyclonedx.json
|   |       |           
|   |       +---pyee
|   |       |   |   asyncio.py
|   |       |   |   base.py
|   |       |   |   cls.py
|   |       |   |   executor.py
|   |       |   |   py.typed
|   |       |   |   trio.py
|   |       |   |   twisted.py
|   |       |   |   uplift.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           asyncio.cpython-310.pyc
|   |       |           base.cpython-310.pyc
|   |       |           cls.cpython-310.pyc
|   |       |           executor.cpython-310.pyc
|   |       |           trio.cpython-310.pyc
|   |       |           twisted.cpython-310.pyc
|   |       |           uplift.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---pyee-13.0.1.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---pygments
|   |       |   |   cmdline.py
|   |       |   |   console.py
|   |       |   |   filter.py
|   |       |   |   formatter.py
|   |       |   |   lexer.py
|   |       |   |   modeline.py
|   |       |   |   plugin.py
|   |       |   |   regexopt.py
|   |       |   |   scanner.py
|   |       |   |   sphinxext.py
|   |       |   |   style.py
|   |       |   |   token.py
|   |       |   |   unistring.py
|   |       |   |   util.py
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   +---filters
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---formatters
|   |       |   |   |   bbcode.py
|   |       |   |   |   groff.py
|   |       |   |   |   html.py
|   |       |   |   |   img.py
|   |       |   |   |   irc.py
|   |       |   |   |   latex.py
|   |       |   |   |   other.py
|   |       |   |   |   pangomarkup.py
|   |       |   |   |   rtf.py
|   |       |   |   |   svg.py
|   |       |   |   |   terminal.py
|   |       |   |   |   terminal256.py
|   |       |   |   |   _mapping.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           bbcode.cpython-310.pyc
|   |       |   |           groff.cpython-310.pyc
|   |       |   |           html.cpython-310.pyc
|   |       |   |           img.cpython-310.pyc
|   |       |   |           irc.cpython-310.pyc
|   |       |   |           latex.cpython-310.pyc
|   |       |   |           other.cpython-310.pyc
|   |       |   |           pangomarkup.cpython-310.pyc
|   |       |   |           rtf.cpython-310.pyc
|   |       |   |           svg.cpython-310.pyc
|   |       |   |           terminal.cpython-310.pyc
|   |       |   |           terminal256.cpython-310.pyc
|   |       |   |           _mapping.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---lexers
|   |       |   |   |   actionscript.py
|   |       |   |   |   ada.py
|   |       |   |   |   agile.py
|   |       |   |   |   algebra.py
|   |       |   |   |   ambient.py
|   |       |   |   |   amdgpu.py
|   |       |   |   |   ampl.py
|   |       |   |   |   apdlexer.py
|   |       |   |   |   apl.py
|   |       |   |   |   archetype.py
|   |       |   |   |   arrow.py
|   |       |   |   |   arturo.py
|   |       |   |   |   asc.py
|   |       |   |   |   asm.py
|   |       |   |   |   asn1.py
|   |       |   |   |   automation.py
|   |       |   |   |   bare.py
|   |       |   |   |   basic.py
|   |       |   |   |   bdd.py
|   |       |   |   |   berry.py
|   |       |   |   |   bibtex.py
|   |       |   |   |   blueprint.py
|   |       |   |   |   boa.py
|   |       |   |   |   bqn.py
|   |       |   |   |   business.py
|   |       |   |   |   capnproto.py
|   |       |   |   |   carbon.py
|   |       |   |   |   cddl.py
|   |       |   |   |   chapel.py
|   |       |   |   |   clean.py
|   |       |   |   |   codeql.py
|   |       |   |   |   comal.py
|   |       |   |   |   compiled.py
|   |       |   |   |   configs.py
|   |       |   |   |   console.py
|   |       |   |   |   cplint.py
|   |       |   |   |   crystal.py
|   |       |   |   |   csound.py
|   |       |   |   |   css.py
|   |       |   |   |   c_cpp.py
|   |       |   |   |   c_like.py
|   |       |   |   |   d.py
|   |       |   |   |   dalvik.py
|   |       |   |   |   data.py
|   |       |   |   |   dax.py
|   |       |   |   |   devicetree.py
|   |       |   |   |   diff.py
|   |       |   |   |   dns.py
|   |       |   |   |   dotnet.py
|   |       |   |   |   dsls.py
|   |       |   |   |   dylan.py
|   |       |   |   |   ecl.py
|   |       |   |   |   eiffel.py
|   |       |   |   |   elm.py
|   |       |   |   |   elpi.py
|   |       |   |   |   email.py
|   |       |   |   |   erlang.py
|   |       |   |   |   esoteric.py
|   |       |   |   |   ezhil.py
|   |       |   |   |   factor.py
|   |       |   |   |   fantom.py
|   |       |   |   |   felix.py
|   |       |   |   |   fift.py
|   |       |   |   |   floscript.py
|   |       |   |   |   forth.py
|   |       |   |   |   fortran.py
|   |       |   |   |   foxpro.py
|   |       |   |   |   freefem.py
|   |       |   |   |   func.py
|   |       |   |   |   functional.py
|   |       |   |   |   futhark.py
|   |       |   |   |   gcodelexer.py
|   |       |   |   |   gdscript.py
|   |       |   |   |   gleam.py
|   |       |   |   |   go.py
|   |       |   |   |   grammar_notation.py
|   |       |   |   |   graph.py
|   |       |   |   |   graphics.py
|   |       |   |   |   graphql.py
|   |       |   |   |   graphviz.py
|   |       |   |   |   gsql.py
|   |       |   |   |   hare.py
|   |       |   |   |   haskell.py
|   |       |   |   |   haxe.py
|   |       |   |   |   hdl.py
|   |       |   |   |   hexdump.py
|   |       |   |   |   html.py
|   |       |   |   |   idl.py
|   |       |   |   |   igor.py
|   |       |   |   |   inferno.py
|   |       |   |   |   installers.py
|   |       |   |   |   int_fiction.py
|   |       |   |   |   iolang.py
|   |       |   |   |   j.py
|   |       |   |   |   javascript.py
|   |       |   |   |   jmespath.py
|   |       |   |   |   jslt.py
|   |       |   |   |   json5.py
|   |       |   |   |   jsonnet.py
|   |       |   |   |   jsx.py
|   |       |   |   |   julia.py
|   |       |   |   |   jvm.py
|   |       |   |   |   kuin.py
|   |       |   |   |   kusto.py
|   |       |   |   |   ldap.py
|   |       |   |   |   lean.py
|   |       |   |   |   lilypond.py
|   |       |   |   |   lisp.py
|   |       |   |   |   macaulay2.py
|   |       |   |   |   make.py
|   |       |   |   |   maple.py
|   |       |   |   |   markup.py
|   |       |   |   |   math.py
|   |       |   |   |   matlab.py
|   |       |   |   |   maxima.py
|   |       |   |   |   meson.py
|   |       |   |   |   mime.py
|   |       |   |   |   minecraft.py
|   |       |   |   |   mips.py
|   |       |   |   |   ml.py
|   |       |   |   |   modeling.py
|   |       |   |   |   modula2.py
|   |       |   |   |   mojo.py
|   |       |   |   |   monte.py
|   |       |   |   |   mosel.py
|   |       |   |   |   ncl.py
|   |       |   |   |   nimrod.py
|   |       |   |   |   nit.py
|   |       |   |   |   nix.py
|   |       |   |   |   numbair.py
|   |       |   |   |   oberon.py
|   |       |   |   |   objective.py
|   |       |   |   |   ooc.py
|   |       |   |   |   openscad.py
|   |       |   |   |   other.py
|   |       |   |   |   parasail.py
|   |       |   |   |   parsers.py
|   |       |   |   |   pascal.py
|   |       |   |   |   pawn.py
|   |       |   |   |   pddl.py
|   |       |   |   |   perl.py
|   |       |   |   |   phix.py
|   |       |   |   |   php.py
|   |       |   |   |   pointless.py
|   |       |   |   |   pony.py
|   |       |   |   |   praat.py
|   |       |   |   |   procfile.py
|   |       |   |   |   prolog.py
|   |       |   |   |   promql.py
|   |       |   |   |   prql.py
|   |       |   |   |   ptx.py
|   |       |   |   |   python.py
|   |       |   |   |   q.py
|   |       |   |   |   qlik.py
|   |       |   |   |   qvt.py
|   |       |   |   |   r.py
|   |       |   |   |   rdf.py
|   |       |   |   |   rebol.py
|   |       |   |   |   rego.py
|   |       |   |   |   rell.py
|   |       |   |   |   resource.py
|   |       |   |   |   ride.py
|   |       |   |   |   rita.py
|   |       |   |   |   rnc.py
|   |       |   |   |   roboconf.py
|   |       |   |   |   robotframework.py
|   |       |   |   |   ruby.py
|   |       |   |   |   rust.py
|   |       |   |   |   sas.py
|   |       |   |   |   savi.py
|   |       |   |   |   scdoc.py
|   |       |   |   |   scripting.py
|   |       |   |   |   sgf.py
|   |       |   |   |   shell.py
|   |       |   |   |   sieve.py
|   |       |   |   |   slash.py
|   |       |   |   |   smalltalk.py
|   |       |   |   |   smithy.py
|   |       |   |   |   smv.py
|   |       |   |   |   snobol.py
|   |       |   |   |   solidity.py
|   |       |   |   |   soong.py
|   |       |   |   |   sophia.py
|   |       |   |   |   special.py
|   |       |   |   |   spice.py
|   |       |   |   |   sql.py
|   |       |   |   |   srcinfo.py
|   |       |   |   |   stata.py
|   |       |   |   |   supercollider.py
|   |       |   |   |   tablegen.py
|   |       |   |   |   tact.py
|   |       |   |   |   tal.py
|   |       |   |   |   tcl.py
|   |       |   |   |   teal.py
|   |       |   |   |   templates.py
|   |       |   |   |   teraterm.py
|   |       |   |   |   testing.py
|   |       |   |   |   text.py
|   |       |   |   |   textedit.py
|   |       |   |   |   textfmts.py
|   |       |   |   |   theorem.py
|   |       |   |   |   thingsdb.py
|   |       |   |   |   tlb.py
|   |       |   |   |   tls.py
|   |       |   |   |   tnt.py
|   |       |   |   |   trafficscript.py
|   |       |   |   |   typoscript.py
|   |       |   |   |   typst.py
|   |       |   |   |   ul4.py
|   |       |   |   |   unicon.py
|   |       |   |   |   urbi.py
|   |       |   |   |   usd.py
|   |       |   |   |   varnish.py
|   |       |   |   |   verification.py
|   |       |   |   |   verifpal.py
|   |       |   |   |   vip.py
|   |       |   |   |   vyper.py
|   |       |   |   |   web.py
|   |       |   |   |   webassembly.py
|   |       |   |   |   webidl.py
|   |       |   |   |   webmisc.py
|   |       |   |   |   wgsl.py
|   |       |   |   |   whiley.py
|   |       |   |   |   wowtoc.py
|   |       |   |   |   wren.py
|   |       |   |   |   x10.py
|   |       |   |   |   xorg.py
|   |       |   |   |   yang.py
|   |       |   |   |   yara.py
|   |       |   |   |   zig.py
|   |       |   |   |   _ada_builtins.py
|   |       |   |   |   _asy_builtins.py
|   |       |   |   |   _cl_builtins.py
|   |       |   |   |   _cocoa_builtins.py
|   |       |   |   |   _csound_builtins.py
|   |       |   |   |   _css_builtins.py
|   |       |   |   |   _googlesql_builtins.py
|   |       |   |   |   _julia_builtins.py
|   |       |   |   |   _lasso_builtins.py
|   |       |   |   |   _lilypond_builtins.py
|   |       |   |   |   _luau_builtins.py
|   |       |   |   |   _lua_builtins.py
|   |       |   |   |   _mapping.py
|   |       |   |   |   _mql_builtins.py
|   |       |   |   |   _mysql_builtins.py
|   |       |   |   |   _openedge_builtins.py
|   |       |   |   |   _php_builtins.py
|   |       |   |   |   _postgres_builtins.py
|   |       |   |   |   _qlik_builtins.py
|   |       |   |   |   _scheme_builtins.py
|   |       |   |   |   _scilab_builtins.py
|   |       |   |   |   _sourcemod_builtins.py
|   |       |   |   |   _sql_builtins.py
|   |       |   |   |   _stan_builtins.py
|   |       |   |   |   _stata_builtins.py
|   |       |   |   |   _tsql_builtins.py
|   |       |   |   |   _usd_builtins.py
|   |       |   |   |   _vbscript_builtins.py
|   |       |   |   |   _vim_builtins.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           actionscript.cpython-310.pyc
|   |       |   |           ada.cpython-310.pyc
|   |       |   |           agile.cpython-310.pyc
|   |       |   |           algebra.cpython-310.pyc
|   |       |   |           ambient.cpython-310.pyc
|   |       |   |           amdgpu.cpython-310.pyc
|   |       |   |           ampl.cpython-310.pyc
|   |       |   |           apdlexer.cpython-310.pyc
|   |       |   |           apl.cpython-310.pyc
|   |       |   |           archetype.cpython-310.pyc
|   |       |   |           arrow.cpython-310.pyc
|   |       |   |           arturo.cpython-310.pyc
|   |       |   |           asc.cpython-310.pyc
|   |       |   |           asm.cpython-310.pyc
|   |       |   |           asn1.cpython-310.pyc
|   |       |   |           automation.cpython-310.pyc
|   |       |   |           bare.cpython-310.pyc
|   |       |   |           basic.cpython-310.pyc
|   |       |   |           bdd.cpython-310.pyc
|   |       |   |           berry.cpython-310.pyc
|   |       |   |           bibtex.cpython-310.pyc
|   |       |   |           blueprint.cpython-310.pyc
|   |       |   |           boa.cpython-310.pyc
|   |       |   |           bqn.cpython-310.pyc
|   |       |   |           business.cpython-310.pyc
|   |       |   |           capnproto.cpython-310.pyc
|   |       |   |           carbon.cpython-310.pyc
|   |       |   |           cddl.cpython-310.pyc
|   |       |   |           chapel.cpython-310.pyc
|   |       |   |           clean.cpython-310.pyc
|   |       |   |           codeql.cpython-310.pyc
|   |       |   |           comal.cpython-310.pyc
|   |       |   |           compiled.cpython-310.pyc
|   |       |   |           configs.cpython-310.pyc
|   |       |   |           console.cpython-310.pyc
|   |       |   |           cplint.cpython-310.pyc
|   |       |   |           crystal.cpython-310.pyc
|   |       |   |           csound.cpython-310.pyc
|   |       |   |           css.cpython-310.pyc
|   |       |   |           c_cpp.cpython-310.pyc
|   |       |   |           c_like.cpython-310.pyc
|   |       |   |           d.cpython-310.pyc
|   |       |   |           dalvik.cpython-310.pyc
|   |       |   |           data.cpython-310.pyc
|   |       |   |           dax.cpython-310.pyc
|   |       |   |           devicetree.cpython-310.pyc
|   |       |   |           diff.cpython-310.pyc
|   |       |   |           dns.cpython-310.pyc
|   |       |   |           dotnet.cpython-310.pyc
|   |       |   |           dsls.cpython-310.pyc
|   |       |   |           dylan.cpython-310.pyc
|   |       |   |           ecl.cpython-310.pyc
|   |       |   |           eiffel.cpython-310.pyc
|   |       |   |           elm.cpython-310.pyc
|   |       |   |           elpi.cpython-310.pyc
|   |       |   |           email.cpython-310.pyc
|   |       |   |           erlang.cpython-310.pyc
|   |       |   |           esoteric.cpython-310.pyc
|   |       |   |           ezhil.cpython-310.pyc
|   |       |   |           factor.cpython-310.pyc
|   |       |   |           fantom.cpython-310.pyc
|   |       |   |           felix.cpython-310.pyc
|   |       |   |           fift.cpython-310.pyc
|   |       |   |           floscript.cpython-310.pyc
|   |       |   |           forth.cpython-310.pyc
|   |       |   |           fortran.cpython-310.pyc
|   |       |   |           foxpro.cpython-310.pyc
|   |       |   |           freefem.cpython-310.pyc
|   |       |   |           func.cpython-310.pyc
|   |       |   |           functional.cpython-310.pyc
|   |       |   |           futhark.cpython-310.pyc
|   |       |   |           gcodelexer.cpython-310.pyc
|   |       |   |           gdscript.cpython-310.pyc
|   |       |   |           gleam.cpython-310.pyc
|   |       |   |           go.cpython-310.pyc
|   |       |   |           grammar_notation.cpython-310.pyc
|   |       |   |           graph.cpython-310.pyc
|   |       |   |           graphics.cpython-310.pyc
|   |       |   |           graphql.cpython-310.pyc
|   |       |   |           graphviz.cpython-310.pyc
|   |       |   |           gsql.cpython-310.pyc
|   |       |   |           hare.cpython-310.pyc
|   |       |   |           haskell.cpython-310.pyc
|   |       |   |           haxe.cpython-310.pyc
|   |       |   |           hdl.cpython-310.pyc
|   |       |   |           hexdump.cpython-310.pyc
|   |       |   |           html.cpython-310.pyc
|   |       |   |           idl.cpython-310.pyc
|   |       |   |           igor.cpython-310.pyc
|   |       |   |           inferno.cpython-310.pyc
|   |       |   |           installers.cpython-310.pyc
|   |       |   |           int_fiction.cpython-310.pyc
|   |       |   |           iolang.cpython-310.pyc
|   |       |   |           j.cpython-310.pyc
|   |       |   |           javascript.cpython-310.pyc
|   |       |   |           jmespath.cpython-310.pyc
|   |       |   |           jslt.cpython-310.pyc
|   |       |   |           json5.cpython-310.pyc
|   |       |   |           jsonnet.cpython-310.pyc
|   |       |   |           jsx.cpython-310.pyc
|   |       |   |           julia.cpython-310.pyc
|   |       |   |           jvm.cpython-310.pyc
|   |       |   |           kuin.cpython-310.pyc
|   |       |   |           kusto.cpython-310.pyc
|   |       |   |           ldap.cpython-310.pyc
|   |       |   |           lean.cpython-310.pyc
|   |       |   |           lilypond.cpython-310.pyc
|   |       |   |           lisp.cpython-310.pyc
|   |       |   |           macaulay2.cpython-310.pyc
|   |       |   |           make.cpython-310.pyc
|   |       |   |           maple.cpython-310.pyc
|   |       |   |           markup.cpython-310.pyc
|   |       |   |           math.cpython-310.pyc
|   |       |   |           matlab.cpython-310.pyc
|   |       |   |           maxima.cpython-310.pyc
|   |       |   |           meson.cpython-310.pyc
|   |       |   |           mime.cpython-310.pyc
|   |       |   |           minecraft.cpython-310.pyc
|   |       |   |           mips.cpython-310.pyc
|   |       |   |           ml.cpython-310.pyc
|   |       |   |           modeling.cpython-310.pyc
|   |       |   |           modula2.cpython-310.pyc
|   |       |   |           mojo.cpython-310.pyc
|   |       |   |           monte.cpython-310.pyc
|   |       |   |           mosel.cpython-310.pyc
|   |       |   |           ncl.cpython-310.pyc
|   |       |   |           nimrod.cpython-310.pyc
|   |       |   |           nit.cpython-310.pyc
|   |       |   |           nix.cpython-310.pyc
|   |       |   |           numbair.cpython-310.pyc
|   |       |   |           oberon.cpython-310.pyc
|   |       |   |           objective.cpython-310.pyc
|   |       |   |           ooc.cpython-310.pyc
|   |       |   |           openscad.cpython-310.pyc
|   |       |   |           other.cpython-310.pyc
|   |       |   |           parasail.cpython-310.pyc
|   |       |   |           parsers.cpython-310.pyc
|   |       |   |           pascal.cpython-310.pyc
|   |       |   |           pawn.cpython-310.pyc
|   |       |   |           pddl.cpython-310.pyc
|   |       |   |           perl.cpython-310.pyc
|   |       |   |           phix.cpython-310.pyc
|   |       |   |           php.cpython-310.pyc
|   |       |   |           pointless.cpython-310.pyc
|   |       |   |           pony.cpython-310.pyc
|   |       |   |           praat.cpython-310.pyc
|   |       |   |           procfile.cpython-310.pyc
|   |       |   |           prolog.cpython-310.pyc
|   |       |   |           promql.cpython-310.pyc
|   |       |   |           prql.cpython-310.pyc
|   |       |   |           ptx.cpython-310.pyc
|   |       |   |           python.cpython-310.pyc
|   |       |   |           q.cpython-310.pyc
|   |       |   |           qlik.cpython-310.pyc
|   |       |   |           qvt.cpython-310.pyc
|   |       |   |           r.cpython-310.pyc
|   |       |   |           rdf.cpython-310.pyc
|   |       |   |           rebol.cpython-310.pyc
|   |       |   |           rego.cpython-310.pyc
|   |       |   |           rell.cpython-310.pyc
|   |       |   |           resource.cpython-310.pyc
|   |       |   |           ride.cpython-310.pyc
|   |       |   |           rita.cpython-310.pyc
|   |       |   |           rnc.cpython-310.pyc
|   |       |   |           roboconf.cpython-310.pyc
|   |       |   |           robotframework.cpython-310.pyc
|   |       |   |           ruby.cpython-310.pyc
|   |       |   |           rust.cpython-310.pyc
|   |       |   |           sas.cpython-310.pyc
|   |       |   |           savi.cpython-310.pyc
|   |       |   |           scdoc.cpython-310.pyc
|   |       |   |           scripting.cpython-310.pyc
|   |       |   |           sgf.cpython-310.pyc
|   |       |   |           shell.cpython-310.pyc
|   |       |   |           sieve.cpython-310.pyc
|   |       |   |           slash.cpython-310.pyc
|   |       |   |           smalltalk.cpython-310.pyc
|   |       |   |           smithy.cpython-310.pyc
|   |       |   |           smv.cpython-310.pyc
|   |       |   |           snobol.cpython-310.pyc
|   |       |   |           solidity.cpython-310.pyc
|   |       |   |           soong.cpython-310.pyc
|   |       |   |           sophia.cpython-310.pyc
|   |       |   |           special.cpython-310.pyc
|   |       |   |           spice.cpython-310.pyc
|   |       |   |           sql.cpython-310.pyc
|   |       |   |           srcinfo.cpython-310.pyc
|   |       |   |           stata.cpython-310.pyc
|   |       |   |           supercollider.cpython-310.pyc
|   |       |   |           tablegen.cpython-310.pyc
|   |       |   |           tact.cpython-310.pyc
|   |       |   |           tal.cpython-310.pyc
|   |       |   |           tcl.cpython-310.pyc
|   |       |   |           teal.cpython-310.pyc
|   |       |   |           templates.cpython-310.pyc
|   |       |   |           teraterm.cpython-310.pyc
|   |       |   |           testing.cpython-310.pyc
|   |       |   |           text.cpython-310.pyc
|   |       |   |           textedit.cpython-310.pyc
|   |       |   |           textfmts.cpython-310.pyc
|   |       |   |           theorem.cpython-310.pyc
|   |       |   |           thingsdb.cpython-310.pyc
|   |       |   |           tlb.cpython-310.pyc
|   |       |   |           tls.cpython-310.pyc
|   |       |   |           tnt.cpython-310.pyc
|   |       |   |           trafficscript.cpython-310.pyc
|   |       |   |           typoscript.cpython-310.pyc
|   |       |   |           typst.cpython-310.pyc
|   |       |   |           ul4.cpython-310.pyc
|   |       |   |           unicon.cpython-310.pyc
|   |       |   |           urbi.cpython-310.pyc
|   |       |   |           usd.cpython-310.pyc
|   |       |   |           varnish.cpython-310.pyc
|   |       |   |           verification.cpython-310.pyc
|   |       |   |           verifpal.cpython-310.pyc
|   |       |   |           vip.cpython-310.pyc
|   |       |   |           vyper.cpython-310.pyc
|   |       |   |           web.cpython-310.pyc
|   |       |   |           webassembly.cpython-310.pyc
|   |       |   |           webidl.cpython-310.pyc
|   |       |   |           webmisc.cpython-310.pyc
|   |       |   |           wgsl.cpython-310.pyc
|   |       |   |           whiley.cpython-310.pyc
|   |       |   |           wowtoc.cpython-310.pyc
|   |       |   |           wren.cpython-310.pyc
|   |       |   |           x10.cpython-310.pyc
|   |       |   |           xorg.cpython-310.pyc
|   |       |   |           yang.cpython-310.pyc
|   |       |   |           yara.cpython-310.pyc
|   |       |   |           zig.cpython-310.pyc
|   |       |   |           _ada_builtins.cpython-310.pyc
|   |       |   |           _asy_builtins.cpython-310.pyc
|   |       |   |           _cl_builtins.cpython-310.pyc
|   |       |   |           _cocoa_builtins.cpython-310.pyc
|   |       |   |           _csound_builtins.cpython-310.pyc
|   |       |   |           _css_builtins.cpython-310.pyc
|   |       |   |           _googlesql_builtins.cpython-310.pyc
|   |       |   |           _julia_builtins.cpython-310.pyc
|   |       |   |           _lasso_builtins.cpython-310.pyc
|   |       |   |           _lilypond_builtins.cpython-310.pyc
|   |       |   |           _luau_builtins.cpython-310.pyc
|   |       |   |           _lua_builtins.cpython-310.pyc
|   |       |   |           _mapping.cpython-310.pyc
|   |       |   |           _mql_builtins.cpython-310.pyc
|   |       |   |           _mysql_builtins.cpython-310.pyc
|   |       |   |           _openedge_builtins.cpython-310.pyc
|   |       |   |           _php_builtins.cpython-310.pyc
|   |       |   |           _postgres_builtins.cpython-310.pyc
|   |       |   |           _qlik_builtins.cpython-310.pyc
|   |       |   |           _scheme_builtins.cpython-310.pyc
|   |       |   |           _scilab_builtins.cpython-310.pyc
|   |       |   |           _sourcemod_builtins.cpython-310.pyc
|   |       |   |           _sql_builtins.cpython-310.pyc
|   |       |   |           _stan_builtins.cpython-310.pyc
|   |       |   |           _stata_builtins.cpython-310.pyc
|   |       |   |           _tsql_builtins.cpython-310.pyc
|   |       |   |           _usd_builtins.cpython-310.pyc
|   |       |   |           _vbscript_builtins.cpython-310.pyc
|   |       |   |           _vim_builtins.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---styles
|   |       |   |   |   abap.py
|   |       |   |   |   algol.py
|   |       |   |   |   algol_nu.py
|   |       |   |   |   arduino.py
|   |       |   |   |   autumn.py
|   |       |   |   |   borland.py
|   |       |   |   |   bw.py
|   |       |   |   |   coffee.py
|   |       |   |   |   colorful.py
|   |       |   |   |   default.py
|   |       |   |   |   dracula.py
|   |       |   |   |   emacs.py
|   |       |   |   |   friendly.py
|   |       |   |   |   friendly_grayscale.py
|   |       |   |   |   fruity.py
|   |       |   |   |   gh_dark.py
|   |       |   |   |   gruvbox.py
|   |       |   |   |   igor.py
|   |       |   |   |   inkpot.py
|   |       |   |   |   lightbulb.py
|   |       |   |   |   lilypond.py
|   |       |   |   |   lovelace.py
|   |       |   |   |   manni.py
|   |       |   |   |   material.py
|   |       |   |   |   monokai.py
|   |       |   |   |   murphy.py
|   |       |   |   |   native.py
|   |       |   |   |   nord.py
|   |       |   |   |   onedark.py
|   |       |   |   |   paraiso_dark.py
|   |       |   |   |   paraiso_light.py
|   |       |   |   |   pastie.py
|   |       |   |   |   perldoc.py
|   |       |   |   |   rainbow_dash.py
|   |       |   |   |   rrt.py
|   |       |   |   |   sas.py
|   |       |   |   |   solarized.py
|   |       |   |   |   staroffice.py
|   |       |   |   |   stata_dark.py
|   |       |   |   |   stata_light.py
|   |       |   |   |   tango.py
|   |       |   |   |   trac.py
|   |       |   |   |   vim.py
|   |       |   |   |   vs.py
|   |       |   |   |   xcode.py
|   |       |   |   |   zenburn.py
|   |       |   |   |   _mapping.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           abap.cpython-310.pyc
|   |       |   |           algol.cpython-310.pyc
|   |       |   |           algol_nu.cpython-310.pyc
|   |       |   |           arduino.cpython-310.pyc
|   |       |   |           autumn.cpython-310.pyc
|   |       |   |           borland.cpython-310.pyc
|   |       |   |           bw.cpython-310.pyc
|   |       |   |           coffee.cpython-310.pyc
|   |       |   |           colorful.cpython-310.pyc
|   |       |   |           default.cpython-310.pyc
|   |       |   |           dracula.cpython-310.pyc
|   |       |   |           emacs.cpython-310.pyc
|   |       |   |           friendly.cpython-310.pyc
|   |       |   |           friendly_grayscale.cpython-310.pyc
|   |       |   |           fruity.cpython-310.pyc
|   |       |   |           gh_dark.cpython-310.pyc
|   |       |   |           gruvbox.cpython-310.pyc
|   |       |   |           igor.cpython-310.pyc
|   |       |   |           inkpot.cpython-310.pyc
|   |       |   |           lightbulb.cpython-310.pyc
|   |       |   |           lilypond.cpython-310.pyc
|   |       |   |           lovelace.cpython-310.pyc
|   |       |   |           manni.cpython-310.pyc
|   |       |   |           material.cpython-310.pyc
|   |       |   |           monokai.cpython-310.pyc
|   |       |   |           murphy.cpython-310.pyc
|   |       |   |           native.cpython-310.pyc
|   |       |   |           nord.cpython-310.pyc
|   |       |   |           onedark.cpython-310.pyc
|   |       |   |           paraiso_dark.cpython-310.pyc
|   |       |   |           paraiso_light.cpython-310.pyc
|   |       |   |           pastie.cpython-310.pyc
|   |       |   |           perldoc.cpython-310.pyc
|   |       |   |           rainbow_dash.cpython-310.pyc
|   |       |   |           rrt.cpython-310.pyc
|   |       |   |           sas.cpython-310.pyc
|   |       |   |           solarized.cpython-310.pyc
|   |       |   |           staroffice.cpython-310.pyc
|   |       |   |           stata_dark.cpython-310.pyc
|   |       |   |           stata_light.cpython-310.pyc
|   |       |   |           tango.cpython-310.pyc
|   |       |   |           trac.cpython-310.pyc
|   |       |   |           vim.cpython-310.pyc
|   |       |   |           vs.cpython-310.pyc
|   |       |   |           xcode.cpython-310.pyc
|   |       |   |           zenburn.cpython-310.pyc
|   |       |   |           _mapping.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           cmdline.cpython-310.pyc
|   |       |           console.cpython-310.pyc
|   |       |           filter.cpython-310.pyc
|   |       |           formatter.cpython-310.pyc
|   |       |           lexer.cpython-310.pyc
|   |       |           modeline.cpython-310.pyc
|   |       |           plugin.cpython-310.pyc
|   |       |           regexopt.cpython-310.pyc
|   |       |           scanner.cpython-310.pyc
|   |       |           sphinxext.cpython-310.pyc
|   |       |           style.cpython-310.pyc
|   |       |           token.cpython-310.pyc
|   |       |           unistring.cpython-310.pyc
|   |       |           util.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           __main__.cpython-310.pyc
|   |       |           
|   |       +---pygments-2.20.0.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           AUTHORS
|   |       |           LICENSE
|   |       |           
|   |       +---pytest
|   |       |   |   py.typed
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           __init__.cpython-310.pyc
|   |       |           __main__.cpython-310.pyc
|   |       |           
|   |       +---pytest-9.0.3.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---pytest_asyncio
|   |       |   |   plugin.py
|   |       |   |   py.typed
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           plugin.cpython-310-pytest-9.0.3.pyc
|   |       |           plugin.cpython-310.pyc
|   |       |           __init__.cpython-310-pytest-9.0.3.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---pytest_asyncio-1.3.0.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---pytest_cov
|   |       |   |   engine.py
|   |       |   |   plugin.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           engine.cpython-310.pyc
|   |       |           plugin.cpython-310-pytest-9.0.3.pyc
|   |       |           plugin.cpython-310.pyc
|   |       |           __init__.cpython-310-pytest-9.0.3.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---pytest_cov-7.1.0.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           AUTHORS.rst
|   |       |           LICENSE
|   |       |           
|   |       +---python_dateutil-2.9.0.post0.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       top_level.txt
|   |       |       WHEEL
|   |       |       zip-safe
|   |       |       
|   |       +---python_dotenv-1.2.2.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---pytz
|   |       |   |   exceptions.py
|   |       |   |   lazy.py
|   |       |   |   reference.py
|   |       |   |   tzfile.py
|   |       |   |   tzinfo.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---zoneinfo
|   |       |   |   |   CET
|   |       |   |   |   CST6CDT
|   |       |   |   |   Cuba
|   |       |   |   |   EET
|   |       |   |   |   Egypt
|   |       |   |   |   Eire
|   |       |   |   |   EST
|   |       |   |   |   EST5EDT
|   |       |   |   |   Factory
|   |       |   |   |   GB
|   |       |   |   |   GB-Eire
|   |       |   |   |   GMT
|   |       |   |   |   GMT+0
|   |       |   |   |   GMT-0
|   |       |   |   |   GMT0
|   |       |   |   |   Greenwich
|   |       |   |   |   Hongkong
|   |       |   |   |   HST
|   |       |   |   |   Iceland
|   |       |   |   |   Iran
|   |       |   |   |   iso3166.tab
|   |       |   |   |   Israel
|   |       |   |   |   Jamaica
|   |       |   |   |   Japan
|   |       |   |   |   Kwajalein
|   |       |   |   |   leapseconds
|   |       |   |   |   Libya
|   |       |   |   |   MET
|   |       |   |   |   MST
|   |       |   |   |   MST7MDT
|   |       |   |   |   Navajo
|   |       |   |   |   NZ
|   |       |   |   |   NZ-CHAT
|   |       |   |   |   Poland
|   |       |   |   |   Portugal
|   |       |   |   |   PRC
|   |       |   |   |   PST8PDT
|   |       |   |   |   ROC
|   |       |   |   |   ROK
|   |       |   |   |   Singapore
|   |       |   |   |   Turkey
|   |       |   |   |   tzdata.zi
|   |       |   |   |   UCT
|   |       |   |   |   Universal
|   |       |   |   |   UTC
|   |       |   |   |   W-SU
|   |       |   |   |   WET
|   |       |   |   |   zone.tab
|   |       |   |   |   zone1970.tab
|   |       |   |   |   zonenow.tab
|   |       |   |   |   Zulu
|   |       |   |   |   
|   |       |   |   +---Africa
|   |       |   |   |       Abidjan
|   |       |   |   |       Accra
|   |       |   |   |       Addis_Ababa
|   |       |   |   |       Algiers
|   |       |   |   |       Asmara
|   |       |   |   |       Asmera
|   |       |   |   |       Bamako
|   |       |   |   |       Bangui
|   |       |   |   |       Banjul
|   |       |   |   |       Bissau
|   |       |   |   |       Blantyre
|   |       |   |   |       Brazzaville
|   |       |   |   |       Bujumbura
|   |       |   |   |       Cairo
|   |       |   |   |       Casablanca
|   |       |   |   |       Ceuta
|   |       |   |   |       Conakry
|   |       |   |   |       Dakar
|   |       |   |   |       Dar_es_Salaam
|   |       |   |   |       Djibouti
|   |       |   |   |       Douala
|   |       |   |   |       El_Aaiun
|   |       |   |   |       Freetown
|   |       |   |   |       Gaborone
|   |       |   |   |       Harare
|   |       |   |   |       Johannesburg
|   |       |   |   |       Juba
|   |       |   |   |       Kampala
|   |       |   |   |       Khartoum
|   |       |   |   |       Kigali
|   |       |   |   |       Kinshasa
|   |       |   |   |       Lagos
|   |       |   |   |       Libreville
|   |       |   |   |       Lome
|   |       |   |   |       Luanda
|   |       |   |   |       Lubumbashi
|   |       |   |   |       Lusaka
|   |       |   |   |       Malabo
|   |       |   |   |       Maputo
|   |       |   |   |       Maseru
|   |       |   |   |       Mbabane
|   |       |   |   |       Mogadishu
|   |       |   |   |       Monrovia
|   |       |   |   |       Nairobi
|   |       |   |   |       Ndjamena
|   |       |   |   |       Niamey
|   |       |   |   |       Nouakchott
|   |       |   |   |       Ouagadougou
|   |       |   |   |       Porto-Novo
|   |       |   |   |       Sao_Tome
|   |       |   |   |       Timbuktu
|   |       |   |   |       Tripoli
|   |       |   |   |       Tunis
|   |       |   |   |       Windhoek
|   |       |   |   |       
|   |       |   |   +---America
|   |       |   |   |   |   Adak
|   |       |   |   |   |   Anchorage
|   |       |   |   |   |   Anguilla
|   |       |   |   |   |   Antigua
|   |       |   |   |   |   Araguaina
|   |       |   |   |   |   Aruba
|   |       |   |   |   |   Asuncion
|   |       |   |   |   |   Atikokan
|   |       |   |   |   |   Atka
|   |       |   |   |   |   Bahia
|   |       |   |   |   |   Bahia_Banderas
|   |       |   |   |   |   Barbados
|   |       |   |   |   |   Belem
|   |       |   |   |   |   Belize
|   |       |   |   |   |   Blanc-Sablon
|   |       |   |   |   |   Boa_Vista
|   |       |   |   |   |   Bogota
|   |       |   |   |   |   Boise
|   |       |   |   |   |   Buenos_Aires
|   |       |   |   |   |   Cambridge_Bay
|   |       |   |   |   |   Campo_Grande
|   |       |   |   |   |   Cancun
|   |       |   |   |   |   Caracas
|   |       |   |   |   |   Catamarca
|   |       |   |   |   |   Cayenne
|   |       |   |   |   |   Cayman
|   |       |   |   |   |   Chicago
|   |       |   |   |   |   Chihuahua
|   |       |   |   |   |   Ciudad_Juarez
|   |       |   |   |   |   Coral_Harbour
|   |       |   |   |   |   Cordoba
|   |       |   |   |   |   Costa_Rica
|   |       |   |   |   |   Coyhaique
|   |       |   |   |   |   Creston
|   |       |   |   |   |   Cuiaba
|   |       |   |   |   |   Curacao
|   |       |   |   |   |   Danmarkshavn
|   |       |   |   |   |   Dawson
|   |       |   |   |   |   Dawson_Creek
|   |       |   |   |   |   Denver
|   |       |   |   |   |   Detroit
|   |       |   |   |   |   Dominica
|   |       |   |   |   |   Edmonton
|   |       |   |   |   |   Eirunepe
|   |       |   |   |   |   El_Salvador
|   |       |   |   |   |   Ensenada
|   |       |   |   |   |   Fortaleza
|   |       |   |   |   |   Fort_Nelson
|   |       |   |   |   |   Fort_Wayne
|   |       |   |   |   |   Glace_Bay
|   |       |   |   |   |   Godthab
|   |       |   |   |   |   Goose_Bay
|   |       |   |   |   |   Grand_Turk
|   |       |   |   |   |   Grenada
|   |       |   |   |   |   Guadeloupe
|   |       |   |   |   |   Guatemala
|   |       |   |   |   |   Guayaquil
|   |       |   |   |   |   Guyana
|   |       |   |   |   |   Halifax
|   |       |   |   |   |   Havana
|   |       |   |   |   |   Hermosillo
|   |       |   |   |   |   Indianapolis
|   |       |   |   |   |   Inuvik
|   |       |   |   |   |   Iqaluit
|   |       |   |   |   |   Jamaica
|   |       |   |   |   |   Jujuy
|   |       |   |   |   |   Juneau
|   |       |   |   |   |   Knox_IN
|   |       |   |   |   |   Kralendijk
|   |       |   |   |   |   La_Paz
|   |       |   |   |   |   Lima
|   |       |   |   |   |   Los_Angeles
|   |       |   |   |   |   Louisville
|   |       |   |   |   |   Lower_Princes
|   |       |   |   |   |   Maceio
|   |       |   |   |   |   Managua
|   |       |   |   |   |   Manaus
|   |       |   |   |   |   Marigot
|   |       |   |   |   |   Martinique
|   |       |   |   |   |   Matamoros
|   |       |   |   |   |   Mazatlan
|   |       |   |   |   |   Mendoza
|   |       |   |   |   |   Menominee
|   |       |   |   |   |   Merida
|   |       |   |   |   |   Metlakatla
|   |       |   |   |   |   Mexico_City
|   |       |   |   |   |   Miquelon
|   |       |   |   |   |   Moncton
|   |       |   |   |   |   Monterrey
|   |       |   |   |   |   Montevideo
|   |       |   |   |   |   Montreal
|   |       |   |   |   |   Montserrat
|   |       |   |   |   |   Nassau
|   |       |   |   |   |   New_York
|   |       |   |   |   |   Nipigon
|   |       |   |   |   |   Nome
|   |       |   |   |   |   Noronha
|   |       |   |   |   |   Nuuk
|   |       |   |   |   |   Ojinaga
|   |       |   |   |   |   Panama
|   |       |   |   |   |   Pangnirtung
|   |       |   |   |   |   Paramaribo
|   |       |   |   |   |   Phoenix
|   |       |   |   |   |   Port-au-Prince
|   |       |   |   |   |   Porto_Acre
|   |       |   |   |   |   Porto_Velho
|   |       |   |   |   |   Port_of_Spain
|   |       |   |   |   |   Puerto_Rico
|   |       |   |   |   |   Punta_Arenas
|   |       |   |   |   |   Rainy_River
|   |       |   |   |   |   Rankin_Inlet
|   |       |   |   |   |   Recife
|   |       |   |   |   |   Regina
|   |       |   |   |   |   Resolute
|   |       |   |   |   |   Rio_Branco
|   |       |   |   |   |   Rosario
|   |       |   |   |   |   Santarem
|   |       |   |   |   |   Santa_Isabel
|   |       |   |   |   |   Santiago
|   |       |   |   |   |   Santo_Domingo
|   |       |   |   |   |   Sao_Paulo
|   |       |   |   |   |   Scoresbysund
|   |       |   |   |   |   Shiprock
|   |       |   |   |   |   Sitka
|   |       |   |   |   |   St_Barthelemy
|   |       |   |   |   |   St_Johns
|   |       |   |   |   |   St_Kitts
|   |       |   |   |   |   St_Lucia
|   |       |   |   |   |   St_Thomas
|   |       |   |   |   |   St_Vincent
|   |       |   |   |   |   Swift_Current
|   |       |   |   |   |   Tegucigalpa
|   |       |   |   |   |   Thule
|   |       |   |   |   |   Thunder_Bay
|   |       |   |   |   |   Tijuana
|   |       |   |   |   |   Toronto
|   |       |   |   |   |   Tortola
|   |       |   |   |   |   Vancouver
|   |       |   |   |   |   Virgin
|   |       |   |   |   |   Whitehorse
|   |       |   |   |   |   Winnipeg
|   |       |   |   |   |   Yakutat
|   |       |   |   |   |   Yellowknife
|   |       |   |   |   |   
|   |       |   |   |   +---Argentina
|   |       |   |   |   |       Buenos_Aires
|   |       |   |   |   |       Catamarca
|   |       |   |   |   |       ComodRivadavia
|   |       |   |   |   |       Cordoba
|   |       |   |   |   |       Jujuy
|   |       |   |   |   |       La_Rioja
|   |       |   |   |   |       Mendoza
|   |       |   |   |   |       Rio_Gallegos
|   |       |   |   |   |       Salta
|   |       |   |   |   |       San_Juan
|   |       |   |   |   |       San_Luis
|   |       |   |   |   |       Tucuman
|   |       |   |   |   |       Ushuaia
|   |       |   |   |   |       
|   |       |   |   |   +---Indiana
|   |       |   |   |   |       Indianapolis
|   |       |   |   |   |       Knox
|   |       |   |   |   |       Marengo
|   |       |   |   |   |       Petersburg
|   |       |   |   |   |       Tell_City
|   |       |   |   |   |       Vevay
|   |       |   |   |   |       Vincennes
|   |       |   |   |   |       Winamac
|   |       |   |   |   |       
|   |       |   |   |   +---Kentucky
|   |       |   |   |   |       Louisville
|   |       |   |   |   |       Monticello
|   |       |   |   |   |       
|   |       |   |   |   \---North_Dakota
|   |       |   |   |           Beulah
|   |       |   |   |           Center
|   |       |   |   |           New_Salem
|   |       |   |   |           
|   |       |   |   +---Antarctica
|   |       |   |   |       Casey
|   |       |   |   |       Davis
|   |       |   |   |       DumontDUrville
|   |       |   |   |       Macquarie
|   |       |   |   |       Mawson
|   |       |   |   |       McMurdo
|   |       |   |   |       Palmer
|   |       |   |   |       Rothera
|   |       |   |   |       South_Pole
|   |       |   |   |       Syowa
|   |       |   |   |       Troll
|   |       |   |   |       Vostok
|   |       |   |   |       
|   |       |   |   +---Arctic
|   |       |   |   |       Longyearbyen
|   |       |   |   |       
|   |       |   |   +---Asia
|   |       |   |   |       Aden
|   |       |   |   |       Almaty
|   |       |   |   |       Amman
|   |       |   |   |       Anadyr
|   |       |   |   |       Aqtau
|   |       |   |   |       Aqtobe
|   |       |   |   |       Ashgabat
|   |       |   |   |       Ashkhabad
|   |       |   |   |       Atyrau
|   |       |   |   |       Baghdad
|   |       |   |   |       Bahrain
|   |       |   |   |       Baku
|   |       |   |   |       Bangkok
|   |       |   |   |       Barnaul
|   |       |   |   |       Beirut
|   |       |   |   |       Bishkek
|   |       |   |   |       Brunei
|   |       |   |   |       Calcutta
|   |       |   |   |       Chita
|   |       |   |   |       Choibalsan
|   |       |   |   |       Chongqing
|   |       |   |   |       Chungking
|   |       |   |   |       Colombo
|   |       |   |   |       Dacca
|   |       |   |   |       Damascus
|   |       |   |   |       Dhaka
|   |       |   |   |       Dili
|   |       |   |   |       Dubai
|   |       |   |   |       Dushanbe
|   |       |   |   |       Famagusta
|   |       |   |   |       Gaza
|   |       |   |   |       Harbin
|   |       |   |   |       Hebron
|   |       |   |   |       Hong_Kong
|   |       |   |   |       Hovd
|   |       |   |   |       Ho_Chi_Minh
|   |       |   |   |       Irkutsk
|   |       |   |   |       Istanbul
|   |       |   |   |       Jakarta
|   |       |   |   |       Jayapura
|   |       |   |   |       Jerusalem
|   |       |   |   |       Kabul
|   |       |   |   |       Kamchatka
|   |       |   |   |       Karachi
|   |       |   |   |       Kashgar
|   |       |   |   |       Kathmandu
|   |       |   |   |       Katmandu
|   |       |   |   |       Khandyga
|   |       |   |   |       Kolkata
|   |       |   |   |       Krasnoyarsk
|   |       |   |   |       Kuala_Lumpur
|   |       |   |   |       Kuching
|   |       |   |   |       Kuwait
|   |       |   |   |       Macao
|   |       |   |   |       Macau
|   |       |   |   |       Magadan
|   |       |   |   |       Makassar
|   |       |   |   |       Manila
|   |       |   |   |       Muscat
|   |       |   |   |       Nicosia
|   |       |   |   |       Novokuznetsk
|   |       |   |   |       Novosibirsk
|   |       |   |   |       Omsk
|   |       |   |   |       Oral
|   |       |   |   |       Phnom_Penh
|   |       |   |   |       Pontianak
|   |       |   |   |       Pyongyang
|   |       |   |   |       Qatar
|   |       |   |   |       Qostanay
|   |       |   |   |       Qyzylorda
|   |       |   |   |       Rangoon
|   |       |   |   |       Riyadh
|   |       |   |   |       Saigon
|   |       |   |   |       Sakhalin
|   |       |   |   |       Samarkand
|   |       |   |   |       Seoul
|   |       |   |   |       Shanghai
|   |       |   |   |       Singapore
|   |       |   |   |       Srednekolymsk
|   |       |   |   |       Taipei
|   |       |   |   |       Tashkent
|   |       |   |   |       Tbilisi
|   |       |   |   |       Tehran
|   |       |   |   |       Tel_Aviv
|   |       |   |   |       Thimbu
|   |       |   |   |       Thimphu
|   |       |   |   |       Tokyo
|   |       |   |   |       Tomsk
|   |       |   |   |       Ujung_Pandang
|   |       |   |   |       Ulaanbaatar
|   |       |   |   |       Ulan_Bator
|   |       |   |   |       Urumqi
|   |       |   |   |       Ust-Nera
|   |       |   |   |       Vientiane
|   |       |   |   |       Vladivostok
|   |       |   |   |       Yakutsk
|   |       |   |   |       Yangon
|   |       |   |   |       Yekaterinburg
|   |       |   |   |       Yerevan
|   |       |   |   |       
|   |       |   |   +---Atlantic
|   |       |   |   |       Azores
|   |       |   |   |       Bermuda
|   |       |   |   |       Canary
|   |       |   |   |       Cape_Verde
|   |       |   |   |       Faeroe
|   |       |   |   |       Faroe
|   |       |   |   |       Jan_Mayen
|   |       |   |   |       Madeira
|   |       |   |   |       Reykjavik
|   |       |   |   |       South_Georgia
|   |       |   |   |       Stanley
|   |       |   |   |       St_Helena
|   |       |   |   |       
|   |       |   |   +---Australia
|   |       |   |   |       ACT
|   |       |   |   |       Adelaide
|   |       |   |   |       Brisbane
|   |       |   |   |       Broken_Hill
|   |       |   |   |       Canberra
|   |       |   |   |       Currie
|   |       |   |   |       Darwin
|   |       |   |   |       Eucla
|   |       |   |   |       Hobart
|   |       |   |   |       LHI
|   |       |   |   |       Lindeman
|   |       |   |   |       Lord_Howe
|   |       |   |   |       Melbourne
|   |       |   |   |       North
|   |       |   |   |       NSW
|   |       |   |   |       Perth
|   |       |   |   |       Queensland
|   |       |   |   |       South
|   |       |   |   |       Sydney
|   |       |   |   |       Tasmania
|   |       |   |   |       Victoria
|   |       |   |   |       West
|   |       |   |   |       Yancowinna
|   |       |   |   |       
|   |       |   |   +---Brazil
|   |       |   |   |       Acre
|   |       |   |   |       DeNoronha
|   |       |   |   |       East
|   |       |   |   |       West
|   |       |   |   |       
|   |       |   |   +---Canada
|   |       |   |   |       Atlantic
|   |       |   |   |       Central
|   |       |   |   |       Eastern
|   |       |   |   |       Mountain
|   |       |   |   |       Newfoundland
|   |       |   |   |       Pacific
|   |       |   |   |       Saskatchewan
|   |       |   |   |       Yukon
|   |       |   |   |       
|   |       |   |   +---Chile
|   |       |   |   |       Continental
|   |       |   |   |       EasterIsland
|   |       |   |   |       
|   |       |   |   +---Etc
|   |       |   |   |       GMT
|   |       |   |   |       GMT+0
|   |       |   |   |       GMT+1
|   |       |   |   |       GMT+10
|   |       |   |   |       GMT+11
|   |       |   |   |       GMT+12
|   |       |   |   |       GMT+2
|   |       |   |   |       GMT+3
|   |       |   |   |       GMT+4
|   |       |   |   |       GMT+5
|   |       |   |   |       GMT+6
|   |       |   |   |       GMT+7
|   |       |   |   |       GMT+8
|   |       |   |   |       GMT+9
|   |       |   |   |       GMT-0
|   |       |   |   |       GMT-1
|   |       |   |   |       GMT-10
|   |       |   |   |       GMT-11
|   |       |   |   |       GMT-12
|   |       |   |   |       GMT-13
|   |       |   |   |       GMT-14
|   |       |   |   |       GMT-2
|   |       |   |   |       GMT-3
|   |       |   |   |       GMT-4
|   |       |   |   |       GMT-5
|   |       |   |   |       GMT-6
|   |       |   |   |       GMT-7
|   |       |   |   |       GMT-8
|   |       |   |   |       GMT-9
|   |       |   |   |       GMT0
|   |       |   |   |       Greenwich
|   |       |   |   |       UCT
|   |       |   |   |       Universal
|   |       |   |   |       UTC
|   |       |   |   |       Zulu
|   |       |   |   |       
|   |       |   |   +---Europe
|   |       |   |   |       Amsterdam
|   |       |   |   |       Andorra
|   |       |   |   |       Astrakhan
|   |       |   |   |       Athens
|   |       |   |   |       Belfast
|   |       |   |   |       Belgrade
|   |       |   |   |       Berlin
|   |       |   |   |       Bratislava
|   |       |   |   |       Brussels
|   |       |   |   |       Bucharest
|   |       |   |   |       Budapest
|   |       |   |   |       Busingen
|   |       |   |   |       Chisinau
|   |       |   |   |       Copenhagen
|   |       |   |   |       Dublin
|   |       |   |   |       Gibraltar
|   |       |   |   |       Guernsey
|   |       |   |   |       Helsinki
|   |       |   |   |       Isle_of_Man
|   |       |   |   |       Istanbul
|   |       |   |   |       Jersey
|   |       |   |   |       Kaliningrad
|   |       |   |   |       Kiev
|   |       |   |   |       Kirov
|   |       |   |   |       Kyiv
|   |       |   |   |       Lisbon
|   |       |   |   |       Ljubljana
|   |       |   |   |       London
|   |       |   |   |       Luxembourg
|   |       |   |   |       Madrid
|   |       |   |   |       Malta
|   |       |   |   |       Mariehamn
|   |       |   |   |       Minsk
|   |       |   |   |       Monaco
|   |       |   |   |       Moscow
|   |       |   |   |       Nicosia
|   |       |   |   |       Oslo
|   |       |   |   |       Paris
|   |       |   |   |       Podgorica
|   |       |   |   |       Prague
|   |       |   |   |       Riga
|   |       |   |   |       Rome
|   |       |   |   |       Samara
|   |       |   |   |       San_Marino
|   |       |   |   |       Sarajevo
|   |       |   |   |       Saratov
|   |       |   |   |       Simferopol
|   |       |   |   |       Skopje
|   |       |   |   |       Sofia
|   |       |   |   |       Stockholm
|   |       |   |   |       Tallinn
|   |       |   |   |       Tirane
|   |       |   |   |       Tiraspol
|   |       |   |   |       Ulyanovsk
|   |       |   |   |       Uzhgorod
|   |       |   |   |       Vaduz
|   |       |   |   |       Vatican
|   |       |   |   |       Vienna
|   |       |   |   |       Vilnius
|   |       |   |   |       Volgograd
|   |       |   |   |       Warsaw
|   |       |   |   |       Zagreb
|   |       |   |   |       Zaporozhye
|   |       |   |   |       Zurich
|   |       |   |   |       
|   |       |   |   +---Indian
|   |       |   |   |       Antananarivo
|   |       |   |   |       Chagos
|   |       |   |   |       Christmas
|   |       |   |   |       Cocos
|   |       |   |   |       Comoro
|   |       |   |   |       Kerguelen
|   |       |   |   |       Mahe
|   |       |   |   |       Maldives
|   |       |   |   |       Mauritius
|   |       |   |   |       Mayotte
|   |       |   |   |       Reunion
|   |       |   |   |       
|   |       |   |   +---Mexico
|   |       |   |   |       BajaNorte
|   |       |   |   |       BajaSur
|   |       |   |   |       General
|   |       |   |   |       
|   |       |   |   +---Pacific
|   |       |   |   |       Apia
|   |       |   |   |       Auckland
|   |       |   |   |       Bougainville
|   |       |   |   |       Chatham
|   |       |   |   |       Chuuk
|   |       |   |   |       Easter
|   |       |   |   |       Efate
|   |       |   |   |       Enderbury
|   |       |   |   |       Fakaofo
|   |       |   |   |       Fiji
|   |       |   |   |       Funafuti
|   |       |   |   |       Galapagos
|   |       |   |   |       Gambier
|   |       |   |   |       Guadalcanal
|   |       |   |   |       Guam
|   |       |   |   |       Honolulu
|   |       |   |   |       Johnston
|   |       |   |   |       Kanton
|   |       |   |   |       Kiritimati
|   |       |   |   |       Kosrae
|   |       |   |   |       Kwajalein
|   |       |   |   |       Majuro
|   |       |   |   |       Marquesas
|   |       |   |   |       Midway
|   |       |   |   |       Nauru
|   |       |   |   |       Niue
|   |       |   |   |       Norfolk
|   |       |   |   |       Noumea
|   |       |   |   |       Pago_Pago
|   |       |   |   |       Palau
|   |       |   |   |       Pitcairn
|   |       |   |   |       Pohnpei
|   |       |   |   |       Ponape
|   |       |   |   |       Port_Moresby
|   |       |   |   |       Rarotonga
|   |       |   |   |       Saipan
|   |       |   |   |       Samoa
|   |       |   |   |       Tahiti
|   |       |   |   |       Tarawa
|   |       |   |   |       Tongatapu
|   |       |   |   |       Truk
|   |       |   |   |       Wake
|   |       |   |   |       Wallis
|   |       |   |   |       Yap
|   |       |   |   |       
|   |       |   |   \---US
|   |       |   |           Alaska
|   |       |   |           Aleutian
|   |       |   |           Arizona
|   |       |   |           Central
|   |       |   |           East-Indiana
|   |       |   |           Eastern
|   |       |   |           Hawaii
|   |       |   |           Indiana-Starke
|   |       |   |           Michigan
|   |       |   |           Mountain
|   |       |   |           Pacific
|   |       |   |           Samoa
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           exceptions.cpython-310.pyc
|   |       |           lazy.cpython-310.pyc
|   |       |           reference.cpython-310.pyc
|   |       |           tzfile.cpython-310.pyc
|   |       |           tzinfo.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---pytz-2026.1.post1.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE.txt
|   |       |       METADATA
|   |       |       RECORD
|   |       |       top_level.txt
|   |       |       WHEEL
|   |       |       zip-safe
|   |       |       
|   |       +---rich
|   |       |   |   abc.py
|   |       |   |   align.py
|   |       |   |   ansi.py
|   |       |   |   bar.py
|   |       |   |   box.py
|   |       |   |   cells.py
|   |       |   |   color.py
|   |       |   |   color_triplet.py
|   |       |   |   columns.py
|   |       |   |   console.py
|   |       |   |   constrain.py
|   |       |   |   containers.py
|   |       |   |   control.py
|   |       |   |   default_styles.py
|   |       |   |   diagnose.py
|   |       |   |   emoji.py
|   |       |   |   errors.py
|   |       |   |   filesize.py
|   |       |   |   file_proxy.py
|   |       |   |   highlighter.py
|   |       |   |   json.py
|   |       |   |   jupyter.py
|   |       |   |   layout.py
|   |       |   |   live.py
|   |       |   |   live_render.py
|   |       |   |   logging.py
|   |       |   |   markdown.py
|   |       |   |   markup.py
|   |       |   |   measure.py
|   |       |   |   padding.py
|   |       |   |   pager.py
|   |       |   |   palette.py
|   |       |   |   panel.py
|   |       |   |   pretty.py
|   |       |   |   progress.py
|   |       |   |   progress_bar.py
|   |       |   |   prompt.py
|   |       |   |   protocol.py
|   |       |   |   py.typed
|   |       |   |   region.py
|   |       |   |   repr.py
|   |       |   |   rule.py
|   |       |   |   scope.py
|   |       |   |   screen.py
|   |       |   |   segment.py
|   |       |   |   spinner.py
|   |       |   |   status.py
|   |       |   |   style.py
|   |       |   |   styled.py
|   |       |   |   syntax.py
|   |       |   |   table.py
|   |       |   |   terminal_theme.py
|   |       |   |   text.py
|   |       |   |   theme.py
|   |       |   |   themes.py
|   |       |   |   traceback.py
|   |       |   |   tree.py
|   |       |   |   _emoji_codes.py
|   |       |   |   _emoji_replace.py
|   |       |   |   _export_format.py
|   |       |   |   _extension.py
|   |       |   |   _fileno.py
|   |       |   |   _inspect.py
|   |       |   |   _log_render.py
|   |       |   |   _loop.py
|   |       |   |   _null_file.py
|   |       |   |   _palettes.py
|   |       |   |   _pick.py
|   |       |   |   _ratio.py
|   |       |   |   _spinners.py
|   |       |   |   _stack.py
|   |       |   |   _timer.py
|   |       |   |   _win32_console.py
|   |       |   |   _windows.py
|   |       |   |   _windows_renderer.py
|   |       |   |   _wrap.py
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   +---_unicode_data
|   |       |   |   |   unicode10-0-0.py
|   |       |   |   |   unicode11-0-0.py
|   |       |   |   |   unicode12-0-0.py
|   |       |   |   |   unicode12-1-0.py
|   |       |   |   |   unicode13-0-0.py
|   |       |   |   |   unicode14-0-0.py
|   |       |   |   |   unicode15-0-0.py
|   |       |   |   |   unicode15-1-0.py
|   |       |   |   |   unicode16-0-0.py
|   |       |   |   |   unicode17-0-0.py
|   |       |   |   |   unicode4-1-0.py
|   |       |   |   |   unicode5-0-0.py
|   |       |   |   |   unicode5-1-0.py
|   |       |   |   |   unicode5-2-0.py
|   |       |   |   |   unicode6-0-0.py
|   |       |   |   |   unicode6-1-0.py
|   |       |   |   |   unicode6-2-0.py
|   |       |   |   |   unicode6-3-0.py
|   |       |   |   |   unicode7-0-0.py
|   |       |   |   |   unicode8-0-0.py
|   |       |   |   |   unicode9-0-0.py
|   |       |   |   |   _versions.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           unicode10-0-0.cpython-310.pyc
|   |       |   |           unicode11-0-0.cpython-310.pyc
|   |       |   |           unicode12-0-0.cpython-310.pyc
|   |       |   |           unicode12-1-0.cpython-310.pyc
|   |       |   |           unicode13-0-0.cpython-310.pyc
|   |       |   |           unicode14-0-0.cpython-310.pyc
|   |       |   |           unicode15-0-0.cpython-310.pyc
|   |       |   |           unicode15-1-0.cpython-310.pyc
|   |       |   |           unicode16-0-0.cpython-310.pyc
|   |       |   |           unicode17-0-0.cpython-310.pyc
|   |       |   |           unicode4-1-0.cpython-310.pyc
|   |       |   |           unicode5-0-0.cpython-310.pyc
|   |       |   |           unicode5-1-0.cpython-310.pyc
|   |       |   |           unicode5-2-0.cpython-310.pyc
|   |       |   |           unicode6-0-0.cpython-310.pyc
|   |       |   |           unicode6-1-0.cpython-310.pyc
|   |       |   |           unicode6-2-0.cpython-310.pyc
|   |       |   |           unicode6-3-0.cpython-310.pyc
|   |       |   |           unicode7-0-0.cpython-310.pyc
|   |       |   |           unicode8-0-0.cpython-310.pyc
|   |       |   |           unicode9-0-0.cpython-310.pyc
|   |       |   |           _versions.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           abc.cpython-310.pyc
|   |       |           align.cpython-310.pyc
|   |       |           ansi.cpython-310.pyc
|   |       |           bar.cpython-310.pyc
|   |       |           box.cpython-310.pyc
|   |       |           cells.cpython-310.pyc
|   |       |           color.cpython-310.pyc
|   |       |           color_triplet.cpython-310.pyc
|   |       |           columns.cpython-310.pyc
|   |       |           console.cpython-310.pyc
|   |       |           constrain.cpython-310.pyc
|   |       |           containers.cpython-310.pyc
|   |       |           control.cpython-310.pyc
|   |       |           default_styles.cpython-310.pyc
|   |       |           diagnose.cpython-310.pyc
|   |       |           emoji.cpython-310.pyc
|   |       |           errors.cpython-310.pyc
|   |       |           filesize.cpython-310.pyc
|   |       |           file_proxy.cpython-310.pyc
|   |       |           highlighter.cpython-310.pyc
|   |       |           json.cpython-310.pyc
|   |       |           jupyter.cpython-310.pyc
|   |       |           layout.cpython-310.pyc
|   |       |           live.cpython-310.pyc
|   |       |           live_render.cpython-310.pyc
|   |       |           logging.cpython-310.pyc
|   |       |           markdown.cpython-310.pyc
|   |       |           markup.cpython-310.pyc
|   |       |           measure.cpython-310.pyc
|   |       |           padding.cpython-310.pyc
|   |       |           pager.cpython-310.pyc
|   |       |           palette.cpython-310.pyc
|   |       |           panel.cpython-310.pyc
|   |       |           pretty.cpython-310.pyc
|   |       |           progress.cpython-310.pyc
|   |       |           progress_bar.cpython-310.pyc
|   |       |           prompt.cpython-310.pyc
|   |       |           protocol.cpython-310.pyc
|   |       |           region.cpython-310.pyc
|   |       |           repr.cpython-310.pyc
|   |       |           rule.cpython-310.pyc
|   |       |           scope.cpython-310.pyc
|   |       |           screen.cpython-310.pyc
|   |       |           segment.cpython-310.pyc
|   |       |           spinner.cpython-310.pyc
|   |       |           status.cpython-310.pyc
|   |       |           style.cpython-310.pyc
|   |       |           styled.cpython-310.pyc
|   |       |           syntax.cpython-310.pyc
|   |       |           table.cpython-310.pyc
|   |       |           terminal_theme.cpython-310.pyc
|   |       |           text.cpython-310.pyc
|   |       |           theme.cpython-310.pyc
|   |       |           themes.cpython-310.pyc
|   |       |           traceback.cpython-310.pyc
|   |       |           tree.cpython-310.pyc
|   |       |           _emoji_codes.cpython-310.pyc
|   |       |           _emoji_replace.cpython-310.pyc
|   |       |           _export_format.cpython-310.pyc
|   |       |           _extension.cpython-310.pyc
|   |       |           _fileno.cpython-310.pyc
|   |       |           _inspect.cpython-310.pyc
|   |       |           _log_render.cpython-310.pyc
|   |       |           _loop.cpython-310.pyc
|   |       |           _null_file.cpython-310.pyc
|   |       |           _palettes.cpython-310.pyc
|   |       |           _pick.cpython-310.pyc
|   |       |           _ratio.cpython-310.pyc
|   |       |           _spinners.cpython-310.pyc
|   |       |           _stack.cpython-310.pyc
|   |       |           _timer.cpython-310.pyc
|   |       |           _win32_console.cpython-310.pyc
|   |       |           _windows.cpython-310.pyc
|   |       |           _windows_renderer.cpython-310.pyc
|   |       |           _wrap.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           __main__.cpython-310.pyc
|   |       |           
|   |       +---rich-15.0.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---ruff
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           __init__.cpython-310.pyc
|   |       |           __main__.cpython-310.pyc
|   |       |           
|   |       +---ruff-0.6.9.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---setuptools
|   |       |   |   archive_util.py
|   |       |   |   build_meta.py
|   |       |   |   cli-32.exe
|   |       |   |   cli-64.exe
|   |       |   |   cli-arm64.exe
|   |       |   |   cli.exe
|   |       |   |   depends.py
|   |       |   |   dep_util.py
|   |       |   |   discovery.py
|   |       |   |   dist.py
|   |       |   |   errors.py
|   |       |   |   extension.py
|   |       |   |   glob.py
|   |       |   |   gui-32.exe
|   |       |   |   gui-64.exe
|   |       |   |   gui-arm64.exe
|   |       |   |   gui.exe
|   |       |   |   installer.py
|   |       |   |   launch.py
|   |       |   |   logging.py
|   |       |   |   monkey.py
|   |       |   |   msvc.py
|   |       |   |   namespaces.py
|   |       |   |   package_index.py
|   |       |   |   py34compat.py
|   |       |   |   sandbox.py
|   |       |   |   script (dev).tmpl
|   |       |   |   script.tmpl
|   |       |   |   unicode_utils.py
|   |       |   |   version.py
|   |       |   |   wheel.py
|   |       |   |   windows_support.py
|   |       |   |   _deprecation_warning.py
|   |       |   |   _entry_points.py
|   |       |   |   _imp.py
|   |       |   |   _importlib.py
|   |       |   |   _itertools.py
|   |       |   |   _path.py
|   |       |   |   _reqs.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---command
|   |       |   |   |   alias.py
|   |       |   |   |   bdist_egg.py
|   |       |   |   |   bdist_rpm.py
|   |       |   |   |   build.py
|   |       |   |   |   build_clib.py
|   |       |   |   |   build_ext.py
|   |       |   |   |   build_py.py
|   |       |   |   |   develop.py
|   |       |   |   |   dist_info.py
|   |       |   |   |   easy_install.py
|   |       |   |   |   editable_wheel.py
|   |       |   |   |   egg_info.py
|   |       |   |   |   install.py
|   |       |   |   |   install_egg_info.py
|   |       |   |   |   install_lib.py
|   |       |   |   |   install_scripts.py
|   |       |   |   |   launcher manifest.xml
|   |       |   |   |   py36compat.py
|   |       |   |   |   register.py
|   |       |   |   |   rotate.py
|   |       |   |   |   saveopts.py
|   |       |   |   |   sdist.py
|   |       |   |   |   setopt.py
|   |       |   |   |   test.py
|   |       |   |   |   upload.py
|   |       |   |   |   upload_docs.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           alias.cpython-310.pyc
|   |       |   |           bdist_egg.cpython-310.pyc
|   |       |   |           bdist_rpm.cpython-310.pyc
|   |       |   |           build.cpython-310.pyc
|   |       |   |           build_clib.cpython-310.pyc
|   |       |   |           build_ext.cpython-310.pyc
|   |       |   |           build_py.cpython-310.pyc
|   |       |   |           develop.cpython-310.pyc
|   |       |   |           dist_info.cpython-310.pyc
|   |       |   |           easy_install.cpython-310.pyc
|   |       |   |           editable_wheel.cpython-310.pyc
|   |       |   |           egg_info.cpython-310.pyc
|   |       |   |           install.cpython-310.pyc
|   |       |   |           install_egg_info.cpython-310.pyc
|   |       |   |           install_lib.cpython-310.pyc
|   |       |   |           install_scripts.cpython-310.pyc
|   |       |   |           py36compat.cpython-310.pyc
|   |       |   |           register.cpython-310.pyc
|   |       |   |           rotate.cpython-310.pyc
|   |       |   |           saveopts.cpython-310.pyc
|   |       |   |           sdist.cpython-310.pyc
|   |       |   |           setopt.cpython-310.pyc
|   |       |   |           test.cpython-310.pyc
|   |       |   |           upload.cpython-310.pyc
|   |       |   |           upload_docs.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---config
|   |       |   |   |   expand.py
|   |       |   |   |   pyprojecttoml.py
|   |       |   |   |   setupcfg.py
|   |       |   |   |   _apply_pyprojecttoml.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---_validate_pyproject
|   |       |   |   |   |   error_reporting.py
|   |       |   |   |   |   extra_validations.py
|   |       |   |   |   |   fastjsonschema_exceptions.py
|   |       |   |   |   |   fastjsonschema_validations.py
|   |       |   |   |   |   formats.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           error_reporting.cpython-310.pyc
|   |       |   |   |           extra_validations.cpython-310.pyc
|   |       |   |   |           fastjsonschema_exceptions.cpython-310.pyc
|   |       |   |   |           fastjsonschema_validations.cpython-310.pyc
|   |       |   |   |           formats.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           expand.cpython-310.pyc
|   |       |   |           pyprojecttoml.cpython-310.pyc
|   |       |   |           setupcfg.cpython-310.pyc
|   |       |   |           _apply_pyprojecttoml.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---extern
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_distutils
|   |       |   |   |   archive_util.py
|   |       |   |   |   bcppcompiler.py
|   |       |   |   |   ccompiler.py
|   |       |   |   |   cmd.py
|   |       |   |   |   config.py
|   |       |   |   |   core.py
|   |       |   |   |   cygwinccompiler.py
|   |       |   |   |   debug.py
|   |       |   |   |   dep_util.py
|   |       |   |   |   dir_util.py
|   |       |   |   |   dist.py
|   |       |   |   |   errors.py
|   |       |   |   |   extension.py
|   |       |   |   |   fancy_getopt.py
|   |       |   |   |   filelist.py
|   |       |   |   |   file_util.py
|   |       |   |   |   log.py
|   |       |   |   |   msvc9compiler.py
|   |       |   |   |   msvccompiler.py
|   |       |   |   |   py38compat.py
|   |       |   |   |   py39compat.py
|   |       |   |   |   spawn.py
|   |       |   |   |   sysconfig.py
|   |       |   |   |   text_file.py
|   |       |   |   |   unixccompiler.py
|   |       |   |   |   util.py
|   |       |   |   |   version.py
|   |       |   |   |   versionpredicate.py
|   |       |   |   |   _collections.py
|   |       |   |   |   _functools.py
|   |       |   |   |   _macos_compat.py
|   |       |   |   |   _msvccompiler.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---command
|   |       |   |   |   |   bdist.py
|   |       |   |   |   |   bdist_dumb.py
|   |       |   |   |   |   bdist_rpm.py
|   |       |   |   |   |   build.py
|   |       |   |   |   |   build_clib.py
|   |       |   |   |   |   build_ext.py
|   |       |   |   |   |   build_py.py
|   |       |   |   |   |   build_scripts.py
|   |       |   |   |   |   check.py
|   |       |   |   |   |   clean.py
|   |       |   |   |   |   config.py
|   |       |   |   |   |   install.py
|   |       |   |   |   |   install_data.py
|   |       |   |   |   |   install_egg_info.py
|   |       |   |   |   |   install_headers.py
|   |       |   |   |   |   install_lib.py
|   |       |   |   |   |   install_scripts.py
|   |       |   |   |   |   py37compat.py
|   |       |   |   |   |   register.py
|   |       |   |   |   |   sdist.py
|   |       |   |   |   |   upload.py
|   |       |   |   |   |   _framework_compat.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           bdist.cpython-310.pyc
|   |       |   |   |           bdist_dumb.cpython-310.pyc
|   |       |   |   |           bdist_rpm.cpython-310.pyc
|   |       |   |   |           build.cpython-310.pyc
|   |       |   |   |           build_clib.cpython-310.pyc
|   |       |   |   |           build_ext.cpython-310.pyc
|   |       |   |   |           build_py.cpython-310.pyc
|   |       |   |   |           build_scripts.cpython-310.pyc
|   |       |   |   |           check.cpython-310.pyc
|   |       |   |   |           clean.cpython-310.pyc
|   |       |   |   |           config.cpython-310.pyc
|   |       |   |   |           install.cpython-310.pyc
|   |       |   |   |           install_data.cpython-310.pyc
|   |       |   |   |           install_egg_info.cpython-310.pyc
|   |       |   |   |           install_headers.cpython-310.pyc
|   |       |   |   |           install_lib.cpython-310.pyc
|   |       |   |   |           install_scripts.cpython-310.pyc
|   |       |   |   |           py37compat.cpython-310.pyc
|   |       |   |   |           register.cpython-310.pyc
|   |       |   |   |           sdist.cpython-310.pyc
|   |       |   |   |           upload.cpython-310.pyc
|   |       |   |   |           _framework_compat.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           archive_util.cpython-310.pyc
|   |       |   |           bcppcompiler.cpython-310.pyc
|   |       |   |           ccompiler.cpython-310.pyc
|   |       |   |           cmd.cpython-310.pyc
|   |       |   |           config.cpython-310.pyc
|   |       |   |           core.cpython-310.pyc
|   |       |   |           cygwinccompiler.cpython-310.pyc
|   |       |   |           debug.cpython-310.pyc
|   |       |   |           dep_util.cpython-310.pyc
|   |       |   |           dir_util.cpython-310.pyc
|   |       |   |           dist.cpython-310.pyc
|   |       |   |           errors.cpython-310.pyc
|   |       |   |           extension.cpython-310.pyc
|   |       |   |           fancy_getopt.cpython-310.pyc
|   |       |   |           filelist.cpython-310.pyc
|   |       |   |           file_util.cpython-310.pyc
|   |       |   |           log.cpython-310.pyc
|   |       |   |           msvc9compiler.cpython-310.pyc
|   |       |   |           msvccompiler.cpython-310.pyc
|   |       |   |           py38compat.cpython-310.pyc
|   |       |   |           py39compat.cpython-310.pyc
|   |       |   |           spawn.cpython-310.pyc
|   |       |   |           sysconfig.cpython-310.pyc
|   |       |   |           text_file.cpython-310.pyc
|   |       |   |           unixccompiler.cpython-310.pyc
|   |       |   |           util.cpython-310.pyc
|   |       |   |           version.cpython-310.pyc
|   |       |   |           versionpredicate.cpython-310.pyc
|   |       |   |           _collections.cpython-310.pyc
|   |       |   |           _functools.cpython-310.pyc
|   |       |   |           _macos_compat.cpython-310.pyc
|   |       |   |           _msvccompiler.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_vendor
|   |       |   |   |   ordered_set.py
|   |       |   |   |   typing_extensions.py
|   |       |   |   |   zipp.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---importlib_metadata
|   |       |   |   |   |   _adapters.py
|   |       |   |   |   |   _collections.py
|   |       |   |   |   |   _compat.py
|   |       |   |   |   |   _functools.py
|   |       |   |   |   |   _itertools.py
|   |       |   |   |   |   _meta.py
|   |       |   |   |   |   _text.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _adapters.cpython-310.pyc
|   |       |   |   |           _collections.cpython-310.pyc
|   |       |   |   |           _compat.cpython-310.pyc
|   |       |   |   |           _functools.cpython-310.pyc
|   |       |   |   |           _itertools.cpython-310.pyc
|   |       |   |   |           _meta.cpython-310.pyc
|   |       |   |   |           _text.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---importlib_resources
|   |       |   |   |   |   abc.py
|   |       |   |   |   |   readers.py
|   |       |   |   |   |   simple.py
|   |       |   |   |   |   _adapters.py
|   |       |   |   |   |   _common.py
|   |       |   |   |   |   _compat.py
|   |       |   |   |   |   _itertools.py
|   |       |   |   |   |   _legacy.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           abc.cpython-310.pyc
|   |       |   |   |           readers.cpython-310.pyc
|   |       |   |   |           simple.cpython-310.pyc
|   |       |   |   |           _adapters.cpython-310.pyc
|   |       |   |   |           _common.cpython-310.pyc
|   |       |   |   |           _compat.cpython-310.pyc
|   |       |   |   |           _itertools.cpython-310.pyc
|   |       |   |   |           _legacy.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---jaraco
|   |       |   |   |   |   context.py
|   |       |   |   |   |   functools.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---text
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           context.cpython-310.pyc
|   |       |   |   |           functools.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---more_itertools
|   |       |   |   |   |   more.py
|   |       |   |   |   |   recipes.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           more.cpython-310.pyc
|   |       |   |   |           recipes.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---packaging
|   |       |   |   |   |   markers.py
|   |       |   |   |   |   requirements.py
|   |       |   |   |   |   specifiers.py
|   |       |   |   |   |   tags.py
|   |       |   |   |   |   utils.py
|   |       |   |   |   |   version.py
|   |       |   |   |   |   _manylinux.py
|   |       |   |   |   |   _musllinux.py
|   |       |   |   |   |   _structures.py
|   |       |   |   |   |   __about__.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           markers.cpython-310.pyc
|   |       |   |   |           requirements.cpython-310.pyc
|   |       |   |   |           specifiers.cpython-310.pyc
|   |       |   |   |           tags.cpython-310.pyc
|   |       |   |   |           utils.cpython-310.pyc
|   |       |   |   |           version.cpython-310.pyc
|   |       |   |   |           _manylinux.cpython-310.pyc
|   |       |   |   |           _musllinux.cpython-310.pyc
|   |       |   |   |           _structures.cpython-310.pyc
|   |       |   |   |           __about__.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---pyparsing
|   |       |   |   |   |   actions.py
|   |       |   |   |   |   common.py
|   |       |   |   |   |   core.py
|   |       |   |   |   |   exceptions.py
|   |       |   |   |   |   helpers.py
|   |       |   |   |   |   results.py
|   |       |   |   |   |   testing.py
|   |       |   |   |   |   unicode.py
|   |       |   |   |   |   util.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---diagram
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           actions.cpython-310.pyc
|   |       |   |   |           common.cpython-310.pyc
|   |       |   |   |           core.cpython-310.pyc
|   |       |   |   |           exceptions.cpython-310.pyc
|   |       |   |   |           helpers.cpython-310.pyc
|   |       |   |   |           results.cpython-310.pyc
|   |       |   |   |           testing.cpython-310.pyc
|   |       |   |   |           unicode.cpython-310.pyc
|   |       |   |   |           util.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---tomli
|   |       |   |   |   |   _parser.py
|   |       |   |   |   |   _re.py
|   |       |   |   |   |   _types.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _parser.cpython-310.pyc
|   |       |   |   |           _re.cpython-310.pyc
|   |       |   |   |           _types.cpython-310.pyc
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           ordered_set.cpython-310.pyc
|   |       |   |           typing_extensions.cpython-310.pyc
|   |       |   |           zipp.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           archive_util.cpython-310.pyc
|   |       |           build_meta.cpython-310.pyc
|   |       |           depends.cpython-310.pyc
|   |       |           dep_util.cpython-310.pyc
|   |       |           discovery.cpython-310.pyc
|   |       |           dist.cpython-310.pyc
|   |       |           errors.cpython-310.pyc
|   |       |           extension.cpython-310.pyc
|   |       |           glob.cpython-310.pyc
|   |       |           installer.cpython-310.pyc
|   |       |           launch.cpython-310.pyc
|   |       |           logging.cpython-310.pyc
|   |       |           monkey.cpython-310.pyc
|   |       |           msvc.cpython-310.pyc
|   |       |           namespaces.cpython-310.pyc
|   |       |           package_index.cpython-310.pyc
|   |       |           py34compat.cpython-310.pyc
|   |       |           sandbox.cpython-310.pyc
|   |       |           unicode_utils.cpython-310.pyc
|   |       |           version.cpython-310.pyc
|   |       |           wheel.cpython-310.pyc
|   |       |           windows_support.cpython-310.pyc
|   |       |           _deprecation_warning.cpython-310.pyc
|   |       |           _entry_points.cpython-310.pyc
|   |       |           _imp.cpython-310.pyc
|   |       |           _importlib.cpython-310.pyc
|   |       |           _itertools.cpython-310.pyc
|   |       |           _path.cpython-310.pyc
|   |       |           _reqs.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---setuptools-65.5.0.dist-info
|   |       |       entry_points.txt
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       REQUESTED
|   |       |       top_level.txt
|   |       |       WHEEL
|   |       |       
|   |       +---shellingham
|   |       |   |   nt.py
|   |       |   |   _core.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---posix
|   |       |   |   |   proc.py
|   |       |   |   |   ps.py
|   |       |   |   |   _core.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           proc.cpython-310.pyc
|   |       |   |           ps.cpython-310.pyc
|   |       |   |           _core.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           nt.cpython-310.pyc
|   |       |           _core.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---shellingham-1.5.4.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       top_level.txt
|   |       |       WHEEL
|   |       |       zip-safe
|   |       |       
|   |       +---six-1.17.0.dist-info
|   |       |       INSTALLER
|   |       |       LICENSE
|   |       |       METADATA
|   |       |       RECORD
|   |       |       top_level.txt
|   |       |       WHEEL
|   |       |       
|   |       +---structlog
|   |       |   |   contextvars.py
|   |       |   |   dev.py
|   |       |   |   exceptions.py
|   |       |   |   processors.py
|   |       |   |   py.typed
|   |       |   |   stdlib.py
|   |       |   |   testing.py
|   |       |   |   threadlocal.py
|   |       |   |   tracebacks.py
|   |       |   |   twisted.py
|   |       |   |   types.py
|   |       |   |   typing.py
|   |       |   |   _base.py
|   |       |   |   _config.py
|   |       |   |   _frames.py
|   |       |   |   _generic.py
|   |       |   |   _greenlets.py
|   |       |   |   _log_levels.py
|   |       |   |   _native.py
|   |       |   |   _output.py
|   |       |   |   _utils.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           contextvars.cpython-310.pyc
|   |       |           dev.cpython-310.pyc
|   |       |           exceptions.cpython-310.pyc
|   |       |           processors.cpython-310.pyc
|   |       |           stdlib.cpython-310.pyc
|   |       |           testing.cpython-310.pyc
|   |       |           threadlocal.cpython-310.pyc
|   |       |           tracebacks.cpython-310.pyc
|   |       |           twisted.cpython-310.pyc
|   |       |           types.cpython-310.pyc
|   |       |           typing.cpython-310.pyc
|   |       |           _base.cpython-310.pyc
|   |       |           _config.cpython-310.pyc
|   |       |           _frames.cpython-310.pyc
|   |       |           _generic.cpython-310.pyc
|   |       |           _greenlets.cpython-310.pyc
|   |       |           _log_levels.cpython-310.pyc
|   |       |           _native.cpython-310.pyc
|   |       |           _output.cpython-310.pyc
|   |       |           _utils.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---structlog-25.5.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE-APACHE
|   |       |           LICENSE-MIT
|   |       |           NOTICE
|   |       |           
|   |       +---tenacity
|   |       |   |   after.py
|   |       |   |   before.py
|   |       |   |   before_sleep.py
|   |       |   |   nap.py
|   |       |   |   py.typed
|   |       |   |   retry.py
|   |       |   |   stop.py
|   |       |   |   tornadoweb.py
|   |       |   |   wait.py
|   |       |   |   _utils.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---asyncio
|   |       |   |   |   retry.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           retry.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           after.cpython-310.pyc
|   |       |           before.cpython-310.pyc
|   |       |           before_sleep.cpython-310.pyc
|   |       |           nap.cpython-310.pyc
|   |       |           retry.cpython-310.pyc
|   |       |           stop.cpython-310.pyc
|   |       |           tornadoweb.cpython-310.pyc
|   |       |           wait.cpython-310.pyc
|   |       |           _utils.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---tenacity-9.1.4.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---tomli
|   |       |   |   py.typed
|   |       |   |   _parser.py
|   |       |   |   _re.py
|   |       |   |   _types.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           _parser.cpython-310.pyc
|   |       |           _re.cpython-310.pyc
|   |       |           _types.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---tomli-2.4.1.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---typer
|   |       |   |   cli.py
|   |       |   |   colors.py
|   |       |   |   completion.py
|   |       |   |   core.py
|   |       |   |   main.py
|   |       |   |   models.py
|   |       |   |   params.py
|   |       |   |   py.typed
|   |       |   |   rich_utils.py
|   |       |   |   testing.py
|   |       |   |   utils.py
|   |       |   |   _completion_classes.py
|   |       |   |   _completion_shared.py
|   |       |   |   _types.py
|   |       |   |   _typing.py
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           cli.cpython-310.pyc
|   |       |           colors.cpython-310.pyc
|   |       |           completion.cpython-310.pyc
|   |       |           core.cpython-310.pyc
|   |       |           main.cpython-310.pyc
|   |       |           models.cpython-310.pyc
|   |       |           params.cpython-310.pyc
|   |       |           rich_utils.cpython-310.pyc
|   |       |           testing.cpython-310.pyc
|   |       |           utils.cpython-310.pyc
|   |       |           _completion_classes.cpython-310.pyc
|   |       |           _completion_shared.cpython-310.pyc
|   |       |           _types.cpython-310.pyc
|   |       |           _typing.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           __main__.cpython-310.pyc
|   |       |           
|   |       +---typer-0.24.1.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---typing_extensions-4.15.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---typing_inspection
|   |       |   |   introspection.py
|   |       |   |   py.typed
|   |       |   |   typing_objects.py
|   |       |   |   typing_objects.pyi
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           introspection.cpython-310.pyc
|   |       |           typing_objects.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---typing_inspection-0.4.2.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---tzdata
|   |       |   |   zones
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---zoneinfo
|   |       |   |   |   CET
|   |       |   |   |   CST6CDT
|   |       |   |   |   Cuba
|   |       |   |   |   EET
|   |       |   |   |   Egypt
|   |       |   |   |   Eire
|   |       |   |   |   EST
|   |       |   |   |   EST5EDT
|   |       |   |   |   Factory
|   |       |   |   |   GB
|   |       |   |   |   GB-Eire
|   |       |   |   |   GMT
|   |       |   |   |   GMT+0
|   |       |   |   |   GMT-0
|   |       |   |   |   GMT0
|   |       |   |   |   Greenwich
|   |       |   |   |   Hongkong
|   |       |   |   |   HST
|   |       |   |   |   Iceland
|   |       |   |   |   Iran
|   |       |   |   |   iso3166.tab
|   |       |   |   |   Israel
|   |       |   |   |   Jamaica
|   |       |   |   |   Japan
|   |       |   |   |   Kwajalein
|   |       |   |   |   leapseconds
|   |       |   |   |   Libya
|   |       |   |   |   MET
|   |       |   |   |   MST
|   |       |   |   |   MST7MDT
|   |       |   |   |   Navajo
|   |       |   |   |   NZ
|   |       |   |   |   NZ-CHAT
|   |       |   |   |   Poland
|   |       |   |   |   Portugal
|   |       |   |   |   PRC
|   |       |   |   |   PST8PDT
|   |       |   |   |   ROC
|   |       |   |   |   ROK
|   |       |   |   |   Singapore
|   |       |   |   |   Turkey
|   |       |   |   |   tzdata.zi
|   |       |   |   |   UCT
|   |       |   |   |   Universal
|   |       |   |   |   UTC
|   |       |   |   |   W-SU
|   |       |   |   |   WET
|   |       |   |   |   zone.tab
|   |       |   |   |   zone1970.tab
|   |       |   |   |   zonenow.tab
|   |       |   |   |   Zulu
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---Africa
|   |       |   |   |   |   Abidjan
|   |       |   |   |   |   Accra
|   |       |   |   |   |   Addis_Ababa
|   |       |   |   |   |   Algiers
|   |       |   |   |   |   Asmara
|   |       |   |   |   |   Asmera
|   |       |   |   |   |   Bamako
|   |       |   |   |   |   Bangui
|   |       |   |   |   |   Banjul
|   |       |   |   |   |   Bissau
|   |       |   |   |   |   Blantyre
|   |       |   |   |   |   Brazzaville
|   |       |   |   |   |   Bujumbura
|   |       |   |   |   |   Cairo
|   |       |   |   |   |   Casablanca
|   |       |   |   |   |   Ceuta
|   |       |   |   |   |   Conakry
|   |       |   |   |   |   Dakar
|   |       |   |   |   |   Dar_es_Salaam
|   |       |   |   |   |   Djibouti
|   |       |   |   |   |   Douala
|   |       |   |   |   |   El_Aaiun
|   |       |   |   |   |   Freetown
|   |       |   |   |   |   Gaborone
|   |       |   |   |   |   Harare
|   |       |   |   |   |   Johannesburg
|   |       |   |   |   |   Juba
|   |       |   |   |   |   Kampala
|   |       |   |   |   |   Khartoum
|   |       |   |   |   |   Kigali
|   |       |   |   |   |   Kinshasa
|   |       |   |   |   |   Lagos
|   |       |   |   |   |   Libreville
|   |       |   |   |   |   Lome
|   |       |   |   |   |   Luanda
|   |       |   |   |   |   Lubumbashi
|   |       |   |   |   |   Lusaka
|   |       |   |   |   |   Malabo
|   |       |   |   |   |   Maputo
|   |       |   |   |   |   Maseru
|   |       |   |   |   |   Mbabane
|   |       |   |   |   |   Mogadishu
|   |       |   |   |   |   Monrovia
|   |       |   |   |   |   Nairobi
|   |       |   |   |   |   Ndjamena
|   |       |   |   |   |   Niamey
|   |       |   |   |   |   Nouakchott
|   |       |   |   |   |   Ouagadougou
|   |       |   |   |   |   Porto-Novo
|   |       |   |   |   |   Sao_Tome
|   |       |   |   |   |   Timbuktu
|   |       |   |   |   |   Tripoli
|   |       |   |   |   |   Tunis
|   |       |   |   |   |   Windhoek
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---America
|   |       |   |   |   |   Adak
|   |       |   |   |   |   Anchorage
|   |       |   |   |   |   Anguilla
|   |       |   |   |   |   Antigua
|   |       |   |   |   |   Araguaina
|   |       |   |   |   |   Aruba
|   |       |   |   |   |   Asuncion
|   |       |   |   |   |   Atikokan
|   |       |   |   |   |   Atka
|   |       |   |   |   |   Bahia
|   |       |   |   |   |   Bahia_Banderas
|   |       |   |   |   |   Barbados
|   |       |   |   |   |   Belem
|   |       |   |   |   |   Belize
|   |       |   |   |   |   Blanc-Sablon
|   |       |   |   |   |   Boa_Vista
|   |       |   |   |   |   Bogota
|   |       |   |   |   |   Boise
|   |       |   |   |   |   Buenos_Aires
|   |       |   |   |   |   Cambridge_Bay
|   |       |   |   |   |   Campo_Grande
|   |       |   |   |   |   Cancun
|   |       |   |   |   |   Caracas
|   |       |   |   |   |   Catamarca
|   |       |   |   |   |   Cayenne
|   |       |   |   |   |   Cayman
|   |       |   |   |   |   Chicago
|   |       |   |   |   |   Chihuahua
|   |       |   |   |   |   Ciudad_Juarez
|   |       |   |   |   |   Coral_Harbour
|   |       |   |   |   |   Cordoba
|   |       |   |   |   |   Costa_Rica
|   |       |   |   |   |   Coyhaique
|   |       |   |   |   |   Creston
|   |       |   |   |   |   Cuiaba
|   |       |   |   |   |   Curacao
|   |       |   |   |   |   Danmarkshavn
|   |       |   |   |   |   Dawson
|   |       |   |   |   |   Dawson_Creek
|   |       |   |   |   |   Denver
|   |       |   |   |   |   Detroit
|   |       |   |   |   |   Dominica
|   |       |   |   |   |   Edmonton
|   |       |   |   |   |   Eirunepe
|   |       |   |   |   |   El_Salvador
|   |       |   |   |   |   Ensenada
|   |       |   |   |   |   Fortaleza
|   |       |   |   |   |   Fort_Nelson
|   |       |   |   |   |   Fort_Wayne
|   |       |   |   |   |   Glace_Bay
|   |       |   |   |   |   Godthab
|   |       |   |   |   |   Goose_Bay
|   |       |   |   |   |   Grand_Turk
|   |       |   |   |   |   Grenada
|   |       |   |   |   |   Guadeloupe
|   |       |   |   |   |   Guatemala
|   |       |   |   |   |   Guayaquil
|   |       |   |   |   |   Guyana
|   |       |   |   |   |   Halifax
|   |       |   |   |   |   Havana
|   |       |   |   |   |   Hermosillo
|   |       |   |   |   |   Indianapolis
|   |       |   |   |   |   Inuvik
|   |       |   |   |   |   Iqaluit
|   |       |   |   |   |   Jamaica
|   |       |   |   |   |   Jujuy
|   |       |   |   |   |   Juneau
|   |       |   |   |   |   Knox_IN
|   |       |   |   |   |   Kralendijk
|   |       |   |   |   |   La_Paz
|   |       |   |   |   |   Lima
|   |       |   |   |   |   Los_Angeles
|   |       |   |   |   |   Louisville
|   |       |   |   |   |   Lower_Princes
|   |       |   |   |   |   Maceio
|   |       |   |   |   |   Managua
|   |       |   |   |   |   Manaus
|   |       |   |   |   |   Marigot
|   |       |   |   |   |   Martinique
|   |       |   |   |   |   Matamoros
|   |       |   |   |   |   Mazatlan
|   |       |   |   |   |   Mendoza
|   |       |   |   |   |   Menominee
|   |       |   |   |   |   Merida
|   |       |   |   |   |   Metlakatla
|   |       |   |   |   |   Mexico_City
|   |       |   |   |   |   Miquelon
|   |       |   |   |   |   Moncton
|   |       |   |   |   |   Monterrey
|   |       |   |   |   |   Montevideo
|   |       |   |   |   |   Montreal
|   |       |   |   |   |   Montserrat
|   |       |   |   |   |   Nassau
|   |       |   |   |   |   New_York
|   |       |   |   |   |   Nipigon
|   |       |   |   |   |   Nome
|   |       |   |   |   |   Noronha
|   |       |   |   |   |   Nuuk
|   |       |   |   |   |   Ojinaga
|   |       |   |   |   |   Panama
|   |       |   |   |   |   Pangnirtung
|   |       |   |   |   |   Paramaribo
|   |       |   |   |   |   Phoenix
|   |       |   |   |   |   Port-au-Prince
|   |       |   |   |   |   Porto_Acre
|   |       |   |   |   |   Porto_Velho
|   |       |   |   |   |   Port_of_Spain
|   |       |   |   |   |   Puerto_Rico
|   |       |   |   |   |   Punta_Arenas
|   |       |   |   |   |   Rainy_River
|   |       |   |   |   |   Rankin_Inlet
|   |       |   |   |   |   Recife
|   |       |   |   |   |   Regina
|   |       |   |   |   |   Resolute
|   |       |   |   |   |   Rio_Branco
|   |       |   |   |   |   Rosario
|   |       |   |   |   |   Santarem
|   |       |   |   |   |   Santa_Isabel
|   |       |   |   |   |   Santiago
|   |       |   |   |   |   Santo_Domingo
|   |       |   |   |   |   Sao_Paulo
|   |       |   |   |   |   Scoresbysund
|   |       |   |   |   |   Shiprock
|   |       |   |   |   |   Sitka
|   |       |   |   |   |   St_Barthelemy
|   |       |   |   |   |   St_Johns
|   |       |   |   |   |   St_Kitts
|   |       |   |   |   |   St_Lucia
|   |       |   |   |   |   St_Thomas
|   |       |   |   |   |   St_Vincent
|   |       |   |   |   |   Swift_Current
|   |       |   |   |   |   Tegucigalpa
|   |       |   |   |   |   Thule
|   |       |   |   |   |   Thunder_Bay
|   |       |   |   |   |   Tijuana
|   |       |   |   |   |   Toronto
|   |       |   |   |   |   Tortola
|   |       |   |   |   |   Vancouver
|   |       |   |   |   |   Virgin
|   |       |   |   |   |   Whitehorse
|   |       |   |   |   |   Winnipeg
|   |       |   |   |   |   Yakutat
|   |       |   |   |   |   Yellowknife
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---Argentina
|   |       |   |   |   |   |   Buenos_Aires
|   |       |   |   |   |   |   Catamarca
|   |       |   |   |   |   |   ComodRivadavia
|   |       |   |   |   |   |   Cordoba
|   |       |   |   |   |   |   Jujuy
|   |       |   |   |   |   |   La_Rioja
|   |       |   |   |   |   |   Mendoza
|   |       |   |   |   |   |   Rio_Gallegos
|   |       |   |   |   |   |   Salta
|   |       |   |   |   |   |   San_Juan
|   |       |   |   |   |   |   San_Luis
|   |       |   |   |   |   |   Tucuman
|   |       |   |   |   |   |   Ushuaia
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---Indiana
|   |       |   |   |   |   |   Indianapolis
|   |       |   |   |   |   |   Knox
|   |       |   |   |   |   |   Marengo
|   |       |   |   |   |   |   Petersburg
|   |       |   |   |   |   |   Tell_City
|   |       |   |   |   |   |   Vevay
|   |       |   |   |   |   |   Vincennes
|   |       |   |   |   |   |   Winamac
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---Kentucky
|   |       |   |   |   |   |   Louisville
|   |       |   |   |   |   |   Monticello
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---North_Dakota
|   |       |   |   |   |   |   Beulah
|   |       |   |   |   |   |   Center
|   |       |   |   |   |   |   New_Salem
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           __init__.cpython-310.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---Antarctica
|   |       |   |   |   |   Casey
|   |       |   |   |   |   Davis
|   |       |   |   |   |   DumontDUrville
|   |       |   |   |   |   Macquarie
|   |       |   |   |   |   Mawson
|   |       |   |   |   |   McMurdo
|   |       |   |   |   |   Palmer
|   |       |   |   |   |   Rothera
|   |       |   |   |   |   South_Pole
|   |       |   |   |   |   Syowa
|   |       |   |   |   |   Troll
|   |       |   |   |   |   Vostok
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---Arctic
|   |       |   |   |   |   Longyearbyen
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---Asia
|   |       |   |   |   |   Aden
|   |       |   |   |   |   Almaty
|   |       |   |   |   |   Amman
|   |       |   |   |   |   Anadyr
|   |       |   |   |   |   Aqtau
|   |       |   |   |   |   Aqtobe
|   |       |   |   |   |   Ashgabat
|   |       |   |   |   |   Ashkhabad
|   |       |   |   |   |   Atyrau
|   |       |   |   |   |   Baghdad
|   |       |   |   |   |   Bahrain
|   |       |   |   |   |   Baku
|   |       |   |   |   |   Bangkok
|   |       |   |   |   |   Barnaul
|   |       |   |   |   |   Beirut
|   |       |   |   |   |   Bishkek
|   |       |   |   |   |   Brunei
|   |       |   |   |   |   Calcutta
|   |       |   |   |   |   Chita
|   |       |   |   |   |   Choibalsan
|   |       |   |   |   |   Chongqing
|   |       |   |   |   |   Chungking
|   |       |   |   |   |   Colombo
|   |       |   |   |   |   Dacca
|   |       |   |   |   |   Damascus
|   |       |   |   |   |   Dhaka
|   |       |   |   |   |   Dili
|   |       |   |   |   |   Dubai
|   |       |   |   |   |   Dushanbe
|   |       |   |   |   |   Famagusta
|   |       |   |   |   |   Gaza
|   |       |   |   |   |   Harbin
|   |       |   |   |   |   Hebron
|   |       |   |   |   |   Hong_Kong
|   |       |   |   |   |   Hovd
|   |       |   |   |   |   Ho_Chi_Minh
|   |       |   |   |   |   Irkutsk
|   |       |   |   |   |   Istanbul
|   |       |   |   |   |   Jakarta
|   |       |   |   |   |   Jayapura
|   |       |   |   |   |   Jerusalem
|   |       |   |   |   |   Kabul
|   |       |   |   |   |   Kamchatka
|   |       |   |   |   |   Karachi
|   |       |   |   |   |   Kashgar
|   |       |   |   |   |   Kathmandu
|   |       |   |   |   |   Katmandu
|   |       |   |   |   |   Khandyga
|   |       |   |   |   |   Kolkata
|   |       |   |   |   |   Krasnoyarsk
|   |       |   |   |   |   Kuala_Lumpur
|   |       |   |   |   |   Kuching
|   |       |   |   |   |   Kuwait
|   |       |   |   |   |   Macao
|   |       |   |   |   |   Macau
|   |       |   |   |   |   Magadan
|   |       |   |   |   |   Makassar
|   |       |   |   |   |   Manila
|   |       |   |   |   |   Muscat
|   |       |   |   |   |   Nicosia
|   |       |   |   |   |   Novokuznetsk
|   |       |   |   |   |   Novosibirsk
|   |       |   |   |   |   Omsk
|   |       |   |   |   |   Oral
|   |       |   |   |   |   Phnom_Penh
|   |       |   |   |   |   Pontianak
|   |       |   |   |   |   Pyongyang
|   |       |   |   |   |   Qatar
|   |       |   |   |   |   Qostanay
|   |       |   |   |   |   Qyzylorda
|   |       |   |   |   |   Rangoon
|   |       |   |   |   |   Riyadh
|   |       |   |   |   |   Saigon
|   |       |   |   |   |   Sakhalin
|   |       |   |   |   |   Samarkand
|   |       |   |   |   |   Seoul
|   |       |   |   |   |   Shanghai
|   |       |   |   |   |   Singapore
|   |       |   |   |   |   Srednekolymsk
|   |       |   |   |   |   Taipei
|   |       |   |   |   |   Tashkent
|   |       |   |   |   |   Tbilisi
|   |       |   |   |   |   Tehran
|   |       |   |   |   |   Tel_Aviv
|   |       |   |   |   |   Thimbu
|   |       |   |   |   |   Thimphu
|   |       |   |   |   |   Tokyo
|   |       |   |   |   |   Tomsk
|   |       |   |   |   |   Ujung_Pandang
|   |       |   |   |   |   Ulaanbaatar
|   |       |   |   |   |   Ulan_Bator
|   |       |   |   |   |   Urumqi
|   |       |   |   |   |   Ust-Nera
|   |       |   |   |   |   Vientiane
|   |       |   |   |   |   Vladivostok
|   |       |   |   |   |   Yakutsk
|   |       |   |   |   |   Yangon
|   |       |   |   |   |   Yekaterinburg
|   |       |   |   |   |   Yerevan
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---Atlantic
|   |       |   |   |   |   Azores
|   |       |   |   |   |   Bermuda
|   |       |   |   |   |   Canary
|   |       |   |   |   |   Cape_Verde
|   |       |   |   |   |   Faeroe
|   |       |   |   |   |   Faroe
|   |       |   |   |   |   Jan_Mayen
|   |       |   |   |   |   Madeira
|   |       |   |   |   |   Reykjavik
|   |       |   |   |   |   South_Georgia
|   |       |   |   |   |   Stanley
|   |       |   |   |   |   St_Helena
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---Australia
|   |       |   |   |   |   ACT
|   |       |   |   |   |   Adelaide
|   |       |   |   |   |   Brisbane
|   |       |   |   |   |   Broken_Hill
|   |       |   |   |   |   Canberra
|   |       |   |   |   |   Currie
|   |       |   |   |   |   Darwin
|   |       |   |   |   |   Eucla
|   |       |   |   |   |   Hobart
|   |       |   |   |   |   LHI
|   |       |   |   |   |   Lindeman
|   |       |   |   |   |   Lord_Howe
|   |       |   |   |   |   Melbourne
|   |       |   |   |   |   North
|   |       |   |   |   |   NSW
|   |       |   |   |   |   Perth
|   |       |   |   |   |   Queensland
|   |       |   |   |   |   South
|   |       |   |   |   |   Sydney
|   |       |   |   |   |   Tasmania
|   |       |   |   |   |   Victoria
|   |       |   |   |   |   West
|   |       |   |   |   |   Yancowinna
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---Brazil
|   |       |   |   |   |   Acre
|   |       |   |   |   |   DeNoronha
|   |       |   |   |   |   East
|   |       |   |   |   |   West
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---Canada
|   |       |   |   |   |   Atlantic
|   |       |   |   |   |   Central
|   |       |   |   |   |   Eastern
|   |       |   |   |   |   Mountain
|   |       |   |   |   |   Newfoundland
|   |       |   |   |   |   Pacific
|   |       |   |   |   |   Saskatchewan
|   |       |   |   |   |   Yukon
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---Chile
|   |       |   |   |   |   Continental
|   |       |   |   |   |   EasterIsland
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---Etc
|   |       |   |   |   |   GMT
|   |       |   |   |   |   GMT+0
|   |       |   |   |   |   GMT+1
|   |       |   |   |   |   GMT+10
|   |       |   |   |   |   GMT+11
|   |       |   |   |   |   GMT+12
|   |       |   |   |   |   GMT+2
|   |       |   |   |   |   GMT+3
|   |       |   |   |   |   GMT+4
|   |       |   |   |   |   GMT+5
|   |       |   |   |   |   GMT+6
|   |       |   |   |   |   GMT+7
|   |       |   |   |   |   GMT+8
|   |       |   |   |   |   GMT+9
|   |       |   |   |   |   GMT-0
|   |       |   |   |   |   GMT-1
|   |       |   |   |   |   GMT-10
|   |       |   |   |   |   GMT-11
|   |       |   |   |   |   GMT-12
|   |       |   |   |   |   GMT-13
|   |       |   |   |   |   GMT-14
|   |       |   |   |   |   GMT-2
|   |       |   |   |   |   GMT-3
|   |       |   |   |   |   GMT-4
|   |       |   |   |   |   GMT-5
|   |       |   |   |   |   GMT-6
|   |       |   |   |   |   GMT-7
|   |       |   |   |   |   GMT-8
|   |       |   |   |   |   GMT-9
|   |       |   |   |   |   GMT0
|   |       |   |   |   |   Greenwich
|   |       |   |   |   |   UCT
|   |       |   |   |   |   Universal
|   |       |   |   |   |   UTC
|   |       |   |   |   |   Zulu
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---Europe
|   |       |   |   |   |   Amsterdam
|   |       |   |   |   |   Andorra
|   |       |   |   |   |   Astrakhan
|   |       |   |   |   |   Athens
|   |       |   |   |   |   Belfast
|   |       |   |   |   |   Belgrade
|   |       |   |   |   |   Berlin
|   |       |   |   |   |   Bratislava
|   |       |   |   |   |   Brussels
|   |       |   |   |   |   Bucharest
|   |       |   |   |   |   Budapest
|   |       |   |   |   |   Busingen
|   |       |   |   |   |   Chisinau
|   |       |   |   |   |   Copenhagen
|   |       |   |   |   |   Dublin
|   |       |   |   |   |   Gibraltar
|   |       |   |   |   |   Guernsey
|   |       |   |   |   |   Helsinki
|   |       |   |   |   |   Isle_of_Man
|   |       |   |   |   |   Istanbul
|   |       |   |   |   |   Jersey
|   |       |   |   |   |   Kaliningrad
|   |       |   |   |   |   Kiev
|   |       |   |   |   |   Kirov
|   |       |   |   |   |   Kyiv
|   |       |   |   |   |   Lisbon
|   |       |   |   |   |   Ljubljana
|   |       |   |   |   |   London
|   |       |   |   |   |   Luxembourg
|   |       |   |   |   |   Madrid
|   |       |   |   |   |   Malta
|   |       |   |   |   |   Mariehamn
|   |       |   |   |   |   Minsk
|   |       |   |   |   |   Monaco
|   |       |   |   |   |   Moscow
|   |       |   |   |   |   Nicosia
|   |       |   |   |   |   Oslo
|   |       |   |   |   |   Paris
|   |       |   |   |   |   Podgorica
|   |       |   |   |   |   Prague
|   |       |   |   |   |   Riga
|   |       |   |   |   |   Rome
|   |       |   |   |   |   Samara
|   |       |   |   |   |   San_Marino
|   |       |   |   |   |   Sarajevo
|   |       |   |   |   |   Saratov
|   |       |   |   |   |   Simferopol
|   |       |   |   |   |   Skopje
|   |       |   |   |   |   Sofia
|   |       |   |   |   |   Stockholm
|   |       |   |   |   |   Tallinn
|   |       |   |   |   |   Tirane
|   |       |   |   |   |   Tiraspol
|   |       |   |   |   |   Ulyanovsk
|   |       |   |   |   |   Uzhgorod
|   |       |   |   |   |   Vaduz
|   |       |   |   |   |   Vatican
|   |       |   |   |   |   Vienna
|   |       |   |   |   |   Vilnius
|   |       |   |   |   |   Volgograd
|   |       |   |   |   |   Warsaw
|   |       |   |   |   |   Zagreb
|   |       |   |   |   |   Zaporozhye
|   |       |   |   |   |   Zurich
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---Indian
|   |       |   |   |   |   Antananarivo
|   |       |   |   |   |   Chagos
|   |       |   |   |   |   Christmas
|   |       |   |   |   |   Cocos
|   |       |   |   |   |   Comoro
|   |       |   |   |   |   Kerguelen
|   |       |   |   |   |   Mahe
|   |       |   |   |   |   Maldives
|   |       |   |   |   |   Mauritius
|   |       |   |   |   |   Mayotte
|   |       |   |   |   |   Reunion
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---Mexico
|   |       |   |   |   |   BajaNorte
|   |       |   |   |   |   BajaSur
|   |       |   |   |   |   General
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---Pacific
|   |       |   |   |   |   Apia
|   |       |   |   |   |   Auckland
|   |       |   |   |   |   Bougainville
|   |       |   |   |   |   Chatham
|   |       |   |   |   |   Chuuk
|   |       |   |   |   |   Easter
|   |       |   |   |   |   Efate
|   |       |   |   |   |   Enderbury
|   |       |   |   |   |   Fakaofo
|   |       |   |   |   |   Fiji
|   |       |   |   |   |   Funafuti
|   |       |   |   |   |   Galapagos
|   |       |   |   |   |   Gambier
|   |       |   |   |   |   Guadalcanal
|   |       |   |   |   |   Guam
|   |       |   |   |   |   Honolulu
|   |       |   |   |   |   Johnston
|   |       |   |   |   |   Kanton
|   |       |   |   |   |   Kiritimati
|   |       |   |   |   |   Kosrae
|   |       |   |   |   |   Kwajalein
|   |       |   |   |   |   Majuro
|   |       |   |   |   |   Marquesas
|   |       |   |   |   |   Midway
|   |       |   |   |   |   Nauru
|   |       |   |   |   |   Niue
|   |       |   |   |   |   Norfolk
|   |       |   |   |   |   Noumea
|   |       |   |   |   |   Pago_Pago
|   |       |   |   |   |   Palau
|   |       |   |   |   |   Pitcairn
|   |       |   |   |   |   Pohnpei
|   |       |   |   |   |   Ponape
|   |       |   |   |   |   Port_Moresby
|   |       |   |   |   |   Rarotonga
|   |       |   |   |   |   Saipan
|   |       |   |   |   |   Samoa
|   |       |   |   |   |   Tahiti
|   |       |   |   |   |   Tarawa
|   |       |   |   |   |   Tongatapu
|   |       |   |   |   |   Truk
|   |       |   |   |   |   Wake
|   |       |   |   |   |   Wallis
|   |       |   |   |   |   Yap
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   +---US
|   |       |   |   |   |   Alaska
|   |       |   |   |   |   Aleutian
|   |       |   |   |   |   Arizona
|   |       |   |   |   |   Central
|   |       |   |   |   |   East-Indiana
|   |       |   |   |   |   Eastern
|   |       |   |   |   |   Hawaii
|   |       |   |   |   |   Indiana-Starke
|   |       |   |   |   |   Michigan
|   |       |   |   |   |   Mountain
|   |       |   |   |   |   Pacific
|   |       |   |   |   |   Samoa
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-310.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---tzdata-2026.1.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |       |   LICENSE
|   |       |       |   
|   |       |       \---licenses
|   |       |               LICENSE_APACHE
|   |       |               
|   |       +---_distutils_hack
|   |       |   |   override.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           override.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       +---_pytest
|   |       |   |   cacheprovider.py
|   |       |   |   capture.py
|   |       |   |   compat.py
|   |       |   |   debugging.py
|   |       |   |   deprecated.py
|   |       |   |   doctest.py
|   |       |   |   faulthandler.py
|   |       |   |   fixtures.py
|   |       |   |   freeze_support.py
|   |       |   |   helpconfig.py
|   |       |   |   hookspec.py
|   |       |   |   junitxml.py
|   |       |   |   legacypath.py
|   |       |   |   logging.py
|   |       |   |   main.py
|   |       |   |   monkeypatch.py
|   |       |   |   nodes.py
|   |       |   |   outcomes.py
|   |       |   |   pastebin.py
|   |       |   |   pathlib.py
|   |       |   |   py.typed
|   |       |   |   pytester.py
|   |       |   |   pytester_assertions.py
|   |       |   |   python.py
|   |       |   |   python_api.py
|   |       |   |   raises.py
|   |       |   |   recwarn.py
|   |       |   |   reports.py
|   |       |   |   runner.py
|   |       |   |   scope.py
|   |       |   |   setuponly.py
|   |       |   |   setupplan.py
|   |       |   |   skipping.py
|   |       |   |   stash.py
|   |       |   |   stepwise.py
|   |       |   |   subtests.py
|   |       |   |   terminal.py
|   |       |   |   terminalprogress.py
|   |       |   |   threadexception.py
|   |       |   |   timing.py
|   |       |   |   tmpdir.py
|   |       |   |   tracemalloc.py
|   |       |   |   unittest.py
|   |       |   |   unraisableexception.py
|   |       |   |   warnings.py
|   |       |   |   warning_types.py
|   |       |   |   _argcomplete.py
|   |       |   |   _version.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---assertion
|   |       |   |   |   rewrite.py
|   |       |   |   |   truncate.py
|   |       |   |   |   util.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           rewrite.cpython-310.pyc
|   |       |   |           truncate.cpython-310.pyc
|   |       |   |           util.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---config
|   |       |   |   |   argparsing.py
|   |       |   |   |   compat.py
|   |       |   |   |   exceptions.py
|   |       |   |   |   findpaths.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           argparsing.cpython-310.pyc
|   |       |   |           compat.cpython-310.pyc
|   |       |   |           exceptions.cpython-310.pyc
|   |       |   |           findpaths.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---mark
|   |       |   |   |   expression.py
|   |       |   |   |   structures.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           expression.cpython-310.pyc
|   |       |   |           structures.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_code
|   |       |   |   |   code.py
|   |       |   |   |   source.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           code.cpython-310.pyc
|   |       |   |           source.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_io
|   |       |   |   |   pprint.py
|   |       |   |   |   saferepr.py
|   |       |   |   |   terminalwriter.py
|   |       |   |   |   wcwidth.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           pprint.cpython-310.pyc
|   |       |   |           saferepr.cpython-310.pyc
|   |       |   |           terminalwriter.cpython-310.pyc
|   |       |   |           wcwidth.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   +---_py
|   |       |   |   |   error.py
|   |       |   |   |   path.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           error.cpython-310.pyc
|   |       |   |           path.cpython-310.pyc
|   |       |   |           __init__.cpython-310.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           cacheprovider.cpython-310.pyc
|   |       |           capture.cpython-310.pyc
|   |       |           compat.cpython-310.pyc
|   |       |           debugging.cpython-310.pyc
|   |       |           deprecated.cpython-310.pyc
|   |       |           doctest.cpython-310.pyc
|   |       |           faulthandler.cpython-310.pyc
|   |       |           fixtures.cpython-310.pyc
|   |       |           freeze_support.cpython-310.pyc
|   |       |           helpconfig.cpython-310.pyc
|   |       |           hookspec.cpython-310.pyc
|   |       |           junitxml.cpython-310.pyc
|   |       |           legacypath.cpython-310.pyc
|   |       |           logging.cpython-310.pyc
|   |       |           main.cpython-310.pyc
|   |       |           monkeypatch.cpython-310.pyc
|   |       |           nodes.cpython-310.pyc
|   |       |           outcomes.cpython-310.pyc
|   |       |           pastebin.cpython-310.pyc
|   |       |           pathlib.cpython-310.pyc
|   |       |           pytester.cpython-310.pyc
|   |       |           pytester_assertions.cpython-310.pyc
|   |       |           python.cpython-310.pyc
|   |       |           python_api.cpython-310.pyc
|   |       |           raises.cpython-310.pyc
|   |       |           recwarn.cpython-310.pyc
|   |       |           reports.cpython-310.pyc
|   |       |           runner.cpython-310.pyc
|   |       |           scope.cpython-310.pyc
|   |       |           setuponly.cpython-310.pyc
|   |       |           setupplan.cpython-310.pyc
|   |       |           skipping.cpython-310.pyc
|   |       |           stash.cpython-310.pyc
|   |       |           stepwise.cpython-310.pyc
|   |       |           subtests.cpython-310.pyc
|   |       |           terminal.cpython-310.pyc
|   |       |           terminalprogress.cpython-310-pytest-9.0.3.pyc
|   |       |           terminalprogress.cpython-310.pyc
|   |       |           threadexception.cpython-310.pyc
|   |       |           timing.cpython-310.pyc
|   |       |           tmpdir.cpython-310.pyc
|   |       |           tracemalloc.cpython-310.pyc
|   |       |           unittest.cpython-310.pyc
|   |       |           unraisableexception.cpython-310.pyc
|   |       |           warnings.cpython-310.pyc
|   |       |           warning_types.cpython-310.pyc
|   |       |           _argcomplete.cpython-310.pyc
|   |       |           _version.cpython-310.pyc
|   |       |           __init__.cpython-310.pyc
|   |       |           
|   |       \---__pycache__
|   |               py.cpython-310.pyc
|   |               six.cpython-310.pyc
|   |               typing_extensions.cpython-310.pyc
|   |               
|   \---Scripts
|           activate
|           activate.bat
|           Activate.ps1
|           coverage-3.10.exe
|           coverage.exe
|           coverage3.exe
|           deactivate.bat
|           dotenv.exe
|           f2py.exe
|           luanny.exe
|           markdown-it.exe
|           numpy-config.exe
|           pip.exe
|           pip3.10.exe
|           pip3.exe
|           playwright.exe
|           py.test.exe
|           pygmentize.exe
|           pytest.exe
|           python.exe
|           pythonw.exe
|           ruff.exe
|           typer.exe
|           
+---build
|   \---Luanny
|       |   Analysis-00.toc
|       |   base_library.zip
|       |   COLLECT-00.toc
|       |   EXE-00.toc
|       |   Luanny.exe
|       |   Luanny.pkg
|       |   PKG-00.toc
|       |   PYZ-00.pyz
|       |   PYZ-00.toc
|       |   warn-Luanny.txt
|       |   xref-Luanny.html
|       |   
|       \---localpycs
|               pyimod01_archive.pyc
|               pyimod02_importers.pyc
|               pyimod03_ctypes.pyc
|               pyimod04_pywin32.pyc
|               struct.pyc
|               
+---data
|   \---govbr_20260417_181540
|       |   posts.json
|       |   report.md
|       |   summary.csv
|       |   
|       \---evidence
|           +---DXIXsUIsaR6
|           |       page.html
|           |       screenshot.png
|           |       
|           \---DXJoAPekbE2
|                   page.html
|                   screenshot.png
|                   
+---dist
|   \---Luanny
|       |   executar.bat
|       |   LEIA-ME.txt
|       |   Luanny.exe
|       |   
|       \---_internal
|           |   30fcd23745efe32ce681__mypyc.cp312-win_amd64.pyd
|           |   api-ms-win-core-console-l1-1-0.dll
|           |   api-ms-win-core-datetime-l1-1-0.dll
|           |   api-ms-win-core-debug-l1-1-0.dll
|           |   api-ms-win-core-errorhandling-l1-1-0.dll
|           |   api-ms-win-core-fibers-l1-1-0.dll
|           |   api-ms-win-core-fibers-l1-1-1.dll
|           |   api-ms-win-core-file-l1-1-0.dll
|           |   api-ms-win-core-file-l1-2-0.dll
|           |   api-ms-win-core-file-l2-1-0.dll
|           |   api-ms-win-core-handle-l1-1-0.dll
|           |   api-ms-win-core-heap-l1-1-0.dll
|           |   api-ms-win-core-interlocked-l1-1-0.dll
|           |   api-ms-win-core-kernel32-legacy-l1-1-1.dll
|           |   api-ms-win-core-libraryloader-l1-1-0.dll
|           |   api-ms-win-core-localization-l1-2-0.dll
|           |   api-ms-win-core-memory-l1-1-0.dll
|           |   api-ms-win-core-namedpipe-l1-1-0.dll
|           |   api-ms-win-core-processenvironment-l1-1-0.dll
|           |   api-ms-win-core-processthreads-l1-1-0.dll
|           |   api-ms-win-core-processthreads-l1-1-1.dll
|           |   api-ms-win-core-profile-l1-1-0.dll
|           |   api-ms-win-core-rtlsupport-l1-1-0.dll
|           |   api-ms-win-core-string-l1-1-0.dll
|           |   api-ms-win-core-synch-l1-1-0.dll
|           |   api-ms-win-core-synch-l1-2-0.dll
|           |   api-ms-win-core-sysinfo-l1-1-0.dll
|           |   api-ms-win-core-sysinfo-l1-2-0.dll
|           |   api-ms-win-core-timezone-l1-1-0.dll
|           |   api-ms-win-core-util-l1-1-0.dll
|           |   api-ms-win-crt-conio-l1-1-0.dll
|           |   api-ms-win-crt-convert-l1-1-0.dll
|           |   api-ms-win-crt-environment-l1-1-0.dll
|           |   api-ms-win-crt-filesystem-l1-1-0.dll
|           |   api-ms-win-crt-heap-l1-1-0.dll
|           |   api-ms-win-crt-locale-l1-1-0.dll
|           |   api-ms-win-crt-math-l1-1-0.dll
|           |   api-ms-win-crt-private-l1-1-0.dll
|           |   api-ms-win-crt-process-l1-1-0.dll
|           |   api-ms-win-crt-runtime-l1-1-0.dll
|           |   api-ms-win-crt-stdio-l1-1-0.dll
|           |   api-ms-win-crt-string-l1-1-0.dll
|           |   api-ms-win-crt-time-l1-1-0.dll
|           |   api-ms-win-crt-utility-l1-1-0.dll
|           |   base_library.zip
|           |   libcrypto-3.dll
|           |   libffi-8.dll
|           |   libssl-3.dll
|           |   pyexpat.pyd
|           |   python3.dll
|           |   python312.dll
|           |   select.pyd
|           |   sqlite3.dll
|           |   ucrtbase.dll
|           |   unicodedata.pyd
|           |   VCRUNTIME140.dll
|           |   VCRUNTIME140_1.dll
|           |   _asyncio.pyd
|           |   _bz2.pyd
|           |   _ctypes.pyd
|           |   _decimal.pyd
|           |   _elementtree.pyd
|           |   _hashlib.pyd
|           |   _lzma.pyd
|           |   _multiprocessing.pyd
|           |   _overlapped.pyd
|           |   _queue.pyd
|           |   _socket.pyd
|           |   _sqlite3.pyd
|           |   _ssl.pyd
|           |   _uuid.pyd
|           |   _wmi.pyd
|           |   _zoneinfo.pyd
|           |   
|           +---attrs-25.3.0.dist-info
|           |   |   INSTALLER
|           |   |   METADATA
|           |   |   RECORD
|           |   |   WHEEL
|           |   |   
|           |   \---licenses
|           |           LICENSE
|           |           
|           +---black
|           |   |   brackets.cp312-win_amd64.pyd
|           |   |   cache.cp312-win_amd64.pyd
|           |   |   comments.cp312-win_amd64.pyd
|           |   |   const.cp312-win_amd64.pyd
|           |   |   handle_ipynb_magics.cp312-win_amd64.pyd
|           |   |   linegen.cp312-win_amd64.pyd
|           |   |   lines.cp312-win_amd64.pyd
|           |   |   mode.cp312-win_amd64.pyd
|           |   |   nodes.cp312-win_amd64.pyd
|           |   |   numerics.cp312-win_amd64.pyd
|           |   |   parsing.cp312-win_amd64.pyd
|           |   |   py.typed
|           |   |   ranges.cp312-win_amd64.pyd
|           |   |   rusty.cp312-win_amd64.pyd
|           |   |   schema.cp312-win_amd64.pyd
|           |   |   strings.cp312-win_amd64.pyd
|           |   |   trans.cp312-win_amd64.pyd
|           |   |   _width_table.cp312-win_amd64.pyd
|           |   |   __init__.cp312-win_amd64.pyd
|           |   |   
|           |   \---resources
|           |           black.schema.json
|           |           __init__.cp312-win_amd64.pyd
|           |           
|           +---blib2to3
|           |   |   Grammar.txt
|           |   |   LICENSE
|           |   |   PatternGrammar.txt
|           |   |   pygram.cp312-win_amd64.pyd
|           |   |   pytree.cp312-win_amd64.pyd
|           |   |   README
|           |   |   
|           |   \---pgen2
|           |           conv.cp312-win_amd64.pyd
|           |           driver.cp312-win_amd64.pyd
|           |           grammar.cp312-win_amd64.pyd
|           |           literals.cp312-win_amd64.pyd
|           |           parse.cp312-win_amd64.pyd
|           |           pgen.cp312-win_amd64.pyd
|           |           token.cp312-win_amd64.pyd
|           |           tokenize.cp312-win_amd64.pyd
|           |           
|           +---charset_normalizer
|           |       md.cp312-win_amd64.pyd
|           |       md__mypyc.cp312-win_amd64.pyd
|           |       
|           +---click-8.2.2.dist-info
|           |   |   INSTALLER
|           |   |   METADATA
|           |   |   RECORD
|           |   |   REQUESTED
|           |   |   WHEEL
|           |   |   
|           |   \---licenses
|           |           LICENSE.txt
|           |           
|           +---greenlet
|           |       _greenlet.cp312-win_amd64.pyd
|           |       
|           +---IPython
|           |   |   py.typed
|           |   |   
|           |   +---core
|           |   |   \---profile
|           |   |           README_STARTUP
|           |   |           
|           |   +---extensions
|           |   |   |   autoreload.py
|           |   |   |   storemagic.py
|           |   |   |   __init__.py
|           |   |   |   
|           |   |   \---deduperreload
|           |   |           deduperreload.py
|           |   |           deduperreload_patching.py
|           |   |           __init__.py
|           |   |           
|           |   \---testing
|           |       \---plugin
|           |               test_combo.txt
|           |               test_example.txt
|           |               test_exampleip.txt
|           |               
|           +---jedi
|           |   \---third_party
|           |       +---django-stubs
|           |       |   |   LICENSE.txt
|           |       |   |   
|           |       |   \---django-stubs
|           |       |       |   shortcuts.pyi
|           |       |       |   __init__.pyi
|           |       |       |   
|           |       |       +---apps
|           |       |       |       config.pyi
|           |       |       |       registry.pyi
|           |       |       |       __init__.pyi
|           |       |       |       
|           |       |       +---conf
|           |       |       |   |   global_settings.pyi
|           |       |       |   |   __init__.pyi
|           |       |       |   |   
|           |       |       |   +---locale
|           |       |       |   |       __init__.pyi
|           |       |       |   |       
|           |       |       |   \---urls
|           |       |       |           i18n.pyi
|           |       |       |           static.pyi
|           |       |       |           __init__.pyi
|           |       |       |           
|           |       |       +---contrib
|           |       |       |   |   __init__.pyi
|           |       |       |   |   
|           |       |       |   +---admin
|           |       |       |   |   |   actions.pyi
|           |       |       |   |   |   apps.pyi
|           |       |       |   |   |   checks.pyi
|           |       |       |   |   |   decorators.pyi
|           |       |       |   |   |   filters.pyi
|           |       |       |   |   |   forms.pyi
|           |       |       |   |   |   helpers.pyi
|           |       |       |   |   |   models.pyi
|           |       |       |   |   |   options.pyi
|           |       |       |   |   |   sites.pyi
|           |       |       |   |   |   tests.pyi
|           |       |       |   |   |   utils.pyi
|           |       |       |   |   |   widgets.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   +---templatetags
|           |       |       |   |   |       admin_list.pyi
|           |       |       |   |   |       admin_modify.pyi
|           |       |       |   |   |       admin_static.pyi
|           |       |       |   |   |       admin_urls.pyi
|           |       |       |   |   |       base.pyi
|           |       |       |   |   |       log.pyi
|           |       |       |   |   |       __init__.pyi
|           |       |       |   |   |       
|           |       |       |   |   \---views
|           |       |       |   |           autocomplete.pyi
|           |       |       |   |           decorators.pyi
|           |       |       |   |           main.pyi
|           |       |       |   |           __init__.pyi
|           |       |       |   |           
|           |       |       |   +---admindocs
|           |       |       |   |       middleware.pyi
|           |       |       |   |       urls.pyi
|           |       |       |   |       utils.pyi
|           |       |       |   |       views.pyi
|           |       |       |   |       __init__.pyi
|           |       |       |   |       
|           |       |       |   +---auth
|           |       |       |   |   |   admin.pyi
|           |       |       |   |   |   apps.pyi
|           |       |       |   |   |   backends.pyi
|           |       |       |   |   |   base_user.pyi
|           |       |       |   |   |   checks.pyi
|           |       |       |   |   |   context_processors.pyi
|           |       |       |   |   |   decorators.pyi
|           |       |       |   |   |   forms.pyi
|           |       |       |   |   |   hashers.pyi
|           |       |       |   |   |   middleware.pyi
|           |       |       |   |   |   mixins.pyi
|           |       |       |   |   |   models.pyi
|           |       |       |   |   |   password_validation.pyi
|           |       |       |   |   |   signals.pyi
|           |       |       |   |   |   tokens.pyi
|           |       |       |   |   |   urls.pyi
|           |       |       |   |   |   validators.pyi
|           |       |       |   |   |   views.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   +---handlers
|           |       |       |   |   |       modwsgi.pyi
|           |       |       |   |   |       __init__.pyi
|           |       |       |   |   |       
|           |       |       |   |   \---management
|           |       |       |   |       |   __init__.pyi
|           |       |       |   |       |   
|           |       |       |   |       \---commands
|           |       |       |   |               changepassword.pyi
|           |       |       |   |               createsuperuser.pyi
|           |       |       |   |               __init__.pyi
|           |       |       |   |               
|           |       |       |   +---contenttypes
|           |       |       |   |   |   admin.pyi
|           |       |       |   |   |   apps.pyi
|           |       |       |   |   |   checks.pyi
|           |       |       |   |   |   fields.pyi
|           |       |       |   |   |   forms.pyi
|           |       |       |   |   |   models.pyi
|           |       |       |   |   |   views.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   \---management
|           |       |       |   |       |   __init__.pyi
|           |       |       |   |       |   
|           |       |       |   |       \---commands
|           |       |       |   |               remove_stale_contenttypes.pyi
|           |       |       |   |               __init__.pyi
|           |       |       |   |               
|           |       |       |   +---flatpages
|           |       |       |   |   |   forms.pyi
|           |       |       |   |   |   middleware.pyi
|           |       |       |   |   |   models.pyi
|           |       |       |   |   |   sitemaps.pyi
|           |       |       |   |   |   urls.pyi
|           |       |       |   |   |   views.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   \---templatetags
|           |       |       |   |           flatpages.pyi
|           |       |       |   |           __init__.pyi
|           |       |       |   |           
|           |       |       |   +---gis
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   \---db
|           |       |       |   |       |   __init__.pyi
|           |       |       |   |       |   
|           |       |       |   |       \---models
|           |       |       |   |               fields.pyi
|           |       |       |   |               __init__.pyi
|           |       |       |   |               
|           |       |       |   +---humanize
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   \---templatetags
|           |       |       |   |           humanize.pyi
|           |       |       |   |           __init__.pyi
|           |       |       |   |           
|           |       |       |   +---messages
|           |       |       |   |   |   api.pyi
|           |       |       |   |   |   constants.pyi
|           |       |       |   |   |   context_processors.pyi
|           |       |       |   |   |   middleware.pyi
|           |       |       |   |   |   utils.pyi
|           |       |       |   |   |   views.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   \---storage
|           |       |       |   |           base.pyi
|           |       |       |   |           cookie.pyi
|           |       |       |   |           fallback.pyi
|           |       |       |   |           session.pyi
|           |       |       |   |           __init__.pyi
|           |       |       |   |           
|           |       |       |   +---postgres
|           |       |       |   |   |   constraints.pyi
|           |       |       |   |   |   functions.pyi
|           |       |       |   |   |   indexes.pyi
|           |       |       |   |   |   lookups.pyi
|           |       |       |   |   |   operations.pyi
|           |       |       |   |   |   search.pyi
|           |       |       |   |   |   signals.pyi
|           |       |       |   |   |   validators.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   +---aggregates
|           |       |       |   |   |       general.pyi
|           |       |       |   |   |       mixins.pyi
|           |       |       |   |   |       statistics.pyi
|           |       |       |   |   |       __init__.pyi
|           |       |       |   |   |       
|           |       |       |   |   \---fields
|           |       |       |   |           array.pyi
|           |       |       |   |           citext.pyi
|           |       |       |   |           hstore.pyi
|           |       |       |   |           jsonb.pyi
|           |       |       |   |           mixins.pyi
|           |       |       |   |           ranges.pyi
|           |       |       |   |           __init__.pyi
|           |       |       |   |           
|           |       |       |   +---redirects
|           |       |       |   |       middleware.pyi
|           |       |       |   |       models.pyi
|           |       |       |   |       __init__.pyi
|           |       |       |   |       
|           |       |       |   +---sessions
|           |       |       |   |   |   base_session.pyi
|           |       |       |   |   |   exceptions.pyi
|           |       |       |   |   |   middleware.pyi
|           |       |       |   |   |   models.pyi
|           |       |       |   |   |   serializers.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   +---backends
|           |       |       |   |   |       base.pyi
|           |       |       |   |   |       cache.pyi
|           |       |       |   |   |       cached_db.pyi
|           |       |       |   |   |       db.pyi
|           |       |       |   |   |       file.pyi
|           |       |       |   |   |       signed_cookies.pyi
|           |       |       |   |   |       __init__.pyi
|           |       |       |   |   |       
|           |       |       |   |   \---management
|           |       |       |   |       |   __init__.pyi
|           |       |       |   |       |   
|           |       |       |   |       \---commands
|           |       |       |   |               clearsessions.pyi
|           |       |       |   |               __init__.pyi
|           |       |       |   |               
|           |       |       |   +---sitemaps
|           |       |       |   |   |   views.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   \---management
|           |       |       |   |       |   __init__.pyi
|           |       |       |   |       |   
|           |       |       |   |       \---commands
|           |       |       |   |               ping_google.pyi
|           |       |       |   |               __init__.pyi
|           |       |       |   |               
|           |       |       |   +---sites
|           |       |       |   |       apps.pyi
|           |       |       |   |       management.pyi
|           |       |       |   |       managers.pyi
|           |       |       |   |       middleware.pyi
|           |       |       |   |       models.pyi
|           |       |       |   |       requests.pyi
|           |       |       |   |       shortcuts.pyi
|           |       |       |   |       __init__.pyi
|           |       |       |   |       
|           |       |       |   +---staticfiles
|           |       |       |   |   |   apps.pyi
|           |       |       |   |   |   checks.pyi
|           |       |       |   |   |   finders.pyi
|           |       |       |   |   |   handlers.pyi
|           |       |       |   |   |   storage.pyi
|           |       |       |   |   |   testing.pyi
|           |       |       |   |   |   urls.pyi
|           |       |       |   |   |   utils.pyi
|           |       |       |   |   |   views.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   +---management
|           |       |       |   |   |   |   __init__.pyi
|           |       |       |   |   |   |   
|           |       |       |   |   |   \---commands
|           |       |       |   |   |           collectstatic.pyi
|           |       |       |   |   |           findstatic.pyi
|           |       |       |   |   |           runserver.pyi
|           |       |       |   |   |           __init__.pyi
|           |       |       |   |   |           
|           |       |       |   |   \---templatetags
|           |       |       |   |           staticfiles.pyi
|           |       |       |   |           __init__.pyi
|           |       |       |   |           
|           |       |       |   \---syndication
|           |       |       |           views.pyi
|           |       |       |           __init__.pyi
|           |       |       |           
|           |       |       +---core
|           |       |       |   |   exceptions.pyi
|           |       |       |   |   paginator.pyi
|           |       |       |   |   signals.pyi
|           |       |       |   |   signing.pyi
|           |       |       |   |   validators.pyi
|           |       |       |   |   wsgi.pyi
|           |       |       |   |   __init__.pyi
|           |       |       |   |   
|           |       |       |   +---cache
|           |       |       |   |   |   utils.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   \---backends
|           |       |       |   |           base.pyi
|           |       |       |   |           db.pyi
|           |       |       |   |           dummy.pyi
|           |       |       |   |           filebased.pyi
|           |       |       |   |           locmem.pyi
|           |       |       |   |           memcached.pyi
|           |       |       |   |           __init__.pyi
|           |       |       |   |           
|           |       |       |   +---checks
|           |       |       |   |   |   caches.pyi
|           |       |       |   |   |   database.pyi
|           |       |       |   |   |   messages.pyi
|           |       |       |   |   |   model_checks.pyi
|           |       |       |   |   |   registry.pyi
|           |       |       |   |   |   templates.pyi
|           |       |       |   |   |   translation.pyi
|           |       |       |   |   |   urls.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   \---security
|           |       |       |   |           base.pyi
|           |       |       |   |           csrf.pyi
|           |       |       |   |           sessions.pyi
|           |       |       |   |           __init__.pyi
|           |       |       |   |           
|           |       |       |   +---files
|           |       |       |   |       base.pyi
|           |       |       |   |       images.pyi
|           |       |       |   |       locks.pyi
|           |       |       |   |       move.pyi
|           |       |       |   |       storage.pyi
|           |       |       |   |       temp.pyi
|           |       |       |   |       uploadedfile.pyi
|           |       |       |   |       uploadhandler.pyi
|           |       |       |   |       utils.pyi
|           |       |       |   |       __init__.pyi
|           |       |       |   |       
|           |       |       |   +---handlers
|           |       |       |   |       base.pyi
|           |       |       |   |       exception.pyi
|           |       |       |   |       wsgi.pyi
|           |       |       |   |       __init__.pyi
|           |       |       |   |       
|           |       |       |   +---mail
|           |       |       |   |   |   message.pyi
|           |       |       |   |   |   utils.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   \---backends
|           |       |       |   |           base.pyi
|           |       |       |   |           console.pyi
|           |       |       |   |           dummy.pyi
|           |       |       |   |           filebased.pyi
|           |       |       |   |           locmem.pyi
|           |       |       |   |           smtp.pyi
|           |       |       |   |           __init__.pyi
|           |       |       |   |           
|           |       |       |   +---management
|           |       |       |   |   |   base.pyi
|           |       |       |   |   |   color.pyi
|           |       |       |   |   |   sql.pyi
|           |       |       |   |   |   templates.pyi
|           |       |       |   |   |   utils.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   \---commands
|           |       |       |   |           dumpdata.pyi
|           |       |       |   |           loaddata.pyi
|           |       |       |   |           makemessages.pyi
|           |       |       |   |           runserver.pyi
|           |       |       |   |           testserver.pyi
|           |       |       |   |           __init__.pyi
|           |       |       |   |           
|           |       |       |   +---serializers
|           |       |       |   |       base.pyi
|           |       |       |   |       json.pyi
|           |       |       |   |       python.pyi
|           |       |       |   |       __init__.pyi
|           |       |       |   |       
|           |       |       |   \---servers
|           |       |       |           basehttp.pyi
|           |       |       |           __init__.pyi
|           |       |       |           
|           |       |       +---db
|           |       |       |   |   transaction.pyi
|           |       |       |   |   utils.pyi
|           |       |       |   |   __init__.pyi
|           |       |       |   |   
|           |       |       |   +---backends
|           |       |       |   |   |   ddl_references.pyi
|           |       |       |   |   |   signals.pyi
|           |       |       |   |   |   utils.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   +---base
|           |       |       |   |   |       base.pyi
|           |       |       |   |   |       client.pyi
|           |       |       |   |   |       creation.pyi
|           |       |       |   |   |       features.pyi
|           |       |       |   |   |       introspection.pyi
|           |       |       |   |   |       operations.pyi
|           |       |       |   |   |       schema.pyi
|           |       |       |   |   |       validation.pyi
|           |       |       |   |   |       __init__.pyi
|           |       |       |   |   |       
|           |       |       |   |   +---dummy
|           |       |       |   |   |       base.pyi
|           |       |       |   |   |       __init__.pyi
|           |       |       |   |   |       
|           |       |       |   |   +---mysql
|           |       |       |   |   |       client.pyi
|           |       |       |   |   |       __init__.pyi
|           |       |       |   |   |       
|           |       |       |   |   +---postgresql
|           |       |       |   |   |       base.pyi
|           |       |       |   |   |       client.pyi
|           |       |       |   |   |       creation.pyi
|           |       |       |   |   |       operations.pyi
|           |       |       |   |   |       __init__.pyi
|           |       |       |   |   |       
|           |       |       |   |   \---sqlite3
|           |       |       |   |           base.pyi
|           |       |       |   |           creation.pyi
|           |       |       |   |           features.pyi
|           |       |       |   |           introspection.pyi
|           |       |       |   |           operations.pyi
|           |       |       |   |           schema.pyi
|           |       |       |   |           __init__.pyi
|           |       |       |   |           
|           |       |       |   +---migrations
|           |       |       |   |   |   autodetector.pyi
|           |       |       |   |   |   exceptions.pyi
|           |       |       |   |   |   executor.pyi
|           |       |       |   |   |   graph.pyi
|           |       |       |   |   |   loader.pyi
|           |       |       |   |   |   migration.pyi
|           |       |       |   |   |   optimizer.pyi
|           |       |       |   |   |   questioner.pyi
|           |       |       |   |   |   recorder.pyi
|           |       |       |   |   |   serializer.pyi
|           |       |       |   |   |   state.pyi
|           |       |       |   |   |   topological_sort.pyi
|           |       |       |   |   |   utils.pyi
|           |       |       |   |   |   writer.pyi
|           |       |       |   |   |   __init__.pyi
|           |       |       |   |   |   
|           |       |       |   |   \---operations
|           |       |       |   |           base.pyi
|           |       |       |   |           fields.pyi
|           |       |       |   |           models.pyi
|           |       |       |   |           special.pyi
|           |       |       |   |           utils.pyi
|           |       |       |   |           __init__.pyi
|           |       |       |   |           
|           |       |       |   \---models
|           |       |       |       |   aggregates.pyi
|           |       |       |       |   base.pyi
|           |       |       |       |   constraints.pyi
|           |       |       |       |   deletion.pyi
|           |       |       |       |   enums.pyi
|           |       |       |       |   expressions.pyi
|           |       |       |       |   indexes.pyi
|           |       |       |       |   lookups.pyi
|           |       |       |       |   manager.pyi
|           |       |       |       |   options.pyi
|           |       |       |       |   query.pyi
|           |       |       |       |   query_utils.pyi
|           |       |       |       |   signals.pyi
|           |       |       |       |   utils.pyi
|           |       |       |       |   __init__.pyi
|           |       |       |       |   
|           |       |       |       +---fields
|           |       |       |       |       files.pyi
|           |       |       |       |       mixins.pyi
|           |       |       |       |       proxy.pyi
|           |       |       |       |       related.pyi
|           |       |       |       |       related_descriptors.pyi
|           |       |       |       |       related_lookups.pyi
|           |       |       |       |       reverse_related.pyi
|           |       |       |       |       __init__.pyi
|           |       |       |       |       
|           |       |       |       +---functions
|           |       |       |       |       comparison.pyi
|           |       |       |       |       datetime.pyi
|           |       |       |       |       math.pyi
|           |       |       |       |       mixins.pyi
|           |       |       |       |       text.pyi
|           |       |       |       |       window.pyi
|           |       |       |       |       __init__.pyi
|           |       |       |       |       
|           |       |       |       \---sql
|           |       |       |               compiler.pyi
|           |       |       |               constants.pyi
|           |       |       |               datastructures.pyi
|           |       |       |               query.pyi
|           |       |       |               subqueries.pyi
|           |       |       |               where.pyi
|           |       |       |               __init__.pyi
|           |       |       |               
|           |       |       +---dispatch
|           |       |       |       dispatcher.pyi
|           |       |       |       __init__.pyi
|           |       |       |       
|           |       |       +---forms
|           |       |       |       boundfield.pyi
|           |       |       |       fields.pyi
|           |       |       |       forms.pyi
|           |       |       |       formsets.pyi
|           |       |       |       models.pyi
|           |       |       |       renderers.pyi
|           |       |       |       utils.pyi
|           |       |       |       widgets.pyi
|           |       |       |       __init__.pyi
|           |       |       |       
|           |       |       +---http
|           |       |       |       cookie.pyi
|           |       |       |       multipartparser.pyi
|           |       |       |       request.pyi
|           |       |       |       response.pyi
|           |       |       |       __init__.pyi
|           |       |       |       
|           |       |       +---middleware
|           |       |       |       cache.pyi
|           |       |       |       clickjacking.pyi
|           |       |       |       common.pyi
|           |       |       |       csrf.pyi
|           |       |       |       gzip.pyi
|           |       |       |       http.pyi
|           |       |       |       locale.pyi
|           |       |       |       security.pyi
|           |       |       |       __init__.pyi
|           |       |       |       
|           |       |       +---template
|           |       |       |   |   base.pyi
|           |       |       |   |   context.pyi
|           |       |       |   |   context_processors.pyi
|           |       |       |   |   defaultfilters.pyi
|           |       |       |   |   defaulttags.pyi
|           |       |       |   |   engine.pyi
|           |       |       |   |   exceptions.pyi
|           |       |       |   |   library.pyi
|           |       |       |   |   loader.pyi
|           |       |       |   |   loader_tags.pyi
|           |       |       |   |   response.pyi
|           |       |       |   |   smartif.pyi
|           |       |       |   |   utils.pyi
|           |       |       |   |   __init__.pyi
|           |       |       |   |   
|           |       |       |   +---backends
|           |       |       |   |       base.pyi
|           |       |       |   |       django.pyi
|           |       |       |   |       dummy.pyi
|           |       |       |   |       jinja2.pyi
|           |       |       |   |       utils.pyi
|           |       |       |   |       __init__.pyi
|           |       |       |   |       
|           |       |       |   \---loaders
|           |       |       |           app_directories.pyi
|           |       |       |           base.pyi
|           |       |       |           cached.pyi
|           |       |       |           filesystem.pyi
|           |       |       |           locmem.pyi
|           |       |       |           __init__.pyi
|           |       |       |           
|           |       |       +---templatetags
|           |       |       |       cache.pyi
|           |       |       |       i18n.pyi
|           |       |       |       l10n.pyi
|           |       |       |       static.pyi
|           |       |       |       tz.pyi
|           |       |       |       __init__.pyi
|           |       |       |       
|           |       |       +---test
|           |       |       |       client.pyi
|           |       |       |       html.pyi
|           |       |       |       runner.pyi
|           |       |       |       selenium.pyi
|           |       |       |       signals.pyi
|           |       |       |       testcases.pyi
|           |       |       |       utils.pyi
|           |       |       |       __init__.pyi
|           |       |       |       
|           |       |       +---urls
|           |       |       |       base.pyi
|           |       |       |       conf.pyi
|           |       |       |       converters.pyi
|           |       |       |       exceptions.pyi
|           |       |       |       resolvers.pyi
|           |       |       |       utils.pyi
|           |       |       |       __init__.pyi
|           |       |       |       
|           |       |       +---utils
|           |       |       |   |   archive.pyi
|           |       |       |   |   autoreload.pyi
|           |       |       |   |   baseconv.pyi
|           |       |       |   |   cache.pyi
|           |       |       |   |   crypto.pyi
|           |       |       |   |   datastructures.pyi
|           |       |       |   |   dateformat.pyi
|           |       |       |   |   dateparse.pyi
|           |       |       |   |   dates.pyi
|           |       |       |   |   datetime_safe.pyi
|           |       |       |   |   deconstruct.pyi
|           |       |       |   |   decorators.pyi
|           |       |       |   |   deprecation.pyi
|           |       |       |   |   duration.pyi
|           |       |       |   |   encoding.pyi
|           |       |       |   |   feedgenerator.pyi
|           |       |       |   |   formats.pyi
|           |       |       |   |   functional.pyi
|           |       |       |   |   hashable.pyi
|           |       |       |   |   html.pyi
|           |       |       |   |   http.pyi
|           |       |       |   |   inspect.pyi
|           |       |       |   |   ipv6.pyi
|           |       |       |   |   itercompat.pyi
|           |       |       |   |   jslex.pyi
|           |       |       |   |   log.pyi
|           |       |       |   |   lorem_ipsum.pyi
|           |       |       |   |   module_loading.pyi
|           |       |       |   |   numberformat.pyi
|           |       |       |   |   regex_helper.pyi
|           |       |       |   |   safestring.pyi
|           |       |       |   |   six.pyi
|           |       |       |   |   termcolors.pyi
|           |       |       |   |   text.pyi
|           |       |       |   |   timesince.pyi
|           |       |       |   |   timezone.pyi
|           |       |       |   |   topological_sort.pyi
|           |       |       |   |   tree.pyi
|           |       |       |   |   version.pyi
|           |       |       |   |   xmlutils.pyi
|           |       |       |   |   _os.pyi
|           |       |       |   |   __init__.pyi
|           |       |       |   |   
|           |       |       |   \---translation
|           |       |       |           reloader.pyi
|           |       |       |           template.pyi
|           |       |       |           trans_null.pyi
|           |       |       |           trans_real.pyi
|           |       |       |           __init__.pyi
|           |       |       |           
|           |       |       \---views
|           |       |           |   csrf.pyi
|           |       |           |   debug.pyi
|           |       |           |   defaults.pyi
|           |       |           |   i18n.pyi
|           |       |           |   static.pyi
|           |       |           |   __init__.pyi
|           |       |           |   
|           |       |           +---decorators
|           |       |           |       cache.pyi
|           |       |           |       clickjacking.pyi
|           |       |           |       csrf.pyi
|           |       |           |       debug.pyi
|           |       |           |       gzip.pyi
|           |       |           |       http.pyi
|           |       |           |       vary.pyi
|           |       |           |       __init__.pyi
|           |       |           |       
|           |       |           \---generic
|           |       |                   base.pyi
|           |       |                   dates.pyi
|           |       |                   detail.pyi
|           |       |                   edit.pyi
|           |       |                   list.pyi
|           |       |                   __init__.pyi
|           |       |                   
|           |       \---typeshed
|           |           |   LICENSE
|           |           |   
|           |           +---stdlib
|           |           |   +---2
|           |           |   |   |   abc.pyi
|           |           |   |   |   ast.pyi
|           |           |   |   |   atexit.pyi
|           |           |   |   |   BaseHTTPServer.pyi
|           |           |   |   |   builtins.pyi
|           |           |   |   |   CGIHTTPServer.pyi
|           |           |   |   |   collections.pyi
|           |           |   |   |   commands.pyi
|           |           |   |   |   compileall.pyi
|           |           |   |   |   ConfigParser.pyi
|           |           |   |   |   Cookie.pyi
|           |           |   |   |   cookielib.pyi
|           |           |   |   |   copy_reg.pyi
|           |           |   |   |   cPickle.pyi
|           |           |   |   |   cStringIO.pyi
|           |           |   |   |   dircache.pyi
|           |           |   |   |   dummy_thread.pyi
|           |           |   |   |   exceptions.pyi
|           |           |   |   |   fcntl.pyi
|           |           |   |   |   fnmatch.pyi
|           |           |   |   |   functools.pyi
|           |           |   |   |   future_builtins.pyi
|           |           |   |   |   gc.pyi
|           |           |   |   |   getopt.pyi
|           |           |   |   |   getpass.pyi
|           |           |   |   |   gettext.pyi
|           |           |   |   |   glob.pyi
|           |           |   |   |   gzip.pyi
|           |           |   |   |   hashlib.pyi
|           |           |   |   |   heapq.pyi
|           |           |   |   |   htmlentitydefs.pyi
|           |           |   |   |   HTMLParser.pyi
|           |           |   |   |   httplib.pyi
|           |           |   |   |   imp.pyi
|           |           |   |   |   importlib.pyi
|           |           |   |   |   inspect.pyi
|           |           |   |   |   io.pyi
|           |           |   |   |   itertools.pyi
|           |           |   |   |   json.pyi
|           |           |   |   |   markupbase.pyi
|           |           |   |   |   md5.pyi
|           |           |   |   |   mimetools.pyi
|           |           |   |   |   mutex.pyi
|           |           |   |   |   ntpath.pyi
|           |           |   |   |   nturl2path.pyi
|           |           |   |   |   os2emxpath.pyi
|           |           |   |   |   pipes.pyi
|           |           |   |   |   platform.pyi
|           |           |   |   |   popen2.pyi
|           |           |   |   |   posix.pyi
|           |           |   |   |   posixpath.pyi
|           |           |   |   |   Queue.pyi
|           |           |   |   |   random.pyi
|           |           |   |   |   re.pyi
|           |           |   |   |   repr.pyi
|           |           |   |   |   resource.pyi
|           |           |   |   |   rfc822.pyi
|           |           |   |   |   robotparser.pyi
|           |           |   |   |   runpy.pyi
|           |           |   |   |   sets.pyi
|           |           |   |   |   sha.pyi
|           |           |   |   |   shelve.pyi
|           |           |   |   |   shlex.pyi
|           |           |   |   |   signal.pyi
|           |           |   |   |   SimpleHTTPServer.pyi
|           |           |   |   |   smtplib.pyi
|           |           |   |   |   SocketServer.pyi
|           |           |   |   |   spwd.pyi
|           |           |   |   |   sre_constants.pyi
|           |           |   |   |   sre_parse.pyi
|           |           |   |   |   stat.pyi
|           |           |   |   |   string.pyi
|           |           |   |   |   StringIO.pyi
|           |           |   |   |   stringold.pyi
|           |           |   |   |   strop.pyi
|           |           |   |   |   subprocess.pyi
|           |           |   |   |   symbol.pyi
|           |           |   |   |   sys.pyi
|           |           |   |   |   tempfile.pyi
|           |           |   |   |   textwrap.pyi
|           |           |   |   |   thread.pyi
|           |           |   |   |   toaiff.pyi
|           |           |   |   |   tokenize.pyi
|           |           |   |   |   types.pyi
|           |           |   |   |   typing.pyi
|           |           |   |   |   unittest.pyi
|           |           |   |   |   urllib.pyi
|           |           |   |   |   urllib2.pyi
|           |           |   |   |   urlparse.pyi
|           |           |   |   |   user.pyi
|           |           |   |   |   UserDict.pyi
|           |           |   |   |   UserList.pyi
|           |           |   |   |   UserString.pyi
|           |           |   |   |   whichdb.pyi
|           |           |   |   |   xmlrpclib.pyi
|           |           |   |   |   _ast.pyi
|           |           |   |   |   _collections.pyi
|           |           |   |   |   _functools.pyi
|           |           |   |   |   _hotshot.pyi
|           |           |   |   |   _io.pyi
|           |           |   |   |   _json.pyi
|           |           |   |   |   _md5.pyi
|           |           |   |   |   _sha.pyi
|           |           |   |   |   _sha256.pyi
|           |           |   |   |   _sha512.pyi
|           |           |   |   |   _socket.pyi
|           |           |   |   |   _sre.pyi
|           |           |   |   |   _struct.pyi
|           |           |   |   |   _symtable.pyi
|           |           |   |   |   _threading_local.pyi
|           |           |   |   |   _winreg.pyi
|           |           |   |   |   __builtin__.pyi
|           |           |   |   |   
|           |           |   |   +---distutils
|           |           |   |   |   |   archive_util.pyi
|           |           |   |   |   |   bcppcompiler.pyi
|           |           |   |   |   |   ccompiler.pyi
|           |           |   |   |   |   cmd.pyi
|           |           |   |   |   |   config.pyi
|           |           |   |   |   |   core.pyi
|           |           |   |   |   |   cygwinccompiler.pyi
|           |           |   |   |   |   debug.pyi
|           |           |   |   |   |   dep_util.pyi
|           |           |   |   |   |   dir_util.pyi
|           |           |   |   |   |   dist.pyi
|           |           |   |   |   |   emxccompiler.pyi
|           |           |   |   |   |   errors.pyi
|           |           |   |   |   |   extension.pyi
|           |           |   |   |   |   fancy_getopt.pyi
|           |           |   |   |   |   filelist.pyi
|           |           |   |   |   |   file_util.pyi
|           |           |   |   |   |   log.pyi
|           |           |   |   |   |   msvccompiler.pyi
|           |           |   |   |   |   spawn.pyi
|           |           |   |   |   |   sysconfig.pyi
|           |           |   |   |   |   text_file.pyi
|           |           |   |   |   |   unixccompiler.pyi
|           |           |   |   |   |   util.pyi
|           |           |   |   |   |   version.pyi
|           |           |   |   |   |   __init__.pyi
|           |           |   |   |   |   
|           |           |   |   |   \---command
|           |           |   |   |           bdist.pyi
|           |           |   |   |           bdist_dumb.pyi
|           |           |   |   |           bdist_msi.pyi
|           |           |   |   |           bdist_packager.pyi
|           |           |   |   |           bdist_rpm.pyi
|           |           |   |   |           bdist_wininst.pyi
|           |           |   |   |           build.pyi
|           |           |   |   |           build_clib.pyi
|           |           |   |   |           build_ext.pyi
|           |           |   |   |           build_py.pyi
|           |           |   |   |           build_scripts.pyi
|           |           |   |   |           check.pyi
|           |           |   |   |           clean.pyi
|           |           |   |   |           config.pyi
|           |           |   |   |           install.pyi
|           |           |   |   |           install_data.pyi
|           |           |   |   |           install_egg_info.pyi
|           |           |   |   |           install_headers.pyi
|           |           |   |   |           install_lib.pyi
|           |           |   |   |           install_scripts.pyi
|           |           |   |   |           register.pyi
|           |           |   |   |           sdist.pyi
|           |           |   |   |           upload.pyi
|           |           |   |   |           __init__.pyi
|           |           |   |   |           
|           |           |   |   +---email
|           |           |   |   |   |   base64mime.pyi
|           |           |   |   |   |   charset.pyi
|           |           |   |   |   |   encoders.pyi
|           |           |   |   |   |   feedparser.pyi
|           |           |   |   |   |   generator.pyi
|           |           |   |   |   |   header.pyi
|           |           |   |   |   |   iterators.pyi
|           |           |   |   |   |   message.pyi
|           |           |   |   |   |   MIMEText.pyi
|           |           |   |   |   |   parser.pyi
|           |           |   |   |   |   quoprimime.pyi
|           |           |   |   |   |   utils.pyi
|           |           |   |   |   |   _parseaddr.pyi
|           |           |   |   |   |   __init__.pyi
|           |           |   |   |   |   
|           |           |   |   |   \---mime
|           |           |   |   |           application.pyi
|           |           |   |   |           audio.pyi
|           |           |   |   |           base.pyi
|           |           |   |   |           image.pyi
|           |           |   |   |           message.pyi
|           |           |   |   |           multipart.pyi
|           |           |   |   |           nonmultipart.pyi
|           |           |   |   |           text.pyi
|           |           |   |   |           __init__.pyi
|           |           |   |   |           
|           |           |   |   +---encodings
|           |           |   |   |       utf_8.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---multiprocessing
|           |           |   |   |   |   pool.pyi
|           |           |   |   |   |   process.pyi
|           |           |   |   |   |   util.pyi
|           |           |   |   |   |   __init__.pyi
|           |           |   |   |   |   
|           |           |   |   |   \---dummy
|           |           |   |   |           connection.pyi
|           |           |   |   |           __init__.pyi
|           |           |   |   |           
|           |           |   |   \---os
|           |           |   |           path.pyi
|           |           |   |           __init__.pyi
|           |           |   |           
|           |           |   +---2and3
|           |           |   |   |   aifc.pyi
|           |           |   |   |   antigravity.pyi
|           |           |   |   |   argparse.pyi
|           |           |   |   |   array.pyi
|           |           |   |   |   asynchat.pyi
|           |           |   |   |   asyncore.pyi
|           |           |   |   |   audioop.pyi
|           |           |   |   |   base64.pyi
|           |           |   |   |   bdb.pyi
|           |           |   |   |   binascii.pyi
|           |           |   |   |   binhex.pyi
|           |           |   |   |   bisect.pyi
|           |           |   |   |   bz2.pyi
|           |           |   |   |   calendar.pyi
|           |           |   |   |   cgi.pyi
|           |           |   |   |   cgitb.pyi
|           |           |   |   |   chunk.pyi
|           |           |   |   |   cmath.pyi
|           |           |   |   |   cmd.pyi
|           |           |   |   |   code.pyi
|           |           |   |   |   codecs.pyi
|           |           |   |   |   codeop.pyi
|           |           |   |   |   colorsys.pyi
|           |           |   |   |   contextlib.pyi
|           |           |   |   |   copy.pyi
|           |           |   |   |   cProfile.pyi
|           |           |   |   |   crypt.pyi
|           |           |   |   |   csv.pyi
|           |           |   |   |   datetime.pyi
|           |           |   |   |   decimal.pyi
|           |           |   |   |   difflib.pyi
|           |           |   |   |   dis.pyi
|           |           |   |   |   doctest.pyi
|           |           |   |   |   dummy_threading.pyi
|           |           |   |   |   errno.pyi
|           |           |   |   |   filecmp.pyi
|           |           |   |   |   fileinput.pyi
|           |           |   |   |   formatter.pyi
|           |           |   |   |   fractions.pyi
|           |           |   |   |   ftplib.pyi
|           |           |   |   |   genericpath.pyi
|           |           |   |   |   grp.pyi
|           |           |   |   |   hmac.pyi
|           |           |   |   |   imaplib.pyi
|           |           |   |   |   imghdr.pyi
|           |           |   |   |   keyword.pyi
|           |           |   |   |   linecache.pyi
|           |           |   |   |   locale.pyi
|           |           |   |   |   macpath.pyi
|           |           |   |   |   mailbox.pyi
|           |           |   |   |   mailcap.pyi
|           |           |   |   |   marshal.pyi
|           |           |   |   |   math.pyi
|           |           |   |   |   mimetypes.pyi
|           |           |   |   |   mmap.pyi
|           |           |   |   |   modulefinder.pyi
|           |           |   |   |   msvcrt.pyi
|           |           |   |   |   netrc.pyi
|           |           |   |   |   nis.pyi
|           |           |   |   |   numbers.pyi
|           |           |   |   |   opcode.pyi
|           |           |   |   |   operator.pyi
|           |           |   |   |   optparse.pyi
|           |           |   |   |   parser.pyi
|           |           |   |   |   pdb.pyi
|           |           |   |   |   pickle.pyi
|           |           |   |   |   pickletools.pyi
|           |           |   |   |   pkgutil.pyi
|           |           |   |   |   plistlib.pyi
|           |           |   |   |   poplib.pyi
|           |           |   |   |   pprint.pyi
|           |           |   |   |   profile.pyi
|           |           |   |   |   pstats.pyi
|           |           |   |   |   pty.pyi
|           |           |   |   |   pwd.pyi
|           |           |   |   |   pyclbr.pyi
|           |           |   |   |   pydoc.pyi
|           |           |   |   |   py_compile.pyi
|           |           |   |   |   quopri.pyi
|           |           |   |   |   readline.pyi
|           |           |   |   |   rlcompleter.pyi
|           |           |   |   |   sched.pyi
|           |           |   |   |   select.pyi
|           |           |   |   |   shutil.pyi
|           |           |   |   |   site.pyi
|           |           |   |   |   smtpd.pyi
|           |           |   |   |   sndhdr.pyi
|           |           |   |   |   socket.pyi
|           |           |   |   |   sre_compile.pyi
|           |           |   |   |   ssl.pyi
|           |           |   |   |   stringprep.pyi
|           |           |   |   |   struct.pyi
|           |           |   |   |   sunau.pyi
|           |           |   |   |   symtable.pyi
|           |           |   |   |   sysconfig.pyi
|           |           |   |   |   syslog.pyi
|           |           |   |   |   tabnanny.pyi
|           |           |   |   |   tarfile.pyi
|           |           |   |   |   telnetlib.pyi
|           |           |   |   |   termios.pyi
|           |           |   |   |   this.pyi
|           |           |   |   |   threading.pyi
|           |           |   |   |   time.pyi
|           |           |   |   |   timeit.pyi
|           |           |   |   |   token.pyi
|           |           |   |   |   trace.pyi
|           |           |   |   |   traceback.pyi
|           |           |   |   |   tty.pyi
|           |           |   |   |   turtle.pyi
|           |           |   |   |   unicodedata.pyi
|           |           |   |   |   uu.pyi
|           |           |   |   |   uuid.pyi
|           |           |   |   |   warnings.pyi
|           |           |   |   |   wave.pyi
|           |           |   |   |   weakref.pyi
|           |           |   |   |   webbrowser.pyi
|           |           |   |   |   winsound.pyi
|           |           |   |   |   xdrlib.pyi
|           |           |   |   |   zipfile.pyi
|           |           |   |   |   zipimport.pyi
|           |           |   |   |   zlib.pyi
|           |           |   |   |   _bisect.pyi
|           |           |   |   |   _codecs.pyi
|           |           |   |   |   _csv.pyi
|           |           |   |   |   _curses.pyi
|           |           |   |   |   _dummy_threading.pyi
|           |           |   |   |   _heapq.pyi
|           |           |   |   |   _msi.pyi
|           |           |   |   |   _random.pyi
|           |           |   |   |   _warnings.pyi
|           |           |   |   |   _weakref.pyi
|           |           |   |   |   _weakrefset.pyi
|           |           |   |   |   __future__.pyi
|           |           |   |   |   
|           |           |   |   +---ctypes
|           |           |   |   |       util.pyi
|           |           |   |   |       wintypes.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---curses
|           |           |   |   |       ascii.pyi
|           |           |   |   |       panel.pyi
|           |           |   |   |       textpad.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---ensurepip
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---lib2to3
|           |           |   |   |   |   pygram.pyi
|           |           |   |   |   |   pytree.pyi
|           |           |   |   |   |   __init__.pyi
|           |           |   |   |   |   
|           |           |   |   |   \---pgen2
|           |           |   |   |           driver.pyi
|           |           |   |   |           grammar.pyi
|           |           |   |   |           literals.pyi
|           |           |   |   |           parse.pyi
|           |           |   |   |           pgen.pyi
|           |           |   |   |           token.pyi
|           |           |   |   |           tokenize.pyi
|           |           |   |   |           __init__.pyi
|           |           |   |   |           
|           |           |   |   +---logging
|           |           |   |   |       config.pyi
|           |           |   |   |       handlers.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---msilib
|           |           |   |   |       schema.pyi
|           |           |   |   |       sequence.pyi
|           |           |   |   |       text.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---pydoc_data
|           |           |   |   |       topics.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---pyexpat
|           |           |   |   |       errors.pyi
|           |           |   |   |       model.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---sqlite3
|           |           |   |   |       dbapi2.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---wsgiref
|           |           |   |   |       handlers.pyi
|           |           |   |   |       headers.pyi
|           |           |   |   |       simple_server.pyi
|           |           |   |   |       types.pyi
|           |           |   |   |       util.pyi
|           |           |   |   |       validate.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---xml
|           |           |   |   |   |   __init__.pyi
|           |           |   |   |   |   
|           |           |   |   |   +---dom
|           |           |   |   |   |       domreg.pyi
|           |           |   |   |   |       expatbuilder.pyi
|           |           |   |   |   |       minicompat.pyi
|           |           |   |   |   |       minidom.pyi
|           |           |   |   |   |       NodeFilter.pyi
|           |           |   |   |   |       pulldom.pyi
|           |           |   |   |   |       xmlbuilder.pyi
|           |           |   |   |   |       __init__.pyi
|           |           |   |   |   |       
|           |           |   |   |   +---etree
|           |           |   |   |   |       cElementTree.pyi
|           |           |   |   |   |       ElementInclude.pyi
|           |           |   |   |   |       ElementPath.pyi
|           |           |   |   |   |       ElementTree.pyi
|           |           |   |   |   |       __init__.pyi
|           |           |   |   |   |       
|           |           |   |   |   +---parsers
|           |           |   |   |   |   |   __init__.pyi
|           |           |   |   |   |   |   
|           |           |   |   |   |   \---expat
|           |           |   |   |   |           errors.pyi
|           |           |   |   |   |           model.pyi
|           |           |   |   |   |           __init__.pyi
|           |           |   |   |   |           
|           |           |   |   |   \---sax
|           |           |   |   |           handler.pyi
|           |           |   |   |           saxutils.pyi
|           |           |   |   |           xmlreader.pyi
|           |           |   |   |           __init__.pyi
|           |           |   |   |           
|           |           |   |   \---_typeshed
|           |           |   |           wsgi.pyi
|           |           |   |           xml.pyi
|           |           |   |           __init__.pyi
|           |           |   |           
|           |           |   +---3
|           |           |   |   |   abc.pyi
|           |           |   |   |   ast.pyi
|           |           |   |   |   atexit.pyi
|           |           |   |   |   builtins.pyi
|           |           |   |   |   compileall.pyi
|           |           |   |   |   configparser.pyi
|           |           |   |   |   copyreg.pyi
|           |           |   |   |   enum.pyi
|           |           |   |   |   faulthandler.pyi
|           |           |   |   |   fcntl.pyi
|           |           |   |   |   fnmatch.pyi
|           |           |   |   |   functools.pyi
|           |           |   |   |   gc.pyi
|           |           |   |   |   getopt.pyi
|           |           |   |   |   getpass.pyi
|           |           |   |   |   gettext.pyi
|           |           |   |   |   glob.pyi
|           |           |   |   |   gzip.pyi
|           |           |   |   |   hashlib.pyi
|           |           |   |   |   heapq.pyi
|           |           |   |   |   imp.pyi
|           |           |   |   |   inspect.pyi
|           |           |   |   |   io.pyi
|           |           |   |   |   ipaddress.pyi
|           |           |   |   |   itertools.pyi
|           |           |   |   |   lzma.pyi
|           |           |   |   |   macurl2path.pyi
|           |           |   |   |   nntplib.pyi
|           |           |   |   |   ntpath.pyi
|           |           |   |   |   nturl2path.pyi
|           |           |   |   |   pathlib.pyi
|           |           |   |   |   pipes.pyi
|           |           |   |   |   platform.pyi
|           |           |   |   |   posix.pyi
|           |           |   |   |   posixpath.pyi
|           |           |   |   |   queue.pyi
|           |           |   |   |   random.pyi
|           |           |   |   |   re.pyi
|           |           |   |   |   reprlib.pyi
|           |           |   |   |   resource.pyi
|           |           |   |   |   runpy.pyi
|           |           |   |   |   secrets.pyi
|           |           |   |   |   selectors.pyi
|           |           |   |   |   shelve.pyi
|           |           |   |   |   shlex.pyi
|           |           |   |   |   signal.pyi
|           |           |   |   |   smtplib.pyi
|           |           |   |   |   socketserver.pyi
|           |           |   |   |   spwd.pyi
|           |           |   |   |   sre_constants.pyi
|           |           |   |   |   sre_parse.pyi
|           |           |   |   |   stat.pyi
|           |           |   |   |   statistics.pyi
|           |           |   |   |   string.pyi
|           |           |   |   |   subprocess.pyi
|           |           |   |   |   symbol.pyi
|           |           |   |   |   sys.pyi
|           |           |   |   |   tempfile.pyi
|           |           |   |   |   textwrap.pyi
|           |           |   |   |   tokenize.pyi
|           |           |   |   |   tracemalloc.pyi
|           |           |   |   |   types.pyi
|           |           |   |   |   typing.pyi
|           |           |   |   |   winreg.pyi
|           |           |   |   |   xxlimited.pyi
|           |           |   |   |   zipapp.pyi
|           |           |   |   |   _ast.pyi
|           |           |   |   |   _bootlocale.pyi
|           |           |   |   |   _compat_pickle.pyi
|           |           |   |   |   _compression.pyi
|           |           |   |   |   _decimal.pyi
|           |           |   |   |   _dummy_thread.pyi
|           |           |   |   |   _imp.pyi
|           |           |   |   |   _importlib_modulespec.pyi
|           |           |   |   |   _json.pyi
|           |           |   |   |   _markupbase.pyi
|           |           |   |   |   _operator.pyi
|           |           |   |   |   _osx_support.pyi
|           |           |   |   |   _posixsubprocess.pyi
|           |           |   |   |   _pydecimal.pyi
|           |           |   |   |   _sitebuiltins.pyi
|           |           |   |   |   _stat.pyi
|           |           |   |   |   _thread.pyi
|           |           |   |   |   _threading_local.pyi
|           |           |   |   |   _tkinter.pyi
|           |           |   |   |   _tracemalloc.pyi
|           |           |   |   |   _winapi.pyi
|           |           |   |   |   
|           |           |   |   +---asyncio
|           |           |   |   |       base_events.pyi
|           |           |   |   |       base_futures.pyi
|           |           |   |   |       base_subprocess.pyi
|           |           |   |   |       base_tasks.pyi
|           |           |   |   |       compat.pyi
|           |           |   |   |       constants.pyi
|           |           |   |   |       coroutines.pyi
|           |           |   |   |       events.pyi
|           |           |   |   |       exceptions.pyi
|           |           |   |   |       format_helpers.pyi
|           |           |   |   |       futures.pyi
|           |           |   |   |       locks.pyi
|           |           |   |   |       log.pyi
|           |           |   |   |       proactor_events.pyi
|           |           |   |   |       protocols.pyi
|           |           |   |   |       queues.pyi
|           |           |   |   |       runners.pyi
|           |           |   |   |       selector_events.pyi
|           |           |   |   |       sslproto.pyi
|           |           |   |   |       staggered.pyi
|           |           |   |   |       streams.pyi
|           |           |   |   |       subprocess.pyi
|           |           |   |   |       tasks.pyi
|           |           |   |   |       threads.pyi
|           |           |   |   |       transports.pyi
|           |           |   |   |       trsock.pyi
|           |           |   |   |       unix_events.pyi
|           |           |   |   |       windows_events.pyi
|           |           |   |   |       windows_utils.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---collections
|           |           |   |   |       abc.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---concurrent
|           |           |   |   |   |   __init__.pyi
|           |           |   |   |   |   
|           |           |   |   |   \---futures
|           |           |   |   |           process.pyi
|           |           |   |   |           thread.pyi
|           |           |   |   |           _base.pyi
|           |           |   |   |           __init__.pyi
|           |           |   |   |           
|           |           |   |   +---dbm
|           |           |   |   |       dumb.pyi
|           |           |   |   |       gnu.pyi
|           |           |   |   |       ndbm.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---distutils
|           |           |   |   |   |   archive_util.pyi
|           |           |   |   |   |   bcppcompiler.pyi
|           |           |   |   |   |   ccompiler.pyi
|           |           |   |   |   |   cmd.pyi
|           |           |   |   |   |   config.pyi
|           |           |   |   |   |   core.pyi
|           |           |   |   |   |   cygwinccompiler.pyi
|           |           |   |   |   |   debug.pyi
|           |           |   |   |   |   dep_util.pyi
|           |           |   |   |   |   dir_util.pyi
|           |           |   |   |   |   dist.pyi
|           |           |   |   |   |   errors.pyi
|           |           |   |   |   |   extension.pyi
|           |           |   |   |   |   fancy_getopt.pyi
|           |           |   |   |   |   filelist.pyi
|           |           |   |   |   |   file_util.pyi
|           |           |   |   |   |   log.pyi
|           |           |   |   |   |   msvccompiler.pyi
|           |           |   |   |   |   spawn.pyi
|           |           |   |   |   |   sysconfig.pyi
|           |           |   |   |   |   text_file.pyi
|           |           |   |   |   |   unixccompiler.pyi
|           |           |   |   |   |   util.pyi
|           |           |   |   |   |   version.pyi
|           |           |   |   |   |   __init__.pyi
|           |           |   |   |   |   
|           |           |   |   |   \---command
|           |           |   |   |           bdist.pyi
|           |           |   |   |           bdist_dumb.pyi
|           |           |   |   |           bdist_msi.pyi
|           |           |   |   |           bdist_packager.pyi
|           |           |   |   |           bdist_rpm.pyi
|           |           |   |   |           bdist_wininst.pyi
|           |           |   |   |           build.pyi
|           |           |   |   |           build_clib.pyi
|           |           |   |   |           build_ext.pyi
|           |           |   |   |           build_py.pyi
|           |           |   |   |           build_scripts.pyi
|           |           |   |   |           check.pyi
|           |           |   |   |           clean.pyi
|           |           |   |   |           config.pyi
|           |           |   |   |           install.pyi
|           |           |   |   |           install_data.pyi
|           |           |   |   |           install_egg_info.pyi
|           |           |   |   |           install_headers.pyi
|           |           |   |   |           install_lib.pyi
|           |           |   |   |           install_scripts.pyi
|           |           |   |   |           register.pyi
|           |           |   |   |           sdist.pyi
|           |           |   |   |           upload.pyi
|           |           |   |   |           __init__.pyi
|           |           |   |   |           
|           |           |   |   +---email
|           |           |   |   |   |   charset.pyi
|           |           |   |   |   |   contentmanager.pyi
|           |           |   |   |   |   encoders.pyi
|           |           |   |   |   |   errors.pyi
|           |           |   |   |   |   feedparser.pyi
|           |           |   |   |   |   generator.pyi
|           |           |   |   |   |   header.pyi
|           |           |   |   |   |   headerregistry.pyi
|           |           |   |   |   |   iterators.pyi
|           |           |   |   |   |   message.pyi
|           |           |   |   |   |   parser.pyi
|           |           |   |   |   |   policy.pyi
|           |           |   |   |   |   utils.pyi
|           |           |   |   |   |   __init__.pyi
|           |           |   |   |   |   
|           |           |   |   |   \---mime
|           |           |   |   |           application.pyi
|           |           |   |   |           audio.pyi
|           |           |   |   |           base.pyi
|           |           |   |   |           image.pyi
|           |           |   |   |           message.pyi
|           |           |   |   |           multipart.pyi
|           |           |   |   |           nonmultipart.pyi
|           |           |   |   |           text.pyi
|           |           |   |   |           __init__.pyi
|           |           |   |   |           
|           |           |   |   +---encodings
|           |           |   |   |       utf_8.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---html
|           |           |   |   |       entities.pyi
|           |           |   |   |       parser.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---http
|           |           |   |   |       client.pyi
|           |           |   |   |       cookiejar.pyi
|           |           |   |   |       cookies.pyi
|           |           |   |   |       server.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---importlib
|           |           |   |   |       abc.pyi
|           |           |   |   |       machinery.pyi
|           |           |   |   |       metadata.pyi
|           |           |   |   |       resources.pyi
|           |           |   |   |       util.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---json
|           |           |   |   |       decoder.pyi
|           |           |   |   |       encoder.pyi
|           |           |   |   |       tool.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---multiprocessing
|           |           |   |   |   |   connection.pyi
|           |           |   |   |   |   context.pyi
|           |           |   |   |   |   managers.pyi
|           |           |   |   |   |   pool.pyi
|           |           |   |   |   |   process.pyi
|           |           |   |   |   |   queues.pyi
|           |           |   |   |   |   sharedctypes.pyi
|           |           |   |   |   |   shared_memory.pyi
|           |           |   |   |   |   spawn.pyi
|           |           |   |   |   |   synchronize.pyi
|           |           |   |   |   |   __init__.pyi
|           |           |   |   |   |   
|           |           |   |   |   \---dummy
|           |           |   |   |           connection.pyi
|           |           |   |   |           __init__.pyi
|           |           |   |   |           
|           |           |   |   +---os
|           |           |   |   |       path.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---tkinter
|           |           |   |   |       commondialog.pyi
|           |           |   |   |       constants.pyi
|           |           |   |   |       dialog.pyi
|           |           |   |   |       filedialog.pyi
|           |           |   |   |       font.pyi
|           |           |   |   |       messagebox.pyi
|           |           |   |   |       ttk.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---unittest
|           |           |   |   |       async_case.pyi
|           |           |   |   |       case.pyi
|           |           |   |   |       loader.pyi
|           |           |   |   |       main.pyi
|           |           |   |   |       mock.pyi
|           |           |   |   |       result.pyi
|           |           |   |   |       runner.pyi
|           |           |   |   |       signals.pyi
|           |           |   |   |       suite.pyi
|           |           |   |   |       util.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---urllib
|           |           |   |   |       error.pyi
|           |           |   |   |       parse.pyi
|           |           |   |   |       request.pyi
|           |           |   |   |       response.pyi
|           |           |   |   |       robotparser.pyi
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   +---venv
|           |           |   |   |       __init__.pyi
|           |           |   |   |       
|           |           |   |   \---xmlrpc
|           |           |   |           client.pyi
|           |           |   |           server.pyi
|           |           |   |           __init__.pyi
|           |           |   |           
|           |           |   +---3.7
|           |           |   |       contextvars.pyi
|           |           |   |       dataclasses.pyi
|           |           |   |       _py_abc.pyi
|           |           |   |       
|           |           |   \---3.9
|           |           |       |   graphlib.pyi
|           |           |       |   
|           |           |       \---zoneinfo
|           |           |               __init__.pyi
|           |           |               
|           |           \---third_party
|           |               +---2
|           |               |   |   enum.pyi
|           |               |   |   ipaddress.pyi
|           |               |   |   pathlib2.pyi
|           |               |   |   pymssql.pyi
|           |               |   |   
|           |               |   +---concurrent
|           |               |   |   |   __init__.pyi
|           |               |   |   |   
|           |               |   |   \---futures
|           |               |   |           process.pyi
|           |               |   |           thread.pyi
|           |               |   |           _base.pyi
|           |               |   |           __init__.pyi
|           |               |   |           
|           |               |   +---fb303
|           |               |   |       FacebookService.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---kazoo
|           |               |   |   |   client.pyi
|           |               |   |   |   exceptions.pyi
|           |               |   |   |   __init__.pyi
|           |               |   |   |   
|           |               |   |   \---recipe
|           |               |   |           watchers.pyi
|           |               |   |           __init__.pyi
|           |               |   |           
|           |               |   +---OpenSSL
|           |               |   |       crypto.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---routes
|           |               |   |       mapper.pyi
|           |               |   |       util.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---scribe
|           |               |   |       scribe.pyi
|           |               |   |       ttypes.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---six
|           |               |   |   |   __init__.pyi
|           |               |   |   |   
|           |               |   |   \---moves
|           |               |   |       |   BaseHTTPServer.pyi
|           |               |   |       |   CGIHTTPServer.pyi
|           |               |   |       |   collections_abc.pyi
|           |               |   |       |   configparser.pyi
|           |               |   |       |   cPickle.pyi
|           |               |   |       |   email_mime_base.pyi
|           |               |   |       |   email_mime_multipart.pyi
|           |               |   |       |   email_mime_nonmultipart.pyi
|           |               |   |       |   email_mime_text.pyi
|           |               |   |       |   html_entities.pyi
|           |               |   |       |   html_parser.pyi
|           |               |   |       |   http_client.pyi
|           |               |   |       |   http_cookiejar.pyi
|           |               |   |       |   http_cookies.pyi
|           |               |   |       |   queue.pyi
|           |               |   |       |   reprlib.pyi
|           |               |   |       |   SimpleHTTPServer.pyi
|           |               |   |       |   socketserver.pyi
|           |               |   |       |   urllib_error.pyi
|           |               |   |       |   urllib_parse.pyi
|           |               |   |       |   urllib_request.pyi
|           |               |   |       |   urllib_response.pyi
|           |               |   |       |   urllib_robotparser.pyi
|           |               |   |       |   xmlrpc_client.pyi
|           |               |   |       |   _dummy_thread.pyi
|           |               |   |       |   _thread.pyi
|           |               |   |       |   __init__.pyi
|           |               |   |       |   
|           |               |   |       \---urllib
|           |               |   |               error.pyi
|           |               |   |               parse.pyi
|           |               |   |               request.pyi
|           |               |   |               response.pyi
|           |               |   |               robotparser.pyi
|           |               |   |               __init__.pyi
|           |               |   |               
|           |               |   \---tornado
|           |               |           concurrent.pyi
|           |               |           gen.pyi
|           |               |           httpclient.pyi
|           |               |           httpserver.pyi
|           |               |           httputil.pyi
|           |               |           ioloop.pyi
|           |               |           locks.pyi
|           |               |           netutil.pyi
|           |               |           process.pyi
|           |               |           tcpserver.pyi
|           |               |           testing.pyi
|           |               |           util.pyi
|           |               |           web.pyi
|           |               |           __init__.pyi
|           |               |           
|           |               +---2and3
|           |               |   |   backports_abc.pyi
|           |               |   |   certifi.pyi
|           |               |   |   croniter.pyi
|           |               |   |   dateparser.pyi
|           |               |   |   decorator.pyi
|           |               |   |   first.pyi
|           |               |   |   gflags.pyi
|           |               |   |   itsdangerous.pyi
|           |               |   |   mock.pyi
|           |               |   |   mypy_extensions.pyi
|           |               |   |   polib.pyi
|           |               |   |   pycurl.pyi
|           |               |   |   pyre_extensions.pyi
|           |               |   |   singledispatch.pyi
|           |               |   |   tabulate.pyi
|           |               |   |   termcolor.pyi
|           |               |   |   toml.pyi
|           |               |   |   typing_extensions.pyi
|           |               |   |   ujson.pyi
|           |               |   |   
|           |               |   +---atomicwrites
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---attr
|           |               |   |       converters.pyi
|           |               |   |       exceptions.pyi
|           |               |   |       filters.pyi
|           |               |   |       validators.pyi
|           |               |   |       _version_info.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---backports
|           |               |   |       ssl_match_hostname.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---bleach
|           |               |   |       callbacks.pyi
|           |               |   |       linkifier.pyi
|           |               |   |       sanitizer.pyi
|           |               |   |       utils.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---boto
|           |               |   |   |   auth.pyi
|           |               |   |   |   auth_handler.pyi
|           |               |   |   |   compat.pyi
|           |               |   |   |   connection.pyi
|           |               |   |   |   exception.pyi
|           |               |   |   |   plugin.pyi
|           |               |   |   |   regioninfo.pyi
|           |               |   |   |   utils.pyi
|           |               |   |   |   __init__.pyi
|           |               |   |   |   
|           |               |   |   +---ec2
|           |               |   |   |       __init__.pyi
|           |               |   |   |       
|           |               |   |   +---elb
|           |               |   |   |       __init__.pyi
|           |               |   |   |       
|           |               |   |   +---kms
|           |               |   |   |       exceptions.pyi
|           |               |   |   |       layer1.pyi
|           |               |   |   |       __init__.pyi
|           |               |   |   |       
|           |               |   |   \---s3
|           |               |   |           acl.pyi
|           |               |   |           bucket.pyi
|           |               |   |           bucketlistresultset.pyi
|           |               |   |           bucketlogging.pyi
|           |               |   |           connection.pyi
|           |               |   |           cors.pyi
|           |               |   |           deletemarker.pyi
|           |               |   |           key.pyi
|           |               |   |           keyfile.pyi
|           |               |   |           lifecycle.pyi
|           |               |   |           multidelete.pyi
|           |               |   |           multipart.pyi
|           |               |   |           prefix.pyi
|           |               |   |           tagging.pyi
|           |               |   |           user.pyi
|           |               |   |           website.pyi
|           |               |   |           __init__.pyi
|           |               |   |           
|           |               |   +---cachetools
|           |               |   |       abc.pyi
|           |               |   |       cache.pyi
|           |               |   |       decorators.pyi
|           |               |   |       func.pyi
|           |               |   |       lfu.pyi
|           |               |   |       lru.pyi
|           |               |   |       rr.pyi
|           |               |   |       ttl.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---characteristic
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---chardet
|           |               |   |       enums.pyi
|           |               |   |       langbulgarianmodel.pyi
|           |               |   |       langcyrillicmodel.pyi
|           |               |   |       langgreekmodel.pyi
|           |               |   |       langhebrewmodel.pyi
|           |               |   |       langhungarianmodel.pyi
|           |               |   |       langthaimodel.pyi
|           |               |   |       langturkishmodel.pyi
|           |               |   |       universaldetector.pyi
|           |               |   |       version.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---click
|           |               |   |       core.pyi
|           |               |   |       decorators.pyi
|           |               |   |       exceptions.pyi
|           |               |   |       formatting.pyi
|           |               |   |       globals.pyi
|           |               |   |       parser.pyi
|           |               |   |       termui.pyi
|           |               |   |       testing.pyi
|           |               |   |       types.pyi
|           |               |   |       utils.pyi
|           |               |   |       _termui_impl.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---cryptography
|           |               |   |   |   exceptions.pyi
|           |               |   |   |   fernet.pyi
|           |               |   |   |   __init__.pyi
|           |               |   |   |   
|           |               |   |   +---hazmat
|           |               |   |   |   |   __init__.pyi
|           |               |   |   |   |   
|           |               |   |   |   +---backends
|           |               |   |   |   |       interfaces.pyi
|           |               |   |   |   |       __init__.pyi
|           |               |   |   |   |       
|           |               |   |   |   +---bindings
|           |               |   |   |   |   |   __init__.pyi
|           |               |   |   |   |   |   
|           |               |   |   |   |   \---openssl
|           |               |   |   |   |           binding.pyi
|           |               |   |   |   |           __init__.pyi
|           |               |   |   |   |           
|           |               |   |   |   \---primitives
|           |               |   |   |       |   cmac.pyi
|           |               |   |   |       |   constant_time.pyi
|           |               |   |   |       |   hashes.pyi
|           |               |   |   |       |   hmac.pyi
|           |               |   |   |       |   keywrap.pyi
|           |               |   |   |       |   padding.pyi
|           |               |   |   |       |   poly1305.pyi
|           |               |   |   |       |   __init__.pyi
|           |               |   |   |       |   
|           |               |   |   |       +---asymmetric
|           |               |   |   |       |       dh.pyi
|           |               |   |   |       |       dsa.pyi
|           |               |   |   |       |       ec.pyi
|           |               |   |   |       |       ed25519.pyi
|           |               |   |   |       |       ed448.pyi
|           |               |   |   |       |       padding.pyi
|           |               |   |   |       |       rsa.pyi
|           |               |   |   |       |       utils.pyi
|           |               |   |   |       |       x25519.pyi
|           |               |   |   |       |       x448.pyi
|           |               |   |   |       |       __init__.pyi
|           |               |   |   |       |       
|           |               |   |   |       +---ciphers
|           |               |   |   |       |       aead.pyi
|           |               |   |   |       |       algorithms.pyi
|           |               |   |   |       |       modes.pyi
|           |               |   |   |       |       __init__.pyi
|           |               |   |   |       |       
|           |               |   |   |       +---kdf
|           |               |   |   |       |       concatkdf.pyi
|           |               |   |   |       |       hkdf.pyi
|           |               |   |   |       |       kbkdf.pyi
|           |               |   |   |       |       pbkdf2.pyi
|           |               |   |   |       |       scrypt.pyi
|           |               |   |   |       |       x963kdf.pyi
|           |               |   |   |       |       __init__.pyi
|           |               |   |   |       |       
|           |               |   |   |       +---serialization
|           |               |   |   |       |       pkcs12.pyi
|           |               |   |   |       |       __init__.pyi
|           |               |   |   |       |       
|           |               |   |   |       \---twofactor
|           |               |   |   |               hotp.pyi
|           |               |   |   |               totp.pyi
|           |               |   |   |               __init__.pyi
|           |               |   |   |               
|           |               |   |   \---x509
|           |               |   |           extensions.pyi
|           |               |   |           oid.pyi
|           |               |   |           __init__.pyi
|           |               |   |           
|           |               |   +---datetimerange
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---dateutil
|           |               |   |   |   easter.pyi
|           |               |   |   |   parser.pyi
|           |               |   |   |   relativedelta.pyi
|           |               |   |   |   rrule.pyi
|           |               |   |   |   utils.pyi
|           |               |   |   |   _common.pyi
|           |               |   |   |   __init__.pyi
|           |               |   |   |   
|           |               |   |   \---tz
|           |               |   |           tz.pyi
|           |               |   |           _common.pyi
|           |               |   |           __init__.pyi
|           |               |   |           
|           |               |   +---deprecated
|           |               |   |       classic.pyi
|           |               |   |       sphinx.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---emoji
|           |               |   |       core.pyi
|           |               |   |       unicode_codes.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---flask
|           |               |   |   |   app.pyi
|           |               |   |   |   blueprints.pyi
|           |               |   |   |   cli.pyi
|           |               |   |   |   config.pyi
|           |               |   |   |   ctx.pyi
|           |               |   |   |   debughelpers.pyi
|           |               |   |   |   globals.pyi
|           |               |   |   |   helpers.pyi
|           |               |   |   |   logging.pyi
|           |               |   |   |   sessions.pyi
|           |               |   |   |   signals.pyi
|           |               |   |   |   templating.pyi
|           |               |   |   |   testing.pyi
|           |               |   |   |   views.pyi
|           |               |   |   |   wrappers.pyi
|           |               |   |   |   __init__.pyi
|           |               |   |   |   
|           |               |   |   \---json
|           |               |   |           tag.pyi
|           |               |   |           __init__.pyi
|           |               |   |           
|           |               |   +---geoip2
|           |               |   |       database.pyi
|           |               |   |       errors.pyi
|           |               |   |       mixins.pyi
|           |               |   |       models.pyi
|           |               |   |       records.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---google
|           |               |   |   |   __init__.pyi
|           |               |   |   |   
|           |               |   |   \---protobuf
|           |               |   |       |   any_pb2.pyi
|           |               |   |       |   api_pb2.pyi
|           |               |   |       |   descriptor.pyi
|           |               |   |       |   descriptor_pb2.pyi
|           |               |   |       |   descriptor_pool.pyi
|           |               |   |       |   duration_pb2.pyi
|           |               |   |       |   empty_pb2.pyi
|           |               |   |       |   field_mask_pb2.pyi
|           |               |   |       |   json_format.pyi
|           |               |   |       |   message.pyi
|           |               |   |       |   message_factory.pyi
|           |               |   |       |   reflection.pyi
|           |               |   |       |   service.pyi
|           |               |   |       |   source_context_pb2.pyi
|           |               |   |       |   struct_pb2.pyi
|           |               |   |       |   symbol_database.pyi
|           |               |   |       |   timestamp_pb2.pyi
|           |               |   |       |   type_pb2.pyi
|           |               |   |       |   wrappers_pb2.pyi
|           |               |   |       |   __init__.pyi
|           |               |   |       |   
|           |               |   |       +---compiler
|           |               |   |       |       plugin_pb2.pyi
|           |               |   |       |       __init__.pyi
|           |               |   |       |       
|           |               |   |       +---internal
|           |               |   |       |       containers.pyi
|           |               |   |       |       decoder.pyi
|           |               |   |       |       encoder.pyi
|           |               |   |       |       enum_type_wrapper.pyi
|           |               |   |       |       extension_dict.pyi
|           |               |   |       |       message_listener.pyi
|           |               |   |       |       python_message.pyi
|           |               |   |       |       well_known_types.pyi
|           |               |   |       |       wire_format.pyi
|           |               |   |       |       __init__.pyi
|           |               |   |       |       
|           |               |   |       \---util
|           |               |   |               __init__.pyi
|           |               |   |               
|           |               |   +---jinja2
|           |               |   |       bccache.pyi
|           |               |   |       compiler.pyi
|           |               |   |       constants.pyi
|           |               |   |       debug.pyi
|           |               |   |       defaults.pyi
|           |               |   |       environment.pyi
|           |               |   |       exceptions.pyi
|           |               |   |       ext.pyi
|           |               |   |       filters.pyi
|           |               |   |       lexer.pyi
|           |               |   |       loaders.pyi
|           |               |   |       meta.pyi
|           |               |   |       nodes.pyi
|           |               |   |       optimizer.pyi
|           |               |   |       parser.pyi
|           |               |   |       runtime.pyi
|           |               |   |       sandbox.pyi
|           |               |   |       tests.pyi
|           |               |   |       utils.pyi
|           |               |   |       visitor.pyi
|           |               |   |       _compat.pyi
|           |               |   |       _stringdefs.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---markdown
|           |               |   |   |   blockparser.pyi
|           |               |   |   |   blockprocessors.pyi
|           |               |   |   |   core.pyi
|           |               |   |   |   inlinepatterns.pyi
|           |               |   |   |   pep562.pyi
|           |               |   |   |   postprocessors.pyi
|           |               |   |   |   preprocessors.pyi
|           |               |   |   |   serializers.pyi
|           |               |   |   |   treeprocessors.pyi
|           |               |   |   |   util.pyi
|           |               |   |   |   __init__.pyi
|           |               |   |   |   __meta__.pyi
|           |               |   |   |   
|           |               |   |   \---extensions
|           |               |   |           abbr.pyi
|           |               |   |           admonition.pyi
|           |               |   |           attr_list.pyi
|           |               |   |           codehilite.pyi
|           |               |   |           def_list.pyi
|           |               |   |           extra.pyi
|           |               |   |           fenced_code.pyi
|           |               |   |           footnotes.pyi
|           |               |   |           legacy_attrs.pyi
|           |               |   |           legacy_em.pyi
|           |               |   |           md_in_html.pyi
|           |               |   |           meta.pyi
|           |               |   |           nl2br.pyi
|           |               |   |           sane_lists.pyi
|           |               |   |           smarty.pyi
|           |               |   |           tables.pyi
|           |               |   |           toc.pyi
|           |               |   |           wikilinks.pyi
|           |               |   |           __init__.pyi
|           |               |   |           
|           |               |   +---markupsafe
|           |               |   |       _compat.pyi
|           |               |   |       _constants.pyi
|           |               |   |       _native.pyi
|           |               |   |       _speedups.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---maxminddb
|           |               |   |       compat.pyi
|           |               |   |       const.pyi
|           |               |   |       decoder.pyi
|           |               |   |       errors.pyi
|           |               |   |       extension.pyi
|           |               |   |       reader.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---nmap
|           |               |   |       nmap.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---paramiko
|           |               |   |       agent.pyi
|           |               |   |       auth_handler.pyi
|           |               |   |       ber.pyi
|           |               |   |       buffered_pipe.pyi
|           |               |   |       channel.pyi
|           |               |   |       client.pyi
|           |               |   |       common.pyi
|           |               |   |       compress.pyi
|           |               |   |       config.pyi
|           |               |   |       dsskey.pyi
|           |               |   |       ecdsakey.pyi
|           |               |   |       ed25519key.pyi
|           |               |   |       file.pyi
|           |               |   |       hostkeys.pyi
|           |               |   |       kex_curve25519.pyi
|           |               |   |       kex_ecdh_nist.pyi
|           |               |   |       kex_gex.pyi
|           |               |   |       kex_group1.pyi
|           |               |   |       kex_group14.pyi
|           |               |   |       kex_group16.pyi
|           |               |   |       kex_gss.pyi
|           |               |   |       message.pyi
|           |               |   |       packet.pyi
|           |               |   |       pipe.pyi
|           |               |   |       pkey.pyi
|           |               |   |       primes.pyi
|           |               |   |       proxy.pyi
|           |               |   |       py3compat.pyi
|           |               |   |       rsakey.pyi
|           |               |   |       server.pyi
|           |               |   |       sftp.pyi
|           |               |   |       sftp_attr.pyi
|           |               |   |       sftp_client.pyi
|           |               |   |       sftp_file.pyi
|           |               |   |       sftp_handle.pyi
|           |               |   |       sftp_server.pyi
|           |               |   |       sftp_si.pyi
|           |               |   |       ssh_exception.pyi
|           |               |   |       ssh_gss.pyi
|           |               |   |       transport.pyi
|           |               |   |       util.pyi
|           |               |   |       win_pageant.pyi
|           |               |   |       _version.pyi
|           |               |   |       _winapi.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---pymysql
|           |               |   |   |   charset.pyi
|           |               |   |   |   connections.pyi
|           |               |   |   |   converters.pyi
|           |               |   |   |   cursors.pyi
|           |               |   |   |   err.pyi
|           |               |   |   |   times.pyi
|           |               |   |   |   util.pyi
|           |               |   |   |   __init__.pyi
|           |               |   |   |   
|           |               |   |   \---constants
|           |               |   |           CLIENT.pyi
|           |               |   |           COMMAND.pyi
|           |               |   |           ER.pyi
|           |               |   |           FIELD_TYPE.pyi
|           |               |   |           FLAG.pyi
|           |               |   |           SERVER_STATUS.pyi
|           |               |   |           __init__.pyi
|           |               |   |           
|           |               |   +---pynamodb
|           |               |   |   |   attributes.pyi
|           |               |   |   |   constants.pyi
|           |               |   |   |   exceptions.pyi
|           |               |   |   |   indexes.pyi
|           |               |   |   |   models.pyi
|           |               |   |   |   settings.pyi
|           |               |   |   |   throttle.pyi
|           |               |   |   |   types.pyi
|           |               |   |   |   __init__.pyi
|           |               |   |   |   
|           |               |   |   \---connection
|           |               |   |           base.pyi
|           |               |   |           table.pyi
|           |               |   |           util.pyi
|           |               |   |           __init__.pyi
|           |               |   |           
|           |               |   +---pytz
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---pyVmomi
|           |               |   |   |   __init__.pyi
|           |               |   |   |   
|           |               |   |   +---vim
|           |               |   |   |       event.pyi
|           |               |   |   |       fault.pyi
|           |               |   |   |       option.pyi
|           |               |   |   |       view.pyi
|           |               |   |   |       __init__.pyi
|           |               |   |   |       
|           |               |   |   \---vmodl
|           |               |   |           fault.pyi
|           |               |   |           query.pyi
|           |               |   |           __init__.pyi
|           |               |   |           
|           |               |   +---redis
|           |               |   |       client.pyi
|           |               |   |       connection.pyi
|           |               |   |       exceptions.pyi
|           |               |   |       utils.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---requests
|           |               |   |   |   adapters.pyi
|           |               |   |   |   api.pyi
|           |               |   |   |   auth.pyi
|           |               |   |   |   compat.pyi
|           |               |   |   |   cookies.pyi
|           |               |   |   |   exceptions.pyi
|           |               |   |   |   hooks.pyi
|           |               |   |   |   models.pyi
|           |               |   |   |   sessions.pyi
|           |               |   |   |   status_codes.pyi
|           |               |   |   |   structures.pyi
|           |               |   |   |   utils.pyi
|           |               |   |   |   __init__.pyi
|           |               |   |   |   
|           |               |   |   \---packages
|           |               |   |       |   __init__.pyi
|           |               |   |       |   
|           |               |   |       \---urllib3
|           |               |   |           |   connection.pyi
|           |               |   |           |   connectionpool.pyi
|           |               |   |           |   exceptions.pyi
|           |               |   |           |   fields.pyi
|           |               |   |           |   filepost.pyi
|           |               |   |           |   poolmanager.pyi
|           |               |   |           |   request.pyi
|           |               |   |           |   response.pyi
|           |               |   |           |   _collections.pyi
|           |               |   |           |   __init__.pyi
|           |               |   |           |   
|           |               |   |           +---contrib
|           |               |   |           |       __init__.pyi
|           |               |   |           |       
|           |               |   |           +---packages
|           |               |   |           |   |   __init__.pyi
|           |               |   |           |   |   
|           |               |   |           |   \---ssl_match_hostname
|           |               |   |           |           _implementation.pyi
|           |               |   |           |           __init__.pyi
|           |               |   |           |           
|           |               |   |           \---util
|           |               |   |                   connection.pyi
|           |               |   |                   request.pyi
|           |               |   |                   response.pyi
|           |               |   |                   retry.pyi
|           |               |   |                   ssl_.pyi
|           |               |   |                   timeout.pyi
|           |               |   |                   url.pyi
|           |               |   |                   __init__.pyi
|           |               |   |                   
|           |               |   +---retry
|           |               |   |       api.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---simplejson
|           |               |   |       decoder.pyi
|           |               |   |       encoder.pyi
|           |               |   |       scanner.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---slugify
|           |               |   |       slugify.pyi
|           |               |   |       special.pyi
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---tzlocal
|           |               |   |       __init__.pyi
|           |               |   |       
|           |               |   +---werkzeug
|           |               |   |   |   datastructures.pyi
|           |               |   |   |   exceptions.pyi
|           |               |   |   |   filesystem.pyi
|           |               |   |   |   formparser.pyi
|           |               |   |   |   http.pyi
|           |               |   |   |   local.pyi
|           |               |   |   |   posixemulation.pyi
|           |               |   |   |   routing.pyi
|           |               |   |   |   script.pyi
|           |               |   |   |   security.pyi
|           |               |   |   |   serving.pyi
|           |               |   |   |   test.pyi
|           |               |   |   |   testapp.pyi
|           |               |   |   |   urls.pyi
|           |               |   |   |   useragents.pyi
|           |               |   |   |   utils.pyi
|           |               |   |   |   wrappers.pyi
|           |               |   |   |   wsgi.pyi
|           |               |   |   |   _compat.pyi
|           |               |   |   |   _internal.pyi
|           |               |   |   |   _reloader.pyi
|           |               |   |   |   __init__.pyi
|           |               |   |   |   
|           |               |   |   +---contrib
|           |               |   |   |       atom.pyi
|           |               |   |   |       cache.pyi
|           |               |   |   |       fixers.pyi
|           |               |   |   |       iterio.pyi
|           |               |   |   |       jsrouting.pyi
|           |               |   |   |       limiter.pyi
|           |               |   |   |       lint.pyi
|           |               |   |   |       profiler.pyi
|           |               |   |   |       securecookie.pyi
|           |               |   |   |       sessions.pyi
|           |               |   |   |       testtools.pyi
|           |               |   |   |       wrappers.pyi
|           |               |   |   |       __init__.pyi
|           |               |   |   |       
|           |               |   |   +---debug
|           |               |   |   |       console.pyi
|           |               |   |   |       repr.pyi
|           |               |   |   |       tbtools.pyi
|           |               |   |   |       __init__.pyi
|           |               |   |   |       
|           |               |   |   \---middleware
|           |               |   |           dispatcher.pyi
|           |               |   |           http_proxy.pyi
|           |               |   |           lint.pyi
|           |               |   |           profiler.pyi
|           |               |   |           proxy_fix.pyi
|           |               |   |           shared_data.pyi
|           |               |   |           __init__.pyi
|           |               |   |           
|           |               |   \---yaml
|           |               |           composer.pyi
|           |               |           constructor.pyi
|           |               |           cyaml.pyi
|           |               |           dumper.pyi
|           |               |           emitter.pyi
|           |               |           error.pyi
|           |               |           events.pyi
|           |               |           loader.pyi
|           |               |           nodes.pyi
|           |               |           parser.pyi
|           |               |           reader.pyi
|           |               |           representer.pyi
|           |               |           resolver.pyi
|           |               |           scanner.pyi
|           |               |           serializer.pyi
|           |               |           tokens.pyi
|           |               |           __init__.pyi
|           |               |           
|           |               \---3
|           |                   |   contextvars.pyi
|           |                   |   dataclasses.pyi
|           |                   |   frozendict.pyi
|           |                   |   orjson.pyi
|           |                   |   
|           |                   +---aiofiles
|           |                   |   |   base.pyi
|           |                   |   |   os.pyi
|           |                   |   |   __init__.pyi
|           |                   |   |   
|           |                   |   \---threadpool
|           |                   |           binary.pyi
|           |                   |           text.pyi
|           |                   |           __init__.pyi
|           |                   |           
|           |                   +---docutils
|           |                   |   |   examples.pyi
|           |                   |   |   nodes.pyi
|           |                   |   |   __init__.pyi
|           |                   |   |   
|           |                   |   \---parsers
|           |                   |       |   __init__.pyi
|           |                   |       |   
|           |                   |       \---rst
|           |                   |               nodes.pyi
|           |                   |               roles.pyi
|           |                   |               states.pyi
|           |                   |               __init__.pyi
|           |                   |               
|           |                   +---filelock
|           |                   |       __init__.pyi
|           |                   |       
|           |                   +---freezegun
|           |                   |       api.pyi
|           |                   |       __init__.pyi
|           |                   |       
|           |                   +---jwt
|           |                   |   |   algorithms.pyi
|           |                   |   |   __init__.pyi
|           |                   |   |   
|           |                   |   \---contrib
|           |                   |       |   __init__.pyi
|           |                   |       |   
|           |                   |       \---algorithms
|           |                   |               pycrypto.pyi
|           |                   |               py_ecdsa.pyi
|           |                   |               __init__.pyi
|           |                   |               
|           |                   +---pkg_resources
|           |                   |       py31compat.pyi
|           |                   |       __init__.pyi
|           |                   |       
|           |                   +---pyrfc3339
|           |                   |       generator.pyi
|           |                   |       parser.pyi
|           |                   |       utils.pyi
|           |                   |       __init__.pyi
|           |                   |       
|           |                   +---six
|           |                   |   |   __init__.pyi
|           |                   |   |   
|           |                   |   \---moves
|           |                   |       |   BaseHTTPServer.pyi
|           |                   |       |   builtins.pyi
|           |                   |       |   CGIHTTPServer.pyi
|           |                   |       |   collections_abc.pyi
|           |                   |       |   configparser.pyi
|           |                   |       |   cPickle.pyi
|           |                   |       |   email_mime_base.pyi
|           |                   |       |   email_mime_multipart.pyi
|           |                   |       |   email_mime_nonmultipart.pyi
|           |                   |       |   email_mime_text.pyi
|           |                   |       |   html_entities.pyi
|           |                   |       |   html_parser.pyi
|           |                   |       |   http_client.pyi
|           |                   |       |   http_cookiejar.pyi
|           |                   |       |   http_cookies.pyi
|           |                   |       |   queue.pyi
|           |                   |       |   reprlib.pyi
|           |                   |       |   SimpleHTTPServer.pyi
|           |                   |       |   socketserver.pyi
|           |                   |       |   tkinter.pyi
|           |                   |       |   tkinter_commondialog.pyi
|           |                   |       |   tkinter_constants.pyi
|           |                   |       |   tkinter_dialog.pyi
|           |                   |       |   tkinter_filedialog.pyi
|           |                   |       |   tkinter_tkfiledialog.pyi
|           |                   |       |   tkinter_ttk.pyi
|           |                   |       |   urllib_error.pyi
|           |                   |       |   urllib_parse.pyi
|           |                   |       |   urllib_request.pyi
|           |                   |       |   urllib_response.pyi
|           |                   |       |   urllib_robotparser.pyi
|           |                   |       |   _dummy_thread.pyi
|           |                   |       |   _thread.pyi
|           |                   |       |   __init__.pyi
|           |                   |       |   
|           |                   |       \---urllib
|           |                   |               error.pyi
|           |                   |               parse.pyi
|           |                   |               request.pyi
|           |                   |               response.pyi
|           |                   |               robotparser.pyi
|           |                   |               __init__.pyi
|           |                   |               
|           |                   +---typed_ast
|           |                   |       ast27.pyi
|           |                   |       ast3.pyi
|           |                   |       conversions.pyi
|           |                   |       __init__.pyi
|           |                   |       
|           |                   \---waitress
|           |                           adjustments.pyi
|           |                           buffers.pyi
|           |                           channel.pyi
|           |                           compat.pyi
|           |                           parser.pyi
|           |                           proxy_headers.pyi
|           |                           receiver.pyi
|           |                           rfc7230.pyi
|           |                           runner.pyi
|           |                           server.pyi
|           |                           task.pyi
|           |                           trigger.pyi
|           |                           utilities.pyi
|           |                           wasyncore.pyi
|           |                           __init__.pyi
|           |                           
|           +---luanny
|           |   |   auth.py
|           |   |   browser.py
|           |   |   cli.py
|           |   |   config.py
|           |   |   evidence_capture.py
|           |   |   exporters.py
|           |   |   log.py
|           |   |   models.py
|           |   |   orchestrator.py
|           |   |   post_extractor.py
|           |   |   profile_discovery.py
|           |   |   selectors.py
|           |   |   __init__.py
|           |   |   __main__.py
|           |   |   
|           |   \---__pycache__
|           |           auth.cpython-310.pyc
|           |           browser.cpython-310.pyc
|           |           cli.cpython-310.pyc
|           |           config.cpython-310.pyc
|           |           evidence_capture.cpython-310.pyc
|           |           exporters.cpython-310.pyc
|           |           log.cpython-310.pyc
|           |           models.cpython-310.pyc
|           |           orchestrator.cpython-310.pyc
|           |           post_extractor.cpython-310.pyc
|           |           profile_discovery.cpython-310.pyc
|           |           selectors.cpython-310.pyc
|           |           __init__.cpython-310.pyc
|           |           __init__.cpython-312.pyc
|           |           __main__.cpython-310.pyc
|           |           
|           +---mypy
|           |   |   errorcodes.cp312-win_amd64.pyd
|           |   |   expandtype.cp312-win_amd64.pyd
|           |   |   nodes.cp312-win_amd64.pyd
|           |   |   options.cp312-win_amd64.pyd
|           |   |   plugin.cp312-win_amd64.pyd
|           |   |   semanal.cp312-win_amd64.pyd
|           |   |   state.cp312-win_amd64.pyd
|           |   |   typeops.cp312-win_amd64.pyd
|           |   |   types.cp312-win_amd64.pyd
|           |   |   typevars.cp312-win_amd64.pyd
|           |   |   type_visitor.cp312-win_amd64.pyd
|           |   |   util.cp312-win_amd64.pyd
|           |   |   __init__.cp312-win_amd64.pyd
|           |   |   
|           |   +---plugins
|           |   |       common.cp312-win_amd64.pyd
|           |   |       dataclasses.cp312-win_amd64.pyd
|           |   |       __init__.cp312-win_amd64.pyd
|           |   |       
|           |   \---server
|           |           trigger.cp312-win_amd64.pyd
|           |           __init__.cp312-win_amd64.pyd
|           |           
|           +---numpy
|           |   +---fft
|           |   |       _pocketfft_umath.cp312-win_amd64.pyd
|           |   |       
|           |   +---linalg
|           |   |       _umath_linalg.cp312-win_amd64.pyd
|           |   |       
|           |   +---random
|           |   |       bit_generator.cp312-win_amd64.pyd
|           |   |       mtrand.cp312-win_amd64.pyd
|           |   |       _bounded_integers.cp312-win_amd64.pyd
|           |   |       _common.cp312-win_amd64.pyd
|           |   |       _generator.cp312-win_amd64.pyd
|           |   |       _mt19937.cp312-win_amd64.pyd
|           |   |       _pcg64.cp312-win_amd64.pyd
|           |   |       _philox.cp312-win_amd64.pyd
|           |   |       _sfc64.cp312-win_amd64.pyd
|           |   |       
|           |   \---_core
|           |           _multiarray_tests.cp312-win_amd64.pyd
|           |           _multiarray_umath.cp312-win_amd64.pyd
|           |           
|           +---numpy-2.3.5.dist-info
|           |       DELVEWHEEL
|           |       entry_points.txt
|           |       INSTALLER
|           |       LICENSE.txt
|           |       METADATA
|           |       RECORD
|           |       WHEEL
|           |       
|           +---numpy.libs
|           |       libscipy_openblas64_-9e3e5a4229c1ca39f10dc82bba9e2b2b.dll
|           |       msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
|           |       
|           +---parso
|           |   |   py.typed
|           |   |   
|           |   \---python
|           |           grammar310.txt
|           |           grammar311.txt
|           |           grammar312.txt
|           |           grammar313.txt
|           |           grammar314.txt
|           |           grammar36.txt
|           |           grammar37.txt
|           |           grammar38.txt
|           |           grammar39.txt
|           |           
|           +---PIL
|           |       _avif.cp312-win_amd64.pyd
|           |       _imaging.cp312-win_amd64.pyd
|           |       _imagingcms.cp312-win_amd64.pyd
|           |       _imagingft.cp312-win_amd64.pyd
|           |       _imagingmath.cp312-win_amd64.pyd
|           |       _imagingtk.cp312-win_amd64.pyd
|           |       _webp.cp312-win_amd64.pyd
|           |       
|           +---playwright
|           |   |   py.typed
|           |   |   
|           |   \---driver
|           |       |   LICENSE
|           |       |   node.exe
|           |       |   README.md
|           |       |   
|           |       \---package
|           |           |   api.json
|           |           |   browsers.json
|           |           |   cli.js
|           |           |   index.d.ts
|           |           |   index.js
|           |           |   index.mjs
|           |           |   LICENSE
|           |           |   NOTICE
|           |           |   package.json
|           |           |   protocol.yml
|           |           |   README.md
|           |           |   ThirdPartyNotices.txt
|           |           |   
|           |           +---bin
|           |           |       install_media_pack.ps1
|           |           |       install_webkit_wsl.ps1
|           |           |       reinstall_chrome_beta_linux.sh
|           |           |       reinstall_chrome_beta_mac.sh
|           |           |       reinstall_chrome_beta_win.ps1
|           |           |       reinstall_chrome_stable_linux.sh
|           |           |       reinstall_chrome_stable_mac.sh
|           |           |       reinstall_chrome_stable_win.ps1
|           |           |       reinstall_msedge_beta_linux.sh
|           |           |       reinstall_msedge_beta_mac.sh
|           |           |       reinstall_msedge_beta_win.ps1
|           |           |       reinstall_msedge_dev_linux.sh
|           |           |       reinstall_msedge_dev_mac.sh
|           |           |       reinstall_msedge_dev_win.ps1
|           |           |       reinstall_msedge_stable_linux.sh
|           |           |       reinstall_msedge_stable_mac.sh
|           |           |       reinstall_msedge_stable_win.ps1
|           |           |       
|           |           +---lib
|           |           |   |   androidServerImpl.js
|           |           |   |   browserServerImpl.js
|           |           |   |   inprocess.js
|           |           |   |   inProcessFactory.js
|           |           |   |   outofprocess.js
|           |           |   |   utils.js
|           |           |   |   utilsBundle.js
|           |           |   |   zipBundle.js
|           |           |   |   zipBundleImpl.js
|           |           |   |   
|           |           |   +---cli
|           |           |   |       driver.js
|           |           |   |       program.js
|           |           |   |       programWithTestStub.js
|           |           |   |       
|           |           |   +---client
|           |           |   |       accessibility.js
|           |           |   |       android.js
|           |           |   |       api.js
|           |           |   |       artifact.js
|           |           |   |       browser.js
|           |           |   |       browserContext.js
|           |           |   |       browserType.js
|           |           |   |       cdpSession.js
|           |           |   |       channelOwner.js
|           |           |   |       clientHelper.js
|           |           |   |       clientInstrumentation.js
|           |           |   |       clientStackTrace.js
|           |           |   |       clock.js
|           |           |   |       connection.js
|           |           |   |       consoleMessage.js
|           |           |   |       coverage.js
|           |           |   |       dialog.js
|           |           |   |       download.js
|           |           |   |       electron.js
|           |           |   |       elementHandle.js
|           |           |   |       errors.js
|           |           |   |       eventEmitter.js
|           |           |   |       events.js
|           |           |   |       fetch.js
|           |           |   |       fileChooser.js
|           |           |   |       fileUtils.js
|           |           |   |       frame.js
|           |           |   |       harRouter.js
|           |           |   |       input.js
|           |           |   |       jsHandle.js
|           |           |   |       jsonPipe.js
|           |           |   |       localUtils.js
|           |           |   |       locator.js
|           |           |   |       network.js
|           |           |   |       page.js
|           |           |   |       platform.js
|           |           |   |       playwright.js
|           |           |   |       selectors.js
|           |           |   |       stream.js
|           |           |   |       timeoutSettings.js
|           |           |   |       tracing.js
|           |           |   |       types.js
|           |           |   |       video.js
|           |           |   |       waiter.js
|           |           |   |       webError.js
|           |           |   |       webSocket.js
|           |           |   |       worker.js
|           |           |   |       writableStream.js
|           |           |   |       
|           |           |   +---generated
|           |           |   |       bindingsControllerSource.js
|           |           |   |       clockSource.js
|           |           |   |       injectedScriptSource.js
|           |           |   |       pollingRecorderSource.js
|           |           |   |       storageScriptSource.js
|           |           |   |       utilityScriptSource.js
|           |           |   |       webSocketMockSource.js
|           |           |   |       
|           |           |   +---protocol
|           |           |   |       serializers.js
|           |           |   |       validator.js
|           |           |   |       validatorPrimitives.js
|           |           |   |       
|           |           |   +---remote
|           |           |   |       playwrightConnection.js
|           |           |   |       playwrightServer.js
|           |           |   |       
|           |           |   +---server
|           |           |   |   |   accessibility.js
|           |           |   |   |   artifact.js
|           |           |   |   |   browser.js
|           |           |   |   |   browserContext.js
|           |           |   |   |   browserType.js
|           |           |   |   |   callLog.js
|           |           |   |   |   clock.js
|           |           |   |   |   console.js
|           |           |   |   |   cookieStore.js
|           |           |   |   |   debugController.js
|           |           |   |   |   debugger.js
|           |           |   |   |   deviceDescriptors.js
|           |           |   |   |   deviceDescriptorsSource.json
|           |           |   |   |   dialog.js
|           |           |   |   |   dom.js
|           |           |   |   |   download.js
|           |           |   |   |   errors.js
|           |           |   |   |   fetch.js
|           |           |   |   |   fileChooser.js
|           |           |   |   |   fileUploadUtils.js
|           |           |   |   |   formData.js
|           |           |   |   |   frames.js
|           |           |   |   |   frameSelectors.js
|           |           |   |   |   harBackend.js
|           |           |   |   |   helper.js
|           |           |   |   |   index.js
|           |           |   |   |   input.js
|           |           |   |   |   instrumentation.js
|           |           |   |   |   javascript.js
|           |           |   |   |   launchApp.js
|           |           |   |   |   localUtils.js
|           |           |   |   |   macEditingCommands.js
|           |           |   |   |   network.js
|           |           |   |   |   page.js
|           |           |   |   |   pipeTransport.js
|           |           |   |   |   playwright.js
|           |           |   |   |   progress.js
|           |           |   |   |   protocolError.js
|           |           |   |   |   recorder.js
|           |           |   |   |   screenshotter.js
|           |           |   |   |   selectors.js
|           |           |   |   |   socksClientCertificatesInterceptor.js
|           |           |   |   |   socksInterceptor.js
|           |           |   |   |   transport.js
|           |           |   |   |   types.js
|           |           |   |   |   usKeyboardLayout.js
|           |           |   |   |   
|           |           |   |   +---android
|           |           |   |   |       android.js
|           |           |   |   |       backendAdb.js
|           |           |   |   |       
|           |           |   |   +---bidi
|           |           |   |   |   |   bidiBrowser.js
|           |           |   |   |   |   bidiChromium.js
|           |           |   |   |   |   bidiConnection.js
|           |           |   |   |   |   bidiExecutionContext.js
|           |           |   |   |   |   bidiFirefox.js
|           |           |   |   |   |   bidiInput.js
|           |           |   |   |   |   bidiNetworkManager.js
|           |           |   |   |   |   bidiOverCdp.js
|           |           |   |   |   |   bidiPage.js
|           |           |   |   |   |   bidiPdf.js
|           |           |   |   |   |   
|           |           |   |   |   \---third_party
|           |           |   |   |           bidiCommands.d.js
|           |           |   |   |           bidiDeserializer.js
|           |           |   |   |           bidiKeyboard.js
|           |           |   |   |           bidiProtocol.js
|           |           |   |   |           bidiProtocolCore.js
|           |           |   |   |           bidiProtocolPermissions.js
|           |           |   |   |           bidiSerializer.js
|           |           |   |   |           firefoxPrefs.js
|           |           |   |   |           
|           |           |   |   +---chromium
|           |           |   |   |       appIcon.png
|           |           |   |   |       chromium.js
|           |           |   |   |       chromiumSwitches.js
|           |           |   |   |       crAccessibility.js
|           |           |   |   |       crBrowser.js
|           |           |   |   |       crConnection.js
|           |           |   |   |       crCoverage.js
|           |           |   |   |       crDevTools.js
|           |           |   |   |       crDragDrop.js
|           |           |   |   |       crExecutionContext.js
|           |           |   |   |       crInput.js
|           |           |   |   |       crNetworkManager.js
|           |           |   |   |       crPage.js
|           |           |   |   |       crPdf.js
|           |           |   |   |       crProtocolHelper.js
|           |           |   |   |       crServiceWorker.js
|           |           |   |   |       defaultFontFamilies.js
|           |           |   |   |       protocol.d.js
|           |           |   |   |       videoRecorder.js
|           |           |   |   |       
|           |           |   |   +---codegen
|           |           |   |   |       csharp.js
|           |           |   |   |       java.js
|           |           |   |   |       javascript.js
|           |           |   |   |       jsonl.js
|           |           |   |   |       language.js
|           |           |   |   |       languages.js
|           |           |   |   |       python.js
|           |           |   |   |       types.js
|           |           |   |   |       
|           |           |   |   +---dispatchers
|           |           |   |   |       androidDispatcher.js
|           |           |   |   |       artifactDispatcher.js
|           |           |   |   |       browserContextDispatcher.js
|           |           |   |   |       browserDispatcher.js
|           |           |   |   |       browserTypeDispatcher.js
|           |           |   |   |       cdpSessionDispatcher.js
|           |           |   |   |       debugControllerDispatcher.js
|           |           |   |   |       dialogDispatcher.js
|           |           |   |   |       dispatcher.js
|           |           |   |   |       electronDispatcher.js
|           |           |   |   |       elementHandlerDispatcher.js
|           |           |   |   |       frameDispatcher.js
|           |           |   |   |       jsHandleDispatcher.js
|           |           |   |   |       jsonPipeDispatcher.js
|           |           |   |   |       localUtilsDispatcher.js
|           |           |   |   |       networkDispatchers.js
|           |           |   |   |       pageDispatcher.js
|           |           |   |   |       playwrightDispatcher.js
|           |           |   |   |       streamDispatcher.js
|           |           |   |   |       tracingDispatcher.js
|           |           |   |   |       webSocketRouteDispatcher.js
|           |           |   |   |       writableStreamDispatcher.js
|           |           |   |   |       
|           |           |   |   +---electron
|           |           |   |   |       electron.js
|           |           |   |   |       loader.js
|           |           |   |   |       
|           |           |   |   +---firefox
|           |           |   |   |       ffAccessibility.js
|           |           |   |   |       ffBrowser.js
|           |           |   |   |       ffConnection.js
|           |           |   |   |       ffExecutionContext.js
|           |           |   |   |       ffInput.js
|           |           |   |   |       ffNetworkManager.js
|           |           |   |   |       ffPage.js
|           |           |   |   |       firefox.js
|           |           |   |   |       protocol.d.js
|           |           |   |   |       
|           |           |   |   +---har
|           |           |   |   |       harRecorder.js
|           |           |   |   |       harTracer.js
|           |           |   |   |       
|           |           |   |   +---recorder
|           |           |   |   |       chat.js
|           |           |   |   |       recorderApp.js
|           |           |   |   |       recorderRunner.js
|           |           |   |   |       recorderSignalProcessor.js
|           |           |   |   |       recorderUtils.js
|           |           |   |   |       throttledFile.js
|           |           |   |   |       
|           |           |   |   +---registry
|           |           |   |   |       browserFetcher.js
|           |           |   |   |       dependencies.js
|           |           |   |   |       index.js
|           |           |   |   |       nativeDeps.js
|           |           |   |   |       oopDownloadBrowserMain.js
|           |           |   |   |       
|           |           |   |   +---trace
|           |           |   |   |   +---recorder
|           |           |   |   |   |       snapshotter.js
|           |           |   |   |   |       snapshotterInjected.js
|           |           |   |   |   |       tracing.js
|           |           |   |   |   |       
|           |           |   |   |   +---test
|           |           |   |   |   |       inMemorySnapshotter.js
|           |           |   |   |   |       
|           |           |   |   |   \---viewer
|           |           |   |   |           traceViewer.js
|           |           |   |   |           
|           |           |   |   +---utils
|           |           |   |   |   |   ascii.js
|           |           |   |   |   |   comparators.js
|           |           |   |   |   |   crypto.js
|           |           |   |   |   |   debug.js
|           |           |   |   |   |   debugLogger.js
|           |           |   |   |   |   env.js
|           |           |   |   |   |   eventsHelper.js
|           |           |   |   |   |   expectUtils.js
|           |           |   |   |   |   fileUtils.js
|           |           |   |   |   |   happyEyeballs.js
|           |           |   |   |   |   hostPlatform.js
|           |           |   |   |   |   httpServer.js
|           |           |   |   |   |   linuxUtils.js
|           |           |   |   |   |   network.js
|           |           |   |   |   |   nodePlatform.js
|           |           |   |   |   |   pipeTransport.js
|           |           |   |   |   |   processLauncher.js
|           |           |   |   |   |   profiler.js
|           |           |   |   |   |   socksProxy.js
|           |           |   |   |   |   spawnAsync.js
|           |           |   |   |   |   task.js
|           |           |   |   |   |   userAgent.js
|           |           |   |   |   |   wsServer.js
|           |           |   |   |   |   zipFile.js
|           |           |   |   |   |   zones.js
|           |           |   |   |   |   
|           |           |   |   |   \---image_tools
|           |           |   |   |           colorUtils.js
|           |           |   |   |           compare.js
|           |           |   |   |           imageChannel.js
|           |           |   |   |           stats.js
|           |           |   |   |           
|           |           |   |   \---webkit
|           |           |   |       |   protocol.d.js
|           |           |   |       |   webkit.js
|           |           |   |       |   wkAccessibility.js
|           |           |   |       |   wkBrowser.js
|           |           |   |       |   wkConnection.js
|           |           |   |       |   wkExecutionContext.js
|           |           |   |       |   wkInput.js
|           |           |   |       |   wkInterceptableRequest.js
|           |           |   |       |   wkPage.js
|           |           |   |       |   wkProvisionalPage.js
|           |           |   |       |   wkWorkers.js
|           |           |   |       |   
|           |           |   |       \---wsl
|           |           |   |               webkit-wsl-transport-client.js
|           |           |   |               webkit-wsl-transport-server.js
|           |           |   |               
|           |           |   +---third_party
|           |           |   |       pixelmatch.js
|           |           |   |       
|           |           |   +---utils
|           |           |   |   \---isomorphic
|           |           |   |           ariaSnapshot.js
|           |           |   |           assert.js
|           |           |   |           colors.js
|           |           |   |           cssParser.js
|           |           |   |           cssTokenizer.js
|           |           |   |           headers.js
|           |           |   |           locatorGenerators.js
|           |           |   |           locatorParser.js
|           |           |   |           locatorUtils.js
|           |           |   |           manualPromise.js
|           |           |   |           mimeType.js
|           |           |   |           multimap.js
|           |           |   |           protocolFormatter.js
|           |           |   |           protocolMetainfo.js
|           |           |   |           rtti.js
|           |           |   |           selectorParser.js
|           |           |   |           semaphore.js
|           |           |   |           stackTrace.js
|           |           |   |           stringUtils.js
|           |           |   |           time.js
|           |           |   |           timeoutRunner.js
|           |           |   |           traceUtils.js
|           |           |   |           types.js
|           |           |   |           urlMatch.js
|           |           |   |           utilityScriptSerializers.js
|           |           |   |           
|           |           |   +---utilsBundleImpl
|           |           |   |       index.js
|           |           |   |       xdg-open
|           |           |   |       
|           |           |   \---vite
|           |           |       +---htmlReport
|           |           |       |       index.html
|           |           |       |       
|           |           |       +---recorder
|           |           |       |   |   index.html
|           |           |       |   |   playwright-logo.svg
|           |           |       |   |   
|           |           |       |   \---assets
|           |           |       |           codeMirrorModule-C3UTv-Ge.css
|           |           |       |           codeMirrorModule-RJCXzfmE.js
|           |           |       |           codicon-DCmgc-ay.ttf
|           |           |       |           index-Ri0uHF7I.css
|           |           |       |           index-Y-X2TGJv.js
|           |           |       |           
|           |           |       \---traceViewer
|           |           |           |   codeMirrorModule.C3UTv-Ge.css
|           |           |           |   codicon.DCmgc-ay.ttf
|           |           |           |   defaultSettingsView.TQ8_7ybu.css
|           |           |           |   index.Bx16ehp1.js
|           |           |           |   index.html
|           |           |           |   index.I8N9v4jT.css
|           |           |           |   playwright-logo.svg
|           |           |           |   snapshot.html
|           |           |           |   sw.bundle.js
|           |           |           |   uiMode.Btcz36p_.css
|           |           |           |   uiMode.DRQ310U5.js
|           |           |           |   uiMode.html
|           |           |           |   xtermModule.DYP7pi_n.css
|           |           |           |   
|           |           |           \---assets
|           |           |                   codeMirrorModule-eyVcHN77.js
|           |           |                   defaultSettingsView-w0zYjHsW.js
|           |           |                   xtermModule-CsJ4vdCR.js
|           |           |                   
|           |           \---types
|           |                   protocol.d.ts
|           |                   structs.d.ts
|           |                   types.d.ts
|           |                   
|           +---prompt_toolkit-3.0.52.dist-info
|           |   |   INSTALLER
|           |   |   METADATA
|           |   |   RECORD
|           |   |   top_level.txt
|           |   |   WHEEL
|           |   |   
|           |   \---licenses
|           |           AUTHORS.rst
|           |           LICENSE
|           |           
|           +---psutil
|           |       _psutil_windows.pyd
|           |       
|           +---pydantic_core
|           |       _pydantic_core.cp312-win_amd64.pyd
|           |       
|           +---setuptools
|           |   \---_vendor
|           |       +---importlib_metadata-8.0.0.dist-info
|           |       |       INSTALLER
|           |       |       LICENSE
|           |       |       METADATA
|           |       |       RECORD
|           |       |       REQUESTED
|           |       |       top_level.txt
|           |       |       WHEEL
|           |       |       
|           |       \---jaraco
|           |           \---text
|           |                   Lorem ipsum.txt
|           |                   
|           +---structlog-25.4.0.dist-info
|           |   |   INSTALLER
|           |   |   METADATA
|           |   |   RECORD
|           |   |   REQUESTED
|           |   |   WHEEL
|           |   |   
|           |   \---licenses
|           |           LICENSE-APACHE
|           |           LICENSE-MIT
|           |           NOTICE
|           |           
|           +---tzdata
|           |   |   zones
|           |   |   
|           |   \---zoneinfo
|           |       |   CET
|           |       |   CST6CDT
|           |       |   Cuba
|           |       |   EET
|           |       |   Egypt
|           |       |   Eire
|           |       |   EST
|           |       |   EST5EDT
|           |       |   Factory
|           |       |   GB
|           |       |   GB-Eire
|           |       |   GMT
|           |       |   GMT+0
|           |       |   GMT-0
|           |       |   GMT0
|           |       |   Greenwich
|           |       |   Hongkong
|           |       |   HST
|           |       |   Iceland
|           |       |   Iran
|           |       |   iso3166.tab
|           |       |   Israel
|           |       |   Jamaica
|           |       |   Japan
|           |       |   Kwajalein
|           |       |   leapseconds
|           |       |   Libya
|           |       |   MET
|           |       |   MST
|           |       |   MST7MDT
|           |       |   Navajo
|           |       |   NZ
|           |       |   NZ-CHAT
|           |       |   Poland
|           |       |   Portugal
|           |       |   PRC
|           |       |   PST8PDT
|           |       |   ROC
|           |       |   ROK
|           |       |   Singapore
|           |       |   Turkey
|           |       |   tzdata.zi
|           |       |   UCT
|           |       |   Universal
|           |       |   UTC
|           |       |   W-SU
|           |       |   WET
|           |       |   zone.tab
|           |       |   zone1970.tab
|           |       |   zonenow.tab
|           |       |   Zulu
|           |       |   
|           |       +---Africa
|           |       |       Abidjan
|           |       |       Accra
|           |       |       Addis_Ababa
|           |       |       Algiers
|           |       |       Asmara
|           |       |       Asmera
|           |       |       Bamako
|           |       |       Bangui
|           |       |       Banjul
|           |       |       Bissau
|           |       |       Blantyre
|           |       |       Brazzaville
|           |       |       Bujumbura
|           |       |       Cairo
|           |       |       Casablanca
|           |       |       Ceuta
|           |       |       Conakry
|           |       |       Dakar
|           |       |       Dar_es_Salaam
|           |       |       Djibouti
|           |       |       Douala
|           |       |       El_Aaiun
|           |       |       Freetown
|           |       |       Gaborone
|           |       |       Harare
|           |       |       Johannesburg
|           |       |       Juba
|           |       |       Kampala
|           |       |       Khartoum
|           |       |       Kigali
|           |       |       Kinshasa
|           |       |       Lagos
|           |       |       Libreville
|           |       |       Lome
|           |       |       Luanda
|           |       |       Lubumbashi
|           |       |       Lusaka
|           |       |       Malabo
|           |       |       Maputo
|           |       |       Maseru
|           |       |       Mbabane
|           |       |       Mogadishu
|           |       |       Monrovia
|           |       |       Nairobi
|           |       |       Ndjamena
|           |       |       Niamey
|           |       |       Nouakchott
|           |       |       Ouagadougou
|           |       |       Porto-Novo
|           |       |       Sao_Tome
|           |       |       Timbuktu
|           |       |       Tripoli
|           |       |       Tunis
|           |       |       Windhoek
|           |       |       
|           |       +---America
|           |       |   |   Adak
|           |       |   |   Anchorage
|           |       |   |   Anguilla
|           |       |   |   Antigua
|           |       |   |   Araguaina
|           |       |   |   Aruba
|           |       |   |   Asuncion
|           |       |   |   Atikokan
|           |       |   |   Atka
|           |       |   |   Bahia
|           |       |   |   Bahia_Banderas
|           |       |   |   Barbados
|           |       |   |   Belem
|           |       |   |   Belize
|           |       |   |   Blanc-Sablon
|           |       |   |   Boa_Vista
|           |       |   |   Bogota
|           |       |   |   Boise
|           |       |   |   Buenos_Aires
|           |       |   |   Cambridge_Bay
|           |       |   |   Campo_Grande
|           |       |   |   Cancun
|           |       |   |   Caracas
|           |       |   |   Catamarca
|           |       |   |   Cayenne
|           |       |   |   Cayman
|           |       |   |   Chicago
|           |       |   |   Chihuahua
|           |       |   |   Ciudad_Juarez
|           |       |   |   Coral_Harbour
|           |       |   |   Cordoba
|           |       |   |   Costa_Rica
|           |       |   |   Coyhaique
|           |       |   |   Creston
|           |       |   |   Cuiaba
|           |       |   |   Curacao
|           |       |   |   Danmarkshavn
|           |       |   |   Dawson
|           |       |   |   Dawson_Creek
|           |       |   |   Denver
|           |       |   |   Detroit
|           |       |   |   Dominica
|           |       |   |   Edmonton
|           |       |   |   Eirunepe
|           |       |   |   El_Salvador
|           |       |   |   Ensenada
|           |       |   |   Fortaleza
|           |       |   |   Fort_Nelson
|           |       |   |   Fort_Wayne
|           |       |   |   Glace_Bay
|           |       |   |   Godthab
|           |       |   |   Goose_Bay
|           |       |   |   Grand_Turk
|           |       |   |   Grenada
|           |       |   |   Guadeloupe
|           |       |   |   Guatemala
|           |       |   |   Guayaquil
|           |       |   |   Guyana
|           |       |   |   Halifax
|           |       |   |   Havana
|           |       |   |   Hermosillo
|           |       |   |   Indianapolis
|           |       |   |   Inuvik
|           |       |   |   Iqaluit
|           |       |   |   Jamaica
|           |       |   |   Jujuy
|           |       |   |   Juneau
|           |       |   |   Knox_IN
|           |       |   |   Kralendijk
|           |       |   |   La_Paz
|           |       |   |   Lima
|           |       |   |   Los_Angeles
|           |       |   |   Louisville
|           |       |   |   Lower_Princes
|           |       |   |   Maceio
|           |       |   |   Managua
|           |       |   |   Manaus
|           |       |   |   Marigot
|           |       |   |   Martinique
|           |       |   |   Matamoros
|           |       |   |   Mazatlan
|           |       |   |   Mendoza
|           |       |   |   Menominee
|           |       |   |   Merida
|           |       |   |   Metlakatla
|           |       |   |   Mexico_City
|           |       |   |   Miquelon
|           |       |   |   Moncton
|           |       |   |   Monterrey
|           |       |   |   Montevideo
|           |       |   |   Montreal
|           |       |   |   Montserrat
|           |       |   |   Nassau
|           |       |   |   New_York
|           |       |   |   Nipigon
|           |       |   |   Nome
|           |       |   |   Noronha
|           |       |   |   Nuuk
|           |       |   |   Ojinaga
|           |       |   |   Panama
|           |       |   |   Pangnirtung
|           |       |   |   Paramaribo
|           |       |   |   Phoenix
|           |       |   |   Port-au-Prince
|           |       |   |   Porto_Acre
|           |       |   |   Porto_Velho
|           |       |   |   Port_of_Spain
|           |       |   |   Puerto_Rico
|           |       |   |   Punta_Arenas
|           |       |   |   Rainy_River
|           |       |   |   Rankin_Inlet
|           |       |   |   Recife
|           |       |   |   Regina
|           |       |   |   Resolute
|           |       |   |   Rio_Branco
|           |       |   |   Rosario
|           |       |   |   Santarem
|           |       |   |   Santa_Isabel
|           |       |   |   Santiago
|           |       |   |   Santo_Domingo
|           |       |   |   Sao_Paulo
|           |       |   |   Scoresbysund
|           |       |   |   Shiprock
|           |       |   |   Sitka
|           |       |   |   St_Barthelemy
|           |       |   |   St_Johns
|           |       |   |   St_Kitts
|           |       |   |   St_Lucia
|           |       |   |   St_Thomas
|           |       |   |   St_Vincent
|           |       |   |   Swift_Current
|           |       |   |   Tegucigalpa
|           |       |   |   Thule
|           |       |   |   Thunder_Bay
|           |       |   |   Tijuana
|           |       |   |   Toronto
|           |       |   |   Tortola
|           |       |   |   Vancouver
|           |       |   |   Virgin
|           |       |   |   Whitehorse
|           |       |   |   Winnipeg
|           |       |   |   Yakutat
|           |       |   |   Yellowknife
|           |       |   |   
|           |       |   +---Argentina
|           |       |   |       Buenos_Aires
|           |       |   |       Catamarca
|           |       |   |       ComodRivadavia
|           |       |   |       Cordoba
|           |       |   |       Jujuy
|           |       |   |       La_Rioja
|           |       |   |       Mendoza
|           |       |   |       Rio_Gallegos
|           |       |   |       Salta
|           |       |   |       San_Juan
|           |       |   |       San_Luis
|           |       |   |       Tucuman
|           |       |   |       Ushuaia
|           |       |   |       
|           |       |   +---Indiana
|           |       |   |       Indianapolis
|           |       |   |       Knox
|           |       |   |       Marengo
|           |       |   |       Petersburg
|           |       |   |       Tell_City
|           |       |   |       Vevay
|           |       |   |       Vincennes
|           |       |   |       Winamac
|           |       |   |       
|           |       |   +---Kentucky
|           |       |   |       Louisville
|           |       |   |       Monticello
|           |       |   |       
|           |       |   \---North_Dakota
|           |       |           Beulah
|           |       |           Center
|           |       |           New_Salem
|           |       |           
|           |       +---Antarctica
|           |       |       Casey
|           |       |       Davis
|           |       |       DumontDUrville
|           |       |       Macquarie
|           |       |       Mawson
|           |       |       McMurdo
|           |       |       Palmer
|           |       |       Rothera
|           |       |       South_Pole
|           |       |       Syowa
|           |       |       Troll
|           |       |       Vostok
|           |       |       
|           |       +---Arctic
|           |       |       Longyearbyen
|           |       |       
|           |       +---Asia
|           |       |       Aden
|           |       |       Almaty
|           |       |       Amman
|           |       |       Anadyr
|           |       |       Aqtau
|           |       |       Aqtobe
|           |       |       Ashgabat
|           |       |       Ashkhabad
|           |       |       Atyrau
|           |       |       Baghdad
|           |       |       Bahrain
|           |       |       Baku
|           |       |       Bangkok
|           |       |       Barnaul
|           |       |       Beirut
|           |       |       Bishkek
|           |       |       Brunei
|           |       |       Calcutta
|           |       |       Chita
|           |       |       Choibalsan
|           |       |       Chongqing
|           |       |       Chungking
|           |       |       Colombo
|           |       |       Dacca
|           |       |       Damascus
|           |       |       Dhaka
|           |       |       Dili
|           |       |       Dubai
|           |       |       Dushanbe
|           |       |       Famagusta
|           |       |       Gaza
|           |       |       Harbin
|           |       |       Hebron
|           |       |       Hong_Kong
|           |       |       Hovd
|           |       |       Ho_Chi_Minh
|           |       |       Irkutsk
|           |       |       Istanbul
|           |       |       Jakarta
|           |       |       Jayapura
|           |       |       Jerusalem
|           |       |       Kabul
|           |       |       Kamchatka
|           |       |       Karachi
|           |       |       Kashgar
|           |       |       Kathmandu
|           |       |       Katmandu
|           |       |       Khandyga
|           |       |       Kolkata
|           |       |       Krasnoyarsk
|           |       |       Kuala_Lumpur
|           |       |       Kuching
|           |       |       Kuwait
|           |       |       Macao
|           |       |       Macau
|           |       |       Magadan
|           |       |       Makassar
|           |       |       Manila
|           |       |       Muscat
|           |       |       Nicosia
|           |       |       Novokuznetsk
|           |       |       Novosibirsk
|           |       |       Omsk
|           |       |       Oral
|           |       |       Phnom_Penh
|           |       |       Pontianak
|           |       |       Pyongyang
|           |       |       Qatar
|           |       |       Qostanay
|           |       |       Qyzylorda
|           |       |       Rangoon
|           |       |       Riyadh
|           |       |       Saigon
|           |       |       Sakhalin
|           |       |       Samarkand
|           |       |       Seoul
|           |       |       Shanghai
|           |       |       Singapore
|           |       |       Srednekolymsk
|           |       |       Taipei
|           |       |       Tashkent
|           |       |       Tbilisi
|           |       |       Tehran
|           |       |       Tel_Aviv
|           |       |       Thimbu
|           |       |       Thimphu
|           |       |       Tokyo
|           |       |       Tomsk
|           |       |       Ujung_Pandang
|           |       |       Ulaanbaatar
|           |       |       Ulan_Bator
|           |       |       Urumqi
|           |       |       Ust-Nera
|           |       |       Vientiane
|           |       |       Vladivostok
|           |       |       Yakutsk
|           |       |       Yangon
|           |       |       Yekaterinburg
|           |       |       Yerevan
|           |       |       
|           |       +---Atlantic
|           |       |       Azores
|           |       |       Bermuda
|           |       |       Canary
|           |       |       Cape_Verde
|           |       |       Faeroe
|           |       |       Faroe
|           |       |       Jan_Mayen
|           |       |       Madeira
|           |       |       Reykjavik
|           |       |       South_Georgia
|           |       |       Stanley
|           |       |       St_Helena
|           |       |       
|           |       +---Australia
|           |       |       ACT
|           |       |       Adelaide
|           |       |       Brisbane
|           |       |       Broken_Hill
|           |       |       Canberra
|           |       |       Currie
|           |       |       Darwin
|           |       |       Eucla
|           |       |       Hobart
|           |       |       LHI
|           |       |       Lindeman
|           |       |       Lord_Howe
|           |       |       Melbourne
|           |       |       North
|           |       |       NSW
|           |       |       Perth
|           |       |       Queensland
|           |       |       South
|           |       |       Sydney
|           |       |       Tasmania
|           |       |       Victoria
|           |       |       West
|           |       |       Yancowinna
|           |       |       
|           |       +---Brazil
|           |       |       Acre
|           |       |       DeNoronha
|           |       |       East
|           |       |       West
|           |       |       
|           |       +---Canada
|           |       |       Atlantic
|           |       |       Central
|           |       |       Eastern
|           |       |       Mountain
|           |       |       Newfoundland
|           |       |       Pacific
|           |       |       Saskatchewan
|           |       |       Yukon
|           |       |       
|           |       +---Chile
|           |       |       Continental
|           |       |       EasterIsland
|           |       |       
|           |       +---Etc
|           |       |       GMT
|           |       |       GMT+0
|           |       |       GMT+1
|           |       |       GMT+10
|           |       |       GMT+11
|           |       |       GMT+12
|           |       |       GMT+2
|           |       |       GMT+3
|           |       |       GMT+4
|           |       |       GMT+5
|           |       |       GMT+6
|           |       |       GMT+7
|           |       |       GMT+8
|           |       |       GMT+9
|           |       |       GMT-0
|           |       |       GMT-1
|           |       |       GMT-10
|           |       |       GMT-11
|           |       |       GMT-12
|           |       |       GMT-13
|           |       |       GMT-14
|           |       |       GMT-2
|           |       |       GMT-3
|           |       |       GMT-4
|           |       |       GMT-5
|           |       |       GMT-6
|           |       |       GMT-7
|           |       |       GMT-8
|           |       |       GMT-9
|           |       |       GMT0
|           |       |       Greenwich
|           |       |       UCT
|           |       |       Universal
|           |       |       UTC
|           |       |       Zulu
|           |       |       
|           |       +---Europe
|           |       |       Amsterdam
|           |       |       Andorra
|           |       |       Astrakhan
|           |       |       Athens
|           |       |       Belfast
|           |       |       Belgrade
|           |       |       Berlin
|           |       |       Bratislava
|           |       |       Brussels
|           |       |       Bucharest
|           |       |       Budapest
|           |       |       Busingen
|           |       |       Chisinau
|           |       |       Copenhagen
|           |       |       Dublin
|           |       |       Gibraltar
|           |       |       Guernsey
|           |       |       Helsinki
|           |       |       Isle_of_Man
|           |       |       Istanbul
|           |       |       Jersey
|           |       |       Kaliningrad
|           |       |       Kiev
|           |       |       Kirov
|           |       |       Kyiv
|           |       |       Lisbon
|           |       |       Ljubljana
|           |       |       London
|           |       |       Luxembourg
|           |       |       Madrid
|           |       |       Malta
|           |       |       Mariehamn
|           |       |       Minsk
|           |       |       Monaco
|           |       |       Moscow
|           |       |       Nicosia
|           |       |       Oslo
|           |       |       Paris
|           |       |       Podgorica
|           |       |       Prague
|           |       |       Riga
|           |       |       Rome
|           |       |       Samara
|           |       |       San_Marino
|           |       |       Sarajevo
|           |       |       Saratov
|           |       |       Simferopol
|           |       |       Skopje
|           |       |       Sofia
|           |       |       Stockholm
|           |       |       Tallinn
|           |       |       Tirane
|           |       |       Tiraspol
|           |       |       Ulyanovsk
|           |       |       Uzhgorod
|           |       |       Vaduz
|           |       |       Vatican
|           |       |       Vienna
|           |       |       Vilnius
|           |       |       Volgograd
|           |       |       Warsaw
|           |       |       Zagreb
|           |       |       Zaporozhye
|           |       |       Zurich
|           |       |       
|           |       +---Indian
|           |       |       Antananarivo
|           |       |       Chagos
|           |       |       Christmas
|           |       |       Cocos
|           |       |       Comoro
|           |       |       Kerguelen
|           |       |       Mahe
|           |       |       Maldives
|           |       |       Mauritius
|           |       |       Mayotte
|           |       |       Reunion
|           |       |       
|           |       +---Mexico
|           |       |       BajaNorte
|           |       |       BajaSur
|           |       |       General
|           |       |       
|           |       +---Pacific
|           |       |       Apia
|           |       |       Auckland
|           |       |       Bougainville
|           |       |       Chatham
|           |       |       Chuuk
|           |       |       Easter
|           |       |       Efate
|           |       |       Enderbury
|           |       |       Fakaofo
|           |       |       Fiji
|           |       |       Funafuti
|           |       |       Galapagos
|           |       |       Gambier
|           |       |       Guadalcanal
|           |       |       Guam
|           |       |       Honolulu
|           |       |       Johnston
|           |       |       Kanton
|           |       |       Kiritimati
|           |       |       Kosrae
|           |       |       Kwajalein
|           |       |       Majuro
|           |       |       Marquesas
|           |       |       Midway
|           |       |       Nauru
|           |       |       Niue
|           |       |       Norfolk
|           |       |       Noumea
|           |       |       Pago_Pago
|           |       |       Palau
|           |       |       Pitcairn
|           |       |       Pohnpei
|           |       |       Ponape
|           |       |       Port_Moresby
|           |       |       Rarotonga
|           |       |       Saipan
|           |       |       Samoa
|           |       |       Tahiti
|           |       |       Tarawa
|           |       |       Tongatapu
|           |       |       Truk
|           |       |       Wake
|           |       |       Wallis
|           |       |       Yap
|           |       |       
|           |       \---US
|           |               Alaska
|           |               Aleutian
|           |               Arizona
|           |               Central
|           |               East-Indiana
|           |               Eastern
|           |               Hawaii
|           |               Indiana-Starke
|           |               Michigan
|           |               Mountain
|           |               Pacific
|           |               Samoa
|           |               
|           \---yaml
|                   _yaml.cp312-win_amd64.pyd
|                   
+---docs
|       sobre_dados_coletados_idioma.md
|       sobre_dados_coletados_idioma.pdf
|       
+---implementation_logs
|       implementation_plan.md
|       implementation_plan.md.metadata.json
|       implementation_plan.md.resolved
|       implementation_plan.md.resolved.0
|       implementation_plan.md.resolved.1
|       implementation_plan.md.resolved.10
|       implementation_plan.md.resolved.11
|       implementation_plan.md.resolved.12
|       implementation_plan.md.resolved.2
|       implementation_plan.md.resolved.3
|       implementation_plan.md.resolved.4
|       implementation_plan.md.resolved.5
|       implementation_plan.md.resolved.6
|       implementation_plan.md.resolved.7
|       implementation_plan.md.resolved.8
|       implementation_plan.md.resolved.9
|       instagram_grid_investigation_1776445880514.webp
|       instagram_login_investigation_1776426098106.webp
|       task.md
|       task.md.metadata.json
|       task.md.resolved
|       task.md.resolved.0
|       task.md.resolved.1
|       task.md.resolved.2
|       task.md.resolved.3
|       task.md.resolved.4
|       task.md.resolved.5
|       task.md.resolved.6
|       task.md.resolved.7
|       task.md.resolved.8
|       task.md.resolved.9
|       walkthrough.md
|       walkthrough.md.metadata.json
|       walkthrough.md.resolved
|       walkthrough.md.resolved.0
|       walkthrough.md.resolved.1
|       walkthrough.md.resolved.2
|       walkthrough.md.resolved.3
|       walkthrough.md.resolved.4
|       walkthrough.md.resolved.5
|       walkthrough.md.resolved.6
|       
+---logs
+---scripts
|       build.py
|       
+---src
|   \---luanny
|       |   auth.py
|       |   browser.py
|       |   cli.py
|       |   config.py
|       |   evidence_capture.py
|       |   exporters.py
|       |   log.py
|       |   models.py
|       |   orchestrator.py
|       |   post_extractor.py
|       |   profile_discovery.py
|       |   selectors.py
|       |   __init__.py
|       |   __main__.py
|       |   
|       \---__pycache__
|               auth.cpython-310.pyc
|               browser.cpython-310.pyc
|               cli.cpython-310.pyc
|               config.cpython-310.pyc
|               evidence_capture.cpython-310.pyc
|               exporters.cpython-310.pyc
|               log.cpython-310.pyc
|               models.cpython-310.pyc
|               orchestrator.cpython-310.pyc
|               post_extractor.cpython-310.pyc
|               profile_discovery.cpython-310.pyc
|               selectors.cpython-310.pyc
|               __init__.cpython-310.pyc
|               __init__.cpython-312.pyc
|               __main__.cpython-310.pyc
|               
\---tests
    |   conftest.py
    |   test_auth.py
    |   test_browser.py
    |   test_config.py
    |   test_discovery.py
    |   test_e2e.py
    |   test_evidence.py
    |   test_exporters.py
    |   test_extractor.py
    |   test_models.py
    |   test_robustness.py
    |   
    +---fixtures
    |   \---instagram
    |           __init__.py
    |           
    \---__pycache__
            conftest.cpython-310-pytest-9.0.3.pyc
            test_auth.cpython-310-pytest-9.0.3.pyc
            test_browser.cpython-310-pytest-9.0.3.pyc
            test_config.cpython-310-pytest-9.0.3.pyc
            test_discovery.cpython-310-pytest-9.0.3.pyc
            test_e2e.cpython-310-pytest-9.0.3.pyc
            test_evidence.cpython-310-pytest-9.0.3.pyc
            test_exporters.cpython-310-pytest-9.0.3.pyc
            test_extractor.cpython-310-pytest-9.0.3.pyc
            test_models.cpython-310-pytest-9.0.3.pyc
            test_robustness.cpython-310-pytest-9.0.3.pyc
            
``` 
