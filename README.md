###### Setup

#### Gnuplot

  - misc.

#### LaTex

  - `latexmk`
  - `Texlive` - base + recommended

#### PDF

  - `zathura`

#### Python

  - `matplotlib`
  - `numpy`
  - `pandas`

#### Unix

  - `xdotool`

#### Vim

  - `vimTeX`
  - `ultisnips`

#### Zathura

  - misc.
###### Gnuplot

  - misc.

#### LaTex

  - `latexmk`
  - `Texlive` - base + recommended

#### PDF

  - `zathura`

#### Python

  - `matplotlib`
  - `numpy`
  - `pandas`

#### Unix

  - `xdotool`

#### Vim

  - `vimTeX`
  - `ultisnips`

#### Zathura

  - misc.

###### tree
```
.
├── calculus
│   └── 1.doc
│       └── lambda.pdf
├── CHANGELOG.md
├── .gitignore
├── lpmn_project
│   ├── bin
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── easy_install
│   │   ├── easy_install-3.6
│   │   ├── f2py
│   │   ├── f2py3
│   │   ├── f2py3.6
│   │   ├── iptest
│   │   ├── iptest3
│   │   ├── ipython
│   │   ├── ipython3
│   │   ├── isympy
│   │   ├── jsonschema
│   │   ├── jupyter
│   │   ├── jupyter-bundlerextension
│   │   ├── jupyter-console
│   │   ├── jupyter-kernel
│   │   ├── jupyter-kernelspec
│   │   ├── jupyter-migrate
│   │   ├── jupyter-nbconvert
│   │   ├── jupyter-nbextension
│   │   ├── jupyter-notebook
│   │   ├── jupyter-qtconsole
│   │   ├── jupyter-run
│   │   ├── jupyter-serverextension
│   │   ├── jupyter-troubleshoot
│   │   ├── jupyter-trust
│   │   ├── nosetests
│   │   ├── nosetests-3.4
│   │   ├── pip
│   │   ├── pip3
│   │   ├── pip3.6
│   │   ├── pygmentize
│   │   ├── python -> python3
│   │   └── python3 -> /usr/bin/python3
│   ├── etc
│   │   └── jupyter
│   │       └── nbconfig
│   │           └── notebook.d
│   │               └── widgetsnbextension.json
│   ├── include
│   ├── lib
│   │   └── python3.6
│   │       └── site-packages
│   │           ├── attr
│   │           │   ├── _compat.py
│   │           │   ├── _config.py
│   │           │   ├── converters.py
│   │           │   ├── converters.pyi
│   │           │   ├── exceptions.py
│   │           │   ├── exceptions.pyi
│   │           │   ├── filters.py
│   │           │   ├── filters.pyi
│   │           │   ├── _funcs.py
│   │           │   ├── __init__.py
│   │           │   ├── __init__.pyi
│   │           │   ├── _make.py
│   │           │   ├── __pycache__
│   │           │   │   ├── _compat.cpython-36.pyc
│   │           │   │   ├── _config.cpython-36.pyc
│   │           │   │   ├── converters.cpython-36.pyc
│   │           │   │   ├── exceptions.cpython-36.pyc
│   │           │   │   ├── filters.cpython-36.pyc
│   │           │   │   ├── _funcs.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── _make.cpython-36.pyc
│   │           │   │   └── validators.cpython-36.pyc
│   │           │   ├── py.typed
│   │           │   ├── validators.py
│   │           │   └── validators.pyi
│   │           ├── attrs-19.1.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── backcall
│   │           │   ├── backcall.py
│   │           │   ├── __init__.py
│   │           │   ├── __pycache__
│   │           │   │   ├── backcall.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   └── _signatures.cpython-36.pyc
│   │           │   └── _signatures.py
│   │           ├── backcall-0.1.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── bleach
│   │           │   ├── callbacks.py
│   │           │   ├── html5lib_shim.py
│   │           │   ├── __init__.py
│   │           │   ├── linkifier.py
│   │           │   ├── __pycache__
│   │           │   │   ├── callbacks.cpython-36.pyc
│   │           │   │   ├── html5lib_shim.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── linkifier.cpython-36.pyc
│   │           │   │   ├── sanitizer.cpython-36.pyc
│   │           │   │   └── utils.cpython-36.pyc
│   │           │   ├── sanitizer.py
│   │           │   ├── utils.py
│   │           │   └── _vendor
│   │           │       ├── html5lib
│   │           │       │   ├── constants.py
│   │           │       │   ├── filters
│   │           │       │   │   ├── alphabeticalattributes.py
│   │           │       │   │   ├── base.py
│   │           │       │   │   ├── __init__.py
│   │           │       │   │   ├── inject_meta_charset.py
│   │           │       │   │   ├── lint.py
│   │           │       │   │   ├── optionaltags.py
│   │           │       │   │   ├── __pycache__
│   │           │       │   │   │   ├── alphabeticalattributes.cpython-36.pyc
│   │           │       │   │   │   ├── base.cpython-36.pyc
│   │           │       │   │   │   ├── __init__.cpython-36.pyc
│   │           │       │   │   │   ├── inject_meta_charset.cpython-36.pyc
│   │           │       │   │   │   ├── lint.cpython-36.pyc
│   │           │       │   │   │   ├── optionaltags.cpython-36.pyc
│   │           │       │   │   │   ├── sanitizer.cpython-36.pyc
│   │           │       │   │   │   └── whitespace.cpython-36.pyc
│   │           │       │   │   ├── sanitizer.py
│   │           │       │   │   └── whitespace.py
│   │           │       │   ├── html5parser.py
│   │           │       │   ├── _ihatexml.py
│   │           │       │   ├── __init__.py
│   │           │       │   ├── _inputstream.py
│   │           │       │   ├── __pycache__
│   │           │       │   │   ├── constants.cpython-36.pyc
│   │           │       │   │   ├── html5parser.cpython-36.pyc
│   │           │       │   │   ├── _ihatexml.cpython-36.pyc
│   │           │       │   │   ├── __init__.cpython-36.pyc
│   │           │       │   │   ├── _inputstream.cpython-36.pyc
│   │           │       │   │   ├── serializer.cpython-36.pyc
│   │           │       │   │   ├── _tokenizer.cpython-36.pyc
│   │           │       │   │   └── _utils.cpython-36.pyc
│   │           │       │   ├── serializer.py
│   │           │       │   ├── _tokenizer.py
│   │           │       │   ├── treeadapters
│   │           │       │   │   ├── genshi.py
│   │           │       │   │   ├── __init__.py
│   │           │       │   │   ├── __pycache__
│   │           │       │   │   │   ├── genshi.cpython-36.pyc
│   │           │       │   │   │   ├── __init__.cpython-36.pyc
│   │           │       │   │   │   └── sax.cpython-36.pyc
│   │           │       │   │   └── sax.py
│   │           │       │   ├── treebuilders
│   │           │       │   │   ├── base.py
│   │           │       │   │   ├── dom.py
│   │           │       │   │   ├── etree_lxml.py
│   │           │       │   │   ├── etree.py
│   │           │       │   │   ├── __init__.py
│   │           │       │   │   └── __pycache__
│   │           │       │   │       ├── base.cpython-36.pyc
│   │           │       │   │       ├── dom.cpython-36.pyc
│   │           │       │   │       ├── etree.cpython-36.pyc
│   │           │       │   │       ├── etree_lxml.cpython-36.pyc
│   │           │       │   │       └── __init__.cpython-36.pyc
│   │           │       │   ├── treewalkers
│   │           │       │   │   ├── base.py
│   │           │       │   │   ├── dom.py
│   │           │       │   │   ├── etree_lxml.py
│   │           │       │   │   ├── etree.py
│   │           │       │   │   ├── genshi.py
│   │           │       │   │   ├── __init__.py
│   │           │       │   │   └── __pycache__
│   │           │       │   │       ├── base.cpython-36.pyc
│   │           │       │   │       ├── dom.cpython-36.pyc
│   │           │       │   │       ├── etree.cpython-36.pyc
│   │           │       │   │       ├── etree_lxml.cpython-36.pyc
│   │           │       │   │       ├── genshi.cpython-36.pyc
│   │           │       │   │       └── __init__.cpython-36.pyc
│   │           │       │   ├── _trie
│   │           │       │   │   ├── _base.py
│   │           │       │   │   ├── datrie.py
│   │           │       │   │   ├── __init__.py
│   │           │       │   │   ├── __pycache__
│   │           │       │   │   │   ├── _base.cpython-36.pyc
│   │           │       │   │   │   ├── datrie.cpython-36.pyc
│   │           │       │   │   │   ├── __init__.cpython-36.pyc
│   │           │       │   │   │   └── py.cpython-36.pyc
│   │           │       │   │   └── py.py
│   │           │       │   └── _utils.py
│   │           │       ├── html5lib-1.0.1.dist-info
│   │           │       │   ├── DESCRIPTION.rst
│   │           │       │   ├── INSTALLER
│   │           │       │   ├── LICENSE.txt
│   │           │       │   ├── METADATA
│   │           │       │   ├── metadata.json
│   │           │       │   ├── RECORD
│   │           │       │   ├── top_level.txt
│   │           │       │   └── WHEEL
│   │           │       ├── __init__.py
│   │           │       ├── pip_install_vendor.sh
│   │           │       ├── __pycache__
│   │           │       │   └── __init__.cpython-36.pyc
│   │           │       ├── README.rst
│   │           │       └── vendor.txt
│   │           ├── bleach-3.1.0.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── cycler-0.10.0.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── cycler.py
│   │           ├── dateutil
│   │           │   ├── _common.py
│   │           │   ├── easter.py
│   │           │   ├── __init__.py
│   │           │   ├── parser
│   │           │   │   ├── __init__.py
│   │           │   │   ├── isoparser.py
│   │           │   │   ├── _parser.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       ├── isoparser.cpython-36.pyc
│   │           │   │       └── _parser.cpython-36.pyc
│   │           │   ├── __pycache__
│   │           │   │   ├── _common.cpython-36.pyc
│   │           │   │   ├── easter.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── relativedelta.cpython-36.pyc
│   │           │   │   ├── rrule.cpython-36.pyc
│   │           │   │   ├── tzwin.cpython-36.pyc
│   │           │   │   ├── utils.cpython-36.pyc
│   │           │   │   └── _version.cpython-36.pyc
│   │           │   ├── relativedelta.py
│   │           │   ├── rrule.py
│   │           │   ├── tz
│   │           │   │   ├── _common.py
│   │           │   │   ├── _factories.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _common.cpython-36.pyc
│   │           │   │   │   ├── _factories.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── tz.cpython-36.pyc
│   │           │   │   │   └── win.cpython-36.pyc
│   │           │   │   ├── tz.py
│   │           │   │   └── win.py
│   │           │   ├── tzwin.py
│   │           │   ├── utils.py
│   │           │   ├── _version.py
│   │           │   └── zoneinfo
│   │           │       ├── dateutil-zoneinfo.tar.gz
│   │           │       ├── __init__.py
│   │           │       ├── __pycache__
│   │           │       │   ├── __init__.cpython-36.pyc
│   │           │       │   └── rebuild.cpython-36.pyc
│   │           │       └── rebuild.py
│   │           ├── decorator-4.4.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── pbr.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── decorator.py
│   │           ├── defusedxml
│   │           │   ├── cElementTree.py
│   │           │   ├── common.py
│   │           │   ├── ElementTree.py
│   │           │   ├── expatbuilder.py
│   │           │   ├── expatreader.py
│   │           │   ├── __init__.py
│   │           │   ├── lxml.py
│   │           │   ├── minidom.py
│   │           │   ├── pulldom.py
│   │           │   ├── __pycache__
│   │           │   │   ├── cElementTree.cpython-36.pyc
│   │           │   │   ├── common.cpython-36.pyc
│   │           │   │   ├── ElementTree.cpython-36.pyc
│   │           │   │   ├── expatbuilder.cpython-36.pyc
│   │           │   │   ├── expatreader.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── lxml.cpython-36.pyc
│   │           │   │   ├── minidom.cpython-36.pyc
│   │           │   │   ├── pulldom.cpython-36.pyc
│   │           │   │   ├── sax.cpython-36.pyc
│   │           │   │   └── xmlrpc.cpython-36.pyc
│   │           │   ├── sax.py
│   │           │   └── xmlrpc.py
│   │           ├── defusedxml-0.6.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── easy_install.py
│   │           ├── entrypoints-0.3.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── entrypoints.py
│   │           ├── ipykernel
│   │           │   ├── codeutil.py
│   │           │   ├── comm
│   │           │   │   ├── comm.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── manager.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── comm.cpython-36.pyc
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       └── manager.cpython-36.pyc
│   │           │   ├── connect.py
│   │           │   ├── datapub.py
│   │           │   ├── displayhook.py
│   │           │   ├── embed.py
│   │           │   ├── _eventloop_macos.py
│   │           │   ├── eventloops.py
│   │           │   ├── gui
│   │           │   │   ├── gtk3embed.py
│   │           │   │   ├── gtkembed.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── gtk3embed.cpython-36.pyc
│   │           │   │       ├── gtkembed.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── heartbeat.py
│   │           │   ├── __init__.py
│   │           │   ├── inprocess
│   │           │   │   ├── blocking.py
│   │           │   │   ├── channels.py
│   │           │   │   ├── client.py
│   │           │   │   ├── constants.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── ipkernel.py
│   │           │   │   ├── manager.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── blocking.cpython-36.pyc
│   │           │   │   │   ├── channels.cpython-36.pyc
│   │           │   │   │   ├── client.cpython-36.pyc
│   │           │   │   │   ├── constants.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── ipkernel.cpython-36.pyc
│   │           │   │   │   ├── manager.cpython-36.pyc
│   │           │   │   │   └── socket.cpython-36.pyc
│   │           │   │   ├── socket.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_kernel.cpython-36.pyc
│   │           │   │       │   └── test_kernelmanager.cpython-36.pyc
│   │           │   │       ├── test_kernelmanager.py
│   │           │   │       └── test_kernel.py
│   │           │   ├── iostream.py
│   │           │   ├── ipkernel.py
│   │           │   ├── jsonutil.py
│   │           │   ├── kernelapp.py
│   │           │   ├── kernelbase.py
│   │           │   ├── kernelspec.py
│   │           │   ├── log.py
│   │           │   ├── __main__.py
│   │           │   ├── parentpoller.py
│   │           │   ├── pickleutil.py
│   │           │   ├── __pycache__
│   │           │   │   ├── codeutil.cpython-36.pyc
│   │           │   │   ├── connect.cpython-36.pyc
│   │           │   │   ├── datapub.cpython-36.pyc
│   │           │   │   ├── displayhook.cpython-36.pyc
│   │           │   │   ├── embed.cpython-36.pyc
│   │           │   │   ├── _eventloop_macos.cpython-36.pyc
│   │           │   │   ├── eventloops.cpython-36.pyc
│   │           │   │   ├── heartbeat.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── iostream.cpython-36.pyc
│   │           │   │   ├── ipkernel.cpython-36.pyc
│   │           │   │   ├── jsonutil.cpython-36.pyc
│   │           │   │   ├── kernelapp.cpython-36.pyc
│   │           │   │   ├── kernelbase.cpython-36.pyc
│   │           │   │   ├── kernelspec.cpython-36.pyc
│   │           │   │   ├── log.cpython-36.pyc
│   │           │   │   ├── __main__.cpython-36.pyc
│   │           │   │   ├── parentpoller.cpython-36.pyc
│   │           │   │   ├── pickleutil.cpython-36.pyc
│   │           │   │   ├── serialize.cpython-36.pyc
│   │           │   │   ├── _version.cpython-36.pyc
│   │           │   │   └── zmqshell.cpython-36.pyc
│   │           │   ├── pylab
│   │           │   │   ├── backend_inline.py
│   │           │   │   ├── config.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── backend_inline.cpython-36.pyc
│   │           │   │       ├── config.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── resources
│   │           │   │   ├── logo-32x32.png
│   │           │   │   └── logo-64x64.png
│   │           │   ├── serialize.py
│   │           │   ├── tests
│   │           │   │   ├── _asyncio.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _asyncio.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── test_async.cpython-36.pyc
│   │           │   │   │   ├── test_connect.cpython-36.pyc
│   │           │   │   │   ├── test_embed_kernel.cpython-36.pyc
│   │           │   │   │   ├── test_eventloop.cpython-36.pyc
│   │           │   │   │   ├── test_io.cpython-36.pyc
│   │           │   │   │   ├── test_jsonutil.cpython-36.pyc
│   │           │   │   │   ├── test_kernel.cpython-36.pyc
│   │           │   │   │   ├── test_kernelspec.cpython-36.pyc
│   │           │   │   │   ├── test_message_spec.cpython-36.pyc
│   │           │   │   │   ├── test_pickleutil.cpython-36.pyc
│   │           │   │   │   ├── test_serialize.cpython-36.pyc
│   │           │   │   │   ├── test_start_kernel.cpython-36.pyc
│   │           │   │   │   ├── test_zmq_shell.cpython-36.pyc
│   │           │   │   │   └── utils.cpython-36.pyc
│   │           │   │   ├── test_async.py
│   │           │   │   ├── test_connect.py
│   │           │   │   ├── test_embed_kernel.py
│   │           │   │   ├── test_eventloop.py
│   │           │   │   ├── test_io.py
│   │           │   │   ├── test_jsonutil.py
│   │           │   │   ├── test_kernel.py
│   │           │   │   ├── test_kernelspec.py
│   │           │   │   ├── test_message_spec.py
│   │           │   │   ├── test_pickleutil.py
│   │           │   │   ├── test_serialize.py
│   │           │   │   ├── test_start_kernel.py
│   │           │   │   ├── test_zmq_shell.py
│   │           │   │   └── utils.py
│   │           │   ├── _version.py
│   │           │   └── zmqshell.py
│   │           ├── ipykernel-5.1.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── ipykernel_launcher.py
│   │           ├── IPython
│   │           │   ├── config.py
│   │           │   ├── consoleapp.py
│   │           │   ├── core
│   │           │   │   ├── alias.py
│   │           │   │   ├── application.py
│   │           │   │   ├── async_helpers.py
│   │           │   │   ├── autocall.py
│   │           │   │   ├── builtin_trap.py
│   │           │   │   ├── compilerop.py
│   │           │   │   ├── completerlib.py
│   │           │   │   ├── completer.py
│   │           │   │   ├── crashhandler.py
│   │           │   │   ├── debugger.py
│   │           │   │   ├── displayhook.py
│   │           │   │   ├── displaypub.py
│   │           │   │   ├── display.py
│   │           │   │   ├── display_trap.py
│   │           │   │   ├── error.py
│   │           │   │   ├── events.py
│   │           │   │   ├── excolors.py
│   │           │   │   ├── extensions.py
│   │           │   │   ├── formatters.py
│   │           │   │   ├── getipython.py
│   │           │   │   ├── historyapp.py
│   │           │   │   ├── history.py
│   │           │   │   ├── hooks.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── inputsplitter.py
│   │           │   │   ├── inputtransformer2.py
│   │           │   │   ├── inputtransformer.py
│   │           │   │   ├── interactiveshell.py
│   │           │   │   ├── latex_symbols.py
│   │           │   │   ├── logger.py
│   │           │   │   ├── macro.py
│   │           │   │   ├── magic_arguments.py
│   │           │   │   ├── magic.py
│   │           │   │   ├── magics
│   │           │   │   │   ├── auto.py
│   │           │   │   │   ├── basic.py
│   │           │   │   │   ├── code.py
│   │           │   │   │   ├── config.py
│   │           │   │   │   ├── display.py
│   │           │   │   │   ├── execution.py
│   │           │   │   │   ├── extension.py
│   │           │   │   │   ├── history.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── logging.py
│   │           │   │   │   ├── namespace.py
│   │           │   │   │   ├── osm.py
│   │           │   │   │   ├── packaging.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── auto.cpython-36.pyc
│   │           │   │   │   │   ├── basic.cpython-36.pyc
│   │           │   │   │   │   ├── code.cpython-36.pyc
│   │           │   │   │   │   ├── config.cpython-36.pyc
│   │           │   │   │   │   ├── display.cpython-36.pyc
│   │           │   │   │   │   ├── execution.cpython-36.pyc
│   │           │   │   │   │   ├── extension.cpython-36.pyc
│   │           │   │   │   │   ├── history.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── logging.cpython-36.pyc
│   │           │   │   │   │   ├── namespace.cpython-36.pyc
│   │           │   │   │   │   ├── osm.cpython-36.pyc
│   │           │   │   │   │   ├── packaging.cpython-36.pyc
│   │           │   │   │   │   ├── pylab.cpython-36.pyc
│   │           │   │   │   │   └── script.cpython-36.pyc
│   │           │   │   │   ├── pylab.py
│   │           │   │   │   └── script.py
│   │           │   │   ├── oinspect.py
│   │           │   │   ├── page.py
│   │           │   │   ├── payloadpage.py
│   │           │   │   ├── payload.py
│   │           │   │   ├── prefilter.py
│   │           │   │   ├── profile
│   │           │   │   │   └── README_STARTUP
│   │           │   │   ├── profileapp.py
│   │           │   │   ├── profiledir.py
│   │           │   │   ├── prompts.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── alias.cpython-36.pyc
│   │           │   │   │   ├── application.cpython-36.pyc
│   │           │   │   │   ├── async_helpers.cpython-36.pyc
│   │           │   │   │   ├── autocall.cpython-36.pyc
│   │           │   │   │   ├── builtin_trap.cpython-36.pyc
│   │           │   │   │   ├── compilerop.cpython-36.pyc
│   │           │   │   │   ├── completer.cpython-36.pyc
│   │           │   │   │   ├── completerlib.cpython-36.pyc
│   │           │   │   │   ├── crashhandler.cpython-36.pyc
│   │           │   │   │   ├── debugger.cpython-36.pyc
│   │           │   │   │   ├── display.cpython-36.pyc
│   │           │   │   │   ├── displayhook.cpython-36.pyc
│   │           │   │   │   ├── displaypub.cpython-36.pyc
│   │           │   │   │   ├── display_trap.cpython-36.pyc
│   │           │   │   │   ├── error.cpython-36.pyc
│   │           │   │   │   ├── events.cpython-36.pyc
│   │           │   │   │   ├── excolors.cpython-36.pyc
│   │           │   │   │   ├── extensions.cpython-36.pyc
│   │           │   │   │   ├── formatters.cpython-36.pyc
│   │           │   │   │   ├── getipython.cpython-36.pyc
│   │           │   │   │   ├── historyapp.cpython-36.pyc
│   │           │   │   │   ├── history.cpython-36.pyc
│   │           │   │   │   ├── hooks.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── inputsplitter.cpython-36.pyc
│   │           │   │   │   ├── inputtransformer2.cpython-36.pyc
│   │           │   │   │   ├── inputtransformer.cpython-36.pyc
│   │           │   │   │   ├── interactiveshell.cpython-36.pyc
│   │           │   │   │   ├── latex_symbols.cpython-36.pyc
│   │           │   │   │   ├── logger.cpython-36.pyc
│   │           │   │   │   ├── macro.cpython-36.pyc
│   │           │   │   │   ├── magic_arguments.cpython-36.pyc
│   │           │   │   │   ├── magic.cpython-36.pyc
│   │           │   │   │   ├── oinspect.cpython-36.pyc
│   │           │   │   │   ├── page.cpython-36.pyc
│   │           │   │   │   ├── payload.cpython-36.pyc
│   │           │   │   │   ├── payloadpage.cpython-36.pyc
│   │           │   │   │   ├── prefilter.cpython-36.pyc
│   │           │   │   │   ├── profileapp.cpython-36.pyc
│   │           │   │   │   ├── profiledir.cpython-36.pyc
│   │           │   │   │   ├── prompts.cpython-36.pyc
│   │           │   │   │   ├── pylabtools.cpython-36.pyc
│   │           │   │   │   ├── release.cpython-36.pyc
│   │           │   │   │   ├── shellapp.cpython-36.pyc
│   │           │   │   │   ├── splitinput.cpython-36.pyc
│   │           │   │   │   ├── ultratb.cpython-36.pyc
│   │           │   │   │   └── usage.cpython-36.pyc
│   │           │   │   ├── pylabtools.py
│   │           │   │   ├── release.py
│   │           │   │   ├── shellapp.py
│   │           │   │   ├── splitinput.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── 2x2.jpg
│   │           │   │   │   ├── 2x2.png
│   │           │   │   │   ├── bad_all.py
│   │           │   │   │   ├── daft_extension
│   │           │   │   │   │   ├── daft_extension.py
│   │           │   │   │   │   └── __pycache__
│   │           │   │   │   │       └── daft_extension.cpython-36.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── nonascii2.py
│   │           │   │   │   ├── nonascii.py
│   │           │   │   │   ├── print_argv.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── bad_all.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── nonascii2.cpython-36.pyc
│   │           │   │   │   │   ├── nonascii.cpython-36.pyc
│   │           │   │   │   │   ├── print_argv.cpython-36.pyc
│   │           │   │   │   │   ├── refbug.cpython-36.pyc
│   │           │   │   │   │   ├── simpleerr.cpython-36.pyc
│   │           │   │   │   │   ├── tclass.cpython-36.pyc
│   │           │   │   │   │   ├── test_alias.cpython-36.pyc
│   │           │   │   │   │   ├── test_application.cpython-36.pyc
│   │           │   │   │   │   ├── test_async_helpers.cpython-36.pyc
│   │           │   │   │   │   ├── test_autocall.cpython-36.pyc
│   │           │   │   │   │   ├── test_compilerop.cpython-36.pyc
│   │           │   │   │   │   ├── test_completer.cpython-36.pyc
│   │           │   │   │   │   ├── test_completerlib.cpython-36.pyc
│   │           │   │   │   │   ├── test_debugger.cpython-36.pyc
│   │           │   │   │   │   ├── test_display.cpython-36.pyc
│   │           │   │   │   │   ├── test_displayhook.cpython-36.pyc
│   │           │   │   │   │   ├── test_events.cpython-36.pyc
│   │           │   │   │   │   ├── test_extension.cpython-36.pyc
│   │           │   │   │   │   ├── test_formatters.cpython-36.pyc
│   │           │   │   │   │   ├── test_handlers.cpython-36.pyc
│   │           │   │   │   │   ├── test_history.cpython-36.pyc
│   │           │   │   │   │   ├── test_hooks.cpython-36.pyc
│   │           │   │   │   │   ├── test_imports.cpython-36.pyc
│   │           │   │   │   │   ├── test_inputsplitter.cpython-36.pyc
│   │           │   │   │   │   ├── test_inputtransformer2.cpython-36.pyc
│   │           │   │   │   │   ├── test_inputtransformer2_line.cpython-36.pyc
│   │           │   │   │   │   ├── test_inputtransformer.cpython-36.pyc
│   │           │   │   │   │   ├── test_interactiveshell.cpython-36.pyc
│   │           │   │   │   │   ├── test_iplib.cpython-36.pyc
│   │           │   │   │   │   ├── test_logger.cpython-36.pyc
│   │           │   │   │   │   ├── test_magic_arguments.cpython-36.pyc
│   │           │   │   │   │   ├── test_magic.cpython-36.pyc
│   │           │   │   │   │   ├── test_magic_terminal.cpython-36.pyc
│   │           │   │   │   │   ├── test_oinspect.cpython-36.pyc
│   │           │   │   │   │   ├── test_page.cpython-36.pyc
│   │           │   │   │   │   ├── test_paths.cpython-36.pyc
│   │           │   │   │   │   ├── test_prefilter.cpython-36.pyc
│   │           │   │   │   │   ├── test_profile.cpython-36.pyc
│   │           │   │   │   │   ├── test_prompts.cpython-36.pyc
│   │           │   │   │   │   ├── test_pylabtools.cpython-36.pyc
│   │           │   │   │   │   ├── test_run.cpython-36.pyc
│   │           │   │   │   │   ├── test_shellapp.cpython-36.pyc
│   │           │   │   │   │   ├── test_splitinput.cpython-36.pyc
│   │           │   │   │   │   └── test_ultratb.cpython-36.pyc
│   │           │   │   │   ├── refbug.py
│   │           │   │   │   ├── simpleerr.py
│   │           │   │   │   ├── tclass.py
│   │           │   │   │   ├── test_alias.py
│   │           │   │   │   ├── test_application.py
│   │           │   │   │   ├── test_async_helpers.py
│   │           │   │   │   ├── test_autocall.py
│   │           │   │   │   ├── test_compilerop.py
│   │           │   │   │   ├── test_completerlib.py
│   │           │   │   │   ├── test_completer.py
│   │           │   │   │   ├── test_debugger.py
│   │           │   │   │   ├── test_displayhook.py
│   │           │   │   │   ├── test_display.py
│   │           │   │   │   ├── test_events.py
│   │           │   │   │   ├── test_extension.py
│   │           │   │   │   ├── test_formatters.py
│   │           │   │   │   ├── test_handlers.py
│   │           │   │   │   ├── test_history.py
│   │           │   │   │   ├── test_hooks.py
│   │           │   │   │   ├── test_imports.py
│   │           │   │   │   ├── test_inputsplitter.py
│   │           │   │   │   ├── test_inputtransformer2_line.py
│   │           │   │   │   ├── test_inputtransformer2.py
│   │           │   │   │   ├── test_inputtransformer.py
│   │           │   │   │   ├── test_interactiveshell.py
│   │           │   │   │   ├── test_iplib.py
│   │           │   │   │   ├── test_logger.py
│   │           │   │   │   ├── test_magic_arguments.py
│   │           │   │   │   ├── test_magic.py
│   │           │   │   │   ├── test_magic_terminal.py
│   │           │   │   │   ├── test_oinspect.py
│   │           │   │   │   ├── test_page.py
│   │           │   │   │   ├── test_paths.py
│   │           │   │   │   ├── test_prefilter.py
│   │           │   │   │   ├── test_profile.py
│   │           │   │   │   ├── test_prompts.py
│   │           │   │   │   ├── test_pylabtools.py
│   │           │   │   │   ├── test_run.py
│   │           │   │   │   ├── test_shellapp.py
│   │           │   │   │   ├── test_splitinput.py
│   │           │   │   │   └── test_ultratb.py
│   │           │   │   ├── ultratb.py
│   │           │   │   └── usage.py
│   │           │   ├── display.py
│   │           │   ├── extensions
│   │           │   │   ├── autoreload.py
│   │           │   │   ├── cythonmagic.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── autoreload.cpython-36.pyc
│   │           │   │   │   ├── cythonmagic.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── rmagic.cpython-36.pyc
│   │           │   │   │   ├── storemagic.cpython-36.pyc
│   │           │   │   │   └── sympyprinting.cpython-36.pyc
│   │           │   │   ├── rmagic.py
│   │           │   │   ├── storemagic.py
│   │           │   │   ├── sympyprinting.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_autoreload.cpython-36.pyc
│   │           │   │       │   └── test_storemagic.cpython-36.pyc
│   │           │   │       ├── test_autoreload.py
│   │           │   │       └── test_storemagic.py
│   │           │   ├── external
│   │           │   │   ├── decorators
│   │           │   │   │   ├── _decorators.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _numpy_testing_noseclasses.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── _decorators.cpython-36.pyc
│   │           │   │   │       ├── __init__.cpython-36.pyc
│   │           │   │   │       └── _numpy_testing_noseclasses.cpython-36.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── mathjax.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── mathjax.cpython-36.pyc
│   │           │   │   │   ├── qt_for_kernel.cpython-36.pyc
│   │           │   │   │   └── qt_loaders.cpython-36.pyc
│   │           │   │   ├── qt_for_kernel.py
│   │           │   │   └── qt_loaders.py
│   │           │   ├── frontend.py
│   │           │   ├── html.py
│   │           │   ├── __init__.py
│   │           │   ├── kernel
│   │           │   │   ├── adapter.py
│   │           │   │   ├── channelsabc.py
│   │           │   │   ├── channels.py
│   │           │   │   ├── clientabc.py
│   │           │   │   ├── client.py
│   │           │   │   ├── connect.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── kernelspecapp.py
│   │           │   │   ├── kernelspec.py
│   │           │   │   ├── launcher.py
│   │           │   │   ├── __main__.py
│   │           │   │   ├── managerabc.py
│   │           │   │   ├── manager.py
│   │           │   │   ├── multikernelmanager.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── adapter.cpython-36.pyc
│   │           │   │   │   ├── channelsabc.cpython-36.pyc
│   │           │   │   │   ├── channels.cpython-36.pyc
│   │           │   │   │   ├── clientabc.cpython-36.pyc
│   │           │   │   │   ├── client.cpython-36.pyc
│   │           │   │   │   ├── connect.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── kernelspecapp.cpython-36.pyc
│   │           │   │   │   ├── kernelspec.cpython-36.pyc
│   │           │   │   │   ├── launcher.cpython-36.pyc
│   │           │   │   │   ├── __main__.cpython-36.pyc
│   │           │   │   │   ├── managerabc.cpython-36.pyc
│   │           │   │   │   ├── manager.cpython-36.pyc
│   │           │   │   │   ├── multikernelmanager.cpython-36.pyc
│   │           │   │   │   ├── restarter.cpython-36.pyc
│   │           │   │   │   └── threaded.cpython-36.pyc
│   │           │   │   ├── restarter.py
│   │           │   │   └── threaded.py
│   │           │   ├── lib
│   │           │   │   ├── backgroundjobs.py
│   │           │   │   ├── clipboard.py
│   │           │   │   ├── deepreload.py
│   │           │   │   ├── demo.py
│   │           │   │   ├── display.py
│   │           │   │   ├── editorhooks.py
│   │           │   │   ├── guisupport.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── inputhookglut.py
│   │           │   │   ├── inputhookgtk3.py
│   │           │   │   ├── inputhookgtk.py
│   │           │   │   ├── inputhook.py
│   │           │   │   ├── inputhookpyglet.py
│   │           │   │   ├── inputhookqt4.py
│   │           │   │   ├── inputhookwx.py
│   │           │   │   ├── kernel.py
│   │           │   │   ├── latextools.py
│   │           │   │   ├── lexers.py
│   │           │   │   ├── pretty.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── backgroundjobs.cpython-36.pyc
│   │           │   │   │   ├── clipboard.cpython-36.pyc
│   │           │   │   │   ├── deepreload.cpython-36.pyc
│   │           │   │   │   ├── demo.cpython-36.pyc
│   │           │   │   │   ├── display.cpython-36.pyc
│   │           │   │   │   ├── editorhooks.cpython-36.pyc
│   │           │   │   │   ├── guisupport.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── inputhook.cpython-36.pyc
│   │           │   │   │   ├── inputhookglut.cpython-36.pyc
│   │           │   │   │   ├── inputhookgtk3.cpython-36.pyc
│   │           │   │   │   ├── inputhookgtk.cpython-36.pyc
│   │           │   │   │   ├── inputhookpyglet.cpython-36.pyc
│   │           │   │   │   ├── inputhookqt4.cpython-36.pyc
│   │           │   │   │   ├── inputhookwx.cpython-36.pyc
│   │           │   │   │   ├── kernel.cpython-36.pyc
│   │           │   │   │   ├── latextools.cpython-36.pyc
│   │           │   │   │   ├── lexers.cpython-36.pyc
│   │           │   │   │   ├── pretty.cpython-36.pyc
│   │           │   │   │   └── security.cpython-36.pyc
│   │           │   │   ├── security.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_backgroundjobs.cpython-36.pyc
│   │           │   │       │   ├── test_clipboard.cpython-36.pyc
│   │           │   │       │   ├── test_deepreload.cpython-36.pyc
│   │           │   │       │   ├── test_display.cpython-36.pyc
│   │           │   │       │   ├── test_editorhooks.cpython-36.pyc
│   │           │   │       │   ├── test_imports.cpython-36.pyc
│   │           │   │       │   ├── test_latextools.cpython-36.pyc
│   │           │   │       │   ├── test_lexers.cpython-36.pyc
│   │           │   │       │   ├── test_pretty.cpython-36.pyc
│   │           │   │       │   └── test_security.cpython-36.pyc
│   │           │   │       ├── test_backgroundjobs.py
│   │           │   │       ├── test_clipboard.py
│   │           │   │       ├── test_deepreload.py
│   │           │   │       ├── test_display.py
│   │           │   │       ├── test_editorhooks.py
│   │           │   │       ├── test_imports.py
│   │           │   │       ├── test_latextools.py
│   │           │   │       ├── test_lexers.py
│   │           │   │       ├── test_pretty.py
│   │           │   │       ├── test_security.py
│   │           │   │       └── test.wav
│   │           │   ├── __main__.py
│   │           │   ├── nbconvert.py
│   │           │   ├── nbformat.py
│   │           │   ├── parallel.py
│   │           │   ├── paths.py
│   │           │   ├── __pycache__
│   │           │   │   ├── config.cpython-36.pyc
│   │           │   │   ├── consoleapp.cpython-36.pyc
│   │           │   │   ├── display.cpython-36.pyc
│   │           │   │   ├── frontend.cpython-36.pyc
│   │           │   │   ├── html.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── __main__.cpython-36.pyc
│   │           │   │   ├── nbconvert.cpython-36.pyc
│   │           │   │   ├── nbformat.cpython-36.pyc
│   │           │   │   ├── parallel.cpython-36.pyc
│   │           │   │   ├── paths.cpython-36.pyc
│   │           │   │   └── qt.cpython-36.pyc
│   │           │   ├── qt.py
│   │           │   ├── sphinxext
│   │           │   │   ├── custom_doctests.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── ipython_console_highlighting.py
│   │           │   │   ├── ipython_directive.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── custom_doctests.cpython-36.pyc
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       ├── ipython_console_highlighting.cpython-36.pyc
│   │           │   │       └── ipython_directive.cpython-36.pyc
│   │           │   ├── terminal
│   │           │   │   ├── console.py
│   │           │   │   ├── debugger.py
│   │           │   │   ├── embed.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── interactiveshell.py
│   │           │   │   ├── ipapp.py
│   │           │   │   ├── magics.py
│   │           │   │   ├── prompts.py
│   │           │   │   ├── pt_inputhooks
│   │           │   │   │   ├── glut.py
│   │           │   │   │   ├── gtk3.py
│   │           │   │   │   ├── gtk.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── osx.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── glut.cpython-36.pyc
│   │           │   │   │   │   ├── gtk3.cpython-36.pyc
│   │           │   │   │   │   ├── gtk.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── osx.cpython-36.pyc
│   │           │   │   │   │   ├── pyglet.cpython-36.pyc
│   │           │   │   │   │   ├── qt.cpython-36.pyc
│   │           │   │   │   │   ├── tk.cpython-36.pyc
│   │           │   │   │   │   └── wx.cpython-36.pyc
│   │           │   │   │   ├── pyglet.py
│   │           │   │   │   ├── qt.py
│   │           │   │   │   ├── tk.py
│   │           │   │   │   └── wx.py
│   │           │   │   ├── ptshell.py
│   │           │   │   ├── ptutils.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── console.cpython-36.pyc
│   │           │   │   │   ├── debugger.cpython-36.pyc
│   │           │   │   │   ├── embed.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── interactiveshell.cpython-36.pyc
│   │           │   │   │   ├── ipapp.cpython-36.pyc
│   │           │   │   │   ├── magics.cpython-36.pyc
│   │           │   │   │   ├── prompts.cpython-36.pyc
│   │           │   │   │   ├── ptshell.cpython-36.pyc
│   │           │   │   │   ├── ptutils.cpython-36.pyc
│   │           │   │   │   └── shortcuts.cpython-36.pyc
│   │           │   │   ├── shortcuts.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_debug_magic.cpython-36.pyc
│   │           │   │       │   ├── test_embed.cpython-36.pyc
│   │           │   │       │   ├── test_help.cpython-36.pyc
│   │           │   │       │   └── test_interactivshell.cpython-36.pyc
│   │           │   │       ├── test_debug_magic.py
│   │           │   │       ├── test_embed.py
│   │           │   │       ├── test_help.py
│   │           │   │       └── test_interactivshell.py
│   │           │   ├── testing
│   │           │   │   ├── decorators.py
│   │           │   │   ├── globalipapp.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── iptestcontroller.py
│   │           │   │   ├── iptest.py
│   │           │   │   ├── ipunittest.py
│   │           │   │   ├── __main__.py
│   │           │   │   ├── plugin
│   │           │   │   │   ├── dtexample.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── ipdoctest.py
│   │           │   │   │   ├── iptest.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── dtexample.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── ipdoctest.cpython-36.pyc
│   │           │   │   │   │   ├── iptest.cpython-36.pyc
│   │           │   │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   │   ├── show_refs.cpython-36.pyc
│   │           │   │   │   │   ├── simple.cpython-36.pyc
│   │           │   │   │   │   ├── simplevars.cpython-36.pyc
│   │           │   │   │   │   ├── test_ipdoctest.cpython-36.pyc
│   │           │   │   │   │   └── test_refs.cpython-36.pyc
│   │           │   │   │   ├── README.txt
│   │           │   │   │   ├── setup.py
│   │           │   │   │   ├── show_refs.py
│   │           │   │   │   ├── simple.py
│   │           │   │   │   ├── simplevars.py
│   │           │   │   │   ├── test_combo.txt
│   │           │   │   │   ├── test_exampleip.txt
│   │           │   │   │   ├── test_example.txt
│   │           │   │   │   ├── test_ipdoctest.py
│   │           │   │   │   └── test_refs.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── decorators.cpython-36.pyc
│   │           │   │   │   ├── globalipapp.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── iptestcontroller.cpython-36.pyc
│   │           │   │   │   ├── iptest.cpython-36.pyc
│   │           │   │   │   ├── ipunittest.cpython-36.pyc
│   │           │   │   │   ├── __main__.cpython-36.pyc
│   │           │   │   │   ├── skipdoctest.cpython-36.pyc
│   │           │   │   │   └── tools.cpython-36.pyc
│   │           │   │   ├── skipdoctest.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_decorators.cpython-36.pyc
│   │           │   │   │   │   ├── test_ipunittest.cpython-36.pyc
│   │           │   │   │   │   └── test_tools.cpython-36.pyc
│   │           │   │   │   ├── test_decorators.py
│   │           │   │   │   ├── test_ipunittest.py
│   │           │   │   │   └── test_tools.py
│   │           │   │   └── tools.py
│   │           │   └── utils
│   │           │       ├── capture.py
│   │           │       ├── colorable.py
│   │           │       ├── coloransi.py
│   │           │       ├── contexts.py
│   │           │       ├── daemonize.py
│   │           │       ├── data.py
│   │           │       ├── decorators.py
│   │           │       ├── dir2.py
│   │           │       ├── encoding.py
│   │           │       ├── eventful.py
│   │           │       ├── frame.py
│   │           │       ├── generics.py
│   │           │       ├── importstring.py
│   │           │       ├── __init__.py
│   │           │       ├── io.py
│   │           │       ├── ipstruct.py
│   │           │       ├── jsonutil.py
│   │           │       ├── localinterfaces.py
│   │           │       ├── log.py
│   │           │       ├── module_paths.py
│   │           │       ├── openpy.py
│   │           │       ├── path.py
│   │           │       ├── pickleutil.py
│   │           │       ├── _process_cli.py
│   │           │       ├── _process_common.py
│   │           │       ├── _process_posix.py
│   │           │       ├── process.py
│   │           │       ├── _process_win32_controller.py
│   │           │       ├── _process_win32.py
│   │           │       ├── py3compat.py
│   │           │       ├── __pycache__
│   │           │       │   ├── capture.cpython-36.pyc
│   │           │       │   ├── colorable.cpython-36.pyc
│   │           │       │   ├── coloransi.cpython-36.pyc
│   │           │       │   ├── contexts.cpython-36.pyc
│   │           │       │   ├── daemonize.cpython-36.pyc
│   │           │       │   ├── data.cpython-36.pyc
│   │           │       │   ├── decorators.cpython-36.pyc
│   │           │       │   ├── dir2.cpython-36.pyc
│   │           │       │   ├── encoding.cpython-36.pyc
│   │           │       │   ├── eventful.cpython-36.pyc
│   │           │       │   ├── frame.cpython-36.pyc
│   │           │       │   ├── generics.cpython-36.pyc
│   │           │       │   ├── importstring.cpython-36.pyc
│   │           │       │   ├── __init__.cpython-36.pyc
│   │           │       │   ├── io.cpython-36.pyc
│   │           │       │   ├── ipstruct.cpython-36.pyc
│   │           │       │   ├── jsonutil.cpython-36.pyc
│   │           │       │   ├── localinterfaces.cpython-36.pyc
│   │           │       │   ├── log.cpython-36.pyc
│   │           │       │   ├── module_paths.cpython-36.pyc
│   │           │       │   ├── openpy.cpython-36.pyc
│   │           │       │   ├── path.cpython-36.pyc
│   │           │       │   ├── pickleutil.cpython-36.pyc
│   │           │       │   ├── _process_cli.cpython-36.pyc
│   │           │       │   ├── _process_common.cpython-36.pyc
│   │           │       │   ├── process.cpython-36.pyc
│   │           │       │   ├── _process_posix.cpython-36.pyc
│   │           │       │   ├── _process_win32_controller.cpython-36.pyc
│   │           │       │   ├── _process_win32.cpython-36.pyc
│   │           │       │   ├── py3compat.cpython-36.pyc
│   │           │       │   ├── PyColorize.cpython-36.pyc
│   │           │       │   ├── sentinel.cpython-36.pyc
│   │           │       │   ├── shimmodule.cpython-36.pyc
│   │           │       │   ├── signatures.cpython-36.pyc
│   │           │       │   ├── strdispatch.cpython-36.pyc
│   │           │       │   ├── _sysinfo.cpython-36.pyc
│   │           │       │   ├── sysinfo.cpython-36.pyc
│   │           │       │   ├── syspathcontext.cpython-36.pyc
│   │           │       │   ├── tempdir.cpython-36.pyc
│   │           │       │   ├── terminal.cpython-36.pyc
│   │           │       │   ├── text.cpython-36.pyc
│   │           │       │   ├── timing.cpython-36.pyc
│   │           │       │   ├── tokenutil.cpython-36.pyc
│   │           │       │   ├── traitlets.cpython-36.pyc
│   │           │       │   ├── tz.cpython-36.pyc
│   │           │       │   ├── ulinecache.cpython-36.pyc
│   │           │       │   ├── version.cpython-36.pyc
│   │           │       │   └── wildcard.cpython-36.pyc
│   │           │       ├── PyColorize.py
│   │           │       ├── sentinel.py
│   │           │       ├── shimmodule.py
│   │           │       ├── signatures.py
│   │           │       ├── strdispatch.py
│   │           │       ├── _sysinfo.py
│   │           │       ├── sysinfo.py
│   │           │       ├── syspathcontext.py
│   │           │       ├── tempdir.py
│   │           │       ├── terminal.py
│   │           │       ├── tests
│   │           │       │   ├── __init__.py
│   │           │       │   ├── __pycache__
│   │           │       │   │   ├── __init__.cpython-36.pyc
│   │           │       │   │   ├── test_capture.cpython-36.pyc
│   │           │       │   │   ├── test_decorators.cpython-36.pyc
│   │           │       │   │   ├── test_dir2.cpython-36.pyc
│   │           │       │   │   ├── test_imports.cpython-36.pyc
│   │           │       │   │   ├── test_importstring.cpython-36.pyc
│   │           │       │   │   ├── test_io.cpython-36.pyc
│   │           │       │   │   ├── test_module_paths.cpython-36.pyc
│   │           │       │   │   ├── test_openpy.cpython-36.pyc
│   │           │       │   │   ├── test_path.cpython-36.pyc
│   │           │       │   │   ├── test_process.cpython-36.pyc
│   │           │       │   │   ├── test_pycolorize.cpython-36.pyc
│   │           │       │   │   ├── test_shimmodule.cpython-36.pyc
│   │           │       │   │   ├── test_sysinfo.cpython-36.pyc
│   │           │       │   │   ├── test_tempdir.cpython-36.pyc
│   │           │       │   │   ├── test_text.cpython-36.pyc
│   │           │       │   │   ├── test_tokenutil.cpython-36.pyc
│   │           │       │   │   └── test_wildcard.cpython-36.pyc
│   │           │       │   ├── test_capture.py
│   │           │       │   ├── test_decorators.py
│   │           │       │   ├── test_dir2.py
│   │           │       │   ├── test_imports.py
│   │           │       │   ├── test_importstring.py
│   │           │       │   ├── test_io.py
│   │           │       │   ├── test_module_paths.py
│   │           │       │   ├── test_openpy.py
│   │           │       │   ├── test_path.py
│   │           │       │   ├── test_process.py
│   │           │       │   ├── test_pycolorize.py
│   │           │       │   ├── test_shimmodule.py
│   │           │       │   ├── test_sysinfo.py
│   │           │       │   ├── test_tempdir.py
│   │           │       │   ├── test_text.py
│   │           │       │   ├── test_tokenutil.py
│   │           │       │   └── test_wildcard.py
│   │           │       ├── text.py
│   │           │       ├── timing.py
│   │           │       ├── tokenutil.py
│   │           │       ├── traitlets.py
│   │           │       ├── tz.py
│   │           │       ├── ulinecache.py
│   │           │       ├── version.py
│   │           │       └── wildcard.py
│   │           ├── ipython-7.5.0.dist-info
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── ipython_genutils
│   │           │   ├── encoding.py
│   │           │   ├── importstring.py
│   │           │   ├── __init__.py
│   │           │   ├── ipstruct.py
│   │           │   ├── path.py
│   │           │   ├── py3compat.py
│   │           │   ├── __pycache__
│   │           │   │   ├── encoding.cpython-36.pyc
│   │           │   │   ├── importstring.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── ipstruct.cpython-36.pyc
│   │           │   │   ├── path.cpython-36.pyc
│   │           │   │   ├── py3compat.cpython-36.pyc
│   │           │   │   ├── tempdir.cpython-36.pyc
│   │           │   │   ├── text.cpython-36.pyc
│   │           │   │   └── _version.cpython-36.pyc
│   │           │   ├── tempdir.py
│   │           │   ├── testing
│   │           │   │   ├── decorators.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── decorators.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── tests
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── test_importstring.cpython-36.pyc
│   │           │   │   │   ├── test_path.cpython-36.pyc
│   │           │   │   │   ├── test_tempdir.cpython-36.pyc
│   │           │   │   │   └── test_text.cpython-36.pyc
│   │           │   │   ├── test_importstring.py
│   │           │   │   ├── test_path.py
│   │           │   │   ├── test_tempdir.py
│   │           │   │   └── test_text.py
│   │           │   ├── text.py
│   │           │   └── _version.py
│   │           ├── ipython_genutils-0.2.0.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── ipywidgets
│   │           │   ├── embed.py
│   │           │   ├── __init__.py
│   │           │   ├── __pycache__
│   │           │   │   ├── embed.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   └── _version.cpython-36.pyc
│   │           │   ├── state.schema.json
│   │           │   ├── tests
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── test_embed.cpython-36.pyc
│   │           │   │   └── test_embed.py
│   │           │   ├── _version.py
│   │           │   ├── view.schema.json
│   │           │   └── widgets
│   │           │       ├── docutils.py
│   │           │       ├── domwidget.py
│   │           │       ├── __init__.py
│   │           │       ├── interaction.py
│   │           │       ├── __pycache__
│   │           │       │   ├── docutils.cpython-36.pyc
│   │           │       │   ├── domwidget.cpython-36.pyc
│   │           │       │   ├── __init__.cpython-36.pyc
│   │           │       │   ├── interaction.cpython-36.pyc
│   │           │       │   ├── trait_types.cpython-36.pyc
│   │           │       │   ├── valuewidget.cpython-36.pyc
│   │           │       │   ├── widget_bool.cpython-36.pyc
│   │           │       │   ├── widget_box.cpython-36.pyc
│   │           │       │   ├── widget_button.cpython-36.pyc
│   │           │       │   ├── widget_color.cpython-36.pyc
│   │           │       │   ├── widget_controller.cpython-36.pyc
│   │           │       │   ├── widget_core.cpython-36.pyc
│   │           │       │   ├── widget.cpython-36.pyc
│   │           │       │   ├── widget_date.cpython-36.pyc
│   │           │       │   ├── widget_description.cpython-36.pyc
│   │           │       │   ├── widget_float.cpython-36.pyc
│   │           │       │   ├── widget_int.cpython-36.pyc
│   │           │       │   ├── widget_layout.cpython-36.pyc
│   │           │       │   ├── widget_link.cpython-36.pyc
│   │           │       │   ├── widget_media.cpython-36.pyc
│   │           │       │   ├── widget_output.cpython-36.pyc
│   │           │       │   ├── widget_selectioncontainer.cpython-36.pyc
│   │           │       │   ├── widget_selection.cpython-36.pyc
│   │           │       │   ├── widget_string.cpython-36.pyc
│   │           │       │   └── widget_style.cpython-36.pyc
│   │           │       ├── tests
│   │           │       │   ├── data
│   │           │       │   │   └── jupyter-logo-transparent.png
│   │           │       │   ├── __init__.py
│   │           │       │   ├── __pycache__
│   │           │       │   │   ├── __init__.cpython-36.pyc
│   │           │       │   │   ├── test_docutils.cpython-36.pyc
│   │           │       │   │   ├── test_interaction.cpython-36.pyc
│   │           │       │   │   ├── test_link.cpython-36.pyc
│   │           │       │   │   ├── test_selectioncontainer.cpython-36.pyc
│   │           │       │   │   ├── test_send_state.cpython-36.pyc
│   │           │       │   │   ├── test_set_state.cpython-36.pyc
│   │           │       │   │   ├── test_traits.cpython-36.pyc
│   │           │       │   │   ├── test_widget_box.cpython-36.pyc
│   │           │       │   │   ├── test_widget.cpython-36.pyc
│   │           │       │   │   ├── test_widget_float.cpython-36.pyc
│   │           │       │   │   ├── test_widget_image.cpython-36.pyc
│   │           │       │   │   ├── test_widget_output.cpython-36.pyc
│   │           │       │   │   ├── test_widget_selection.cpython-36.pyc
│   │           │       │   │   └── utils.cpython-36.pyc
│   │           │       │   ├── test_docutils.py
│   │           │       │   ├── test_interaction.py
│   │           │       │   ├── test_link.py
│   │           │       │   ├── test_selectioncontainer.py
│   │           │       │   ├── test_send_state.py
│   │           │       │   ├── test_set_state.py
│   │           │       │   ├── test_traits.py
│   │           │       │   ├── test_widget_box.py
│   │           │       │   ├── test_widget_float.py
│   │           │       │   ├── test_widget_image.py
│   │           │       │   ├── test_widget_output.py
│   │           │       │   ├── test_widget.py
│   │           │       │   ├── test_widget_selection.py
│   │           │       │   └── utils.py
│   │           │       ├── trait_types.py
│   │           │       ├── valuewidget.py
│   │           │       ├── widget_bool.py
│   │           │       ├── widget_box.py
│   │           │       ├── widget_button.py
│   │           │       ├── widget_color.py
│   │           │       ├── widget_controller.py
│   │           │       ├── widget_core.py
│   │           │       ├── widget_date.py
│   │           │       ├── widget_description.py
│   │           │       ├── widget_float.py
│   │           │       ├── widget_int.py
│   │           │       ├── widget_layout.py
│   │           │       ├── widget_link.py
│   │           │       ├── widget_media.py
│   │           │       ├── widget_output.py
│   │           │       ├── widget.py
│   │           │       ├── widget_selectioncontainer.py
│   │           │       ├── widget_selection.py
│   │           │       ├── widget_string.py
│   │           │       └── widget_style.py
│   │           ├── ipywidgets-7.4.2.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── isympy.py
│   │           ├── jedi
│   │           │   ├── api
│   │           │   │   ├── classes.py
│   │           │   │   ├── completion.py
│   │           │   │   ├── environment.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── helpers.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── interpreter.py
│   │           │   │   ├── keywords.py
│   │           │   │   ├── project.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── classes.cpython-36.pyc
│   │           │   │   │   ├── completion.cpython-36.pyc
│   │           │   │   │   ├── environment.cpython-36.pyc
│   │           │   │   │   ├── exceptions.cpython-36.pyc
│   │           │   │   │   ├── helpers.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── interpreter.cpython-36.pyc
│   │           │   │   │   ├── keywords.cpython-36.pyc
│   │           │   │   │   ├── project.cpython-36.pyc
│   │           │   │   │   └── replstartup.cpython-36.pyc
│   │           │   │   └── replstartup.py
│   │           │   ├── cache.py
│   │           │   ├── common
│   │           │   │   ├── context.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── context.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── utils.cpython-36.pyc
│   │           │   │   └── utils.py
│   │           │   ├── _compatibility.py
│   │           │   ├── debug.py
│   │           │   ├── evaluate
│   │           │   │   ├── analysis.py
│   │           │   │   ├── arguments.py
│   │           │   │   ├── base_context.py
│   │           │   │   ├── cache.py
│   │           │   │   ├── compiled
│   │           │   │   │   ├── access.py
│   │           │   │   │   ├── context.py
│   │           │   │   │   ├── fake
│   │           │   │   │   │   ├── builtins.pym
│   │           │   │   │   │   ├── datetime.pym
│   │           │   │   │   │   ├── _functools.pym
│   │           │   │   │   │   ├── io.pym
│   │           │   │   │   │   ├── operator.pym
│   │           │   │   │   │   ├── posix.pym
│   │           │   │   │   │   ├── _sqlite3.pym
│   │           │   │   │   │   ├── _sre.pym
│   │           │   │   │   │   └── _weakref.pym
│   │           │   │   │   ├── fake.py
│   │           │   │   │   ├── getattr_static.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── mixed.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── access.cpython-36.pyc
│   │           │   │   │   │   ├── context.cpython-36.pyc
│   │           │   │   │   │   ├── fake.cpython-36.pyc
│   │           │   │   │   │   ├── getattr_static.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── mixed.cpython-36.pyc
│   │           │   │   │   └── subprocess
│   │           │   │   │       ├── functions.py
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __main__.py
│   │           │   │   │       └── __pycache__
│   │           │   │   │           ├── functions.cpython-36.pyc
│   │           │   │   │           ├── __init__.cpython-36.pyc
│   │           │   │   │           └── __main__.cpython-36.pyc
│   │           │   │   ├── context
│   │           │   │   │   ├── asynchronous.py
│   │           │   │   │   ├── function.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── instance.py
│   │           │   │   │   ├── iterable.py
│   │           │   │   │   ├── klass.py
│   │           │   │   │   ├── module.py
│   │           │   │   │   ├── namespace.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── asynchronous.cpython-36.pyc
│   │           │   │   │       ├── function.cpython-36.pyc
│   │           │   │   │       ├── __init__.cpython-36.pyc
│   │           │   │   │       ├── instance.cpython-36.pyc
│   │           │   │   │       ├── iterable.cpython-36.pyc
│   │           │   │   │       ├── klass.cpython-36.pyc
│   │           │   │   │       ├── module.cpython-36.pyc
│   │           │   │   │       └── namespace.cpython-36.pyc
│   │           │   │   ├── docstrings.py
│   │           │   │   ├── dynamic.py
│   │           │   │   ├── filters.py
│   │           │   │   ├── finder.py
│   │           │   │   ├── flow_analysis.py
│   │           │   │   ├── helpers.py
│   │           │   │   ├── imports.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── jedi_typing.py
│   │           │   │   ├── lazy_context.py
│   │           │   │   ├── param.py
│   │           │   │   ├── parser_cache.py
│   │           │   │   ├── pep0484.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── analysis.cpython-36.pyc
│   │           │   │   │   ├── arguments.cpython-36.pyc
│   │           │   │   │   ├── base_context.cpython-36.pyc
│   │           │   │   │   ├── cache.cpython-36.pyc
│   │           │   │   │   ├── docstrings.cpython-36.pyc
│   │           │   │   │   ├── dynamic.cpython-36.pyc
│   │           │   │   │   ├── filters.cpython-36.pyc
│   │           │   │   │   ├── finder.cpython-36.pyc
│   │           │   │   │   ├── flow_analysis.cpython-36.pyc
│   │           │   │   │   ├── helpers.cpython-36.pyc
│   │           │   │   │   ├── imports.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── jedi_typing.cpython-36.pyc
│   │           │   │   │   ├── lazy_context.cpython-36.pyc
│   │           │   │   │   ├── param.cpython-36.pyc
│   │           │   │   │   ├── parser_cache.cpython-36.pyc
│   │           │   │   │   ├── pep0484.cpython-36.pyc
│   │           │   │   │   ├── recursion.cpython-36.pyc
│   │           │   │   │   ├── stdlib.cpython-36.pyc
│   │           │   │   │   ├── syntax_tree.cpython-36.pyc
│   │           │   │   │   ├── sys_path.cpython-36.pyc
│   │           │   │   │   ├── usages.cpython-36.pyc
│   │           │   │   │   └── utils.cpython-36.pyc
│   │           │   │   ├── recursion.py
│   │           │   │   ├── stdlib.py
│   │           │   │   ├── syntax_tree.py
│   │           │   │   ├── sys_path.py
│   │           │   │   ├── usages.py
│   │           │   │   └── utils.py
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── parser_utils.py
│   │           │   ├── __pycache__
│   │           │   │   ├── cache.cpython-36.pyc
│   │           │   │   ├── _compatibility.cpython-36.pyc
│   │           │   │   ├── debug.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── __main__.cpython-36.pyc
│   │           │   │   ├── parser_utils.cpython-36.pyc
│   │           │   │   ├── refactoring.cpython-36.pyc
│   │           │   │   ├── settings.cpython-36.pyc
│   │           │   │   └── utils.cpython-36.pyc
│   │           │   ├── refactoring.py
│   │           │   ├── settings.py
│   │           │   └── utils.py
│   │           ├── jedi-0.13.3.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── jinja2
│   │           │   ├── asyncfilters.py
│   │           │   ├── asyncsupport.py
│   │           │   ├── bccache.py
│   │           │   ├── _compat.py
│   │           │   ├── compiler.py
│   │           │   ├── constants.py
│   │           │   ├── debug.py
│   │           │   ├── defaults.py
│   │           │   ├── environment.py
│   │           │   ├── exceptions.py
│   │           │   ├── ext.py
│   │           │   ├── filters.py
│   │           │   ├── _identifier.py
│   │           │   ├── idtracking.py
│   │           │   ├── __init__.py
│   │           │   ├── lexer.py
│   │           │   ├── loaders.py
│   │           │   ├── meta.py
│   │           │   ├── nativetypes.py
│   │           │   ├── optimizer.py
│   │           │   ├── parser.py
│   │           │   ├── __pycache__
│   │           │   │   ├── asyncfilters.cpython-36.pyc
│   │           │   │   ├── asyncsupport.cpython-36.pyc
│   │           │   │   ├── bccache.cpython-36.pyc
│   │           │   │   ├── _compat.cpython-36.pyc
│   │           │   │   ├── compiler.cpython-36.pyc
│   │           │   │   ├── constants.cpython-36.pyc
│   │           │   │   ├── debug.cpython-36.pyc
│   │           │   │   ├── defaults.cpython-36.pyc
│   │           │   │   ├── environment.cpython-36.pyc
│   │           │   │   ├── exceptions.cpython-36.pyc
│   │           │   │   ├── ext.cpython-36.pyc
│   │           │   │   ├── filters.cpython-36.pyc
│   │           │   │   ├── _identifier.cpython-36.pyc
│   │           │   │   ├── idtracking.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── lexer.cpython-36.pyc
│   │           │   │   ├── loaders.cpython-36.pyc
│   │           │   │   ├── meta.cpython-36.pyc
│   │           │   │   ├── nativetypes.cpython-36.pyc
│   │           │   │   ├── optimizer.cpython-36.pyc
│   │           │   │   ├── parser.cpython-36.pyc
│   │           │   │   ├── runtime.cpython-36.pyc
│   │           │   │   ├── sandbox.cpython-36.pyc
│   │           │   │   ├── tests.cpython-36.pyc
│   │           │   │   ├── utils.cpython-36.pyc
│   │           │   │   └── visitor.cpython-36.pyc
│   │           │   ├── runtime.py
│   │           │   ├── sandbox.py
│   │           │   ├── tests.py
│   │           │   ├── utils.py
│   │           │   └── visitor.py
│   │           ├── Jinja2-2.10.1.dist-info
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── jsonschema
│   │           │   ├── benchmarks
│   │           │   │   ├── __init__.py
│   │           │   │   ├── issue232.py
│   │           │   │   ├── json_schema_test_suite.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       ├── issue232.cpython-36.pyc
│   │           │   │       └── json_schema_test_suite.cpython-36.pyc
│   │           │   ├── cli.py
│   │           │   ├── compat.py
│   │           │   ├── exceptions.py
│   │           │   ├── _format.py
│   │           │   ├── __init__.py
│   │           │   ├── _legacy_validators.py
│   │           │   ├── __main__.py
│   │           │   ├── __pycache__
│   │           │   │   ├── cli.cpython-36.pyc
│   │           │   │   ├── compat.cpython-36.pyc
│   │           │   │   ├── exceptions.cpython-36.pyc
│   │           │   │   ├── _format.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── _legacy_validators.cpython-36.pyc
│   │           │   │   ├── __main__.cpython-36.pyc
│   │           │   │   ├── _reflect.cpython-36.pyc
│   │           │   │   ├── _types.cpython-36.pyc
│   │           │   │   ├── _utils.cpython-36.pyc
│   │           │   │   ├── _validators.cpython-36.pyc
│   │           │   │   └── validators.cpython-36.pyc
│   │           │   ├── _reflect.py
│   │           │   ├── schemas
│   │           │   │   ├── draft3.json
│   │           │   │   ├── draft4.json
│   │           │   │   ├── draft6.json
│   │           │   │   └── draft7.json
│   │           │   ├── tests
│   │           │   │   ├── compat.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── compat.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── _suite.cpython-36.pyc
│   │           │   │   │   ├── test_cli.cpython-36.pyc
│   │           │   │   │   ├── test_exceptions.cpython-36.pyc
│   │           │   │   │   ├── test_format.cpython-36.pyc
│   │           │   │   │   ├── test_jsonschema_test_suite.cpython-36.pyc
│   │           │   │   │   ├── test_types.cpython-36.pyc
│   │           │   │   │   └── test_validators.cpython-36.pyc
│   │           │   │   ├── _suite.py
│   │           │   │   ├── test_cli.py
│   │           │   │   ├── test_exceptions.py
│   │           │   │   ├── test_format.py
│   │           │   │   ├── test_jsonschema_test_suite.py
│   │           │   │   ├── test_types.py
│   │           │   │   └── test_validators.py
│   │           │   ├── _types.py
│   │           │   ├── _utils.py
│   │           │   ├── _validators.py
│   │           │   └── validators.py
│   │           ├── jsonschema-3.0.1.dist-info
│   │           │   ├── COPYING
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── jupyter-1.0.0.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── pbr.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── jupyter_client
│   │           │   ├── adapter.py
│   │           │   ├── blocking
│   │           │   │   ├── channels.py
│   │           │   │   ├── client.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── channels.cpython-36.pyc
│   │           │   │       ├── client.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── channelsabc.py
│   │           │   ├── channels.py
│   │           │   ├── clientabc.py
│   │           │   ├── client.py
│   │           │   ├── connect.py
│   │           │   ├── consoleapp.py
│   │           │   ├── __init__.py
│   │           │   ├── ioloop
│   │           │   │   ├── __init__.py
│   │           │   │   ├── manager.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── manager.cpython-36.pyc
│   │           │   │   │   └── restarter.cpython-36.pyc
│   │           │   │   └── restarter.py
│   │           │   ├── jsonutil.py
│   │           │   ├── kernelapp.py
│   │           │   ├── kernelspecapp.py
│   │           │   ├── kernelspec.py
│   │           │   ├── launcher.py
│   │           │   ├── localinterfaces.py
│   │           │   ├── managerabc.py
│   │           │   ├── manager.py
│   │           │   ├── multikernelmanager.py
│   │           │   ├── __pycache__
│   │           │   │   ├── adapter.cpython-36.pyc
│   │           │   │   ├── channelsabc.cpython-36.pyc
│   │           │   │   ├── channels.cpython-36.pyc
│   │           │   │   ├── clientabc.cpython-36.pyc
│   │           │   │   ├── client.cpython-36.pyc
│   │           │   │   ├── connect.cpython-36.pyc
│   │           │   │   ├── consoleapp.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── jsonutil.cpython-36.pyc
│   │           │   │   ├── kernelapp.cpython-36.pyc
│   │           │   │   ├── kernelspecapp.cpython-36.pyc
│   │           │   │   ├── kernelspec.cpython-36.pyc
│   │           │   │   ├── launcher.cpython-36.pyc
│   │           │   │   ├── localinterfaces.cpython-36.pyc
│   │           │   │   ├── managerabc.cpython-36.pyc
│   │           │   │   ├── manager.cpython-36.pyc
│   │           │   │   ├── multikernelmanager.cpython-36.pyc
│   │           │   │   ├── restarter.cpython-36.pyc
│   │           │   │   ├── runapp.cpython-36.pyc
│   │           │   │   ├── session.cpython-36.pyc
│   │           │   │   ├── threaded.cpython-36.pyc
│   │           │   │   ├── _version.cpython-36.pyc
│   │           │   │   └── win_interrupt.cpython-36.pyc
│   │           │   ├── restarter.py
│   │           │   ├── runapp.py
│   │           │   ├── session.py
│   │           │   ├── tests
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── signalkernel.cpython-36.pyc
│   │           │   │   │   ├── test_adapter.cpython-36.pyc
│   │           │   │   │   ├── test_client.cpython-36.pyc
│   │           │   │   │   ├── test_connect.cpython-36.pyc
│   │           │   │   │   ├── test_jsonutil.cpython-36.pyc
│   │           │   │   │   ├── test_kernelapp.cpython-36.pyc
│   │           │   │   │   ├── test_kernelmanager.cpython-36.pyc
│   │           │   │   │   ├── test_kernelspec.cpython-36.pyc
│   │           │   │   │   ├── test_localinterfaces.cpython-36.pyc
│   │           │   │   │   ├── test_multikernelmanager.cpython-36.pyc
│   │           │   │   │   ├── test_public_api.cpython-36.pyc
│   │           │   │   │   ├── test_session.cpython-36.pyc
│   │           │   │   │   └── utils.cpython-36.pyc
│   │           │   │   ├── signalkernel.py
│   │           │   │   ├── test_adapter.py
│   │           │   │   ├── test_client.py
│   │           │   │   ├── test_connect.py
│   │           │   │   ├── test_jsonutil.py
│   │           │   │   ├── test_kernelapp.py
│   │           │   │   ├── test_kernelmanager.py
│   │           │   │   ├── test_kernelspec.py
│   │           │   │   ├── test_localinterfaces.py
│   │           │   │   ├── test_multikernelmanager.py
│   │           │   │   ├── test_public_api.py
│   │           │   │   ├── test_session.py
│   │           │   │   └── utils.py
│   │           │   ├── threaded.py
│   │           │   ├── _version.py
│   │           │   └── win_interrupt.py
│   │           ├── jupyter_client-5.2.4.dist-info
│   │           │   ├── COPYING.md
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── jupyter_console
│   │           │   ├── app.py
│   │           │   ├── completer.py
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── ptshell.py
│   │           │   ├── __pycache__
│   │           │   │   ├── app.cpython-36.pyc
│   │           │   │   ├── completer.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── __main__.cpython-36.pyc
│   │           │   │   ├── ptshell.cpython-36.pyc
│   │           │   │   ├── _version.cpython-36.pyc
│   │           │   │   └── zmqhistory.cpython-36.pyc
│   │           │   ├── tests
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── test_console.cpython-36.pyc
│   │           │   │   │   ├── test_image_handler.cpython-36.pyc
│   │           │   │   │   └── writetofile.cpython-36.pyc
│   │           │   │   ├── test_console.py
│   │           │   │   ├── test_image_handler.py
│   │           │   │   └── writetofile.py
│   │           │   ├── _version.py
│   │           │   └── zmqhistory.py
│   │           ├── jupyter_console-6.0.0.dist-info
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── jupyter_core
│   │           │   ├── application.py
│   │           │   ├── command.py
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── migrate.py
│   │           │   ├── paths.py
│   │           │   ├── __pycache__
│   │           │   │   ├── application.cpython-36.pyc
│   │           │   │   ├── command.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── __main__.cpython-36.pyc
│   │           │   │   ├── migrate.cpython-36.pyc
│   │           │   │   ├── paths.cpython-36.pyc
│   │           │   │   ├── troubleshoot.cpython-36.pyc
│   │           │   │   └── version.cpython-36.pyc
│   │           │   ├── tests
│   │           │   │   ├── dotipython
│   │           │   │   │   ├── nbextensions
│   │           │   │   │   │   └── myext.js
│   │           │   │   │   └── profile_default
│   │           │   │   │       ├── ipython_config.py
│   │           │   │   │       ├── ipython_console_config.py
│   │           │   │   │       ├── ipython_kernel_config.py
│   │           │   │   │       ├── ipython_nbconvert_config.py
│   │           │   │   │       ├── ipython_notebook_config.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── ipython_config.cpython-34.pyc
│   │           │   │   │       │   ├── ipython_config.cpython-35.pyc
│   │           │   │   │       │   ├── ipython_config.cpython-36.pyc
│   │           │   │   │       │   ├── ipython_console_config.cpython-34.pyc
│   │           │   │   │       │   ├── ipython_console_config.cpython-35.pyc
│   │           │   │   │       │   ├── ipython_console_config.cpython-36.pyc
│   │           │   │   │       │   ├── ipython_kernel_config.cpython-34.pyc
│   │           │   │   │       │   ├── ipython_kernel_config.cpython-35.pyc
│   │           │   │   │       │   ├── ipython_kernel_config.cpython-36.pyc
│   │           │   │   │       │   ├── ipython_nbconvert_config.cpython-34.pyc
│   │           │   │   │       │   ├── ipython_nbconvert_config.cpython-35.pyc
│   │           │   │   │       │   ├── ipython_nbconvert_config.cpython-36.pyc
│   │           │   │   │       │   ├── ipython_notebook_config.cpython-34.pyc
│   │           │   │   │       │   ├── ipython_notebook_config.cpython-35.pyc
│   │           │   │   │       │   └── ipython_notebook_config.cpython-36.pyc
│   │           │   │   │       └── static
│   │           │   │   │           └── custom
│   │           │   │   │               ├── custom.css
│   │           │   │   │               └── custom.js
│   │           │   │   ├── dotipython_empty
│   │           │   │   │   └── profile_default
│   │           │   │   │       ├── ipython_config.py
│   │           │   │   │       ├── ipython_console_config.py
│   │           │   │   │       ├── ipython_kernel_config.py
│   │           │   │   │       ├── ipython_nbconvert_config.py
│   │           │   │   │       ├── ipython_notebook_config.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── ipython_config.cpython-34.pyc
│   │           │   │   │       │   ├── ipython_config.cpython-35.pyc
│   │           │   │   │       │   ├── ipython_config.cpython-36.pyc
│   │           │   │   │       │   ├── ipython_console_config.cpython-34.pyc
│   │           │   │   │       │   ├── ipython_console_config.cpython-35.pyc
│   │           │   │   │       │   ├── ipython_console_config.cpython-36.pyc
│   │           │   │   │       │   ├── ipython_kernel_config.cpython-34.pyc
│   │           │   │   │       │   ├── ipython_kernel_config.cpython-35.pyc
│   │           │   │   │       │   ├── ipython_kernel_config.cpython-36.pyc
│   │           │   │   │       │   ├── ipython_nbconvert_config.cpython-34.pyc
│   │           │   │   │       │   ├── ipython_nbconvert_config.cpython-35.pyc
│   │           │   │   │       │   ├── ipython_nbconvert_config.cpython-36.pyc
│   │           │   │   │       │   ├── ipython_notebook_config.cpython-34.pyc
│   │           │   │   │       │   ├── ipython_notebook_config.cpython-35.pyc
│   │           │   │   │       │   └── ipython_notebook_config.cpython-36.pyc
│   │           │   │   │       └── static
│   │           │   │   │           └── custom
│   │           │   │   │               ├── custom.css
│   │           │   │   │               └── custom.js
│   │           │   │   ├── __init__.py
│   │           │   │   ├── mocking.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-34.pyc
│   │           │   │   │   ├── __init__.cpython-35.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── mocking.cpython-34.pyc
│   │           │   │   │   ├── mocking.cpython-35.pyc
│   │           │   │   │   ├── mocking.cpython-36.pyc
│   │           │   │   │   ├── test_application.cpython-34.pyc
│   │           │   │   │   ├── test_application.cpython-35.pyc
│   │           │   │   │   ├── test_application.cpython-35-PYTEST.pyc
│   │           │   │   │   ├── test_application.cpython-36.pyc
│   │           │   │   │   ├── test_command.cpython-34.pyc
│   │           │   │   │   ├── test_command.cpython-35.pyc
│   │           │   │   │   ├── test_command.cpython-35-PYTEST.pyc
│   │           │   │   │   ├── test_command.cpython-36.pyc
│   │           │   │   │   ├── test_migrate.cpython-34.pyc
│   │           │   │   │   ├── test_migrate.cpython-35.pyc
│   │           │   │   │   ├── test_migrate.cpython-35-PYTEST.pyc
│   │           │   │   │   ├── test_migrate.cpython-36.pyc
│   │           │   │   │   ├── test_paths.cpython-34.pyc
│   │           │   │   │   ├── test_paths.cpython-35.pyc
│   │           │   │   │   ├── test_paths.cpython-35-PYTEST.pyc
│   │           │   │   │   └── test_paths.cpython-36.pyc
│   │           │   │   ├── test_application.py
│   │           │   │   ├── test_command.py
│   │           │   │   ├── test_migrate.py
│   │           │   │   └── test_paths.py
│   │           │   ├── troubleshoot.py
│   │           │   ├── utils
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── shutil_which.cpython-36.pyc
│   │           │   │   └── shutil_which.py
│   │           │   └── version.py
│   │           ├── jupyter_core-4.4.0.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── jupyter.py
│   │           ├── kiwisolver-1.1.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── kiwisolver.cpython-36m-x86_64-linux-gnu.so
│   │           ├── markupsafe
│   │           │   ├── _compat.py
│   │           │   ├── _constants.py
│   │           │   ├── __init__.py
│   │           │   ├── _native.py
│   │           │   ├── __pycache__
│   │           │   │   ├── _compat.cpython-36.pyc
│   │           │   │   ├── _constants.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   └── _native.cpython-36.pyc
│   │           │   ├── _speedups.c
│   │           │   └── _speedups.cpython-36m-x86_64-linux-gnu.so
│   │           ├── MarkupSafe-1.1.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── matplotlib
│   │           │   ├── afm.py
│   │           │   ├── _animation_data.py
│   │           │   ├── animation.py
│   │           │   ├── artist.py
│   │           │   ├── axes
│   │           │   │   ├── _axes.py
│   │           │   │   ├── _base.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _axes.cpython-36.pyc
│   │           │   │   │   ├── _base.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── _subplots.cpython-36.pyc
│   │           │   │   └── _subplots.py
│   │           │   ├── axis.py
│   │           │   ├── backend_bases.py
│   │           │   ├── backend_managers.py
│   │           │   ├── backends
│   │           │   │   ├── _backend_agg.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── backend_agg.py
│   │           │   │   ├── backend_cairo.py
│   │           │   │   ├── backend_gtk3agg.py
│   │           │   │   ├── backend_gtk3cairo.py
│   │           │   │   ├── backend_gtk3.py
│   │           │   │   ├── backend_macosx.py
│   │           │   │   ├── backend_mixed.py
│   │           │   │   ├── backend_nbagg.py
│   │           │   │   ├── backend_pdf.py
│   │           │   │   ├── backend_pgf.py
│   │           │   │   ├── backend_ps.py
│   │           │   │   ├── backend_qt4agg.py
│   │           │   │   ├── backend_qt4cairo.py
│   │           │   │   ├── backend_qt4.py
│   │           │   │   ├── backend_qt5agg.py
│   │           │   │   ├── backend_qt5cairo.py
│   │           │   │   ├── backend_qt5.py
│   │           │   │   ├── backend_svg.py
│   │           │   │   ├── backend_template.py
│   │           │   │   ├── backend_tkagg.py
│   │           │   │   ├── backend_tkcairo.py
│   │           │   │   ├── _backend_tk.py
│   │           │   │   ├── backend_webagg_core.py
│   │           │   │   ├── backend_webagg.py
│   │           │   │   ├── backend_wxagg.py
│   │           │   │   ├── backend_wxcairo.py
│   │           │   │   ├── backend_wx.py
│   │           │   │   ├── _gtk3_compat.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── backend_agg.cpython-36.pyc
│   │           │   │   │   ├── backend_cairo.cpython-36.pyc
│   │           │   │   │   ├── backend_gtk3agg.cpython-36.pyc
│   │           │   │   │   ├── backend_gtk3cairo.cpython-36.pyc
│   │           │   │   │   ├── backend_gtk3.cpython-36.pyc
│   │           │   │   │   ├── backend_macosx.cpython-36.pyc
│   │           │   │   │   ├── backend_mixed.cpython-36.pyc
│   │           │   │   │   ├── backend_nbagg.cpython-36.pyc
│   │           │   │   │   ├── backend_pdf.cpython-36.pyc
│   │           │   │   │   ├── backend_pgf.cpython-36.pyc
│   │           │   │   │   ├── backend_ps.cpython-36.pyc
│   │           │   │   │   ├── backend_qt4agg.cpython-36.pyc
│   │           │   │   │   ├── backend_qt4cairo.cpython-36.pyc
│   │           │   │   │   ├── backend_qt4.cpython-36.pyc
│   │           │   │   │   ├── backend_qt5agg.cpython-36.pyc
│   │           │   │   │   ├── backend_qt5cairo.cpython-36.pyc
│   │           │   │   │   ├── backend_qt5.cpython-36.pyc
│   │           │   │   │   ├── backend_svg.cpython-36.pyc
│   │           │   │   │   ├── backend_template.cpython-36.pyc
│   │           │   │   │   ├── backend_tkagg.cpython-36.pyc
│   │           │   │   │   ├── backend_tkcairo.cpython-36.pyc
│   │           │   │   │   ├── _backend_tk.cpython-36.pyc
│   │           │   │   │   ├── backend_webagg_core.cpython-36.pyc
│   │           │   │   │   ├── backend_webagg.cpython-36.pyc
│   │           │   │   │   ├── backend_wxagg.cpython-36.pyc
│   │           │   │   │   ├── backend_wxcairo.cpython-36.pyc
│   │           │   │   │   ├── backend_wx.cpython-36.pyc
│   │           │   │   │   ├── _gtk3_compat.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── qt_compat.cpython-36.pyc
│   │           │   │   │   ├── tkagg.cpython-36.pyc
│   │           │   │   │   ├── windowing.cpython-36.pyc
│   │           │   │   │   └── wx_compat.cpython-36.pyc
│   │           │   │   ├── qt_compat.py
│   │           │   │   ├── qt_editor
│   │           │   │   │   ├── figureoptions.py
│   │           │   │   │   ├── formlayout.py
│   │           │   │   │   ├── formsubplottool.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── figureoptions.cpython-36.pyc
│   │           │   │   │       ├── formlayout.cpython-36.pyc
│   │           │   │   │       ├── formsubplottool.cpython-36.pyc
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   ├── _tkagg.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── tkagg.py
│   │           │   │   ├── web_backend
│   │           │   │   │   ├── all_figures.html
│   │           │   │   │   ├── css
│   │           │   │   │   │   ├── boilerplate.css
│   │           │   │   │   │   ├── fbm.css
│   │           │   │   │   │   └── page.css
│   │           │   │   │   ├── ipython_inline_figure.html
│   │           │   │   │   ├── jquery
│   │           │   │   │   │   └── js
│   │           │   │   │   │       ├── jquery-1.11.3.js
│   │           │   │   │   │       └── jquery-1.11.3.min.js
│   │           │   │   │   ├── jquery-ui-1.12.1
│   │           │   │   │   │   ├── AUTHORS.txt
│   │           │   │   │   │   ├── external
│   │           │   │   │   │   │   └── jquery
│   │           │   │   │   │   │       └── jquery.js
│   │           │   │   │   │   ├── images
│   │           │   │   │   │   │   ├── ui-icons_444444_256x240.png
│   │           │   │   │   │   │   ├── ui-icons_555555_256x240.png
│   │           │   │   │   │   │   ├── ui-icons_777620_256x240.png
│   │           │   │   │   │   │   ├── ui-icons_777777_256x240.png
│   │           │   │   │   │   │   ├── ui-icons_cc0000_256x240.png
│   │           │   │   │   │   │   └── ui-icons_ffffff_256x240.png
│   │           │   │   │   │   ├── index.html
│   │           │   │   │   │   ├── jquery-ui.css
│   │           │   │   │   │   ├── jquery-ui.js
│   │           │   │   │   │   ├── jquery-ui.min.css
│   │           │   │   │   │   ├── jquery-ui.min.js
│   │           │   │   │   │   ├── jquery-ui.structure.css
│   │           │   │   │   │   ├── jquery-ui.structure.min.css
│   │           │   │   │   │   ├── jquery-ui.theme.css
│   │           │   │   │   │   ├── jquery-ui.theme.min.css
│   │           │   │   │   │   ├── LICENSE.txt
│   │           │   │   │   │   └── package.json
│   │           │   │   │   ├── js
│   │           │   │   │   │   ├── mpl.js
│   │           │   │   │   │   ├── mpl_tornado.js
│   │           │   │   │   │   └── nbagg_mpl.js
│   │           │   │   │   ├── nbagg_uat.ipynb
│   │           │   │   │   └── single_figure.html
│   │           │   │   ├── windowing.py
│   │           │   │   └── wx_compat.py
│   │           │   ├── backend_tools.py
│   │           │   ├── bezier.py
│   │           │   ├── blocking_input.py
│   │           │   ├── category.py
│   │           │   ├── cbook
│   │           │   │   ├── deprecation.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── deprecation.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── _cm_listed.py
│   │           │   ├── _cm.py
│   │           │   ├── cm.py
│   │           │   ├── collections.py
│   │           │   ├── colorbar.py
│   │           │   ├── _color_data.py
│   │           │   ├── colors.py
│   │           │   ├── compat
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── subprocess.cpython-36.pyc
│   │           │   │   └── subprocess.py
│   │           │   ├── _constrained_layout.py
│   │           │   ├── container.py
│   │           │   ├── _contour.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── contour.py
│   │           │   ├── dates.py
│   │           │   ├── docstring.py
│   │           │   ├── dviread.py
│   │           │   ├── figure.py
│   │           │   ├── fontconfig_pattern.py
│   │           │   ├── font_manager.py
│   │           │   ├── ft2font.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── gridspec.py
│   │           │   ├── hatch.py
│   │           │   ├── _image.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── image.py
│   │           │   ├── __init__.py
│   │           │   ├── _layoutbox.py
│   │           │   ├── legend_handler.py
│   │           │   ├── legend.py
│   │           │   ├── .libs
│   │           │   │   ├── libpng16-cfdb1654.so.16.21.0
│   │           │   │   └── libz-a147dcb0.so.1.2.3
│   │           │   ├── lines.py
│   │           │   ├── markers.py
│   │           │   ├── _mathtext_data.py
│   │           │   ├── mathtext.py
│   │           │   ├── mlab.py
│   │           │   ├── mpl-data
│   │           │   │   ├── fonts
│   │           │   │   │   ├── afm
│   │           │   │   │   │   ├── cmex10.afm
│   │           │   │   │   │   ├── cmmi10.afm
│   │           │   │   │   │   ├── cmr10.afm
│   │           │   │   │   │   ├── cmsy10.afm
│   │           │   │   │   │   ├── cmtt10.afm
│   │           │   │   │   │   ├── pagd8a.afm
│   │           │   │   │   │   ├── pagdo8a.afm
│   │           │   │   │   │   ├── pagk8a.afm
│   │           │   │   │   │   ├── pagko8a.afm
│   │           │   │   │   │   ├── pbkd8a.afm
│   │           │   │   │   │   ├── pbkdi8a.afm
│   │           │   │   │   │   ├── pbkl8a.afm
│   │           │   │   │   │   ├── pbkli8a.afm
│   │           │   │   │   │   ├── pcrb8a.afm
│   │           │   │   │   │   ├── pcrbo8a.afm
│   │           │   │   │   │   ├── pcrr8a.afm
│   │           │   │   │   │   ├── pcrro8a.afm
│   │           │   │   │   │   ├── phvb8a.afm
│   │           │   │   │   │   ├── phvb8an.afm
│   │           │   │   │   │   ├── phvbo8a.afm
│   │           │   │   │   │   ├── phvbo8an.afm
│   │           │   │   │   │   ├── phvl8a.afm
│   │           │   │   │   │   ├── phvlo8a.afm
│   │           │   │   │   │   ├── phvr8a.afm
│   │           │   │   │   │   ├── phvr8an.afm
│   │           │   │   │   │   ├── phvro8a.afm
│   │           │   │   │   │   ├── phvro8an.afm
│   │           │   │   │   │   ├── pncb8a.afm
│   │           │   │   │   │   ├── pncbi8a.afm
│   │           │   │   │   │   ├── pncr8a.afm
│   │           │   │   │   │   ├── pncri8a.afm
│   │           │   │   │   │   ├── pplb8a.afm
│   │           │   │   │   │   ├── pplbi8a.afm
│   │           │   │   │   │   ├── pplr8a.afm
│   │           │   │   │   │   ├── pplri8a.afm
│   │           │   │   │   │   ├── psyr.afm
│   │           │   │   │   │   ├── ptmb8a.afm
│   │           │   │   │   │   ├── ptmbi8a.afm
│   │           │   │   │   │   ├── ptmr8a.afm
│   │           │   │   │   │   ├── ptmri8a.afm
│   │           │   │   │   │   ├── putb8a.afm
│   │           │   │   │   │   ├── putbi8a.afm
│   │           │   │   │   │   ├── putr8a.afm
│   │           │   │   │   │   ├── putri8a.afm
│   │           │   │   │   │   ├── pzcmi8a.afm
│   │           │   │   │   │   └── pzdr.afm
│   │           │   │   │   ├── pdfcorefonts
│   │           │   │   │   │   ├── Courier.afm
│   │           │   │   │   │   ├── Courier-Bold.afm
│   │           │   │   │   │   ├── Courier-BoldOblique.afm
│   │           │   │   │   │   ├── Courier-Oblique.afm
│   │           │   │   │   │   ├── Helvetica.afm
│   │           │   │   │   │   ├── Helvetica-Bold.afm
│   │           │   │   │   │   ├── Helvetica-BoldOblique.afm
│   │           │   │   │   │   ├── Helvetica-Oblique.afm
│   │           │   │   │   │   ├── readme.txt
│   │           │   │   │   │   ├── Symbol.afm
│   │           │   │   │   │   ├── Times-Bold.afm
│   │           │   │   │   │   ├── Times-BoldItalic.afm
│   │           │   │   │   │   ├── Times-Italic.afm
│   │           │   │   │   │   ├── Times-Roman.afm
│   │           │   │   │   │   └── ZapfDingbats.afm
│   │           │   │   │   └── ttf
│   │           │   │   │       ├── cmb10.ttf
│   │           │   │   │       ├── cmex10.ttf
│   │           │   │   │       ├── cmmi10.ttf
│   │           │   │   │       ├── cmr10.ttf
│   │           │   │   │       ├── cmss10.ttf
│   │           │   │   │       ├── cmsy10.ttf
│   │           │   │   │       ├── cmtt10.ttf
│   │           │   │   │       ├── DejaVuSans-BoldOblique.ttf
│   │           │   │   │       ├── DejaVuSans-Bold.ttf
│   │           │   │   │       ├── DejaVuSansDisplay.ttf
│   │           │   │   │       ├── DejaVuSansMono-BoldOblique.ttf
│   │           │   │   │       ├── DejaVuSansMono-Bold.ttf
│   │           │   │   │       ├── DejaVuSansMono-Oblique.ttf
│   │           │   │   │       ├── DejaVuSansMono.ttf
│   │           │   │   │       ├── DejaVuSans-Oblique.ttf
│   │           │   │   │       ├── DejaVuSans.ttf
│   │           │   │   │       ├── DejaVuSerif-BoldItalic.ttf
│   │           │   │   │       ├── DejaVuSerif-Bold.ttf
│   │           │   │   │       ├── DejaVuSerifDisplay.ttf
│   │           │   │   │       ├── DejaVuSerif-Italic.ttf
│   │           │   │   │       ├── DejaVuSerif.ttf
│   │           │   │   │       ├── LICENSE_DEJAVU
│   │           │   │   │       ├── LICENSE_STIX
│   │           │   │   │       ├── local.conf
│   │           │   │   │       ├── STIXGeneralBolIta.ttf
│   │           │   │   │       ├── STIXGeneralBol.ttf
│   │           │   │   │       ├── STIXGeneralItalic.ttf
│   │           │   │   │       ├── STIXGeneral.ttf
│   │           │   │   │       ├── STIXNonUniBolIta.ttf
│   │           │   │   │       ├── STIXNonUniBol.ttf
│   │           │   │   │       ├── STIXNonUniIta.ttf
│   │           │   │   │       ├── STIXNonUni.ttf
│   │           │   │   │       ├── STIXSizFiveSymReg.ttf
│   │           │   │   │       ├── STIXSizFourSymBol.ttf
│   │           │   │   │       ├── STIXSizFourSymReg.ttf
│   │           │   │   │       ├── STIXSizOneSymBol.ttf
│   │           │   │   │       ├── STIXSizOneSymReg.ttf
│   │           │   │   │       ├── STIXSizThreeSymBol.ttf
│   │           │   │   │       ├── STIXSizThreeSymReg.ttf
│   │           │   │   │       ├── STIXSizTwoSymBol.ttf
│   │           │   │   │       └── STIXSizTwoSymReg.ttf
│   │           │   │   ├── images
│   │           │   │   │   ├── back.gif
│   │           │   │   │   ├── back_large.gif
│   │           │   │   │   ├── back_large.png
│   │           │   │   │   ├── back.pdf
│   │           │   │   │   ├── back.png
│   │           │   │   │   ├── back.svg
│   │           │   │   │   ├── filesave.gif
│   │           │   │   │   ├── filesave_large.gif
│   │           │   │   │   ├── filesave_large.png
│   │           │   │   │   ├── filesave.pdf
│   │           │   │   │   ├── filesave.png
│   │           │   │   │   ├── filesave.svg
│   │           │   │   │   ├── forward.gif
│   │           │   │   │   ├── forward_large.gif
│   │           │   │   │   ├── forward_large.png
│   │           │   │   │   ├── forward.pdf
│   │           │   │   │   ├── forward.png
│   │           │   │   │   ├── forward.svg
│   │           │   │   │   ├── hand.gif
│   │           │   │   │   ├── hand_large.gif
│   │           │   │   │   ├── hand.pdf
│   │           │   │   │   ├── hand.png
│   │           │   │   │   ├── hand.svg
│   │           │   │   │   ├── help_large.png
│   │           │   │   │   ├── help_large.ppm
│   │           │   │   │   ├── help.pdf
│   │           │   │   │   ├── help.png
│   │           │   │   │   ├── help.ppm
│   │           │   │   │   ├── help.svg
│   │           │   │   │   ├── home.gif
│   │           │   │   │   ├── home_large.gif
│   │           │   │   │   ├── home_large.png
│   │           │   │   │   ├── home.pdf
│   │           │   │   │   ├── home.png
│   │           │   │   │   ├── home.svg
│   │           │   │   │   ├── matplotlib_large.png
│   │           │   │   │   ├── matplotlib.pdf
│   │           │   │   │   ├── matplotlib.png
│   │           │   │   │   ├── matplotlib.ppm
│   │           │   │   │   ├── matplotlib.svg
│   │           │   │   │   ├── move.gif
│   │           │   │   │   ├── move_large.gif
│   │           │   │   │   ├── move_large.png
│   │           │   │   │   ├── move.pdf
│   │           │   │   │   ├── move.png
│   │           │   │   │   ├── move.svg
│   │           │   │   │   ├── qt4_editor_options_large.png
│   │           │   │   │   ├── qt4_editor_options.pdf
│   │           │   │   │   ├── qt4_editor_options.png
│   │           │   │   │   ├── qt4_editor_options.svg
│   │           │   │   │   ├── subplots.gif
│   │           │   │   │   ├── subplots_large.gif
│   │           │   │   │   ├── subplots_large.png
│   │           │   │   │   ├── subplots.pdf
│   │           │   │   │   ├── subplots.png
│   │           │   │   │   ├── subplots.svg
│   │           │   │   │   ├── zoom_to_rect.gif
│   │           │   │   │   ├── zoom_to_rect_large.gif
│   │           │   │   │   ├── zoom_to_rect_large.png
│   │           │   │   │   ├── zoom_to_rect.pdf
│   │           │   │   │   ├── zoom_to_rect.png
│   │           │   │   │   └── zoom_to_rect.svg
│   │           │   │   ├── matplotlibrc
│   │           │   │   ├── sample_data
│   │           │   │   │   ├── aapl.npz
│   │           │   │   │   ├── ada.png
│   │           │   │   │   ├── axes_grid
│   │           │   │   │   │   └── bivariate_normal.npy
│   │           │   │   │   ├── ct.raw.gz
│   │           │   │   │   ├── data_x_x2_x3.csv
│   │           │   │   │   ├── demodata.csv
│   │           │   │   │   ├── eeg.dat
│   │           │   │   │   ├── embedding_in_wx3.xrc
│   │           │   │   │   ├── goog.npz
│   │           │   │   │   ├── grace_hopper.jpg
│   │           │   │   │   ├── grace_hopper.png
│   │           │   │   │   ├── jacksboro_fault_dem.npz
│   │           │   │   │   ├── logo2.png
│   │           │   │   │   ├── membrane.dat
│   │           │   │   │   ├── Minduka_Present_Blue_Pack.png
│   │           │   │   │   ├── msft.csv
│   │           │   │   │   ├── None_vs_nearest-pdf.png
│   │           │   │   │   ├── percent_bachelors_degrees_women_usa.csv
│   │           │   │   │   ├── README.txt
│   │           │   │   │   └── s1045.ima.gz
│   │           │   │   └── stylelib
│   │           │   │       ├── bmh.mplstyle
│   │           │   │       ├── classic.mplstyle
│   │           │   │       ├── _classic_test.mplstyle
│   │           │   │       ├── dark_background.mplstyle
│   │           │   │       ├── fast.mplstyle
│   │           │   │       ├── fivethirtyeight.mplstyle
│   │           │   │       ├── ggplot.mplstyle
│   │           │   │       ├── grayscale.mplstyle
│   │           │   │       ├── seaborn-bright.mplstyle
│   │           │   │       ├── seaborn-colorblind.mplstyle
│   │           │   │       ├── seaborn-darkgrid.mplstyle
│   │           │   │       ├── seaborn-dark.mplstyle
│   │           │   │       ├── seaborn-dark-palette.mplstyle
│   │           │   │       ├── seaborn-deep.mplstyle
│   │           │   │       ├── seaborn.mplstyle
│   │           │   │       ├── seaborn-muted.mplstyle
│   │           │   │       ├── seaborn-notebook.mplstyle
│   │           │   │       ├── seaborn-paper.mplstyle
│   │           │   │       ├── seaborn-pastel.mplstyle
│   │           │   │       ├── seaborn-poster.mplstyle
│   │           │   │       ├── seaborn-talk.mplstyle
│   │           │   │       ├── seaborn-ticks.mplstyle
│   │           │   │       ├── seaborn-whitegrid.mplstyle
│   │           │   │       ├── seaborn-white.mplstyle
│   │           │   │       ├── Solarize_Light2.mplstyle
│   │           │   │       └── tableau-colorblind10.mplstyle
│   │           │   ├── offsetbox.py
│   │           │   ├── patches.py
│   │           │   ├── _path.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── patheffects.py
│   │           │   ├── path.py
│   │           │   ├── _png.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── projections
│   │           │   │   ├── geo.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── polar.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── geo.cpython-36.pyc
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       └── polar.cpython-36.pyc
│   │           │   ├── __pycache__
│   │           │   │   ├── afm.cpython-36.pyc
│   │           │   │   ├── animation.cpython-36.pyc
│   │           │   │   ├── _animation_data.cpython-36.pyc
│   │           │   │   ├── artist.cpython-36.pyc
│   │           │   │   ├── axis.cpython-36.pyc
│   │           │   │   ├── backend_bases.cpython-36.pyc
│   │           │   │   ├── backend_managers.cpython-36.pyc
│   │           │   │   ├── backend_tools.cpython-36.pyc
│   │           │   │   ├── bezier.cpython-36.pyc
│   │           │   │   ├── blocking_input.cpython-36.pyc
│   │           │   │   ├── category.cpython-36.pyc
│   │           │   │   ├── _cm.cpython-36.pyc
│   │           │   │   ├── cm.cpython-36.pyc
│   │           │   │   ├── _cm_listed.cpython-36.pyc
│   │           │   │   ├── collections.cpython-36.pyc
│   │           │   │   ├── colorbar.cpython-36.pyc
│   │           │   │   ├── _color_data.cpython-36.pyc
│   │           │   │   ├── colors.cpython-36.pyc
│   │           │   │   ├── _constrained_layout.cpython-36.pyc
│   │           │   │   ├── container.cpython-36.pyc
│   │           │   │   ├── contour.cpython-36.pyc
│   │           │   │   ├── dates.cpython-36.pyc
│   │           │   │   ├── docstring.cpython-36.pyc
│   │           │   │   ├── dviread.cpython-36.pyc
│   │           │   │   ├── figure.cpython-36.pyc
│   │           │   │   ├── fontconfig_pattern.cpython-36.pyc
│   │           │   │   ├── font_manager.cpython-36.pyc
│   │           │   │   ├── gridspec.cpython-36.pyc
│   │           │   │   ├── hatch.cpython-36.pyc
│   │           │   │   ├── image.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── _layoutbox.cpython-36.pyc
│   │           │   │   ├── legend.cpython-36.pyc
│   │           │   │   ├── legend_handler.cpython-36.pyc
│   │           │   │   ├── lines.cpython-36.pyc
│   │           │   │   ├── markers.cpython-36.pyc
│   │           │   │   ├── mathtext.cpython-36.pyc
│   │           │   │   ├── _mathtext_data.cpython-36.pyc
│   │           │   │   ├── mlab.cpython-36.pyc
│   │           │   │   ├── offsetbox.cpython-36.pyc
│   │           │   │   ├── patches.cpython-36.pyc
│   │           │   │   ├── path.cpython-36.pyc
│   │           │   │   ├── patheffects.cpython-36.pyc
│   │           │   │   ├── pylab.cpython-36.pyc
│   │           │   │   ├── _pylab_helpers.cpython-36.pyc
│   │           │   │   ├── pyplot.cpython-36.pyc
│   │           │   │   ├── quiver.cpython-36.pyc
│   │           │   │   ├── rcsetup.cpython-36.pyc
│   │           │   │   ├── sankey.cpython-36.pyc
│   │           │   │   ├── scale.cpython-36.pyc
│   │           │   │   ├── spines.cpython-36.pyc
│   │           │   │   ├── stackplot.cpython-36.pyc
│   │           │   │   ├── streamplot.cpython-36.pyc
│   │           │   │   ├── table.cpython-36.pyc
│   │           │   │   ├── texmanager.cpython-36.pyc
│   │           │   │   ├── text.cpython-36.pyc
│   │           │   │   ├── textpath.cpython-36.pyc
│   │           │   │   ├── ticker.cpython-36.pyc
│   │           │   │   ├── tight_bbox.cpython-36.pyc
│   │           │   │   ├── tight_layout.cpython-36.pyc
│   │           │   │   ├── transforms.cpython-36.pyc
│   │           │   │   ├── type1font.cpython-36.pyc
│   │           │   │   ├── units.cpython-36.pyc
│   │           │   │   ├── _version.cpython-36.pyc
│   │           │   │   └── widgets.cpython-36.pyc
│   │           │   ├── _pylab_helpers.py
│   │           │   ├── pylab.py
│   │           │   ├── pyplot.py
│   │           │   ├── _qhull.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── quiver.py
│   │           │   ├── rcsetup.py
│   │           │   ├── sankey.py
│   │           │   ├── scale.py
│   │           │   ├── sphinxext
│   │           │   │   ├── __init__.py
│   │           │   │   ├── mathmpl.py
│   │           │   │   ├── plot_directive.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── mathmpl.cpython-36.pyc
│   │           │   │   │   └── plot_directive.cpython-36.pyc
│   │           │   │   └── tests
│   │           │   │       ├── conftest.py
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── conftest.cpython-36.pyc
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   └── test_tinypages.cpython-36.pyc
│   │           │   │       ├── test_tinypages.py
│   │           │   │       └── tinypages
│   │           │   │           ├── conf.py
│   │           │   │           ├── index.rst
│   │           │   │           ├── __pycache__
│   │           │   │           │   ├── conf.cpython-36.pyc
│   │           │   │           │   ├── range4.cpython-36.pyc
│   │           │   │           │   └── range6.cpython-36.pyc
│   │           │   │           ├── range4.py
│   │           │   │           ├── range6.py
│   │           │   │           ├── some_plots.rst
│   │           │   │           └── _static
│   │           │   │               └── README.txt
│   │           │   ├── spines.py
│   │           │   ├── stackplot.py
│   │           │   ├── streamplot.py
│   │           │   ├── style
│   │           │   │   ├── core.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── core.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── table.py
│   │           │   ├── testing
│   │           │   │   ├── compare.py
│   │           │   │   ├── conftest.py
│   │           │   │   ├── decorators.py
│   │           │   │   ├── determinism.py
│   │           │   │   ├── disable_internet.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── jpl_units
│   │           │   │   │   ├── Duration.py
│   │           │   │   │   ├── EpochConverter.py
│   │           │   │   │   ├── Epoch.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── Duration.cpython-36.pyc
│   │           │   │   │   │   ├── EpochConverter.cpython-36.pyc
│   │           │   │   │   │   ├── Epoch.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── StrConverter.cpython-36.pyc
│   │           │   │   │   │   ├── UnitDblConverter.cpython-36.pyc
│   │           │   │   │   │   ├── UnitDbl.cpython-36.pyc
│   │           │   │   │   │   └── UnitDblFormatter.cpython-36.pyc
│   │           │   │   │   ├── StrConverter.py
│   │           │   │   │   ├── UnitDblConverter.py
│   │           │   │   │   ├── UnitDblFormatter.py
│   │           │   │   │   └── UnitDbl.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── compare.cpython-36.pyc
│   │           │   │       ├── conftest.cpython-36.pyc
│   │           │   │       ├── decorators.cpython-36.pyc
│   │           │   │       ├── determinism.cpython-36.pyc
│   │           │   │       ├── disable_internet.cpython-36.pyc
│   │           │   │       ├── exceptions.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── tests
│   │           │   │   ├── cmr10.pfb
│   │           │   │   ├── conftest.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── mpltest.ttf
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── test_afm.cpython-36.pyc
│   │           │   │   │   ├── test_agg.cpython-36.pyc
│   │           │   │   │   ├── test_animation.cpython-36.pyc
│   │           │   │   │   ├── test_arrow_patches.cpython-36.pyc
│   │           │   │   │   ├── test_artist.cpython-36.pyc
│   │           │   │   │   ├── test_axes.cpython-36.pyc
│   │           │   │   │   ├── test_backend_bases.cpython-36.pyc
│   │           │   │   │   ├── test_backend_cairo.cpython-36.pyc
│   │           │   │   │   ├── test_backend_nbagg.cpython-36.pyc
│   │           │   │   │   ├── test_backend_pdf.cpython-36.pyc
│   │           │   │   │   ├── test_backend_pgf.cpython-36.pyc
│   │           │   │   │   ├── test_backend_ps.cpython-36.pyc
│   │           │   │   │   ├── test_backend_qt4.cpython-36.pyc
│   │           │   │   │   ├── test_backend_qt5.cpython-36.pyc
│   │           │   │   │   ├── test_backends_interactive.cpython-36.pyc
│   │           │   │   │   ├── test_backend_svg.cpython-36.pyc
│   │           │   │   │   ├── test_backend_tools.cpython-36.pyc
│   │           │   │   │   ├── test_basic.cpython-36.pyc
│   │           │   │   │   ├── test_bbox_tight.cpython-36.pyc
│   │           │   │   │   ├── test_category.cpython-36.pyc
│   │           │   │   │   ├── test_cbook.cpython-36.pyc
│   │           │   │   │   ├── test_collections.cpython-36.pyc
│   │           │   │   │   ├── test_colorbar.cpython-36.pyc
│   │           │   │   │   ├── test_colors.cpython-36.pyc
│   │           │   │   │   ├── test_compare_images.cpython-36.pyc
│   │           │   │   │   ├── test_constrainedlayout.cpython-36.pyc
│   │           │   │   │   ├── test_container.cpython-36.pyc
│   │           │   │   │   ├── test_contour.cpython-36.pyc
│   │           │   │   │   ├── test_cycles.cpython-36.pyc
│   │           │   │   │   ├── test_dates.cpython-36.pyc
│   │           │   │   │   ├── test_dviread.cpython-36.pyc
│   │           │   │   │   ├── test_figure.cpython-36.pyc
│   │           │   │   │   ├── test_font_manager.cpython-36.pyc
│   │           │   │   │   ├── test_gridspec.cpython-36.pyc
│   │           │   │   │   ├── test_image.cpython-36.pyc
│   │           │   │   │   ├── test_legend.cpython-36.pyc
│   │           │   │   │   ├── test_lines.cpython-36.pyc
│   │           │   │   │   ├── test_marker.cpython-36.pyc
│   │           │   │   │   ├── test_mathtext.cpython-36.pyc
│   │           │   │   │   ├── test_matplotlib.cpython-36.pyc
│   │           │   │   │   ├── test_mlab.cpython-36.pyc
│   │           │   │   │   ├── test_offsetbox.cpython-36.pyc
│   │           │   │   │   ├── test_patches.cpython-36.pyc
│   │           │   │   │   ├── test_path.cpython-36.pyc
│   │           │   │   │   ├── test_patheffects.cpython-36.pyc
│   │           │   │   │   ├── test_pickle.cpython-36.pyc
│   │           │   │   │   ├── test_png.cpython-36.pyc
│   │           │   │   │   ├── test_preprocess_data.cpython-36.pyc
│   │           │   │   │   ├── test_pyplot.cpython-36.pyc
│   │           │   │   │   ├── test_quiver.cpython-36.pyc
│   │           │   │   │   ├── test_rcparams.cpython-36.pyc
│   │           │   │   │   ├── test_sankey.cpython-36.pyc
│   │           │   │   │   ├── test_scale.cpython-36.pyc
│   │           │   │   │   ├── test_simplification.cpython-36.pyc
│   │           │   │   │   ├── test_skew.cpython-36.pyc
│   │           │   │   │   ├── test_spines.cpython-36.pyc
│   │           │   │   │   ├── test_streamplot.cpython-36.pyc
│   │           │   │   │   ├── test_style.cpython-36.pyc
│   │           │   │   │   ├── test_subplots.cpython-36.pyc
│   │           │   │   │   ├── test_table.cpython-36.pyc
│   │           │   │   │   ├── test_texmanager.cpython-36.pyc
│   │           │   │   │   ├── test_text.cpython-36.pyc
│   │           │   │   │   ├── test_ticker.cpython-36.pyc
│   │           │   │   │   ├── test_tightlayout.cpython-36.pyc
│   │           │   │   │   ├── test_transforms.cpython-36.pyc
│   │           │   │   │   ├── test_triangulation.cpython-36.pyc
│   │           │   │   │   ├── test_ttconv.cpython-36.pyc
│   │           │   │   │   ├── test_type1font.cpython-36.pyc
│   │           │   │   │   ├── test_units.cpython-36.pyc
│   │           │   │   │   ├── test_usetex.cpython-36.pyc
│   │           │   │   │   └── test_widgets.cpython-36.pyc
│   │           │   │   ├── test_afm.py
│   │           │   │   ├── test_agg.py
│   │           │   │   ├── test_animation.py
│   │           │   │   ├── test_arrow_patches.py
│   │           │   │   ├── test_artist.py
│   │           │   │   ├── test_axes.py
│   │           │   │   ├── test_backend_bases.py
│   │           │   │   ├── test_backend_cairo.py
│   │           │   │   ├── test_backend_nbagg.py
│   │           │   │   ├── test_backend_pdf.py
│   │           │   │   ├── test_backend_pgf.py
│   │           │   │   ├── test_backend_ps.py
│   │           │   │   ├── test_backend_qt4.py
│   │           │   │   ├── test_backend_qt5.py
│   │           │   │   ├── test_backends_interactive.py
│   │           │   │   ├── test_backend_svg.py
│   │           │   │   ├── test_backend_tools.py
│   │           │   │   ├── test_basic.py
│   │           │   │   ├── test_bbox_tight.py
│   │           │   │   ├── test_category.py
│   │           │   │   ├── test_cbook.py
│   │           │   │   ├── test_collections.py
│   │           │   │   ├── test_colorbar.py
│   │           │   │   ├── test_colors.py
│   │           │   │   ├── test_compare_images.py
│   │           │   │   ├── test_constrainedlayout.py
│   │           │   │   ├── test_container.py
│   │           │   │   ├── test_contour.py
│   │           │   │   ├── test_cycles.py
│   │           │   │   ├── test_dates.py
│   │           │   │   ├── test_dviread.py
│   │           │   │   ├── test_figure.py
│   │           │   │   ├── test_font_manager.py
│   │           │   │   ├── test_gridspec.py
│   │           │   │   ├── test_image.py
│   │           │   │   ├── test_legend.py
│   │           │   │   ├── test_lines.py
│   │           │   │   ├── test_marker.py
│   │           │   │   ├── test_mathtext.py
│   │           │   │   ├── test_matplotlib.py
│   │           │   │   ├── test_mlab.py
│   │           │   │   ├── test_offsetbox.py
│   │           │   │   ├── test_patches.py
│   │           │   │   ├── test_patheffects.py
│   │           │   │   ├── test_path.py
│   │           │   │   ├── test_pickle.py
│   │           │   │   ├── test_png.py
│   │           │   │   ├── test_preprocess_data.py
│   │           │   │   ├── test_pyplot.py
│   │           │   │   ├── test_quiver.py
│   │           │   │   ├── test_rcparams.py
│   │           │   │   ├── test_rcparams.rc
│   │           │   │   ├── test_sankey.py
│   │           │   │   ├── test_scale.py
│   │           │   │   ├── test_simplification.py
│   │           │   │   ├── test_skew.py
│   │           │   │   ├── test_spines.py
│   │           │   │   ├── test_streamplot.py
│   │           │   │   ├── test_style.py
│   │           │   │   ├── test_subplots.py
│   │           │   │   ├── test_table.py
│   │           │   │   ├── test_texmanager.py
│   │           │   │   ├── test_text.py
│   │           │   │   ├── test_ticker.py
│   │           │   │   ├── test_tightlayout.py
│   │           │   │   ├── test_transforms.py
│   │           │   │   ├── test_triangulation.py
│   │           │   │   ├── test_ttconv.py
│   │           │   │   ├── test_type1font.py
│   │           │   │   ├── test_units.py
│   │           │   │   ├── test_usetex.py
│   │           │   │   ├── test_utf32_be_rcparams.rc
│   │           │   │   └── test_widgets.py
│   │           │   ├── texmanager.py
│   │           │   ├── textpath.py
│   │           │   ├── text.py
│   │           │   ├── ticker.py
│   │           │   ├── tight_bbox.py
│   │           │   ├── tight_layout.py
│   │           │   ├── transforms.py
│   │           │   ├── tri
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── triangulation.cpython-36.pyc
│   │           │   │   │   ├── tricontour.cpython-36.pyc
│   │           │   │   │   ├── trifinder.cpython-36.pyc
│   │           │   │   │   ├── triinterpolate.cpython-36.pyc
│   │           │   │   │   ├── tripcolor.cpython-36.pyc
│   │           │   │   │   ├── triplot.cpython-36.pyc
│   │           │   │   │   ├── trirefine.cpython-36.pyc
│   │           │   │   │   └── tritools.cpython-36.pyc
│   │           │   │   ├── triangulation.py
│   │           │   │   ├── tricontour.py
│   │           │   │   ├── trifinder.py
│   │           │   │   ├── triinterpolate.py
│   │           │   │   ├── tripcolor.py
│   │           │   │   ├── triplot.py
│   │           │   │   ├── trirefine.py
│   │           │   │   └── tritools.py
│   │           │   ├── _tri.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── ttconv.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── type1font.py
│   │           │   ├── units.py
│   │           │   ├── _version.py
│   │           │   └── widgets.py
│   │           ├── matplotlib-3.0.3.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── namespace_packages.txt
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── matplotlib-3.0.3-py3.6-nspkg.pth
│   │           ├── mistune-0.8.4.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── mistune.py
│   │           ├── mpl_toolkits
│   │           │   ├── axes_grid
│   │           │   │   ├── anchored_artists.py
│   │           │   │   ├── angle_helper.py
│   │           │   │   ├── axes_divider.py
│   │           │   │   ├── axes_grid.py
│   │           │   │   ├── axes_rgb.py
│   │           │   │   ├── axes_size.py
│   │           │   │   ├── axis_artist.py
│   │           │   │   ├── axislines.py
│   │           │   │   ├── axisline_style.py
│   │           │   │   ├── clip_path.py
│   │           │   │   ├── colorbar.py
│   │           │   │   ├── floating_axes.py
│   │           │   │   ├── grid_finder.py
│   │           │   │   ├── grid_helper_curvelinear.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── inset_locator.py
│   │           │   │   ├── parasite_axes.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── anchored_artists.cpython-36.pyc
│   │           │   │       ├── angle_helper.cpython-36.pyc
│   │           │   │       ├── axes_divider.cpython-36.pyc
│   │           │   │       ├── axes_grid.cpython-36.pyc
│   │           │   │       ├── axes_rgb.cpython-36.pyc
│   │           │   │       ├── axes_size.cpython-36.pyc
│   │           │   │       ├── axis_artist.cpython-36.pyc
│   │           │   │       ├── axislines.cpython-36.pyc
│   │           │   │       ├── axisline_style.cpython-36.pyc
│   │           │   │       ├── clip_path.cpython-36.pyc
│   │           │   │       ├── colorbar.cpython-36.pyc
│   │           │   │       ├── floating_axes.cpython-36.pyc
│   │           │   │       ├── grid_finder.cpython-36.pyc
│   │           │   │       ├── grid_helper_curvelinear.cpython-36.pyc
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       ├── inset_locator.cpython-36.pyc
│   │           │   │       └── parasite_axes.cpython-36.pyc
│   │           │   ├── axes_grid1
│   │           │   │   ├── anchored_artists.py
│   │           │   │   ├── axes_divider.py
│   │           │   │   ├── axes_grid.py
│   │           │   │   ├── axes_rgb.py
│   │           │   │   ├── axes_size.py
│   │           │   │   ├── colorbar.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── inset_locator.py
│   │           │   │   ├── mpl_axes.py
│   │           │   │   ├── parasite_axes.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── anchored_artists.cpython-36.pyc
│   │           │   │       ├── axes_divider.cpython-36.pyc
│   │           │   │       ├── axes_grid.cpython-36.pyc
│   │           │   │       ├── axes_rgb.cpython-36.pyc
│   │           │   │       ├── axes_size.cpython-36.pyc
│   │           │   │       ├── colorbar.cpython-36.pyc
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       ├── inset_locator.cpython-36.pyc
│   │           │   │       ├── mpl_axes.cpython-36.pyc
│   │           │   │       └── parasite_axes.cpython-36.pyc
│   │           │   ├── axisartist
│   │           │   │   ├── angle_helper.py
│   │           │   │   ├── axes_divider.py
│   │           │   │   ├── axes_grid.py
│   │           │   │   ├── axes_rgb.py
│   │           │   │   ├── axis_artist.py
│   │           │   │   ├── axislines.py
│   │           │   │   ├── axisline_style.py
│   │           │   │   ├── clip_path.py
│   │           │   │   ├── floating_axes.py
│   │           │   │   ├── grid_finder.py
│   │           │   │   ├── grid_helper_curvelinear.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── parasite_axes.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── angle_helper.cpython-36.pyc
│   │           │   │       ├── axes_divider.cpython-36.pyc
│   │           │   │       ├── axes_grid.cpython-36.pyc
│   │           │   │       ├── axes_rgb.cpython-36.pyc
│   │           │   │       ├── axis_artist.cpython-36.pyc
│   │           │   │       ├── axislines.cpython-36.pyc
│   │           │   │       ├── axisline_style.cpython-36.pyc
│   │           │   │       ├── clip_path.cpython-36.pyc
│   │           │   │       ├── floating_axes.cpython-36.pyc
│   │           │   │       ├── grid_finder.cpython-36.pyc
│   │           │   │       ├── grid_helper_curvelinear.cpython-36.pyc
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       └── parasite_axes.cpython-36.pyc
│   │           │   ├── mplot3d
│   │           │   │   ├── art3d.py
│   │           │   │   ├── axes3d.py
│   │           │   │   ├── axis3d.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── proj3d.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── art3d.cpython-36.pyc
│   │           │   │       ├── axes3d.cpython-36.pyc
│   │           │   │       ├── axis3d.cpython-36.pyc
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       └── proj3d.cpython-36.pyc
│   │           │   └── tests
│   │           │       ├── baseline_images
│   │           │       │   ├── test_axes_grid
│   │           │       │   │   └── imagegrid_cbar_mode.png
│   │           │       │   ├── test_axes_grid1
│   │           │       │   │   ├── anchored_direction_arrows_many_args.png
│   │           │       │   │   ├── anchored_direction_arrows.png
│   │           │       │   │   ├── divider_append_axes.pdf
│   │           │       │   │   ├── divider_append_axes.png
│   │           │       │   │   ├── divider_append_axes.svg
│   │           │       │   │   ├── fill_facecolor.png
│   │           │       │   │   ├── image_grid.png
│   │           │       │   │   ├── inset_axes.png
│   │           │       │   │   ├── inset_locator.png
│   │           │       │   │   ├── inverted_zoomed_axes.png
│   │           │       │   │   ├── twin_axes_empty_and_removed.png
│   │           │       │   │   └── zoomed_axes.png
│   │           │       │   ├── test_axisartist_axis_artist
│   │           │       │   │   ├── axis_artist_labelbase.png
│   │           │       │   │   ├── axis_artist.png
│   │           │       │   │   ├── axis_artist_ticklabels.png
│   │           │       │   │   └── axis_artist_ticks.png
│   │           │       │   ├── test_axisartist_axislines
│   │           │       │   │   ├── ParasiteAxesAuxTrans_meshplot.png
│   │           │       │   │   ├── Subplot.png
│   │           │       │   │   └── SubplotZero.png
│   │           │       │   ├── test_axisartist_clip_path
│   │           │       │   │   └── clip_path.png
│   │           │       │   ├── test_axisartist_floating_axes
│   │           │       │   │   ├── curvelinear3.png
│   │           │       │   │   └── curvelinear4.png
│   │           │       │   ├── test_axisartist_grid_helper_curvelinear
│   │           │       │   │   ├── axis_direction.png
│   │           │       │   │   ├── custom_transform.png
│   │           │       │   │   └── polar_box.png
│   │           │       │   └── test_mplot3d
│   │           │       │       ├── axes3d_cla.png
│   │           │       │       ├── axes3d_labelpad.png
│   │           │       │       ├── axes3d_ortho.pdf
│   │           │       │       ├── axes3d_ortho.png
│   │           │       │       ├── axes3d_ortho.svg
│   │           │       │       ├── bar3d_notshaded.png
│   │           │       │       ├── bar3d.pdf
│   │           │       │       ├── bar3d.png
│   │           │       │       ├── bar3d_shaded.png
│   │           │       │       ├── bar3d.svg
│   │           │       │       ├── contour3d.pdf
│   │           │       │       ├── contour3d.png
│   │           │       │       ├── contour3d.svg
│   │           │       │       ├── contourf3d_fill.pdf
│   │           │       │       ├── contourf3d_fill.png
│   │           │       │       ├── contourf3d_fill.svg
│   │           │       │       ├── contourf3d.pdf
│   │           │       │       ├── contourf3d.png
│   │           │       │       ├── contourf3d.svg
│   │           │       │       ├── lines3d.pdf
│   │           │       │       ├── lines3d.png
│   │           │       │       ├── lines3d.svg
│   │           │       │       ├── mixedsubplot.pdf
│   │           │       │       ├── mixedsubplot.png
│   │           │       │       ├── mixedsubplot.svg
│   │           │       │       ├── plot_3d_from_2d.png
│   │           │       │       ├── poly3dcollection_closed.pdf
│   │           │       │       ├── poly3dcollection_closed.png
│   │           │       │       ├── poly3dcollection_closed.svg
│   │           │       │       ├── proj3d_axes_cube_ortho.png
│   │           │       │       ├── proj3d_axes_cube.png
│   │           │       │       ├── proj3d_lines_dists.png
│   │           │       │       ├── quiver3d_empty.pdf
│   │           │       │       ├── quiver3d_empty.png
│   │           │       │       ├── quiver3d_empty.svg
│   │           │       │       ├── quiver3d_masked.pdf
│   │           │       │       ├── quiver3d_masked.png
│   │           │       │       ├── quiver3d_masked.svg
│   │           │       │       ├── quiver3d.pdf
│   │           │       │       ├── quiver3d_pivot_middle.png
│   │           │       │       ├── quiver3d_pivot_tail.png
│   │           │       │       ├── quiver3d.png
│   │           │       │       ├── quiver3d.svg
│   │           │       │       ├── scatter3d_color.png
│   │           │       │       ├── scatter3d.pdf
│   │           │       │       ├── scatter3d.png
│   │           │       │       ├── scatter3d.svg
│   │           │       │       ├── surface3d.pdf
│   │           │       │       ├── surface3d.png
│   │           │       │       ├── surface3d_shaded.png
│   │           │       │       ├── surface3d.svg
│   │           │       │       ├── text3d.pdf
│   │           │       │       ├── text3d.png
│   │           │       │       ├── text3d.svg
│   │           │       │       ├── tricontour.png
│   │           │       │       ├── trisurf3d.pdf
│   │           │       │       ├── trisurf3d.png
│   │           │       │       ├── trisurf3d_shaded.png
│   │           │       │       ├── trisurf3d.svg
│   │           │       │       ├── voxels-alpha.png
│   │           │       │       ├── voxels-edge-style.png
│   │           │       │       ├── voxels-named-colors.png
│   │           │       │       ├── voxels-rgb-data.png
│   │           │       │       ├── voxels-simple.png
│   │           │       │       ├── voxels-xyz.png
│   │           │       │       ├── wireframe3d.pdf
│   │           │       │       ├── wireframe3d.png
│   │           │       │       ├── wireframe3d.svg
│   │           │       │       ├── wireframe3dzerocstride.png
│   │           │       │       └── wireframe3dzerorstride.png
│   │           │       ├── conftest.py
│   │           │       ├── __init__.py
│   │           │       ├── __pycache__
│   │           │       │   ├── conftest.cpython-36.pyc
│   │           │       │   ├── __init__.cpython-36.pyc
│   │           │       │   ├── test_axes_grid1.cpython-36.pyc
│   │           │       │   ├── test_axes_grid.cpython-36.pyc
│   │           │       │   ├── test_axisartist_angle_helper.cpython-36.pyc
│   │           │       │   ├── test_axisartist_axis_artist.cpython-36.pyc
│   │           │       │   ├── test_axisartist_axislines.cpython-36.pyc
│   │           │       │   ├── test_axisartist_clip_path.cpython-36.pyc
│   │           │       │   ├── test_axisartist_floating_axes.cpython-36.pyc
│   │           │       │   ├── test_axisartist_grid_finder.cpython-36.pyc
│   │           │       │   ├── test_axisartist_grid_helper_curvelinear.cpython-36.pyc
│   │           │       │   └── test_mplot3d.cpython-36.pyc
│   │           │       ├── test_axes_grid1.py
│   │           │       ├── test_axes_grid.py
│   │           │       ├── test_axisartist_angle_helper.py
│   │           │       ├── test_axisartist_axis_artist.py
│   │           │       ├── test_axisartist_axislines.py
│   │           │       ├── test_axisartist_clip_path.py
│   │           │       ├── test_axisartist_floating_axes.py
│   │           │       ├── test_axisartist_grid_finder.py
│   │           │       ├── test_axisartist_grid_helper_curvelinear.py
│   │           │       └── test_mplot3d.py
│   │           ├── mpmath
│   │           │   ├── calculus
│   │           │   │   ├── approximation.py
│   │           │   │   ├── calculus.py
│   │           │   │   ├── differentiation.py
│   │           │   │   ├── extrapolation.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── inverselaplace.py
│   │           │   │   ├── odes.py
│   │           │   │   ├── optimization.py
│   │           │   │   ├── polynomials.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── approximation.cpython-36.pyc
│   │           │   │   │   ├── calculus.cpython-36.pyc
│   │           │   │   │   ├── differentiation.cpython-36.pyc
│   │           │   │   │   ├── extrapolation.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── inverselaplace.cpython-36.pyc
│   │           │   │   │   ├── odes.cpython-36.pyc
│   │           │   │   │   ├── optimization.cpython-36.pyc
│   │           │   │   │   ├── polynomials.cpython-36.pyc
│   │           │   │   │   └── quadrature.cpython-36.pyc
│   │           │   │   └── quadrature.py
│   │           │   ├── ctx_base.py
│   │           │   ├── ctx_fp.py
│   │           │   ├── ctx_iv.py
│   │           │   ├── ctx_mp.py
│   │           │   ├── ctx_mp_python.py
│   │           │   ├── function_docs.py
│   │           │   ├── functions
│   │           │   │   ├── bessel.py
│   │           │   │   ├── elliptic.py
│   │           │   │   ├── expintegrals.py
│   │           │   │   ├── factorials.py
│   │           │   │   ├── functions.py
│   │           │   │   ├── hypergeometric.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── orthogonal.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── bessel.cpython-36.pyc
│   │           │   │   │   ├── elliptic.cpython-36.pyc
│   │           │   │   │   ├── expintegrals.cpython-36.pyc
│   │           │   │   │   ├── factorials.cpython-36.pyc
│   │           │   │   │   ├── functions.cpython-36.pyc
│   │           │   │   │   ├── hypergeometric.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── orthogonal.cpython-36.pyc
│   │           │   │   │   ├── qfunctions.cpython-36.pyc
│   │           │   │   │   ├── rszeta.cpython-36.pyc
│   │           │   │   │   ├── theta.cpython-36.pyc
│   │           │   │   │   ├── zeta.cpython-36.pyc
│   │           │   │   │   └── zetazeros.cpython-36.pyc
│   │           │   │   ├── qfunctions.py
│   │           │   │   ├── rszeta.py
│   │           │   │   ├── theta.py
│   │           │   │   ├── zeta.py
│   │           │   │   └── zetazeros.py
│   │           │   ├── identification.py
│   │           │   ├── __init__.py
│   │           │   ├── libmp
│   │           │   │   ├── backend.py
│   │           │   │   ├── gammazeta.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── libelefun.py
│   │           │   │   ├── libhyper.py
│   │           │   │   ├── libintmath.py
│   │           │   │   ├── libmpc.py
│   │           │   │   ├── libmpf.py
│   │           │   │   ├── libmpi.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── backend.cpython-36.pyc
│   │           │   │   │   ├── gammazeta.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── libelefun.cpython-36.pyc
│   │           │   │   │   ├── libhyper.cpython-36.pyc
│   │           │   │   │   ├── libintmath.cpython-36.pyc
│   │           │   │   │   ├── libmpc.cpython-36.pyc
│   │           │   │   │   ├── libmpf.cpython-36.pyc
│   │           │   │   │   ├── libmpi.cpython-36.pyc
│   │           │   │   │   └── six.cpython-36.pyc
│   │           │   │   └── six.py
│   │           │   ├── math2.py
│   │           │   ├── matrices
│   │           │   │   ├── calculus.py
│   │           │   │   ├── eigen.py
│   │           │   │   ├── eigen_symmetric.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── linalg.py
│   │           │   │   ├── matrices.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── calculus.cpython-36.pyc
│   │           │   │       ├── eigen.cpython-36.pyc
│   │           │   │       ├── eigen_symmetric.cpython-36.pyc
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       ├── linalg.cpython-36.pyc
│   │           │   │       └── matrices.cpython-36.pyc
│   │           │   ├── __pycache__
│   │           │   │   ├── ctx_base.cpython-36.pyc
│   │           │   │   ├── ctx_fp.cpython-36.pyc
│   │           │   │   ├── ctx_iv.cpython-36.pyc
│   │           │   │   ├── ctx_mp.cpython-36.pyc
│   │           │   │   ├── ctx_mp_python.cpython-36.pyc
│   │           │   │   ├── function_docs.cpython-36.pyc
│   │           │   │   ├── identification.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── math2.cpython-36.pyc
│   │           │   │   ├── rational.cpython-36.pyc
│   │           │   │   ├── usertools.cpython-36.pyc
│   │           │   │   └── visualization.cpython-36.pyc
│   │           │   ├── rational.py
│   │           │   ├── tests
│   │           │   │   ├── extratest_gamma.py
│   │           │   │   ├── extratest_zeta.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── extratest_gamma.cpython-36.pyc
│   │           │   │   │   ├── extratest_zeta.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── runtests.cpython-36.pyc
│   │           │   │   │   ├── test_basic_ops.cpython-36.pyc
│   │           │   │   │   ├── test_bitwise.cpython-36.pyc
│   │           │   │   │   ├── test_calculus.cpython-36.pyc
│   │           │   │   │   ├── test_compatibility.cpython-36.pyc
│   │           │   │   │   ├── test_convert.cpython-36.pyc
│   │           │   │   │   ├── test_diff.cpython-36.pyc
│   │           │   │   │   ├── test_division.cpython-36.pyc
│   │           │   │   │   ├── test_eigen.cpython-36.pyc
│   │           │   │   │   ├── test_eigen_symmetric.cpython-36.pyc
│   │           │   │   │   ├── test_elliptic.cpython-36.pyc
│   │           │   │   │   ├── test_fp.cpython-36.pyc
│   │           │   │   │   ├── test_functions2.cpython-36.pyc
│   │           │   │   │   ├── test_functions.cpython-36.pyc
│   │           │   │   │   ├── test_gammazeta.cpython-36.pyc
│   │           │   │   │   ├── test_hp.cpython-36.pyc
│   │           │   │   │   ├── test_identify.cpython-36.pyc
│   │           │   │   │   ├── test_interval.cpython-36.pyc
│   │           │   │   │   ├── test_levin.cpython-36.pyc
│   │           │   │   │   ├── test_linalg.cpython-36.pyc
│   │           │   │   │   ├── test_matrices.cpython-36.pyc
│   │           │   │   │   ├── test_mpmath.cpython-36.pyc
│   │           │   │   │   ├── test_ode.cpython-36.pyc
│   │           │   │   │   ├── test_pickle.cpython-36.pyc
│   │           │   │   │   ├── test_power.cpython-36.pyc
│   │           │   │   │   ├── test_quad.cpython-36.pyc
│   │           │   │   │   ├── test_rootfinding.cpython-36.pyc
│   │           │   │   │   ├── test_special.cpython-36.pyc
│   │           │   │   │   ├── test_str.cpython-36.pyc
│   │           │   │   │   ├── test_summation.cpython-36.pyc
│   │           │   │   │   ├── test_trig.cpython-36.pyc
│   │           │   │   │   ├── test_visualization.cpython-36.pyc
│   │           │   │   │   └── torture.cpython-36.pyc
│   │           │   │   ├── runtests.py
│   │           │   │   ├── test_basic_ops.py
│   │           │   │   ├── test_bitwise.py
│   │           │   │   ├── test_calculus.py
│   │           │   │   ├── test_compatibility.py
│   │           │   │   ├── test_convert.py
│   │           │   │   ├── test_diff.py
│   │           │   │   ├── test_division.py
│   │           │   │   ├── test_eigen.py
│   │           │   │   ├── test_eigen_symmetric.py
│   │           │   │   ├── test_elliptic.py
│   │           │   │   ├── test_fp.py
│   │           │   │   ├── test_functions2.py
│   │           │   │   ├── test_functions.py
│   │           │   │   ├── test_gammazeta.py
│   │           │   │   ├── test_hp.py
│   │           │   │   ├── test_identify.py
│   │           │   │   ├── test_interval.py
│   │           │   │   ├── test_levin.py
│   │           │   │   ├── test_linalg.py
│   │           │   │   ├── test_matrices.py
│   │           │   │   ├── test_mpmath.py
│   │           │   │   ├── test_ode.py
│   │           │   │   ├── test_pickle.py
│   │           │   │   ├── test_power.py
│   │           │   │   ├── test_quad.py
│   │           │   │   ├── test_rootfinding.py
│   │           │   │   ├── test_special.py
│   │           │   │   ├── test_str.py
│   │           │   │   ├── test_summation.py
│   │           │   │   ├── test_trig.py
│   │           │   │   ├── test_visualization.py
│   │           │   │   └── torture.py
│   │           │   ├── usertools.py
│   │           │   └── visualization.py
│   │           ├── mpmath-1.1.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── nbconvert
│   │           │   ├── exporters
│   │           │   │   ├── asciidoc.py
│   │           │   │   ├── base.py
│   │           │   │   ├── exporter_locator.py
│   │           │   │   ├── exporter.py
│   │           │   │   ├── export.py
│   │           │   │   ├── html.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── latex.py
│   │           │   │   ├── markdown.py
│   │           │   │   ├── notebook.py
│   │           │   │   ├── pdf.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── asciidoc.cpython-36.pyc
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── export.cpython-36.pyc
│   │           │   │   │   ├── exporter.cpython-36.pyc
│   │           │   │   │   ├── exporter_locator.cpython-36.pyc
│   │           │   │   │   ├── html.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── latex.cpython-36.pyc
│   │           │   │   │   ├── markdown.cpython-36.pyc
│   │           │   │   │   ├── notebook.cpython-36.pyc
│   │           │   │   │   ├── pdf.cpython-36.pyc
│   │           │   │   │   ├── python.cpython-36.pyc
│   │           │   │   │   ├── rst.cpython-36.pyc
│   │           │   │   │   ├── script.cpython-36.pyc
│   │           │   │   │   ├── slides.cpython-36.pyc
│   │           │   │   │   └── templateexporter.cpython-36.pyc
│   │           │   │   ├── python.py
│   │           │   │   ├── rst.py
│   │           │   │   ├── script.py
│   │           │   │   ├── slides.py
│   │           │   │   ├── templateexporter.py
│   │           │   │   └── tests
│   │           │   │       ├── base.py
│   │           │   │       ├── cheese.py
│   │           │   │       ├── files
│   │           │   │       │   ├── attachment.ipynb
│   │           │   │       │   ├── notebook2.ipynb
│   │           │   │       │   ├── pngmetadata.ipynb
│   │           │   │       │   ├── prompt_numbers.ipynb
│   │           │   │       │   ├── rawtest.ipynb
│   │           │   │       │   └── svg.ipynb
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── base.cpython-36.pyc
│   │           │   │       │   ├── cheese.cpython-36.pyc
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_asciidoc.cpython-36.pyc
│   │           │   │       │   ├── test_export.cpython-36.pyc
│   │           │   │       │   ├── test_exporter.cpython-36.pyc
│   │           │   │       │   ├── test_html.cpython-36.pyc
│   │           │   │       │   ├── test_latex.cpython-36.pyc
│   │           │   │       │   ├── test_markdown.cpython-36.pyc
│   │           │   │       │   ├── test_notebook.cpython-36.pyc
│   │           │   │       │   ├── test_pdf.cpython-36.pyc
│   │           │   │       │   ├── test_python.cpython-36.pyc
│   │           │   │       │   ├── test_rst.cpython-36.pyc
│   │           │   │       │   ├── test_script.cpython-36.pyc
│   │           │   │       │   ├── test_slides.cpython-36.pyc
│   │           │   │       │   └── test_templateexporter.cpython-36.pyc
│   │           │   │       ├── test_asciidoc.py
│   │           │   │       ├── test_exporter.py
│   │           │   │       ├── test_export.py
│   │           │   │       ├── test_html.py
│   │           │   │       ├── test_latex.py
│   │           │   │       ├── test_markdown.py
│   │           │   │       ├── test_notebook.py
│   │           │   │       ├── test_pdf.py
│   │           │   │       ├── test_python.py
│   │           │   │       ├── test_rst.py
│   │           │   │       ├── test_script.py
│   │           │   │       ├── test_slides.py
│   │           │   │       └── test_templateexporter.py
│   │           │   ├── filters
│   │           │   │   ├── ansi.py
│   │           │   │   ├── citation.py
│   │           │   │   ├── datatypefilter.py
│   │           │   │   ├── filter_links.py
│   │           │   │   ├── highlight.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── latex.py
│   │           │   │   ├── markdown_mistune.py
│   │           │   │   ├── markdown.py
│   │           │   │   ├── metadata.py
│   │           │   │   ├── pandoc.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── ansi.cpython-36.pyc
│   │           │   │   │   ├── citation.cpython-36.pyc
│   │           │   │   │   ├── datatypefilter.cpython-36.pyc
│   │           │   │   │   ├── filter_links.cpython-36.pyc
│   │           │   │   │   ├── highlight.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── latex.cpython-36.pyc
│   │           │   │   │   ├── markdown.cpython-36.pyc
│   │           │   │   │   ├── markdown_mistune.cpython-36.pyc
│   │           │   │   │   ├── metadata.cpython-36.pyc
│   │           │   │   │   ├── pandoc.cpython-36.pyc
│   │           │   │   │   └── strings.cpython-36.pyc
│   │           │   │   ├── strings.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_ansi.cpython-36.pyc
│   │           │   │       │   ├── test_citation.cpython-36.pyc
│   │           │   │       │   ├── test_datatypefilter.cpython-36.pyc
│   │           │   │       │   ├── test_highlight.cpython-36.pyc
│   │           │   │       │   ├── test_latex.cpython-36.pyc
│   │           │   │       │   ├── test_markdown.cpython-36.pyc
│   │           │   │       │   ├── test_metadata.cpython-36.pyc
│   │           │   │       │   └── test_strings.cpython-36.pyc
│   │           │   │       ├── test_ansi.py
│   │           │   │       ├── test_citation.py
│   │           │   │       ├── test_datatypefilter.py
│   │           │   │       ├── test_highlight.py
│   │           │   │       ├── test_latex.py
│   │           │   │       ├── test_markdown.py
│   │           │   │       ├── test_metadata.py
│   │           │   │       └── test_strings.py
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── nbconvertapp.py
│   │           │   ├── postprocessors
│   │           │   │   ├── base.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── serve.cpython-36.pyc
│   │           │   │   ├── serve.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   └── test_serve.cpython-36.pyc
│   │           │   │       └── test_serve.py
│   │           │   ├── preprocessors
│   │           │   │   ├── base.py
│   │           │   │   ├── clearmetadata.py
│   │           │   │   ├── clearoutput.py
│   │           │   │   ├── coalescestreams.py
│   │           │   │   ├── convertfigures.py
│   │           │   │   ├── csshtmlheader.py
│   │           │   │   ├── execute.py
│   │           │   │   ├── extractoutput.py
│   │           │   │   ├── highlightmagics.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── latex.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── clearmetadata.cpython-36.pyc
│   │           │   │   │   ├── clearoutput.cpython-36.pyc
│   │           │   │   │   ├── coalescestreams.cpython-36.pyc
│   │           │   │   │   ├── convertfigures.cpython-36.pyc
│   │           │   │   │   ├── csshtmlheader.cpython-36.pyc
│   │           │   │   │   ├── execute.cpython-36.pyc
│   │           │   │   │   ├── extractoutput.cpython-36.pyc
│   │           │   │   │   ├── highlightmagics.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── latex.cpython-36.pyc
│   │           │   │   │   ├── regexremove.cpython-36.pyc
│   │           │   │   │   ├── sanitize.cpython-36.pyc
│   │           │   │   │   ├── svg2pdf.cpython-36.pyc
│   │           │   │   │   └── tagremove.cpython-36.pyc
│   │           │   │   ├── regexremove.py
│   │           │   │   ├── sanitize.py
│   │           │   │   ├── svg2pdf.py
│   │           │   │   ├── tagremove.py
│   │           │   │   └── tests
│   │           │   │       ├── base.py
│   │           │   │       ├── fake_kernelmanager.py
│   │           │   │       ├── files
│   │           │   │       │   ├── Clear Output.ipynb
│   │           │   │       │   ├── Disable Stdin.ipynb
│   │           │   │       │   ├── Empty Cell.ipynb
│   │           │   │       │   ├── Factorials.ipynb
│   │           │   │       │   ├── HelloWorld.ipynb
│   │           │   │       │   ├── Inline Image.ipynb
│   │           │   │       │   ├── Interrupt-IPY6.ipynb
│   │           │   │       │   ├── Interrupt.ipynb
│   │           │   │       │   ├── JupyterWidgets.ipynb
│   │           │   │       │   ├── python.png
│   │           │   │       │   ├── Skip Exceptions-IPY6.ipynb
│   │           │   │       │   ├── Skip Exceptions.ipynb
│   │           │   │       │   ├── Skip Exceptions with Cell Tags-IPY6.ipynb
│   │           │   │       │   ├── Skip Exceptions with Cell Tags.ipynb
│   │           │   │       │   ├── SVG.ipynb
│   │           │   │       │   ├── Unicode.ipynb
│   │           │   │       │   ├── UnicodePy3.ipynb
│   │           │   │       │   └── update-display-id.ipynb
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── base.cpython-36.pyc
│   │           │   │       │   ├── fake_kernelmanager.cpython-36.pyc
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_clearmetadata.cpython-36.pyc
│   │           │   │       │   ├── test_clearoutput.cpython-36.pyc
│   │           │   │       │   ├── test_coalescestreams.cpython-36.pyc
│   │           │   │       │   ├── test_csshtmlheader.cpython-36.pyc
│   │           │   │       │   ├── test_execute.cpython-36.pyc
│   │           │   │       │   ├── test_extractoutput.cpython-36.pyc
│   │           │   │       │   ├── test_highlightmagics.cpython-36.pyc
│   │           │   │       │   ├── test_latex.cpython-36.pyc
│   │           │   │       │   ├── test_regexremove.cpython-36.pyc
│   │           │   │       │   ├── test_sanitize.cpython-36.pyc
│   │           │   │       │   ├── test_svg2pdf.cpython-36.pyc
│   │           │   │       │   └── test_tagremove.cpython-36.pyc
│   │           │   │       ├── test_clearmetadata.py
│   │           │   │       ├── test_clearoutput.py
│   │           │   │       ├── test_coalescestreams.py
│   │           │   │       ├── test_csshtmlheader.py
│   │           │   │       ├── test_execute.py
│   │           │   │       ├── test_extractoutput.py
│   │           │   │       ├── test_highlightmagics.py
│   │           │   │       ├── test_latex.py
│   │           │   │       ├── test_regexremove.py
│   │           │   │       ├── test_sanitize.py
│   │           │   │       ├── test_svg2pdf.py
│   │           │   │       └── test_tagremove.py
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── __main__.cpython-36.pyc
│   │           │   │   ├── nbconvertapp.cpython-36.pyc
│   │           │   │   └── _version.cpython-36.pyc
│   │           │   ├── resources
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   └── style.min.css
│   │           │   ├── templates
│   │           │   │   ├── asciidoc.tpl
│   │           │   │   ├── html
│   │           │   │   │   ├── basic.tpl
│   │           │   │   │   ├── full.tpl
│   │           │   │   │   ├── mathjax.tpl
│   │           │   │   │   └── slides_reveal.tpl
│   │           │   │   ├── latex
│   │           │   │   │   ├── article.tplx
│   │           │   │   │   ├── base.tplx
│   │           │   │   │   ├── document_contents.tplx
│   │           │   │   │   ├── report.tplx
│   │           │   │   │   ├── skeleton
│   │           │   │   │   │   ├── display_priority.tplx
│   │           │   │   │   │   └── null.tplx
│   │           │   │   │   ├── style_bw_ipython.tplx
│   │           │   │   │   ├── style_bw_python.tplx
│   │           │   │   │   ├── style_ipython.tplx
│   │           │   │   │   ├── style_jupyter.tplx
│   │           │   │   │   └── style_python.tplx
│   │           │   │   ├── markdown.tpl
│   │           │   │   ├── python.tpl
│   │           │   │   ├── README.md
│   │           │   │   ├── rst.tpl
│   │           │   │   ├── script.tpl
│   │           │   │   └── skeleton
│   │           │   │       ├── display_priority.tpl
│   │           │   │       ├── null.tpl
│   │           │   │       └── README.md
│   │           │   ├── tests
│   │           │   │   ├── base.py
│   │           │   │   ├── exporter_entrypoint
│   │           │   │   │   ├── eptest-0.1.dist-info
│   │           │   │   │   │   └── entry_points.txt
│   │           │   │   │   ├── eptest.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       └── eptest.cpython-36.pyc
│   │           │   │   ├── fake_exporters.py
│   │           │   │   ├── files
│   │           │   │   │   ├── containerized_deployments.jpeg
│   │           │   │   │   ├── hello.py
│   │           │   │   │   ├── jupyter_nbconvert_config.py
│   │           │   │   │   ├── latex-linked-image.ipynb
│   │           │   │   │   ├── markdown_display_priority.ipynb
│   │           │   │   │   ├── notebook1.ipynb
│   │           │   │   │   ├── notebook2.ipynb
│   │           │   │   │   ├── notebook3_with_errors.ipynb
│   │           │   │   │   ├── notebook4_jpeg.ipynb
│   │           │   │   │   ├── notebook_jl.ipynb
│   │           │   │   │   ├── override.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── hello.cpython-36.pyc
│   │           │   │   │   │   ├── jupyter_nbconvert_config.cpython-36.pyc
│   │           │   │   │   │   └── override.cpython-36.pyc
│   │           │   │   │   ├── testimage.png
│   │           │   │   │   └── Widget_List.ipynb
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── fake_exporters.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── test_nbconvertapp.cpython-36.pyc
│   │           │   │   │   └── utils.cpython-36.pyc
│   │           │   │   ├── test_nbconvertapp.py
│   │           │   │   └── utils.py
│   │           │   ├── utils
│   │           │   │   ├── base.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── io.py
│   │           │   │   ├── lexers.py
│   │           │   │   ├── pandoc.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── exceptions.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── io.cpython-36.pyc
│   │           │   │   │   ├── lexers.cpython-36.pyc
│   │           │   │   │   ├── pandoc.cpython-36.pyc
│   │           │   │   │   └── version.cpython-36.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_io.cpython-36.pyc
│   │           │   │   │   │   ├── test_pandoc.cpython-36.pyc
│   │           │   │   │   │   └── test_version.cpython-36.pyc
│   │           │   │   │   ├── test_io.py
│   │           │   │   │   ├── test_pandoc.py
│   │           │   │   │   └── test_version.py
│   │           │   │   └── version.py
│   │           │   ├── _version.py
│   │           │   └── writers
│   │           │       ├── base.py
│   │           │       ├── debug.py
│   │           │       ├── files.py
│   │           │       ├── __init__.py
│   │           │       ├── __pycache__
│   │           │       │   ├── base.cpython-36.pyc
│   │           │       │   ├── debug.cpython-36.pyc
│   │           │       │   ├── files.cpython-36.pyc
│   │           │       │   ├── __init__.cpython-36.pyc
│   │           │       │   └── stdout.cpython-36.pyc
│   │           │       ├── stdout.py
│   │           │       └── tests
│   │           │           ├── __init__.py
│   │           │           ├── __pycache__
│   │           │           │   ├── __init__.cpython-36.pyc
│   │           │           │   ├── test_debug.cpython-36.pyc
│   │           │           │   ├── test_files.cpython-36.pyc
│   │           │           │   └── test_stdout.cpython-36.pyc
│   │           │           ├── test_debug.py
│   │           │           ├── test_files.py
│   │           │           └── test_stdout.py
│   │           ├── nbconvert-5.5.0.dist-info
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── nbformat
│   │           │   ├── converter.py
│   │           │   ├── current.py
│   │           │   ├── __init__.py
│   │           │   ├── notebooknode.py
│   │           │   ├── __pycache__
│   │           │   │   ├── converter.cpython-36.pyc
│   │           │   │   ├── current.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── notebooknode.cpython-36.pyc
│   │           │   │   ├── reader.cpython-36.pyc
│   │           │   │   ├── sentinel.cpython-36.pyc
│   │           │   │   ├── sign.cpython-36.pyc
│   │           │   │   ├── validator.cpython-36.pyc
│   │           │   │   └── _version.cpython-36.pyc
│   │           │   ├── reader.py
│   │           │   ├── sentinel.py
│   │           │   ├── sign.py
│   │           │   ├── tests
│   │           │   │   ├── base.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── invalid.ipynb
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── test_api.cpython-36.pyc
│   │           │   │   │   ├── test_convert.cpython-36.pyc
│   │           │   │   │   ├── test_reader.cpython-36.pyc
│   │           │   │   │   ├── test_sign.cpython-36.pyc
│   │           │   │   │   └── test_validator.cpython-36.pyc
│   │           │   │   ├── test2.ipynb
│   │           │   │   ├── test3.ipynb
│   │           │   │   ├── test4custom.ipynb
│   │           │   │   ├── test4docinfo.ipynb
│   │           │   │   ├── test4.ipynb
│   │           │   │   ├── test4jupyter_metadata.ipynb
│   │           │   │   ├── test4plus.ipynb
│   │           │   │   ├── test_api.py
│   │           │   │   ├── test_convert.py
│   │           │   │   ├── test_reader.py
│   │           │   │   ├── test_sign.py
│   │           │   │   └── test_validator.py
│   │           │   ├── v1
│   │           │   │   ├── convert.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── nbbase.py
│   │           │   │   ├── nbjson.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── convert.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── nbbase.cpython-36.pyc
│   │           │   │   │   ├── nbjson.cpython-36.pyc
│   │           │   │   │   └── rwbase.cpython-36.pyc
│   │           │   │   ├── rwbase.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── nbexamples.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── nbexamples.cpython-36.pyc
│   │           │   │       │   ├── test_json.cpython-36.pyc
│   │           │   │       │   └── test_nbbase.cpython-36.pyc
│   │           │   │       ├── test_json.py
│   │           │   │       └── test_nbbase.py
│   │           │   ├── v2
│   │           │   │   ├── convert.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── nbbase.py
│   │           │   │   ├── nbjson.py
│   │           │   │   ├── nbpy.py
│   │           │   │   ├── nbxml.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── convert.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── nbbase.cpython-36.pyc
│   │           │   │   │   ├── nbjson.cpython-36.pyc
│   │           │   │   │   ├── nbpy.cpython-36.pyc
│   │           │   │   │   ├── nbxml.cpython-36.pyc
│   │           │   │   │   └── rwbase.cpython-36.pyc
│   │           │   │   ├── rwbase.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── nbexamples.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── nbexamples.cpython-36.pyc
│   │           │   │       │   ├── test_json.cpython-36.pyc
│   │           │   │       │   ├── test_nbbase.cpython-36.pyc
│   │           │   │       │   └── test_nbpy.cpython-36.pyc
│   │           │   │       ├── test_json.py
│   │           │   │       ├── test_nbbase.py
│   │           │   │       └── test_nbpy.py
│   │           │   ├── v3
│   │           │   │   ├── convert.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── nbbase.py
│   │           │   │   ├── nbformat.v3.schema.json
│   │           │   │   ├── nbjson.py
│   │           │   │   ├── nbpy.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── convert.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── nbbase.cpython-36.pyc
│   │           │   │   │   ├── nbjson.cpython-36.pyc
│   │           │   │   │   ├── nbpy.cpython-36.pyc
│   │           │   │   │   └── rwbase.cpython-36.pyc
│   │           │   │   ├── rwbase.py
│   │           │   │   └── tests
│   │           │   │       ├── formattest.py
│   │           │   │       ├── __init__.py
│   │           │   │       ├── nbexamples.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── formattest.cpython-36.pyc
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── nbexamples.cpython-36.pyc
│   │           │   │       │   ├── test_json.cpython-36.pyc
│   │           │   │       │   ├── test_misc.cpython-36.pyc
│   │           │   │       │   ├── test_nbbase.cpython-36.pyc
│   │           │   │       │   └── test_nbpy.cpython-36.pyc
│   │           │   │       ├── test_json.py
│   │           │   │       ├── test_misc.py
│   │           │   │       ├── test_nbbase.py
│   │           │   │       └── test_nbpy.py
│   │           │   ├── v4
│   │           │   │   ├── convert.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── nbbase.py
│   │           │   │   ├── nbformat.v4.schema.json
│   │           │   │   ├── nbjson.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── convert.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── nbbase.cpython-36.pyc
│   │           │   │   │   ├── nbjson.cpython-36.pyc
│   │           │   │   │   └── rwbase.cpython-36.pyc
│   │           │   │   ├── rwbase.py
│   │           │   │   └── tests
│   │           │   │       ├── formattest.py
│   │           │   │       ├── __init__.py
│   │           │   │       ├── nbexamples.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── formattest.cpython-36.pyc
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── nbexamples.cpython-36.pyc
│   │           │   │       │   ├── test_convert.cpython-36.pyc
│   │           │   │       │   ├── test_json.cpython-36.pyc
│   │           │   │       │   ├── test_nbbase.cpython-36.pyc
│   │           │   │       │   └── test_validate.cpython-36.pyc
│   │           │   │       ├── test_convert.py
│   │           │   │       ├── test_json.py
│   │           │   │       ├── test_nbbase.py
│   │           │   │       └── test_validate.py
│   │           │   ├── validator.py
│   │           │   └── _version.py
│   │           ├── nbformat-4.4.0.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── nose
│   │           │   ├── case.py
│   │           │   ├── commands.py
│   │           │   ├── config.py
│   │           │   ├── core.py
│   │           │   ├── exc.py
│   │           │   ├── ext
│   │           │   │   ├── dtcompat.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── dtcompat.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── failure.py
│   │           │   ├── importer.py
│   │           │   ├── __init__.py
│   │           │   ├── inspector.py
│   │           │   ├── loader.py
│   │           │   ├── __main__.py
│   │           │   ├── plugins
│   │           │   │   ├── allmodules.py
│   │           │   │   ├── attrib.py
│   │           │   │   ├── base.py
│   │           │   │   ├── builtin.py
│   │           │   │   ├── capture.py
│   │           │   │   ├── collect.py
│   │           │   │   ├── cover.py
│   │           │   │   ├── debug.py
│   │           │   │   ├── deprecated.py
│   │           │   │   ├── doctests.py
│   │           │   │   ├── errorclass.py
│   │           │   │   ├── failuredetail.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── isolate.py
│   │           │   │   ├── logcapture.py
│   │           │   │   ├── manager.py
│   │           │   │   ├── multiprocess.py
│   │           │   │   ├── plugintest.py
│   │           │   │   ├── prof.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── allmodules.cpython-36.pyc
│   │           │   │   │   ├── attrib.cpython-36.pyc
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── builtin.cpython-36.pyc
│   │           │   │   │   ├── capture.cpython-36.pyc
│   │           │   │   │   ├── collect.cpython-36.pyc
│   │           │   │   │   ├── cover.cpython-36.pyc
│   │           │   │   │   ├── debug.cpython-36.pyc
│   │           │   │   │   ├── deprecated.cpython-36.pyc
│   │           │   │   │   ├── doctests.cpython-36.pyc
│   │           │   │   │   ├── errorclass.cpython-36.pyc
│   │           │   │   │   ├── failuredetail.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── isolate.cpython-36.pyc
│   │           │   │   │   ├── logcapture.cpython-36.pyc
│   │           │   │   │   ├── manager.cpython-36.pyc
│   │           │   │   │   ├── multiprocess.cpython-36.pyc
│   │           │   │   │   ├── plugintest.cpython-36.pyc
│   │           │   │   │   ├── prof.cpython-36.pyc
│   │           │   │   │   ├── skip.cpython-36.pyc
│   │           │   │   │   ├── testid.cpython-36.pyc
│   │           │   │   │   └── xunit.cpython-36.pyc
│   │           │   │   ├── skip.py
│   │           │   │   ├── testid.py
│   │           │   │   └── xunit.py
│   │           │   ├── proxy.py
│   │           │   ├── __pycache__
│   │           │   │   ├── case.cpython-36.pyc
│   │           │   │   ├── commands.cpython-36.pyc
│   │           │   │   ├── config.cpython-36.pyc
│   │           │   │   ├── core.cpython-36.pyc
│   │           │   │   ├── exc.cpython-36.pyc
│   │           │   │   ├── failure.cpython-36.pyc
│   │           │   │   ├── importer.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── inspector.cpython-36.pyc
│   │           │   │   ├── loader.cpython-36.pyc
│   │           │   │   ├── __main__.cpython-36.pyc
│   │           │   │   ├── proxy.cpython-36.pyc
│   │           │   │   ├── pyversion.cpython-36.pyc
│   │           │   │   ├── result.cpython-36.pyc
│   │           │   │   ├── selector.cpython-36.pyc
│   │           │   │   ├── suite.cpython-36.pyc
│   │           │   │   ├── twistedtools.cpython-36.pyc
│   │           │   │   └── util.cpython-36.pyc
│   │           │   ├── pyversion.py
│   │           │   ├── result.py
│   │           │   ├── selector.py
│   │           │   ├── sphinx
│   │           │   │   ├── __init__.py
│   │           │   │   ├── pluginopts.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       └── pluginopts.cpython-36.pyc
│   │           │   ├── suite.py
│   │           │   ├── tools
│   │           │   │   ├── __init__.py
│   │           │   │   ├── nontrivial.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── nontrivial.cpython-36.pyc
│   │           │   │   │   └── trivial.cpython-36.pyc
│   │           │   │   └── trivial.py
│   │           │   ├── twistedtools.py
│   │           │   ├── usage.txt
│   │           │   └── util.py
│   │           ├── nose-1.3.7.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── notebook
│   │           │   ├── auth
│   │           │   │   ├── __init__.py
│   │           │   │   ├── login.py
│   │           │   │   ├── logout.py
│   │           │   │   ├── __main__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── login.cpython-36.pyc
│   │           │   │   │   ├── logout.cpython-36.pyc
│   │           │   │   │   ├── __main__.cpython-36.pyc
│   │           │   │   │   └── security.cpython-36.pyc
│   │           │   │   ├── security.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_login.cpython-36.pyc
│   │           │   │       │   └── test_security.cpython-36.pyc
│   │           │   │       ├── test_login.py
│   │           │   │       └── test_security.py
│   │           │   ├── base
│   │           │   │   ├── handlers.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── handlers.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── zmqhandlers.cpython-36.pyc
│   │           │   │   └── zmqhandlers.py
│   │           │   ├── bundler
│   │           │   │   ├── bundlerextensions.py
│   │           │   │   ├── handlers.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __main__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── bundlerextensions.cpython-36.pyc
│   │           │   │   │   ├── handlers.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── __main__.cpython-36.pyc
│   │           │   │   │   ├── tarball_bundler.cpython-36.pyc
│   │           │   │   │   ├── tools.cpython-36.pyc
│   │           │   │   │   └── zip_bundler.cpython-36.pyc
│   │           │   │   ├── tarball_bundler.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_bundler_api.cpython-36.pyc
│   │           │   │   │   │   ├── test_bundlerextension.cpython-36.pyc
│   │           │   │   │   │   └── test_bundler_tools.cpython-36.pyc
│   │           │   │   │   ├── resources
│   │           │   │   │   │   ├── another_subdir
│   │           │   │   │   │   │   └── test_file.txt
│   │           │   │   │   │   ├── empty.ipynb
│   │           │   │   │   │   └── subdir
│   │           │   │   │   │       ├── subsubdir
│   │           │   │   │   │       │   └── .gitkeep
│   │           │   │   │   │       └── test_file.txt
│   │           │   │   │   ├── test_bundler_api.py
│   │           │   │   │   ├── test_bundlerextension.py
│   │           │   │   │   └── test_bundler_tools.py
│   │           │   │   ├── tools.py
│   │           │   │   └── zip_bundler.py
│   │           │   ├── config_manager.py
│   │           │   ├── edit
│   │           │   │   ├── handlers.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── handlers.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── extensions.py
│   │           │   ├── files
│   │           │   │   ├── handlers.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── handlers.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── i18n
│   │           │   │   ├── fr_FR
│   │           │   │   │   └── LC_MESSAGES
│   │           │   │   │       ├── nbjs.json
│   │           │   │   │       ├── nbjs.po
│   │           │   │   │       ├── nbui.mo
│   │           │   │   │       ├── nbui.po
│   │           │   │   │       ├── notebook.mo
│   │           │   │   │       └── notebook.po
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   └── zh_CN
│   │           │   │       └── LC_MESSAGES
│   │           │   │           ├── nbjs.json
│   │           │   │           ├── nbjs.po
│   │           │   │           ├── nbui.mo
│   │           │   │           ├── nbui.po
│   │           │   │           ├── notebook.mo
│   │           │   │           └── notebook.po
│   │           │   ├── __init__.py
│   │           │   ├── jstest.py
│   │           │   ├── kernelspecs
│   │           │   │   ├── handlers.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── handlers.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── log.py
│   │           │   ├── __main__.py
│   │           │   ├── metrics.py
│   │           │   ├── nbconvert
│   │           │   │   ├── handlers.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── handlers.cpython-36.pyc
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   └── test_nbconvert_handlers.cpython-36.pyc
│   │           │   │       └── test_nbconvert_handlers.py
│   │           │   ├── nbextensions.py
│   │           │   ├── notebook
│   │           │   │   ├── handlers.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── handlers.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── notebookapp.py
│   │           │   ├── __pycache__
│   │           │   │   ├── config_manager.cpython-36.pyc
│   │           │   │   ├── extensions.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── jstest.cpython-36.pyc
│   │           │   │   ├── log.cpython-36.pyc
│   │           │   │   ├── __main__.cpython-36.pyc
│   │           │   │   ├── metrics.cpython-36.pyc
│   │           │   │   ├── nbextensions.cpython-36.pyc
│   │           │   │   ├── notebookapp.cpython-36.pyc
│   │           │   │   ├── serverextensions.cpython-36.pyc
│   │           │   │   ├── _sysinfo.cpython-36.pyc
│   │           │   │   ├── transutils.cpython-36.pyc
│   │           │   │   ├── _tz.cpython-36.pyc
│   │           │   │   ├── utils.cpython-36.pyc
│   │           │   │   └── _version.cpython-36.pyc
│   │           │   ├── serverextensions.py
│   │           │   ├── services
│   │           │   │   ├── api
│   │           │   │   │   ├── api.yaml
│   │           │   │   │   ├── handlers.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── handlers.cpython-36.pyc
│   │           │   │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   └── test_api.cpython-36.pyc
│   │           │   │   │       └── test_api.py
│   │           │   │   ├── config
│   │           │   │   │   ├── handlers.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── manager.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── handlers.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── manager.cpython-36.pyc
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   └── test_config_api.cpython-36.pyc
│   │           │   │   │       └── test_config_api.py
│   │           │   │   ├── contents
│   │           │   │   │   ├── checkpoints.py
│   │           │   │   │   ├── filecheckpoints.py
│   │           │   │   │   ├── fileio.py
│   │           │   │   │   ├── filemanager.py
│   │           │   │   │   ├── handlers.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── largefilemanager.py
│   │           │   │   │   ├── manager.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── checkpoints.cpython-36.pyc
│   │           │   │   │   │   ├── filecheckpoints.cpython-36.pyc
│   │           │   │   │   │   ├── fileio.cpython-36.pyc
│   │           │   │   │   │   ├── filemanager.cpython-36.pyc
│   │           │   │   │   │   ├── handlers.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── largefilemanager.cpython-36.pyc
│   │           │   │   │   │   └── manager.cpython-36.pyc
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_contents_api.cpython-36.pyc
│   │           │   │   │       │   ├── test_fileio.cpython-36.pyc
│   │           │   │   │       │   ├── test_largefilemanager.cpython-36.pyc
│   │           │   │   │       │   └── test_manager.cpython-36.pyc
│   │           │   │   │       ├── test_contents_api.py
│   │           │   │   │       ├── test_fileio.py
│   │           │   │   │       ├── test_largefilemanager.py
│   │           │   │   │       └── test_manager.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── kernels
│   │           │   │   │   ├── handlers.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── kernelmanager.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── handlers.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── kernelmanager.cpython-36.pyc
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   └── test_kernels_api.cpython-36.pyc
│   │           │   │   │       └── test_kernels_api.py
│   │           │   │   ├── kernelspecs
│   │           │   │   │   ├── handlers.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── handlers.cpython-36.pyc
│   │           │   │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   └── test_kernelspecs_api.cpython-36.pyc
│   │           │   │   │       └── test_kernelspecs_api.py
│   │           │   │   ├── nbconvert
│   │           │   │   │   ├── handlers.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── handlers.cpython-36.pyc
│   │           │   │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   └── test_nbconvert_api.cpython-36.pyc
│   │           │   │   │       └── test_nbconvert_api.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── shutdown.cpython-36.pyc
│   │           │   │   ├── security
│   │           │   │   │   ├── handlers.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── handlers.cpython-36.pyc
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   ├── sessions
│   │           │   │   │   ├── handlers.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── handlers.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── sessionmanager.cpython-36.pyc
│   │           │   │   │   ├── sessionmanager.py
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_sessionmanager.cpython-36.pyc
│   │           │   │   │       │   └── test_sessions_api.cpython-36.pyc
│   │           │   │   │       ├── test_sessionmanager.py
│   │           │   │   │       └── test_sessions_api.py
│   │           │   │   └── shutdown.py
│   │           │   ├── static
│   │           │   │   ├── auth
│   │           │   │   │   ├── css
│   │           │   │   │   │   └── override.css
│   │           │   │   │   └── js
│   │           │   │   │       ├── loginmain.js
│   │           │   │   │       ├── loginwidget.js
│   │           │   │   │       ├── logoutmain.js
│   │           │   │   │       ├── main.js
│   │           │   │   │       ├── main.min.js
│   │           │   │   │       └── main.min.js.map
│   │           │   │   ├── base
│   │           │   │   │   ├── images
│   │           │   │   │   │   ├── favicon-busy-1.ico
│   │           │   │   │   │   ├── favicon-busy-2.ico
│   │           │   │   │   │   ├── favicon-busy-3.ico
│   │           │   │   │   │   ├── favicon-file.ico
│   │           │   │   │   │   ├── favicon.ico
│   │           │   │   │   │   ├── favicon-notebook.ico
│   │           │   │   │   │   ├── favicon-terminal.ico
│   │           │   │   │   │   └── logo.png
│   │           │   │   │   └── js
│   │           │   │   │       ├── dialog.js
│   │           │   │   │       ├── events.js
│   │           │   │   │       ├── i18n.js
│   │           │   │   │       ├── keyboard.js
│   │           │   │   │       ├── namespace.js
│   │           │   │   │       ├── notificationarea.js
│   │           │   │   │       ├── notificationwidget.js
│   │           │   │   │       ├── page.js
│   │           │   │   │       ├── promises.js
│   │           │   │   │       ├── security.js
│   │           │   │   │       └── utils.js
│   │           │   │   ├── bidi
│   │           │   │   │   ├── bidi.js
│   │           │   │   │   └── numericshaping.js
│   │           │   │   ├── components
│   │           │   │   │   ├── backbone
│   │           │   │   │   │   └── backbone-min.js
│   │           │   │   │   ├── bootstrap
│   │           │   │   │   │   └── dist
│   │           │   │   │   │       └── js
│   │           │   │   │   │           └── bootstrap.min.js
│   │           │   │   │   ├── bootstrap-tour
│   │           │   │   │   │   └── build
│   │           │   │   │   │       ├── css
│   │           │   │   │   │       │   └── bootstrap-tour.min.css
│   │           │   │   │   │       └── js
│   │           │   │   │   │           └── bootstrap-tour.min.js
│   │           │   │   │   ├── codemirror
│   │           │   │   │   │   ├── addon
│   │           │   │   │   │   │   ├── comment
│   │           │   │   │   │   │   │   ├── comment.js
│   │           │   │   │   │   │   │   └── continuecomment.js
│   │           │   │   │   │   │   ├── dialog
│   │           │   │   │   │   │   │   ├── dialog.css
│   │           │   │   │   │   │   │   └── dialog.js
│   │           │   │   │   │   │   ├── display
│   │           │   │   │   │   │   │   ├── autorefresh.js
│   │           │   │   │   │   │   │   ├── fullscreen.css
│   │           │   │   │   │   │   │   ├── fullscreen.js
│   │           │   │   │   │   │   │   ├── panel.js
│   │           │   │   │   │   │   │   ├── placeholder.js
│   │           │   │   │   │   │   │   └── rulers.js
│   │           │   │   │   │   │   ├── edit
│   │           │   │   │   │   │   │   ├── closebrackets.js
│   │           │   │   │   │   │   │   ├── closetag.js
│   │           │   │   │   │   │   │   ├── continuelist.js
│   │           │   │   │   │   │   │   ├── matchbrackets.js
│   │           │   │   │   │   │   │   ├── matchtags.js
│   │           │   │   │   │   │   │   └── trailingspace.js
│   │           │   │   │   │   │   ├── fold
│   │           │   │   │   │   │   │   ├── brace-fold.js
│   │           │   │   │   │   │   │   ├── comment-fold.js
│   │           │   │   │   │   │   │   ├── foldcode.js
│   │           │   │   │   │   │   │   ├── foldgutter.css
│   │           │   │   │   │   │   │   ├── foldgutter.js
│   │           │   │   │   │   │   │   ├── indent-fold.js
│   │           │   │   │   │   │   │   ├── markdown-fold.js
│   │           │   │   │   │   │   │   └── xml-fold.js
│   │           │   │   │   │   │   ├── hint
│   │           │   │   │   │   │   │   ├── anyword-hint.js
│   │           │   │   │   │   │   │   ├── css-hint.js
│   │           │   │   │   │   │   │   ├── html-hint.js
│   │           │   │   │   │   │   │   ├── javascript-hint.js
│   │           │   │   │   │   │   │   ├── show-hint.css
│   │           │   │   │   │   │   │   ├── show-hint.js
│   │           │   │   │   │   │   │   ├── sql-hint.js
│   │           │   │   │   │   │   │   └── xml-hint.js
│   │           │   │   │   │   │   ├── lint
│   │           │   │   │   │   │   │   ├── coffeescript-lint.js
│   │           │   │   │   │   │   │   ├── css-lint.js
│   │           │   │   │   │   │   │   ├── html-lint.js
│   │           │   │   │   │   │   │   ├── javascript-lint.js
│   │           │   │   │   │   │   │   ├── json-lint.js
│   │           │   │   │   │   │   │   ├── lint.css
│   │           │   │   │   │   │   │   ├── lint.js
│   │           │   │   │   │   │   │   └── yaml-lint.js
│   │           │   │   │   │   │   ├── merge
│   │           │   │   │   │   │   │   ├── merge.css
│   │           │   │   │   │   │   │   └── merge.js
│   │           │   │   │   │   │   ├── mode
│   │           │   │   │   │   │   │   ├── loadmode.js
│   │           │   │   │   │   │   │   ├── multiplex.js
│   │           │   │   │   │   │   │   ├── multiplex_test.js
│   │           │   │   │   │   │   │   ├── overlay.js
│   │           │   │   │   │   │   │   └── simple.js
│   │           │   │   │   │   │   ├── runmode
│   │           │   │   │   │   │   │   ├── colorize.js
│   │           │   │   │   │   │   │   ├── runmode.js
│   │           │   │   │   │   │   │   ├── runmode.node.js
│   │           │   │   │   │   │   │   └── runmode-standalone.js
│   │           │   │   │   │   │   ├── scroll
│   │           │   │   │   │   │   │   ├── annotatescrollbar.js
│   │           │   │   │   │   │   │   ├── scrollpastend.js
│   │           │   │   │   │   │   │   ├── simplescrollbars.css
│   │           │   │   │   │   │   │   └── simplescrollbars.js
│   │           │   │   │   │   │   ├── search
│   │           │   │   │   │   │   │   ├── jump-to-line.js
│   │           │   │   │   │   │   │   ├── matchesonscrollbar.css
│   │           │   │   │   │   │   │   ├── matchesonscrollbar.js
│   │           │   │   │   │   │   │   ├── match-highlighter.js
│   │           │   │   │   │   │   │   ├── searchcursor.js
│   │           │   │   │   │   │   │   └── search.js
│   │           │   │   │   │   │   ├── selection
│   │           │   │   │   │   │   │   ├── active-line.js
│   │           │   │   │   │   │   │   ├── mark-selection.js
│   │           │   │   │   │   │   │   └── selection-pointer.js
│   │           │   │   │   │   │   ├── tern
│   │           │   │   │   │   │   │   ├── tern.css
│   │           │   │   │   │   │   │   ├── tern.js
│   │           │   │   │   │   │   │   └── worker.js
│   │           │   │   │   │   │   └── wrap
│   │           │   │   │   │   │       └── hardwrap.js
│   │           │   │   │   │   ├── keymap
│   │           │   │   │   │   │   ├── emacs.js
│   │           │   │   │   │   │   ├── sublime.js
│   │           │   │   │   │   │   └── vim.js
│   │           │   │   │   │   ├── lib
│   │           │   │   │   │   │   ├── codemirror.css
│   │           │   │   │   │   │   └── codemirror.js
│   │           │   │   │   │   ├── mode
│   │           │   │   │   │   │   ├── apl
│   │           │   │   │   │   │   │   └── apl.js
│   │           │   │   │   │   │   ├── asciiarmor
│   │           │   │   │   │   │   │   └── asciiarmor.js
│   │           │   │   │   │   │   ├── asn.1
│   │           │   │   │   │   │   │   └── asn.1.js
│   │           │   │   │   │   │   ├── asterisk
│   │           │   │   │   │   │   │   └── asterisk.js
│   │           │   │   │   │   │   ├── brainfuck
│   │           │   │   │   │   │   │   └── brainfuck.js
│   │           │   │   │   │   │   ├── clike
│   │           │   │   │   │   │   │   └── clike.js
│   │           │   │   │   │   │   ├── clojure
│   │           │   │   │   │   │   │   └── clojure.js
│   │           │   │   │   │   │   ├── cmake
│   │           │   │   │   │   │   │   └── cmake.js
│   │           │   │   │   │   │   ├── cobol
│   │           │   │   │   │   │   │   └── cobol.js
│   │           │   │   │   │   │   ├── coffeescript
│   │           │   │   │   │   │   │   └── coffeescript.js
│   │           │   │   │   │   │   ├── commonlisp
│   │           │   │   │   │   │   │   └── commonlisp.js
│   │           │   │   │   │   │   ├── crystal
│   │           │   │   │   │   │   │   └── crystal.js
│   │           │   │   │   │   │   ├── css
│   │           │   │   │   │   │   │   └── css.js
│   │           │   │   │   │   │   ├── cypher
│   │           │   │   │   │   │   │   └── cypher.js
│   │           │   │   │   │   │   ├── dart
│   │           │   │   │   │   │   │   └── dart.js
│   │           │   │   │   │   │   ├── diff
│   │           │   │   │   │   │   │   └── diff.js
│   │           │   │   │   │   │   ├── django
│   │           │   │   │   │   │   │   └── django.js
│   │           │   │   │   │   │   ├── dockerfile
│   │           │   │   │   │   │   │   └── dockerfile.js
│   │           │   │   │   │   │   ├── dtd
│   │           │   │   │   │   │   │   └── dtd.js
│   │           │   │   │   │   │   ├── dylan
│   │           │   │   │   │   │   │   └── dylan.js
│   │           │   │   │   │   │   ├── ebnf
│   │           │   │   │   │   │   │   └── ebnf.js
│   │           │   │   │   │   │   ├── ecl
│   │           │   │   │   │   │   │   └── ecl.js
│   │           │   │   │   │   │   ├── eiffel
│   │           │   │   │   │   │   │   └── eiffel.js
│   │           │   │   │   │   │   ├── elm
│   │           │   │   │   │   │   │   └── elm.js
│   │           │   │   │   │   │   ├── erlang
│   │           │   │   │   │   │   │   └── erlang.js
│   │           │   │   │   │   │   ├── factor
│   │           │   │   │   │   │   │   └── factor.js
│   │           │   │   │   │   │   ├── fcl
│   │           │   │   │   │   │   │   └── fcl.js
│   │           │   │   │   │   │   ├── forth
│   │           │   │   │   │   │   │   └── forth.js
│   │           │   │   │   │   │   ├── fortran
│   │           │   │   │   │   │   │   └── fortran.js
│   │           │   │   │   │   │   ├── gas
│   │           │   │   │   │   │   │   └── gas.js
│   │           │   │   │   │   │   ├── gfm
│   │           │   │   │   │   │   │   └── gfm.js
│   │           │   │   │   │   │   ├── gherkin
│   │           │   │   │   │   │   │   └── gherkin.js
│   │           │   │   │   │   │   ├── go
│   │           │   │   │   │   │   │   └── go.js
│   │           │   │   │   │   │   ├── groovy
│   │           │   │   │   │   │   │   └── groovy.js
│   │           │   │   │   │   │   ├── haml
│   │           │   │   │   │   │   │   └── haml.js
│   │           │   │   │   │   │   ├── handlebars
│   │           │   │   │   │   │   │   └── handlebars.js
│   │           │   │   │   │   │   ├── haskell
│   │           │   │   │   │   │   │   └── haskell.js
│   │           │   │   │   │   │   ├── haskell-literate
│   │           │   │   │   │   │   │   └── haskell-literate.js
│   │           │   │   │   │   │   ├── haxe
│   │           │   │   │   │   │   │   └── haxe.js
│   │           │   │   │   │   │   ├── htmlembedded
│   │           │   │   │   │   │   │   └── htmlembedded.js
│   │           │   │   │   │   │   ├── htmlmixed
│   │           │   │   │   │   │   │   └── htmlmixed.js
│   │           │   │   │   │   │   ├── http
│   │           │   │   │   │   │   │   └── http.js
│   │           │   │   │   │   │   ├── idl
│   │           │   │   │   │   │   │   └── idl.js
│   │           │   │   │   │   │   ├── javascript
│   │           │   │   │   │   │   │   └── javascript.js
│   │           │   │   │   │   │   ├── jinja2
│   │           │   │   │   │   │   │   └── jinja2.js
│   │           │   │   │   │   │   ├── jsx
│   │           │   │   │   │   │   │   └── jsx.js
│   │           │   │   │   │   │   ├── julia
│   │           │   │   │   │   │   │   └── julia.js
│   │           │   │   │   │   │   ├── livescript
│   │           │   │   │   │   │   │   └── livescript.js
│   │           │   │   │   │   │   ├── lua
│   │           │   │   │   │   │   │   └── lua.js
│   │           │   │   │   │   │   ├── markdown
│   │           │   │   │   │   │   │   └── markdown.js
│   │           │   │   │   │   │   ├── mathematica
│   │           │   │   │   │   │   │   └── mathematica.js
│   │           │   │   │   │   │   ├── mbox
│   │           │   │   │   │   │   │   └── mbox.js
│   │           │   │   │   │   │   ├── meta.js
│   │           │   │   │   │   │   ├── mirc
│   │           │   │   │   │   │   │   └── mirc.js
│   │           │   │   │   │   │   ├── mllike
│   │           │   │   │   │   │   │   └── mllike.js
│   │           │   │   │   │   │   ├── modelica
│   │           │   │   │   │   │   │   └── modelica.js
│   │           │   │   │   │   │   ├── mscgen
│   │           │   │   │   │   │   │   └── mscgen.js
│   │           │   │   │   │   │   ├── mumps
│   │           │   │   │   │   │   │   └── mumps.js
│   │           │   │   │   │   │   ├── nginx
│   │           │   │   │   │   │   │   └── nginx.js
│   │           │   │   │   │   │   ├── nsis
│   │           │   │   │   │   │   │   └── nsis.js
│   │           │   │   │   │   │   ├── ntriples
│   │           │   │   │   │   │   │   └── ntriples.js
│   │           │   │   │   │   │   ├── octave
│   │           │   │   │   │   │   │   └── octave.js
│   │           │   │   │   │   │   ├── oz
│   │           │   │   │   │   │   │   └── oz.js
│   │           │   │   │   │   │   ├── pascal
│   │           │   │   │   │   │   │   └── pascal.js
│   │           │   │   │   │   │   ├── pegjs
│   │           │   │   │   │   │   │   └── pegjs.js
│   │           │   │   │   │   │   ├── perl
│   │           │   │   │   │   │   │   └── perl.js
│   │           │   │   │   │   │   ├── php
│   │           │   │   │   │   │   │   └── php.js
│   │           │   │   │   │   │   ├── pig
│   │           │   │   │   │   │   │   └── pig.js
│   │           │   │   │   │   │   ├── powershell
│   │           │   │   │   │   │   │   └── powershell.js
│   │           │   │   │   │   │   ├── properties
│   │           │   │   │   │   │   │   └── properties.js
│   │           │   │   │   │   │   ├── protobuf
│   │           │   │   │   │   │   │   └── protobuf.js
│   │           │   │   │   │   │   ├── pug
│   │           │   │   │   │   │   │   └── pug.js
│   │           │   │   │   │   │   ├── puppet
│   │           │   │   │   │   │   │   └── puppet.js
│   │           │   │   │   │   │   ├── python
│   │           │   │   │   │   │   │   └── python.js
│   │           │   │   │   │   │   ├── q
│   │           │   │   │   │   │   │   └── q.js
│   │           │   │   │   │   │   ├── r
│   │           │   │   │   │   │   │   └── r.js
│   │           │   │   │   │   │   ├── rpm
│   │           │   │   │   │   │   │   └── rpm.js
│   │           │   │   │   │   │   ├── rst
│   │           │   │   │   │   │   │   └── rst.js
│   │           │   │   │   │   │   ├── ruby
│   │           │   │   │   │   │   │   └── ruby.js
│   │           │   │   │   │   │   ├── rust
│   │           │   │   │   │   │   │   └── rust.js
│   │           │   │   │   │   │   ├── sas
│   │           │   │   │   │   │   │   └── sas.js
│   │           │   │   │   │   │   ├── sass
│   │           │   │   │   │   │   │   └── sass.js
│   │           │   │   │   │   │   ├── scheme
│   │           │   │   │   │   │   │   └── scheme.js
│   │           │   │   │   │   │   ├── shell
│   │           │   │   │   │   │   │   └── shell.js
│   │           │   │   │   │   │   ├── sieve
│   │           │   │   │   │   │   │   └── sieve.js
│   │           │   │   │   │   │   ├── slim
│   │           │   │   │   │   │   │   └── slim.js
│   │           │   │   │   │   │   ├── smalltalk
│   │           │   │   │   │   │   │   └── smalltalk.js
│   │           │   │   │   │   │   ├── smarty
│   │           │   │   │   │   │   │   └── smarty.js
│   │           │   │   │   │   │   ├── solr
│   │           │   │   │   │   │   │   └── solr.js
│   │           │   │   │   │   │   ├── soy
│   │           │   │   │   │   │   │   └── soy.js
│   │           │   │   │   │   │   ├── sparql
│   │           │   │   │   │   │   │   └── sparql.js
│   │           │   │   │   │   │   ├── spreadsheet
│   │           │   │   │   │   │   │   └── spreadsheet.js
│   │           │   │   │   │   │   ├── sql
│   │           │   │   │   │   │   │   └── sql.js
│   │           │   │   │   │   │   ├── stex
│   │           │   │   │   │   │   │   └── stex.js
│   │           │   │   │   │   │   ├── stylus
│   │           │   │   │   │   │   │   └── stylus.js
│   │           │   │   │   │   │   ├── swift
│   │           │   │   │   │   │   │   └── swift.js
│   │           │   │   │   │   │   ├── tcl
│   │           │   │   │   │   │   │   └── tcl.js
│   │           │   │   │   │   │   ├── textile
│   │           │   │   │   │   │   │   └── textile.js
│   │           │   │   │   │   │   ├── tiddlywiki
│   │           │   │   │   │   │   │   ├── tiddlywiki.css
│   │           │   │   │   │   │   │   └── tiddlywiki.js
│   │           │   │   │   │   │   ├── tiki
│   │           │   │   │   │   │   │   ├── tiki.css
│   │           │   │   │   │   │   │   └── tiki.js
│   │           │   │   │   │   │   ├── toml
│   │           │   │   │   │   │   │   └── toml.js
│   │           │   │   │   │   │   ├── tornado
│   │           │   │   │   │   │   │   └── tornado.js
│   │           │   │   │   │   │   ├── troff
│   │           │   │   │   │   │   │   └── troff.js
│   │           │   │   │   │   │   ├── ttcn
│   │           │   │   │   │   │   │   └── ttcn.js
│   │           │   │   │   │   │   ├── ttcn-cfg
│   │           │   │   │   │   │   │   └── ttcn-cfg.js
│   │           │   │   │   │   │   ├── turtle
│   │           │   │   │   │   │   │   └── turtle.js
│   │           │   │   │   │   │   ├── twig
│   │           │   │   │   │   │   │   └── twig.js
│   │           │   │   │   │   │   ├── vb
│   │           │   │   │   │   │   │   └── vb.js
│   │           │   │   │   │   │   ├── vbscript
│   │           │   │   │   │   │   │   └── vbscript.js
│   │           │   │   │   │   │   ├── velocity
│   │           │   │   │   │   │   │   └── velocity.js
│   │           │   │   │   │   │   ├── verilog
│   │           │   │   │   │   │   │   └── verilog.js
│   │           │   │   │   │   │   ├── vhdl
│   │           │   │   │   │   │   │   └── vhdl.js
│   │           │   │   │   │   │   ├── vue
│   │           │   │   │   │   │   │   └── vue.js
│   │           │   │   │   │   │   ├── webidl
│   │           │   │   │   │   │   │   └── webidl.js
│   │           │   │   │   │   │   ├── xml
│   │           │   │   │   │   │   │   └── xml.js
│   │           │   │   │   │   │   ├── xquery
│   │           │   │   │   │   │   │   └── xquery.js
│   │           │   │   │   │   │   ├── yacas
│   │           │   │   │   │   │   │   └── yacas.js
│   │           │   │   │   │   │   ├── yaml
│   │           │   │   │   │   │   │   └── yaml.js
│   │           │   │   │   │   │   ├── yaml-frontmatter
│   │           │   │   │   │   │   │   └── yaml-frontmatter.js
│   │           │   │   │   │   │   └── z80
│   │           │   │   │   │   │       └── z80.js
│   │           │   │   │   │   ├── rollup.config.js
│   │           │   │   │   │   ├── src
│   │           │   │   │   │   │   ├── codemirror.js
│   │           │   │   │   │   │   ├── display
│   │           │   │   │   │   │   │   ├── Display.js
│   │           │   │   │   │   │   │   ├── focus.js
│   │           │   │   │   │   │   │   ├── gutters.js
│   │           │   │   │   │   │   │   ├── highlight_worker.js
│   │           │   │   │   │   │   │   ├── line_numbers.js
│   │           │   │   │   │   │   │   ├── mode_state.js
│   │           │   │   │   │   │   │   ├── operations.js
│   │           │   │   │   │   │   │   ├── scrollbars.js
│   │           │   │   │   │   │   │   ├── scroll_events.js
│   │           │   │   │   │   │   │   ├── scrolling.js
│   │           │   │   │   │   │   │   ├── selection.js
│   │           │   │   │   │   │   │   ├── update_display.js
│   │           │   │   │   │   │   │   ├── update_line.js
│   │           │   │   │   │   │   │   ├── update_lines.js
│   │           │   │   │   │   │   │   └── view_tracking.js
│   │           │   │   │   │   │   ├── edit
│   │           │   │   │   │   │   │   ├── CodeMirror.js
│   │           │   │   │   │   │   │   ├── commands.js
│   │           │   │   │   │   │   │   ├── deleteNearSelection.js
│   │           │   │   │   │   │   │   ├── drop_events.js
│   │           │   │   │   │   │   │   ├── fromTextArea.js
│   │           │   │   │   │   │   │   ├── global_events.js
│   │           │   │   │   │   │   │   ├── key_events.js
│   │           │   │   │   │   │   │   ├── legacy.js
│   │           │   │   │   │   │   │   ├── main.js
│   │           │   │   │   │   │   │   ├── methods.js
│   │           │   │   │   │   │   │   ├── mouse_events.js
│   │           │   │   │   │   │   │   ├── options.js
│   │           │   │   │   │   │   │   └── utils.js
│   │           │   │   │   │   │   ├── input
│   │           │   │   │   │   │   │   ├── ContentEditableInput.js
│   │           │   │   │   │   │   │   ├── indent.js
│   │           │   │   │   │   │   │   ├── input.js
│   │           │   │   │   │   │   │   ├── keymap.js
│   │           │   │   │   │   │   │   ├── keynames.js
│   │           │   │   │   │   │   │   ├── movement.js
│   │           │   │   │   │   │   │   └── TextareaInput.js
│   │           │   │   │   │   │   ├── line
│   │           │   │   │   │   │   │   ├── highlight.js
│   │           │   │   │   │   │   │   ├── line_data.js
│   │           │   │   │   │   │   │   ├── pos.js
│   │           │   │   │   │   │   │   ├── saw_special_spans.js
│   │           │   │   │   │   │   │   ├── spans.js
│   │           │   │   │   │   │   │   └── utils_line.js
│   │           │   │   │   │   │   ├── measurement
│   │           │   │   │   │   │   │   ├── position_measurement.js
│   │           │   │   │   │   │   │   └── widgets.js
│   │           │   │   │   │   │   ├── model
│   │           │   │   │   │   │   │   ├── change_measurement.js
│   │           │   │   │   │   │   │   ├── changes.js
│   │           │   │   │   │   │   │   ├── chunk.js
│   │           │   │   │   │   │   │   ├── Doc.js
│   │           │   │   │   │   │   │   ├── document_data.js
│   │           │   │   │   │   │   │   ├── history.js
│   │           │   │   │   │   │   │   ├── line_widget.js
│   │           │   │   │   │   │   │   ├── mark_text.js
│   │           │   │   │   │   │   │   ├── selection.js
│   │           │   │   │   │   │   │   └── selection_updates.js
│   │           │   │   │   │   │   ├── modes.js
│   │           │   │   │   │   │   └── util
│   │           │   │   │   │   │       ├── bidi.js
│   │           │   │   │   │   │       ├── browser.js
│   │           │   │   │   │   │       ├── dom.js
│   │           │   │   │   │   │       ├── event.js
│   │           │   │   │   │   │       ├── feature_detection.js
│   │           │   │   │   │   │       ├── misc.js
│   │           │   │   │   │   │       ├── operation_group.js
│   │           │   │   │   │   │       └── StringStream.js
│   │           │   │   │   │   └── theme
│   │           │   │   │   │       ├── 3024-day.css
│   │           │   │   │   │       ├── 3024-night.css
│   │           │   │   │   │       ├── abcdef.css
│   │           │   │   │   │       ├── ambiance.css
│   │           │   │   │   │       ├── ambiance-mobile.css
│   │           │   │   │   │       ├── base16-dark.css
│   │           │   │   │   │       ├── base16-light.css
│   │           │   │   │   │       ├── bespin.css
│   │           │   │   │   │       ├── blackboard.css
│   │           │   │   │   │       ├── cobalt.css
│   │           │   │   │   │       ├── colorforth.css
│   │           │   │   │   │       ├── dracula.css
│   │           │   │   │   │       ├── duotone-dark.css
│   │           │   │   │   │       ├── duotone-light.css
│   │           │   │   │   │       ├── eclipse.css
│   │           │   │   │   │       ├── elegant.css
│   │           │   │   │   │       ├── erlang-dark.css
│   │           │   │   │   │       ├── gruvbox-dark.css
│   │           │   │   │   │       ├── hopscotch.css
│   │           │   │   │   │       ├── icecoder.css
│   │           │   │   │   │       ├── idea.css
│   │           │   │   │   │       ├── isotope.css
│   │           │   │   │   │       ├── lesser-dark.css
│   │           │   │   │   │       ├── liquibyte.css
│   │           │   │   │   │       ├── lucario.css
│   │           │   │   │   │       ├── material.css
│   │           │   │   │   │       ├── mbo.css
│   │           │   │   │   │       ├── mdn-like.css
│   │           │   │   │   │       ├── midnight.css
│   │           │   │   │   │       ├── monokai.css
│   │           │   │   │   │       ├── neat.css
│   │           │   │   │   │       ├── neo.css
│   │           │   │   │   │       ├── night.css
│   │           │   │   │   │       ├── oceanic-next.css
│   │           │   │   │   │       ├── panda-syntax.css
│   │           │   │   │   │       ├── paraiso-dark.css
│   │           │   │   │   │       ├── paraiso-light.css
│   │           │   │   │   │       ├── pastel-on-dark.css
│   │           │   │   │   │       ├── railscasts.css
│   │           │   │   │   │       ├── rubyblue.css
│   │           │   │   │   │       ├── seti.css
│   │           │   │   │   │       ├── shadowfox.css
│   │           │   │   │   │       ├── solarized.css
│   │           │   │   │   │       ├── ssms.css
│   │           │   │   │   │       ├── the-matrix.css
│   │           │   │   │   │       ├── tomorrow-night-bright.css
│   │           │   │   │   │       ├── tomorrow-night-eighties.css
│   │           │   │   │   │       ├── ttcn.css
│   │           │   │   │   │       ├── twilight.css
│   │           │   │   │   │       ├── vibrant-ink.css
│   │           │   │   │   │       ├── xq-dark.css
│   │           │   │   │   │       ├── xq-light.css
│   │           │   │   │   │       ├── yeti.css
│   │           │   │   │   │       └── zenburn.css
│   │           │   │   │   ├── es6-promise
│   │           │   │   │   │   ├── promise.js
│   │           │   │   │   │   └── promise.min.js
│   │           │   │   │   ├── font-awesome
│   │           │   │   │   │   ├── css
│   │           │   │   │   │   │   ├── font-awesome.css
│   │           │   │   │   │   │   └── font-awesome.min.css
│   │           │   │   │   │   └── fonts
│   │           │   │   │   │       ├── FontAwesome.otf
│   │           │   │   │   │       ├── fontawesome-webfont.eot
│   │           │   │   │   │       ├── fontawesome-webfont.svg
│   │           │   │   │   │       ├── fontawesome-webfont.ttf
│   │           │   │   │   │       ├── fontawesome-webfont.woff
│   │           │   │   │   │       └── fontawesome-webfont.woff2
│   │           │   │   │   ├── google-caja
│   │           │   │   │   │   └── html-css-sanitizer-minified.js
│   │           │   │   │   ├── jed
│   │           │   │   │   │   └── jed.js
│   │           │   │   │   ├── jquery
│   │           │   │   │   │   └── jquery.min.js
│   │           │   │   │   ├── jquery-typeahead
│   │           │   │   │   │   └── dist
│   │           │   │   │   │       ├── jquery.typeahead.min.css
│   │           │   │   │   │       └── jquery.typeahead.min.js
│   │           │   │   │   ├── jquery-ui
│   │           │   │   │   │   ├── jquery-ui.min.js
│   │           │   │   │   │   └── themes
│   │           │   │   │   │       └── smoothness
│   │           │   │   │   │           ├── images
│   │           │   │   │   │           │   ├── ui-bg_glass_55_fbf9ee_1x400.png
│   │           │   │   │   │           │   ├── ui-bg_glass_65_ffffff_1x400.png
│   │           │   │   │   │           │   ├── ui-bg_glass_75_dadada_1x400.png
│   │           │   │   │   │           │   ├── ui-bg_glass_75_e6e6e6_1x400.png
│   │           │   │   │   │           │   ├── ui-bg_glass_95_fef1ec_1x400.png
│   │           │   │   │   │           │   ├── ui-bg_highlight-soft_75_cccccc_1x100.png
│   │           │   │   │   │           │   ├── ui-icons_222222_256x240.png
│   │           │   │   │   │           │   ├── ui-icons_2e83ff_256x240.png
│   │           │   │   │   │           │   ├── ui-icons_454545_256x240.png
│   │           │   │   │   │           │   ├── ui-icons_888888_256x240.png
│   │           │   │   │   │           │   └── ui-icons_cd0a0a_256x240.png
│   │           │   │   │   │           └── jquery-ui.min.css
│   │           │   │   │   ├── marked
│   │           │   │   │   │   └── lib
│   │           │   │   │   │       └── marked.js
│   │           │   │   │   ├── MathJax
│   │           │   │   │   │   ├── config
│   │           │   │   │   │   │   ├── Safe.js
│   │           │   │   │   │   │   └── TeX-AMS-MML_HTMLorMML-full.js
│   │           │   │   │   │   ├── extensions
│   │           │   │   │   │   │   ├── a11y
│   │           │   │   │   │   │   │   ├── accessibility-menu.js
│   │           │   │   │   │   │   │   ├── auto-collapse.js
│   │           │   │   │   │   │   │   ├── collapsible.js
│   │           │   │   │   │   │   │   ├── explorer.js
│   │           │   │   │   │   │   │   ├── invalid_keypress.mp3
│   │           │   │   │   │   │   │   ├── invalid_keypress.ogg
│   │           │   │   │   │   │   │   ├── mathjax-sre.js
│   │           │   │   │   │   │   │   ├── mathmaps
│   │           │   │   │   │   │   │   │   ├── en
│   │           │   │   │   │   │   │   │   │   ├── functions
│   │           │   │   │   │   │   │   │   │   │   ├── algebra.js
│   │           │   │   │   │   │   │   │   │   │   ├── elementary.js
│   │           │   │   │   │   │   │   │   │   │   ├── hyperbolic.js
│   │           │   │   │   │   │   │   │   │   │   └── trigonometry.js
│   │           │   │   │   │   │   │   │   │   ├── symbols
│   │           │   │   │   │   │   │   │   │   │   ├── greek-capital.js
│   │           │   │   │   │   │   │   │   │   │   ├── greek-mathfonts-bold.js
│   │           │   │   │   │   │   │   │   │   │   ├── greek-mathfonts-italic.js
│   │           │   │   │   │   │   │   │   │   │   ├── greek-mathfonts-sans-serif-bold.js
│   │           │   │   │   │   │   │   │   │   │   ├── greek-scripts.js
│   │           │   │   │   │   │   │   │   │   │   ├── greek-small.js
│   │           │   │   │   │   │   │   │   │   │   ├── greek-symbols.js
│   │           │   │   │   │   │   │   │   │   │   ├── hebrew_letters.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-lower-double-accent.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-lower-normal.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-lower-phonetic.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-lower-single-accent.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-bold-fraktur.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-bold.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-bold-script.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-double-struck.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-fraktur.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-italic.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-monospace.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-sans-serif-bold.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-sans-serif-italic.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-sans-serif.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-script.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-rest.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-upper-double-accent.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-upper-normal.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-upper-single-accent.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_angles.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_arrows.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_characters.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_delimiters.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_digits.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_geometry.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_harpoons.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_non_characters.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_symbols.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_whitespace.js
│   │           │   │   │   │   │   │   │   │   │   └── other_stars.js
│   │           │   │   │   │   │   │   │   │   └── units
│   │           │   │   │   │   │   │   │   │       ├── energy.js
│   │           │   │   │   │   │   │   │   │       ├── length.js
│   │           │   │   │   │   │   │   │   │       ├── memory.js
│   │           │   │   │   │   │   │   │   │       ├── other.js
│   │           │   │   │   │   │   │   │   │       ├── speed.js
│   │           │   │   │   │   │   │   │   │       ├── temperature.js
│   │           │   │   │   │   │   │   │   │       ├── time.js
│   │           │   │   │   │   │   │   │   │       ├── volume.js
│   │           │   │   │   │   │   │   │   │       └── weight.js
│   │           │   │   │   │   │   │   │   ├── es
│   │           │   │   │   │   │   │   │   │   ├── functions
│   │           │   │   │   │   │   │   │   │   │   ├── algebra.js
│   │           │   │   │   │   │   │   │   │   │   ├── elementary.js
│   │           │   │   │   │   │   │   │   │   │   ├── hyperbolic.js
│   │           │   │   │   │   │   │   │   │   │   └── trigonometry.js
│   │           │   │   │   │   │   │   │   │   ├── symbols
│   │           │   │   │   │   │   │   │   │   │   ├── greek-capital.js
│   │           │   │   │   │   │   │   │   │   │   ├── greek-mathfonts-bold.js
│   │           │   │   │   │   │   │   │   │   │   ├── greek-mathfonts-italic.js
│   │           │   │   │   │   │   │   │   │   │   ├── greek-mathfonts-sans-serif-bold.js
│   │           │   │   │   │   │   │   │   │   │   ├── greek-scripts.js
│   │           │   │   │   │   │   │   │   │   │   ├── greek-small.js
│   │           │   │   │   │   │   │   │   │   │   ├── greek-symbols.js
│   │           │   │   │   │   │   │   │   │   │   ├── hebrew_letters.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-lower-double-accent.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-lower-normal.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-lower-phonetic.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-lower-single-accent.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-bold-fraktur.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-bold.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-bold-script.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-double-struck.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-fraktur.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-italic.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-monospace.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-sans-serif-bold.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-sans-serif-italic.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-sans-serif.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-mathfonts-script.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-rest.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-upper-double-accent.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-upper-normal.js
│   │           │   │   │   │   │   │   │   │   │   ├── latin-upper-single-accent.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_angles.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_arrows.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_characters.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_delimiters.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_digits.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_geometry.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_harpoons.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_non_characters.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_symbols.js
│   │           │   │   │   │   │   │   │   │   │   ├── math_whitespace.js
│   │           │   │   │   │   │   │   │   │   │   └── other_stars.js
│   │           │   │   │   │   │   │   │   │   └── units
│   │           │   │   │   │   │   │   │   │       ├── energy.js
│   │           │   │   │   │   │   │   │   │       ├── length.js
│   │           │   │   │   │   │   │   │   │       ├── memory.js
│   │           │   │   │   │   │   │   │   │       ├── other.js
│   │           │   │   │   │   │   │   │   │       ├── speed.js
│   │           │   │   │   │   │   │   │   │       ├── temperature.js
│   │           │   │   │   │   │   │   │   │       ├── time.js
│   │           │   │   │   │   │   │   │   │       ├── volume.js
│   │           │   │   │   │   │   │   │   │       └── weight.js
│   │           │   │   │   │   │   │   │   └── mathmaps_ie.js
│   │           │   │   │   │   │   │   ├── semantic-enrich.js
│   │           │   │   │   │   │   │   └── wgxpath.install.js
│   │           │   │   │   │   │   ├── asciimath2jax.js
│   │           │   │   │   │   │   ├── AssistiveMML.js
│   │           │   │   │   │   │   ├── CHTML-preview.js
│   │           │   │   │   │   │   ├── fast-preview.js
│   │           │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   ├── HTML-CSS
│   │           │   │   │   │   │   │   └── handle-floats.js
│   │           │   │   │   │   │   ├── jsMath2jax.js
│   │           │   │   │   │   │   ├── MatchWebFonts.js
│   │           │   │   │   │   │   ├── MathEvents.js
│   │           │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   ├── MathML
│   │           │   │   │   │   │   │   ├── content-mathml.js
│   │           │   │   │   │   │   │   └── mml3.js
│   │           │   │   │   │   │   ├── MathZoom.js
│   │           │   │   │   │   │   ├── mml2jax.js
│   │           │   │   │   │   │   ├── Safe.js
│   │           │   │   │   │   │   ├── TeX
│   │           │   │   │   │   │   │   ├── action.js
│   │           │   │   │   │   │   │   ├── AMScd.js
│   │           │   │   │   │   │   │   ├── AMSmath.js
│   │           │   │   │   │   │   │   ├── AMSsymbols.js
│   │           │   │   │   │   │   │   ├── autobold.js
│   │           │   │   │   │   │   │   ├── autoload-all.js
│   │           │   │   │   │   │   │   ├── bbox.js
│   │           │   │   │   │   │   │   ├── begingroup.js
│   │           │   │   │   │   │   │   ├── boldsymbol.js
│   │           │   │   │   │   │   │   ├── cancel.js
│   │           │   │   │   │   │   │   ├── color.js
│   │           │   │   │   │   │   │   ├── enclose.js
│   │           │   │   │   │   │   │   ├── extpfeil.js
│   │           │   │   │   │   │   │   ├── HTML.js
│   │           │   │   │   │   │   │   ├── mathchoice.js
│   │           │   │   │   │   │   │   ├── mediawiki-texvc.js
│   │           │   │   │   │   │   │   ├── mhchem3
│   │           │   │   │   │   │   │   │   └── mhchem.js
│   │           │   │   │   │   │   │   ├── mhchem.js
│   │           │   │   │   │   │   │   ├── newcommand.js
│   │           │   │   │   │   │   │   ├── noErrors.js
│   │           │   │   │   │   │   │   ├── noUndefined.js
│   │           │   │   │   │   │   │   ├── unicode.js
│   │           │   │   │   │   │   │   └── verb.js
│   │           │   │   │   │   │   ├── tex2jax.js
│   │           │   │   │   │   │   └── toMathML.js
│   │           │   │   │   │   ├── fonts
│   │           │   │   │   │   │   └── HTML-CSS
│   │           │   │   │   │   │       └── STIX-Web
│   │           │   │   │   │   │           └── woff
│   │           │   │   │   │   │               ├── STIXMathJax_Alphabets-BoldItalic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Alphabets-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Alphabets-Italic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Alphabets-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Arrows-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Arrows-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_DoubleStruck-BoldItalic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_DoubleStruck-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_DoubleStruck-Italic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_DoubleStruck-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Fraktur-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Fraktur-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Latin-BoldItalic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Latin-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Latin-Italic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Latin-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Main-BoldItalic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Main-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Main-Italic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Main-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Marks-BoldItalic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Marks-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Marks-Italic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Marks-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Misc-BoldItalic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Misc-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Misc-Italic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Misc-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Monospace-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Normal-BoldItalic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Normal-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Normal-Italic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Operators-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Operators-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_SansSerif-BoldItalic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_SansSerif-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_SansSerif-Italic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_SansSerif-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Script-BoldItalic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Script-Italic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Script-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Shapes-BoldItalic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Shapes-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Shapes-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Size1-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Size2-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Size3-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Size4-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Size5-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Symbols-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Symbols-Regular.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Variants-BoldItalic.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Variants-Bold.woff
│   │           │   │   │   │   │               ├── STIXMathJax_Variants-Italic.woff
│   │           │   │   │   │   │               └── STIXMathJax_Variants-Regular.woff
│   │           │   │   │   │   ├── jax
│   │           │   │   │   │   │   ├── element
│   │           │   │   │   │   │   │   └── mml
│   │           │   │   │   │   │   │       ├── jax.js
│   │           │   │   │   │   │   │       └── optable
│   │           │   │   │   │   │   │           ├── Arrows.js
│   │           │   │   │   │   │   │           ├── BasicLatin.js
│   │           │   │   │   │   │   │           ├── CombDiacritMarks.js
│   │           │   │   │   │   │   │           ├── CombDiactForSymbols.js
│   │           │   │   │   │   │   │           ├── Dingbats.js
│   │           │   │   │   │   │   │           ├── GeneralPunctuation.js
│   │           │   │   │   │   │   │           ├── GeometricShapes.js
│   │           │   │   │   │   │   │           ├── GreekAndCoptic.js
│   │           │   │   │   │   │   │           ├── Latin1Supplement.js
│   │           │   │   │   │   │   │           ├── LetterlikeSymbols.js
│   │           │   │   │   │   │   │           ├── MathOperators.js
│   │           │   │   │   │   │   │           ├── MiscMathSymbolsA.js
│   │           │   │   │   │   │   │           ├── MiscMathSymbolsB.js
│   │           │   │   │   │   │   │           ├── MiscSymbolsAndArrows.js
│   │           │   │   │   │   │   │           ├── MiscTechnical.js
│   │           │   │   │   │   │   │           ├── SpacingModLetters.js
│   │           │   │   │   │   │   │           ├── SupplementalArrowsA.js
│   │           │   │   │   │   │   │           ├── SupplementalArrowsB.js
│   │           │   │   │   │   │   │           └── SuppMathOperators.js
│   │           │   │   │   │   │   ├── input
│   │           │   │   │   │   │   │   └── TeX
│   │           │   │   │   │   │   │       ├── config.js
│   │           │   │   │   │   │   │       └── jax.js
│   │           │   │   │   │   │   └── output
│   │           │   │   │   │   │       ├── CommonHTML
│   │           │   │   │   │   │       │   ├── autoload
│   │           │   │   │   │   │       │   │   ├── annotation-xml.js
│   │           │   │   │   │   │       │   │   ├── maction.js
│   │           │   │   │   │   │       │   │   ├── menclose.js
│   │           │   │   │   │   │       │   │   ├── mglyph.js
│   │           │   │   │   │   │       │   │   ├── mmultiscripts.js
│   │           │   │   │   │   │       │   │   ├── ms.js
│   │           │   │   │   │   │       │   │   ├── mtable.js
│   │           │   │   │   │   │       │   │   └── multiline.js
│   │           │   │   │   │   │       │   ├── config.js
│   │           │   │   │   │   │       │   └── jax.js
│   │           │   │   │   │   │       ├── HTML-CSS
│   │           │   │   │   │   │       │   ├── autoload
│   │           │   │   │   │   │       │   │   ├── annotation-xml.js
│   │           │   │   │   │   │       │   │   ├── maction.js
│   │           │   │   │   │   │       │   │   ├── menclose.js
│   │           │   │   │   │   │       │   │   ├── mglyph.js
│   │           │   │   │   │   │       │   │   ├── mmultiscripts.js
│   │           │   │   │   │   │       │   │   ├── ms.js
│   │           │   │   │   │   │       │   │   ├── mtable.js
│   │           │   │   │   │   │       │   │   └── multiline.js
│   │           │   │   │   │   │       │   ├── config.js
│   │           │   │   │   │   │       │   ├── fonts
│   │           │   │   │   │   │       │   │   └── STIX-Web
│   │           │   │   │   │   │       │   │       ├── Alphabets
│   │           │   │   │   │   │       │   │       │   ├── Bold
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── BoldItalic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── Italic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Arrows
│   │           │   │   │   │   │       │   │       │   ├── Bold
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── DoubleStruck
│   │           │   │   │   │   │       │   │       │   ├── Bold
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── BoldItalic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── Italic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── fontdata-extra.js
│   │           │   │   │   │   │       │   │       ├── fontdata.js
│   │           │   │   │   │   │       │   │       ├── Fraktur
│   │           │   │   │   │   │       │   │       │   ├── Bold
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Latin
│   │           │   │   │   │   │       │   │       │   ├── Bold
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── BoldItalic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── Italic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Main
│   │           │   │   │   │   │       │   │       │   ├── Bold
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── BoldItalic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── Italic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Marks
│   │           │   │   │   │   │       │   │       │   ├── Bold
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── BoldItalic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── Italic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Misc
│   │           │   │   │   │   │       │   │       │   ├── Bold
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── BoldItalic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── Italic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Monospace
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Normal
│   │           │   │   │   │   │       │   │       │   ├── Bold
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── BoldItalic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Italic
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Operators
│   │           │   │   │   │   │       │   │       │   ├── Bold
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── SansSerif
│   │           │   │   │   │   │       │   │       │   ├── Bold
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── BoldItalic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── Italic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Script
│   │           │   │   │   │   │       │   │       │   ├── BoldItalic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── Italic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Shapes
│   │           │   │   │   │   │       │   │       │   ├── Bold
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   ├── BoldItalic
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Size1
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Size2
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Size3
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Size4
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Size5
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       ├── Symbols
│   │           │   │   │   │   │       │   │       │   ├── Bold
│   │           │   │   │   │   │       │   │       │   │   └── Main.js
│   │           │   │   │   │   │       │   │       │   └── Regular
│   │           │   │   │   │   │       │   │       │       └── Main.js
│   │           │   │   │   │   │       │   │       └── Variants
│   │           │   │   │   │   │       │   │           ├── Bold
│   │           │   │   │   │   │       │   │           │   └── Main.js
│   │           │   │   │   │   │       │   │           ├── BoldItalic
│   │           │   │   │   │   │       │   │           │   └── Main.js
│   │           │   │   │   │   │       │   │           ├── Italic
│   │           │   │   │   │   │       │   │           │   └── Main.js
│   │           │   │   │   │   │       │   │           └── Regular
│   │           │   │   │   │   │       │   │               └── Main.js
│   │           │   │   │   │   │       │   ├── imageFonts.js
│   │           │   │   │   │   │       │   └── jax.js
│   │           │   │   │   │   │       ├── NativeMML
│   │           │   │   │   │   │       │   ├── config.js
│   │           │   │   │   │   │       │   └── jax.js
│   │           │   │   │   │   │       ├── PlainSource
│   │           │   │   │   │   │       │   ├── config.js
│   │           │   │   │   │   │       │   └── jax.js
│   │           │   │   │   │   │       ├── PreviewHTML
│   │           │   │   │   │   │       │   ├── config.js
│   │           │   │   │   │   │       │   └── jax.js
│   │           │   │   │   │   │       └── SVG
│   │           │   │   │   │   │           ├── autoload
│   │           │   │   │   │   │           │   ├── annotation-xml.js
│   │           │   │   │   │   │           │   ├── maction.js
│   │           │   │   │   │   │           │   ├── menclose.js
│   │           │   │   │   │   │           │   ├── mglyph.js
│   │           │   │   │   │   │           │   ├── mmultiscripts.js
│   │           │   │   │   │   │           │   ├── ms.js
│   │           │   │   │   │   │           │   ├── mtable.js
│   │           │   │   │   │   │           │   └── multiline.js
│   │           │   │   │   │   │           ├── config.js
│   │           │   │   │   │   │           ├── fonts
│   │           │   │   │   │   │           │   └── STIX-Web
│   │           │   │   │   │   │           │       ├── Alphabets
│   │           │   │   │   │   │           │       │   ├── Bold
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── BoldItalic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── Italic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Arrows
│   │           │   │   │   │   │           │       │   ├── Bold
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── DoubleStruck
│   │           │   │   │   │   │           │       │   ├── Bold
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── BoldItalic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── Italic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── fontdata-extra.js
│   │           │   │   │   │   │           │       ├── fontdata.js
│   │           │   │   │   │   │           │       ├── Fraktur
│   │           │   │   │   │   │           │       │   ├── Bold
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Latin
│   │           │   │   │   │   │           │       │   ├── Bold
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── BoldItalic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── Italic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Main
│   │           │   │   │   │   │           │       │   ├── Bold
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── BoldItalic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── Italic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Marks
│   │           │   │   │   │   │           │       │   ├── Bold
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── BoldItalic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── Italic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Misc
│   │           │   │   │   │   │           │       │   ├── Bold
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── BoldItalic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── Italic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Monospace
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Normal
│   │           │   │   │   │   │           │       │   ├── Bold
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── BoldItalic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Italic
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Operators
│   │           │   │   │   │   │           │       │   ├── Bold
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── SansSerif
│   │           │   │   │   │   │           │       │   ├── Bold
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── BoldItalic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── Italic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Script
│   │           │   │   │   │   │           │       │   ├── BoldItalic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── Italic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Shapes
│   │           │   │   │   │   │           │       │   ├── Bold
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   ├── BoldItalic
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Size1
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Size2
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Size3
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Size4
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Size5
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       ├── Symbols
│   │           │   │   │   │   │           │       │   ├── Bold
│   │           │   │   │   │   │           │       │   │   └── Main.js
│   │           │   │   │   │   │           │       │   └── Regular
│   │           │   │   │   │   │           │       │       └── Main.js
│   │           │   │   │   │   │           │       └── Variants
│   │           │   │   │   │   │           │           ├── Bold
│   │           │   │   │   │   │           │           │   └── Main.js
│   │           │   │   │   │   │           │           ├── BoldItalic
│   │           │   │   │   │   │           │           │   └── Main.js
│   │           │   │   │   │   │           │           ├── Italic
│   │           │   │   │   │   │           │           │   └── Main.js
│   │           │   │   │   │   │           │           └── Regular
│   │           │   │   │   │   │           │               └── Main.js
│   │           │   │   │   │   │           └── jax.js
│   │           │   │   │   │   ├── localization
│   │           │   │   │   │   │   ├── ar
│   │           │   │   │   │   │   │   ├── ar.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── ast
│   │           │   │   │   │   │   │   ├── ast.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── bcc
│   │           │   │   │   │   │   │   ├── bcc.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── bg
│   │           │   │   │   │   │   │   ├── bg.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── br
│   │           │   │   │   │   │   │   ├── br.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── ca
│   │           │   │   │   │   │   │   ├── ca.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── cdo
│   │           │   │   │   │   │   │   ├── cdo.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── ce
│   │           │   │   │   │   │   │   ├── ce.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── cs
│   │           │   │   │   │   │   │   ├── cs.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── cy
│   │           │   │   │   │   │   │   ├── cy.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── da
│   │           │   │   │   │   │   │   ├── da.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── de
│   │           │   │   │   │   │   │   ├── de.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── diq
│   │           │   │   │   │   │   │   ├── diq.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── en
│   │           │   │   │   │   │   │   ├── en.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── eo
│   │           │   │   │   │   │   │   ├── eo.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── es
│   │           │   │   │   │   │   │   ├── es.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── fa
│   │           │   │   │   │   │   │   ├── fa.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── fi
│   │           │   │   │   │   │   │   ├── fi.js
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── fr
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── fr.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── gl
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── gl.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── he
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── he.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── ia
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── ia.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── it
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── it.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── ja
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── ja.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── kn
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── kn.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── ko
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── ko.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── lb
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── lb.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── lki
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── lki.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── lt
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── lt.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── mk
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── mk.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── nl
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── nl.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── oc
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── oc.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── pl
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── pl.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── pt
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── pt.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── pt-br
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── pt-br.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── qqq
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── qqq.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── ru
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── ru.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── scn
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── scn.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── sco
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── sco.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── sk
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── sk.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── sl
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── sl.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── sv
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── sv.js
│   │           │   │   │   │   │   │   └── TeX.js
│   │           │   │   │   │   │   ├── th
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── TeX.js
│   │           │   │   │   │   │   │   └── th.js
│   │           │   │   │   │   │   ├── tr
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── TeX.js
│   │           │   │   │   │   │   │   └── tr.js
│   │           │   │   │   │   │   ├── uk
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── TeX.js
│   │           │   │   │   │   │   │   └── uk.js
│   │           │   │   │   │   │   ├── vi
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── TeX.js
│   │           │   │   │   │   │   │   └── vi.js
│   │           │   │   │   │   │   ├── zh-hans
│   │           │   │   │   │   │   │   ├── FontWarnings.js
│   │           │   │   │   │   │   │   ├── HelpDialog.js
│   │           │   │   │   │   │   │   ├── HTML-CSS.js
│   │           │   │   │   │   │   │   ├── MathMenu.js
│   │           │   │   │   │   │   │   ├── MathML.js
│   │           │   │   │   │   │   │   ├── TeX.js
│   │           │   │   │   │   │   │   └── zh-hans.js
│   │           │   │   │   │   │   └── zh-hant
│   │           │   │   │   │   │       ├── FontWarnings.js
│   │           │   │   │   │   │       ├── HelpDialog.js
│   │           │   │   │   │   │       ├── HTML-CSS.js
│   │           │   │   │   │   │       ├── MathMenu.js
│   │           │   │   │   │   │       ├── MathML.js
│   │           │   │   │   │   │       ├── TeX.js
│   │           │   │   │   │   │       └── zh-hant.js
│   │           │   │   │   │   └── MathJax.js
│   │           │   │   │   ├── moment
│   │           │   │   │   │   ├── min
│   │           │   │   │   │   │   ├── locales.js
│   │           │   │   │   │   │   ├── locales.min.js
│   │           │   │   │   │   │   ├── moment.min.js
│   │           │   │   │   │   │   ├── moment-with-locales.js
│   │           │   │   │   │   │   └── moment-with-locales.min.js
│   │           │   │   │   │   └── moment.js
│   │           │   │   │   ├── preact
│   │           │   │   │   │   └── index.js
│   │           │   │   │   ├── preact-compat
│   │           │   │   │   │   └── index.js
│   │           │   │   │   ├── proptypes
│   │           │   │   │   │   └── index.js
│   │           │   │   │   ├── requirejs
│   │           │   │   │   │   └── require.js
│   │           │   │   │   ├── requirejs-plugins
│   │           │   │   │   │   └── src
│   │           │   │   │   │       └── json.js
│   │           │   │   │   ├── requirejs-text
│   │           │   │   │   │   └── text.js
│   │           │   │   │   ├── text-encoding
│   │           │   │   │   │   └── lib
│   │           │   │   │   │       └── encoding.js
│   │           │   │   │   ├── underscore
│   │           │   │   │   │   └── underscore-min.js
│   │           │   │   │   ├── xterm.js
│   │           │   │   │   │   └── index.js
│   │           │   │   │   ├── xterm.js-css
│   │           │   │   │   │   └── index.css
│   │           │   │   │   └── xterm.js-fit
│   │           │   │   │       └── index.js
│   │           │   │   ├── custom
│   │           │   │   │   ├── custom.css
│   │           │   │   │   └── custom.js
│   │           │   │   ├── edit
│   │           │   │   │   └── js
│   │           │   │   │       ├── editor.js
│   │           │   │   │       ├── main.js
│   │           │   │   │       ├── main.min.js
│   │           │   │   │       ├── main.min.js.map
│   │           │   │   │       ├── menubar.js
│   │           │   │   │       ├── notificationarea.js
│   │           │   │   │       └── savewidget.js
│   │           │   │   ├── favicon.ico
│   │           │   │   ├── notebook
│   │           │   │   │   ├── css
│   │           │   │   │   │   └── override.css
│   │           │   │   │   └── js
│   │           │   │   │       ├── about.js
│   │           │   │   │       ├── actions.js
│   │           │   │   │       ├── cell.js
│   │           │   │   │       ├── celltoolbar.js
│   │           │   │   │       ├── celltoolbarpresets
│   │           │   │   │       │   ├── attachments.js
│   │           │   │   │       │   ├── default.js
│   │           │   │   │       │   ├── example.js
│   │           │   │   │       │   ├── rawcell.js
│   │           │   │   │       │   ├── slideshow.js
│   │           │   │   │       │   └── tags.js
│   │           │   │   │       ├── clipboard.js
│   │           │   │   │       ├── codecell.js
│   │           │   │   │       ├── codemirror-ipythongfm.js
│   │           │   │   │       ├── codemirror-ipython.js
│   │           │   │   │       ├── commandpalette.js
│   │           │   │   │       ├── completer.js
│   │           │   │   │       ├── contexthint.js
│   │           │   │   │       ├── kernelselector.js
│   │           │   │   │       ├── keyboardmanager.js
│   │           │   │   │       ├── main.js
│   │           │   │   │       ├── main.min.js
│   │           │   │   │       ├── main.min.js.map
│   │           │   │   │       ├── maintoolbar.js
│   │           │   │   │       ├── mathjaxutils.js
│   │           │   │   │       ├── menubar.js
│   │           │   │   │       ├── notebook.js
│   │           │   │   │       ├── notificationarea.js
│   │           │   │   │       ├── outputarea.js
│   │           │   │   │       ├── pager.js
│   │           │   │   │       ├── promises.js
│   │           │   │   │       ├── quickhelp.js
│   │           │   │   │       ├── savewidget.js
│   │           │   │   │       ├── scrollmanager.js
│   │           │   │   │       ├── searchandreplace.js
│   │           │   │   │       ├── shortcuteditor.js
│   │           │   │   │       ├── textcell.js
│   │           │   │   │       ├── toolbar.js
│   │           │   │   │       ├── tooltip.js
│   │           │   │   │       └── tour.js
│   │           │   │   ├── robots.txt
│   │           │   │   ├── services
│   │           │   │   │   ├── config.js
│   │           │   │   │   ├── contents.js
│   │           │   │   │   ├── kernels
│   │           │   │   │   │   ├── comm.js
│   │           │   │   │   │   ├── kernel.js
│   │           │   │   │   │   └── serialize.js
│   │           │   │   │   └── sessions
│   │           │   │   │       └── session.js
│   │           │   │   ├── style
│   │           │   │   │   ├── ipython.less
│   │           │   │   │   ├── ipython.min.css
│   │           │   │   │   ├── ipython.min.css.map
│   │           │   │   │   ├── style.less
│   │           │   │   │   ├── style.min.css
│   │           │   │   │   └── style.min.css.map
│   │           │   │   ├── terminal
│   │           │   │   │   ├── css
│   │           │   │   │   │   └── override.css
│   │           │   │   │   └── js
│   │           │   │   │       ├── main.js
│   │           │   │   │       ├── main.min.js
│   │           │   │   │       ├── main.min.js.map
│   │           │   │   │       └── terminado.js
│   │           │   │   └── tree
│   │           │   │       └── js
│   │           │   │           ├── kernellist.js
│   │           │   │           ├── main.js
│   │           │   │           ├── main.min.js
│   │           │   │           ├── main.min.js.map
│   │           │   │           ├── newnotebook.js
│   │           │   │           ├── notebooklist.js
│   │           │   │           ├── sessionlist.js
│   │           │   │           ├── shutdownbutton.js
│   │           │   │           └── terminallist.js
│   │           │   ├── _sysinfo.py
│   │           │   ├── templates
│   │           │   │   ├── 404.html
│   │           │   │   ├── browser-open.html
│   │           │   │   ├── edit.html
│   │           │   │   ├── error.html
│   │           │   │   ├── login.html
│   │           │   │   ├── logout.html
│   │           │   │   ├── notebook.html
│   │           │   │   ├── page.html
│   │           │   │   ├── terminal.html
│   │           │   │   ├── tree.html
│   │           │   │   └── view.html
│   │           │   ├── terminal
│   │           │   │   ├── api_handlers.py
│   │           │   │   ├── handlers.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── api_handlers.cpython-36.pyc
│   │           │   │       ├── handlers.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── tests
│   │           │   │   ├── base
│   │           │   │   │   ├── highlight.js
│   │           │   │   │   ├── keyboard.js
│   │           │   │   │   ├── misc.js
│   │           │   │   │   ├── security.js
│   │           │   │   │   └── utils.js
│   │           │   │   ├── __init__.py
│   │           │   │   ├── launchnotebook.py
│   │           │   │   ├── mockextension
│   │           │   │   │   └── index.js
│   │           │   │   ├── notebook
│   │           │   │   │   ├── attachments.js
│   │           │   │   │   ├── buffering.js
│   │           │   │   │   ├── clipboard_multiselect.js
│   │           │   │   │   ├── display_id.js
│   │           │   │   │   ├── display_image.js
│   │           │   │   │   ├── dualmode_arrows.js
│   │           │   │   │   ├── dualmode_cellmode.js
│   │           │   │   │   ├── dualmode_clipboard.js
│   │           │   │   │   ├── dualmode_execute.js
│   │           │   │   │   ├── dualmode.js
│   │           │   │   │   ├── dualmode_markdown.js
│   │           │   │   │   ├── dualmode_merge.js
│   │           │   │   │   ├── execute_code.js
│   │           │   │   │   ├── execute_selected_cells.js
│   │           │   │   │   ├── inject_js.js
│   │           │   │   │   ├── interrupt.js
│   │           │   │   │   ├── isolated_svg.js
│   │           │   │   │   ├── kernel_menu.js
│   │           │   │   │   ├── markdown.js
│   │           │   │   │   ├── merge_cells_api.js
│   │           │   │   │   ├── move_multiselection.js
│   │           │   │   │   ├── multiselect.js
│   │           │   │   │   ├── multiselect_toggle.js
│   │           │   │   │   ├── notifications.js
│   │           │   │   │   ├── output.js
│   │           │   │   │   ├── roundtrip.js
│   │           │   │   │   ├── safe_append_output.js
│   │           │   │   │   ├── save.js
│   │           │   │   │   ├── shutdown.js
│   │           │   │   │   └── tags.js
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── launchnotebook.cpython-36.pyc
│   │           │   │   │   ├── test_config_manager.cpython-36.pyc
│   │           │   │   │   ├── test_files.cpython-36.pyc
│   │           │   │   │   ├── test_i18n.cpython-36.pyc
│   │           │   │   │   ├── test_nbextensions.cpython-36.pyc
│   │           │   │   │   ├── test_notebookapp.cpython-36.pyc
│   │           │   │   │   ├── test_paths.cpython-36.pyc
│   │           │   │   │   ├── test_serialize.cpython-36.pyc
│   │           │   │   │   ├── test_serverextensions.cpython-36.pyc
│   │           │   │   │   └── test_utils.cpython-36.pyc
│   │           │   │   ├── selenium
│   │           │   │   │   ├── conftest.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── quick_selenium.cpython-36.pyc
│   │           │   │   │   │   ├── test_dashboard_nav.cpython-36.pyc
│   │           │   │   │   │   ├── test_deletecell.cpython-36.pyc
│   │           │   │   │   │   ├── test_dualmode_insertcell.cpython-36.pyc
│   │           │   │   │   │   ├── test_find_and_replace.cpython-36.pyc
│   │           │   │   │   │   ├── test_markdown.cpython-36.pyc
│   │           │   │   │   │   ├── test_prompt_numbers.cpython-36.pyc
│   │           │   │   │   │   ├── test_save_as_notebook.cpython-36.pyc
│   │           │   │   │   │   ├── undelete.cpython-36.pyc
│   │           │   │   │   │   └── utils.cpython-36.pyc
│   │           │   │   │   ├── quick_selenium.py
│   │           │   │   │   ├── test_dashboard_nav.py
│   │           │   │   │   ├── test_deletecell.py
│   │           │   │   │   ├── test_dualmode_insertcell.py
│   │           │   │   │   ├── test_find_and_replace.py
│   │           │   │   │   ├── test_markdown.py
│   │           │   │   │   ├── test_prompt_numbers.py
│   │           │   │   │   ├── test_save_as_notebook.py
│   │           │   │   │   ├── undelete.py
│   │           │   │   │   └── utils.py
│   │           │   │   ├── services
│   │           │   │   │   ├── kernel.js
│   │           │   │   │   ├── serialize.js
│   │           │   │   │   └── session.js
│   │           │   │   ├── test_config_manager.py
│   │           │   │   ├── test_files.py
│   │           │   │   ├── test_i18n.py
│   │           │   │   ├── test_nbextensions.py
│   │           │   │   ├── test_notebookapp.py
│   │           │   │   ├── test_paths.py
│   │           │   │   ├── test_serialize.py
│   │           │   │   ├── test_serverextensions.py
│   │           │   │   ├── test_utils.py
│   │           │   │   └── util.js
│   │           │   ├── transutils.py
│   │           │   ├── tree
│   │           │   │   ├── handlers.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── handlers.cpython-36.pyc
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   └── test_tree_handler.cpython-36.pyc
│   │           │   │       └── test_tree_handler.py
│   │           │   ├── _tz.py
│   │           │   ├── utils.py
│   │           │   ├── _version.py
│   │           │   └── view
│   │           │       ├── handlers.py
│   │           │       ├── __init__.py
│   │           │       └── __pycache__
│   │           │           ├── handlers.cpython-36.pyc
│   │           │           └── __init__.cpython-36.pyc
│   │           ├── notebook-5.7.8.dist-info
│   │           │   ├── COPYING.md
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── numpy
│   │           │   ├── compat
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _inspect.py
│   │           │   │   ├── py3k.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── _inspect.cpython-36.pyc
│   │           │   │   │   ├── py3k.cpython-36.pyc
│   │           │   │   │   └── setup.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   └── test_compat.cpython-36.pyc
│   │           │   │       └── test_compat.py
│   │           │   ├── __config__.py
│   │           │   ├── conftest.py
│   │           │   ├── core
│   │           │   │   ├── _add_newdocs.py
│   │           │   │   ├── _aliased_types.py
│   │           │   │   ├── arrayprint.py
│   │           │   │   ├── cversions.py
│   │           │   │   ├── defchararray.py
│   │           │   │   ├── _dtype_ctypes.py
│   │           │   │   ├── _dtype.py
│   │           │   │   ├── _dummy.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── einsumfunc.py
│   │           │   │   ├── fromnumeric.py
│   │           │   │   ├── function_base.py
│   │           │   │   ├── generate_numpy_api.py
│   │           │   │   ├── getlimits.py
│   │           │   │   ├── include
│   │           │   │   │   └── numpy
│   │           │   │   │       ├── arrayobject.h
│   │           │   │   │       ├── arrayscalars.h
│   │           │   │   │       ├── halffloat.h
│   │           │   │   │       ├── __multiarray_api.h
│   │           │   │   │       ├── multiarray_api.txt
│   │           │   │   │       ├── ndarrayobject.h
│   │           │   │   │       ├── ndarraytypes.h
│   │           │   │   │       ├── _neighborhood_iterator_imp.h
│   │           │   │   │       ├── noprefix.h
│   │           │   │   │       ├── npy_1_7_deprecated_api.h
│   │           │   │   │       ├── npy_3kcompat.h
│   │           │   │   │       ├── npy_common.h
│   │           │   │   │       ├── npy_cpu.h
│   │           │   │   │       ├── npy_endian.h
│   │           │   │   │       ├── npy_interrupt.h
│   │           │   │   │       ├── npy_math.h
│   │           │   │   │       ├── npy_no_deprecated_api.h
│   │           │   │   │       ├── npy_os.h
│   │           │   │   │       ├── _numpyconfig.h
│   │           │   │   │       ├── numpyconfig.h
│   │           │   │   │       ├── old_defines.h
│   │           │   │   │       ├── oldnumeric.h
│   │           │   │   │       ├── __ufunc_api.h
│   │           │   │   │       ├── ufunc_api.txt
│   │           │   │   │       ├── ufuncobject.h
│   │           │   │   │       └── utils.h
│   │           │   │   ├── info.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _internal.py
│   │           │   │   ├── lib
│   │           │   │   │   ├── libnpymath.a
│   │           │   │   │   └── npy-pkg-config
│   │           │   │   │       ├── mlib.ini
│   │           │   │   │       └── npymath.ini
│   │           │   │   ├── machar.py
│   │           │   │   ├── memmap.py
│   │           │   │   ├── _methods.py
│   │           │   │   ├── multiarray.py
│   │           │   │   ├── _multiarray_tests.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _multiarray_umath.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── numeric.py
│   │           │   │   ├── numerictypes.py
│   │           │   │   ├── _operand_flag_tests.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── overrides.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _add_newdocs.cpython-36.pyc
│   │           │   │   │   ├── _aliased_types.cpython-36.pyc
│   │           │   │   │   ├── arrayprint.cpython-36.pyc
│   │           │   │   │   ├── cversions.cpython-36.pyc
│   │           │   │   │   ├── defchararray.cpython-36.pyc
│   │           │   │   │   ├── _dtype.cpython-36.pyc
│   │           │   │   │   ├── _dtype_ctypes.cpython-36.pyc
│   │           │   │   │   ├── einsumfunc.cpython-36.pyc
│   │           │   │   │   ├── fromnumeric.cpython-36.pyc
│   │           │   │   │   ├── function_base.cpython-36.pyc
│   │           │   │   │   ├── generate_numpy_api.cpython-36.pyc
│   │           │   │   │   ├── getlimits.cpython-36.pyc
│   │           │   │   │   ├── info.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── _internal.cpython-36.pyc
│   │           │   │   │   ├── machar.cpython-36.pyc
│   │           │   │   │   ├── memmap.cpython-36.pyc
│   │           │   │   │   ├── _methods.cpython-36.pyc
│   │           │   │   │   ├── multiarray.cpython-36.pyc
│   │           │   │   │   ├── numeric.cpython-36.pyc
│   │           │   │   │   ├── numerictypes.cpython-36.pyc
│   │           │   │   │   ├── overrides.cpython-36.pyc
│   │           │   │   │   ├── records.cpython-36.pyc
│   │           │   │   │   ├── setup_common.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   ├── shape_base.cpython-36.pyc
│   │           │   │   │   ├── _string_helpers.cpython-36.pyc
│   │           │   │   │   ├── _type_aliases.cpython-36.pyc
│   │           │   │   │   ├── umath.cpython-36.pyc
│   │           │   │   │   └── umath_tests.cpython-36.pyc
│   │           │   │   ├── _rational_tests.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── records.py
│   │           │   │   ├── setup_common.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── shape_base.py
│   │           │   │   ├── _string_helpers.py
│   │           │   │   ├── _struct_ufunc_tests.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── astype_copy.pkl
│   │           │   │   │   │   └── recarray_from_file.fits
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _locales.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── _locales.cpython-36.pyc
│   │           │   │   │   │   ├── test_abc.cpython-36.pyc
│   │           │   │   │   │   ├── test_api.cpython-36.pyc
│   │           │   │   │   │   ├── test_arrayprint.cpython-36.pyc
│   │           │   │   │   │   ├── test_datetime.cpython-36.pyc
│   │           │   │   │   │   ├── test_defchararray.cpython-36.pyc
│   │           │   │   │   │   ├── test_deprecations.cpython-36.pyc
│   │           │   │   │   │   ├── test_dtype.cpython-36.pyc
│   │           │   │   │   │   ├── test_einsum.cpython-36.pyc
│   │           │   │   │   │   ├── test_errstate.cpython-36.pyc
│   │           │   │   │   │   ├── test_extint128.cpython-36.pyc
│   │           │   │   │   │   ├── test_function_base.cpython-36.pyc
│   │           │   │   │   │   ├── test_getlimits.cpython-36.pyc
│   │           │   │   │   │   ├── test_half.cpython-36.pyc
│   │           │   │   │   │   ├── test_indexerrors.cpython-36.pyc
│   │           │   │   │   │   ├── test_indexing.cpython-36.pyc
│   │           │   │   │   │   ├── test_item_selection.cpython-36.pyc
│   │           │   │   │   │   ├── test_longdouble.cpython-36.pyc
│   │           │   │   │   │   ├── test_machar.cpython-36.pyc
│   │           │   │   │   │   ├── test_memmap.cpython-36.pyc
│   │           │   │   │   │   ├── test_mem_overlap.cpython-36.pyc
│   │           │   │   │   │   ├── test_multiarray.cpython-36.pyc
│   │           │   │   │   │   ├── test_nditer.cpython-36.pyc
│   │           │   │   │   │   ├── test_numeric.cpython-36.pyc
│   │           │   │   │   │   ├── test_numerictypes.cpython-36.pyc
│   │           │   │   │   │   ├── test_overrides.cpython-36.pyc
│   │           │   │   │   │   ├── test_print.cpython-36.pyc
│   │           │   │   │   │   ├── test_records.cpython-36.pyc
│   │           │   │   │   │   ├── test_regression.cpython-36.pyc
│   │           │   │   │   │   ├── test_scalarbuffer.cpython-36.pyc
│   │           │   │   │   │   ├── test_scalar_ctors.cpython-36.pyc
│   │           │   │   │   │   ├── test_scalarinherit.cpython-36.pyc
│   │           │   │   │   │   ├── test_scalarmath.cpython-36.pyc
│   │           │   │   │   │   ├── test_scalarprint.cpython-36.pyc
│   │           │   │   │   │   ├── test_shape_base.cpython-36.pyc
│   │           │   │   │   │   ├── test_ufunc.cpython-36.pyc
│   │           │   │   │   │   ├── test_umath_complex.cpython-36.pyc
│   │           │   │   │   │   ├── test_umath.cpython-36.pyc
│   │           │   │   │   │   └── test_unicode.cpython-36.pyc
│   │           │   │   │   ├── test_abc.py
│   │           │   │   │   ├── test_api.py
│   │           │   │   │   ├── test_arrayprint.py
│   │           │   │   │   ├── test_datetime.py
│   │           │   │   │   ├── test_defchararray.py
│   │           │   │   │   ├── test_deprecations.py
│   │           │   │   │   ├── test_dtype.py
│   │           │   │   │   ├── test_einsum.py
│   │           │   │   │   ├── test_errstate.py
│   │           │   │   │   ├── test_extint128.py
│   │           │   │   │   ├── test_function_base.py
│   │           │   │   │   ├── test_getlimits.py
│   │           │   │   │   ├── test_half.py
│   │           │   │   │   ├── test_indexerrors.py
│   │           │   │   │   ├── test_indexing.py
│   │           │   │   │   ├── test_item_selection.py
│   │           │   │   │   ├── test_longdouble.py
│   │           │   │   │   ├── test_machar.py
│   │           │   │   │   ├── test_memmap.py
│   │           │   │   │   ├── test_mem_overlap.py
│   │           │   │   │   ├── test_multiarray.py
│   │           │   │   │   ├── test_nditer.py
│   │           │   │   │   ├── test_numeric.py
│   │           │   │   │   ├── test_numerictypes.py
│   │           │   │   │   ├── test_overrides.py
│   │           │   │   │   ├── test_print.py
│   │           │   │   │   ├── test_records.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   ├── test_scalarbuffer.py
│   │           │   │   │   ├── test_scalar_ctors.py
│   │           │   │   │   ├── test_scalarinherit.py
│   │           │   │   │   ├── test_scalarmath.py
│   │           │   │   │   ├── test_scalarprint.py
│   │           │   │   │   ├── test_shape_base.py
│   │           │   │   │   ├── test_ufunc.py
│   │           │   │   │   ├── test_umath_complex.py
│   │           │   │   │   ├── test_umath.py
│   │           │   │   │   └── test_unicode.py
│   │           │   │   ├── _type_aliases.py
│   │           │   │   ├── umath.py
│   │           │   │   ├── _umath_tests.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   └── umath_tests.py
│   │           │   ├── ctypeslib.py
│   │           │   ├── _distributor_init.py
│   │           │   ├── distutils
│   │           │   │   ├── ccompiler.py
│   │           │   │   ├── command
│   │           │   │   │   ├── autodist.py
│   │           │   │   │   ├── bdist_rpm.py
│   │           │   │   │   ├── build_clib.py
│   │           │   │   │   ├── build_ext.py
│   │           │   │   │   ├── build.py
│   │           │   │   │   ├── build_py.py
│   │           │   │   │   ├── build_scripts.py
│   │           │   │   │   ├── build_src.py
│   │           │   │   │   ├── config_compiler.py
│   │           │   │   │   ├── config.py
│   │           │   │   │   ├── develop.py
│   │           │   │   │   ├── egg_info.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── install_clib.py
│   │           │   │   │   ├── install_data.py
│   │           │   │   │   ├── install_headers.py
│   │           │   │   │   ├── install.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── autodist.cpython-36.pyc
│   │           │   │   │   │   ├── bdist_rpm.cpython-36.pyc
│   │           │   │   │   │   ├── build_clib.cpython-36.pyc
│   │           │   │   │   │   ├── build.cpython-36.pyc
│   │           │   │   │   │   ├── build_ext.cpython-36.pyc
│   │           │   │   │   │   ├── build_py.cpython-36.pyc
│   │           │   │   │   │   ├── build_scripts.cpython-36.pyc
│   │           │   │   │   │   ├── build_src.cpython-36.pyc
│   │           │   │   │   │   ├── config_compiler.cpython-36.pyc
│   │           │   │   │   │   ├── config.cpython-36.pyc
│   │           │   │   │   │   ├── develop.cpython-36.pyc
│   │           │   │   │   │   ├── egg_info.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── install_clib.cpython-36.pyc
│   │           │   │   │   │   ├── install.cpython-36.pyc
│   │           │   │   │   │   ├── install_data.cpython-36.pyc
│   │           │   │   │   │   ├── install_headers.cpython-36.pyc
│   │           │   │   │   │   └── sdist.cpython-36.pyc
│   │           │   │   │   └── sdist.py
│   │           │   │   ├── compat.py
│   │           │   │   ├── __config__.py
│   │           │   │   ├── conv_template.py
│   │           │   │   ├── core.py
│   │           │   │   ├── cpuinfo.py
│   │           │   │   ├── exec_command.py
│   │           │   │   ├── extension.py
│   │           │   │   ├── fcompiler
│   │           │   │   │   ├── absoft.py
│   │           │   │   │   ├── compaq.py
│   │           │   │   │   ├── environment.py
│   │           │   │   │   ├── g95.py
│   │           │   │   │   ├── gnu.py
│   │           │   │   │   ├── hpux.py
│   │           │   │   │   ├── ibm.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── intel.py
│   │           │   │   │   ├── lahey.py
│   │           │   │   │   ├── mips.py
│   │           │   │   │   ├── nag.py
│   │           │   │   │   ├── none.py
│   │           │   │   │   ├── pathf95.py
│   │           │   │   │   ├── pg.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── absoft.cpython-36.pyc
│   │           │   │   │   │   ├── compaq.cpython-36.pyc
│   │           │   │   │   │   ├── environment.cpython-36.pyc
│   │           │   │   │   │   ├── g95.cpython-36.pyc
│   │           │   │   │   │   ├── gnu.cpython-36.pyc
│   │           │   │   │   │   ├── hpux.cpython-36.pyc
│   │           │   │   │   │   ├── ibm.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── intel.cpython-36.pyc
│   │           │   │   │   │   ├── lahey.cpython-36.pyc
│   │           │   │   │   │   ├── mips.cpython-36.pyc
│   │           │   │   │   │   ├── nag.cpython-36.pyc
│   │           │   │   │   │   ├── none.cpython-36.pyc
│   │           │   │   │   │   ├── pathf95.cpython-36.pyc
│   │           │   │   │   │   ├── pg.cpython-36.pyc
│   │           │   │   │   │   ├── sun.cpython-36.pyc
│   │           │   │   │   │   └── vast.cpython-36.pyc
│   │           │   │   │   ├── sun.py
│   │           │   │   │   └── vast.py
│   │           │   │   ├── from_template.py
│   │           │   │   ├── info.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── intelccompiler.py
│   │           │   │   ├── lib2def.py
│   │           │   │   ├── line_endings.py
│   │           │   │   ├── log.py
│   │           │   │   ├── mingw
│   │           │   │   │   └── gfortran_vs2003_hack.c
│   │           │   │   ├── mingw32ccompiler.py
│   │           │   │   ├── misc_util.py
│   │           │   │   ├── msvc9compiler.py
│   │           │   │   ├── msvccompiler.py
│   │           │   │   ├── npy_pkg_config.py
│   │           │   │   ├── numpy_distribution.py
│   │           │   │   ├── pathccompiler.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── ccompiler.cpython-36.pyc
│   │           │   │   │   ├── compat.cpython-36.pyc
│   │           │   │   │   ├── __config__.cpython-36.pyc
│   │           │   │   │   ├── conv_template.cpython-36.pyc
│   │           │   │   │   ├── core.cpython-36.pyc
│   │           │   │   │   ├── cpuinfo.cpython-36.pyc
│   │           │   │   │   ├── exec_command.cpython-36.pyc
│   │           │   │   │   ├── extension.cpython-36.pyc
│   │           │   │   │   ├── from_template.cpython-36.pyc
│   │           │   │   │   ├── info.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── intelccompiler.cpython-36.pyc
│   │           │   │   │   ├── lib2def.cpython-36.pyc
│   │           │   │   │   ├── line_endings.cpython-36.pyc
│   │           │   │   │   ├── log.cpython-36.pyc
│   │           │   │   │   ├── mingw32ccompiler.cpython-36.pyc
│   │           │   │   │   ├── misc_util.cpython-36.pyc
│   │           │   │   │   ├── msvc9compiler.cpython-36.pyc
│   │           │   │   │   ├── msvccompiler.cpython-36.pyc
│   │           │   │   │   ├── npy_pkg_config.cpython-36.pyc
│   │           │   │   │   ├── numpy_distribution.cpython-36.pyc
│   │           │   │   │   ├── pathccompiler.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   ├── _shell_utils.cpython-36.pyc
│   │           │   │   │   ├── system_info.cpython-36.pyc
│   │           │   │   │   ├── unixccompiler.cpython-36.pyc
│   │           │   │   │   └── __version__.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   ├── _shell_utils.py
│   │           │   │   ├── system_info.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_exec_command.cpython-36.pyc
│   │           │   │   │   │   ├── test_fcompiler.cpython-36.pyc
│   │           │   │   │   │   ├── test_fcompiler_gnu.cpython-36.pyc
│   │           │   │   │   │   ├── test_fcompiler_intel.cpython-36.pyc
│   │           │   │   │   │   ├── test_fcompiler_nagfor.cpython-36.pyc
│   │           │   │   │   │   ├── test_from_template.cpython-36.pyc
│   │           │   │   │   │   ├── test_misc_util.cpython-36.pyc
│   │           │   │   │   │   ├── test_npy_pkg_config.cpython-36.pyc
│   │           │   │   │   │   ├── test_shell_utils.cpython-36.pyc
│   │           │   │   │   │   └── test_system_info.cpython-36.pyc
│   │           │   │   │   ├── test_exec_command.py
│   │           │   │   │   ├── test_fcompiler_gnu.py
│   │           │   │   │   ├── test_fcompiler_intel.py
│   │           │   │   │   ├── test_fcompiler_nagfor.py
│   │           │   │   │   ├── test_fcompiler.py
│   │           │   │   │   ├── test_from_template.py
│   │           │   │   │   ├── test_misc_util.py
│   │           │   │   │   ├── test_npy_pkg_config.py
│   │           │   │   │   ├── test_shell_utils.py
│   │           │   │   │   └── test_system_info.py
│   │           │   │   ├── unixccompiler.py
│   │           │   │   └── __version__.py
│   │           │   ├── doc
│   │           │   │   ├── basics.py
│   │           │   │   ├── broadcasting.py
│   │           │   │   ├── byteswapping.py
│   │           │   │   ├── constants.py
│   │           │   │   ├── creation.py
│   │           │   │   ├── glossary.py
│   │           │   │   ├── indexing.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── internals.py
│   │           │   │   ├── misc.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── basics.cpython-36.pyc
│   │           │   │   │   ├── broadcasting.cpython-36.pyc
│   │           │   │   │   ├── byteswapping.cpython-36.pyc
│   │           │   │   │   ├── constants.cpython-36.pyc
│   │           │   │   │   ├── creation.cpython-36.pyc
│   │           │   │   │   ├── glossary.cpython-36.pyc
│   │           │   │   │   ├── indexing.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── internals.cpython-36.pyc
│   │           │   │   │   ├── misc.cpython-36.pyc
│   │           │   │   │   ├── structured_arrays.cpython-36.pyc
│   │           │   │   │   ├── subclassing.cpython-36.pyc
│   │           │   │   │   └── ufuncs.cpython-36.pyc
│   │           │   │   ├── structured_arrays.py
│   │           │   │   ├── subclassing.py
│   │           │   │   └── ufuncs.py
│   │           │   ├── dual.py
│   │           │   ├── f2py
│   │           │   │   ├── auxfuncs.py
│   │           │   │   ├── capi_maps.py
│   │           │   │   ├── cb_rules.py
│   │           │   │   ├── cfuncs.py
│   │           │   │   ├── common_rules.py
│   │           │   │   ├── crackfortran.py
│   │           │   │   ├── diagnose.py
│   │           │   │   ├── f2py2e.py
│   │           │   │   ├── f2py_testing.py
│   │           │   │   ├── f90mod_rules.py
│   │           │   │   ├── func2subr.py
│   │           │   │   ├── info.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __main__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── auxfuncs.cpython-36.pyc
│   │           │   │   │   ├── capi_maps.cpython-36.pyc
│   │           │   │   │   ├── cb_rules.cpython-36.pyc
│   │           │   │   │   ├── cfuncs.cpython-36.pyc
│   │           │   │   │   ├── common_rules.cpython-36.pyc
│   │           │   │   │   ├── crackfortran.cpython-36.pyc
│   │           │   │   │   ├── diagnose.cpython-36.pyc
│   │           │   │   │   ├── f2py2e.cpython-36.pyc
│   │           │   │   │   ├── f2py_testing.cpython-36.pyc
│   │           │   │   │   ├── f90mod_rules.cpython-36.pyc
│   │           │   │   │   ├── func2subr.cpython-36.pyc
│   │           │   │   │   ├── info.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── __main__.cpython-36.pyc
│   │           │   │   │   ├── rules.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   ├── use_rules.cpython-36.pyc
│   │           │   │   │   └── __version__.cpython-36.pyc
│   │           │   │   ├── rules.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── src
│   │           │   │   │   ├── fortranobject.c
│   │           │   │   │   └── fortranobject.h
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_array_from_pyobj.cpython-36.pyc
│   │           │   │   │   │   ├── test_assumed_shape.cpython-36.pyc
│   │           │   │   │   │   ├── test_block_docstring.cpython-36.pyc
│   │           │   │   │   │   ├── test_callback.cpython-36.pyc
│   │           │   │   │   │   ├── test_common.cpython-36.pyc
│   │           │   │   │   │   ├── test_compile_function.cpython-36.pyc
│   │           │   │   │   │   ├── test_kind.cpython-36.pyc
│   │           │   │   │   │   ├── test_mixed.cpython-36.pyc
│   │           │   │   │   │   ├── test_parameter.cpython-36.pyc
│   │           │   │   │   │   ├── test_quoted_character.cpython-36.pyc
│   │           │   │   │   │   ├── test_regression.cpython-36.pyc
│   │           │   │   │   │   ├── test_return_character.cpython-36.pyc
│   │           │   │   │   │   ├── test_return_complex.cpython-36.pyc
│   │           │   │   │   │   ├── test_return_integer.cpython-36.pyc
│   │           │   │   │   │   ├── test_return_logical.cpython-36.pyc
│   │           │   │   │   │   ├── test_return_real.cpython-36.pyc
│   │           │   │   │   │   ├── test_semicolon_split.cpython-36.pyc
│   │           │   │   │   │   ├── test_size.cpython-36.pyc
│   │           │   │   │   │   ├── test_string.cpython-36.pyc
│   │           │   │   │   │   └── util.cpython-36.pyc
│   │           │   │   │   ├── src
│   │           │   │   │   │   ├── array_from_pyobj
│   │           │   │   │   │   │   └── wrapmodule.c
│   │           │   │   │   │   ├── assumed_shape
│   │           │   │   │   │   │   ├── .f2py_f2cmap
│   │           │   │   │   │   │   ├── foo_free.f90
│   │           │   │   │   │   │   ├── foo_mod.f90
│   │           │   │   │   │   │   ├── foo_use.f90
│   │           │   │   │   │   │   └── precision.f90
│   │           │   │   │   │   ├── common
│   │           │   │   │   │   │   └── block.f
│   │           │   │   │   │   ├── kind
│   │           │   │   │   │   │   └── foo.f90
│   │           │   │   │   │   ├── mixed
│   │           │   │   │   │   │   ├── foo.f
│   │           │   │   │   │   │   ├── foo_fixed.f90
│   │           │   │   │   │   │   └── foo_free.f90
│   │           │   │   │   │   ├── parameter
│   │           │   │   │   │   │   ├── constant_both.f90
│   │           │   │   │   │   │   ├── constant_compound.f90
│   │           │   │   │   │   │   ├── constant_integer.f90
│   │           │   │   │   │   │   ├── constant_non_compound.f90
│   │           │   │   │   │   │   └── constant_real.f90
│   │           │   │   │   │   ├── regression
│   │           │   │   │   │   │   └── inout.f90
│   │           │   │   │   │   ├── size
│   │           │   │   │   │   │   └── foo.f90
│   │           │   │   │   │   └── string
│   │           │   │   │   │       └── char.f90
│   │           │   │   │   ├── test_array_from_pyobj.py
│   │           │   │   │   ├── test_assumed_shape.py
│   │           │   │   │   ├── test_block_docstring.py
│   │           │   │   │   ├── test_callback.py
│   │           │   │   │   ├── test_common.py
│   │           │   │   │   ├── test_compile_function.py
│   │           │   │   │   ├── test_kind.py
│   │           │   │   │   ├── test_mixed.py
│   │           │   │   │   ├── test_parameter.py
│   │           │   │   │   ├── test_quoted_character.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   ├── test_return_character.py
│   │           │   │   │   ├── test_return_complex.py
│   │           │   │   │   ├── test_return_integer.py
│   │           │   │   │   ├── test_return_logical.py
│   │           │   │   │   ├── test_return_real.py
│   │           │   │   │   ├── test_semicolon_split.py
│   │           │   │   │   ├── test_size.py
│   │           │   │   │   ├── test_string.py
│   │           │   │   │   └── util.py
│   │           │   │   ├── use_rules.py
│   │           │   │   └── __version__.py
│   │           │   ├── fft
│   │           │   │   ├── fftpack_lite.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── fftpack.py
│   │           │   │   ├── helper.py
│   │           │   │   ├── info.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── fftpack.cpython-36.pyc
│   │           │   │   │   ├── helper.cpython-36.pyc
│   │           │   │   │   ├── info.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── setup.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_fftpack.cpython-36.pyc
│   │           │   │       │   └── test_helper.cpython-36.pyc
│   │           │   │       ├── test_fftpack.py
│   │           │   │       └── test_helper.py
│   │           │   ├── _globals.py
│   │           │   ├── __init__.py
│   │           │   ├── lib
│   │           │   │   ├── arraypad.py
│   │           │   │   ├── arraysetops.py
│   │           │   │   ├── arrayterator.py
│   │           │   │   ├── _datasource.py
│   │           │   │   ├── financial.py
│   │           │   │   ├── format.py
│   │           │   │   ├── function_base.py
│   │           │   │   ├── histograms.py
│   │           │   │   ├── index_tricks.py
│   │           │   │   ├── info.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _iotools.py
│   │           │   │   ├── mixins.py
│   │           │   │   ├── nanfunctions.py
│   │           │   │   ├── npyio.py
│   │           │   │   ├── polynomial.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── arraypad.cpython-36.pyc
│   │           │   │   │   ├── arraysetops.cpython-36.pyc
│   │           │   │   │   ├── arrayterator.cpython-36.pyc
│   │           │   │   │   ├── _datasource.cpython-36.pyc
│   │           │   │   │   ├── financial.cpython-36.pyc
│   │           │   │   │   ├── format.cpython-36.pyc
│   │           │   │   │   ├── function_base.cpython-36.pyc
│   │           │   │   │   ├── histograms.cpython-36.pyc
│   │           │   │   │   ├── index_tricks.cpython-36.pyc
│   │           │   │   │   ├── info.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── _iotools.cpython-36.pyc
│   │           │   │   │   ├── mixins.cpython-36.pyc
│   │           │   │   │   ├── nanfunctions.cpython-36.pyc
│   │           │   │   │   ├── npyio.cpython-36.pyc
│   │           │   │   │   ├── polynomial.cpython-36.pyc
│   │           │   │   │   ├── recfunctions.cpython-36.pyc
│   │           │   │   │   ├── scimath.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   ├── shape_base.cpython-36.pyc
│   │           │   │   │   ├── stride_tricks.cpython-36.pyc
│   │           │   │   │   ├── twodim_base.cpython-36.pyc
│   │           │   │   │   ├── type_check.cpython-36.pyc
│   │           │   │   │   ├── ufunclike.cpython-36.pyc
│   │           │   │   │   ├── user_array.cpython-36.pyc
│   │           │   │   │   ├── utils.cpython-36.pyc
│   │           │   │   │   └── _version.cpython-36.pyc
│   │           │   │   ├── recfunctions.py
│   │           │   │   ├── scimath.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── shape_base.py
│   │           │   │   ├── stride_tricks.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── py2-objarr.npy
│   │           │   │   │   │   ├── py2-objarr.npz
│   │           │   │   │   │   ├── py3-objarr.npy
│   │           │   │   │   │   ├── py3-objarr.npz
│   │           │   │   │   │   ├── python3.npy
│   │           │   │   │   │   └── win64python2.npy
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_arraypad.cpython-36.pyc
│   │           │   │   │   │   ├── test_arraysetops.cpython-36.pyc
│   │           │   │   │   │   ├── test_arrayterator.cpython-36.pyc
│   │           │   │   │   │   ├── test__datasource.cpython-36.pyc
│   │           │   │   │   │   ├── test_financial.cpython-36.pyc
│   │           │   │   │   │   ├── test_format.cpython-36.pyc
│   │           │   │   │   │   ├── test_function_base.cpython-36.pyc
│   │           │   │   │   │   ├── test_histograms.cpython-36.pyc
│   │           │   │   │   │   ├── test_index_tricks.cpython-36.pyc
│   │           │   │   │   │   ├── test_io.cpython-36.pyc
│   │           │   │   │   │   ├── test__iotools.cpython-36.pyc
│   │           │   │   │   │   ├── test_mixins.cpython-36.pyc
│   │           │   │   │   │   ├── test_nanfunctions.cpython-36.pyc
│   │           │   │   │   │   ├── test_packbits.cpython-36.pyc
│   │           │   │   │   │   ├── test_polynomial.cpython-36.pyc
│   │           │   │   │   │   ├── test_recfunctions.cpython-36.pyc
│   │           │   │   │   │   ├── test_regression.cpython-36.pyc
│   │           │   │   │   │   ├── test_shape_base.cpython-36.pyc
│   │           │   │   │   │   ├── test_stride_tricks.cpython-36.pyc
│   │           │   │   │   │   ├── test_twodim_base.cpython-36.pyc
│   │           │   │   │   │   ├── test_type_check.cpython-36.pyc
│   │           │   │   │   │   ├── test_ufunclike.cpython-36.pyc
│   │           │   │   │   │   ├── test_utils.cpython-36.pyc
│   │           │   │   │   │   └── test__version.cpython-36.pyc
│   │           │   │   │   ├── test_arraypad.py
│   │           │   │   │   ├── test_arraysetops.py
│   │           │   │   │   ├── test_arrayterator.py
│   │           │   │   │   ├── test__datasource.py
│   │           │   │   │   ├── test_financial.py
│   │           │   │   │   ├── test_format.py
│   │           │   │   │   ├── test_function_base.py
│   │           │   │   │   ├── test_histograms.py
│   │           │   │   │   ├── test_index_tricks.py
│   │           │   │   │   ├── test_io.py
│   │           │   │   │   ├── test__iotools.py
│   │           │   │   │   ├── test_mixins.py
│   │           │   │   │   ├── test_nanfunctions.py
│   │           │   │   │   ├── test_packbits.py
│   │           │   │   │   ├── test_polynomial.py
│   │           │   │   │   ├── test_recfunctions.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   ├── test_shape_base.py
│   │           │   │   │   ├── test_stride_tricks.py
│   │           │   │   │   ├── test_twodim_base.py
│   │           │   │   │   ├── test_type_check.py
│   │           │   │   │   ├── test_ufunclike.py
│   │           │   │   │   ├── test_utils.py
│   │           │   │   │   └── test__version.py
│   │           │   │   ├── twodim_base.py
│   │           │   │   ├── type_check.py
│   │           │   │   ├── ufunclike.py
│   │           │   │   ├── user_array.py
│   │           │   │   ├── utils.py
│   │           │   │   └── _version.py
│   │           │   ├── .libs
│   │           │   │   ├── libgfortran-ed201abd.so.3.0.0
│   │           │   │   └── libopenblasp-r0-382c8f3a.3.5.dev.so
│   │           │   ├── LICENSE.txt
│   │           │   ├── linalg
│   │           │   │   ├── info.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── lapack_lite.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── linalg.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── info.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── linalg.cpython-36.pyc
│   │           │   │   │   └── setup.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_build.cpython-36.pyc
│   │           │   │   │   │   ├── test_deprecations.cpython-36.pyc
│   │           │   │   │   │   ├── test_linalg.cpython-36.pyc
│   │           │   │   │   │   └── test_regression.cpython-36.pyc
│   │           │   │   │   ├── test_build.py
│   │           │   │   │   ├── test_deprecations.py
│   │           │   │   │   ├── test_linalg.py
│   │           │   │   │   └── test_regression.py
│   │           │   │   └── _umath_linalg.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── ma
│   │           │   │   ├── bench.py
│   │           │   │   ├── core.py
│   │           │   │   ├── extras.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── mrecords.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── bench.cpython-36.pyc
│   │           │   │   │   ├── core.cpython-36.pyc
│   │           │   │   │   ├── extras.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── mrecords.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   ├── testutils.cpython-36.pyc
│   │           │   │   │   ├── timer_comparison.cpython-36.pyc
│   │           │   │   │   └── version.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_core.cpython-36.pyc
│   │           │   │   │   │   ├── test_deprecations.cpython-36.pyc
│   │           │   │   │   │   ├── test_extras.cpython-36.pyc
│   │           │   │   │   │   ├── test_mrecords.cpython-36.pyc
│   │           │   │   │   │   ├── test_old_ma.cpython-36.pyc
│   │           │   │   │   │   ├── test_regression.cpython-36.pyc
│   │           │   │   │   │   └── test_subclassing.cpython-36.pyc
│   │           │   │   │   ├── test_core.py
│   │           │   │   │   ├── test_deprecations.py
│   │           │   │   │   ├── test_extras.py
│   │           │   │   │   ├── test_mrecords.py
│   │           │   │   │   ├── test_old_ma.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   └── test_subclassing.py
│   │           │   │   ├── testutils.py
│   │           │   │   ├── timer_comparison.py
│   │           │   │   └── version.py
│   │           │   ├── matlib.py
│   │           │   ├── matrixlib
│   │           │   │   ├── defmatrix.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── defmatrix.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── setup.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_defmatrix.cpython-36.pyc
│   │           │   │       │   ├── test_interaction.cpython-36.pyc
│   │           │   │       │   ├── test_masked_matrix.cpython-36.pyc
│   │           │   │       │   ├── test_matrix_linalg.cpython-36.pyc
│   │           │   │       │   ├── test_multiarray.cpython-36.pyc
│   │           │   │       │   ├── test_numeric.cpython-36.pyc
│   │           │   │       │   └── test_regression.cpython-36.pyc
│   │           │   │       ├── test_defmatrix.py
│   │           │   │       ├── test_interaction.py
│   │           │   │       ├── test_masked_matrix.py
│   │           │   │       ├── test_matrix_linalg.py
│   │           │   │       ├── test_multiarray.py
│   │           │   │       ├── test_numeric.py
│   │           │   │       └── test_regression.py
│   │           │   ├── polynomial
│   │           │   │   ├── chebyshev.py
│   │           │   │   ├── hermite_e.py
│   │           │   │   ├── hermite.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── laguerre.py
│   │           │   │   ├── legendre.py
│   │           │   │   ├── _polybase.py
│   │           │   │   ├── polynomial.py
│   │           │   │   ├── polyutils.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── chebyshev.cpython-36.pyc
│   │           │   │   │   ├── hermite.cpython-36.pyc
│   │           │   │   │   ├── hermite_e.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── laguerre.cpython-36.pyc
│   │           │   │   │   ├── legendre.cpython-36.pyc
│   │           │   │   │   ├── _polybase.cpython-36.pyc
│   │           │   │   │   ├── polynomial.cpython-36.pyc
│   │           │   │   │   ├── polyutils.cpython-36.pyc
│   │           │   │   │   └── setup.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_chebyshev.cpython-36.pyc
│   │           │   │       │   ├── test_classes.cpython-36.pyc
│   │           │   │       │   ├── test_hermite.cpython-36.pyc
│   │           │   │       │   ├── test_hermite_e.cpython-36.pyc
│   │           │   │       │   ├── test_laguerre.cpython-36.pyc
│   │           │   │       │   ├── test_legendre.cpython-36.pyc
│   │           │   │       │   ├── test_polynomial.cpython-36.pyc
│   │           │   │       │   ├── test_polyutils.cpython-36.pyc
│   │           │   │       │   └── test_printing.cpython-36.pyc
│   │           │   │       ├── test_chebyshev.py
│   │           │   │       ├── test_classes.py
│   │           │   │       ├── test_hermite_e.py
│   │           │   │       ├── test_hermite.py
│   │           │   │       ├── test_laguerre.py
│   │           │   │       ├── test_legendre.py
│   │           │   │       ├── test_polynomial.py
│   │           │   │       ├── test_polyutils.py
│   │           │   │       └── test_printing.py
│   │           │   ├── __pycache__
│   │           │   │   ├── __config__.cpython-36.pyc
│   │           │   │   ├── conftest.cpython-36.pyc
│   │           │   │   ├── ctypeslib.cpython-36.pyc
│   │           │   │   ├── _distributor_init.cpython-36.pyc
│   │           │   │   ├── dual.cpython-36.pyc
│   │           │   │   ├── _globals.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── matlib.cpython-36.pyc
│   │           │   │   ├── _pytesttester.cpython-36.pyc
│   │           │   │   ├── setup.cpython-36.pyc
│   │           │   │   └── version.cpython-36.pyc
│   │           │   ├── _pytesttester.py
│   │           │   ├── random
│   │           │   │   ├── info.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── mtrand.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── info.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── setup.cpython-36.pyc
│   │           │   │   ├── randomkit.h
│   │           │   │   ├── setup.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_random.cpython-36.pyc
│   │           │   │       │   └── test_regression.cpython-36.pyc
│   │           │   │       ├── test_random.py
│   │           │   │       └── test_regression.py
│   │           │   ├── setup.py
│   │           │   ├── testing
│   │           │   │   ├── decorators.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── noseclasses.py
│   │           │   │   ├── nosetester.py
│   │           │   │   ├── print_coercion_tables.py
│   │           │   │   ├── _private
│   │           │   │   │   ├── decorators.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── noseclasses.py
│   │           │   │   │   ├── nosetester.py
│   │           │   │   │   ├── parameterized.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── decorators.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── noseclasses.cpython-36.pyc
│   │           │   │   │   │   ├── nosetester.cpython-36.pyc
│   │           │   │   │   │   ├── parameterized.cpython-36.pyc
│   │           │   │   │   │   └── utils.cpython-36.pyc
│   │           │   │   │   └── utils.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── decorators.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── noseclasses.cpython-36.pyc
│   │           │   │   │   ├── nosetester.cpython-36.pyc
│   │           │   │   │   ├── print_coercion_tables.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   └── utils.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_decorators.cpython-36.pyc
│   │           │   │   │   │   ├── test_doctesting.cpython-36.pyc
│   │           │   │   │   │   └── test_utils.cpython-36.pyc
│   │           │   │   │   ├── test_decorators.py
│   │           │   │   │   ├── test_doctesting.py
│   │           │   │   │   └── test_utils.py
│   │           │   │   └── utils.py
│   │           │   ├── tests
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── test_ctypeslib.cpython-36.pyc
│   │           │   │   │   ├── test_matlib.cpython-36.pyc
│   │           │   │   │   ├── test_numpy_version.cpython-36.pyc
│   │           │   │   │   ├── test_public_api.cpython-36.pyc
│   │           │   │   │   ├── test_reloading.cpython-36.pyc
│   │           │   │   │   ├── test_scripts.cpython-36.pyc
│   │           │   │   │   └── test_warnings.cpython-36.pyc
│   │           │   │   ├── test_ctypeslib.py
│   │           │   │   ├── test_matlib.py
│   │           │   │   ├── test_numpy_version.py
│   │           │   │   ├── test_public_api.py
│   │           │   │   ├── test_reloading.py
│   │           │   │   ├── test_scripts.py
│   │           │   │   └── test_warnings.py
│   │           │   └── version.py
│   │           ├── numpy-1.16.3.dist-info
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── pandas
│   │           │   ├── api
│   │           │   │   ├── extensions
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   └── types
│   │           │   │       ├── __init__.py
│   │           │   │       └── __pycache__
│   │           │   │           └── __init__.cpython-36.pyc
│   │           │   ├── arrays
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── compat
│   │           │   │   ├── chainmap_impl.py
│   │           │   │   ├── chainmap.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── numpy
│   │           │   │   │   ├── function.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── function.cpython-36.pyc
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   ├── pickle_compat.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── chainmap.cpython-36.pyc
│   │           │   │       ├── chainmap_impl.cpython-36.pyc
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       └── pickle_compat.cpython-36.pyc
│   │           │   ├── conftest.py
│   │           │   ├── core
│   │           │   │   ├── accessor.py
│   │           │   │   ├── algorithms.py
│   │           │   │   ├── api.py
│   │           │   │   ├── apply.py
│   │           │   │   ├── arrays
│   │           │   │   │   ├── array_.py
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── categorical.py
│   │           │   │   │   ├── datetimelike.py
│   │           │   │   │   ├── datetimes.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── integer.py
│   │           │   │   │   ├── interval.py
│   │           │   │   │   ├── numpy_.py
│   │           │   │   │   ├── period.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── array_.cpython-36.pyc
│   │           │   │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   │   ├── categorical.cpython-36.pyc
│   │           │   │   │   │   ├── datetimelike.cpython-36.pyc
│   │           │   │   │   │   ├── datetimes.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── integer.cpython-36.pyc
│   │           │   │   │   │   ├── interval.cpython-36.pyc
│   │           │   │   │   │   ├── numpy_.cpython-36.pyc
│   │           │   │   │   │   ├── period.cpython-36.pyc
│   │           │   │   │   │   ├── _ranges.cpython-36.pyc
│   │           │   │   │   │   ├── sparse.cpython-36.pyc
│   │           │   │   │   │   └── timedeltas.cpython-36.pyc
│   │           │   │   │   ├── _ranges.py
│   │           │   │   │   ├── sparse.py
│   │           │   │   │   └── timedeltas.py
│   │           │   │   ├── base.py
│   │           │   │   ├── categorical.py
│   │           │   │   ├── common.py
│   │           │   │   ├── computation
│   │           │   │   │   ├── align.py
│   │           │   │   │   ├── api.py
│   │           │   │   │   ├── check.py
│   │           │   │   │   ├── common.py
│   │           │   │   │   ├── engines.py
│   │           │   │   │   ├── eval.py
│   │           │   │   │   ├── expressions.py
│   │           │   │   │   ├── expr.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── ops.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── align.cpython-36.pyc
│   │           │   │   │   │   ├── api.cpython-36.pyc
│   │           │   │   │   │   ├── check.cpython-36.pyc
│   │           │   │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   │   ├── engines.cpython-36.pyc
│   │           │   │   │   │   ├── eval.cpython-36.pyc
│   │           │   │   │   │   ├── expr.cpython-36.pyc
│   │           │   │   │   │   ├── expressions.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── ops.cpython-36.pyc
│   │           │   │   │   │   ├── pytables.cpython-36.pyc
│   │           │   │   │   │   └── scope.cpython-36.pyc
│   │           │   │   │   ├── pytables.py
│   │           │   │   │   └── scope.py
│   │           │   │   ├── config_init.py
│   │           │   │   ├── config.py
│   │           │   │   ├── dtypes
│   │           │   │   │   ├── api.py
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── cast.py
│   │           │   │   │   ├── common.py
│   │           │   │   │   ├── concat.py
│   │           │   │   │   ├── dtypes.py
│   │           │   │   │   ├── generic.py
│   │           │   │   │   ├── inference.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── missing.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── api.cpython-36.pyc
│   │           │   │   │       ├── base.cpython-36.pyc
│   │           │   │   │       ├── cast.cpython-36.pyc
│   │           │   │   │       ├── common.cpython-36.pyc
│   │           │   │   │       ├── concat.cpython-36.pyc
│   │           │   │   │       ├── dtypes.cpython-36.pyc
│   │           │   │   │       ├── generic.cpython-36.pyc
│   │           │   │   │       ├── inference.cpython-36.pyc
│   │           │   │   │       ├── __init__.cpython-36.pyc
│   │           │   │   │       └── missing.cpython-36.pyc
│   │           │   │   ├── frame.py
│   │           │   │   ├── generic.py
│   │           │   │   ├── groupby
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── categorical.py
│   │           │   │   │   ├── generic.py
│   │           │   │   │   ├── groupby.py
│   │           │   │   │   ├── grouper.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── ops.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── base.cpython-36.pyc
│   │           │   │   │       ├── categorical.cpython-36.pyc
│   │           │   │   │       ├── generic.cpython-36.pyc
│   │           │   │   │       ├── groupby.cpython-36.pyc
│   │           │   │   │       ├── grouper.cpython-36.pyc
│   │           │   │   │       ├── __init__.cpython-36.pyc
│   │           │   │   │       └── ops.cpython-36.pyc
│   │           │   │   ├── indexes
│   │           │   │   │   ├── accessors.py
│   │           │   │   │   ├── api.py
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── category.py
│   │           │   │   │   ├── datetimelike.py
│   │           │   │   │   ├── datetimes.py
│   │           │   │   │   ├── frozen.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── interval.py
│   │           │   │   │   ├── multi.py
│   │           │   │   │   ├── numeric.py
│   │           │   │   │   ├── period.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── accessors.cpython-36.pyc
│   │           │   │   │   │   ├── api.cpython-36.pyc
│   │           │   │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   │   ├── category.cpython-36.pyc
│   │           │   │   │   │   ├── datetimelike.cpython-36.pyc
│   │           │   │   │   │   ├── datetimes.cpython-36.pyc
│   │           │   │   │   │   ├── frozen.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── interval.cpython-36.pyc
│   │           │   │   │   │   ├── multi.cpython-36.pyc
│   │           │   │   │   │   ├── numeric.cpython-36.pyc
│   │           │   │   │   │   ├── period.cpython-36.pyc
│   │           │   │   │   │   ├── range.cpython-36.pyc
│   │           │   │   │   │   └── timedeltas.cpython-36.pyc
│   │           │   │   │   ├── range.py
│   │           │   │   │   └── timedeltas.py
│   │           │   │   ├── indexing.py
│   │           │   │   ├── index.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── internals
│   │           │   │   │   ├── arrays.py
│   │           │   │   │   ├── blocks.py
│   │           │   │   │   ├── concat.py
│   │           │   │   │   ├── construction.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── managers.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── arrays.cpython-36.pyc
│   │           │   │   │       ├── blocks.cpython-36.pyc
│   │           │   │   │       ├── concat.cpython-36.pyc
│   │           │   │   │       ├── construction.cpython-36.pyc
│   │           │   │   │       ├── __init__.cpython-36.pyc
│   │           │   │   │       └── managers.cpython-36.pyc
│   │           │   │   ├── missing.py
│   │           │   │   ├── nanops.py
│   │           │   │   ├── ops.py
│   │           │   │   ├── panel.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── accessor.cpython-36.pyc
│   │           │   │   │   ├── algorithms.cpython-36.pyc
│   │           │   │   │   ├── api.cpython-36.pyc
│   │           │   │   │   ├── apply.cpython-36.pyc
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── categorical.cpython-36.pyc
│   │           │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   ├── config.cpython-36.pyc
│   │           │   │   │   ├── config_init.cpython-36.pyc
│   │           │   │   │   ├── frame.cpython-36.pyc
│   │           │   │   │   ├── generic.cpython-36.pyc
│   │           │   │   │   ├── index.cpython-36.pyc
│   │           │   │   │   ├── indexing.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── missing.cpython-36.pyc
│   │           │   │   │   ├── nanops.cpython-36.pyc
│   │           │   │   │   ├── ops.cpython-36.pyc
│   │           │   │   │   ├── panel.cpython-36.pyc
│   │           │   │   │   ├── resample.cpython-36.pyc
│   │           │   │   │   ├── series.cpython-36.pyc
│   │           │   │   │   ├── sorting.cpython-36.pyc
│   │           │   │   │   ├── strings.cpython-36.pyc
│   │           │   │   │   └── window.cpython-36.pyc
│   │           │   │   ├── resample.py
│   │           │   │   ├── reshape
│   │           │   │   │   ├── api.py
│   │           │   │   │   ├── concat.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── melt.py
│   │           │   │   │   ├── merge.py
│   │           │   │   │   ├── pivot.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── api.cpython-36.pyc
│   │           │   │   │   │   ├── concat.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── melt.cpython-36.pyc
│   │           │   │   │   │   ├── merge.cpython-36.pyc
│   │           │   │   │   │   ├── pivot.cpython-36.pyc
│   │           │   │   │   │   ├── reshape.cpython-36.pyc
│   │           │   │   │   │   ├── tile.cpython-36.pyc
│   │           │   │   │   │   └── util.cpython-36.pyc
│   │           │   │   │   ├── reshape.py
│   │           │   │   │   ├── tile.py
│   │           │   │   │   └── util.py
│   │           │   │   ├── series.py
│   │           │   │   ├── sorting.py
│   │           │   │   ├── sparse
│   │           │   │   │   ├── api.py
│   │           │   │   │   ├── frame.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── api.cpython-36.pyc
│   │           │   │   │   │   ├── frame.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── scipy_sparse.cpython-36.pyc
│   │           │   │   │   │   └── series.cpython-36.pyc
│   │           │   │   │   ├── scipy_sparse.py
│   │           │   │   │   └── series.py
│   │           │   │   ├── strings.py
│   │           │   │   ├── tools
│   │           │   │   │   ├── datetimes.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── numeric.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── datetimes.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── numeric.cpython-36.pyc
│   │           │   │   │   │   └── timedeltas.cpython-36.pyc
│   │           │   │   │   └── timedeltas.py
│   │           │   │   ├── util
│   │           │   │   │   ├── hashing.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── hashing.cpython-36.pyc
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   └── window.py
│   │           │   ├── errors
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── __init__.py
│   │           │   ├── io
│   │           │   │   ├── api.py
│   │           │   │   ├── clipboard
│   │           │   │   │   ├── clipboards.py
│   │           │   │   │   ├── exceptions.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── clipboards.cpython-36.pyc
│   │           │   │   │   │   ├── exceptions.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── windows.cpython-36.pyc
│   │           │   │   │   └── windows.py
│   │           │   │   ├── clipboards.py
│   │           │   │   ├── common.py
│   │           │   │   ├── date_converters.py
│   │           │   │   ├── excel.py
│   │           │   │   ├── feather_format.py
│   │           │   │   ├── formats
│   │           │   │   │   ├── console.py
│   │           │   │   │   ├── css.py
│   │           │   │   │   ├── csvs.py
│   │           │   │   │   ├── excel.py
│   │           │   │   │   ├── format.py
│   │           │   │   │   ├── html.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── latex.py
│   │           │   │   │   ├── printing.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── console.cpython-36.pyc
│   │           │   │   │   │   ├── css.cpython-36.pyc
│   │           │   │   │   │   ├── csvs.cpython-36.pyc
│   │           │   │   │   │   ├── excel.cpython-36.pyc
│   │           │   │   │   │   ├── format.cpython-36.pyc
│   │           │   │   │   │   ├── html.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── latex.cpython-36.pyc
│   │           │   │   │   │   ├── printing.cpython-36.pyc
│   │           │   │   │   │   ├── style.cpython-36.pyc
│   │           │   │   │   │   └── terminal.cpython-36.pyc
│   │           │   │   │   ├── style.py
│   │           │   │   │   ├── templates
│   │           │   │   │   │   └── html.tpl
│   │           │   │   │   └── terminal.py
│   │           │   │   ├── gbq.py
│   │           │   │   ├── gcs.py
│   │           │   │   ├── html.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── json
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── json.py
│   │           │   │   │   ├── normalize.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── json.cpython-36.pyc
│   │           │   │   │   │   ├── normalize.cpython-36.pyc
│   │           │   │   │   │   └── table_schema.cpython-36.pyc
│   │           │   │   │   └── table_schema.py
│   │           │   │   ├── msgpack
│   │           │   │   │   ├── exceptions.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _packer.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── exceptions.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── _version.cpython-36.pyc
│   │           │   │   │   ├── _unpacker.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   └── _version.py
│   │           │   │   ├── packers.py
│   │           │   │   ├── parquet.py
│   │           │   │   ├── parsers.py
│   │           │   │   ├── pickle.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── api.cpython-36.pyc
│   │           │   │   │   ├── clipboards.cpython-36.pyc
│   │           │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   ├── date_converters.cpython-36.pyc
│   │           │   │   │   ├── excel.cpython-36.pyc
│   │           │   │   │   ├── feather_format.cpython-36.pyc
│   │           │   │   │   ├── gbq.cpython-36.pyc
│   │           │   │   │   ├── gcs.cpython-36.pyc
│   │           │   │   │   ├── html.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── packers.cpython-36.pyc
│   │           │   │   │   ├── parquet.cpython-36.pyc
│   │           │   │   │   ├── parsers.cpython-36.pyc
│   │           │   │   │   ├── pickle.cpython-36.pyc
│   │           │   │   │   ├── pytables.cpython-36.pyc
│   │           │   │   │   ├── s3.cpython-36.pyc
│   │           │   │   │   ├── sql.cpython-36.pyc
│   │           │   │   │   └── stata.cpython-36.pyc
│   │           │   │   ├── pytables.py
│   │           │   │   ├── s3.py
│   │           │   │   ├── sas
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── sas7bdat.cpython-36.pyc
│   │           │   │   │   │   ├── sas_constants.cpython-36.pyc
│   │           │   │   │   │   ├── sasreader.cpython-36.pyc
│   │           │   │   │   │   └── sas_xport.cpython-36.pyc
│   │           │   │   │   ├── sas7bdat.py
│   │           │   │   │   ├── sas_constants.py
│   │           │   │   │   ├── _sas.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── sasreader.py
│   │           │   │   │   └── sas_xport.py
│   │           │   │   ├── sql.py
│   │           │   │   └── stata.py
│   │           │   ├── _libs
│   │           │   │   ├── algos.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── groupby.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── hashing.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── hashtable.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── index.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── indexing.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── __init__.py
│   │           │   │   ├── internals.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── interval.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── join.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── json.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── lib.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── missing.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── ops.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── parsers.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── properties.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   ├── reduction.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── reshape.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── skiplist.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── sparse.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── testing.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── tslib.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── tslibs
│   │           │   │   │   ├── ccalendar.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── conversion.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── fields.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── frequencies.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── nattype.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── np_datetime.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── offsets.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── parsing.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── period.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   │   ├── resolution.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── strptime.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── timedeltas.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── timestamps.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   └── timezones.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── window.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   └── writers.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── plotting
│   │           │   │   ├── _compat.py
│   │           │   │   ├── _converter.py
│   │           │   │   ├── _core.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _misc.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _compat.cpython-36.pyc
│   │           │   │   │   ├── _converter.cpython-36.pyc
│   │           │   │   │   ├── _core.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── _misc.cpython-36.pyc
│   │           │   │   │   ├── _style.cpython-36.pyc
│   │           │   │   │   ├── _timeseries.cpython-36.pyc
│   │           │   │   │   └── _tools.cpython-36.pyc
│   │           │   │   ├── _style.py
│   │           │   │   ├── _timeseries.py
│   │           │   │   └── _tools.py
│   │           │   ├── __pycache__
│   │           │   │   ├── conftest.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── testing.cpython-36.pyc
│   │           │   │   └── _version.cpython-36.pyc
│   │           │   ├── testing.py
│   │           │   ├── tests
│   │           │   │   ├── api
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_api.cpython-36.pyc
│   │           │   │   │   │   └── test_types.cpython-36.pyc
│   │           │   │   │   ├── test_api.py
│   │           │   │   │   └── test_types.py
│   │           │   │   ├── arithmetic
│   │           │   │   │   ├── conftest.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_datetime64.cpython-36.pyc
│   │           │   │   │   │   ├── test_numeric.cpython-36.pyc
│   │           │   │   │   │   ├── test_object.cpython-36.pyc
│   │           │   │   │   │   ├── test_period.cpython-36.pyc
│   │           │   │   │   │   └── test_timedelta64.cpython-36.pyc
│   │           │   │   │   ├── test_datetime64.py
│   │           │   │   │   ├── test_numeric.py
│   │           │   │   │   ├── test_object.py
│   │           │   │   │   ├── test_period.py
│   │           │   │   │   └── test_timedelta64.py
│   │           │   │   ├── arrays
│   │           │   │   │   ├── categorical
│   │           │   │   │   │   ├── common.py
│   │           │   │   │   │   ├── conftest.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_algos.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_analytics.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_api.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_constructors.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_dtypes.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_indexing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_missing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_operators.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_repr.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_sorting.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_subclass.cpython-36.pyc
│   │           │   │   │   │   │   └── test_warnings.cpython-36.pyc
│   │           │   │   │   │   ├── test_algos.py
│   │           │   │   │   │   ├── test_analytics.py
│   │           │   │   │   │   ├── test_api.py
│   │           │   │   │   │   ├── test_constructors.py
│   │           │   │   │   │   ├── test_dtypes.py
│   │           │   │   │   │   ├── test_indexing.py
│   │           │   │   │   │   ├── test_missing.py
│   │           │   │   │   │   ├── test_operators.py
│   │           │   │   │   │   ├── test_repr.py
│   │           │   │   │   │   ├── test_sorting.py
│   │           │   │   │   │   ├── test_subclass.py
│   │           │   │   │   │   └── test_warnings.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── interval
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_interval.cpython-36.pyc
│   │           │   │   │   │   │   └── test_ops.cpython-36.pyc
│   │           │   │   │   │   ├── test_interval.py
│   │           │   │   │   │   └── test_ops.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_array.cpython-36.pyc
│   │           │   │   │   │   ├── test_datetimelike.cpython-36.pyc
│   │           │   │   │   │   ├── test_datetimes.cpython-36.pyc
│   │           │   │   │   │   ├── test_integer.cpython-36.pyc
│   │           │   │   │   │   ├── test_numpy.cpython-36.pyc
│   │           │   │   │   │   ├── test_period.cpython-36.pyc
│   │           │   │   │   │   └── test_timedeltas.cpython-36.pyc
│   │           │   │   │   ├── sparse
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_arithmetics.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_array.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_dtype.cpython-36.pyc
│   │           │   │   │   │   │   └── test_libsparse.cpython-36.pyc
│   │           │   │   │   │   ├── test_arithmetics.py
│   │           │   │   │   │   ├── test_array.py
│   │           │   │   │   │   ├── test_dtype.py
│   │           │   │   │   │   └── test_libsparse.py
│   │           │   │   │   ├── test_array.py
│   │           │   │   │   ├── test_datetimelike.py
│   │           │   │   │   ├── test_datetimes.py
│   │           │   │   │   ├── test_integer.py
│   │           │   │   │   ├── test_numpy.py
│   │           │   │   │   ├── test_period.py
│   │           │   │   │   └── test_timedeltas.py
│   │           │   │   ├── computation
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_compat.cpython-36.pyc
│   │           │   │   │   │   └── test_eval.cpython-36.pyc
│   │           │   │   │   ├── test_compat.py
│   │           │   │   │   └── test_eval.py
│   │           │   │   ├── dtypes
│   │           │   │   │   ├── cast
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_construct_from_scalar.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_construct_ndarray.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_construct_object_arr.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_convert_objects.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_downcast.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_find_common_type.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_infer_datetimelike.cpython-36.pyc
│   │           │   │   │   │   │   └── test_infer_dtype.cpython-36.pyc
│   │           │   │   │   │   ├── test_construct_from_scalar.py
│   │           │   │   │   │   ├── test_construct_ndarray.py
│   │           │   │   │   │   ├── test_construct_object_arr.py
│   │           │   │   │   │   ├── test_convert_objects.py
│   │           │   │   │   │   ├── test_downcast.py
│   │           │   │   │   │   ├── test_find_common_type.py
│   │           │   │   │   │   ├── test_infer_datetimelike.py
│   │           │   │   │   │   └── test_infer_dtype.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_common.cpython-36.pyc
│   │           │   │   │   │   ├── test_concat.cpython-36.pyc
│   │           │   │   │   │   ├── test_dtypes.cpython-36.pyc
│   │           │   │   │   │   ├── test_generic.cpython-36.pyc
│   │           │   │   │   │   ├── test_inference.cpython-36.pyc
│   │           │   │   │   │   └── test_missing.cpython-36.pyc
│   │           │   │   │   ├── test_common.py
│   │           │   │   │   ├── test_concat.py
│   │           │   │   │   ├── test_dtypes.py
│   │           │   │   │   ├── test_generic.py
│   │           │   │   │   ├── test_inference.py
│   │           │   │   │   └── test_missing.py
│   │           │   │   ├── extension
│   │           │   │   │   ├── arrow
│   │           │   │   │   │   ├── bool.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── bool.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   └── test_bool.cpython-36.pyc
│   │           │   │   │   │   └── test_bool.py
│   │           │   │   │   ├── base
│   │           │   │   │   │   ├── base.py
│   │           │   │   │   │   ├── casting.py
│   │           │   │   │   │   ├── constructors.py
│   │           │   │   │   │   ├── dtype.py
│   │           │   │   │   │   ├── getitem.py
│   │           │   │   │   │   ├── groupby.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── interface.py
│   │           │   │   │   │   ├── io.py
│   │           │   │   │   │   ├── methods.py
│   │           │   │   │   │   ├── missing.py
│   │           │   │   │   │   ├── ops.py
│   │           │   │   │   │   ├── printing.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   │   │   ├── casting.cpython-36.pyc
│   │           │   │   │   │   │   ├── constructors.cpython-36.pyc
│   │           │   │   │   │   │   ├── dtype.cpython-36.pyc
│   │           │   │   │   │   │   ├── getitem.cpython-36.pyc
│   │           │   │   │   │   │   ├── groupby.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── interface.cpython-36.pyc
│   │           │   │   │   │   │   ├── io.cpython-36.pyc
│   │           │   │   │   │   │   ├── methods.cpython-36.pyc
│   │           │   │   │   │   │   ├── missing.cpython-36.pyc
│   │           │   │   │   │   │   ├── ops.cpython-36.pyc
│   │           │   │   │   │   │   ├── printing.cpython-36.pyc
│   │           │   │   │   │   │   ├── reduce.cpython-36.pyc
│   │           │   │   │   │   │   ├── reshaping.cpython-36.pyc
│   │           │   │   │   │   │   └── setitem.cpython-36.pyc
│   │           │   │   │   │   ├── reduce.py
│   │           │   │   │   │   ├── reshaping.py
│   │           │   │   │   │   └── setitem.py
│   │           │   │   │   ├── conftest.py
│   │           │   │   │   ├── decimal
│   │           │   │   │   │   ├── array.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── array.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   └── test_decimal.cpython-36.pyc
│   │           │   │   │   │   └── test_decimal.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── json
│   │           │   │   │   │   ├── array.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── array.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   └── test_json.cpython-36.pyc
│   │           │   │   │   │   └── test_json.py
│   │           │   │   │   ├── numpy_
│   │           │   │   │   │   ├── conftest.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_numpy.cpython-36.pyc
│   │           │   │   │   │   │   └── test_numpy_nested.cpython-36.pyc
│   │           │   │   │   │   ├── test_numpy_nested.py
│   │           │   │   │   │   └── test_numpy.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_categorical.cpython-36.pyc
│   │           │   │   │   │   ├── test_common.cpython-36.pyc
│   │           │   │   │   │   ├── test_datetime.cpython-36.pyc
│   │           │   │   │   │   ├── test_external_block.cpython-36.pyc
│   │           │   │   │   │   ├── test_integer.cpython-36.pyc
│   │           │   │   │   │   ├── test_interval.cpython-36.pyc
│   │           │   │   │   │   ├── test_period.cpython-36.pyc
│   │           │   │   │   │   └── test_sparse.cpython-36.pyc
│   │           │   │   │   ├── test_categorical.py
│   │           │   │   │   ├── test_common.py
│   │           │   │   │   ├── test_datetime.py
│   │           │   │   │   ├── test_external_block.py
│   │           │   │   │   ├── test_integer.py
│   │           │   │   │   ├── test_interval.py
│   │           │   │   │   ├── test_period.py
│   │           │   │   │   └── test_sparse.py
│   │           │   │   ├── frame
│   │           │   │   │   ├── common.py
│   │           │   │   │   ├── conftest.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_alter_axes.cpython-36.pyc
│   │           │   │   │   │   ├── test_analytics.cpython-36.pyc
│   │           │   │   │   │   ├── test_api.cpython-36.pyc
│   │           │   │   │   │   ├── test_apply.cpython-36.pyc
│   │           │   │   │   │   ├── test_arithmetic.cpython-36.pyc
│   │           │   │   │   │   ├── test_asof.cpython-36.pyc
│   │           │   │   │   │   ├── test_axis_select_reindex.cpython-36.pyc
│   │           │   │   │   │   ├── test_block_internals.cpython-36.pyc
│   │           │   │   │   │   ├── test_combine_concat.cpython-36.pyc
│   │           │   │   │   │   ├── test_constructors.cpython-36.pyc
│   │           │   │   │   │   ├── test_convert_to.cpython-36.pyc
│   │           │   │   │   │   ├── test_dtypes.cpython-36.pyc
│   │           │   │   │   │   ├── test_duplicates.cpython-36.pyc
│   │           │   │   │   │   ├── test_indexing.cpython-36.pyc
│   │           │   │   │   │   ├── test_join.cpython-36.pyc
│   │           │   │   │   │   ├── test_missing.cpython-36.pyc
│   │           │   │   │   │   ├── test_mutate_columns.cpython-36.pyc
│   │           │   │   │   │   ├── test_nonunique_indexes.cpython-36.pyc
│   │           │   │   │   │   ├── test_operators.cpython-36.pyc
│   │           │   │   │   │   ├── test_period.cpython-36.pyc
│   │           │   │   │   │   ├── test_quantile.cpython-36.pyc
│   │           │   │   │   │   ├── test_query_eval.cpython-36.pyc
│   │           │   │   │   │   ├── test_rank.cpython-36.pyc
│   │           │   │   │   │   ├── test_replace.cpython-36.pyc
│   │           │   │   │   │   ├── test_repr_info.cpython-36.pyc
│   │           │   │   │   │   ├── test_reshape.cpython-36.pyc
│   │           │   │   │   │   ├── test_sorting.cpython-36.pyc
│   │           │   │   │   │   ├── test_sort_values_level_as_str.cpython-36.pyc
│   │           │   │   │   │   ├── test_subclass.cpython-36.pyc
│   │           │   │   │   │   ├── test_timeseries.cpython-36.pyc
│   │           │   │   │   │   ├── test_timezones.cpython-36.pyc
│   │           │   │   │   │   ├── test_to_csv.cpython-36.pyc
│   │           │   │   │   │   └── test_validate.cpython-36.pyc
│   │           │   │   │   ├── test_alter_axes.py
│   │           │   │   │   ├── test_analytics.py
│   │           │   │   │   ├── test_api.py
│   │           │   │   │   ├── test_apply.py
│   │           │   │   │   ├── test_arithmetic.py
│   │           │   │   │   ├── test_asof.py
│   │           │   │   │   ├── test_axis_select_reindex.py
│   │           │   │   │   ├── test_block_internals.py
│   │           │   │   │   ├── test_combine_concat.py
│   │           │   │   │   ├── test_constructors.py
│   │           │   │   │   ├── test_convert_to.py
│   │           │   │   │   ├── test_dtypes.py
│   │           │   │   │   ├── test_duplicates.py
│   │           │   │   │   ├── test_indexing.py
│   │           │   │   │   ├── test_join.py
│   │           │   │   │   ├── test_missing.py
│   │           │   │   │   ├── test_mutate_columns.py
│   │           │   │   │   ├── test_nonunique_indexes.py
│   │           │   │   │   ├── test_operators.py
│   │           │   │   │   ├── test_period.py
│   │           │   │   │   ├── test_quantile.py
│   │           │   │   │   ├── test_query_eval.py
│   │           │   │   │   ├── test_rank.py
│   │           │   │   │   ├── test_replace.py
│   │           │   │   │   ├── test_repr_info.py
│   │           │   │   │   ├── test_reshape.py
│   │           │   │   │   ├── test_sorting.py
│   │           │   │   │   ├── test_sort_values_level_as_str.py
│   │           │   │   │   ├── test_subclass.py
│   │           │   │   │   ├── test_timeseries.py
│   │           │   │   │   ├── test_timezones.py
│   │           │   │   │   ├── test_to_csv.py
│   │           │   │   │   └── test_validate.py
│   │           │   │   ├── generic
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_frame.cpython-36.pyc
│   │           │   │   │   │   ├── test_generic.cpython-36.pyc
│   │           │   │   │   │   ├── test_label_or_level_utils.cpython-36.pyc
│   │           │   │   │   │   ├── test_panel.cpython-36.pyc
│   │           │   │   │   │   └── test_series.cpython-36.pyc
│   │           │   │   │   ├── test_frame.py
│   │           │   │   │   ├── test_generic.py
│   │           │   │   │   ├── test_label_or_level_utils.py
│   │           │   │   │   ├── test_panel.py
│   │           │   │   │   └── test_series.py
│   │           │   │   ├── groupby
│   │           │   │   │   ├── aggregate
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_aggregate.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_cython.cpython-36.pyc
│   │           │   │   │   │   │   └── test_other.cpython-36.pyc
│   │           │   │   │   │   ├── test_aggregate.py
│   │           │   │   │   │   ├── test_cython.py
│   │           │   │   │   │   └── test_other.py
│   │           │   │   │   ├── conftest.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_apply.cpython-36.pyc
│   │           │   │   │   │   ├── test_bin_groupby.cpython-36.pyc
│   │           │   │   │   │   ├── test_categorical.cpython-36.pyc
│   │           │   │   │   │   ├── test_counting.cpython-36.pyc
│   │           │   │   │   │   ├── test_filters.cpython-36.pyc
│   │           │   │   │   │   ├── test_function.cpython-36.pyc
│   │           │   │   │   │   ├── test_groupby.cpython-36.pyc
│   │           │   │   │   │   ├── test_grouping.cpython-36.pyc
│   │           │   │   │   │   ├── test_index_as_string.cpython-36.pyc
│   │           │   │   │   │   ├── test_nth.cpython-36.pyc
│   │           │   │   │   │   ├── test_rank.cpython-36.pyc
│   │           │   │   │   │   ├── test_timegrouper.cpython-36.pyc
│   │           │   │   │   │   ├── test_transform.cpython-36.pyc
│   │           │   │   │   │   ├── test_value_counts.cpython-36.pyc
│   │           │   │   │   │   └── test_whitelist.cpython-36.pyc
│   │           │   │   │   ├── test_apply.py
│   │           │   │   │   ├── test_bin_groupby.py
│   │           │   │   │   ├── test_categorical.py
│   │           │   │   │   ├── test_counting.py
│   │           │   │   │   ├── test_filters.py
│   │           │   │   │   ├── test_function.py
│   │           │   │   │   ├── test_groupby.py
│   │           │   │   │   ├── test_grouping.py
│   │           │   │   │   ├── test_index_as_string.py
│   │           │   │   │   ├── test_nth.py
│   │           │   │   │   ├── test_rank.py
│   │           │   │   │   ├── test_timegrouper.py
│   │           │   │   │   ├── test_transform.py
│   │           │   │   │   ├── test_value_counts.py
│   │           │   │   │   └── test_whitelist.py
│   │           │   │   ├── indexes
│   │           │   │   │   ├── common.py
│   │           │   │   │   ├── conftest.py
│   │           │   │   │   ├── datetimelike.py
│   │           │   │   │   ├── datetimes
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_arithmetic.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_astype.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_construction.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_date_range.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_datetime.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_datetimelike.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_formats.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_indexing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_misc.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_missing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_ops.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_partial_slicing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_scalar_compat.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_setops.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_timezones.cpython-36.pyc
│   │           │   │   │   │   │   └── test_tools.cpython-36.pyc
│   │           │   │   │   │   ├── test_arithmetic.py
│   │           │   │   │   │   ├── test_astype.py
│   │           │   │   │   │   ├── test_construction.py
│   │           │   │   │   │   ├── test_date_range.py
│   │           │   │   │   │   ├── test_datetimelike.py
│   │           │   │   │   │   ├── test_datetime.py
│   │           │   │   │   │   ├── test_formats.py
│   │           │   │   │   │   ├── test_indexing.py
│   │           │   │   │   │   ├── test_misc.py
│   │           │   │   │   │   ├── test_missing.py
│   │           │   │   │   │   ├── test_ops.py
│   │           │   │   │   │   ├── test_partial_slicing.py
│   │           │   │   │   │   ├── test_scalar_compat.py
│   │           │   │   │   │   ├── test_setops.py
│   │           │   │   │   │   ├── test_timezones.py
│   │           │   │   │   │   └── test_tools.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── interval
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_astype.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_construction.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_interval.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_interval_new.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_interval_range.cpython-36.pyc
│   │           │   │   │   │   │   └── test_interval_tree.cpython-36.pyc
│   │           │   │   │   │   ├── test_astype.py
│   │           │   │   │   │   ├── test_construction.py
│   │           │   │   │   │   ├── test_interval_new.py
│   │           │   │   │   │   ├── test_interval.py
│   │           │   │   │   │   ├── test_interval_range.py
│   │           │   │   │   │   └── test_interval_tree.py
│   │           │   │   │   ├── multi
│   │           │   │   │   │   ├── conftest.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_analytics.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_astype.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_compat.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_constructor.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_contains.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_conversion.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_copy.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_drop.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_duplicates.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_equivalence.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_format.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_get_set.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_indexing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_integrity.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_join.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_missing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_monotonic.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_names.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_partial_indexing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_reindex.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_reshape.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_set_ops.cpython-36.pyc
│   │           │   │   │   │   │   └── test_sorting.cpython-36.pyc
│   │           │   │   │   │   ├── test_analytics.py
│   │           │   │   │   │   ├── test_astype.py
│   │           │   │   │   │   ├── test_compat.py
│   │           │   │   │   │   ├── test_constructor.py
│   │           │   │   │   │   ├── test_contains.py
│   │           │   │   │   │   ├── test_conversion.py
│   │           │   │   │   │   ├── test_copy.py
│   │           │   │   │   │   ├── test_drop.py
│   │           │   │   │   │   ├── test_duplicates.py
│   │           │   │   │   │   ├── test_equivalence.py
│   │           │   │   │   │   ├── test_format.py
│   │           │   │   │   │   ├── test_get_set.py
│   │           │   │   │   │   ├── test_indexing.py
│   │           │   │   │   │   ├── test_integrity.py
│   │           │   │   │   │   ├── test_join.py
│   │           │   │   │   │   ├── test_missing.py
│   │           │   │   │   │   ├── test_monotonic.py
│   │           │   │   │   │   ├── test_names.py
│   │           │   │   │   │   ├── test_partial_indexing.py
│   │           │   │   │   │   ├── test_reindex.py
│   │           │   │   │   │   ├── test_reshape.py
│   │           │   │   │   │   ├── test_set_ops.py
│   │           │   │   │   │   └── test_sorting.py
│   │           │   │   │   ├── period
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_arithmetic.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_asfreq.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_astype.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_construction.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_formats.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_indexing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_ops.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_partial_slicing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_period.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_period_range.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_scalar_compat.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_setops.cpython-36.pyc
│   │           │   │   │   │   │   └── test_tools.cpython-36.pyc
│   │           │   │   │   │   ├── test_arithmetic.py
│   │           │   │   │   │   ├── test_asfreq.py
│   │           │   │   │   │   ├── test_astype.py
│   │           │   │   │   │   ├── test_construction.py
│   │           │   │   │   │   ├── test_formats.py
│   │           │   │   │   │   ├── test_indexing.py
│   │           │   │   │   │   ├── test_ops.py
│   │           │   │   │   │   ├── test_partial_slicing.py
│   │           │   │   │   │   ├── test_period.py
│   │           │   │   │   │   ├── test_period_range.py
│   │           │   │   │   │   ├── test_scalar_compat.py
│   │           │   │   │   │   ├── test_setops.py
│   │           │   │   │   │   └── test_tools.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   ├── datetimelike.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_base.cpython-36.pyc
│   │           │   │   │   │   ├── test_category.cpython-36.pyc
│   │           │   │   │   │   ├── test_common.cpython-36.pyc
│   │           │   │   │   │   ├── test_frozen.cpython-36.pyc
│   │           │   │   │   │   ├── test_numeric.cpython-36.pyc
│   │           │   │   │   │   └── test_range.cpython-36.pyc
│   │           │   │   │   ├── test_base.py
│   │           │   │   │   ├── test_category.py
│   │           │   │   │   ├── test_common.py
│   │           │   │   │   ├── test_frozen.py
│   │           │   │   │   ├── test_numeric.py
│   │           │   │   │   ├── test_range.py
│   │           │   │   │   └── timedeltas
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_arithmetic.cpython-36.pyc
│   │           │   │   │       │   ├── test_astype.cpython-36.pyc
│   │           │   │   │       │   ├── test_construction.cpython-36.pyc
│   │           │   │   │       │   ├── test_formats.cpython-36.pyc
│   │           │   │   │       │   ├── test_indexing.cpython-36.pyc
│   │           │   │   │       │   ├── test_ops.cpython-36.pyc
│   │           │   │   │       │   ├── test_partial_slicing.cpython-36.pyc
│   │           │   │   │       │   ├── test_scalar_compat.cpython-36.pyc
│   │           │   │   │       │   ├── test_setops.cpython-36.pyc
│   │           │   │   │       │   ├── test_timedelta.cpython-36.pyc
│   │           │   │   │       │   ├── test_timedelta_range.cpython-36.pyc
│   │           │   │   │       │   └── test_tools.cpython-36.pyc
│   │           │   │   │       ├── test_arithmetic.py
│   │           │   │   │       ├── test_astype.py
│   │           │   │   │       ├── test_construction.py
│   │           │   │   │       ├── test_formats.py
│   │           │   │   │       ├── test_indexing.py
│   │           │   │   │       ├── test_ops.py
│   │           │   │   │       ├── test_partial_slicing.py
│   │           │   │   │       ├── test_scalar_compat.py
│   │           │   │   │       ├── test_setops.py
│   │           │   │   │       ├── test_timedelta.py
│   │           │   │   │       ├── test_timedelta_range.py
│   │           │   │   │       └── test_tools.py
│   │           │   │   ├── indexing
│   │           │   │   │   ├── common.py
│   │           │   │   │   ├── conftest.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── interval
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_interval.cpython-36.pyc
│   │           │   │   │   │   │   └── test_interval_new.cpython-36.pyc
│   │           │   │   │   │   ├── test_interval_new.py
│   │           │   │   │   │   └── test_interval.py
│   │           │   │   │   ├── multiindex
│   │           │   │   │   │   ├── conftest.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_chaining_and_caching.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_datetime.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_getitem.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_iloc.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_indexing_slow.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_ix.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_loc.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_multiindex.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_panel.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_partial.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_setitem.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_set_ops.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_slice.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_sorted.cpython-36.pyc
│   │           │   │   │   │   │   └── test_xs.cpython-36.pyc
│   │           │   │   │   │   ├── test_chaining_and_caching.py
│   │           │   │   │   │   ├── test_datetime.py
│   │           │   │   │   │   ├── test_getitem.py
│   │           │   │   │   │   ├── test_iloc.py
│   │           │   │   │   │   ├── test_indexing_slow.py
│   │           │   │   │   │   ├── test_ix.py
│   │           │   │   │   │   ├── test_loc.py
│   │           │   │   │   │   ├── test_multiindex.py
│   │           │   │   │   │   ├── test_panel.py
│   │           │   │   │   │   ├── test_partial.py
│   │           │   │   │   │   ├── test_setitem.py
│   │           │   │   │   │   ├── test_set_ops.py
│   │           │   │   │   │   ├── test_slice.py
│   │           │   │   │   │   ├── test_sorted.py
│   │           │   │   │   │   └── test_xs.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_callable.cpython-36.pyc
│   │           │   │   │   │   ├── test_categorical.cpython-36.pyc
│   │           │   │   │   │   ├── test_chaining_and_caching.cpython-36.pyc
│   │           │   │   │   │   ├── test_coercion.cpython-36.pyc
│   │           │   │   │   │   ├── test_datetime.cpython-36.pyc
│   │           │   │   │   │   ├── test_floats.cpython-36.pyc
│   │           │   │   │   │   ├── test_iloc.cpython-36.pyc
│   │           │   │   │   │   ├── test_indexing.cpython-36.pyc
│   │           │   │   │   │   ├── test_indexing_engines.cpython-36.pyc
│   │           │   │   │   │   ├── test_indexing_slow.cpython-36.pyc
│   │           │   │   │   │   ├── test_ix.cpython-36.pyc
│   │           │   │   │   │   ├── test_loc.cpython-36.pyc
│   │           │   │   │   │   ├── test_panel.cpython-36.pyc
│   │           │   │   │   │   ├── test_partial.cpython-36.pyc
│   │           │   │   │   │   ├── test_scalar.cpython-36.pyc
│   │           │   │   │   │   └── test_timedelta.cpython-36.pyc
│   │           │   │   │   ├── test_callable.py
│   │           │   │   │   ├── test_categorical.py
│   │           │   │   │   ├── test_chaining_and_caching.py
│   │           │   │   │   ├── test_coercion.py
│   │           │   │   │   ├── test_datetime.py
│   │           │   │   │   ├── test_floats.py
│   │           │   │   │   ├── test_iloc.py
│   │           │   │   │   ├── test_indexing_engines.py
│   │           │   │   │   ├── test_indexing.py
│   │           │   │   │   ├── test_indexing_slow.py
│   │           │   │   │   ├── test_ix.py
│   │           │   │   │   ├── test_loc.py
│   │           │   │   │   ├── test_panel.py
│   │           │   │   │   ├── test_partial.py
│   │           │   │   │   ├── test_scalar.py
│   │           │   │   │   └── test_timedelta.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── internals
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── test_internals.cpython-36.pyc
│   │           │   │   │   └── test_internals.py
│   │           │   │   ├── io
│   │           │   │   │   ├── conftest.py
│   │           │   │   │   ├── formats
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_console.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_css.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_eng_formatting.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_format.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_printing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_style.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_to_csv.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_to_excel.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_to_html.cpython-36.pyc
│   │           │   │   │   │   │   └── test_to_latex.cpython-36.pyc
│   │           │   │   │   │   ├── test_console.py
│   │           │   │   │   │   ├── test_css.py
│   │           │   │   │   │   ├── test_eng_formatting.py
│   │           │   │   │   │   ├── test_format.py
│   │           │   │   │   │   ├── test_printing.py
│   │           │   │   │   │   ├── test_style.py
│   │           │   │   │   │   ├── test_to_csv.py
│   │           │   │   │   │   ├── test_to_excel.py
│   │           │   │   │   │   ├── test_to_html.py
│   │           │   │   │   │   └── test_to_latex.py
│   │           │   │   │   ├── generate_legacy_storage_files.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── json
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_compression.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_json_table_schema.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_normalize.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_pandas.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_readlines.cpython-36.pyc
│   │           │   │   │   │   │   └── test_ujson.cpython-36.pyc
│   │           │   │   │   │   ├── test_compression.py
│   │           │   │   │   │   ├── test_json_table_schema.py
│   │           │   │   │   │   ├── test_normalize.py
│   │           │   │   │   │   ├── test_pandas.py
│   │           │   │   │   │   ├── test_readlines.py
│   │           │   │   │   │   └── test_ujson.py
│   │           │   │   │   ├── msgpack
│   │           │   │   │   │   ├── common.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_buffer.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_case.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_except.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_extension.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_format.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_limits.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_newspec.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_obj.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_pack.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_read_size.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_seq.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_sequnpack.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_subtype.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_unpack.cpython-36.pyc
│   │           │   │   │   │   │   └── test_unpack_raw.cpython-36.pyc
│   │           │   │   │   │   ├── test_buffer.py
│   │           │   │   │   │   ├── test_case.py
│   │           │   │   │   │   ├── test_except.py
│   │           │   │   │   │   ├── test_extension.py
│   │           │   │   │   │   ├── test_format.py
│   │           │   │   │   │   ├── test_limits.py
│   │           │   │   │   │   ├── test_newspec.py
│   │           │   │   │   │   ├── test_obj.py
│   │           │   │   │   │   ├── test_pack.py
│   │           │   │   │   │   ├── test_read_size.py
│   │           │   │   │   │   ├── test_seq.py
│   │           │   │   │   │   ├── test_sequnpack.py
│   │           │   │   │   │   ├── test_subtype.py
│   │           │   │   │   │   ├── test_unpack.py
│   │           │   │   │   │   └── test_unpack_raw.py
│   │           │   │   │   ├── parser
│   │           │   │   │   │   ├── conftest.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_comment.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_common.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_compression.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_converters.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_c_parser_only.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_dialect.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_dtypes.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_header.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_index_col.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_mangle_dupes.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_multi_thread.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_na_values.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_network.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_parse_dates.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_python_parser_only.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_quoting.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_read_fwf.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_skiprows.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_textreader.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_unsupported.cpython-36.pyc
│   │           │   │   │   │   │   └── test_usecols.cpython-36.pyc
│   │           │   │   │   │   ├── test_comment.py
│   │           │   │   │   │   ├── test_common.py
│   │           │   │   │   │   ├── test_compression.py
│   │           │   │   │   │   ├── test_converters.py
│   │           │   │   │   │   ├── test_c_parser_only.py
│   │           │   │   │   │   ├── test_dialect.py
│   │           │   │   │   │   ├── test_dtypes.py
│   │           │   │   │   │   ├── test_header.py
│   │           │   │   │   │   ├── test_index_col.py
│   │           │   │   │   │   ├── test_mangle_dupes.py
│   │           │   │   │   │   ├── test_multi_thread.py
│   │           │   │   │   │   ├── test_na_values.py
│   │           │   │   │   │   ├── test_network.py
│   │           │   │   │   │   ├── test_parse_dates.py
│   │           │   │   │   │   ├── test_python_parser_only.py
│   │           │   │   │   │   ├── test_quoting.py
│   │           │   │   │   │   ├── test_read_fwf.py
│   │           │   │   │   │   ├── test_skiprows.py
│   │           │   │   │   │   ├── test_textreader.py
│   │           │   │   │   │   ├── test_unsupported.py
│   │           │   │   │   │   └── test_usecols.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   ├── generate_legacy_storage_files.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_clipboard.cpython-36.pyc
│   │           │   │   │   │   ├── test_common.cpython-36.pyc
│   │           │   │   │   │   ├── test_compression.cpython-36.pyc
│   │           │   │   │   │   ├── test_date_converters.cpython-36.pyc
│   │           │   │   │   │   ├── test_excel.cpython-36.pyc
│   │           │   │   │   │   ├── test_feather.cpython-36.pyc
│   │           │   │   │   │   ├── test_gbq.cpython-36.pyc
│   │           │   │   │   │   ├── test_gcs.cpython-36.pyc
│   │           │   │   │   │   ├── test_html.cpython-36.pyc
│   │           │   │   │   │   ├── test_packers.cpython-36.pyc
│   │           │   │   │   │   ├── test_parquet.cpython-36.pyc
│   │           │   │   │   │   ├── test_pickle.cpython-36.pyc
│   │           │   │   │   │   ├── test_pytables.cpython-36.pyc
│   │           │   │   │   │   ├── test_s3.cpython-36.pyc
│   │           │   │   │   │   ├── test_sql.cpython-36.pyc
│   │           │   │   │   │   └── test_stata.cpython-36.pyc
│   │           │   │   │   ├── sas
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_sas7bdat.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_sas.cpython-36.pyc
│   │           │   │   │   │   │   └── test_xport.cpython-36.pyc
│   │           │   │   │   │   ├── test_sas7bdat.py
│   │           │   │   │   │   ├── test_sas.py
│   │           │   │   │   │   └── test_xport.py
│   │           │   │   │   ├── test_clipboard.py
│   │           │   │   │   ├── test_common.py
│   │           │   │   │   ├── test_compression.py
│   │           │   │   │   ├── test_date_converters.py
│   │           │   │   │   ├── test_excel.py
│   │           │   │   │   ├── test_feather.py
│   │           │   │   │   ├── test_gbq.py
│   │           │   │   │   ├── test_gcs.py
│   │           │   │   │   ├── test_html.py
│   │           │   │   │   ├── test_packers.py
│   │           │   │   │   ├── test_parquet.py
│   │           │   │   │   ├── test_pickle.py
│   │           │   │   │   ├── test_pytables.py
│   │           │   │   │   ├── test_s3.py
│   │           │   │   │   ├── test_sql.py
│   │           │   │   │   └── test_stata.py
│   │           │   │   ├── plotting
│   │           │   │   │   ├── common.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_boxplot_method.cpython-36.pyc
│   │           │   │   │   │   ├── test_converter.cpython-36.pyc
│   │           │   │   │   │   ├── test_datetimelike.cpython-36.pyc
│   │           │   │   │   │   ├── test_frame.cpython-36.pyc
│   │           │   │   │   │   ├── test_groupby.cpython-36.pyc
│   │           │   │   │   │   ├── test_hist_method.cpython-36.pyc
│   │           │   │   │   │   ├── test_misc.cpython-36.pyc
│   │           │   │   │   │   └── test_series.cpython-36.pyc
│   │           │   │   │   ├── test_boxplot_method.py
│   │           │   │   │   ├── test_converter.py
│   │           │   │   │   ├── test_datetimelike.py
│   │           │   │   │   ├── test_frame.py
│   │           │   │   │   ├── test_groupby.py
│   │           │   │   │   ├── test_hist_method.py
│   │           │   │   │   ├── test_misc.py
│   │           │   │   │   └── test_series.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── test_algos.cpython-36.pyc
│   │           │   │   │   ├── test_base.cpython-36.pyc
│   │           │   │   │   ├── test_common.cpython-36.pyc
│   │           │   │   │   ├── test_compat.cpython-36.pyc
│   │           │   │   │   ├── test_config.cpython-36.pyc
│   │           │   │   │   ├── test_downstream.cpython-36.pyc
│   │           │   │   │   ├── test_errors.cpython-36.pyc
│   │           │   │   │   ├── test_expressions.cpython-36.pyc
│   │           │   │   │   ├── test_join.cpython-36.pyc
│   │           │   │   │   ├── test_lib.cpython-36.pyc
│   │           │   │   │   ├── test_multilevel.cpython-36.pyc
│   │           │   │   │   ├── test_nanops.cpython-36.pyc
│   │           │   │   │   ├── test_panel.cpython-36.pyc
│   │           │   │   │   ├── test_register_accessor.cpython-36.pyc
│   │           │   │   │   ├── test_sorting.cpython-36.pyc
│   │           │   │   │   ├── test_strings.cpython-36.pyc
│   │           │   │   │   ├── test_take.cpython-36.pyc
│   │           │   │   │   └── test_window.cpython-36.pyc
│   │           │   │   ├── reductions
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_reductions.cpython-36.pyc
│   │           │   │   │   │   └── test_stat_reductions.cpython-36.pyc
│   │           │   │   │   ├── test_reductions.py
│   │           │   │   │   └── test_stat_reductions.py
│   │           │   │   ├── resample
│   │           │   │   │   ├── conftest.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_base.cpython-36.pyc
│   │           │   │   │   │   ├── test_datetime_index.cpython-36.pyc
│   │           │   │   │   │   ├── test_period_index.cpython-36.pyc
│   │           │   │   │   │   ├── test_resample_api.cpython-36.pyc
│   │           │   │   │   │   ├── test_resampler_grouper.cpython-36.pyc
│   │           │   │   │   │   ├── test_timedelta.cpython-36.pyc
│   │           │   │   │   │   └── test_time_grouper.cpython-36.pyc
│   │           │   │   │   ├── test_base.py
│   │           │   │   │   ├── test_datetime_index.py
│   │           │   │   │   ├── test_period_index.py
│   │           │   │   │   ├── test_resample_api.py
│   │           │   │   │   ├── test_resampler_grouper.py
│   │           │   │   │   ├── test_timedelta.py
│   │           │   │   │   └── test_time_grouper.py
│   │           │   │   ├── reshape
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── merge
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_join.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_merge_asof.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_merge.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_merge_index_as_string.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_merge_ordered.cpython-36.pyc
│   │           │   │   │   │   │   └── test_multi.cpython-36.pyc
│   │           │   │   │   │   ├── test_join.py
│   │           │   │   │   │   ├── test_merge_asof.py
│   │           │   │   │   │   ├── test_merge_index_as_string.py
│   │           │   │   │   │   ├── test_merge_ordered.py
│   │           │   │   │   │   ├── test_merge.py
│   │           │   │   │   │   └── test_multi.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_concat.cpython-36.pyc
│   │           │   │   │   │   ├── test_cut.cpython-36.pyc
│   │           │   │   │   │   ├── test_melt.cpython-36.pyc
│   │           │   │   │   │   ├── test_pivot.cpython-36.pyc
│   │           │   │   │   │   ├── test_qcut.cpython-36.pyc
│   │           │   │   │   │   ├── test_reshape.cpython-36.pyc
│   │           │   │   │   │   ├── test_union_categoricals.cpython-36.pyc
│   │           │   │   │   │   └── test_util.cpython-36.pyc
│   │           │   │   │   ├── test_concat.py
│   │           │   │   │   ├── test_cut.py
│   │           │   │   │   ├── test_melt.py
│   │           │   │   │   ├── test_pivot.py
│   │           │   │   │   ├── test_qcut.py
│   │           │   │   │   ├── test_reshape.py
│   │           │   │   │   ├── test_union_categoricals.py
│   │           │   │   │   └── test_util.py
│   │           │   │   ├── scalar
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── interval
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_interval.cpython-36.pyc
│   │           │   │   │   │   │   └── test_ops.cpython-36.pyc
│   │           │   │   │   │   ├── test_interval.py
│   │           │   │   │   │   └── test_ops.py
│   │           │   │   │   ├── period
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_asfreq.cpython-36.pyc
│   │           │   │   │   │   │   └── test_period.cpython-36.pyc
│   │           │   │   │   │   ├── test_asfreq.py
│   │           │   │   │   │   └── test_period.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── test_nat.cpython-36.pyc
│   │           │   │   │   ├── test_nat.py
│   │           │   │   │   ├── timedelta
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_arithmetic.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_construction.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_formats.cpython-36.pyc
│   │           │   │   │   │   │   └── test_timedelta.cpython-36.pyc
│   │           │   │   │   │   ├── test_arithmetic.py
│   │           │   │   │   │   ├── test_construction.py
│   │           │   │   │   │   ├── test_formats.py
│   │           │   │   │   │   └── test_timedelta.py
│   │           │   │   │   └── timestamp
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_arithmetic.cpython-36.pyc
│   │           │   │   │       │   ├── test_comparisons.cpython-36.pyc
│   │           │   │   │       │   ├── test_rendering.cpython-36.pyc
│   │           │   │   │       │   ├── test_timestamp.cpython-36.pyc
│   │           │   │   │       │   ├── test_timezones.cpython-36.pyc
│   │           │   │   │       │   └── test_unary_ops.cpython-36.pyc
│   │           │   │   │       ├── test_arithmetic.py
│   │           │   │   │       ├── test_comparisons.py
│   │           │   │   │       ├── test_rendering.py
│   │           │   │   │       ├── test_timestamp.py
│   │           │   │   │       ├── test_timezones.py
│   │           │   │   │       └── test_unary_ops.py
│   │           │   │   ├── series
│   │           │   │   │   ├── common.py
│   │           │   │   │   ├── conftest.py
│   │           │   │   │   ├── indexing
│   │           │   │   │   │   ├── conftest.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_alter_index.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_boolean.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_callable.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_datetime.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_iloc.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_indexing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_loc.cpython-36.pyc
│   │           │   │   │   │   │   └── test_numeric.cpython-36.pyc
│   │           │   │   │   │   ├── test_alter_index.py
│   │           │   │   │   │   ├── test_boolean.py
│   │           │   │   │   │   ├── test_callable.py
│   │           │   │   │   │   ├── test_datetime.py
│   │           │   │   │   │   ├── test_iloc.py
│   │           │   │   │   │   ├── test_indexing.py
│   │           │   │   │   │   ├── test_loc.py
│   │           │   │   │   │   └── test_numeric.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_alter_axes.cpython-36.pyc
│   │           │   │   │   │   ├── test_analytics.cpython-36.pyc
│   │           │   │   │   │   ├── test_api.cpython-36.pyc
│   │           │   │   │   │   ├── test_apply.cpython-36.pyc
│   │           │   │   │   │   ├── test_arithmetic.cpython-36.pyc
│   │           │   │   │   │   ├── test_asof.cpython-36.pyc
│   │           │   │   │   │   ├── test_block_internals.cpython-36.pyc
│   │           │   │   │   │   ├── test_combine_concat.cpython-36.pyc
│   │           │   │   │   │   ├── test_constructors.cpython-36.pyc
│   │           │   │   │   │   ├── test_datetime_values.cpython-36.pyc
│   │           │   │   │   │   ├── test_dtypes.cpython-36.pyc
│   │           │   │   │   │   ├── test_duplicates.cpython-36.pyc
│   │           │   │   │   │   ├── test_internals.cpython-36.pyc
│   │           │   │   │   │   ├── test_io.cpython-36.pyc
│   │           │   │   │   │   ├── test_missing.cpython-36.pyc
│   │           │   │   │   │   ├── test_operators.cpython-36.pyc
│   │           │   │   │   │   ├── test_period.cpython-36.pyc
│   │           │   │   │   │   ├── test_quantile.cpython-36.pyc
│   │           │   │   │   │   ├── test_rank.cpython-36.pyc
│   │           │   │   │   │   ├── test_replace.cpython-36.pyc
│   │           │   │   │   │   ├── test_repr.cpython-36.pyc
│   │           │   │   │   │   ├── test_sorting.cpython-36.pyc
│   │           │   │   │   │   ├── test_subclass.cpython-36.pyc
│   │           │   │   │   │   ├── test_timeseries.cpython-36.pyc
│   │           │   │   │   │   ├── test_timezones.cpython-36.pyc
│   │           │   │   │   │   └── test_validate.cpython-36.pyc
│   │           │   │   │   ├── test_alter_axes.py
│   │           │   │   │   ├── test_analytics.py
│   │           │   │   │   ├── test_api.py
│   │           │   │   │   ├── test_apply.py
│   │           │   │   │   ├── test_arithmetic.py
│   │           │   │   │   ├── test_asof.py
│   │           │   │   │   ├── test_block_internals.py
│   │           │   │   │   ├── test_combine_concat.py
│   │           │   │   │   ├── test_constructors.py
│   │           │   │   │   ├── test_datetime_values.py
│   │           │   │   │   ├── test_dtypes.py
│   │           │   │   │   ├── test_duplicates.py
│   │           │   │   │   ├── test_internals.py
│   │           │   │   │   ├── test_io.py
│   │           │   │   │   ├── test_missing.py
│   │           │   │   │   ├── test_operators.py
│   │           │   │   │   ├── test_period.py
│   │           │   │   │   ├── test_quantile.py
│   │           │   │   │   ├── test_rank.py
│   │           │   │   │   ├── test_replace.py
│   │           │   │   │   ├── test_repr.py
│   │           │   │   │   ├── test_sorting.py
│   │           │   │   │   ├── test_subclass.py
│   │           │   │   │   ├── test_timeseries.py
│   │           │   │   │   ├── test_timezones.py
│   │           │   │   │   └── test_validate.py
│   │           │   │   ├── sparse
│   │           │   │   │   ├── common.py
│   │           │   │   │   ├── frame
│   │           │   │   │   │   ├── conftest.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_analytics.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_apply.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_frame.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_indexing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_to_csv.cpython-36.pyc
│   │           │   │   │   │   │   └── test_to_from_scipy.cpython-36.pyc
│   │           │   │   │   │   ├── test_analytics.py
│   │           │   │   │   │   ├── test_apply.py
│   │           │   │   │   │   ├── test_frame.py
│   │           │   │   │   │   ├── test_indexing.py
│   │           │   │   │   │   ├── test_to_csv.py
│   │           │   │   │   │   └── test_to_from_scipy.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_combine_concat.cpython-36.pyc
│   │           │   │   │   │   ├── test_format.cpython-36.pyc
│   │           │   │   │   │   ├── test_groupby.cpython-36.pyc
│   │           │   │   │   │   ├── test_indexing.cpython-36.pyc
│   │           │   │   │   │   ├── test_pivot.cpython-36.pyc
│   │           │   │   │   │   └── test_reshape.cpython-36.pyc
│   │           │   │   │   ├── series
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_indexing.cpython-36.pyc
│   │           │   │   │   │   │   └── test_series.cpython-36.pyc
│   │           │   │   │   │   ├── test_indexing.py
│   │           │   │   │   │   └── test_series.py
│   │           │   │   │   ├── test_combine_concat.py
│   │           │   │   │   ├── test_format.py
│   │           │   │   │   ├── test_groupby.py
│   │           │   │   │   ├── test_indexing.py
│   │           │   │   │   ├── test_pivot.py
│   │           │   │   │   └── test_reshape.py
│   │           │   │   ├── test_algos.py
│   │           │   │   ├── test_base.py
│   │           │   │   ├── test_common.py
│   │           │   │   ├── test_compat.py
│   │           │   │   ├── test_config.py
│   │           │   │   ├── test_downstream.py
│   │           │   │   ├── test_errors.py
│   │           │   │   ├── test_expressions.py
│   │           │   │   ├── test_join.py
│   │           │   │   ├── test_lib.py
│   │           │   │   ├── test_multilevel.py
│   │           │   │   ├── test_nanops.py
│   │           │   │   ├── test_panel.py
│   │           │   │   ├── test_register_accessor.py
│   │           │   │   ├── test_sorting.py
│   │           │   │   ├── test_strings.py
│   │           │   │   ├── test_take.py
│   │           │   │   ├── test_window.py
│   │           │   │   ├── tools
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── test_numeric.cpython-36.pyc
│   │           │   │   │   └── test_numeric.py
│   │           │   │   ├── tseries
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── offsets
│   │           │   │   │   │   ├── common.py
│   │           │   │   │   │   ├── conftest.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   │   │   ├── conftest.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_fiscal.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_offsets.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_offsets_properties.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_ticks.cpython-36.pyc
│   │           │   │   │   │   │   └── test_yqm_offsets.cpython-36.pyc
│   │           │   │   │   │   ├── test_fiscal.py
│   │           │   │   │   │   ├── test_offsets_properties.py
│   │           │   │   │   │   ├── test_offsets.py
│   │           │   │   │   │   ├── test_ticks.py
│   │           │   │   │   │   └── test_yqm_offsets.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_frequencies.cpython-36.pyc
│   │           │   │   │   │   └── test_holiday.cpython-36.pyc
│   │           │   │   │   ├── test_frequencies.py
│   │           │   │   │   └── test_holiday.py
│   │           │   │   ├── tslibs
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_api.cpython-36.pyc
│   │           │   │   │   │   ├── test_array_to_datetime.cpython-36.pyc
│   │           │   │   │   │   ├── test_ccalendar.cpython-36.pyc
│   │           │   │   │   │   ├── test_conversion.cpython-36.pyc
│   │           │   │   │   │   ├── test_libfrequencies.cpython-36.pyc
│   │           │   │   │   │   ├── test_liboffsets.cpython-36.pyc
│   │           │   │   │   │   ├── test_normalize_date.cpython-36.pyc
│   │           │   │   │   │   ├── test_parse_iso8601.cpython-36.pyc
│   │           │   │   │   │   ├── test_parsing.cpython-36.pyc
│   │           │   │   │   │   ├── test_period_asfreq.cpython-36.pyc
│   │           │   │   │   │   ├── test_timedeltas.cpython-36.pyc
│   │           │   │   │   │   └── test_timezones.cpython-36.pyc
│   │           │   │   │   ├── test_api.py
│   │           │   │   │   ├── test_array_to_datetime.py
│   │           │   │   │   ├── test_ccalendar.py
│   │           │   │   │   ├── test_conversion.py
│   │           │   │   │   ├── test_libfrequencies.py
│   │           │   │   │   ├── test_liboffsets.py
│   │           │   │   │   ├── test_normalize_date.py
│   │           │   │   │   ├── test_parse_iso8601.py
│   │           │   │   │   ├── test_parsing.py
│   │           │   │   │   ├── test_period_asfreq.py
│   │           │   │   │   ├── test_timedeltas.py
│   │           │   │   │   └── test_timezones.py
│   │           │   │   └── util
│   │           │   │       ├── conftest.py
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── conftest.cpython-36.pyc
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_assert_almost_equal.cpython-36.pyc
│   │           │   │       │   ├── test_assert_categorical_equal.cpython-36.pyc
│   │           │   │       │   ├── test_assert_extension_array_equal.cpython-36.pyc
│   │           │   │       │   ├── test_assert_frame_equal.cpython-36.pyc
│   │           │   │       │   ├── test_assert_index_equal.cpython-36.pyc
│   │           │   │       │   ├── test_assert_interval_array_equal.cpython-36.pyc
│   │           │   │       │   ├── test_assert_numpy_array_equal.cpython-36.pyc
│   │           │   │       │   ├── test_assert_series_equal.cpython-36.pyc
│   │           │   │       │   ├── test_deprecate.cpython-36.pyc
│   │           │   │       │   ├── test_deprecate_kwarg.cpython-36.pyc
│   │           │   │       │   ├── test_hashing.cpython-36.pyc
│   │           │   │       │   ├── test_locale.cpython-36.pyc
│   │           │   │       │   ├── test_move.cpython-36.pyc
│   │           │   │       │   ├── test_safe_import.cpython-36.pyc
│   │           │   │       │   ├── test_util.cpython-36.pyc
│   │           │   │       │   ├── test_validate_args_and_kwargs.cpython-36.pyc
│   │           │   │       │   ├── test_validate_args.cpython-36.pyc
│   │           │   │       │   └── test_validate_kwargs.cpython-36.pyc
│   │           │   │       ├── test_assert_almost_equal.py
│   │           │   │       ├── test_assert_categorical_equal.py
│   │           │   │       ├── test_assert_extension_array_equal.py
│   │           │   │       ├── test_assert_frame_equal.py
│   │           │   │       ├── test_assert_index_equal.py
│   │           │   │       ├── test_assert_interval_array_equal.py
│   │           │   │       ├── test_assert_numpy_array_equal.py
│   │           │   │       ├── test_assert_series_equal.py
│   │           │   │       ├── test_deprecate_kwarg.py
│   │           │   │       ├── test_deprecate.py
│   │           │   │       ├── test_hashing.py
│   │           │   │       ├── test_locale.py
│   │           │   │       ├── test_move.py
│   │           │   │       ├── test_safe_import.py
│   │           │   │       ├── test_util.py
│   │           │   │       ├── test_validate_args_and_kwargs.py
│   │           │   │       ├── test_validate_args.py
│   │           │   │       └── test_validate_kwargs.py
│   │           │   ├── tseries
│   │           │   │   ├── api.py
│   │           │   │   ├── converter.py
│   │           │   │   ├── frequencies.py
│   │           │   │   ├── holiday.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── offsets.py
│   │           │   │   ├── plotting.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── api.cpython-36.pyc
│   │           │   │       ├── converter.cpython-36.pyc
│   │           │   │       ├── frequencies.cpython-36.pyc
│   │           │   │       ├── holiday.cpython-36.pyc
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       ├── offsets.cpython-36.pyc
│   │           │   │       └── plotting.cpython-36.pyc
│   │           │   ├── util
│   │           │   │   ├── _decorators.py
│   │           │   │   ├── _depr_module.py
│   │           │   │   ├── _doctools.py
│   │           │   │   ├── _exceptions.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _move.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _print_versions.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _decorators.cpython-36.pyc
│   │           │   │   │   ├── _depr_module.cpython-36.pyc
│   │           │   │   │   ├── _doctools.cpython-36.pyc
│   │           │   │   │   ├── _exceptions.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── _print_versions.cpython-36.pyc
│   │           │   │   │   ├── _test_decorators.cpython-36.pyc
│   │           │   │   │   ├── _tester.cpython-36.pyc
│   │           │   │   │   ├── testing.cpython-36.pyc
│   │           │   │   │   └── _validators.cpython-36.pyc
│   │           │   │   ├── _test_decorators.py
│   │           │   │   ├── _tester.py
│   │           │   │   ├── testing.py
│   │           │   │   └── _validators.py
│   │           │   └── _version.py
│   │           ├── pandas-0.24.2.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── pandocfilters-1.4.2.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── pandocfilters.py
│   │           ├── parso
│   │           │   ├── cache.py
│   │           │   ├── _compatibility.py
│   │           │   ├── file_io.py
│   │           │   ├── grammar.py
│   │           │   ├── __init__.py
│   │           │   ├── normalizer.py
│   │           │   ├── parser.py
│   │           │   ├── pgen2
│   │           │   │   ├── generator.py
│   │           │   │   ├── grammar_parser.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── generator.cpython-36.pyc
│   │           │   │       ├── grammar_parser.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── __pycache__
│   │           │   │   ├── cache.cpython-36.pyc
│   │           │   │   ├── _compatibility.cpython-36.pyc
│   │           │   │   ├── file_io.cpython-36.pyc
│   │           │   │   ├── grammar.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── normalizer.cpython-36.pyc
│   │           │   │   ├── parser.cpython-36.pyc
│   │           │   │   ├── tree.cpython-36.pyc
│   │           │   │   └── utils.cpython-36.pyc
│   │           │   ├── python
│   │           │   │   ├── diff.py
│   │           │   │   ├── errors.py
│   │           │   │   ├── grammar26.txt
│   │           │   │   ├── grammar27.txt
│   │           │   │   ├── grammar33.txt
│   │           │   │   ├── grammar34.txt
│   │           │   │   ├── grammar35.txt
│   │           │   │   ├── grammar36.txt
│   │           │   │   ├── grammar37.txt
│   │           │   │   ├── grammar38.txt
│   │           │   │   ├── __init__.py
│   │           │   │   ├── parser.py
│   │           │   │   ├── pep8.py
│   │           │   │   ├── prefix.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── diff.cpython-36.pyc
│   │           │   │   │   ├── errors.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── parser.cpython-36.pyc
│   │           │   │   │   ├── pep8.cpython-36.pyc
│   │           │   │   │   ├── prefix.cpython-36.pyc
│   │           │   │   │   ├── token.cpython-36.pyc
│   │           │   │   │   ├── tokenize.cpython-36.pyc
│   │           │   │   │   └── tree.cpython-36.pyc
│   │           │   │   ├── tokenize.py
│   │           │   │   ├── token.py
│   │           │   │   └── tree.py
│   │           │   ├── tree.py
│   │           │   └── utils.py
│   │           ├── parso-0.4.0.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── pexpect
│   │           │   ├── ANSI.py
│   │           │   ├── _async.py
│   │           │   ├── bashrc.sh
│   │           │   ├── exceptions.py
│   │           │   ├── expect.py
│   │           │   ├── fdpexpect.py
│   │           │   ├── FSM.py
│   │           │   ├── __init__.py
│   │           │   ├── popen_spawn.py
│   │           │   ├── pty_spawn.py
│   │           │   ├── pxssh.py
│   │           │   ├── __pycache__
│   │           │   │   ├── ANSI.cpython-36.pyc
│   │           │   │   ├── _async.cpython-36.pyc
│   │           │   │   ├── exceptions.cpython-36.pyc
│   │           │   │   ├── expect.cpython-36.pyc
│   │           │   │   ├── fdpexpect.cpython-36.pyc
│   │           │   │   ├── FSM.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── popen_spawn.cpython-36.pyc
│   │           │   │   ├── pty_spawn.cpython-36.pyc
│   │           │   │   ├── pxssh.cpython-36.pyc
│   │           │   │   ├── replwrap.cpython-36.pyc
│   │           │   │   ├── run.cpython-36.pyc
│   │           │   │   ├── screen.cpython-36.pyc
│   │           │   │   ├── spawnbase.cpython-36.pyc
│   │           │   │   └── utils.cpython-36.pyc
│   │           │   ├── replwrap.py
│   │           │   ├── run.py
│   │           │   ├── screen.py
│   │           │   ├── spawnbase.py
│   │           │   └── utils.py
│   │           ├── pexpect-4.7.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── pickleshare-0.7.5.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── pickleshare.py
│   │           ├── pip
│   │           │   ├── basecommand.py
│   │           │   ├── baseparser.py
│   │           │   ├── cmdoptions.py
│   │           │   ├── commands
│   │           │   │   ├── check.py
│   │           │   │   ├── completion.py
│   │           │   │   ├── download.py
│   │           │   │   ├── freeze.py
│   │           │   │   ├── hash.py
│   │           │   │   ├── help.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── install.py
│   │           │   │   ├── list.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── check.cpython-36.pyc
│   │           │   │   │   ├── completion.cpython-36.pyc
│   │           │   │   │   ├── download.cpython-36.pyc
│   │           │   │   │   ├── freeze.cpython-36.pyc
│   │           │   │   │   ├── hash.cpython-36.pyc
│   │           │   │   │   ├── help.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── install.cpython-36.pyc
│   │           │   │   │   ├── list.cpython-36.pyc
│   │           │   │   │   ├── search.cpython-36.pyc
│   │           │   │   │   ├── show.cpython-36.pyc
│   │           │   │   │   ├── uninstall.cpython-36.pyc
│   │           │   │   │   └── wheel.cpython-36.pyc
│   │           │   │   ├── search.py
│   │           │   │   ├── show.py
│   │           │   │   ├── uninstall.py
│   │           │   │   └── wheel.py
│   │           │   ├── compat
│   │           │   │   ├── dictconfig.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── dictconfig.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── download.py
│   │           │   ├── exceptions.py
│   │           │   ├── index.py
│   │           │   ├── __init__.py
│   │           │   ├── locations.py
│   │           │   ├── __main__.py
│   │           │   ├── models
│   │           │   │   ├── index.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── index.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── operations
│   │           │   │   ├── check.py
│   │           │   │   ├── freeze.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── check.cpython-36.pyc
│   │           │   │       ├── freeze.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── pep425tags.py
│   │           │   ├── __pycache__
│   │           │   │   ├── basecommand.cpython-36.pyc
│   │           │   │   ├── baseparser.cpython-36.pyc
│   │           │   │   ├── cmdoptions.cpython-36.pyc
│   │           │   │   ├── download.cpython-36.pyc
│   │           │   │   ├── exceptions.cpython-36.pyc
│   │           │   │   ├── index.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── locations.cpython-36.pyc
│   │           │   │   ├── __main__.cpython-36.pyc
│   │           │   │   ├── pep425tags.cpython-36.pyc
│   │           │   │   ├── status_codes.cpython-36.pyc
│   │           │   │   └── wheel.cpython-36.pyc
│   │           │   ├── req
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── req_file.cpython-36.pyc
│   │           │   │   │   ├── req_install.cpython-36.pyc
│   │           │   │   │   ├── req_set.cpython-36.pyc
│   │           │   │   │   └── req_uninstall.cpython-36.pyc
│   │           │   │   ├── req_file.py
│   │           │   │   ├── req_install.py
│   │           │   │   ├── req_set.py
│   │           │   │   └── req_uninstall.py
│   │           │   ├── status_codes.py
│   │           │   ├── utils
│   │           │   │   ├── appdirs.py
│   │           │   │   ├── build.py
│   │           │   │   ├── deprecation.py
│   │           │   │   ├── encoding.py
│   │           │   │   ├── filesystem.py
│   │           │   │   ├── glibc.py
│   │           │   │   ├── hashes.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── logging.py
│   │           │   │   ├── outdated.py
│   │           │   │   ├── packaging.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── appdirs.cpython-36.pyc
│   │           │   │   │   ├── build.cpython-36.pyc
│   │           │   │   │   ├── deprecation.cpython-36.pyc
│   │           │   │   │   ├── encoding.cpython-36.pyc
│   │           │   │   │   ├── filesystem.cpython-36.pyc
│   │           │   │   │   ├── glibc.cpython-36.pyc
│   │           │   │   │   ├── hashes.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── logging.cpython-36.pyc
│   │           │   │   │   ├── outdated.cpython-36.pyc
│   │           │   │   │   ├── packaging.cpython-36.pyc
│   │           │   │   │   ├── setuptools_build.cpython-36.pyc
│   │           │   │   │   └── ui.cpython-36.pyc
│   │           │   │   ├── setuptools_build.py
│   │           │   │   └── ui.py
│   │           │   ├── vcs
│   │           │   │   ├── bazaar.py
│   │           │   │   ├── git.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── mercurial.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── bazaar.cpython-36.pyc
│   │           │   │   │   ├── git.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── mercurial.cpython-36.pyc
│   │           │   │   │   └── subversion.cpython-36.pyc
│   │           │   │   └── subversion.py
│   │           │   ├── _vendor
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   └── wheel.py
│   │           ├── pip-9.0.1.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── pkg_resources
│   │           │   ├── extern
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── __init__.py
│   │           │   ├── py31compat.py
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   └── py31compat.cpython-36.pyc
│   │           │   └── _vendor
│   │           │       ├── appdirs.py
│   │           │       ├── __init__.py
│   │           │       ├── packaging
│   │           │       │   ├── __about__.py
│   │           │       │   ├── _compat.py
│   │           │       │   ├── __init__.py
│   │           │       │   ├── markers.py
│   │           │       │   ├── __pycache__
│   │           │       │   │   ├── __about__.cpython-36.pyc
│   │           │       │   │   ├── _compat.cpython-36.pyc
│   │           │       │   │   ├── __init__.cpython-36.pyc
│   │           │       │   │   ├── markers.cpython-36.pyc
│   │           │       │   │   ├── requirements.cpython-36.pyc
│   │           │       │   │   ├── specifiers.cpython-36.pyc
│   │           │       │   │   ├── _structures.cpython-36.pyc
│   │           │       │   │   ├── utils.cpython-36.pyc
│   │           │       │   │   └── version.cpython-36.pyc
│   │           │       │   ├── requirements.py
│   │           │       │   ├── specifiers.py
│   │           │       │   ├── _structures.py
│   │           │       │   ├── utils.py
│   │           │       │   └── version.py
│   │           │       ├── __pycache__
│   │           │       │   ├── appdirs.cpython-36.pyc
│   │           │       │   ├── __init__.cpython-36.pyc
│   │           │       │   ├── pyparsing.cpython-36.pyc
│   │           │       │   └── six.cpython-36.pyc
│   │           │       ├── pyparsing.py
│   │           │       └── six.py
│   │           ├── pkg_resources-0.0.0.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── prometheus_client
│   │           │   ├── bridge
│   │           │   │   ├── graphite.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── graphite.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── context_managers.py
│   │           │   ├── core.py
│   │           │   ├── decorator.py
│   │           │   ├── exposition.py
│   │           │   ├── gc_collector.py
│   │           │   ├── __init__.py
│   │           │   ├── metrics_core.py
│   │           │   ├── metrics.py
│   │           │   ├── mmap_dict.py
│   │           │   ├── multiprocess.py
│   │           │   ├── openmetrics
│   │           │   │   ├── exposition.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── parser.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── exposition.cpython-36.pyc
│   │           │   │       ├── __init__.cpython-36.pyc
│   │           │   │       └── parser.cpython-36.pyc
│   │           │   ├── parser.py
│   │           │   ├── platform_collector.py
│   │           │   ├── process_collector.py
│   │           │   ├── __pycache__
│   │           │   │   ├── context_managers.cpython-36.pyc
│   │           │   │   ├── core.cpython-36.pyc
│   │           │   │   ├── decorator.cpython-36.pyc
│   │           │   │   ├── exposition.cpython-36.pyc
│   │           │   │   ├── gc_collector.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── metrics_core.cpython-36.pyc
│   │           │   │   ├── metrics.cpython-36.pyc
│   │           │   │   ├── mmap_dict.cpython-36.pyc
│   │           │   │   ├── multiprocess.cpython-36.pyc
│   │           │   │   ├── parser.cpython-36.pyc
│   │           │   │   ├── platform_collector.cpython-36.pyc
│   │           │   │   ├── process_collector.cpython-36.pyc
│   │           │   │   ├── registry.cpython-36.pyc
│   │           │   │   ├── samples.cpython-36.pyc
│   │           │   │   ├── utils.cpython-36.pyc
│   │           │   │   └── values.cpython-36.pyc
│   │           │   ├── registry.py
│   │           │   ├── samples.py
│   │           │   ├── twisted
│   │           │   │   ├── _exposition.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── _exposition.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── utils.py
│   │           │   └── values.py
│   │           ├── prometheus_client-0.6.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── prompt_toolkit
│   │           │   ├── application
│   │           │   │   ├── application.py
│   │           │   │   ├── current.py
│   │           │   │   ├── dummy.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── application.cpython-36.pyc
│   │           │   │   │   ├── current.cpython-36.pyc
│   │           │   │   │   ├── dummy.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── run_in_terminal.cpython-36.pyc
│   │           │   │   └── run_in_terminal.py
│   │           │   ├── auto_suggest.py
│   │           │   ├── buffer.py
│   │           │   ├── cache.py
│   │           │   ├── clipboard
│   │           │   │   ├── base.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── in_memory.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── in_memory.cpython-36.pyc
│   │           │   │   │   └── pyperclip.cpython-36.pyc
│   │           │   │   └── pyperclip.py
│   │           │   ├── completion
│   │           │   │   ├── base.py
│   │           │   │   ├── filesystem.py
│   │           │   │   ├── fuzzy_completer.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── filesystem.cpython-36.pyc
│   │           │   │   │   ├── fuzzy_completer.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── word_completer.cpython-36.pyc
│   │           │   │   └── word_completer.py
│   │           │   ├── contrib
│   │           │   │   ├── completers
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── system.cpython-36.pyc
│   │           │   │   │   └── system.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   ├── regular_languages
│   │           │   │   │   ├── compiler.py
│   │           │   │   │   ├── completion.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── lexer.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── compiler.cpython-36.pyc
│   │           │   │   │   │   ├── completion.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── lexer.cpython-36.pyc
│   │           │   │   │   │   ├── regex_parser.cpython-36.pyc
│   │           │   │   │   │   └── validation.cpython-36.pyc
│   │           │   │   │   ├── regex_parser.py
│   │           │   │   │   └── validation.py
│   │           │   │   └── telnet
│   │           │   │       ├── __init__.py
│   │           │   │       ├── log.py
│   │           │   │       ├── protocol.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── log.cpython-36.pyc
│   │           │   │       │   ├── protocol.cpython-36.pyc
│   │           │   │       │   └── server.cpython-36.pyc
│   │           │   │       └── server.py
│   │           │   ├── document.py
│   │           │   ├── enums.py
│   │           │   ├── eventloop
│   │           │   │   ├── async_generator.py
│   │           │   │   ├── asyncio_posix.py
│   │           │   │   ├── asyncio_win32.py
│   │           │   │   ├── base.py
│   │           │   │   ├── context.py
│   │           │   │   ├── coroutine.py
│   │           │   │   ├── defaults.py
│   │           │   │   ├── event.py
│   │           │   │   ├── future.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── inputhook.py
│   │           │   │   ├── posix.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── async_generator.cpython-36.pyc
│   │           │   │   │   ├── asyncio_posix.cpython-36.pyc
│   │           │   │   │   ├── asyncio_win32.cpython-36.pyc
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── context.cpython-36.pyc
│   │           │   │   │   ├── coroutine.cpython-36.pyc
│   │           │   │   │   ├── defaults.cpython-36.pyc
│   │           │   │   │   ├── event.cpython-36.pyc
│   │           │   │   │   ├── future.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── inputhook.cpython-36.pyc
│   │           │   │   │   ├── posix.cpython-36.pyc
│   │           │   │   │   ├── select.cpython-36.pyc
│   │           │   │   │   ├── utils.cpython-36.pyc
│   │           │   │   │   └── win32.cpython-36.pyc
│   │           │   │   ├── select.py
│   │           │   │   ├── utils.py
│   │           │   │   └── win32.py
│   │           │   ├── filters
│   │           │   │   ├── app.py
│   │           │   │   ├── base.py
│   │           │   │   ├── cli.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── app.cpython-36.pyc
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── cli.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── utils.cpython-36.pyc
│   │           │   │   └── utils.py
│   │           │   ├── formatted_text
│   │           │   │   ├── ansi.py
│   │           │   │   ├── base.py
│   │           │   │   ├── html.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── ansi.cpython-36.pyc
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── html.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── pygments.cpython-36.pyc
│   │           │   │   │   └── utils.cpython-36.pyc
│   │           │   │   ├── pygments.py
│   │           │   │   └── utils.py
│   │           │   ├── history.py
│   │           │   ├── __init__.py
│   │           │   ├── input
│   │           │   │   ├── ansi_escape_sequences.py
│   │           │   │   ├── base.py
│   │           │   │   ├── defaults.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── posix_pipe.py
│   │           │   │   ├── posix_utils.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── ansi_escape_sequences.cpython-36.pyc
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── defaults.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── posix_pipe.cpython-36.pyc
│   │           │   │   │   ├── posix_utils.cpython-36.pyc
│   │           │   │   │   ├── typeahead.cpython-36.pyc
│   │           │   │   │   ├── vt100.cpython-36.pyc
│   │           │   │   │   ├── vt100_parser.cpython-36.pyc
│   │           │   │   │   ├── win32.cpython-36.pyc
│   │           │   │   │   └── win32_pipe.cpython-36.pyc
│   │           │   │   ├── typeahead.py
│   │           │   │   ├── vt100_parser.py
│   │           │   │   ├── vt100.py
│   │           │   │   ├── win32_pipe.py
│   │           │   │   └── win32.py
│   │           │   ├── key_binding
│   │           │   │   ├── bindings
│   │           │   │   │   ├── auto_suggest.py
│   │           │   │   │   ├── basic.py
│   │           │   │   │   ├── completion.py
│   │           │   │   │   ├── cpr.py
│   │           │   │   │   ├── emacs.py
│   │           │   │   │   ├── focus.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── mouse.py
│   │           │   │   │   ├── named_commands.py
│   │           │   │   │   ├── open_in_editor.py
│   │           │   │   │   ├── page_navigation.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── auto_suggest.cpython-36.pyc
│   │           │   │   │   │   ├── basic.cpython-36.pyc
│   │           │   │   │   │   ├── completion.cpython-36.pyc
│   │           │   │   │   │   ├── cpr.cpython-36.pyc
│   │           │   │   │   │   ├── emacs.cpython-36.pyc
│   │           │   │   │   │   ├── focus.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── mouse.cpython-36.pyc
│   │           │   │   │   │   ├── named_commands.cpython-36.pyc
│   │           │   │   │   │   ├── open_in_editor.cpython-36.pyc
│   │           │   │   │   │   ├── page_navigation.cpython-36.pyc
│   │           │   │   │   │   ├── scroll.cpython-36.pyc
│   │           │   │   │   │   ├── search.cpython-36.pyc
│   │           │   │   │   │   └── vi.cpython-36.pyc
│   │           │   │   │   ├── scroll.py
│   │           │   │   │   ├── search.py
│   │           │   │   │   └── vi.py
│   │           │   │   ├── defaults.py
│   │           │   │   ├── digraphs.py
│   │           │   │   ├── emacs_state.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── key_bindings.py
│   │           │   │   ├── key_processor.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── defaults.cpython-36.pyc
│   │           │   │   │   ├── digraphs.cpython-36.pyc
│   │           │   │   │   ├── emacs_state.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── key_bindings.cpython-36.pyc
│   │           │   │   │   ├── key_processor.cpython-36.pyc
│   │           │   │   │   └── vi_state.cpython-36.pyc
│   │           │   │   └── vi_state.py
│   │           │   ├── keys.py
│   │           │   ├── layout
│   │           │   │   ├── containers.py
│   │           │   │   ├── controls.py
│   │           │   │   ├── dimension.py
│   │           │   │   ├── dummy.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── layout.py
│   │           │   │   ├── margins.py
│   │           │   │   ├── menus.py
│   │           │   │   ├── mouse_handlers.py
│   │           │   │   ├── processors.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── containers.cpython-36.pyc
│   │           │   │   │   ├── controls.cpython-36.pyc
│   │           │   │   │   ├── dimension.cpython-36.pyc
│   │           │   │   │   ├── dummy.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── layout.cpython-36.pyc
│   │           │   │   │   ├── margins.cpython-36.pyc
│   │           │   │   │   ├── menus.cpython-36.pyc
│   │           │   │   │   ├── mouse_handlers.cpython-36.pyc
│   │           │   │   │   ├── processors.cpython-36.pyc
│   │           │   │   │   ├── screen.cpython-36.pyc
│   │           │   │   │   └── utils.cpython-36.pyc
│   │           │   │   ├── screen.py
│   │           │   │   └── utils.py
│   │           │   ├── lexers
│   │           │   │   ├── base.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── pygments.cpython-36.pyc
│   │           │   │   └── pygments.py
│   │           │   ├── log.py
│   │           │   ├── mouse_events.py
│   │           │   ├── output
│   │           │   │   ├── base.py
│   │           │   │   ├── color_depth.py
│   │           │   │   ├── conemu.py
│   │           │   │   ├── defaults.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── color_depth.cpython-36.pyc
│   │           │   │   │   ├── conemu.cpython-36.pyc
│   │           │   │   │   ├── defaults.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── vt100.cpython-36.pyc
│   │           │   │   │   ├── win32.cpython-36.pyc
│   │           │   │   │   └── windows10.cpython-36.pyc
│   │           │   │   ├── vt100.py
│   │           │   │   ├── win32.py
│   │           │   │   └── windows10.py
│   │           │   ├── patch_stdout.py
│   │           │   ├── __pycache__
│   │           │   │   ├── auto_suggest.cpython-36.pyc
│   │           │   │   ├── buffer.cpython-36.pyc
│   │           │   │   ├── cache.cpython-36.pyc
│   │           │   │   ├── document.cpython-36.pyc
│   │           │   │   ├── enums.cpython-36.pyc
│   │           │   │   ├── history.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── keys.cpython-36.pyc
│   │           │   │   ├── log.cpython-36.pyc
│   │           │   │   ├── mouse_events.cpython-36.pyc
│   │           │   │   ├── patch_stdout.cpython-36.pyc
│   │           │   │   ├── renderer.cpython-36.pyc
│   │           │   │   ├── search.cpython-36.pyc
│   │           │   │   ├── selection.cpython-36.pyc
│   │           │   │   ├── token.cpython-36.pyc
│   │           │   │   ├── utils.cpython-36.pyc
│   │           │   │   ├── validation.cpython-36.pyc
│   │           │   │   └── win32_types.cpython-36.pyc
│   │           │   ├── renderer.py
│   │           │   ├── search.py
│   │           │   ├── selection.py
│   │           │   ├── shortcuts
│   │           │   │   ├── dialogs.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── progress_bar
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── formatters.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── base.cpython-36.pyc
│   │           │   │   │       ├── formatters.cpython-36.pyc
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   ├── prompt.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── dialogs.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── prompt.cpython-36.pyc
│   │           │   │   │   └── utils.cpython-36.pyc
│   │           │   │   └── utils.py
│   │           │   ├── styles
│   │           │   │   ├── base.py
│   │           │   │   ├── defaults.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── named_colors.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── defaults.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── named_colors.cpython-36.pyc
│   │           │   │   │   ├── pygments.cpython-36.pyc
│   │           │   │   │   ├── style.cpython-36.pyc
│   │           │   │   │   └── style_transformation.cpython-36.pyc
│   │           │   │   ├── pygments.py
│   │           │   │   ├── style.py
│   │           │   │   └── style_transformation.py
│   │           │   ├── token.py
│   │           │   ├── utils.py
│   │           │   ├── validation.py
│   │           │   ├── widgets
│   │           │   │   ├── base.py
│   │           │   │   ├── dialogs.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── menus.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── dialogs.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── menus.cpython-36.pyc
│   │           │   │   │   └── toolbars.cpython-36.pyc
│   │           │   │   └── toolbars.py
│   │           │   └── win32_types.py
│   │           ├── prompt_toolkit-2.0.9.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── ptyprocess
│   │           │   ├── _fork_pty.py
│   │           │   ├── __init__.py
│   │           │   ├── ptyprocess.py
│   │           │   ├── __pycache__
│   │           │   │   ├── _fork_pty.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── ptyprocess.cpython-36.pyc
│   │           │   │   └── util.cpython-36.pyc
│   │           │   └── util.py
│   │           ├── ptyprocess-0.6.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── pvectorc.cpython-36m-x86_64-linux-gnu.so
│   │           ├── __pycache__
│   │           │   ├── cycler.cpython-36.pyc
│   │           │   ├── decorator.cpython-36.pyc
│   │           │   ├── easy_install.cpython-36.pyc
│   │           │   ├── entrypoints.cpython-36.pyc
│   │           │   ├── ipykernel_launcher.cpython-36.pyc
│   │           │   ├── isympy.cpython-36.pyc
│   │           │   ├── jupyter.cpython-36.pyc
│   │           │   ├── mistune.cpython-36.pyc
│   │           │   ├── pandocfilters.cpython-36.pyc
│   │           │   ├── pickleshare.cpython-36.pyc
│   │           │   ├── pylab.cpython-36.pyc
│   │           │   ├── pyparsing.cpython-36.pyc
│   │           │   ├── _pyrsistent_version.cpython-36.pyc
│   │           │   └── six.cpython-36.pyc
│   │           ├── pygments
│   │           │   ├── cmdline.py
│   │           │   ├── console.py
│   │           │   ├── filter.py
│   │           │   ├── filters
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── formatter.py
│   │           │   ├── formatters
│   │           │   │   ├── bbcode.py
│   │           │   │   ├── html.py
│   │           │   │   ├── img.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── irc.py
│   │           │   │   ├── latex.py
│   │           │   │   ├── _mapping.py
│   │           │   │   ├── other.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── bbcode.cpython-36.pyc
│   │           │   │   │   ├── html.cpython-36.pyc
│   │           │   │   │   ├── img.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── irc.cpython-36.pyc
│   │           │   │   │   ├── latex.cpython-36.pyc
│   │           │   │   │   ├── _mapping.cpython-36.pyc
│   │           │   │   │   ├── other.cpython-36.pyc
│   │           │   │   │   ├── rtf.cpython-36.pyc
│   │           │   │   │   ├── svg.cpython-36.pyc
│   │           │   │   │   ├── terminal256.cpython-36.pyc
│   │           │   │   │   └── terminal.cpython-36.pyc
│   │           │   │   ├── rtf.py
│   │           │   │   ├── svg.py
│   │           │   │   ├── terminal256.py
│   │           │   │   └── terminal.py
│   │           │   ├── __init__.py
│   │           │   ├── lexer.py
│   │           │   ├── lexers
│   │           │   │   ├── actionscript.py
│   │           │   │   ├── agile.py
│   │           │   │   ├── algebra.py
│   │           │   │   ├── ambient.py
│   │           │   │   ├── ampl.py
│   │           │   │   ├── apl.py
│   │           │   │   ├── archetype.py
│   │           │   │   ├── asm.py
│   │           │   │   ├── _asy_builtins.py
│   │           │   │   ├── automation.py
│   │           │   │   ├── basic.py
│   │           │   │   ├── bibtex.py
│   │           │   │   ├── business.py
│   │           │   │   ├── capnproto.py
│   │           │   │   ├── c_cpp.py
│   │           │   │   ├── chapel.py
│   │           │   │   ├── _cl_builtins.py
│   │           │   │   ├── clean.py
│   │           │   │   ├── c_like.py
│   │           │   │   ├── _cocoa_builtins.py
│   │           │   │   ├── compiled.py
│   │           │   │   ├── configs.py
│   │           │   │   ├── console.py
│   │           │   │   ├── crystal.py
│   │           │   │   ├── _csound_builtins.py
│   │           │   │   ├── csound.py
│   │           │   │   ├── css.py
│   │           │   │   ├── dalvik.py
│   │           │   │   ├── data.py
│   │           │   │   ├── diff.py
│   │           │   │   ├── dotnet.py
│   │           │   │   ├── d.py
│   │           │   │   ├── dsls.py
│   │           │   │   ├── dylan.py
│   │           │   │   ├── ecl.py
│   │           │   │   ├── eiffel.py
│   │           │   │   ├── elm.py
│   │           │   │   ├── erlang.py
│   │           │   │   ├── esoteric.py
│   │           │   │   ├── ezhil.py
│   │           │   │   ├── factor.py
│   │           │   │   ├── fantom.py
│   │           │   │   ├── felix.py
│   │           │   │   ├── forth.py
│   │           │   │   ├── fortran.py
│   │           │   │   ├── foxpro.py
│   │           │   │   ├── functional.py
│   │           │   │   ├── go.py
│   │           │   │   ├── grammar_notation.py
│   │           │   │   ├── graphics.py
│   │           │   │   ├── graph.py
│   │           │   │   ├── haskell.py
│   │           │   │   ├── haxe.py
│   │           │   │   ├── hdl.py
│   │           │   │   ├── hexdump.py
│   │           │   │   ├── html.py
│   │           │   │   ├── idl.py
│   │           │   │   ├── igor.py
│   │           │   │   ├── inferno.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── installers.py
│   │           │   │   ├── int_fiction.py
│   │           │   │   ├── iolang.py
│   │           │   │   ├── javascript.py
│   │           │   │   ├── j.py
│   │           │   │   ├── julia.py
│   │           │   │   ├── jvm.py
│   │           │   │   ├── _lasso_builtins.py
│   │           │   │   ├── lisp.py
│   │           │   │   ├── _lua_builtins.py
│   │           │   │   ├── make.py
│   │           │   │   ├── _mapping.py
│   │           │   │   ├── markup.py
│   │           │   │   ├── math.py
│   │           │   │   ├── matlab.py
│   │           │   │   ├── ml.py
│   │           │   │   ├── modeling.py
│   │           │   │   ├── modula2.py
│   │           │   │   ├── monte.py
│   │           │   │   ├── _mql_builtins.py
│   │           │   │   ├── ncl.py
│   │           │   │   ├── nimrod.py
│   │           │   │   ├── nit.py
│   │           │   │   ├── nix.py
│   │           │   │   ├── oberon.py
│   │           │   │   ├── objective.py
│   │           │   │   ├── ooc.py
│   │           │   │   ├── _openedge_builtins.py
│   │           │   │   ├── other.py
│   │           │   │   ├── parasail.py
│   │           │   │   ├── parsers.py
│   │           │   │   ├── pascal.py
│   │           │   │   ├── pawn.py
│   │           │   │   ├── perl.py
│   │           │   │   ├── _php_builtins.py
│   │           │   │   ├── php.py
│   │           │   │   ├── _postgres_builtins.py
│   │           │   │   ├── praat.py
│   │           │   │   ├── prolog.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── actionscript.cpython-36.pyc
│   │           │   │   │   ├── agile.cpython-36.pyc
│   │           │   │   │   ├── algebra.cpython-36.pyc
│   │           │   │   │   ├── ambient.cpython-36.pyc
│   │           │   │   │   ├── ampl.cpython-36.pyc
│   │           │   │   │   ├── apl.cpython-36.pyc
│   │           │   │   │   ├── archetype.cpython-36.pyc
│   │           │   │   │   ├── asm.cpython-36.pyc
│   │           │   │   │   ├── _asy_builtins.cpython-36.pyc
│   │           │   │   │   ├── automation.cpython-36.pyc
│   │           │   │   │   ├── basic.cpython-36.pyc
│   │           │   │   │   ├── bibtex.cpython-36.pyc
│   │           │   │   │   ├── business.cpython-36.pyc
│   │           │   │   │   ├── capnproto.cpython-36.pyc
│   │           │   │   │   ├── c_cpp.cpython-36.pyc
│   │           │   │   │   ├── chapel.cpython-36.pyc
│   │           │   │   │   ├── _cl_builtins.cpython-36.pyc
│   │           │   │   │   ├── clean.cpython-36.pyc
│   │           │   │   │   ├── c_like.cpython-36.pyc
│   │           │   │   │   ├── _cocoa_builtins.cpython-36.pyc
│   │           │   │   │   ├── compiled.cpython-36.pyc
│   │           │   │   │   ├── configs.cpython-36.pyc
│   │           │   │   │   ├── console.cpython-36.pyc
│   │           │   │   │   ├── crystal.cpython-36.pyc
│   │           │   │   │   ├── _csound_builtins.cpython-36.pyc
│   │           │   │   │   ├── csound.cpython-36.pyc
│   │           │   │   │   ├── css.cpython-36.pyc
│   │           │   │   │   ├── dalvik.cpython-36.pyc
│   │           │   │   │   ├── data.cpython-36.pyc
│   │           │   │   │   ├── d.cpython-36.pyc
│   │           │   │   │   ├── diff.cpython-36.pyc
│   │           │   │   │   ├── dotnet.cpython-36.pyc
│   │           │   │   │   ├── dsls.cpython-36.pyc
│   │           │   │   │   ├── dylan.cpython-36.pyc
│   │           │   │   │   ├── ecl.cpython-36.pyc
│   │           │   │   │   ├── eiffel.cpython-36.pyc
│   │           │   │   │   ├── elm.cpython-36.pyc
│   │           │   │   │   ├── erlang.cpython-36.pyc
│   │           │   │   │   ├── esoteric.cpython-36.pyc
│   │           │   │   │   ├── ezhil.cpython-36.pyc
│   │           │   │   │   ├── factor.cpython-36.pyc
│   │           │   │   │   ├── fantom.cpython-36.pyc
│   │           │   │   │   ├── felix.cpython-36.pyc
│   │           │   │   │   ├── forth.cpython-36.pyc
│   │           │   │   │   ├── fortran.cpython-36.pyc
│   │           │   │   │   ├── foxpro.cpython-36.pyc
│   │           │   │   │   ├── functional.cpython-36.pyc
│   │           │   │   │   ├── go.cpython-36.pyc
│   │           │   │   │   ├── grammar_notation.cpython-36.pyc
│   │           │   │   │   ├── graph.cpython-36.pyc
│   │           │   │   │   ├── graphics.cpython-36.pyc
│   │           │   │   │   ├── haskell.cpython-36.pyc
│   │           │   │   │   ├── haxe.cpython-36.pyc
│   │           │   │   │   ├── hdl.cpython-36.pyc
│   │           │   │   │   ├── hexdump.cpython-36.pyc
│   │           │   │   │   ├── html.cpython-36.pyc
│   │           │   │   │   ├── idl.cpython-36.pyc
│   │           │   │   │   ├── igor.cpython-36.pyc
│   │           │   │   │   ├── inferno.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── installers.cpython-36.pyc
│   │           │   │   │   ├── int_fiction.cpython-36.pyc
│   │           │   │   │   ├── iolang.cpython-36.pyc
│   │           │   │   │   ├── javascript.cpython-36.pyc
│   │           │   │   │   ├── j.cpython-36.pyc
│   │           │   │   │   ├── julia.cpython-36.pyc
│   │           │   │   │   ├── jvm.cpython-36.pyc
│   │           │   │   │   ├── _lasso_builtins.cpython-36.pyc
│   │           │   │   │   ├── lisp.cpython-36.pyc
│   │           │   │   │   ├── _lua_builtins.cpython-36.pyc
│   │           │   │   │   ├── make.cpython-36.pyc
│   │           │   │   │   ├── _mapping.cpython-36.pyc
│   │           │   │   │   ├── markup.cpython-36.pyc
│   │           │   │   │   ├── math.cpython-36.pyc
│   │           │   │   │   ├── matlab.cpython-36.pyc
│   │           │   │   │   ├── ml.cpython-36.pyc
│   │           │   │   │   ├── modeling.cpython-36.pyc
│   │           │   │   │   ├── modula2.cpython-36.pyc
│   │           │   │   │   ├── monte.cpython-36.pyc
│   │           │   │   │   ├── _mql_builtins.cpython-36.pyc
│   │           │   │   │   ├── ncl.cpython-36.pyc
│   │           │   │   │   ├── nimrod.cpython-36.pyc
│   │           │   │   │   ├── nit.cpython-36.pyc
│   │           │   │   │   ├── nix.cpython-36.pyc
│   │           │   │   │   ├── oberon.cpython-36.pyc
│   │           │   │   │   ├── objective.cpython-36.pyc
│   │           │   │   │   ├── ooc.cpython-36.pyc
│   │           │   │   │   ├── _openedge_builtins.cpython-36.pyc
│   │           │   │   │   ├── other.cpython-36.pyc
│   │           │   │   │   ├── parasail.cpython-36.pyc
│   │           │   │   │   ├── parsers.cpython-36.pyc
│   │           │   │   │   ├── pascal.cpython-36.pyc
│   │           │   │   │   ├── pawn.cpython-36.pyc
│   │           │   │   │   ├── perl.cpython-36.pyc
│   │           │   │   │   ├── _php_builtins.cpython-36.pyc
│   │           │   │   │   ├── php.cpython-36.pyc
│   │           │   │   │   ├── _postgres_builtins.cpython-36.pyc
│   │           │   │   │   ├── praat.cpython-36.pyc
│   │           │   │   │   ├── prolog.cpython-36.pyc
│   │           │   │   │   ├── python.cpython-36.pyc
│   │           │   │   │   ├── qvt.cpython-36.pyc
│   │           │   │   │   ├── r.cpython-36.pyc
│   │           │   │   │   ├── rdf.cpython-36.pyc
│   │           │   │   │   ├── rebol.cpython-36.pyc
│   │           │   │   │   ├── resource.cpython-36.pyc
│   │           │   │   │   ├── rnc.cpython-36.pyc
│   │           │   │   │   ├── roboconf.cpython-36.pyc
│   │           │   │   │   ├── robotframework.cpython-36.pyc
│   │           │   │   │   ├── ruby.cpython-36.pyc
│   │           │   │   │   ├── rust.cpython-36.pyc
│   │           │   │   │   ├── sas.cpython-36.pyc
│   │           │   │   │   ├── _scilab_builtins.cpython-36.pyc
│   │           │   │   │   ├── scripting.cpython-36.pyc
│   │           │   │   │   ├── shell.cpython-36.pyc
│   │           │   │   │   ├── smalltalk.cpython-36.pyc
│   │           │   │   │   ├── smv.cpython-36.pyc
│   │           │   │   │   ├── snobol.cpython-36.pyc
│   │           │   │   │   ├── _sourcemod_builtins.cpython-36.pyc
│   │           │   │   │   ├── special.cpython-36.pyc
│   │           │   │   │   ├── sql.cpython-36.pyc
│   │           │   │   │   ├── _stan_builtins.cpython-36.pyc
│   │           │   │   │   ├── _stata_builtins.cpython-36.pyc
│   │           │   │   │   ├── stata.cpython-36.pyc
│   │           │   │   │   ├── supercollider.cpython-36.pyc
│   │           │   │   │   ├── tcl.cpython-36.pyc
│   │           │   │   │   ├── templates.cpython-36.pyc
│   │           │   │   │   ├── testing.cpython-36.pyc
│   │           │   │   │   ├── text.cpython-36.pyc
│   │           │   │   │   ├── textedit.cpython-36.pyc
│   │           │   │   │   ├── textfmts.cpython-36.pyc
│   │           │   │   │   ├── theorem.cpython-36.pyc
│   │           │   │   │   ├── trafficscript.cpython-36.pyc
│   │           │   │   │   ├── _tsql_builtins.cpython-36.pyc
│   │           │   │   │   ├── typoscript.cpython-36.pyc
│   │           │   │   │   ├── urbi.cpython-36.pyc
│   │           │   │   │   ├── varnish.cpython-36.pyc
│   │           │   │   │   ├── verification.cpython-36.pyc
│   │           │   │   │   ├── _vim_builtins.cpython-36.pyc
│   │           │   │   │   ├── web.cpython-36.pyc
│   │           │   │   │   ├── webmisc.cpython-36.pyc
│   │           │   │   │   ├── whiley.cpython-36.pyc
│   │           │   │   │   ├── x10.cpython-36.pyc
│   │           │   │   │   └── xorg.cpython-36.pyc
│   │           │   │   ├── python.py
│   │           │   │   ├── qvt.py
│   │           │   │   ├── rdf.py
│   │           │   │   ├── rebol.py
│   │           │   │   ├── resource.py
│   │           │   │   ├── rnc.py
│   │           │   │   ├── roboconf.py
│   │           │   │   ├── robotframework.py
│   │           │   │   ├── r.py
│   │           │   │   ├── ruby.py
│   │           │   │   ├── rust.py
│   │           │   │   ├── sas.py
│   │           │   │   ├── _scilab_builtins.py
│   │           │   │   ├── scripting.py
│   │           │   │   ├── shell.py
│   │           │   │   ├── smalltalk.py
│   │           │   │   ├── smv.py
│   │           │   │   ├── snobol.py
│   │           │   │   ├── _sourcemod_builtins.py
│   │           │   │   ├── special.py
│   │           │   │   ├── sql.py
│   │           │   │   ├── _stan_builtins.py
│   │           │   │   ├── _stata_builtins.py
│   │           │   │   ├── stata.py
│   │           │   │   ├── supercollider.py
│   │           │   │   ├── tcl.py
│   │           │   │   ├── templates.py
│   │           │   │   ├── testing.py
│   │           │   │   ├── textedit.py
│   │           │   │   ├── textfmts.py
│   │           │   │   ├── text.py
│   │           │   │   ├── theorem.py
│   │           │   │   ├── trafficscript.py
│   │           │   │   ├── _tsql_builtins.py
│   │           │   │   ├── typoscript.py
│   │           │   │   ├── urbi.py
│   │           │   │   ├── varnish.py
│   │           │   │   ├── verification.py
│   │           │   │   ├── _vim_builtins.py
│   │           │   │   ├── webmisc.py
│   │           │   │   ├── web.py
│   │           │   │   ├── whiley.py
│   │           │   │   ├── x10.py
│   │           │   │   └── xorg.py
│   │           │   ├── modeline.py
│   │           │   ├── plugin.py
│   │           │   ├── __pycache__
│   │           │   │   ├── cmdline.cpython-36.pyc
│   │           │   │   ├── console.cpython-36.pyc
│   │           │   │   ├── filter.cpython-36.pyc
│   │           │   │   ├── formatter.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── lexer.cpython-36.pyc
│   │           │   │   ├── modeline.cpython-36.pyc
│   │           │   │   ├── plugin.cpython-36.pyc
│   │           │   │   ├── regexopt.cpython-36.pyc
│   │           │   │   ├── scanner.cpython-36.pyc
│   │           │   │   ├── sphinxext.cpython-36.pyc
│   │           │   │   ├── style.cpython-36.pyc
│   │           │   │   ├── token.cpython-36.pyc
│   │           │   │   ├── unistring.cpython-36.pyc
│   │           │   │   └── util.cpython-36.pyc
│   │           │   ├── regexopt.py
│   │           │   ├── scanner.py
│   │           │   ├── sphinxext.py
│   │           │   ├── style.py
│   │           │   ├── styles
│   │           │   │   ├── abap.py
│   │           │   │   ├── algol_nu.py
│   │           │   │   ├── algol.py
│   │           │   │   ├── arduino.py
│   │           │   │   ├── autumn.py
│   │           │   │   ├── borland.py
│   │           │   │   ├── bw.py
│   │           │   │   ├── colorful.py
│   │           │   │   ├── default.py
│   │           │   │   ├── emacs.py
│   │           │   │   ├── friendly.py
│   │           │   │   ├── fruity.py
│   │           │   │   ├── igor.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── lovelace.py
│   │           │   │   ├── manni.py
│   │           │   │   ├── monokai.py
│   │           │   │   ├── murphy.py
│   │           │   │   ├── native.py
│   │           │   │   ├── paraiso_dark.py
│   │           │   │   ├── paraiso_light.py
│   │           │   │   ├── pastie.py
│   │           │   │   ├── perldoc.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── abap.cpython-36.pyc
│   │           │   │   │   ├── algol.cpython-36.pyc
│   │           │   │   │   ├── algol_nu.cpython-36.pyc
│   │           │   │   │   ├── arduino.cpython-36.pyc
│   │           │   │   │   ├── autumn.cpython-36.pyc
│   │           │   │   │   ├── borland.cpython-36.pyc
│   │           │   │   │   ├── bw.cpython-36.pyc
│   │           │   │   │   ├── colorful.cpython-36.pyc
│   │           │   │   │   ├── default.cpython-36.pyc
│   │           │   │   │   ├── emacs.cpython-36.pyc
│   │           │   │   │   ├── friendly.cpython-36.pyc
│   │           │   │   │   ├── fruity.cpython-36.pyc
│   │           │   │   │   ├── igor.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── lovelace.cpython-36.pyc
│   │           │   │   │   ├── manni.cpython-36.pyc
│   │           │   │   │   ├── monokai.cpython-36.pyc
│   │           │   │   │   ├── murphy.cpython-36.pyc
│   │           │   │   │   ├── native.cpython-36.pyc
│   │           │   │   │   ├── paraiso_dark.cpython-36.pyc
│   │           │   │   │   ├── paraiso_light.cpython-36.pyc
│   │           │   │   │   ├── pastie.cpython-36.pyc
│   │           │   │   │   ├── perldoc.cpython-36.pyc
│   │           │   │   │   ├── rainbow_dash.cpython-36.pyc
│   │           │   │   │   ├── rrt.cpython-36.pyc
│   │           │   │   │   ├── sas.cpython-36.pyc
│   │           │   │   │   ├── stata.cpython-36.pyc
│   │           │   │   │   ├── tango.cpython-36.pyc
│   │           │   │   │   ├── trac.cpython-36.pyc
│   │           │   │   │   ├── vim.cpython-36.pyc
│   │           │   │   │   ├── vs.cpython-36.pyc
│   │           │   │   │   └── xcode.cpython-36.pyc
│   │           │   │   ├── rainbow_dash.py
│   │           │   │   ├── rrt.py
│   │           │   │   ├── sas.py
│   │           │   │   ├── stata.py
│   │           │   │   ├── tango.py
│   │           │   │   ├── trac.py
│   │           │   │   ├── vim.py
│   │           │   │   ├── vs.py
│   │           │   │   └── xcode.py
│   │           │   ├── token.py
│   │           │   ├── unistring.py
│   │           │   └── util.py
│   │           ├── Pygments-2.3.1.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── pylab.py
│   │           ├── pyparsing-2.4.0.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── pyparsing.py
│   │           ├── pyrsistent
│   │           │   ├── _checked_types.py
│   │           │   ├── _compat.py
│   │           │   ├── _field_common.py
│   │           │   ├── _helpers.py
│   │           │   ├── _immutable.py
│   │           │   ├── __init__.py
│   │           │   ├── __init__.pyi
│   │           │   ├── _pbag.py
│   │           │   ├── _pclass.py
│   │           │   ├── _pdeque.py
│   │           │   ├── _plist.py
│   │           │   ├── _pmap.py
│   │           │   ├── _precord.py
│   │           │   ├── _pset.py
│   │           │   ├── _pvector.py
│   │           │   ├── __pycache__
│   │           │   │   ├── _checked_types.cpython-36.pyc
│   │           │   │   ├── _compat.cpython-36.pyc
│   │           │   │   ├── _field_common.cpython-36.pyc
│   │           │   │   ├── _helpers.cpython-36.pyc
│   │           │   │   ├── _immutable.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── _pbag.cpython-36.pyc
│   │           │   │   ├── _pclass.cpython-36.pyc
│   │           │   │   ├── _pdeque.cpython-36.pyc
│   │           │   │   ├── _plist.cpython-36.pyc
│   │           │   │   ├── _pmap.cpython-36.pyc
│   │           │   │   ├── _precord.cpython-36.pyc
│   │           │   │   ├── _pset.cpython-36.pyc
│   │           │   │   ├── _pvector.cpython-36.pyc
│   │           │   │   ├── _toolz.cpython-36.pyc
│   │           │   │   ├── _transformations.cpython-36.pyc
│   │           │   │   └── typing.cpython-36.pyc
│   │           │   ├── py.typed
│   │           │   ├── _toolz.py
│   │           │   ├── _transformations.py
│   │           │   ├── typing.py
│   │           │   └── typing.pyi
│   │           ├── pyrsistent-0.15.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENCE.mit
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── _pyrsistent_version.py
│   │           ├── python_dateutil-2.8.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   ├── WHEEL
│   │           │   └── zip-safe
│   │           ├── pytz
│   │           │   ├── exceptions.py
│   │           │   ├── __init__.py
│   │           │   ├── lazy.py
│   │           │   ├── __pycache__
│   │           │   │   ├── exceptions.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── lazy.cpython-36.pyc
│   │           │   │   ├── reference.cpython-36.pyc
│   │           │   │   ├── tzfile.cpython-36.pyc
│   │           │   │   └── tzinfo.cpython-36.pyc
│   │           │   ├── reference.py
│   │           │   ├── tzfile.py
│   │           │   ├── tzinfo.py
│   │           │   └── zoneinfo
│   │           │       ├── Africa
│   │           │       │   ├── Abidjan
│   │           │       │   ├── Accra
│   │           │       │   ├── Addis_Ababa
│   │           │       │   ├── Algiers
│   │           │       │   ├── Asmara
│   │           │       │   ├── Asmera
│   │           │       │   ├── Bamako
│   │           │       │   ├── Bangui
│   │           │       │   ├── Banjul
│   │           │       │   ├── Bissau
│   │           │       │   ├── Blantyre
│   │           │       │   ├── Brazzaville
│   │           │       │   ├── Bujumbura
│   │           │       │   ├── Cairo
│   │           │       │   ├── Casablanca
│   │           │       │   ├── Ceuta
│   │           │       │   ├── Conakry
│   │           │       │   ├── Dakar
│   │           │       │   ├── Dar_es_Salaam
│   │           │       │   ├── Djibouti
│   │           │       │   ├── Douala
│   │           │       │   ├── El_Aaiun
│   │           │       │   ├── Freetown
│   │           │       │   ├── Gaborone
│   │           │       │   ├── Harare
│   │           │       │   ├── Johannesburg
│   │           │       │   ├── Juba
│   │           │       │   ├── Kampala
│   │           │       │   ├── Khartoum
│   │           │       │   ├── Kigali
│   │           │       │   ├── Kinshasa
│   │           │       │   ├── Lagos
│   │           │       │   ├── Libreville
│   │           │       │   ├── Lome
│   │           │       │   ├── Luanda
│   │           │       │   ├── Lubumbashi
│   │           │       │   ├── Lusaka
│   │           │       │   ├── Malabo
│   │           │       │   ├── Maputo
│   │           │       │   ├── Maseru
│   │           │       │   ├── Mbabane
│   │           │       │   ├── Mogadishu
│   │           │       │   ├── Monrovia
│   │           │       │   ├── Nairobi
│   │           │       │   ├── Ndjamena
│   │           │       │   ├── Niamey
│   │           │       │   ├── Nouakchott
│   │           │       │   ├── Ouagadougou
│   │           │       │   ├── Porto-Novo
│   │           │       │   ├── Sao_Tome
│   │           │       │   ├── Timbuktu
│   │           │       │   ├── Tripoli
│   │           │       │   ├── Tunis
│   │           │       │   └── Windhoek
│   │           │       ├── America
│   │           │       │   ├── Adak
│   │           │       │   ├── Anchorage
│   │           │       │   ├── Anguilla
│   │           │       │   ├── Antigua
│   │           │       │   ├── Araguaina
│   │           │       │   ├── Argentina
│   │           │       │   │   ├── Buenos_Aires
│   │           │       │   │   ├── Catamarca
│   │           │       │   │   ├── ComodRivadavia
│   │           │       │   │   ├── Cordoba
│   │           │       │   │   ├── Jujuy
│   │           │       │   │   ├── La_Rioja
│   │           │       │   │   ├── Mendoza
│   │           │       │   │   ├── Rio_Gallegos
│   │           │       │   │   ├── Salta
│   │           │       │   │   ├── San_Juan
│   │           │       │   │   ├── San_Luis
│   │           │       │   │   ├── Tucuman
│   │           │       │   │   └── Ushuaia
│   │           │       │   ├── Aruba
│   │           │       │   ├── Asuncion
│   │           │       │   ├── Atikokan
│   │           │       │   ├── Atka
│   │           │       │   ├── Bahia
│   │           │       │   ├── Bahia_Banderas
│   │           │       │   ├── Barbados
│   │           │       │   ├── Belem
│   │           │       │   ├── Belize
│   │           │       │   ├── Blanc-Sablon
│   │           │       │   ├── Boa_Vista
│   │           │       │   ├── Bogota
│   │           │       │   ├── Boise
│   │           │       │   ├── Buenos_Aires
│   │           │       │   ├── Cambridge_Bay
│   │           │       │   ├── Campo_Grande
│   │           │       │   ├── Cancun
│   │           │       │   ├── Caracas
│   │           │       │   ├── Catamarca
│   │           │       │   ├── Cayenne
│   │           │       │   ├── Cayman
│   │           │       │   ├── Chicago
│   │           │       │   ├── Chihuahua
│   │           │       │   ├── Coral_Harbour
│   │           │       │   ├── Cordoba
│   │           │       │   ├── Costa_Rica
│   │           │       │   ├── Creston
│   │           │       │   ├── Cuiaba
│   │           │       │   ├── Curacao
│   │           │       │   ├── Danmarkshavn
│   │           │       │   ├── Dawson
│   │           │       │   ├── Dawson_Creek
│   │           │       │   ├── Denver
│   │           │       │   ├── Detroit
│   │           │       │   ├── Dominica
│   │           │       │   ├── Edmonton
│   │           │       │   ├── Eirunepe
│   │           │       │   ├── El_Salvador
│   │           │       │   ├── Ensenada
│   │           │       │   ├── Fortaleza
│   │           │       │   ├── Fort_Nelson
│   │           │       │   ├── Fort_Wayne
│   │           │       │   ├── Glace_Bay
│   │           │       │   ├── Godthab
│   │           │       │   ├── Goose_Bay
│   │           │       │   ├── Grand_Turk
│   │           │       │   ├── Grenada
│   │           │       │   ├── Guadeloupe
│   │           │       │   ├── Guatemala
│   │           │       │   ├── Guayaquil
│   │           │       │   ├── Guyana
│   │           │       │   ├── Halifax
│   │           │       │   ├── Havana
│   │           │       │   ├── Hermosillo
│   │           │       │   ├── Indiana
│   │           │       │   │   ├── Indianapolis
│   │           │       │   │   ├── Knox
│   │           │       │   │   ├── Marengo
│   │           │       │   │   ├── Petersburg
│   │           │       │   │   ├── Tell_City
│   │           │       │   │   ├── Vevay
│   │           │       │   │   ├── Vincennes
│   │           │       │   │   └── Winamac
│   │           │       │   ├── Indianapolis
│   │           │       │   ├── Inuvik
│   │           │       │   ├── Iqaluit
│   │           │       │   ├── Jamaica
│   │           │       │   ├── Jujuy
│   │           │       │   ├── Juneau
│   │           │       │   ├── Kentucky
│   │           │       │   │   ├── Louisville
│   │           │       │   │   └── Monticello
│   │           │       │   ├── Knox_IN
│   │           │       │   ├── Kralendijk
│   │           │       │   ├── La_Paz
│   │           │       │   ├── Lima
│   │           │       │   ├── Los_Angeles
│   │           │       │   ├── Louisville
│   │           │       │   ├── Lower_Princes
│   │           │       │   ├── Maceio
│   │           │       │   ├── Managua
│   │           │       │   ├── Manaus
│   │           │       │   ├── Marigot
│   │           │       │   ├── Martinique
│   │           │       │   ├── Matamoros
│   │           │       │   ├── Mazatlan
│   │           │       │   ├── Mendoza
│   │           │       │   ├── Menominee
│   │           │       │   ├── Merida
│   │           │       │   ├── Metlakatla
│   │           │       │   ├── Mexico_City
│   │           │       │   ├── Miquelon
│   │           │       │   ├── Moncton
│   │           │       │   ├── Monterrey
│   │           │       │   ├── Montevideo
│   │           │       │   ├── Montreal
│   │           │       │   ├── Montserrat
│   │           │       │   ├── Nassau
│   │           │       │   ├── New_York
│   │           │       │   ├── Nipigon
│   │           │       │   ├── Nome
│   │           │       │   ├── Noronha
│   │           │       │   ├── North_Dakota
│   │           │       │   │   ├── Beulah
│   │           │       │   │   ├── Center
│   │           │       │   │   └── New_Salem
│   │           │       │   ├── Ojinaga
│   │           │       │   ├── Panama
│   │           │       │   ├── Pangnirtung
│   │           │       │   ├── Paramaribo
│   │           │       │   ├── Phoenix
│   │           │       │   ├── Port-au-Prince
│   │           │       │   ├── Porto_Acre
│   │           │       │   ├── Port_of_Spain
│   │           │       │   ├── Porto_Velho
│   │           │       │   ├── Puerto_Rico
│   │           │       │   ├── Punta_Arenas
│   │           │       │   ├── Rainy_River
│   │           │       │   ├── Rankin_Inlet
│   │           │       │   ├── Recife
│   │           │       │   ├── Regina
│   │           │       │   ├── Resolute
│   │           │       │   ├── Rio_Branco
│   │           │       │   ├── Rosario
│   │           │       │   ├── Santa_Isabel
│   │           │       │   ├── Santarem
│   │           │       │   ├── Santiago
│   │           │       │   ├── Santo_Domingo
│   │           │       │   ├── Sao_Paulo
│   │           │       │   ├── Scoresbysund
│   │           │       │   ├── Shiprock
│   │           │       │   ├── Sitka
│   │           │       │   ├── St_Barthelemy
│   │           │       │   ├── St_Johns
│   │           │       │   ├── St_Kitts
│   │           │       │   ├── St_Lucia
│   │           │       │   ├── St_Thomas
│   │           │       │   ├── St_Vincent
│   │           │       │   ├── Swift_Current
│   │           │       │   ├── Tegucigalpa
│   │           │       │   ├── Thule
│   │           │       │   ├── Thunder_Bay
│   │           │       │   ├── Tijuana
│   │           │       │   ├── Toronto
│   │           │       │   ├── Tortola
│   │           │       │   ├── Vancouver
│   │           │       │   ├── Virgin
│   │           │       │   ├── Whitehorse
│   │           │       │   ├── Winnipeg
│   │           │       │   ├── Yakutat
│   │           │       │   └── Yellowknife
│   │           │       ├── Antarctica
│   │           │       │   ├── Casey
│   │           │       │   ├── Davis
│   │           │       │   ├── DumontDUrville
│   │           │       │   ├── Macquarie
│   │           │       │   ├── Mawson
│   │           │       │   ├── McMurdo
│   │           │       │   ├── Palmer
│   │           │       │   ├── Rothera
│   │           │       │   ├── South_Pole
│   │           │       │   ├── Syowa
│   │           │       │   ├── Troll
│   │           │       │   └── Vostok
│   │           │       ├── Arctic
│   │           │       │   └── Longyearbyen
│   │           │       ├── Asia
│   │           │       │   ├── Aden
│   │           │       │   ├── Almaty
│   │           │       │   ├── Amman
│   │           │       │   ├── Anadyr
│   │           │       │   ├── Aqtau
│   │           │       │   ├── Aqtobe
│   │           │       │   ├── Ashgabat
│   │           │       │   ├── Ashkhabad
│   │           │       │   ├── Atyrau
│   │           │       │   ├── Baghdad
│   │           │       │   ├── Bahrain
│   │           │       │   ├── Baku
│   │           │       │   ├── Bangkok
│   │           │       │   ├── Barnaul
│   │           │       │   ├── Beirut
│   │           │       │   ├── Bishkek
│   │           │       │   ├── Brunei
│   │           │       │   ├── Calcutta
│   │           │       │   ├── Chita
│   │           │       │   ├── Choibalsan
│   │           │       │   ├── Chongqing
│   │           │       │   ├── Chungking
│   │           │       │   ├── Colombo
│   │           │       │   ├── Dacca
│   │           │       │   ├── Damascus
│   │           │       │   ├── Dhaka
│   │           │       │   ├── Dili
│   │           │       │   ├── Dubai
│   │           │       │   ├── Dushanbe
│   │           │       │   ├── Famagusta
│   │           │       │   ├── Gaza
│   │           │       │   ├── Harbin
│   │           │       │   ├── Hebron
│   │           │       │   ├── Ho_Chi_Minh
│   │           │       │   ├── Hong_Kong
│   │           │       │   ├── Hovd
│   │           │       │   ├── Irkutsk
│   │           │       │   ├── Istanbul
│   │           │       │   ├── Jakarta
│   │           │       │   ├── Jayapura
│   │           │       │   ├── Jerusalem
│   │           │       │   ├── Kabul
│   │           │       │   ├── Kamchatka
│   │           │       │   ├── Karachi
│   │           │       │   ├── Kashgar
│   │           │       │   ├── Kathmandu
│   │           │       │   ├── Katmandu
│   │           │       │   ├── Khandyga
│   │           │       │   ├── Kolkata
│   │           │       │   ├── Krasnoyarsk
│   │           │       │   ├── Kuala_Lumpur
│   │           │       │   ├── Kuching
│   │           │       │   ├── Kuwait
│   │           │       │   ├── Macao
│   │           │       │   ├── Macau
│   │           │       │   ├── Magadan
│   │           │       │   ├── Makassar
│   │           │       │   ├── Manila
│   │           │       │   ├── Muscat
│   │           │       │   ├── Nicosia
│   │           │       │   ├── Novokuznetsk
│   │           │       │   ├── Novosibirsk
│   │           │       │   ├── Omsk
│   │           │       │   ├── Oral
│   │           │       │   ├── Phnom_Penh
│   │           │       │   ├── Pontianak
│   │           │       │   ├── Pyongyang
│   │           │       │   ├── Qatar
│   │           │       │   ├── Qostanay
│   │           │       │   ├── Qyzylorda
│   │           │       │   ├── Rangoon
│   │           │       │   ├── Riyadh
│   │           │       │   ├── Saigon
│   │           │       │   ├── Sakhalin
│   │           │       │   ├── Samarkand
│   │           │       │   ├── Seoul
│   │           │       │   ├── Shanghai
│   │           │       │   ├── Singapore
│   │           │       │   ├── Srednekolymsk
│   │           │       │   ├── Taipei
│   │           │       │   ├── Tashkent
│   │           │       │   ├── Tbilisi
│   │           │       │   ├── Tehran
│   │           │       │   ├── Tel_Aviv
│   │           │       │   ├── Thimbu
│   │           │       │   ├── Thimphu
│   │           │       │   ├── Tokyo
│   │           │       │   ├── Tomsk
│   │           │       │   ├── Ujung_Pandang
│   │           │       │   ├── Ulaanbaatar
│   │           │       │   ├── Ulan_Bator
│   │           │       │   ├── Urumqi
│   │           │       │   ├── Ust-Nera
│   │           │       │   ├── Vientiane
│   │           │       │   ├── Vladivostok
│   │           │       │   ├── Yakutsk
│   │           │       │   ├── Yangon
│   │           │       │   ├── Yekaterinburg
│   │           │       │   └── Yerevan
│   │           │       ├── Atlantic
│   │           │       │   ├── Azores
│   │           │       │   ├── Bermuda
│   │           │       │   ├── Canary
│   │           │       │   ├── Cape_Verde
│   │           │       │   ├── Faeroe
│   │           │       │   ├── Faroe
│   │           │       │   ├── Jan_Mayen
│   │           │       │   ├── Madeira
│   │           │       │   ├── Reykjavik
│   │           │       │   ├── South_Georgia
│   │           │       │   ├── Stanley
│   │           │       │   └── St_Helena
│   │           │       ├── Australia
│   │           │       │   ├── ACT
│   │           │       │   ├── Adelaide
│   │           │       │   ├── Brisbane
│   │           │       │   ├── Broken_Hill
│   │           │       │   ├── Canberra
│   │           │       │   ├── Currie
│   │           │       │   ├── Darwin
│   │           │       │   ├── Eucla
│   │           │       │   ├── Hobart
│   │           │       │   ├── LHI
│   │           │       │   ├── Lindeman
│   │           │       │   ├── Lord_Howe
│   │           │       │   ├── Melbourne
│   │           │       │   ├── North
│   │           │       │   ├── NSW
│   │           │       │   ├── Perth
│   │           │       │   ├── Queensland
│   │           │       │   ├── South
│   │           │       │   ├── Sydney
│   │           │       │   ├── Tasmania
│   │           │       │   ├── Victoria
│   │           │       │   ├── West
│   │           │       │   └── Yancowinna
│   │           │       ├── Brazil
│   │           │       │   ├── Acre
│   │           │       │   ├── DeNoronha
│   │           │       │   ├── East
│   │           │       │   └── West
│   │           │       ├── Canada
│   │           │       │   ├── Atlantic
│   │           │       │   ├── Central
│   │           │       │   ├── Eastern
│   │           │       │   ├── Mountain
│   │           │       │   ├── Newfoundland
│   │           │       │   ├── Pacific
│   │           │       │   ├── Saskatchewan
│   │           │       │   └── Yukon
│   │           │       ├── CET
│   │           │       ├── Chile
│   │           │       │   ├── Continental
│   │           │       │   └── EasterIsland
│   │           │       ├── CST6CDT
│   │           │       ├── Cuba
│   │           │       ├── EET
│   │           │       ├── Egypt
│   │           │       ├── Eire
│   │           │       ├── EST
│   │           │       ├── EST5EDT
│   │           │       ├── Etc
│   │           │       │   ├── GMT
│   │           │       │   ├── GMT0
│   │           │       │   ├── GMT-0
│   │           │       │   ├── GMT+0
│   │           │       │   ├── GMT-1
│   │           │       │   ├── GMT+1
│   │           │       │   ├── GMT-10
│   │           │       │   ├── GMT+10
│   │           │       │   ├── GMT-11
│   │           │       │   ├── GMT+11
│   │           │       │   ├── GMT-12
│   │           │       │   ├── GMT+12
│   │           │       │   ├── GMT-13
│   │           │       │   ├── GMT-14
│   │           │       │   ├── GMT-2
│   │           │       │   ├── GMT+2
│   │           │       │   ├── GMT-3
│   │           │       │   ├── GMT+3
│   │           │       │   ├── GMT-4
│   │           │       │   ├── GMT+4
│   │           │       │   ├── GMT-5
│   │           │       │   ├── GMT+5
│   │           │       │   ├── GMT-6
│   │           │       │   ├── GMT+6
│   │           │       │   ├── GMT-7
│   │           │       │   ├── GMT+7
│   │           │       │   ├── GMT-8
│   │           │       │   ├── GMT+8
│   │           │       │   ├── GMT-9
│   │           │       │   ├── GMT+9
│   │           │       │   ├── Greenwich
│   │           │       │   ├── UCT
│   │           │       │   ├── Universal
│   │           │       │   ├── UTC
│   │           │       │   └── Zulu
│   │           │       ├── Europe
│   │           │       │   ├── Amsterdam
│   │           │       │   ├── Andorra
│   │           │       │   ├── Astrakhan
│   │           │       │   ├── Athens
│   │           │       │   ├── Belfast
│   │           │       │   ├── Belgrade
│   │           │       │   ├── Berlin
│   │           │       │   ├── Bratislava
│   │           │       │   ├── Brussels
│   │           │       │   ├── Bucharest
│   │           │       │   ├── Budapest
│   │           │       │   ├── Busingen
│   │           │       │   ├── Chisinau
│   │           │       │   ├── Copenhagen
│   │           │       │   ├── Dublin
│   │           │       │   ├── Gibraltar
│   │           │       │   ├── Guernsey
│   │           │       │   ├── Helsinki
│   │           │       │   ├── Isle_of_Man
│   │           │       │   ├── Istanbul
│   │           │       │   ├── Jersey
│   │           │       │   ├── Kaliningrad
│   │           │       │   ├── Kiev
│   │           │       │   ├── Kirov
│   │           │       │   ├── Lisbon
│   │           │       │   ├── Ljubljana
│   │           │       │   ├── London
│   │           │       │   ├── Luxembourg
│   │           │       │   ├── Madrid
│   │           │       │   ├── Malta
│   │           │       │   ├── Mariehamn
│   │           │       │   ├── Minsk
│   │           │       │   ├── Monaco
│   │           │       │   ├── Moscow
│   │           │       │   ├── Nicosia
│   │           │       │   ├── Oslo
│   │           │       │   ├── Paris
│   │           │       │   ├── Podgorica
│   │           │       │   ├── Prague
│   │           │       │   ├── Riga
│   │           │       │   ├── Rome
│   │           │       │   ├── Samara
│   │           │       │   ├── San_Marino
│   │           │       │   ├── Sarajevo
│   │           │       │   ├── Saratov
│   │           │       │   ├── Simferopol
│   │           │       │   ├── Skopje
│   │           │       │   ├── Sofia
│   │           │       │   ├── Stockholm
│   │           │       │   ├── Tallinn
│   │           │       │   ├── Tirane
│   │           │       │   ├── Tiraspol
│   │           │       │   ├── Ulyanovsk
│   │           │       │   ├── Uzhgorod
│   │           │       │   ├── Vaduz
│   │           │       │   ├── Vatican
│   │           │       │   ├── Vienna
│   │           │       │   ├── Vilnius
│   │           │       │   ├── Volgograd
│   │           │       │   ├── Warsaw
│   │           │       │   ├── Zagreb
│   │           │       │   ├── Zaporozhye
│   │           │       │   └── Zurich
│   │           │       ├── Factory
│   │           │       ├── GB
│   │           │       ├── GB-Eire
│   │           │       ├── GMT
│   │           │       ├── GMT0
│   │           │       ├── GMT-0
│   │           │       ├── GMT+0
│   │           │       ├── Greenwich
│   │           │       ├── Hongkong
│   │           │       ├── HST
│   │           │       ├── Iceland
│   │           │       ├── Indian
│   │           │       │   ├── Antananarivo
│   │           │       │   ├── Chagos
│   │           │       │   ├── Christmas
│   │           │       │   ├── Cocos
│   │           │       │   ├── Comoro
│   │           │       │   ├── Kerguelen
│   │           │       │   ├── Mahe
│   │           │       │   ├── Maldives
│   │           │       │   ├── Mauritius
│   │           │       │   ├── Mayotte
│   │           │       │   └── Reunion
│   │           │       ├── Iran
│   │           │       ├── iso3166.tab
│   │           │       ├── Israel
│   │           │       ├── Jamaica
│   │           │       ├── Japan
│   │           │       ├── Kwajalein
│   │           │       ├── leapseconds
│   │           │       ├── Libya
│   │           │       ├── MET
│   │           │       ├── Mexico
│   │           │       │   ├── BajaNorte
│   │           │       │   ├── BajaSur
│   │           │       │   └── General
│   │           │       ├── MST
│   │           │       ├── MST7MDT
│   │           │       ├── Navajo
│   │           │       ├── NZ
│   │           │       ├── NZ-CHAT
│   │           │       ├── Pacific
│   │           │       │   ├── Apia
│   │           │       │   ├── Auckland
│   │           │       │   ├── Bougainville
│   │           │       │   ├── Chatham
│   │           │       │   ├── Chuuk
│   │           │       │   ├── Easter
│   │           │       │   ├── Efate
│   │           │       │   ├── Enderbury
│   │           │       │   ├── Fakaofo
│   │           │       │   ├── Fiji
│   │           │       │   ├── Funafuti
│   │           │       │   ├── Galapagos
│   │           │       │   ├── Gambier
│   │           │       │   ├── Guadalcanal
│   │           │       │   ├── Guam
│   │           │       │   ├── Honolulu
│   │           │       │   ├── Johnston
│   │           │       │   ├── Kiritimati
│   │           │       │   ├── Kosrae
│   │           │       │   ├── Kwajalein
│   │           │       │   ├── Majuro
│   │           │       │   ├── Marquesas
│   │           │       │   ├── Midway
│   │           │       │   ├── Nauru
│   │           │       │   ├── Niue
│   │           │       │   ├── Norfolk
│   │           │       │   ├── Noumea
│   │           │       │   ├── Pago_Pago
│   │           │       │   ├── Palau
│   │           │       │   ├── Pitcairn
│   │           │       │   ├── Pohnpei
│   │           │       │   ├── Ponape
│   │           │       │   ├── Port_Moresby
│   │           │       │   ├── Rarotonga
│   │           │       │   ├── Saipan
│   │           │       │   ├── Samoa
│   │           │       │   ├── Tahiti
│   │           │       │   ├── Tarawa
│   │           │       │   ├── Tongatapu
│   │           │       │   ├── Truk
│   │           │       │   ├── Wake
│   │           │       │   ├── Wallis
│   │           │       │   └── Yap
│   │           │       ├── Poland
│   │           │       ├── Portugal
│   │           │       ├── posixrules
│   │           │       ├── PRC
│   │           │       ├── PST8PDT
│   │           │       ├── ROC
│   │           │       ├── ROK
│   │           │       ├── Singapore
│   │           │       ├── Turkey
│   │           │       ├── tzdata.zi
│   │           │       ├── UCT
│   │           │       ├── Universal
│   │           │       ├── US
│   │           │       │   ├── Alaska
│   │           │       │   ├── Aleutian
│   │           │       │   ├── Arizona
│   │           │       │   ├── Central
│   │           │       │   ├── Eastern
│   │           │       │   ├── East-Indiana
│   │           │       │   ├── Hawaii
│   │           │       │   ├── Indiana-Starke
│   │           │       │   ├── Michigan
│   │           │       │   ├── Mountain
│   │           │       │   ├── Pacific
│   │           │       │   └── Samoa
│   │           │       ├── UTC
│   │           │       ├── WET
│   │           │       ├── W-SU
│   │           │       ├── zone1970.tab
│   │           │       ├── zone.tab
│   │           │       └── Zulu
│   │           ├── pytz-2019.1.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   ├── WHEEL
│   │           │   └── zip-safe
│   │           ├── pyzmq-18.0.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── qtconsole
│   │           │   ├── ansi_code_processor.py
│   │           │   ├── base_frontend_mixin.py
│   │           │   ├── bracket_matcher.py
│   │           │   ├── call_tip_widget.py
│   │           │   ├── client.py
│   │           │   ├── completion_html.py
│   │           │   ├── completion_plain.py
│   │           │   ├── completion_widget.py
│   │           │   ├── console_widget.py
│   │           │   ├── frontend_widget.py
│   │           │   ├── history_console_widget.py
│   │           │   ├── __init__.py
│   │           │   ├── inprocess.py
│   │           │   ├── ipython_widget.py
│   │           │   ├── jupyter_widget.py
│   │           │   ├── kernel_mixins.py
│   │           │   ├── kill_ring.py
│   │           │   ├── __main__.py
│   │           │   ├── mainwindow.py
│   │           │   ├── manager.py
│   │           │   ├── __pycache__
│   │           │   │   ├── ansi_code_processor.cpython-36.pyc
│   │           │   │   ├── base_frontend_mixin.cpython-36.pyc
│   │           │   │   ├── bracket_matcher.cpython-36.pyc
│   │           │   │   ├── call_tip_widget.cpython-36.pyc
│   │           │   │   ├── client.cpython-36.pyc
│   │           │   │   ├── completion_html.cpython-36.pyc
│   │           │   │   ├── completion_plain.cpython-36.pyc
│   │           │   │   ├── completion_widget.cpython-36.pyc
│   │           │   │   ├── console_widget.cpython-36.pyc
│   │           │   │   ├── frontend_widget.cpython-36.pyc
│   │           │   │   ├── history_console_widget.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── inprocess.cpython-36.pyc
│   │           │   │   ├── ipython_widget.cpython-36.pyc
│   │           │   │   ├── jupyter_widget.cpython-36.pyc
│   │           │   │   ├── kernel_mixins.cpython-36.pyc
│   │           │   │   ├── kill_ring.cpython-36.pyc
│   │           │   │   ├── __main__.cpython-36.pyc
│   │           │   │   ├── mainwindow.cpython-36.pyc
│   │           │   │   ├── manager.cpython-36.pyc
│   │           │   │   ├── pygments_highlighter.cpython-36.pyc
│   │           │   │   ├── qtconsoleapp.cpython-36.pyc
│   │           │   │   ├── qt.cpython-36.pyc
│   │           │   │   ├── qt_loaders.cpython-36.pyc
│   │           │   │   ├── rich_ipython_widget.cpython-36.pyc
│   │           │   │   ├── rich_jupyter_widget.cpython-36.pyc
│   │           │   │   ├── rich_text.cpython-36.pyc
│   │           │   │   ├── styles.cpython-36.pyc
│   │           │   │   ├── svg.cpython-36.pyc
│   │           │   │   ├── usage.cpython-36.pyc
│   │           │   │   ├── util.cpython-36.pyc
│   │           │   │   └── _version.cpython-36.pyc
│   │           │   ├── pygments_highlighter.py
│   │           │   ├── qtconsoleapp.py
│   │           │   ├── qt_loaders.py
│   │           │   ├── qt.py
│   │           │   ├── resources
│   │           │   │   └── icon
│   │           │   │       └── JupyterConsole.svg
│   │           │   ├── rich_ipython_widget.py
│   │           │   ├── rich_jupyter_widget.py
│   │           │   ├── rich_text.py
│   │           │   ├── styles.py
│   │           │   ├── svg.py
│   │           │   ├── tests
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── test_ansi_code_processor.cpython-36.pyc
│   │           │   │   │   ├── test_app.cpython-36.pyc
│   │           │   │   │   ├── test_completion_widget.cpython-36.pyc
│   │           │   │   │   ├── test_console_widget.cpython-36.pyc
│   │           │   │   │   ├── test_frontend_widget.cpython-36.pyc
│   │           │   │   │   ├── test_jupyter_widget.cpython-36.pyc
│   │           │   │   │   ├── test_kill_ring.cpython-36.pyc
│   │           │   │   │   └── test_styles.cpython-36.pyc
│   │           │   │   ├── test_ansi_code_processor.py
│   │           │   │   ├── test_app.py
│   │           │   │   ├── test_completion_widget.py
│   │           │   │   ├── test_console_widget.py
│   │           │   │   ├── test_frontend_widget.py
│   │           │   │   ├── test_jupyter_widget.py
│   │           │   │   ├── test_kill_ring.py
│   │           │   │   └── test_styles.py
│   │           │   ├── usage.py
│   │           │   ├── util.py
│   │           │   └── _version.py
│   │           ├── qtconsole-4.4.4.dist-info
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── scipy
│   │           │   ├── _build_utils
│   │           │   │   ├── _fortran.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _fortran.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── system_info.cpython-36.pyc
│   │           │   │   └── system_info.py
│   │           │   ├── cluster
│   │           │   │   ├── _hierarchy.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── hierarchy.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _optimal_leaf_ordering.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── hierarchy.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   └── vq.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── hierarchy_test_data.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── hierarchy_test_data.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_hierarchy.cpython-36.pyc
│   │           │   │   │   │   └── test_vq.cpython-36.pyc
│   │           │   │   │   ├── test_hierarchy.py
│   │           │   │   │   └── test_vq.py
│   │           │   │   ├── _vq.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   └── vq.py
│   │           │   ├── __config__.py
│   │           │   ├── conftest.py
│   │           │   ├── constants
│   │           │   │   ├── codata.py
│   │           │   │   ├── constants.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── codata.cpython-36.pyc
│   │           │   │   │   ├── constants.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── setup.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_codata.cpython-36.pyc
│   │           │   │       │   └── test_constants.cpython-36.pyc
│   │           │   │       ├── test_codata.py
│   │           │   │       └── test_constants.py
│   │           │   ├── _distributor_init.py
│   │           │   ├── fftpack
│   │           │   │   ├── basic.py
│   │           │   │   ├── convolve.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _fftpack.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── helper.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── pseudo_diffs.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── basic.cpython-36.pyc
│   │           │   │   │   ├── helper.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── pseudo_diffs.cpython-36.pyc
│   │           │   │   │   ├── realtransforms.cpython-36.pyc
│   │           │   │   │   └── setup.cpython-36.pyc
│   │           │   │   ├── realtransforms.py
│   │           │   │   ├── setup.py
│   │           │   │   └── tests
│   │           │   │       ├── fftw_dct.c
│   │           │   │       ├── fftw_double_ref.npz
│   │           │   │       ├── fftw_single_ref.npz
│   │           │   │       ├── gendata.m
│   │           │   │       ├── gendata.py
│   │           │   │       ├── gen_fftw_ref.py
│   │           │   │       ├── __init__.py
│   │           │   │       ├── Makefile
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── gendata.cpython-36.pyc
│   │           │   │       │   ├── gen_fftw_ref.cpython-36.pyc
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_basic.cpython-36.pyc
│   │           │   │       │   ├── test_helper.cpython-36.pyc
│   │           │   │       │   ├── test_import.cpython-36.pyc
│   │           │   │       │   ├── test_pseudo_diffs.cpython-36.pyc
│   │           │   │       │   └── test_real_transforms.cpython-36.pyc
│   │           │   │       ├── test_basic.py
│   │           │   │       ├── test_helper.py
│   │           │   │       ├── test_import.py
│   │           │   │       ├── test.npz
│   │           │   │       ├── test_pseudo_diffs.py
│   │           │   │       └── test_real_transforms.py
│   │           │   ├── HACKING.rst.txt
│   │           │   ├── __init__.py
│   │           │   ├── INSTALL.rst.txt
│   │           │   ├── integrate
│   │           │   │   ├── _bvp.py
│   │           │   │   ├── _dop.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _ivp
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── bdf.py
│   │           │   │   │   ├── common.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── ivp.py
│   │           │   │   │   ├── lsoda.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   │   ├── bdf.cpython-36.pyc
│   │           │   │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── ivp.cpython-36.pyc
│   │           │   │   │   │   ├── lsoda.cpython-36.pyc
│   │           │   │   │   │   ├── radau.cpython-36.pyc
│   │           │   │   │   │   └── rk.cpython-36.pyc
│   │           │   │   │   ├── radau.py
│   │           │   │   │   └── rk.py
│   │           │   │   ├── lsoda.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _odepack.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── odepack.py
│   │           │   │   ├── _ode.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _bvp.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── _ode.cpython-36.pyc
│   │           │   │   │   ├── odepack.cpython-36.pyc
│   │           │   │   │   ├── quadpack.cpython-36.pyc
│   │           │   │   │   ├── quadrature.cpython-36.pyc
│   │           │   │   │   └── setup.cpython-36.pyc
│   │           │   │   ├── _quadpack.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── quadpack.py
│   │           │   │   ├── quadrature.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _test_multivariate.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _test_odeint_banded.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── tests
│   │           │   │   │   ├── banded5x5.f
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_banded_ode_solvers.cpython-36.pyc
│   │           │   │   │   │   ├── test_bvp.cpython-36.pyc
│   │           │   │   │   │   ├── test_integrate.cpython-36.pyc
│   │           │   │   │   │   ├── test_ivp.cpython-36.pyc
│   │           │   │   │   │   ├── test_odeint_jac.cpython-36.pyc
│   │           │   │   │   │   ├── test_quadpack.cpython-36.pyc
│   │           │   │   │   │   └── test_quadrature.cpython-36.pyc
│   │           │   │   │   ├── test_banded_ode_solvers.py
│   │           │   │   │   ├── test_bvp.py
│   │           │   │   │   ├── test_integrate.py
│   │           │   │   │   ├── test_ivp.py
│   │           │   │   │   ├── _test_multivariate.c
│   │           │   │   │   ├── test_odeint_jac.py
│   │           │   │   │   ├── test_quadpack.py
│   │           │   │   │   └── test_quadrature.py
│   │           │   │   └── vode.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── interpolate
│   │           │   │   ├── _bspl.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _bsplines.py
│   │           │   │   ├── _cubic.py
│   │           │   │   ├── dfitpack.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── fitpack2.py
│   │           │   │   ├── _fitpack.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _fitpack_impl.py
│   │           │   │   ├── fitpack.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── interpnd.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── interpnd_info.py
│   │           │   │   ├── _interpolate.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── interpolate.py
│   │           │   │   ├── interpolate_wrapper.py
│   │           │   │   ├── ndgriddata.py
│   │           │   │   ├── _pade.py
│   │           │   │   ├── polyint.py
│   │           │   │   ├── _ppoly.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _bsplines.cpython-36.pyc
│   │           │   │   │   ├── _cubic.cpython-36.pyc
│   │           │   │   │   ├── fitpack2.cpython-36.pyc
│   │           │   │   │   ├── fitpack.cpython-36.pyc
│   │           │   │   │   ├── _fitpack_impl.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── interpnd_info.cpython-36.pyc
│   │           │   │   │   ├── interpolate.cpython-36.pyc
│   │           │   │   │   ├── interpolate_wrapper.cpython-36.pyc
│   │           │   │   │   ├── ndgriddata.cpython-36.pyc
│   │           │   │   │   ├── _pade.cpython-36.pyc
│   │           │   │   │   ├── polyint.cpython-36.pyc
│   │           │   │   │   ├── rbf.cpython-36.pyc
│   │           │   │   │   └── setup.cpython-36.pyc
│   │           │   │   ├── rbf.py
│   │           │   │   ├── setup.py
│   │           │   │   └── tests
│   │           │   │       ├── data
│   │           │   │       │   ├── bug-1310.npz
│   │           │   │       │   └── estimate_gradients_hang.npy
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_bsplines.cpython-36.pyc
│   │           │   │       │   ├── test_fitpack2.cpython-36.pyc
│   │           │   │       │   ├── test_fitpack.cpython-36.pyc
│   │           │   │       │   ├── test_gil.cpython-36.pyc
│   │           │   │       │   ├── test_interpnd.cpython-36.pyc
│   │           │   │       │   ├── test_interpolate.cpython-36.pyc
│   │           │   │       │   ├── test_interpolate_wrapper.cpython-36.pyc
│   │           │   │       │   ├── test_ndgriddata.cpython-36.pyc
│   │           │   │       │   ├── test_pade.cpython-36.pyc
│   │           │   │       │   ├── test_polyint.cpython-36.pyc
│   │           │   │       │   ├── test_rbf.cpython-36.pyc
│   │           │   │       │   └── test_regression.cpython-36.pyc
│   │           │   │       ├── test_bsplines.py
│   │           │   │       ├── test_fitpack2.py
│   │           │   │       ├── test_fitpack.py
│   │           │   │       ├── test_gil.py
│   │           │   │       ├── test_interpnd.py
│   │           │   │       ├── test_interpolate.py
│   │           │   │       ├── test_interpolate_wrapper.py
│   │           │   │       ├── test_ndgriddata.py
│   │           │   │       ├── test_pade.py
│   │           │   │       ├── test_polyint.py
│   │           │   │       ├── test_rbf.py
│   │           │   │       └── test_regression.py
│   │           │   ├── io
│   │           │   │   ├── arff
│   │           │   │   │   ├── arffread.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── arffread.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── setup.cpython-36.pyc
│   │           │   │   │   ├── setup.py
│   │           │   │   │   └── tests
│   │           │   │   │       ├── data
│   │           │   │   │       │   ├── iris.arff
│   │           │   │   │       │   ├── missing.arff
│   │           │   │   │       │   ├── nodata.arff
│   │           │   │   │       │   ├── test1.arff
│   │           │   │   │       │   ├── test2.arff
│   │           │   │   │       │   ├── test3.arff
│   │           │   │   │       │   ├── test4.arff
│   │           │   │   │       │   ├── test5.arff
│   │           │   │   │       │   ├── test6.arff
│   │           │   │   │       │   ├── test7.arff
│   │           │   │   │       │   └── test8.arff
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   └── test_arffread.cpython-36.pyc
│   │           │   │   │       └── test_arffread.py
│   │           │   │   ├── _fortran.py
│   │           │   │   ├── harwell_boeing
│   │           │   │   │   ├── _fortran_format_parser.py
│   │           │   │   │   ├── hb.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── _fortran_format_parser.cpython-36.pyc
│   │           │   │   │   │   ├── hb.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── setup.cpython-36.pyc
│   │           │   │   │   ├── setup.py
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_fortran_format.cpython-36.pyc
│   │           │   │   │       │   └── test_hb.cpython-36.pyc
│   │           │   │   │       ├── test_fortran_format.py
│   │           │   │   │       └── test_hb.py
│   │           │   │   ├── idl.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── matlab
│   │           │   │   │   ├── byteordercodes.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── mio4.py
│   │           │   │   │   ├── mio5_params.py
│   │           │   │   │   ├── mio5.py
│   │           │   │   │   ├── mio5_utils.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── miobase.py
│   │           │   │   │   ├── mio.py
│   │           │   │   │   ├── mio_utils.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── byteordercodes.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── mio4.cpython-36.pyc
│   │           │   │   │   │   ├── mio5.cpython-36.pyc
│   │           │   │   │   │   ├── mio5_params.cpython-36.pyc
│   │           │   │   │   │   ├── miobase.cpython-36.pyc
│   │           │   │   │   │   ├── mio.cpython-36.pyc
│   │           │   │   │   │   └── setup.cpython-36.pyc
│   │           │   │   │   ├── setup.py
│   │           │   │   │   ├── streams.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   └── tests
│   │           │   │   │       ├── afunc.m
│   │           │   │   │       ├── data
│   │           │   │   │       │   ├── bad_miuint32.mat
│   │           │   │   │       │   ├── bad_miutf8_array_name.mat
│   │           │   │   │       │   ├── big_endian.mat
│   │           │   │   │       │   ├── broken_utf8.mat
│   │           │   │   │       │   ├── corrupted_zlib_checksum.mat
│   │           │   │   │       │   ├── corrupted_zlib_data.mat
│   │           │   │   │       │   ├── japanese_utf8.txt
│   │           │   │   │       │   ├── little_endian.mat
│   │           │   │   │       │   ├── logical_sparse.mat
│   │           │   │   │       │   ├── malformed1.mat
│   │           │   │   │       │   ├── miuint32_for_miint32.mat
│   │           │   │   │       │   ├── miutf8_array_name.mat
│   │           │   │   │       │   ├── nasty_duplicate_fieldnames.mat
│   │           │   │   │       │   ├── one_by_zero_char.mat
│   │           │   │   │       │   ├── parabola.mat
│   │           │   │   │       │   ├── single_empty_string.mat
│   │           │   │   │       │   ├── some_functions.mat
│   │           │   │   │       │   ├── sqr.mat
│   │           │   │   │       │   ├── test3dmatrix_6.1_SOL2.mat
│   │           │   │   │       │   ├── test3dmatrix_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── test3dmatrix_7.1_GLNX86.mat
│   │           │   │   │       │   ├── test3dmatrix_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testbool_8_WIN64.mat
│   │           │   │   │       │   ├── testcell_6.1_SOL2.mat
│   │           │   │   │       │   ├── testcell_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── testcell_7.1_GLNX86.mat
│   │           │   │   │       │   ├── testcell_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testcellnest_6.1_SOL2.mat
│   │           │   │   │       │   ├── testcellnest_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── testcellnest_7.1_GLNX86.mat
│   │           │   │   │       │   ├── testcellnest_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testcomplex_4.2c_SOL2.mat
│   │           │   │   │       │   ├── testcomplex_6.1_SOL2.mat
│   │           │   │   │       │   ├── testcomplex_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── testcomplex_7.1_GLNX86.mat
│   │           │   │   │       │   ├── testcomplex_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testdouble_4.2c_SOL2.mat
│   │           │   │   │       │   ├── testdouble_6.1_SOL2.mat
│   │           │   │   │       │   ├── testdouble_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── testdouble_7.1_GLNX86.mat
│   │           │   │   │       │   ├── testdouble_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testemptycell_5.3_SOL2.mat
│   │           │   │   │       │   ├── testemptycell_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── testemptycell_7.1_GLNX86.mat
│   │           │   │   │       │   ├── testemptycell_7.4_GLNX86.mat
│   │           │   │   │       │   ├── test_empty_struct.mat
│   │           │   │   │       │   ├── testfunc_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testhdf5_7.4_GLNX86.mat
│   │           │   │   │       │   ├── test_mat4_le_floats.mat
│   │           │   │   │       │   ├── testmatrix_4.2c_SOL2.mat
│   │           │   │   │       │   ├── testmatrix_6.1_SOL2.mat
│   │           │   │   │       │   ├── testmatrix_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── testmatrix_7.1_GLNX86.mat
│   │           │   │   │       │   ├── testmatrix_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testminus_4.2c_SOL2.mat
│   │           │   │   │       │   ├── testminus_6.1_SOL2.mat
│   │           │   │   │       │   ├── testminus_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── testminus_7.1_GLNX86.mat
│   │           │   │   │       │   ├── testminus_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testmulti_4.2c_SOL2.mat
│   │           │   │   │       │   ├── testmulti_7.1_GLNX86.mat
│   │           │   │   │       │   ├── testmulti_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testobject_6.1_SOL2.mat
│   │           │   │   │       │   ├── testobject_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── testobject_7.1_GLNX86.mat
│   │           │   │   │       │   ├── testobject_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testonechar_4.2c_SOL2.mat
│   │           │   │   │       │   ├── testonechar_6.1_SOL2.mat
│   │           │   │   │       │   ├── testonechar_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── testonechar_7.1_GLNX86.mat
│   │           │   │   │       │   ├── testonechar_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testscalarcell_7.4_GLNX86.mat
│   │           │   │   │       │   ├── test_skip_variable.mat
│   │           │   │   │       │   ├── testsparse_4.2c_SOL2.mat
│   │           │   │   │       │   ├── testsparse_6.1_SOL2.mat
│   │           │   │   │       │   ├── testsparse_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── testsparse_7.1_GLNX86.mat
│   │           │   │   │       │   ├── testsparse_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testsparsecomplex_4.2c_SOL2.mat
│   │           │   │   │       │   ├── testsparsecomplex_6.1_SOL2.mat
│   │           │   │   │       │   ├── testsparsecomplex_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── testsparsecomplex_7.1_GLNX86.mat
│   │           │   │   │       │   ├── testsparsecomplex_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testsparsefloat_7.4_GLNX86.mat
│   │           │   │   │       │   ├── teststring_4.2c_SOL2.mat
│   │           │   │   │       │   ├── teststring_6.1_SOL2.mat
│   │           │   │   │       │   ├── teststring_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── teststring_7.1_GLNX86.mat
│   │           │   │   │       │   ├── teststring_7.4_GLNX86.mat
│   │           │   │   │       │   ├── teststringarray_4.2c_SOL2.mat
│   │           │   │   │       │   ├── teststringarray_6.1_SOL2.mat
│   │           │   │   │       │   ├── teststringarray_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── teststringarray_7.1_GLNX86.mat
│   │           │   │   │       │   ├── teststringarray_7.4_GLNX86.mat
│   │           │   │   │       │   ├── teststruct_6.1_SOL2.mat
│   │           │   │   │       │   ├── teststruct_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── teststruct_7.1_GLNX86.mat
│   │           │   │   │       │   ├── teststruct_7.4_GLNX86.mat
│   │           │   │   │       │   ├── teststructarr_6.1_SOL2.mat
│   │           │   │   │       │   ├── teststructarr_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── teststructarr_7.1_GLNX86.mat
│   │           │   │   │       │   ├── teststructarr_7.4_GLNX86.mat
│   │           │   │   │       │   ├── teststructnest_6.1_SOL2.mat
│   │           │   │   │       │   ├── teststructnest_6.5.1_GLNX86.mat
│   │           │   │   │       │   ├── teststructnest_7.1_GLNX86.mat
│   │           │   │   │       │   ├── teststructnest_7.4_GLNX86.mat
│   │           │   │   │       │   ├── testunicode_7.1_GLNX86.mat
│   │           │   │   │       │   ├── testunicode_7.4_GLNX86.mat
│   │           │   │   │       │   └── testvec_4_GLNX86.mat
│   │           │   │   │       ├── gen_mat4files.m
│   │           │   │   │       ├── gen_mat5files.m
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_byteordercodes.cpython-36.pyc
│   │           │   │   │       │   ├── test_mio5_utils.cpython-36.pyc
│   │           │   │   │       │   ├── test_miobase.cpython-36.pyc
│   │           │   │   │       │   ├── test_mio.cpython-36.pyc
│   │           │   │   │       │   ├── test_mio_funcs.cpython-36.pyc
│   │           │   │   │       │   ├── test_mio_utils.cpython-36.pyc
│   │           │   │   │       │   ├── test_pathological.cpython-36.pyc
│   │           │   │   │       │   └── test_streams.cpython-36.pyc
│   │           │   │   │       ├── save_matfile.m
│   │           │   │   │       ├── test_byteordercodes.py
│   │           │   │   │       ├── test_mio5_utils.py
│   │           │   │   │       ├── test_miobase.py
│   │           │   │   │       ├── test_mio_funcs.py
│   │           │   │   │       ├── test_mio.py
│   │           │   │   │       ├── test_mio_utils.py
│   │           │   │   │       ├── test_pathological.py
│   │           │   │   │       └── test_streams.py
│   │           │   │   ├── mmio.py
│   │           │   │   ├── netcdf.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _fortran.cpython-36.pyc
│   │           │   │   │   ├── idl.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── mmio.cpython-36.pyc
│   │           │   │   │   ├── netcdf.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   └── wavfile.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   ├── _test_fortran.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── array_float32_1d.sav
│   │           │   │   │   │   ├── array_float32_2d.sav
│   │           │   │   │   │   ├── array_float32_3d.sav
│   │           │   │   │   │   ├── array_float32_4d.sav
│   │           │   │   │   │   ├── array_float32_5d.sav
│   │           │   │   │   │   ├── array_float32_6d.sav
│   │           │   │   │   │   ├── array_float32_7d.sav
│   │           │   │   │   │   ├── array_float32_8d.sav
│   │           │   │   │   │   ├── array_float32_pointer_1d.sav
│   │           │   │   │   │   ├── array_float32_pointer_2d.sav
│   │           │   │   │   │   ├── array_float32_pointer_3d.sav
│   │           │   │   │   │   ├── array_float32_pointer_4d.sav
│   │           │   │   │   │   ├── array_float32_pointer_5d.sav
│   │           │   │   │   │   ├── array_float32_pointer_6d.sav
│   │           │   │   │   │   ├── array_float32_pointer_7d.sav
│   │           │   │   │   │   ├── array_float32_pointer_8d.sav
│   │           │   │   │   │   ├── example_1.nc
│   │           │   │   │   │   ├── example_2.nc
│   │           │   │   │   │   ├── example_3_maskedvals.nc
│   │           │   │   │   │   ├── fortran-3x3d-2i.dat
│   │           │   │   │   │   ├── fortran-mixed.dat
│   │           │   │   │   │   ├── fortran-sf8-11x1x10.dat
│   │           │   │   │   │   ├── fortran-sf8-15x10x22.dat
│   │           │   │   │   │   ├── fortran-sf8-1x1x1.dat
│   │           │   │   │   │   ├── fortran-sf8-1x1x5.dat
│   │           │   │   │   │   ├── fortran-sf8-1x1x7.dat
│   │           │   │   │   │   ├── fortran-sf8-1x3x5.dat
│   │           │   │   │   │   ├── fortran-si4-11x1x10.dat
│   │           │   │   │   │   ├── fortran-si4-15x10x22.dat
│   │           │   │   │   │   ├── fortran-si4-1x1x1.dat
│   │           │   │   │   │   ├── fortran-si4-1x1x5.dat
│   │           │   │   │   │   ├── fortran-si4-1x1x7.dat
│   │           │   │   │   │   ├── fortran-si4-1x3x5.dat
│   │           │   │   │   │   ├── invalid_pointer.sav
│   │           │   │   │   │   ├── null_pointer.sav
│   │           │   │   │   │   ├── scalar_byte_descr.sav
│   │           │   │   │   │   ├── scalar_byte.sav
│   │           │   │   │   │   ├── scalar_complex32.sav
│   │           │   │   │   │   ├── scalar_complex64.sav
│   │           │   │   │   │   ├── scalar_float32.sav
│   │           │   │   │   │   ├── scalar_float64.sav
│   │           │   │   │   │   ├── scalar_heap_pointer.sav
│   │           │   │   │   │   ├── scalar_int16.sav
│   │           │   │   │   │   ├── scalar_int32.sav
│   │           │   │   │   │   ├── scalar_int64.sav
│   │           │   │   │   │   ├── scalar_string.sav
│   │           │   │   │   │   ├── scalar_uint16.sav
│   │           │   │   │   │   ├── scalar_uint32.sav
│   │           │   │   │   │   ├── scalar_uint64.sav
│   │           │   │   │   │   ├── struct_arrays_byte_idl80.sav
│   │           │   │   │   │   ├── struct_arrays_replicated_3d.sav
│   │           │   │   │   │   ├── struct_arrays_replicated.sav
│   │           │   │   │   │   ├── struct_arrays.sav
│   │           │   │   │   │   ├── struct_inherit.sav
│   │           │   │   │   │   ├── struct_pointer_arrays_replicated_3d.sav
│   │           │   │   │   │   ├── struct_pointer_arrays_replicated.sav
│   │           │   │   │   │   ├── struct_pointer_arrays.sav
│   │           │   │   │   │   ├── struct_pointers_replicated_3d.sav
│   │           │   │   │   │   ├── struct_pointers_replicated.sav
│   │           │   │   │   │   ├── struct_pointers.sav
│   │           │   │   │   │   ├── struct_scalars_replicated_3d.sav
│   │           │   │   │   │   ├── struct_scalars_replicated.sav
│   │           │   │   │   │   ├── struct_scalars.sav
│   │           │   │   │   │   ├── test-44100Hz-2ch-32bit-float-be.wav
│   │           │   │   │   │   ├── test-44100Hz-2ch-32bit-float-le.wav
│   │           │   │   │   │   ├── test-44100Hz-le-1ch-4bytes-early-eof.wav
│   │           │   │   │   │   ├── test-44100Hz-le-1ch-4bytes-incomplete-chunk.wav
│   │           │   │   │   │   ├── test-44100Hz-le-1ch-4bytes.wav
│   │           │   │   │   │   ├── test-48000Hz-2ch-64bit-float-le-wavex.wav
│   │           │   │   │   │   ├── test-8000Hz-le-2ch-1byteu.wav
│   │           │   │   │   │   └── various_compressed.sav
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_fortran.cpython-36.pyc
│   │           │   │   │   │   ├── test_idl.cpython-36.pyc
│   │           │   │   │   │   ├── test_mmio.cpython-36.pyc
│   │           │   │   │   │   ├── test_netcdf.cpython-36.pyc
│   │           │   │   │   │   ├── test_paths.cpython-36.pyc
│   │           │   │   │   │   └── test_wavfile.cpython-36.pyc
│   │           │   │   │   ├── test_fortran.py
│   │           │   │   │   ├── test_idl.py
│   │           │   │   │   ├── test_mmio.py
│   │           │   │   │   ├── test_netcdf.py
│   │           │   │   │   ├── test_paths.py
│   │           │   │   │   └── test_wavfile.py
│   │           │   │   └── wavfile.py
│   │           │   ├── _lib
│   │           │   │   ├── _ccallback_c.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _ccallback.py
│   │           │   │   ├── decorator.py
│   │           │   │   ├── _fpumode.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _gcutils.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── messagestream.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _numpy_compat.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _ccallback.cpython-36.pyc
│   │           │   │   │   ├── decorator.cpython-36.pyc
│   │           │   │   │   ├── _gcutils.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── _numpy_compat.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   ├── six.cpython-36.pyc
│   │           │   │   │   ├── _testutils.cpython-36.pyc
│   │           │   │   │   ├── _threadsafety.cpython-36.pyc
│   │           │   │   │   ├── _tmpdirs.cpython-36.pyc
│   │           │   │   │   ├── _util.cpython-36.pyc
│   │           │   │   │   └── _version.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   ├── six.py
│   │           │   │   ├── _test_ccallback.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_ccallback.cpython-36.pyc
│   │           │   │   │   │   ├── test__gcutils.cpython-36.pyc
│   │           │   │   │   │   ├── test_import_cycles.cpython-36.pyc
│   │           │   │   │   │   ├── test__testutils.cpython-36.pyc
│   │           │   │   │   │   ├── test__threadsafety.cpython-36.pyc
│   │           │   │   │   │   ├── test_tmpdirs.cpython-36.pyc
│   │           │   │   │   │   ├── test__util.cpython-36.pyc
│   │           │   │   │   │   ├── test__version.cpython-36.pyc
│   │           │   │   │   │   └── test_warnings.cpython-36.pyc
│   │           │   │   │   ├── test_ccallback.py
│   │           │   │   │   ├── test__gcutils.py
│   │           │   │   │   ├── test_import_cycles.py
│   │           │   │   │   ├── test__testutils.py
│   │           │   │   │   ├── test__threadsafety.py
│   │           │   │   │   ├── test_tmpdirs.py
│   │           │   │   │   ├── test__util.py
│   │           │   │   │   ├── test__version.py
│   │           │   │   │   └── test_warnings.py
│   │           │   │   ├── _testutils.py
│   │           │   │   ├── _threadsafety.py
│   │           │   │   ├── _tmpdirs.py
│   │           │   │   ├── _util.py
│   │           │   │   └── _version.py
│   │           │   ├── .libs
│   │           │   │   ├── libgfortran-ed201abd.so.3.0.0
│   │           │   │   └── libopenblasp-r0-382c8f3a.3.5.dev.so
│   │           │   ├── LICENSE.txt
│   │           │   ├── linalg
│   │           │   │   ├── basic.py
│   │           │   │   ├── blas.py
│   │           │   │   ├── cython_blas.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── cython_blas.pxd
│   │           │   │   ├── cython_lapack.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── cython_lapack.pxd
│   │           │   │   ├── _cython_signature_generator.py
│   │           │   │   ├── decomp_cholesky.py
│   │           │   │   ├── _decomp_ldl.py
│   │           │   │   ├── decomp_lu.py
│   │           │   │   ├── _decomp_polar.py
│   │           │   │   ├── decomp.py
│   │           │   │   ├── decomp_qr.py
│   │           │   │   ├── _decomp_qz.py
│   │           │   │   ├── decomp_schur.py
│   │           │   │   ├── decomp_svd.py
│   │           │   │   ├── _decomp_update.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _expm_frechet.py
│   │           │   │   ├── _fblas.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _flapack.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _flinalg.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── flinalg.py
│   │           │   │   ├── _generate_pyx.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _interpolative_backend.py
│   │           │   │   ├── _interpolative.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── interpolative.py
│   │           │   │   ├── lapack.py
│   │           │   │   ├── linalg_version.py
│   │           │   │   ├── _matfuncs_inv_ssq.py
│   │           │   │   ├── matfuncs.py
│   │           │   │   ├── _matfuncs_sqrtm.py
│   │           │   │   ├── misc.py
│   │           │   │   ├── _procrustes.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── basic.cpython-36.pyc
│   │           │   │   │   ├── blas.cpython-36.pyc
│   │           │   │   │   ├── _cython_signature_generator.cpython-36.pyc
│   │           │   │   │   ├── decomp_cholesky.cpython-36.pyc
│   │           │   │   │   ├── decomp.cpython-36.pyc
│   │           │   │   │   ├── _decomp_ldl.cpython-36.pyc
│   │           │   │   │   ├── decomp_lu.cpython-36.pyc
│   │           │   │   │   ├── _decomp_polar.cpython-36.pyc
│   │           │   │   │   ├── decomp_qr.cpython-36.pyc
│   │           │   │   │   ├── _decomp_qz.cpython-36.pyc
│   │           │   │   │   ├── decomp_schur.cpython-36.pyc
│   │           │   │   │   ├── decomp_svd.cpython-36.pyc
│   │           │   │   │   ├── _expm_frechet.cpython-36.pyc
│   │           │   │   │   ├── flinalg.cpython-36.pyc
│   │           │   │   │   ├── _generate_pyx.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── _interpolative_backend.cpython-36.pyc
│   │           │   │   │   ├── interpolative.cpython-36.pyc
│   │           │   │   │   ├── lapack.cpython-36.pyc
│   │           │   │   │   ├── linalg_version.cpython-36.pyc
│   │           │   │   │   ├── matfuncs.cpython-36.pyc
│   │           │   │   │   ├── _matfuncs_inv_ssq.cpython-36.pyc
│   │           │   │   │   ├── _matfuncs_sqrtm.cpython-36.pyc
│   │           │   │   │   ├── misc.cpython-36.pyc
│   │           │   │   │   ├── _procrustes.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   ├── _sketches.cpython-36.pyc
│   │           │   │   │   ├── _solvers.cpython-36.pyc
│   │           │   │   │   ├── special_matrices.cpython-36.pyc
│   │           │   │   │   └── _testutils.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   ├── _sketches.py
│   │           │   │   ├── _solvers.py
│   │           │   │   ├── _solve_toeplitz.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── special_matrices.py
│   │           │   │   ├── src
│   │           │   │   │   ├── id_dist
│   │           │   │   │   │   └── doc
│   │           │   │   │   │       └── doc.tex
│   │           │   │   │   └── lapack_deprecations
│   │           │   │   │       └── LICENSE
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── carex_15_data.npz
│   │           │   │   │   │   ├── carex_18_data.npz
│   │           │   │   │   │   ├── carex_19_data.npz
│   │           │   │   │   │   ├── carex_20_data.npz
│   │           │   │   │   │   ├── carex_6_data.npz
│   │           │   │   │   │   └── gendare_20170120_data.npz
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_basic.cpython-36.pyc
│   │           │   │   │   │   ├── test_blas.cpython-36.pyc
│   │           │   │   │   │   ├── test_build.cpython-36.pyc
│   │           │   │   │   │   ├── test_cython_blas.cpython-36.pyc
│   │           │   │   │   │   ├── test_cython_lapack.cpython-36.pyc
│   │           │   │   │   │   ├── test_decomp_cholesky.cpython-36.pyc
│   │           │   │   │   │   ├── test_decomp.cpython-36.pyc
│   │           │   │   │   │   ├── test_decomp_ldl.cpython-36.pyc
│   │           │   │   │   │   ├── test_decomp_polar.cpython-36.pyc
│   │           │   │   │   │   ├── test_decomp_update.cpython-36.pyc
│   │           │   │   │   │   ├── test_fblas.cpython-36.pyc
│   │           │   │   │   │   ├── test_interpolative.cpython-36.pyc
│   │           │   │   │   │   ├── test_lapack.cpython-36.pyc
│   │           │   │   │   │   ├── test_matfuncs.cpython-36.pyc
│   │           │   │   │   │   ├── test_procrustes.cpython-36.pyc
│   │           │   │   │   │   ├── test_sketches.cpython-36.pyc
│   │           │   │   │   │   ├── test_solvers.cpython-36.pyc
│   │           │   │   │   │   ├── test_solve_toeplitz.cpython-36.pyc
│   │           │   │   │   │   └── test_special_matrices.cpython-36.pyc
│   │           │   │   │   ├── test_basic.py
│   │           │   │   │   ├── test_blas.py
│   │           │   │   │   ├── test_build.py
│   │           │   │   │   ├── test_cython_blas.py
│   │           │   │   │   ├── test_cython_lapack.py
│   │           │   │   │   ├── test_decomp_cholesky.py
│   │           │   │   │   ├── test_decomp_ldl.py
│   │           │   │   │   ├── test_decomp_polar.py
│   │           │   │   │   ├── test_decomp.py
│   │           │   │   │   ├── test_decomp_update.py
│   │           │   │   │   ├── test_fblas.py
│   │           │   │   │   ├── test_interpolative.py
│   │           │   │   │   ├── test_lapack.py
│   │           │   │   │   ├── test_matfuncs.py
│   │           │   │   │   ├── test_procrustes.py
│   │           │   │   │   ├── test_sketches.py
│   │           │   │   │   ├── test_solvers.py
│   │           │   │   │   ├── test_solve_toeplitz.py
│   │           │   │   │   └── test_special_matrices.py
│   │           │   │   └── _testutils.py
│   │           │   ├── linalg.pxd
│   │           │   ├── misc
│   │           │   │   ├── ascent.dat
│   │           │   │   ├── common.py
│   │           │   │   ├── doccer.py
│   │           │   │   ├── ecg.dat
│   │           │   │   ├── face.dat
│   │           │   │   ├── __init__.py
│   │           │   │   ├── pilutil.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   ├── doccer.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── pilutil.cpython-36.pyc
│   │           │   │   │   └── setup.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   └── tests
│   │           │   │       ├── data
│   │           │   │       │   ├── 3x3x3.png
│   │           │   │       │   ├── 3x3x4.png
│   │           │   │       │   ├── 3x4x3.png
│   │           │   │       │   ├── 3x4x4.png
│   │           │   │       │   ├── 3x5x3.png
│   │           │   │       │   ├── 3x5x4.png
│   │           │   │       │   ├── 4x3x3.png
│   │           │   │       │   ├── 4x3x4.png
│   │           │   │       │   ├── 4x4x3.png
│   │           │   │       │   ├── 4x4x4.png
│   │           │   │       │   ├── 4x5x3.png
│   │           │   │       │   ├── 4x5x4.png
│   │           │   │       │   ├── 5x3x3.png
│   │           │   │       │   ├── 5x3x4.png
│   │           │   │       │   ├── 5x4x3.png
│   │           │   │       │   ├── 5x4x4.png
│   │           │   │       │   ├── 5x5x3.png
│   │           │   │       │   ├── 5x5x4.png
│   │           │   │       │   ├── blocks2bit.png
│   │           │   │       │   ├── box1.png
│   │           │   │       │   ├── foo3x5x4indexed.png
│   │           │   │       │   ├── icon_mono_flat.png
│   │           │   │       │   ├── icon_mono.png
│   │           │   │       │   ├── icon.png
│   │           │   │       │   └── pattern4bit.png
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_common.cpython-36.pyc
│   │           │   │       │   ├── test_doccer.cpython-36.pyc
│   │           │   │       │   └── test_pilutil.cpython-36.pyc
│   │           │   │       ├── test_common.py
│   │           │   │       ├── test_doccer.py
│   │           │   │       └── test_pilutil.py
│   │           │   ├── ndimage
│   │           │   │   ├── _ctest.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _ctest_oldapi.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _cytest.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── filters.py
│   │           │   │   ├── fourier.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── interpolation.py
│   │           │   │   ├── io.py
│   │           │   │   ├── measurements.py
│   │           │   │   ├── morphology.py
│   │           │   │   ├── _nd_image.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _ni_docstrings.py
│   │           │   │   ├── _ni_label.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _ni_support.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── filters.cpython-36.pyc
│   │           │   │   │   ├── fourier.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── interpolation.cpython-36.pyc
│   │           │   │   │   ├── io.cpython-36.pyc
│   │           │   │   │   ├── measurements.cpython-36.pyc
│   │           │   │   │   ├── morphology.cpython-36.pyc
│   │           │   │   │   ├── _ni_docstrings.cpython-36.pyc
│   │           │   │   │   ├── _ni_support.cpython-36.pyc
│   │           │   │   │   └── setup.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   └── tests
│   │           │   │       ├── data
│   │           │   │       │   ├── label_inputs.txt
│   │           │   │       │   ├── label_results.txt
│   │           │   │       │   ├── label_strels.txt
│   │           │   │       │   └── README.txt
│   │           │   │       ├── dots.png
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_c_api.cpython-36.pyc
│   │           │   │       │   ├── test_datatypes.cpython-36.pyc
│   │           │   │       │   ├── test_filters.cpython-36.pyc
│   │           │   │       │   ├── test_io.cpython-36.pyc
│   │           │   │       │   ├── test_measurements.cpython-36.pyc
│   │           │   │       │   ├── test_ndimage.cpython-36.pyc
│   │           │   │       │   ├── test_regression.cpython-36.pyc
│   │           │   │       │   └── test_splines.cpython-36.pyc
│   │           │   │       ├── test_c_api.py
│   │           │   │       ├── test_datatypes.py
│   │           │   │       ├── test_filters.py
│   │           │   │       ├── test_io.py
│   │           │   │       ├── test_measurements.py
│   │           │   │       ├── test_ndimage.py
│   │           │   │       ├── test_regression.py
│   │           │   │       └── test_splines.py
│   │           │   ├── odr
│   │           │   │   ├── add_newdocs.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── models.py
│   │           │   │   ├── __odrpack.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── odrpack.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── add_newdocs.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── models.cpython-36.pyc
│   │           │   │   │   ├── odrpack.cpython-36.pyc
│   │           │   │   │   └── setup.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   └── test_odr.cpython-36.pyc
│   │           │   │       └── test_odr.py
│   │           │   ├── optimize
│   │           │   │   ├── _basinhopping.py
│   │           │   │   ├── _cobyla.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── cobyla.py
│   │           │   │   ├── _constraints.py
│   │           │   │   ├── _differentiable_functions.py
│   │           │   │   ├── _differentialevolution.py
│   │           │   │   ├── _dual_annealing.py
│   │           │   │   ├── _group_columns.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _hessian_update_strategy.py
│   │           │   │   ├── _hungarian.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _lbfgsb.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── lbfgsb.py
│   │           │   │   ├── lbfgsb_src
│   │           │   │   │   └── README
│   │           │   │   ├── linesearch.py
│   │           │   │   ├── _linprog_ip.py
│   │           │   │   ├── _linprog.py
│   │           │   │   ├── _linprog_simplex.py
│   │           │   │   ├── _linprog_util.py
│   │           │   │   ├── _lsq
│   │           │   │   │   ├── bvls.py
│   │           │   │   │   ├── common.py
│   │           │   │   │   ├── dogbox.py
│   │           │   │   │   ├── givens_elimination.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── least_squares.py
│   │           │   │   │   ├── lsq_linear.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── bvls.cpython-36.pyc
│   │           │   │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   │   ├── dogbox.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── least_squares.cpython-36.pyc
│   │           │   │   │   │   ├── lsq_linear.cpython-36.pyc
│   │           │   │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   │   ├── trf.cpython-36.pyc
│   │           │   │   │   │   └── trf_linear.cpython-36.pyc
│   │           │   │   │   ├── setup.py
│   │           │   │   │   ├── trf_linear.py
│   │           │   │   │   └── trf.py
│   │           │   │   ├── _minimize.py
│   │           │   │   ├── minpack2.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _minpack.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── minpack.py
│   │           │   │   ├── moduleTNC.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _nnls.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── nnls.py
│   │           │   │   ├── nonlin.py
│   │           │   │   ├── _numdiff.py
│   │           │   │   ├── optimize.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _basinhopping.cpython-36.pyc
│   │           │   │   │   ├── cobyla.cpython-36.pyc
│   │           │   │   │   ├── _constraints.cpython-36.pyc
│   │           │   │   │   ├── _differentiable_functions.cpython-36.pyc
│   │           │   │   │   ├── _differentialevolution.cpython-36.pyc
│   │           │   │   │   ├── _dual_annealing.cpython-36.pyc
│   │           │   │   │   ├── _hessian_update_strategy.cpython-36.pyc
│   │           │   │   │   ├── _hungarian.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── lbfgsb.cpython-36.pyc
│   │           │   │   │   ├── linesearch.cpython-36.pyc
│   │           │   │   │   ├── _linprog.cpython-36.pyc
│   │           │   │   │   ├── _linprog_ip.cpython-36.pyc
│   │           │   │   │   ├── _linprog_simplex.cpython-36.pyc
│   │           │   │   │   ├── _linprog_util.cpython-36.pyc
│   │           │   │   │   ├── _minimize.cpython-36.pyc
│   │           │   │   │   ├── minpack.cpython-36.pyc
│   │           │   │   │   ├── nnls.cpython-36.pyc
│   │           │   │   │   ├── nonlin.cpython-36.pyc
│   │           │   │   │   ├── _numdiff.cpython-36.pyc
│   │           │   │   │   ├── optimize.cpython-36.pyc
│   │           │   │   │   ├── _remove_redundancy.cpython-36.pyc
│   │           │   │   │   ├── _root.cpython-36.pyc
│   │           │   │   │   ├── _root_scalar.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   ├── _shgo.cpython-36.pyc
│   │           │   │   │   ├── slsqp.cpython-36.pyc
│   │           │   │   │   ├── _spectral.cpython-36.pyc
│   │           │   │   │   ├── tnc.cpython-36.pyc
│   │           │   │   │   ├── _trustregion.cpython-36.pyc
│   │           │   │   │   ├── _trustregion_dogleg.cpython-36.pyc
│   │           │   │   │   ├── _trustregion_exact.cpython-36.pyc
│   │           │   │   │   ├── _trustregion_krylov.cpython-36.pyc
│   │           │   │   │   ├── _trustregion_ncg.cpython-36.pyc
│   │           │   │   │   ├── _tstutils.cpython-36.pyc
│   │           │   │   │   └── zeros.cpython-36.pyc
│   │           │   │   ├── _remove_redundancy.py
│   │           │   │   ├── _root.py
│   │           │   │   ├── _root_scalar.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _shgo_lib
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── sobol_seq.cpython-36.pyc
│   │           │   │   │   │   └── triangulation.cpython-36.pyc
│   │           │   │   │   ├── sobol_seq.py
│   │           │   │   │   ├── sobol_vec.gz
│   │           │   │   │   └── triangulation.py
│   │           │   │   ├── _shgo.py
│   │           │   │   ├── _slsqp.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── slsqp.py
│   │           │   │   ├── _spectral.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test__basinhopping.cpython-36.pyc
│   │           │   │   │   │   ├── test_cobyla.cpython-36.pyc
│   │           │   │   │   │   ├── test_constraint_conversion.cpython-36.pyc
│   │           │   │   │   │   ├── test_constraints.cpython-36.pyc
│   │           │   │   │   │   ├── test_differentiable_functions.cpython-36.pyc
│   │           │   │   │   │   ├── test__differential_evolution.cpython-36.pyc
│   │           │   │   │   │   ├── test__dual_annealing.cpython-36.pyc
│   │           │   │   │   │   ├── test_hessian_update_strategy.cpython-36.pyc
│   │           │   │   │   │   ├── test_hungarian.cpython-36.pyc
│   │           │   │   │   │   ├── test_lbfgsb_hessinv.cpython-36.pyc
│   │           │   │   │   │   ├── test_least_squares.cpython-36.pyc
│   │           │   │   │   │   ├── test_linesearch.cpython-36.pyc
│   │           │   │   │   │   ├── test__linprog_clean_inputs.cpython-36.pyc
│   │           │   │   │   │   ├── test_linprog.cpython-36.pyc
│   │           │   │   │   │   ├── test_lsq_common.cpython-36.pyc
│   │           │   │   │   │   ├── test_lsq_linear.cpython-36.pyc
│   │           │   │   │   │   ├── test_minimize_constrained.cpython-36.pyc
│   │           │   │   │   │   ├── test_minpack.cpython-36.pyc
│   │           │   │   │   │   ├── test_nnls.cpython-36.pyc
│   │           │   │   │   │   ├── test_nonlin.cpython-36.pyc
│   │           │   │   │   │   ├── test__numdiff.cpython-36.pyc
│   │           │   │   │   │   ├── test_optimize.cpython-36.pyc
│   │           │   │   │   │   ├── test_regression.cpython-36.pyc
│   │           │   │   │   │   ├── test__remove_redundancy.cpython-36.pyc
│   │           │   │   │   │   ├── test__root.cpython-36.pyc
│   │           │   │   │   │   ├── test__shgo.cpython-36.pyc
│   │           │   │   │   │   ├── test_slsqp.cpython-36.pyc
│   │           │   │   │   │   ├── test__spectral.cpython-36.pyc
│   │           │   │   │   │   ├── test_tnc.cpython-36.pyc
│   │           │   │   │   │   ├── test_trustregion.cpython-36.pyc
│   │           │   │   │   │   ├── test_trustregion_exact.cpython-36.pyc
│   │           │   │   │   │   ├── test_trustregion_krylov.cpython-36.pyc
│   │           │   │   │   │   └── test_zeros.cpython-36.pyc
│   │           │   │   │   ├── test__basinhopping.py
│   │           │   │   │   ├── test_cobyla.py
│   │           │   │   │   ├── test_constraint_conversion.py
│   │           │   │   │   ├── test_constraints.py
│   │           │   │   │   ├── test_differentiable_functions.py
│   │           │   │   │   ├── test__differential_evolution.py
│   │           │   │   │   ├── test__dual_annealing.py
│   │           │   │   │   ├── test_hessian_update_strategy.py
│   │           │   │   │   ├── test_hungarian.py
│   │           │   │   │   ├── test_lbfgsb_hessinv.py
│   │           │   │   │   ├── test_least_squares.py
│   │           │   │   │   ├── test_linesearch.py
│   │           │   │   │   ├── test__linprog_clean_inputs.py
│   │           │   │   │   ├── test_linprog.py
│   │           │   │   │   ├── test_lsq_common.py
│   │           │   │   │   ├── test_lsq_linear.py
│   │           │   │   │   ├── test_minimize_constrained.py
│   │           │   │   │   ├── test_minpack.py
│   │           │   │   │   ├── test_nnls.py
│   │           │   │   │   ├── test_nonlin.py
│   │           │   │   │   ├── test__numdiff.py
│   │           │   │   │   ├── test_optimize.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   ├── test__remove_redundancy.py
│   │           │   │   │   ├── test__root.py
│   │           │   │   │   ├── test__shgo.py
│   │           │   │   │   ├── test_slsqp.py
│   │           │   │   │   ├── test__spectral.py
│   │           │   │   │   ├── test_tnc.py
│   │           │   │   │   ├── test_trustregion_exact.py
│   │           │   │   │   ├── test_trustregion_krylov.py
│   │           │   │   │   ├── test_trustregion.py
│   │           │   │   │   └── test_zeros.py
│   │           │   │   ├── tnc.py
│   │           │   │   ├── _trlib
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── setup.cpython-36.pyc
│   │           │   │   │   ├── setup.py
│   │           │   │   │   └── _trlib.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _trustregion_constr
│   │           │   │   │   ├── canonical_constraint.py
│   │           │   │   │   ├── equality_constrained_sqp.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── minimize_trustregion_constr.py
│   │           │   │   │   ├── projections.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── canonical_constraint.cpython-36.pyc
│   │           │   │   │   │   ├── equality_constrained_sqp.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── minimize_trustregion_constr.cpython-36.pyc
│   │           │   │   │   │   ├── projections.cpython-36.pyc
│   │           │   │   │   │   ├── qp_subproblem.cpython-36.pyc
│   │           │   │   │   │   ├── report.cpython-36.pyc
│   │           │   │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   │   └── tr_interior_point.cpython-36.pyc
│   │           │   │   │   ├── qp_subproblem.py
│   │           │   │   │   ├── report.py
│   │           │   │   │   ├── setup.py
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_canonical_constraint.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_projections.cpython-36.pyc
│   │           │   │   │   │   │   └── test_qp_subproblem.cpython-36.pyc
│   │           │   │   │   │   ├── test_canonical_constraint.py
│   │           │   │   │   │   ├── test_projections.py
│   │           │   │   │   │   └── test_qp_subproblem.py
│   │           │   │   │   └── tr_interior_point.py
│   │           │   │   ├── _trustregion_dogleg.py
│   │           │   │   ├── _trustregion_exact.py
│   │           │   │   ├── _trustregion_krylov.py
│   │           │   │   ├── _trustregion_ncg.py
│   │           │   │   ├── _trustregion.py
│   │           │   │   ├── _tstutils.py
│   │           │   │   ├── _zeros.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   └── zeros.py
│   │           │   ├── __pycache__
│   │           │   │   ├── __config__.cpython-36.pyc
│   │           │   │   ├── conftest.cpython-36.pyc
│   │           │   │   ├── _distributor_init.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── setup.cpython-36.pyc
│   │           │   │   └── version.cpython-36.pyc
│   │           │   ├── setup.py
│   │           │   ├── signal
│   │           │   │   ├── _arraytools.py
│   │           │   │   ├── bsplines.py
│   │           │   │   ├── filter_design.py
│   │           │   │   ├── fir_filter_design.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── lti_conversion.py
│   │           │   │   ├── ltisys.py
│   │           │   │   ├── _max_len_seq_inner.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _max_len_seq.py
│   │           │   │   ├── _peak_finding.py
│   │           │   │   ├── _peak_finding_utils.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _arraytools.cpython-36.pyc
│   │           │   │   │   ├── bsplines.cpython-36.pyc
│   │           │   │   │   ├── filter_design.cpython-36.pyc
│   │           │   │   │   ├── fir_filter_design.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── lti_conversion.cpython-36.pyc
│   │           │   │   │   ├── ltisys.cpython-36.pyc
│   │           │   │   │   ├── _max_len_seq.cpython-36.pyc
│   │           │   │   │   ├── _peak_finding.cpython-36.pyc
│   │           │   │   │   ├── _savitzky_golay.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   ├── signaltools.cpython-36.pyc
│   │           │   │   │   ├── spectral.cpython-36.pyc
│   │           │   │   │   ├── _upfirdn.cpython-36.pyc
│   │           │   │   │   ├── waveforms.cpython-36.pyc
│   │           │   │   │   └── wavelets.cpython-36.pyc
│   │           │   │   ├── _savitzky_golay.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── signaltools.py
│   │           │   │   ├── sigtools.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _spectral.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── spectral.py
│   │           │   │   ├── spline.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── mpsig.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── mpsig.cpython-36.pyc
│   │           │   │   │   │   ├── test_array_tools.cpython-36.pyc
│   │           │   │   │   │   ├── test_bsplines.cpython-36.pyc
│   │           │   │   │   │   ├── test_cont2discrete.cpython-36.pyc
│   │           │   │   │   │   ├── test_dltisys.cpython-36.pyc
│   │           │   │   │   │   ├── test_filter_design.cpython-36.pyc
│   │           │   │   │   │   ├── test_fir_filter_design.cpython-36.pyc
│   │           │   │   │   │   ├── test_ltisys.cpython-36.pyc
│   │           │   │   │   │   ├── test_max_len_seq.cpython-36.pyc
│   │           │   │   │   │   ├── test_peak_finding.cpython-36.pyc
│   │           │   │   │   │   ├── test_savitzky_golay.cpython-36.pyc
│   │           │   │   │   │   ├── test_signaltools.cpython-36.pyc
│   │           │   │   │   │   ├── test_spectral.cpython-36.pyc
│   │           │   │   │   │   ├── test_upfirdn.cpython-36.pyc
│   │           │   │   │   │   ├── test_waveforms.cpython-36.pyc
│   │           │   │   │   │   ├── test_wavelets.cpython-36.pyc
│   │           │   │   │   │   └── test_windows.cpython-36.pyc
│   │           │   │   │   ├── test_array_tools.py
│   │           │   │   │   ├── test_bsplines.py
│   │           │   │   │   ├── test_cont2discrete.py
│   │           │   │   │   ├── test_dltisys.py
│   │           │   │   │   ├── test_filter_design.py
│   │           │   │   │   ├── test_fir_filter_design.py
│   │           │   │   │   ├── test_ltisys.py
│   │           │   │   │   ├── test_max_len_seq.py
│   │           │   │   │   ├── test_peak_finding.py
│   │           │   │   │   ├── test_savitzky_golay.py
│   │           │   │   │   ├── test_signaltools.py
│   │           │   │   │   ├── test_spectral.py
│   │           │   │   │   ├── test_upfirdn.py
│   │           │   │   │   ├── test_waveforms.py
│   │           │   │   │   ├── test_wavelets.py
│   │           │   │   │   └── test_windows.py
│   │           │   │   ├── _upfirdn_apply.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _upfirdn.py
│   │           │   │   ├── waveforms.py
│   │           │   │   ├── wavelets.py
│   │           │   │   └── windows
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── setup.cpython-36.pyc
│   │           │   │       │   └── windows.cpython-36.pyc
│   │           │   │       ├── setup.py
│   │           │   │       └── windows.py
│   │           │   ├── sparse
│   │           │   │   ├── base.py
│   │           │   │   ├── bsr.py
│   │           │   │   ├── compressed.py
│   │           │   │   ├── construct.py
│   │           │   │   ├── coo.py
│   │           │   │   ├── csc.py
│   │           │   │   ├── csgraph
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _laplacian.py
│   │           │   │   │   ├── _min_spanning_tree.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── _laplacian.cpython-36.pyc
│   │           │   │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   │   └── _validation.cpython-36.pyc
│   │           │   │   │   ├── _reordering.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── setup.py
│   │           │   │   │   ├── _shortest_path.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_connected_components.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_conversions.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_graph_laplacian.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_reordering.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_shortest_path.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_spanning_tree.cpython-36.pyc
│   │           │   │   │   │   │   └── test_traversal.cpython-36.pyc
│   │           │   │   │   │   ├── test_connected_components.py
│   │           │   │   │   │   ├── test_conversions.py
│   │           │   │   │   │   ├── test_graph_laplacian.py
│   │           │   │   │   │   ├── test_reordering.py
│   │           │   │   │   │   ├── test_shortest_path.py
│   │           │   │   │   │   ├── test_spanning_tree.py
│   │           │   │   │   │   └── test_traversal.py
│   │           │   │   │   ├── _tools.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   ├── _traversal.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   └── _validation.py
│   │           │   │   ├── _csparsetools.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── csr.py
│   │           │   │   ├── data.py
│   │           │   │   ├── dia.py
│   │           │   │   ├── dok.py
│   │           │   │   ├── extract.py
│   │           │   │   ├── generate_sparsetools.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── lil.py
│   │           │   │   ├── linalg
│   │           │   │   │   ├── dsolve
│   │           │   │   │   │   ├── _add_newdocs.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── linsolve.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── _add_newdocs.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── linsolve.cpython-36.pyc
│   │           │   │   │   │   │   └── setup.cpython-36.pyc
│   │           │   │   │   │   ├── setup.py
│   │           │   │   │   │   ├── SuperLU
│   │           │   │   │   │   │   └── License.txt
│   │           │   │   │   │   ├── _superlu.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   │   └── tests
│   │           │   │   │   │       ├── __init__.py
│   │           │   │   │   │       ├── __pycache__
│   │           │   │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │       │   └── test_linsolve.cpython-36.pyc
│   │           │   │   │   │       └── test_linsolve.py
│   │           │   │   │   ├── eigen
│   │           │   │   │   │   ├── arpack
│   │           │   │   │   │   │   ├── ARPACK
│   │           │   │   │   │   │   │   └── COPYING
│   │           │   │   │   │   │   ├── _arpack.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   │   │   ├── arpack.py
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── arpack.cpython-36.pyc
│   │           │   │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   │   └── setup.cpython-36.pyc
│   │           │   │   │   │   │   ├── setup.py
│   │           │   │   │   │   │   └── tests
│   │           │   │   │   │   │       ├── __init__.py
│   │           │   │   │   │   │       ├── __pycache__
│   │           │   │   │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │       │   └── test_arpack.cpython-36.pyc
│   │           │   │   │   │   │       └── test_arpack.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── lobpcg
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   ├── lobpcg.py
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   │   ├── lobpcg.cpython-36.pyc
│   │           │   │   │   │   │   │   └── setup.cpython-36.pyc
│   │           │   │   │   │   │   ├── setup.py
│   │           │   │   │   │   │   └── tests
│   │           │   │   │   │   │       ├── __init__.py
│   │           │   │   │   │   │       ├── __pycache__
│   │           │   │   │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │       │   └── test_lobpcg.cpython-36.pyc
│   │           │   │   │   │   │       └── test_lobpcg.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   └── setup.cpython-36.pyc
│   │           │   │   │   │   └── setup.py
│   │           │   │   │   ├── _expm_multiply.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── interface.py
│   │           │   │   │   ├── isolve
│   │           │   │   │   │   ├── _gcrotmk.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── _iterative.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   │   │   ├── iterative.py
│   │           │   │   │   │   ├── lgmres.py
│   │           │   │   │   │   ├── lsmr.py
│   │           │   │   │   │   ├── lsqr.py
│   │           │   │   │   │   ├── minres.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── _gcrotmk.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── iterative.cpython-36.pyc
│   │           │   │   │   │   │   ├── lgmres.cpython-36.pyc
│   │           │   │   │   │   │   ├── lsmr.cpython-36.pyc
│   │           │   │   │   │   │   ├── lsqr.cpython-36.pyc
│   │           │   │   │   │   │   ├── minres.cpython-36.pyc
│   │           │   │   │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   │   │   └── utils.cpython-36.pyc
│   │           │   │   │   │   ├── setup.py
│   │           │   │   │   │   ├── tests
│   │           │   │   │   │   │   ├── demo_lgmres.py
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── demo_lgmres.cpython-36.pyc
│   │           │   │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   │   ├── test_gcrotmk.cpython-36.pyc
│   │           │   │   │   │   │   │   ├── test_iterative.cpython-36.pyc
│   │           │   │   │   │   │   │   ├── test_lgmres.cpython-36.pyc
│   │           │   │   │   │   │   │   ├── test_lsmr.cpython-36.pyc
│   │           │   │   │   │   │   │   ├── test_lsqr.cpython-36.pyc
│   │           │   │   │   │   │   │   ├── test_minres.cpython-36.pyc
│   │           │   │   │   │   │   │   └── test_utils.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_gcrotmk.py
│   │           │   │   │   │   │   ├── test_iterative.py
│   │           │   │   │   │   │   ├── test_lgmres.py
│   │           │   │   │   │   │   ├── test_lsmr.py
│   │           │   │   │   │   │   ├── test_lsqr.py
│   │           │   │   │   │   │   ├── test_minres.py
│   │           │   │   │   │   │   └── test_utils.py
│   │           │   │   │   │   └── utils.py
│   │           │   │   │   ├── matfuncs.py
│   │           │   │   │   ├── _norm.py
│   │           │   │   │   ├── _onenormest.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── _expm_multiply.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── interface.cpython-36.pyc
│   │           │   │   │   │   ├── matfuncs.cpython-36.pyc
│   │           │   │   │   │   ├── _norm.cpython-36.pyc
│   │           │   │   │   │   ├── _onenormest.cpython-36.pyc
│   │           │   │   │   │   └── setup.cpython-36.pyc
│   │           │   │   │   ├── setup.py
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_expm_multiply.cpython-36.pyc
│   │           │   │   │       │   ├── test_interface.cpython-36.pyc
│   │           │   │   │       │   ├── test_matfuncs.cpython-36.pyc
│   │           │   │   │       │   ├── test_norm.cpython-36.pyc
│   │           │   │   │       │   └── test_onenormest.cpython-36.pyc
│   │           │   │   │       ├── test_expm_multiply.py
│   │           │   │   │       ├── test_interface.py
│   │           │   │   │       ├── test_matfuncs.py
│   │           │   │   │       ├── test_norm.py
│   │           │   │   │       └── test_onenormest.py
│   │           │   │   ├── _matrix_io.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── base.cpython-36.pyc
│   │           │   │   │   ├── bsr.cpython-36.pyc
│   │           │   │   │   ├── compressed.cpython-36.pyc
│   │           │   │   │   ├── construct.cpython-36.pyc
│   │           │   │   │   ├── coo.cpython-36.pyc
│   │           │   │   │   ├── csc.cpython-36.pyc
│   │           │   │   │   ├── csr.cpython-36.pyc
│   │           │   │   │   ├── data.cpython-36.pyc
│   │           │   │   │   ├── dia.cpython-36.pyc
│   │           │   │   │   ├── dok.cpython-36.pyc
│   │           │   │   │   ├── extract.cpython-36.pyc
│   │           │   │   │   ├── generate_sparsetools.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── lil.cpython-36.pyc
│   │           │   │   │   ├── _matrix_io.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   ├── sparsetools.cpython-36.pyc
│   │           │   │   │   ├── spfuncs.cpython-36.pyc
│   │           │   │   │   └── sputils.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   ├── _sparsetools.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── sparsetools.py
│   │           │   │   ├── spfuncs.py
│   │           │   │   ├── sputils.py
│   │           │   │   └── tests
│   │           │   │       ├── data
│   │           │   │       │   ├── csc_py2.npz
│   │           │   │       │   └── csc_py3.npz
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_base.cpython-36.pyc
│   │           │   │       │   ├── test_construct.cpython-36.pyc
│   │           │   │       │   ├── test_csc.cpython-36.pyc
│   │           │   │       │   ├── test_csr.cpython-36.pyc
│   │           │   │       │   ├── test_extract.cpython-36.pyc
│   │           │   │       │   ├── test_matrix_io.cpython-36.pyc
│   │           │   │       │   ├── test_sparsetools.cpython-36.pyc
│   │           │   │       │   ├── test_spfuncs.cpython-36.pyc
│   │           │   │       │   └── test_sputils.cpython-36.pyc
│   │           │   │       ├── test_base.py
│   │           │   │       ├── test_construct.py
│   │           │   │       ├── test_csc.py
│   │           │   │       ├── test_csr.py
│   │           │   │       ├── test_extract.py
│   │           │   │       ├── test_matrix_io.py
│   │           │   │       ├── test_sparsetools.py
│   │           │   │       ├── test_spfuncs.py
│   │           │   │       └── test_sputils.py
│   │           │   ├── spatial
│   │           │   │   ├── ckdtree.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── distance.py
│   │           │   │   ├── _distance_wrap.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _hausdorff.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── __init__.py
│   │           │   │   ├── kdtree.py
│   │           │   │   ├── _plotutils.py
│   │           │   │   ├── _procrustes.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── distance.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── kdtree.cpython-36.pyc
│   │           │   │   │   ├── _plotutils.cpython-36.pyc
│   │           │   │   │   ├── _procrustes.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   └── _spherical_voronoi.cpython-36.pyc
│   │           │   │   ├── qhull.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── qhull_src
│   │           │   │   │   └── COPYING.txt
│   │           │   │   ├── setup.py
│   │           │   │   ├── _spherical_voronoi.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── cdist-X1.txt
│   │           │   │   │   │   ├── cdist-X2.txt
│   │           │   │   │   │   ├── degenerate_pointset.npz
│   │           │   │   │   │   ├── iris.txt
│   │           │   │   │   │   ├── pdist-boolean-inp.txt
│   │           │   │   │   │   ├── pdist-chebyshev-ml-iris.txt
│   │           │   │   │   │   ├── pdist-chebyshev-ml.txt
│   │           │   │   │   │   ├── pdist-cityblock-ml-iris.txt
│   │           │   │   │   │   ├── pdist-cityblock-ml.txt
│   │           │   │   │   │   ├── pdist-correlation-ml-iris.txt
│   │           │   │   │   │   ├── pdist-correlation-ml.txt
│   │           │   │   │   │   ├── pdist-cosine-ml-iris.txt
│   │           │   │   │   │   ├── pdist-cosine-ml.txt
│   │           │   │   │   │   ├── pdist-double-inp.txt
│   │           │   │   │   │   ├── pdist-euclidean-ml-iris.txt
│   │           │   │   │   │   ├── pdist-euclidean-ml.txt
│   │           │   │   │   │   ├── pdist-hamming-ml.txt
│   │           │   │   │   │   ├── pdist-jaccard-ml.txt
│   │           │   │   │   │   ├── pdist-jensenshannon-ml-iris.txt
│   │           │   │   │   │   ├── pdist-jensenshannon-ml.txt
│   │           │   │   │   │   ├── pdist-minkowski-3.2-ml-iris.txt
│   │           │   │   │   │   ├── pdist-minkowski-3.2-ml.txt
│   │           │   │   │   │   ├── pdist-minkowski-5.8-ml-iris.txt
│   │           │   │   │   │   ├── pdist-seuclidean-ml-iris.txt
│   │           │   │   │   │   ├── pdist-seuclidean-ml.txt
│   │           │   │   │   │   ├── pdist-spearman-ml.txt
│   │           │   │   │   │   ├── random-bool-data.txt
│   │           │   │   │   │   ├── random-double-data.txt
│   │           │   │   │   │   ├── random-int-data.txt
│   │           │   │   │   │   ├── random-uint-data.txt
│   │           │   │   │   │   └── selfdual-4d-polytope.txt
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_distance.cpython-36.pyc
│   │           │   │   │   │   ├── test_hausdorff.cpython-36.pyc
│   │           │   │   │   │   ├── test_kdtree.cpython-36.pyc
│   │           │   │   │   │   ├── test__plotutils.cpython-36.pyc
│   │           │   │   │   │   ├── test__procrustes.cpython-36.pyc
│   │           │   │   │   │   ├── test_qhull.cpython-36.pyc
│   │           │   │   │   │   └── test_spherical_voronoi.cpython-36.pyc
│   │           │   │   │   ├── test_distance.py
│   │           │   │   │   ├── test_hausdorff.py
│   │           │   │   │   ├── test_kdtree.py
│   │           │   │   │   ├── test__plotutils.py
│   │           │   │   │   ├── test__procrustes.py
│   │           │   │   │   ├── test_qhull.py
│   │           │   │   │   └── test_spherical_voronoi.py
│   │           │   │   ├── transform
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── rotation.cpython-36.pyc
│   │           │   │   │   │   └── setup.cpython-36.pyc
│   │           │   │   │   ├── rotation.py
│   │           │   │   │   ├── setup.py
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   └── test_rotation.cpython-36.pyc
│   │           │   │   │       └── test_rotation.py
│   │           │   │   └── _voronoi.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── special
│   │           │   │   ├── add_newdocs.py
│   │           │   │   ├── basic.py
│   │           │   │   ├── _comb.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── cython_special.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── cython_special.pxd
│   │           │   │   ├── _ellip_harm_2.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _ellip_harm.py
│   │           │   │   ├── _generate_pyx.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── lambertw.py
│   │           │   │   ├── _logsumexp.py
│   │           │   │   ├── _mptestutils.py
│   │           │   │   ├── orthogonal.py
│   │           │   │   ├── _precompute
│   │           │   │   │   ├── expn_asy.py
│   │           │   │   │   ├── gammainc_asy.py
│   │           │   │   │   ├── gammainc_data.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── lambertw.py
│   │           │   │   │   ├── loggamma.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── expn_asy.cpython-36.pyc
│   │           │   │   │   │   ├── gammainc_asy.cpython-36.pyc
│   │           │   │   │   │   ├── gammainc_data.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── lambertw.cpython-36.pyc
│   │           │   │   │   │   ├── loggamma.cpython-36.pyc
│   │           │   │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   │   ├── struve_convergence.cpython-36.pyc
│   │           │   │   │   │   ├── utils.cpython-36.pyc
│   │           │   │   │   │   └── zetac.cpython-36.pyc
│   │           │   │   │   ├── setup.py
│   │           │   │   │   ├── struve_convergence.py
│   │           │   │   │   ├── utils.py
│   │           │   │   │   └── zetac.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── add_newdocs.cpython-36.pyc
│   │           │   │   │   ├── basic.cpython-36.pyc
│   │           │   │   │   ├── _ellip_harm.cpython-36.pyc
│   │           │   │   │   ├── _generate_pyx.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── lambertw.cpython-36.pyc
│   │           │   │   │   ├── _logsumexp.cpython-36.pyc
│   │           │   │   │   ├── _mptestutils.cpython-36.pyc
│   │           │   │   │   ├── orthogonal.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   ├── sf_error.cpython-36.pyc
│   │           │   │   │   ├── spfun_stats.cpython-36.pyc
│   │           │   │   │   ├── _spherical_bessel.cpython-36.pyc
│   │           │   │   │   └── _testutils.cpython-36.pyc
│   │           │   │   ├── setup.py
│   │           │   │   ├── sf_error.py
│   │           │   │   ├── specfun.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── spfun_stats.py
│   │           │   │   ├── _spherical_bessel.py
│   │           │   │   ├── _test_round.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── boost.npz
│   │           │   │   │   │   ├── gsl.npz
│   │           │   │   │   │   ├── local.npz
│   │           │   │   │   │   └── README
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_basic.cpython-36.pyc
│   │           │   │   │   │   ├── test_boxcox.cpython-36.pyc
│   │           │   │   │   │   ├── test_cdflib.cpython-36.pyc
│   │           │   │   │   │   ├── test_cython_special.cpython-36.pyc
│   │           │   │   │   │   ├── test_data.cpython-36.pyc
│   │           │   │   │   │   ├── test_digamma.cpython-36.pyc
│   │           │   │   │   │   ├── test_ellip_harm.cpython-36.pyc
│   │           │   │   │   │   ├── test_gammainc.cpython-36.pyc
│   │           │   │   │   │   ├── test_kolmogorov.cpython-36.pyc
│   │           │   │   │   │   ├── test_lambertw.cpython-36.pyc
│   │           │   │   │   │   ├── test_loggamma.cpython-36.pyc
│   │           │   │   │   │   ├── test_logit.cpython-36.pyc
│   │           │   │   │   │   ├── test_logsumexp.cpython-36.pyc
│   │           │   │   │   │   ├── test_mpmath.cpython-36.pyc
│   │           │   │   │   │   ├── test_nan_inputs.cpython-36.pyc
│   │           │   │   │   │   ├── test_orthogonal.cpython-36.pyc
│   │           │   │   │   │   ├── test_orthogonal_eval.cpython-36.pyc
│   │           │   │   │   │   ├── test_owens_t.cpython-36.pyc
│   │           │   │   │   │   ├── test_pcf.cpython-36.pyc
│   │           │   │   │   │   ├── test_precompute_expn_asy.cpython-36.pyc
│   │           │   │   │   │   ├── test_precompute_gammainc.cpython-36.pyc
│   │           │   │   │   │   ├── test_precompute_utils.cpython-36.pyc
│   │           │   │   │   │   ├── test_round.cpython-36.pyc
│   │           │   │   │   │   ├── test_sf_error.cpython-36.pyc
│   │           │   │   │   │   ├── test_sici.cpython-36.pyc
│   │           │   │   │   │   ├── test_spence.cpython-36.pyc
│   │           │   │   │   │   ├── test_spfun_stats.cpython-36.pyc
│   │           │   │   │   │   ├── test_spherical_bessel.cpython-36.pyc
│   │           │   │   │   │   ├── test_sph_harm.cpython-36.pyc
│   │           │   │   │   │   ├── test_trig.cpython-36.pyc
│   │           │   │   │   │   ├── test_wrightomega.cpython-36.pyc
│   │           │   │   │   │   └── test_zeta.cpython-36.pyc
│   │           │   │   │   ├── test_basic.py
│   │           │   │   │   ├── test_boxcox.py
│   │           │   │   │   ├── test_cdflib.py
│   │           │   │   │   ├── test_cython_special.py
│   │           │   │   │   ├── test_data.py
│   │           │   │   │   ├── test_digamma.py
│   │           │   │   │   ├── test_ellip_harm.py
│   │           │   │   │   ├── test_gammainc.py
│   │           │   │   │   ├── test_kolmogorov.py
│   │           │   │   │   ├── test_lambertw.py
│   │           │   │   │   ├── test_loggamma.py
│   │           │   │   │   ├── test_logit.py
│   │           │   │   │   ├── test_logsumexp.py
│   │           │   │   │   ├── test_mpmath.py
│   │           │   │   │   ├── test_nan_inputs.py
│   │           │   │   │   ├── test_orthogonal_eval.py
│   │           │   │   │   ├── test_orthogonal.py
│   │           │   │   │   ├── test_owens_t.py
│   │           │   │   │   ├── test_pcf.py
│   │           │   │   │   ├── test_precompute_expn_asy.py
│   │           │   │   │   ├── test_precompute_gammainc.py
│   │           │   │   │   ├── test_precompute_utils.py
│   │           │   │   │   ├── test_round.py
│   │           │   │   │   ├── test_sf_error.py
│   │           │   │   │   ├── test_sici.py
│   │           │   │   │   ├── test_spence.py
│   │           │   │   │   ├── test_spfun_stats.py
│   │           │   │   │   ├── test_spherical_bessel.py
│   │           │   │   │   ├── test_sph_harm.py
│   │           │   │   │   ├── test_trig.py
│   │           │   │   │   ├── test_wrightomega.py
│   │           │   │   │   └── test_zeta.py
│   │           │   │   ├── _testutils.py
│   │           │   │   ├── _ufuncs.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   └── _ufuncs_cxx.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── special.pxd
│   │           │   ├── stats
│   │           │   │   ├── _binned_statistic.py
│   │           │   │   ├── _constants.py
│   │           │   │   ├── contingency.py
│   │           │   │   ├── _continuous_distns.py
│   │           │   │   ├── _discrete_distns.py
│   │           │   │   ├── _distn_infrastructure.py
│   │           │   │   ├── distributions.py
│   │           │   │   ├── _distr_params.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── kde.py
│   │           │   │   ├── morestats.py
│   │           │   │   ├── mstats_basic.py
│   │           │   │   ├── mstats_extras.py
│   │           │   │   ├── mstats.py
│   │           │   │   ├── _multivariate.py
│   │           │   │   ├── mvn.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _binned_statistic.cpython-36.pyc
│   │           │   │   │   ├── _constants.cpython-36.pyc
│   │           │   │   │   ├── contingency.cpython-36.pyc
│   │           │   │   │   ├── _continuous_distns.cpython-36.pyc
│   │           │   │   │   ├── _discrete_distns.cpython-36.pyc
│   │           │   │   │   ├── _distn_infrastructure.cpython-36.pyc
│   │           │   │   │   ├── distributions.cpython-36.pyc
│   │           │   │   │   ├── _distr_params.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── kde.cpython-36.pyc
│   │           │   │   │   ├── morestats.cpython-36.pyc
│   │           │   │   │   ├── mstats_basic.cpython-36.pyc
│   │           │   │   │   ├── mstats.cpython-36.pyc
│   │           │   │   │   ├── mstats_extras.cpython-36.pyc
│   │           │   │   │   ├── _multivariate.cpython-36.pyc
│   │           │   │   │   ├── _rvs_sampling.cpython-36.pyc
│   │           │   │   │   ├── setup.cpython-36.pyc
│   │           │   │   │   ├── stats.cpython-36.pyc
│   │           │   │   │   ├── _stats_mstats_common.cpython-36.pyc
│   │           │   │   │   ├── _tukeylambda_stats.cpython-36.pyc
│   │           │   │   │   └── vonmises.cpython-36.pyc
│   │           │   │   ├── _rvs_sampling.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── statlib.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _stats.cpython-36m-x86_64-linux-gnu.so
│   │           │   │   ├── _stats_mstats_common.py
│   │           │   │   ├── stats.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── common_tests.py
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── nist_anova
│   │           │   │   │   │   │   ├── AtmWtAg.dat
│   │           │   │   │   │   │   ├── SiRstv.dat
│   │           │   │   │   │   │   ├── SmLs01.dat
│   │           │   │   │   │   │   ├── SmLs02.dat
│   │           │   │   │   │   │   ├── SmLs03.dat
│   │           │   │   │   │   │   ├── SmLs04.dat
│   │           │   │   │   │   │   ├── SmLs05.dat
│   │           │   │   │   │   │   ├── SmLs06.dat
│   │           │   │   │   │   │   ├── SmLs07.dat
│   │           │   │   │   │   │   ├── SmLs08.dat
│   │           │   │   │   │   │   └── SmLs09.dat
│   │           │   │   │   │   ├── nist_linregress
│   │           │   │   │   │   │   └── Norris.dat
│   │           │   │   │   │   ├── stable-cdf-sample-data.npy
│   │           │   │   │   │   └── stable-pdf-sample-data.npy
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── common_tests.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_binned_statistic.cpython-36.pyc
│   │           │   │   │   │   ├── test_contingency.cpython-36.pyc
│   │           │   │   │   │   ├── test_continuous_basic.cpython-36.pyc
│   │           │   │   │   │   ├── test_discrete_basic.cpython-36.pyc
│   │           │   │   │   │   ├── test_discrete_distns.cpython-36.pyc
│   │           │   │   │   │   ├── test_distributions.cpython-36.pyc
│   │           │   │   │   │   ├── test_fit.cpython-36.pyc
│   │           │   │   │   │   ├── test_kdeoth.cpython-36.pyc
│   │           │   │   │   │   ├── test_morestats.cpython-36.pyc
│   │           │   │   │   │   ├── test_mstats_basic.cpython-36.pyc
│   │           │   │   │   │   ├── test_mstats_extras.cpython-36.pyc
│   │           │   │   │   │   ├── test_multivariate.cpython-36.pyc
│   │           │   │   │   │   ├── test_rank.cpython-36.pyc
│   │           │   │   │   │   ├── test_stats.cpython-36.pyc
│   │           │   │   │   │   └── test_tukeylambda_stats.cpython-36.pyc
│   │           │   │   │   ├── test_binned_statistic.py
│   │           │   │   │   ├── test_contingency.py
│   │           │   │   │   ├── test_continuous_basic.py
│   │           │   │   │   ├── test_discrete_basic.py
│   │           │   │   │   ├── test_discrete_distns.py
│   │           │   │   │   ├── test_distributions.py
│   │           │   │   │   ├── test_fit.py
│   │           │   │   │   ├── test_kdeoth.py
│   │           │   │   │   ├── test_morestats.py
│   │           │   │   │   ├── test_mstats_basic.py
│   │           │   │   │   ├── test_mstats_extras.py
│   │           │   │   │   ├── test_multivariate.py
│   │           │   │   │   ├── test_rank.py
│   │           │   │   │   ├── test_stats.py
│   │           │   │   │   └── test_tukeylambda_stats.py
│   │           │   │   ├── _tukeylambda_stats.py
│   │           │   │   └── vonmises.py
│   │           │   ├── THANKS.txt
│   │           │   └── version.py
│   │           ├── scipy-1.2.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── send2trash
│   │           │   ├── compat.py
│   │           │   ├── exceptions.py
│   │           │   ├── __init__.py
│   │           │   ├── plat_gio.py
│   │           │   ├── plat_osx.py
│   │           │   ├── plat_other.py
│   │           │   ├── plat_win.py
│   │           │   └── __pycache__
│   │           │       ├── compat.cpython-36.pyc
│   │           │       ├── exceptions.cpython-36.pyc
│   │           │       ├── __init__.cpython-36.pyc
│   │           │       ├── plat_gio.cpython-36.pyc
│   │           │       ├── plat_osx.cpython-36.pyc
│   │           │       ├── plat_other.cpython-36.pyc
│   │           │       └── plat_win.cpython-36.pyc
│   │           ├── Send2Trash-1.5.0.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── setuptools
│   │           │   ├── archive_util.py
│   │           │   ├── build_meta.py
│   │           │   ├── cli-32.exe
│   │           │   ├── cli-64.exe
│   │           │   ├── cli.exe
│   │           │   ├── command
│   │           │   │   ├── alias.py
│   │           │   │   ├── bdist_egg.py
│   │           │   │   ├── bdist_rpm.py
│   │           │   │   ├── bdist_wininst.py
│   │           │   │   ├── build_clib.py
│   │           │   │   ├── build_ext.py
│   │           │   │   ├── build_py.py
│   │           │   │   ├── develop.py
│   │           │   │   ├── dist_info.py
│   │           │   │   ├── easy_install.py
│   │           │   │   ├── egg_info.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── install_egg_info.py
│   │           │   │   ├── install_lib.py
│   │           │   │   ├── install.py
│   │           │   │   ├── install_scripts.py
│   │           │   │   ├── launcher manifest.xml
│   │           │   │   ├── py36compat.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── alias.cpython-36.pyc
│   │           │   │   │   ├── bdist_egg.cpython-36.pyc
│   │           │   │   │   ├── bdist_rpm.cpython-36.pyc
│   │           │   │   │   ├── bdist_wininst.cpython-36.pyc
│   │           │   │   │   ├── build_clib.cpython-36.pyc
│   │           │   │   │   ├── build_ext.cpython-36.pyc
│   │           │   │   │   ├── build_py.cpython-36.pyc
│   │           │   │   │   ├── develop.cpython-36.pyc
│   │           │   │   │   ├── dist_info.cpython-36.pyc
│   │           │   │   │   ├── easy_install.cpython-36.pyc
│   │           │   │   │   ├── egg_info.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── install.cpython-36.pyc
│   │           │   │   │   ├── install_egg_info.cpython-36.pyc
│   │           │   │   │   ├── install_lib.cpython-36.pyc
│   │           │   │   │   ├── install_scripts.cpython-36.pyc
│   │           │   │   │   ├── py36compat.cpython-36.pyc
│   │           │   │   │   ├── register.cpython-36.pyc
│   │           │   │   │   ├── rotate.cpython-36.pyc
│   │           │   │   │   ├── saveopts.cpython-36.pyc
│   │           │   │   │   ├── sdist.cpython-36.pyc
│   │           │   │   │   ├── setopt.cpython-36.pyc
│   │           │   │   │   ├── test.cpython-36.pyc
│   │           │   │   │   ├── upload.cpython-36.pyc
│   │           │   │   │   └── upload_docs.cpython-36.pyc
│   │           │   │   ├── register.py
│   │           │   │   ├── rotate.py
│   │           │   │   ├── saveopts.py
│   │           │   │   ├── sdist.py
│   │           │   │   ├── setopt.py
│   │           │   │   ├── test.py
│   │           │   │   ├── upload_docs.py
│   │           │   │   └── upload.py
│   │           │   ├── config.py
│   │           │   ├── depends.py
│   │           │   ├── dep_util.py
│   │           │   ├── dist.py
│   │           │   ├── extension.py
│   │           │   ├── extern
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── glibc.py
│   │           │   ├── glob.py
│   │           │   ├── gui-32.exe
│   │           │   ├── gui-64.exe
│   │           │   ├── gui.exe
│   │           │   ├── __init__.py
│   │           │   ├── launch.py
│   │           │   ├── lib2to3_ex.py
│   │           │   ├── monkey.py
│   │           │   ├── msvc.py
│   │           │   ├── namespaces.py
│   │           │   ├── package_index.py
│   │           │   ├── pep425tags.py
│   │           │   ├── py27compat.py
│   │           │   ├── py31compat.py
│   │           │   ├── py33compat.py
│   │           │   ├── py36compat.py
│   │           │   ├── __pycache__
│   │           │   │   ├── archive_util.cpython-36.pyc
│   │           │   │   ├── build_meta.cpython-36.pyc
│   │           │   │   ├── config.cpython-36.pyc
│   │           │   │   ├── depends.cpython-36.pyc
│   │           │   │   ├── dep_util.cpython-36.pyc
│   │           │   │   ├── dist.cpython-36.pyc
│   │           │   │   ├── extension.cpython-36.pyc
│   │           │   │   ├── glibc.cpython-36.pyc
│   │           │   │   ├── glob.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── launch.cpython-36.pyc
│   │           │   │   ├── lib2to3_ex.cpython-36.pyc
│   │           │   │   ├── monkey.cpython-36.pyc
│   │           │   │   ├── msvc.cpython-36.pyc
│   │           │   │   ├── namespaces.cpython-36.pyc
│   │           │   │   ├── package_index.cpython-36.pyc
│   │           │   │   ├── pep425tags.cpython-36.pyc
│   │           │   │   ├── py27compat.cpython-36.pyc
│   │           │   │   ├── py31compat.cpython-36.pyc
│   │           │   │   ├── py33compat.cpython-36.pyc
│   │           │   │   ├── py36compat.cpython-36.pyc
│   │           │   │   ├── sandbox.cpython-36.pyc
│   │           │   │   ├── site-patch.cpython-36.pyc
│   │           │   │   ├── ssl_support.cpython-36.pyc
│   │           │   │   ├── unicode_utils.cpython-36.pyc
│   │           │   │   ├── version.cpython-36.pyc
│   │           │   │   ├── wheel.cpython-36.pyc
│   │           │   │   └── windows_support.cpython-36.pyc
│   │           │   ├── sandbox.py
│   │           │   ├── script (dev).tmpl
│   │           │   ├── script.tmpl
│   │           │   ├── site-patch.py
│   │           │   ├── ssl_support.py
│   │           │   ├── unicode_utils.py
│   │           │   ├── _vendor
│   │           │   │   ├── __init__.py
│   │           │   │   ├── packaging
│   │           │   │   │   ├── __about__.py
│   │           │   │   │   ├── _compat.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── markers.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __about__.cpython-36.pyc
│   │           │   │   │   │   ├── _compat.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── markers.cpython-36.pyc
│   │           │   │   │   │   ├── requirements.cpython-36.pyc
│   │           │   │   │   │   ├── specifiers.cpython-36.pyc
│   │           │   │   │   │   ├── _structures.cpython-36.pyc
│   │           │   │   │   │   ├── utils.cpython-36.pyc
│   │           │   │   │   │   └── version.cpython-36.pyc
│   │           │   │   │   ├── requirements.py
│   │           │   │   │   ├── specifiers.py
│   │           │   │   │   ├── _structures.py
│   │           │   │   │   ├── utils.py
│   │           │   │   │   └── version.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── pyparsing.cpython-36.pyc
│   │           │   │   │   └── six.cpython-36.pyc
│   │           │   │   ├── pyparsing.py
│   │           │   │   └── six.py
│   │           │   ├── version.py
│   │           │   ├── wheel.py
│   │           │   └── windows_support.py
│   │           ├── setuptools-39.0.1.dist-info
│   │           │   ├── dependency_links.txt
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   ├── WHEEL
│   │           │   └── zip-safe
│   │           ├── six-1.12.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── six.py
│   │           ├── sympy
│   │           │   ├── abc.py
│   │           │   ├── algebras
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── quaternion.cpython-36.pyc
│   │           │   │   ├── quaternion.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   └── test_quaternion.cpython-36.pyc
│   │           │   │       └── test_quaternion.py
│   │           │   ├── assumptions
│   │           │   │   ├── ask_generated.py
│   │           │   │   ├── ask.py
│   │           │   │   ├── assume.py
│   │           │   │   ├── handlers
│   │           │   │   │   ├── calculus.py
│   │           │   │   │   ├── common.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── matrices.py
│   │           │   │   │   ├── ntheory.py
│   │           │   │   │   ├── order.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── calculus.cpython-36.pyc
│   │           │   │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── matrices.cpython-36.pyc
│   │           │   │   │   │   ├── ntheory.cpython-36.pyc
│   │           │   │   │   │   ├── order.cpython-36.pyc
│   │           │   │   │   │   └── sets.cpython-36.pyc
│   │           │   │   │   └── sets.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── ask.cpython-36.pyc
│   │           │   │   │   ├── ask_generated.cpython-36.pyc
│   │           │   │   │   ├── assume.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── refine.cpython-36.pyc
│   │           │   │   │   ├── satask.cpython-36.pyc
│   │           │   │   │   └── sathandlers.cpython-36.pyc
│   │           │   │   ├── refine.py
│   │           │   │   ├── satask.py
│   │           │   │   ├── sathandlers.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_assumptions_2.cpython-36.pyc
│   │           │   │       │   ├── test_context.cpython-36.pyc
│   │           │   │       │   ├── test_matrices.cpython-36.pyc
│   │           │   │       │   ├── test_query.cpython-36.pyc
│   │           │   │       │   ├── test_refine.cpython-36.pyc
│   │           │   │       │   ├── test_satask.cpython-36.pyc
│   │           │   │       │   └── test_sathandlers.cpython-36.pyc
│   │           │   │       ├── test_assumptions_2.py
│   │           │   │       ├── test_context.py
│   │           │   │       ├── test_matrices.py
│   │           │   │       ├── test_query.py
│   │           │   │       ├── test_refine.py
│   │           │   │       ├── test_satask.py
│   │           │   │       └── test_sathandlers.py
│   │           │   ├── benchmarks
│   │           │   │   ├── bench_discrete_log.py
│   │           │   │   ├── bench_meijerint.py
│   │           │   │   ├── bench_symbench.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── bench_discrete_log.cpython-36.pyc
│   │           │   │       ├── bench_meijerint.cpython-36.pyc
│   │           │   │       ├── bench_symbench.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── calculus
│   │           │   │   ├── euler.py
│   │           │   │   ├── finite_diff.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── euler.cpython-36.pyc
│   │           │   │   │   ├── finite_diff.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── singularities.cpython-36.pyc
│   │           │   │   │   └── util.cpython-36.pyc
│   │           │   │   ├── singularities.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_euler.cpython-36.pyc
│   │           │   │   │   │   ├── test_finite_diff.cpython-36.pyc
│   │           │   │   │   │   ├── test_singularities.cpython-36.pyc
│   │           │   │   │   │   └── test_util.cpython-36.pyc
│   │           │   │   │   ├── test_euler.py
│   │           │   │   │   ├── test_finite_diff.py
│   │           │   │   │   ├── test_singularities.py
│   │           │   │   │   └── test_util.py
│   │           │   │   └── util.py
│   │           │   ├── categories
│   │           │   │   ├── baseclasses.py
│   │           │   │   ├── diagram_drawing.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── baseclasses.cpython-36.pyc
│   │           │   │   │   ├── diagram_drawing.cpython-36.pyc
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_baseclasses.cpython-36.pyc
│   │           │   │       │   └── test_drawing.cpython-36.pyc
│   │           │   │       ├── test_baseclasses.py
│   │           │   │       └── test_drawing.py
│   │           │   ├── codegen
│   │           │   │   ├── algorithms.py
│   │           │   │   ├── approximations.py
│   │           │   │   ├── array_utils.py
│   │           │   │   ├── ast.py
│   │           │   │   ├── cfunctions.py
│   │           │   │   ├── cnodes.py
│   │           │   │   ├── cutils.py
│   │           │   │   ├── cxxnodes.py
│   │           │   │   ├── fnodes.py
│   │           │   │   ├── futils.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── algorithms.cpython-36.pyc
│   │           │   │   │   ├── approximations.cpython-36.pyc
│   │           │   │   │   ├── array_utils.cpython-36.pyc
│   │           │   │   │   ├── ast.cpython-36.pyc
│   │           │   │   │   ├── cfunctions.cpython-36.pyc
│   │           │   │   │   ├── cnodes.cpython-36.pyc
│   │           │   │   │   ├── cutils.cpython-36.pyc
│   │           │   │   │   ├── cxxnodes.cpython-36.pyc
│   │           │   │   │   ├── fnodes.cpython-36.pyc
│   │           │   │   │   ├── futils.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── pyutils.cpython-36.pyc
│   │           │   │   │   └── rewriting.cpython-36.pyc
│   │           │   │   ├── pyutils.py
│   │           │   │   ├── rewriting.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_algorithms.cpython-36.pyc
│   │           │   │       │   ├── test_applications.cpython-36.pyc
│   │           │   │       │   ├── test_approximations.cpython-36.pyc
│   │           │   │       │   ├── test_array_utils.cpython-36.pyc
│   │           │   │       │   ├── test_ast.cpython-36.pyc
│   │           │   │       │   ├── test_cfunctions.cpython-36.pyc
│   │           │   │       │   ├── test_cnodes.cpython-36.pyc
│   │           │   │       │   ├── test_cxxnodes.cpython-36.pyc
│   │           │   │       │   ├── test_fnodes.cpython-36.pyc
│   │           │   │       │   └── test_rewriting.cpython-36.pyc
│   │           │   │       ├── test_algorithms.py
│   │           │   │       ├── test_applications.py
│   │           │   │       ├── test_approximations.py
│   │           │   │       ├── test_array_utils.py
│   │           │   │       ├── test_ast.py
│   │           │   │       ├── test_cfunctions.py
│   │           │   │       ├── test_cnodes.py
│   │           │   │       ├── test_cxxnodes.py
│   │           │   │       ├── test_fnodes.py
│   │           │   │       └── test_rewriting.py
│   │           │   ├── combinatorics
│   │           │   │   ├── coset_table.py
│   │           │   │   ├── fp_groups.py
│   │           │   │   ├── free_groups.py
│   │           │   │   ├── generators.py
│   │           │   │   ├── graycode.py
│   │           │   │   ├── group_constructs.py
│   │           │   │   ├── homomorphisms.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── named_groups.py
│   │           │   │   ├── partitions.py
│   │           │   │   ├── perm_groups.py
│   │           │   │   ├── permutations.py
│   │           │   │   ├── polyhedron.py
│   │           │   │   ├── prufer.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── coset_table.cpython-36.pyc
│   │           │   │   │   ├── fp_groups.cpython-36.pyc
│   │           │   │   │   ├── free_groups.cpython-36.pyc
│   │           │   │   │   ├── generators.cpython-36.pyc
│   │           │   │   │   ├── graycode.cpython-36.pyc
│   │           │   │   │   ├── group_constructs.cpython-36.pyc
│   │           │   │   │   ├── homomorphisms.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── named_groups.cpython-36.pyc
│   │           │   │   │   ├── partitions.cpython-36.pyc
│   │           │   │   │   ├── perm_groups.cpython-36.pyc
│   │           │   │   │   ├── permutations.cpython-36.pyc
│   │           │   │   │   ├── polyhedron.cpython-36.pyc
│   │           │   │   │   ├── prufer.cpython-36.pyc
│   │           │   │   │   ├── rewritingsystem.cpython-36.pyc
│   │           │   │   │   ├── rewritingsystem_fsm.cpython-36.pyc
│   │           │   │   │   ├── subsets.cpython-36.pyc
│   │           │   │   │   ├── tensor_can.cpython-36.pyc
│   │           │   │   │   ├── testutil.cpython-36.pyc
│   │           │   │   │   └── util.cpython-36.pyc
│   │           │   │   ├── rewritingsystem_fsm.py
│   │           │   │   ├── rewritingsystem.py
│   │           │   │   ├── subsets.py
│   │           │   │   ├── tensor_can.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_coset_table.cpython-36.pyc
│   │           │   │   │   │   ├── test_fp_groups.cpython-36.pyc
│   │           │   │   │   │   ├── test_free_groups.cpython-36.pyc
│   │           │   │   │   │   ├── test_generators.cpython-36.pyc
│   │           │   │   │   │   ├── test_graycode.cpython-36.pyc
│   │           │   │   │   │   ├── test_group_constructs.cpython-36.pyc
│   │           │   │   │   │   ├── test_homomorphisms.cpython-36.pyc
│   │           │   │   │   │   ├── test_named_groups.cpython-36.pyc
│   │           │   │   │   │   ├── test_partitions.cpython-36.pyc
│   │           │   │   │   │   ├── test_perm_groups.cpython-36.pyc
│   │           │   │   │   │   ├── test_permutations.cpython-36.pyc
│   │           │   │   │   │   ├── test_polyhedron.cpython-36.pyc
│   │           │   │   │   │   ├── test_prufer.cpython-36.pyc
│   │           │   │   │   │   ├── test_rewriting.cpython-36.pyc
│   │           │   │   │   │   ├── test_subsets.cpython-36.pyc
│   │           │   │   │   │   ├── test_tensor_can.cpython-36.pyc
│   │           │   │   │   │   ├── test_testutil.cpython-36.pyc
│   │           │   │   │   │   └── test_util.cpython-36.pyc
│   │           │   │   │   ├── test_coset_table.py
│   │           │   │   │   ├── test_fp_groups.py
│   │           │   │   │   ├── test_free_groups.py
│   │           │   │   │   ├── test_generators.py
│   │           │   │   │   ├── test_graycode.py
│   │           │   │   │   ├── test_group_constructs.py
│   │           │   │   │   ├── test_homomorphisms.py
│   │           │   │   │   ├── test_named_groups.py
│   │           │   │   │   ├── test_partitions.py
│   │           │   │   │   ├── test_perm_groups.py
│   │           │   │   │   ├── test_permutations.py
│   │           │   │   │   ├── test_polyhedron.py
│   │           │   │   │   ├── test_prufer.py
│   │           │   │   │   ├── test_rewriting.py
│   │           │   │   │   ├── test_subsets.py
│   │           │   │   │   ├── test_tensor_can.py
│   │           │   │   │   ├── test_testutil.py
│   │           │   │   │   └── test_util.py
│   │           │   │   ├── testutil.py
│   │           │   │   └── util.py
│   │           │   ├── concrete
│   │           │   │   ├── delta.py
│   │           │   │   ├── expr_with_intlimits.py
│   │           │   │   ├── expr_with_limits.py
│   │           │   │   ├── gosper.py
│   │           │   │   ├── guess.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── products.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── delta.cpython-36.pyc
│   │           │   │   │   ├── expr_with_intlimits.cpython-36.pyc
│   │           │   │   │   ├── expr_with_limits.cpython-36.pyc
│   │           │   │   │   ├── gosper.cpython-36.pyc
│   │           │   │   │   ├── guess.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── products.cpython-36.pyc
│   │           │   │   │   └── summations.cpython-36.pyc
│   │           │   │   ├── summations.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_delta.cpython-36.pyc
│   │           │   │       │   ├── test_gosper.cpython-36.pyc
│   │           │   │       │   ├── test_guess.cpython-36.pyc
│   │           │   │       │   ├── test_products.cpython-36.pyc
│   │           │   │       │   └── test_sums_products.cpython-36.pyc
│   │           │   │       ├── test_delta.py
│   │           │   │       ├── test_gosper.py
│   │           │   │       ├── test_guess.py
│   │           │   │       ├── test_products.py
│   │           │   │       └── test_sums_products.py
│   │           │   ├── conftest.py
│   │           │   ├── core
│   │           │   │   ├── add.py
│   │           │   │   ├── alphabets.py
│   │           │   │   ├── assumptions.py
│   │           │   │   ├── backend.py
│   │           │   │   ├── basic.py
│   │           │   │   ├── benchmarks
│   │           │   │   │   ├── bench_arit.py
│   │           │   │   │   ├── bench_assumptions.py
│   │           │   │   │   ├── bench_basic.py
│   │           │   │   │   ├── bench_expand.py
│   │           │   │   │   ├── bench_numbers.py
│   │           │   │   │   ├── bench_sympify.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── bench_arit.cpython-36.pyc
│   │           │   │   │       ├── bench_assumptions.cpython-36.pyc
│   │           │   │   │       ├── bench_basic.cpython-36.pyc
│   │           │   │   │       ├── bench_expand.cpython-36.pyc
│   │           │   │   │       ├── bench_numbers.cpython-36.pyc
│   │           │   │   │       ├── bench_sympify.cpython-36.pyc
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   ├── cache.py
│   │           │   │   ├── compatibility.py
│   │           │   │   ├── containers.py
│   │           │   │   ├── coreerrors.py
│   │           │   │   ├── core.py
│   │           │   │   ├── decorators.py
│   │           │   │   ├── evalf.py
│   │           │   │   ├── evaluate.py
│   │           │   │   ├── expr.py
│   │           │   │   ├── exprtools.py
│   │           │   │   ├── facts.py
│   │           │   │   ├── function.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── logic.py
│   │           │   │   ├── mod.py
│   │           │   │   ├── mul.py
│   │           │   │   ├── multidimensional.py
│   │           │   │   ├── numbers.py
│   │           │   │   ├── operations.py
│   │           │   │   ├── power.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── add.cpython-36.pyc
│   │           │   │   │   ├── alphabets.cpython-36.pyc
│   │           │   │   │   ├── assumptions.cpython-36.pyc
│   │           │   │   │   ├── backend.cpython-36.pyc
│   │           │   │   │   ├── basic.cpython-36.pyc
│   │           │   │   │   ├── cache.cpython-36.pyc
│   │           │   │   │   ├── compatibility.cpython-36.pyc
│   │           │   │   │   ├── containers.cpython-36.pyc
│   │           │   │   │   ├── core.cpython-36.pyc
│   │           │   │   │   ├── coreerrors.cpython-36.pyc
│   │           │   │   │   ├── decorators.cpython-36.pyc
│   │           │   │   │   ├── evalf.cpython-36.pyc
│   │           │   │   │   ├── evaluate.cpython-36.pyc
│   │           │   │   │   ├── expr.cpython-36.pyc
│   │           │   │   │   ├── exprtools.cpython-36.pyc
│   │           │   │   │   ├── facts.cpython-36.pyc
│   │           │   │   │   ├── function.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── logic.cpython-36.pyc
│   │           │   │   │   ├── mod.cpython-36.pyc
│   │           │   │   │   ├── mul.cpython-36.pyc
│   │           │   │   │   ├── multidimensional.cpython-36.pyc
│   │           │   │   │   ├── numbers.cpython-36.pyc
│   │           │   │   │   ├── operations.cpython-36.pyc
│   │           │   │   │   ├── power.cpython-36.pyc
│   │           │   │   │   ├── relational.cpython-36.pyc
│   │           │   │   │   ├── rules.cpython-36.pyc
│   │           │   │   │   ├── singleton.cpython-36.pyc
│   │           │   │   │   ├── symbol.cpython-36.pyc
│   │           │   │   │   ├── sympify.cpython-36.pyc
│   │           │   │   │   └── trace.cpython-36.pyc
│   │           │   │   ├── relational.py
│   │           │   │   ├── rules.py
│   │           │   │   ├── singleton.py
│   │           │   │   ├── symbol.py
│   │           │   │   ├── sympify.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_args.cpython-36.pyc
│   │           │   │   │   │   ├── test_arit.cpython-36.pyc
│   │           │   │   │   │   ├── test_assumptions.cpython-36.pyc
│   │           │   │   │   │   ├── test_basic.cpython-36.pyc
│   │           │   │   │   │   ├── test_cache.cpython-36.pyc
│   │           │   │   │   │   ├── test_compatibility.cpython-36.pyc
│   │           │   │   │   │   ├── test_complex.cpython-36.pyc
│   │           │   │   │   │   ├── test_constructor_postprocessor.cpython-36.pyc
│   │           │   │   │   │   ├── test_containers.cpython-36.pyc
│   │           │   │   │   │   ├── test_count_ops.cpython-36.pyc
│   │           │   │   │   │   ├── test_diff.cpython-36.pyc
│   │           │   │   │   │   ├── test_equal.cpython-36.pyc
│   │           │   │   │   │   ├── test_eval.cpython-36.pyc
│   │           │   │   │   │   ├── test_evalf.cpython-36.pyc
│   │           │   │   │   │   ├── test_evaluate.cpython-36.pyc
│   │           │   │   │   │   ├── test_expand.cpython-36.pyc
│   │           │   │   │   │   ├── test_expr.cpython-36.pyc
│   │           │   │   │   │   ├── test_exprtools.cpython-36.pyc
│   │           │   │   │   │   ├── test_facts.cpython-36.pyc
│   │           │   │   │   │   ├── test_function.cpython-36.pyc
│   │           │   │   │   │   ├── test_logic.cpython-36.pyc
│   │           │   │   │   │   ├── test_match.cpython-36.pyc
│   │           │   │   │   │   ├── test_noncommutative.cpython-36.pyc
│   │           │   │   │   │   ├── test_numbers.cpython-36.pyc
│   │           │   │   │   │   ├── test_operations.cpython-36.pyc
│   │           │   │   │   │   ├── test_power.cpython-36.pyc
│   │           │   │   │   │   ├── test_priority.cpython-36.pyc
│   │           │   │   │   │   ├── test_relational.cpython-36.pyc
│   │           │   │   │   │   ├── test_rules.cpython-36.pyc
│   │           │   │   │   │   ├── test_singleton.cpython-36.pyc
│   │           │   │   │   │   ├── test_subs.cpython-36.pyc
│   │           │   │   │   │   ├── test_symbol.cpython-36.pyc
│   │           │   │   │   │   ├── test_sympify.cpython-36.pyc
│   │           │   │   │   │   ├── test_trace.cpython-36.pyc
│   │           │   │   │   │   ├── test_truediv.cpython-36.pyc
│   │           │   │   │   │   └── test_var.cpython-36.pyc
│   │           │   │   │   ├── test_args.py
│   │           │   │   │   ├── test_arit.py
│   │           │   │   │   ├── test_assumptions.py
│   │           │   │   │   ├── test_basic.py
│   │           │   │   │   ├── test_cache.py
│   │           │   │   │   ├── test_compatibility.py
│   │           │   │   │   ├── test_complex.py
│   │           │   │   │   ├── test_constructor_postprocessor.py
│   │           │   │   │   ├── test_containers.py
│   │           │   │   │   ├── test_count_ops.py
│   │           │   │   │   ├── test_diff.py
│   │           │   │   │   ├── test_equal.py
│   │           │   │   │   ├── test_evalf.py
│   │           │   │   │   ├── test_eval.py
│   │           │   │   │   ├── test_evaluate.py
│   │           │   │   │   ├── test_expand.py
│   │           │   │   │   ├── test_expr.py
│   │           │   │   │   ├── test_exprtools.py
│   │           │   │   │   ├── test_facts.py
│   │           │   │   │   ├── test_function.py
│   │           │   │   │   ├── test_logic.py
│   │           │   │   │   ├── test_match.py
│   │           │   │   │   ├── test_noncommutative.py
│   │           │   │   │   ├── test_numbers.py
│   │           │   │   │   ├── test_operations.py
│   │           │   │   │   ├── test_power.py
│   │           │   │   │   ├── test_priority.py
│   │           │   │   │   ├── test_relational.py
│   │           │   │   │   ├── test_rules.py
│   │           │   │   │   ├── test_singleton.py
│   │           │   │   │   ├── test_subs.py
│   │           │   │   │   ├── test_symbol.py
│   │           │   │   │   ├── test_sympify.py
│   │           │   │   │   ├── test_trace.py
│   │           │   │   │   ├── test_truediv.py
│   │           │   │   │   └── test_var.py
│   │           │   │   └── trace.py
│   │           │   ├── crypto
│   │           │   │   ├── crypto.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── crypto.cpython-36.pyc
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   └── test_crypto.cpython-36.pyc
│   │           │   │       └── test_crypto.py
│   │           │   ├── deprecated
│   │           │   │   ├── class_registry.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── class_registry.cpython-36.pyc
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   └── test_class_registry.cpython-36.pyc
│   │           │   │       └── test_class_registry.py
│   │           │   ├── diffgeom
│   │           │   │   ├── diffgeom.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── diffgeom.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── rn.cpython-36.pyc
│   │           │   │   ├── rn.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_class_structure.cpython-36.pyc
│   │           │   │       │   ├── test_diffgeom.cpython-36.pyc
│   │           │   │       │   ├── test_function_diffgeom_book.cpython-36.pyc
│   │           │   │       │   └── test_hyperbolic_space.cpython-36.pyc
│   │           │   │       ├── test_class_structure.py
│   │           │   │       ├── test_diffgeom.py
│   │           │   │       ├── test_function_diffgeom_book.py
│   │           │   │       └── test_hyperbolic_space.py
│   │           │   ├── discrete
│   │           │   │   ├── convolutions.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── convolutions.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── recurrences.cpython-36.pyc
│   │           │   │   │   └── transforms.cpython-36.pyc
│   │           │   │   ├── recurrences.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_convolutions.cpython-36.pyc
│   │           │   │   │   │   ├── test_recurrences.cpython-36.pyc
│   │           │   │   │   │   └── test_transforms.cpython-36.pyc
│   │           │   │   │   ├── test_convolutions.py
│   │           │   │   │   ├── test_recurrences.py
│   │           │   │   │   └── test_transforms.py
│   │           │   │   └── transforms.py
│   │           │   ├── external
│   │           │   │   ├── importtools.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── importtools.cpython-36.pyc
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_autowrap.cpython-36.pyc
│   │           │   │       │   ├── test_codegen.cpython-36.pyc
│   │           │   │       │   ├── test_importtools.cpython-36.pyc
│   │           │   │       │   ├── test_numpy.cpython-36.pyc
│   │           │   │       │   ├── test_sage.cpython-36.pyc
│   │           │   │       │   └── test_scipy.cpython-36.pyc
│   │           │   │       ├── test_autowrap.py
│   │           │   │       ├── test_codegen.py
│   │           │   │       ├── test_importtools.py
│   │           │   │       ├── test_numpy.py
│   │           │   │       ├── test_sage.py
│   │           │   │       └── test_scipy.py
│   │           │   ├── functions
│   │           │   │   ├── combinatorial
│   │           │   │   │   ├── factorials.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── numbers.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── factorials.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── numbers.cpython-36.pyc
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_comb_factorials.cpython-36.pyc
│   │           │   │   │       │   └── test_comb_numbers.cpython-36.pyc
│   │           │   │   │       ├── test_comb_factorials.py
│   │           │   │   │       └── test_comb_numbers.py
│   │           │   │   ├── elementary
│   │           │   │   │   ├── benchmarks
│   │           │   │   │   │   ├── bench_exp.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── __pycache__
│   │           │   │   │   │       ├── bench_exp.cpython-36.pyc
│   │           │   │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   │   ├── complexes.py
│   │           │   │   │   ├── exponential.py
│   │           │   │   │   ├── hyperbolic.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── integers.py
│   │           │   │   │   ├── miscellaneous.py
│   │           │   │   │   ├── piecewise.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── complexes.cpython-36.pyc
│   │           │   │   │   │   ├── exponential.cpython-36.pyc
│   │           │   │   │   │   ├── hyperbolic.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── integers.cpython-36.pyc
│   │           │   │   │   │   ├── miscellaneous.cpython-36.pyc
│   │           │   │   │   │   ├── piecewise.cpython-36.pyc
│   │           │   │   │   │   └── trigonometric.cpython-36.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_complexes.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_exponential.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_hyperbolic.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_integers.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_interface.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_miscellaneous.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_piecewise.cpython-36.pyc
│   │           │   │   │   │   │   └── test_trigonometric.cpython-36.pyc
│   │           │   │   │   │   ├── test_complexes.py
│   │           │   │   │   │   ├── test_exponential.py
│   │           │   │   │   │   ├── test_hyperbolic.py
│   │           │   │   │   │   ├── test_integers.py
│   │           │   │   │   │   ├── test_interface.py
│   │           │   │   │   │   ├── test_miscellaneous.py
│   │           │   │   │   │   ├── test_piecewise.py
│   │           │   │   │   │   └── test_trigonometric.py
│   │           │   │   │   └── trigonometric.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   └── special
│   │           │   │       ├── benchmarks
│   │           │   │       │   ├── bench_special.py
│   │           │   │       │   ├── __init__.py
│   │           │   │       │   └── __pycache__
│   │           │   │       │       ├── bench_special.cpython-36.pyc
│   │           │   │       │       └── __init__.cpython-36.pyc
│   │           │   │       ├── bessel.py
│   │           │   │       ├── beta_functions.py
│   │           │   │       ├── bsplines.py
│   │           │   │       ├── delta_functions.py
│   │           │   │       ├── elliptic_integrals.py
│   │           │   │       ├── error_functions.py
│   │           │   │       ├── gamma_functions.py
│   │           │   │       ├── hyper.py
│   │           │   │       ├── __init__.py
│   │           │   │       ├── mathieu_functions.py
│   │           │   │       ├── polynomials.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── bessel.cpython-36.pyc
│   │           │   │       │   ├── beta_functions.cpython-36.pyc
│   │           │   │       │   ├── bsplines.cpython-36.pyc
│   │           │   │       │   ├── delta_functions.cpython-36.pyc
│   │           │   │       │   ├── elliptic_integrals.cpython-36.pyc
│   │           │   │       │   ├── error_functions.cpython-36.pyc
│   │           │   │       │   ├── gamma_functions.cpython-36.pyc
│   │           │   │       │   ├── hyper.cpython-36.pyc
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── mathieu_functions.cpython-36.pyc
│   │           │   │       │   ├── polynomials.cpython-36.pyc
│   │           │   │       │   ├── singularity_functions.cpython-36.pyc
│   │           │   │       │   ├── spherical_harmonics.cpython-36.pyc
│   │           │   │       │   ├── tensor_functions.cpython-36.pyc
│   │           │   │       │   └── zeta_functions.cpython-36.pyc
│   │           │   │       ├── singularity_functions.py
│   │           │   │       ├── spherical_harmonics.py
│   │           │   │       ├── tensor_functions.py
│   │           │   │       ├── tests
│   │           │   │       │   ├── __init__.py
│   │           │   │       │   ├── __pycache__
│   │           │   │       │   │   ├── __init__.cpython-36.pyc
│   │           │   │       │   │   ├── test_bessel.cpython-36.pyc
│   │           │   │       │   │   ├── test_beta_functions.cpython-36.pyc
│   │           │   │       │   │   ├── test_bsplines.cpython-36.pyc
│   │           │   │       │   │   ├── test_delta_functions.cpython-36.pyc
│   │           │   │       │   │   ├── test_elliptic_integrals.cpython-36.pyc
│   │           │   │       │   │   ├── test_error_functions.cpython-36.pyc
│   │           │   │       │   │   ├── test_gamma_functions.cpython-36.pyc
│   │           │   │       │   │   ├── test_hyper.cpython-36.pyc
│   │           │   │       │   │   ├── test_mathieu.cpython-36.pyc
│   │           │   │       │   │   ├── test_singularity_functions.cpython-36.pyc
│   │           │   │       │   │   ├── test_spec_polynomials.cpython-36.pyc
│   │           │   │       │   │   ├── test_spherical_harmonics.cpython-36.pyc
│   │           │   │       │   │   ├── test_tensor_functions.cpython-36.pyc
│   │           │   │       │   │   └── test_zeta_functions.cpython-36.pyc
│   │           │   │       │   ├── test_bessel.py
│   │           │   │       │   ├── test_beta_functions.py
│   │           │   │       │   ├── test_bsplines.py
│   │           │   │       │   ├── test_delta_functions.py
│   │           │   │       │   ├── test_elliptic_integrals.py
│   │           │   │       │   ├── test_error_functions.py
│   │           │   │       │   ├── test_gamma_functions.py
│   │           │   │       │   ├── test_hyper.py
│   │           │   │       │   ├── test_mathieu.py
│   │           │   │       │   ├── test_singularity_functions.py
│   │           │   │       │   ├── test_spec_polynomials.py
│   │           │   │       │   ├── test_spherical_harmonics.py
│   │           │   │       │   ├── test_tensor_functions.py
│   │           │   │       │   └── test_zeta_functions.py
│   │           │   │       └── zeta_functions.py
│   │           │   ├── galgebra.py
│   │           │   ├── geometry
│   │           │   │   ├── curve.py
│   │           │   │   ├── ellipse.py
│   │           │   │   ├── entity.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── line.py
│   │           │   │   ├── parabola.py
│   │           │   │   ├── plane.py
│   │           │   │   ├── point.py
│   │           │   │   ├── polygon.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── curve.cpython-36.pyc
│   │           │   │   │   ├── ellipse.cpython-36.pyc
│   │           │   │   │   ├── entity.cpython-36.pyc
│   │           │   │   │   ├── exceptions.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── line.cpython-36.pyc
│   │           │   │   │   ├── parabola.cpython-36.pyc
│   │           │   │   │   ├── plane.cpython-36.pyc
│   │           │   │   │   ├── point.cpython-36.pyc
│   │           │   │   │   ├── polygon.cpython-36.pyc
│   │           │   │   │   └── util.cpython-36.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_curve.cpython-36.pyc
│   │           │   │   │   │   ├── test_ellipse.cpython-36.pyc
│   │           │   │   │   │   ├── test_entity.cpython-36.pyc
│   │           │   │   │   │   ├── test_geometrysets.cpython-36.pyc
│   │           │   │   │   │   ├── test_line.cpython-36.pyc
│   │           │   │   │   │   ├── test_parabola.cpython-36.pyc
│   │           │   │   │   │   ├── test_plane.cpython-36.pyc
│   │           │   │   │   │   ├── test_point.cpython-36.pyc
│   │           │   │   │   │   ├── test_polygon.cpython-36.pyc
│   │           │   │   │   │   └── test_util.cpython-36.pyc
│   │           │   │   │   ├── test_curve.py
│   │           │   │   │   ├── test_ellipse.py
│   │           │   │   │   ├── test_entity.py
│   │           │   │   │   ├── test_geometrysets.py
│   │           │   │   │   ├── test_line.py
│   │           │   │   │   ├── test_parabola.py
│   │           │   │   │   ├── test_plane.py
│   │           │   │   │   ├── test_point.py
│   │           │   │   │   ├── test_polygon.py
│   │           │   │   │   └── test_util.py
│   │           │   │   └── util.py
│   │           │   ├── holonomic
│   │           │   │   ├── holonomicerrors.py
│   │           │   │   ├── holonomic.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── linearsolver.py
│   │           │   │   ├── numerical.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── holonomic.cpython-36.pyc
│   │           │   │   │   ├── holonomicerrors.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── linearsolver.cpython-36.pyc
│   │           │   │   │   ├── numerical.cpython-36.pyc
│   │           │   │   │   └── recurrence.cpython-36.pyc
│   │           │   │   ├── recurrence.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_holonomic.cpython-36.pyc
│   │           │   │       │   └── test_recurrence.cpython-36.pyc
│   │           │   │       ├── test_holonomic.py
│   │           │   │       └── test_recurrence.py
│   │           │   ├── __init__.py
│   │           │   ├── integrals
│   │           │   │   ├── benchmarks
│   │           │   │   │   ├── bench_integrate.py
│   │           │   │   │   ├── bench_trigintegrate.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── bench_integrate.cpython-36.pyc
│   │           │   │   │       ├── bench_trigintegrate.cpython-36.pyc
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   ├── deltafunctions.py
│   │           │   │   ├── heurisch.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── integrals.py
│   │           │   │   ├── intpoly.py
│   │           │   │   ├── manualintegrate.py
│   │           │   │   ├── meijerint_doc.py
│   │           │   │   ├── meijerint.py
│   │           │   │   ├── prde.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── deltafunctions.cpython-36.pyc
│   │           │   │   │   ├── heurisch.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── integrals.cpython-36.pyc
│   │           │   │   │   ├── intpoly.cpython-36.pyc
│   │           │   │   │   ├── manualintegrate.cpython-36.pyc
│   │           │   │   │   ├── meijerint.cpython-36.pyc
│   │           │   │   │   ├── meijerint_doc.cpython-36.pyc
│   │           │   │   │   ├── prde.cpython-36.pyc
│   │           │   │   │   ├── quadrature.cpython-36.pyc
│   │           │   │   │   ├── rationaltools.cpython-36.pyc
│   │           │   │   │   ├── rde.cpython-36.pyc
│   │           │   │   │   ├── risch.cpython-36.pyc
│   │           │   │   │   ├── singularityfunctions.cpython-36.pyc
│   │           │   │   │   ├── transforms.cpython-36.pyc
│   │           │   │   │   └── trigonometry.cpython-36.pyc
│   │           │   │   ├── quadrature.py
│   │           │   │   ├── rationaltools.py
│   │           │   │   ├── rde.py
│   │           │   │   ├── risch.py
│   │           │   │   ├── rubi
│   │           │   │   │   ├── constraints.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── parsetools
│   │           │   │   │   │   ├── generate_rules.py
│   │           │   │   │   │   ├── generate_tests.py
│   │           │   │   │   │   ├── header.py.txt
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── parse.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── generate_rules.cpython-36.pyc
│   │           │   │   │   │   │   ├── generate_tests.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   └── parse.cpython-36.pyc
│   │           │   │   │   │   └── tests
│   │           │   │   │   │       ├── __init__.py
│   │           │   │   │   │       ├── __pycache__
│   │           │   │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │       │   └── test_parse.cpython-36.pyc
│   │           │   │   │   │       └── test_parse.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── constraints.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── rubi.cpython-36.pyc
│   │           │   │   │   │   ├── symbol.cpython-36.pyc
│   │           │   │   │   │   └── utility_function.cpython-36.pyc
│   │           │   │   │   ├── rubi.py
│   │           │   │   │   ├── rubi_tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   │   │   └── tests
│   │           │   │   │   │       ├── __init__.py
│   │           │   │   │   │       ├── __pycache__
│   │           │   │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │       │   ├── test_1_2.cpython-36.pyc
│   │           │   │   │   │       │   ├── test_1_3.cpython-36.pyc
│   │           │   │   │   │       │   ├── test_1_4.cpython-36.pyc
│   │           │   │   │   │       │   ├── test_exponential.cpython-36.pyc
│   │           │   │   │   │       │   ├── test_hyperbolic_sine.cpython-36.pyc
│   │           │   │   │   │       │   ├── test_inverse_hyperbolic_sine.cpython-36.pyc
│   │           │   │   │   │       │   ├── test_inverse_sine.cpython-36.pyc
│   │           │   │   │   │       │   ├── test_logarithms.cpython-36.pyc
│   │           │   │   │   │       │   ├── test_miscellaneous_algebra.cpython-36.pyc
│   │           │   │   │   │       │   ├── test_secant.cpython-36.pyc
│   │           │   │   │   │       │   ├── test_sine.cpython-36.pyc
│   │           │   │   │   │       │   ├── test_special_functions.cpython-36.pyc
│   │           │   │   │   │       │   ├── test_tangent.cpython-36.pyc
│   │           │   │   │   │       │   └── test_trinomials.cpython-36.pyc
│   │           │   │   │   │       ├── test_1_2.py
│   │           │   │   │   │       ├── test_1_3.py
│   │           │   │   │   │       ├── test_1_4.py
│   │           │   │   │   │       ├── test_exponential.py
│   │           │   │   │   │       ├── test_hyperbolic_sine.py
│   │           │   │   │   │       ├── test_inverse_hyperbolic_sine.py
│   │           │   │   │   │       ├── test_inverse_sine.py
│   │           │   │   │   │       ├── test_logarithms.py
│   │           │   │   │   │       ├── test_miscellaneous_algebra.py
│   │           │   │   │   │       ├── test_secant.py
│   │           │   │   │   │       ├── test_sine.py
│   │           │   │   │   │       ├── test_special_functions.py
│   │           │   │   │   │       ├── test_tangent.py
│   │           │   │   │   │       └── test_trinomials.py
│   │           │   │   │   ├── rules
│   │           │   │   │   │   ├── binomial_products.py
│   │           │   │   │   │   ├── exponential.py
│   │           │   │   │   │   ├── hyperbolic.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── integrand_simplification.py
│   │           │   │   │   │   ├── inverse_hyperbolic.py
│   │           │   │   │   │   ├── inverse_trig.py
│   │           │   │   │   │   ├── linear_products.py
│   │           │   │   │   │   ├── logarithms.py
│   │           │   │   │   │   ├── miscellaneous_algebraic.py
│   │           │   │   │   │   ├── miscellaneous_integration.py
│   │           │   │   │   │   ├── miscellaneous_trig.py
│   │           │   │   │   │   ├── piecewise_linear.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── binomial_products.cpython-36.pyc
│   │           │   │   │   │   │   ├── exponential.cpython-36.pyc
│   │           │   │   │   │   │   ├── hyperbolic.cpython-36.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── integrand_simplification.cpython-36.pyc
│   │           │   │   │   │   │   ├── inverse_hyperbolic.cpython-36.pyc
│   │           │   │   │   │   │   ├── inverse_trig.cpython-36.pyc
│   │           │   │   │   │   │   ├── linear_products.cpython-36.pyc
│   │           │   │   │   │   │   ├── logarithms.cpython-36.pyc
│   │           │   │   │   │   │   ├── miscellaneous_algebraic.cpython-36.pyc
│   │           │   │   │   │   │   ├── miscellaneous_integration.cpython-36.pyc
│   │           │   │   │   │   │   ├── miscellaneous_trig.cpython-36.pyc
│   │           │   │   │   │   │   ├── piecewise_linear.cpython-36.pyc
│   │           │   │   │   │   │   ├── quadratic_products.cpython-36.pyc
│   │           │   │   │   │   │   ├── secant.cpython-36.pyc
│   │           │   │   │   │   │   ├── sine.cpython-36.pyc
│   │           │   │   │   │   │   ├── special_functions.cpython-36.pyc
│   │           │   │   │   │   │   ├── tangent.cpython-36.pyc
│   │           │   │   │   │   │   └── trinomial_products.cpython-36.pyc
│   │           │   │   │   │   ├── quadratic_products.py
│   │           │   │   │   │   ├── secant.py
│   │           │   │   │   │   ├── sine.py
│   │           │   │   │   │   ├── special_functions.py
│   │           │   │   │   │   ├── tangent.py
│   │           │   │   │   │   └── trinomial_products.py
│   │           │   │   │   ├── symbol.py
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_rubi_integrate.cpython-36.pyc
│   │           │   │   │   │   │   └── test_utility_function.cpython-36.pyc
│   │           │   │   │   │   ├── test_rubi_integrate.py
│   │           │   │   │   │   └── test_utility_function.py
│   │           │   │   │   └── utility_function.py
│   │           │   │   ├── singularityfunctions.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_deltafunctions.cpython-36.pyc
│   │           │   │   │   │   ├── test_failing_integrals.cpython-36.pyc
│   │           │   │   │   │   ├── test_heurisch.cpython-36.pyc
│   │           │   │   │   │   ├── test_integrals.cpython-36.pyc
│   │           │   │   │   │   ├── test_intpoly.cpython-36.pyc
│   │           │   │   │   │   ├── test_lineintegrals.cpython-36.pyc
│   │           │   │   │   │   ├── test_manual.cpython-36.pyc
│   │           │   │   │   │   ├── test_meijerint.cpython-36.pyc
│   │           │   │   │   │   ├── test_prde.cpython-36.pyc
│   │           │   │   │   │   ├── test_quadrature.cpython-36.pyc
│   │           │   │   │   │   ├── test_rationaltools.cpython-36.pyc
│   │           │   │   │   │   ├── test_rde.cpython-36.pyc
│   │           │   │   │   │   ├── test_risch.cpython-36.pyc
│   │           │   │   │   │   ├── test_singularityfunctions.cpython-36.pyc
│   │           │   │   │   │   ├── test_transforms.cpython-36.pyc
│   │           │   │   │   │   └── test_trigonometry.cpython-36.pyc
│   │           │   │   │   ├── test_deltafunctions.py
│   │           │   │   │   ├── test_failing_integrals.py
│   │           │   │   │   ├── test_heurisch.py
│   │           │   │   │   ├── test_integrals.py
│   │           │   │   │   ├── test_intpoly.py
│   │           │   │   │   ├── test_lineintegrals.py
│   │           │   │   │   ├── test_manual.py
│   │           │   │   │   ├── test_meijerint.py
│   │           │   │   │   ├── test_prde.py
│   │           │   │   │   ├── test_quadrature.py
│   │           │   │   │   ├── test_rationaltools.py
│   │           │   │   │   ├── test_rde.py
│   │           │   │   │   ├── test_risch.py
│   │           │   │   │   ├── test_singularityfunctions.py
│   │           │   │   │   ├── test_transforms.py
│   │           │   │   │   └── test_trigonometry.py
│   │           │   │   ├── transforms.py
│   │           │   │   └── trigonometry.py
│   │           │   ├── interactive
│   │           │   │   ├── __init__.py
│   │           │   │   ├── ipythonprinting.py
│   │           │   │   ├── printing.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── ipythonprinting.cpython-36.pyc
│   │           │   │   │   ├── printing.cpython-36.pyc
│   │           │   │   │   └── session.cpython-36.pyc
│   │           │   │   ├── session.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_interactive.cpython-36.pyc
│   │           │   │       │   ├── test_ipython.cpython-36.pyc
│   │           │   │       │   └── test_ipythonprinting.cpython-36.pyc
│   │           │   │       ├── test_interactive.py
│   │           │   │       ├── test_ipythonprinting.py
│   │           │   │       └── test_ipython.py
│   │           │   ├── liealgebras
│   │           │   │   ├── cartan_matrix.py
│   │           │   │   ├── cartan_type.py
│   │           │   │   ├── dynkin_diagram.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── cartan_matrix.cpython-36.pyc
│   │           │   │   │   ├── cartan_type.cpython-36.pyc
│   │           │   │   │   ├── dynkin_diagram.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── root_system.cpython-36.pyc
│   │           │   │   │   ├── type_a.cpython-36.pyc
│   │           │   │   │   ├── type_b.cpython-36.pyc
│   │           │   │   │   ├── type_c.cpython-36.pyc
│   │           │   │   │   ├── type_d.cpython-36.pyc
│   │           │   │   │   ├── type_e.cpython-36.pyc
│   │           │   │   │   ├── type_f.cpython-36.pyc
│   │           │   │   │   ├── type_g.cpython-36.pyc
│   │           │   │   │   └── weyl_group.cpython-36.pyc
│   │           │   │   ├── root_system.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_cartan_matrix.cpython-36.pyc
│   │           │   │   │   │   ├── test_cartan_type.cpython-36.pyc
│   │           │   │   │   │   ├── test_dynkin_diagram.cpython-36.pyc
│   │           │   │   │   │   ├── test_root_system.cpython-36.pyc
│   │           │   │   │   │   ├── test_type_A.cpython-36.pyc
│   │           │   │   │   │   ├── test_type_B.cpython-36.pyc
│   │           │   │   │   │   ├── test_type_C.cpython-36.pyc
│   │           │   │   │   │   ├── test_type_D.cpython-36.pyc
│   │           │   │   │   │   ├── test_type_E.cpython-36.pyc
│   │           │   │   │   │   ├── test_type_F.cpython-36.pyc
│   │           │   │   │   │   ├── test_type_G.cpython-36.pyc
│   │           │   │   │   │   └── test_weyl_group.cpython-36.pyc
│   │           │   │   │   ├── test_cartan_matrix.py
│   │           │   │   │   ├── test_cartan_type.py
│   │           │   │   │   ├── test_dynkin_diagram.py
│   │           │   │   │   ├── test_root_system.py
│   │           │   │   │   ├── test_type_A.py
│   │           │   │   │   ├── test_type_B.py
│   │           │   │   │   ├── test_type_C.py
│   │           │   │   │   ├── test_type_D.py
│   │           │   │   │   ├── test_type_E.py
│   │           │   │   │   ├── test_type_F.py
│   │           │   │   │   ├── test_type_G.py
│   │           │   │   │   └── test_weyl_group.py
│   │           │   │   ├── type_a.py
│   │           │   │   ├── type_b.py
│   │           │   │   ├── type_c.py
│   │           │   │   ├── type_d.py
│   │           │   │   ├── type_e.py
│   │           │   │   ├── type_f.py
│   │           │   │   ├── type_g.py
│   │           │   │   └── weyl_group.py
│   │           │   ├── logic
│   │           │   │   ├── algorithms
│   │           │   │   │   ├── dpll2.py
│   │           │   │   │   ├── dpll.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── dpll2.cpython-36.pyc
│   │           │   │   │       ├── dpll.cpython-36.pyc
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   ├── boolalg.py
│   │           │   │   ├── inference.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── boolalg.cpython-36.pyc
│   │           │   │   │   ├── inference.cpython-36.pyc
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_boolalg.cpython-36.pyc
│   │           │   │   │   │   ├── test_dimacs.cpython-36.pyc
│   │           │   │   │   │   └── test_inference.cpython-36.pyc
│   │           │   │   │   ├── test_boolalg.py
│   │           │   │   │   ├── test_dimacs.py
│   │           │   │   │   └── test_inference.py
│   │           │   │   └── utilities
│   │           │   │       ├── dimacs.py
│   │           │   │       ├── __init__.py
│   │           │   │       └── __pycache__
│   │           │   │           ├── dimacs.cpython-36.pyc
│   │           │   │           └── __init__.cpython-36.pyc
│   │           │   ├── matrices
│   │           │   │   ├── benchmarks
│   │           │   │   │   ├── bench_matrix.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── bench_matrix.cpython-36.pyc
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   ├── common.py
│   │           │   │   ├── densearith.py
│   │           │   │   ├── dense.py
│   │           │   │   ├── densesolve.py
│   │           │   │   ├── densetools.py
│   │           │   │   ├── expressions
│   │           │   │   │   ├── adjoint.py
│   │           │   │   │   ├── applyfunc.py
│   │           │   │   │   ├── blockmatrix.py
│   │           │   │   │   ├── determinant.py
│   │           │   │   │   ├── diagonal.py
│   │           │   │   │   ├── dotproduct.py
│   │           │   │   │   ├── factorizations.py
│   │           │   │   │   ├── fourier.py
│   │           │   │   │   ├── funcmatrix.py
│   │           │   │   │   ├── hadamard.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── inverse.py
│   │           │   │   │   ├── kronecker.py
│   │           │   │   │   ├── matadd.py
│   │           │   │   │   ├── matexpr.py
│   │           │   │   │   ├── matmul.py
│   │           │   │   │   ├── matpow.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── adjoint.cpython-36.pyc
│   │           │   │   │   │   ├── applyfunc.cpython-36.pyc
│   │           │   │   │   │   ├── blockmatrix.cpython-36.pyc
│   │           │   │   │   │   ├── determinant.cpython-36.pyc
│   │           │   │   │   │   ├── diagonal.cpython-36.pyc
│   │           │   │   │   │   ├── dotproduct.cpython-36.pyc
│   │           │   │   │   │   ├── factorizations.cpython-36.pyc
│   │           │   │   │   │   ├── fourier.cpython-36.pyc
│   │           │   │   │   │   ├── funcmatrix.cpython-36.pyc
│   │           │   │   │   │   ├── hadamard.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── inverse.cpython-36.pyc
│   │           │   │   │   │   ├── kronecker.cpython-36.pyc
│   │           │   │   │   │   ├── matadd.cpython-36.pyc
│   │           │   │   │   │   ├── matexpr.cpython-36.pyc
│   │           │   │   │   │   ├── matmul.cpython-36.pyc
│   │           │   │   │   │   ├── matpow.cpython-36.pyc
│   │           │   │   │   │   ├── slice.cpython-36.pyc
│   │           │   │   │   │   ├── trace.cpython-36.pyc
│   │           │   │   │   │   └── transpose.cpython-36.pyc
│   │           │   │   │   ├── slice.py
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_adjoint.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_applyfunc.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_blockmatrix.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_derivatives.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_determinant.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_diagonal.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_dotproduct.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_factorizations.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_fourier.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_funcmatrix.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_hadamard.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_indexing.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_inverse.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_kronecker.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_matadd.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_matexpr.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_matmul.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_matpow.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_slice.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_trace.cpython-36.pyc
│   │           │   │   │   │   │   └── test_transpose.cpython-36.pyc
│   │           │   │   │   │   ├── test_adjoint.py
│   │           │   │   │   │   ├── test_applyfunc.py
│   │           │   │   │   │   ├── test_blockmatrix.py
│   │           │   │   │   │   ├── test_derivatives.py
│   │           │   │   │   │   ├── test_determinant.py
│   │           │   │   │   │   ├── test_diagonal.py
│   │           │   │   │   │   ├── test_dotproduct.py
│   │           │   │   │   │   ├── test_factorizations.py
│   │           │   │   │   │   ├── test_fourier.py
│   │           │   │   │   │   ├── test_funcmatrix.py
│   │           │   │   │   │   ├── test_hadamard.py
│   │           │   │   │   │   ├── test_indexing.py
│   │           │   │   │   │   ├── test_inverse.py
│   │           │   │   │   │   ├── test_kronecker.py
│   │           │   │   │   │   ├── test_matadd.py
│   │           │   │   │   │   ├── test_matexpr.py
│   │           │   │   │   │   ├── test_matmul.py
│   │           │   │   │   │   ├── test_matpow.py
│   │           │   │   │   │   ├── test_slice.py
│   │           │   │   │   │   ├── test_trace.py
│   │           │   │   │   │   └── test_transpose.py
│   │           │   │   │   ├── trace.py
│   │           │   │   │   └── transpose.py
│   │           │   │   ├── immutable.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── matrices.py
│   │           │   │   ├── normalforms.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── common.cpython-36.pyc
│   │           │   │   │   ├── densearith.cpython-36.pyc
│   │           │   │   │   ├── dense.cpython-36.pyc
│   │           │   │   │   ├── densesolve.cpython-36.pyc
│   │           │   │   │   ├── densetools.cpython-36.pyc
│   │           │   │   │   ├── immutable.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── matrices.cpython-36.pyc
│   │           │   │   │   ├── normalforms.cpython-36.pyc
│   │           │   │   │   ├── sparse.cpython-36.pyc
│   │           │   │   │   └── sparsetools.cpython-36.pyc
│   │           │   │   ├── sparse.py
│   │           │   │   ├── sparsetools.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_commonmatrix.cpython-36.pyc
│   │           │   │       │   ├── test_densearith.cpython-36.pyc
│   │           │   │       │   ├── test_densesolve.cpython-36.pyc
│   │           │   │       │   ├── test_densetools.cpython-36.pyc
│   │           │   │       │   ├── test_immutable.cpython-36.pyc
│   │           │   │       │   ├── test_interactions.cpython-36.pyc
│   │           │   │       │   ├── test_matrices.cpython-36.pyc
│   │           │   │       │   ├── test_normalforms.cpython-36.pyc
│   │           │   │       │   ├── test_sparse.cpython-36.pyc
│   │           │   │       │   └── test_sparsetools.cpython-36.pyc
│   │           │   │       ├── test_commonmatrix.py
│   │           │   │       ├── test_densearith.py
│   │           │   │       ├── test_densesolve.py
│   │           │   │       ├── test_densetools.py
│   │           │   │       ├── test_immutable.py
│   │           │   │       ├── test_interactions.py
│   │           │   │       ├── test_matrices.py
│   │           │   │       ├── test_normalforms.py
│   │           │   │       ├── test_sparse.py
│   │           │   │       └── test_sparsetools.py
│   │           │   ├── multipledispatch
│   │           │   │   ├── conflict.py
│   │           │   │   ├── core.py
│   │           │   │   ├── dispatcher.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── conflict.cpython-36.pyc
│   │           │   │   │   ├── core.cpython-36.pyc
│   │           │   │   │   ├── dispatcher.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── utils.cpython-36.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_conflict.cpython-36.pyc
│   │           │   │   │   │   ├── test_core.cpython-36.pyc
│   │           │   │   │   │   └── test_dispatcher.cpython-36.pyc
│   │           │   │   │   ├── test_conflict.py
│   │           │   │   │   ├── test_core.py
│   │           │   │   │   └── test_dispatcher.py
│   │           │   │   └── utils.py
│   │           │   ├── ntheory
│   │           │   │   ├── bbp_pi.py
│   │           │   │   ├── continued_fraction.py
│   │           │   │   ├── egyptian_fraction.py
│   │           │   │   ├── factor_.py
│   │           │   │   ├── generate.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── modular.py
│   │           │   │   ├── multinomial.py
│   │           │   │   ├── partitions_.py
│   │           │   │   ├── primetest.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── bbp_pi.cpython-36.pyc
│   │           │   │   │   ├── continued_fraction.cpython-36.pyc
│   │           │   │   │   ├── egyptian_fraction.cpython-36.pyc
│   │           │   │   │   ├── factor_.cpython-36.pyc
│   │           │   │   │   ├── generate.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── modular.cpython-36.pyc
│   │           │   │   │   ├── multinomial.cpython-36.pyc
│   │           │   │   │   ├── partitions_.cpython-36.pyc
│   │           │   │   │   ├── primetest.cpython-36.pyc
│   │           │   │   │   └── residue_ntheory.cpython-36.pyc
│   │           │   │   ├── residue_ntheory.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_bbp_pi.cpython-36.pyc
│   │           │   │       │   ├── test_continued_fraction.cpython-36.pyc
│   │           │   │       │   ├── test_egyptian_fraction.cpython-36.pyc
│   │           │   │       │   ├── test_factor_.cpython-36.pyc
│   │           │   │       │   ├── test_generate.cpython-36.pyc
│   │           │   │       │   ├── test_modular.cpython-36.pyc
│   │           │   │       │   ├── test_multinomial.cpython-36.pyc
│   │           │   │       │   ├── test_partitions.cpython-36.pyc
│   │           │   │       │   ├── test_primetest.cpython-36.pyc
│   │           │   │       │   └── test_residue.cpython-36.pyc
│   │           │   │       ├── test_bbp_pi.py
│   │           │   │       ├── test_continued_fraction.py
│   │           │   │       ├── test_egyptian_fraction.py
│   │           │   │       ├── test_factor_.py
│   │           │   │       ├── test_generate.py
│   │           │   │       ├── test_modular.py
│   │           │   │       ├── test_multinomial.py
│   │           │   │       ├── test_partitions.py
│   │           │   │       ├── test_primetest.py
│   │           │   │       └── test_residue.py
│   │           │   ├── parsing
│   │           │   │   ├── ast_parser.py
│   │           │   │   ├── autolev
│   │           │   │   │   ├── _antlr
│   │           │   │   │   │   ├── autolevlexer.py
│   │           │   │   │   │   ├── autolevlistener.py
│   │           │   │   │   │   ├── autolevparser.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── __pycache__
│   │           │   │   │   │       ├── autolevlexer.cpython-36.pyc
│   │           │   │   │   │       ├── autolevlistener.cpython-36.pyc
│   │           │   │   │   │       ├── autolevparser.cpython-36.pyc
│   │           │   │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   │   ├── Autolev.g4
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _listener_autolev_antlr.py
│   │           │   │   │   ├── _parse_autolev_antlr.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── _listener_autolev_antlr.cpython-36.pyc
│   │           │   │   │   │   └── _parse_autolev_antlr.cpython-36.pyc
│   │           │   │   │   └── test-examples
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── ruletest10.cpython-36.pyc
│   │           │   │   │       │   ├── ruletest11.cpython-36.pyc
│   │           │   │   │       │   ├── ruletest12.cpython-36.pyc
│   │           │   │   │       │   ├── ruletest1.cpython-36.pyc
│   │           │   │   │       │   ├── ruletest2.cpython-36.pyc
│   │           │   │   │       │   ├── ruletest3.cpython-36.pyc
│   │           │   │   │       │   ├── ruletest4.cpython-36.pyc
│   │           │   │   │       │   ├── ruletest5.cpython-36.pyc
│   │           │   │   │       │   ├── ruletest6.cpython-36.pyc
│   │           │   │   │       │   ├── ruletest7.cpython-36.pyc
│   │           │   │   │       │   ├── ruletest8.cpython-36.pyc
│   │           │   │   │       │   └── ruletest9.cpython-36.pyc
│   │           │   │   │       ├── pydy-example-repo
│   │           │   │   │       │   ├── chaos_pendulum.al
│   │           │   │   │       │   ├── chaos_pendulum.py
│   │           │   │   │       │   ├── double_pendulum.al
│   │           │   │   │       │   ├── double_pendulum.py
│   │           │   │   │       │   ├── __init__.py
│   │           │   │   │       │   ├── mass_spring_damper.al
│   │           │   │   │       │   ├── mass_spring_damper.py
│   │           │   │   │       │   ├── non_min_pendulum.al
│   │           │   │   │       │   ├── non_min_pendulum.py
│   │           │   │   │       │   └── __pycache__
│   │           │   │   │       │       ├── chaos_pendulum.cpython-36.pyc
│   │           │   │   │       │       ├── double_pendulum.cpython-36.pyc
│   │           │   │   │       │       ├── __init__.cpython-36.pyc
│   │           │   │   │       │       ├── mass_spring_damper.cpython-36.pyc
│   │           │   │   │       │       └── non_min_pendulum.cpython-36.pyc
│   │           │   │   │       ├── ruletest10.al
│   │           │   │   │       ├── ruletest10.py
│   │           │   │   │       ├── ruletest11.al
│   │           │   │   │       ├── ruletest11.py
│   │           │   │   │       ├── ruletest12.al
│   │           │   │   │       ├── ruletest12.py
│   │           │   │   │       ├── ruletest1.al
│   │           │   │   │       ├── ruletest1.py
│   │           │   │   │       ├── ruletest2.al
│   │           │   │   │       ├── ruletest2.py
│   │           │   │   │       ├── ruletest3.al
│   │           │   │   │       ├── ruletest3.py
│   │           │   │   │       ├── ruletest4.al
│   │           │   │   │       ├── ruletest4.py
│   │           │   │   │       ├── ruletest5.al
│   │           │   │   │       ├── ruletest5.py
│   │           │   │   │       ├── ruletest6.al
│   │           │   │   │       ├── ruletest6.py
│   │           │   │   │       ├── ruletest7.al
│   │           │   │   │       ├── ruletest7.py
│   │           │   │   │       ├── ruletest8.al
│   │           │   │   │       ├── ruletest8.py
│   │           │   │   │       ├── ruletest9.al
│   │           │   │   │       └── ruletest9.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── latex
│   │           │   │   │   ├── _antlr
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── latexlexer.py
│   │           │   │   │   │   ├── latexparser.py
│   │           │   │   │   │   └── __pycache__
│   │           │   │   │   │       ├── __init__.cpython-36.pyc
│   │           │   │   │   │       ├── latexlexer.cpython-36.pyc
│   │           │   │   │   │       └── latexparser.cpython-36.pyc
│   │           │   │   │   ├── _build_latex_antlr.py
│   │           │   │   │   ├── errors.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── LaTeX.g4
│   │           │   │   │   ├── LICENSE.txt
│   │           │   │   │   ├── _parse_latex_antlr.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── _build_latex_antlr.cpython-36.pyc
│   │           │   │   │       ├── errors.cpython-36.pyc
│   │           │   │   │       ├── __init__.cpython-36.pyc
│   │           │   │   │       └── _parse_latex_antlr.cpython-36.pyc
│   │           │   │   ├── mathematica.py
│   │           │   │   ├── maxima.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── ast_parser.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── mathematica.cpython-36.pyc
│   │           │   │   │   ├── maxima.cpython-36.pyc
│   │           │   │   │   └── sympy_parser.cpython-36.pyc
│   │           │   │   ├── sympy_parser.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_autolev.cpython-36.pyc
│   │           │   │       │   ├── test_implicit_multiplication_application.cpython-36.pyc
│   │           │   │       │   ├── test_latex.cpython-36.pyc
│   │           │   │       │   ├── test_latex_deps.cpython-36.pyc
│   │           │   │       │   ├── test_mathematica.cpython-36.pyc
│   │           │   │       │   ├── test_maxima.cpython-36.pyc
│   │           │   │       │   └── test_sympy_parser.cpython-36.pyc
│   │           │   │       ├── test_autolev.py
│   │           │   │       ├── test_implicit_multiplication_application.py
│   │           │   │       ├── test_latex_deps.py
│   │           │   │       ├── test_latex.py
│   │           │   │       ├── test_mathematica.py
│   │           │   │       ├── test_maxima.py
│   │           │   │       └── test_sympy_parser.py
│   │           │   ├── physics
│   │           │   │   ├── continuum_mechanics
│   │           │   │   │   ├── beam.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── beam.cpython-36.pyc
│   │           │   │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   └── test_beam.cpython-36.pyc
│   │           │   │   │       └── test_beam.py
│   │           │   │   ├── gaussopt.py
│   │           │   │   ├── hep
│   │           │   │   │   ├── gamma_matrices.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── gamma_matrices.cpython-36.pyc
│   │           │   │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   └── test_gamma_matrices.cpython-36.pyc
│   │           │   │   │       └── test_gamma_matrices.py
│   │           │   │   ├── hydrogen.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── matrices.py
│   │           │   │   ├── mechanics
│   │           │   │   │   ├── body.py
│   │           │   │   │   ├── functions.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── kane.py
│   │           │   │   │   ├── lagrange.py
│   │           │   │   │   ├── linearize.py
│   │           │   │   │   ├── models.py
│   │           │   │   │   ├── particle.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── body.cpython-36.pyc
│   │           │   │   │   │   ├── functions.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── kane.cpython-36.pyc
│   │           │   │   │   │   ├── lagrange.cpython-36.pyc
│   │           │   │   │   │   ├── linearize.cpython-36.pyc
│   │           │   │   │   │   ├── models.cpython-36.pyc
│   │           │   │   │   │   ├── particle.cpython-36.pyc
│   │           │   │   │   │   ├── rigidbody.cpython-36.pyc
│   │           │   │   │   │   └── system.cpython-36.pyc
│   │           │   │   │   ├── rigidbody.py
│   │           │   │   │   ├── system.py
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_body.cpython-36.pyc
│   │           │   │   │       │   ├── test_functions.cpython-36.pyc
│   │           │   │   │       │   ├── test_kane2.cpython-36.pyc
│   │           │   │   │       │   ├── test_kane3.cpython-36.pyc
│   │           │   │   │       │   ├── test_kane.cpython-36.pyc
│   │           │   │   │       │   ├── test_lagrange2.cpython-36.pyc
│   │           │   │   │       │   ├── test_lagrange.cpython-36.pyc
│   │           │   │   │       │   ├── test_linearize.cpython-36.pyc
│   │           │   │   │       │   ├── test_models.cpython-36.pyc
│   │           │   │   │       │   ├── test_particle.cpython-36.pyc
│   │           │   │   │       │   ├── test_rigidbody.cpython-36.pyc
│   │           │   │   │       │   └── test_system.cpython-36.pyc
│   │           │   │   │       ├── test_body.py
│   │           │   │   │       ├── test_functions.py
│   │           │   │   │       ├── test_kane2.py
│   │           │   │   │       ├── test_kane3.py
│   │           │   │   │       ├── test_kane.py
│   │           │   │   │       ├── test_lagrange2.py
│   │           │   │   │       ├── test_lagrange.py
│   │           │   │   │       ├── test_linearize.py
│   │           │   │   │       ├── test_models.py
│   │           │   │   │       ├── test_particle.py
│   │           │   │   │       ├── test_rigidbody.py
│   │           │   │   │       └── test_system.py
│   │           │   │   ├── optics
│   │           │   │   │   ├── gaussopt.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── medium.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── gaussopt.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── medium.cpython-36.pyc
│   │           │   │   │   │   ├── utils.cpython-36.pyc
│   │           │   │   │   │   └── waves.cpython-36.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_gaussopt.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_medium.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_utils.cpython-36.pyc
│   │           │   │   │   │   │   └── test_waves.cpython-36.pyc
│   │           │   │   │   │   ├── test_gaussopt.py
│   │           │   │   │   │   ├── test_medium.py
│   │           │   │   │   │   ├── test_utils.py
│   │           │   │   │   │   └── test_waves.py
│   │           │   │   │   ├── utils.py
│   │           │   │   │   └── waves.py
│   │           │   │   ├── paulialgebra.py
│   │           │   │   ├── pring.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── gaussopt.cpython-36.pyc
│   │           │   │   │   ├── hydrogen.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── matrices.cpython-36.pyc
│   │           │   │   │   ├── paulialgebra.cpython-36.pyc
│   │           │   │   │   ├── pring.cpython-36.pyc
│   │           │   │   │   ├── qho_1d.cpython-36.pyc
│   │           │   │   │   ├── secondquant.cpython-36.pyc
│   │           │   │   │   ├── sho.cpython-36.pyc
│   │           │   │   │   └── wigner.cpython-36.pyc
│   │           │   │   ├── qho_1d.py
│   │           │   │   ├── quantum
│   │           │   │   │   ├── anticommutator.py
│   │           │   │   │   ├── boson.py
│   │           │   │   │   ├── cartesian.py
│   │           │   │   │   ├── cg.py
│   │           │   │   │   ├── circuitplot.py
│   │           │   │   │   ├── circuitutils.py
│   │           │   │   │   ├── commutator.py
│   │           │   │   │   ├── constants.py
│   │           │   │   │   ├── dagger.py
│   │           │   │   │   ├── density.py
│   │           │   │   │   ├── fermion.py
│   │           │   │   │   ├── gate.py
│   │           │   │   │   ├── grover.py
│   │           │   │   │   ├── hilbert.py
│   │           │   │   │   ├── identitysearch.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── innerproduct.py
│   │           │   │   │   ├── matrixcache.py
│   │           │   │   │   ├── matrixutils.py
│   │           │   │   │   ├── operatorordering.py
│   │           │   │   │   ├── operator.py
│   │           │   │   │   ├── operatorset.py
│   │           │   │   │   ├── pauli.py
│   │           │   │   │   ├── piab.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── anticommutator.cpython-36.pyc
│   │           │   │   │   │   ├── boson.cpython-36.pyc
│   │           │   │   │   │   ├── cartesian.cpython-36.pyc
│   │           │   │   │   │   ├── cg.cpython-36.pyc
│   │           │   │   │   │   ├── circuitplot.cpython-36.pyc
│   │           │   │   │   │   ├── circuitutils.cpython-36.pyc
│   │           │   │   │   │   ├── commutator.cpython-36.pyc
│   │           │   │   │   │   ├── constants.cpython-36.pyc
│   │           │   │   │   │   ├── dagger.cpython-36.pyc
│   │           │   │   │   │   ├── density.cpython-36.pyc
│   │           │   │   │   │   ├── fermion.cpython-36.pyc
│   │           │   │   │   │   ├── gate.cpython-36.pyc
│   │           │   │   │   │   ├── grover.cpython-36.pyc
│   │           │   │   │   │   ├── hilbert.cpython-36.pyc
│   │           │   │   │   │   ├── identitysearch.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── innerproduct.cpython-36.pyc
│   │           │   │   │   │   ├── matrixcache.cpython-36.pyc
│   │           │   │   │   │   ├── matrixutils.cpython-36.pyc
│   │           │   │   │   │   ├── operator.cpython-36.pyc
│   │           │   │   │   │   ├── operatorordering.cpython-36.pyc
│   │           │   │   │   │   ├── operatorset.cpython-36.pyc
│   │           │   │   │   │   ├── pauli.cpython-36.pyc
│   │           │   │   │   │   ├── piab.cpython-36.pyc
│   │           │   │   │   │   ├── qapply.cpython-36.pyc
│   │           │   │   │   │   ├── qasm.cpython-36.pyc
│   │           │   │   │   │   ├── qexpr.cpython-36.pyc
│   │           │   │   │   │   ├── qft.cpython-36.pyc
│   │           │   │   │   │   ├── qubit.cpython-36.pyc
│   │           │   │   │   │   ├── represent.cpython-36.pyc
│   │           │   │   │   │   ├── sho1d.cpython-36.pyc
│   │           │   │   │   │   ├── shor.cpython-36.pyc
│   │           │   │   │   │   ├── spin.cpython-36.pyc
│   │           │   │   │   │   ├── state.cpython-36.pyc
│   │           │   │   │   │   └── tensorproduct.cpython-36.pyc
│   │           │   │   │   ├── qapply.py
│   │           │   │   │   ├── qasm.py
│   │           │   │   │   ├── qexpr.py
│   │           │   │   │   ├── qft.py
│   │           │   │   │   ├── qubit.py
│   │           │   │   │   ├── represent.py
│   │           │   │   │   ├── sho1d.py
│   │           │   │   │   ├── shor.py
│   │           │   │   │   ├── spin.py
│   │           │   │   │   ├── state.py
│   │           │   │   │   ├── tensorproduct.py
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_anticommutator.cpython-36.pyc
│   │           │   │   │       │   ├── test_boson.cpython-36.pyc
│   │           │   │   │       │   ├── test_cartesian.cpython-36.pyc
│   │           │   │   │       │   ├── test_cg.cpython-36.pyc
│   │           │   │   │       │   ├── test_circuitplot.cpython-36.pyc
│   │           │   │   │       │   ├── test_circuitutils.cpython-36.pyc
│   │           │   │   │       │   ├── test_commutator.cpython-36.pyc
│   │           │   │   │       │   ├── test_constants.cpython-36.pyc
│   │           │   │   │       │   ├── test_dagger.cpython-36.pyc
│   │           │   │   │       │   ├── test_density.cpython-36.pyc
│   │           │   │   │       │   ├── test_fermion.cpython-36.pyc
│   │           │   │   │       │   ├── test_gate.cpython-36.pyc
│   │           │   │   │       │   ├── test_grover.cpython-36.pyc
│   │           │   │   │       │   ├── test_hilbert.cpython-36.pyc
│   │           │   │   │       │   ├── test_identitysearch.cpython-36.pyc
│   │           │   │   │       │   ├── test_innerproduct.cpython-36.pyc
│   │           │   │   │       │   ├── test_matrixutils.cpython-36.pyc
│   │           │   │   │       │   ├── test_operator.cpython-36.pyc
│   │           │   │   │       │   ├── test_operatorordering.cpython-36.pyc
│   │           │   │   │       │   ├── test_operatorset.cpython-36.pyc
│   │           │   │   │       │   ├── test_pauli.cpython-36.pyc
│   │           │   │   │       │   ├── test_piab.cpython-36.pyc
│   │           │   │   │       │   ├── test_printing.cpython-36.pyc
│   │           │   │   │       │   ├── test_qapply.cpython-36.pyc
│   │           │   │   │       │   ├── test_qasm.cpython-36.pyc
│   │           │   │   │       │   ├── test_qexpr.cpython-36.pyc
│   │           │   │   │       │   ├── test_qft.cpython-36.pyc
│   │           │   │   │       │   ├── test_qubit.cpython-36.pyc
│   │           │   │   │       │   ├── test_represent.cpython-36.pyc
│   │           │   │   │       │   ├── test_sho1d.cpython-36.pyc
│   │           │   │   │       │   ├── test_shor.cpython-36.pyc
│   │           │   │   │       │   ├── test_spin.cpython-36.pyc
│   │           │   │   │       │   ├── test_state.cpython-36.pyc
│   │           │   │   │       │   └── test_tensorproduct.cpython-36.pyc
│   │           │   │   │       ├── test_anticommutator.py
│   │           │   │   │       ├── test_boson.py
│   │           │   │   │       ├── test_cartesian.py
│   │           │   │   │       ├── test_cg.py
│   │           │   │   │       ├── test_circuitplot.py
│   │           │   │   │       ├── test_circuitutils.py
│   │           │   │   │       ├── test_commutator.py
│   │           │   │   │       ├── test_constants.py
│   │           │   │   │       ├── test_dagger.py
│   │           │   │   │       ├── test_density.py
│   │           │   │   │       ├── test_fermion.py
│   │           │   │   │       ├── test_gate.py
│   │           │   │   │       ├── test_grover.py
│   │           │   │   │       ├── test_hilbert.py
│   │           │   │   │       ├── test_identitysearch.py
│   │           │   │   │       ├── test_innerproduct.py
│   │           │   │   │       ├── test_matrixutils.py
│   │           │   │   │       ├── test_operatorordering.py
│   │           │   │   │       ├── test_operator.py
│   │           │   │   │       ├── test_operatorset.py
│   │           │   │   │       ├── test_pauli.py
│   │           │   │   │       ├── test_piab.py
│   │           │   │   │       ├── test_printing.py
│   │           │   │   │       ├── test_qapply.py
│   │           │   │   │       ├── test_qasm.py
│   │           │   │   │       ├── test_qexpr.py
│   │           │   │   │       ├── test_qft.py
│   │           │   │   │       ├── test_qubit.py
│   │           │   │   │       ├── test_represent.py
│   │           │   │   │       ├── test_sho1d.py
│   │           │   │   │       ├── test_shor.py
│   │           │   │   │       ├── test_spin.py
│   │           │   │   │       ├── test_state.py
│   │           │   │   │       └── test_tensorproduct.py
│   │           │   │   ├── secondquant.py
│   │           │   │   ├── sho.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_clebsch_gordan.cpython-36.pyc
│   │           │   │   │   │   ├── test_hydrogen.cpython-36.pyc
│   │           │   │   │   │   ├── test_paulialgebra.cpython-36.pyc
│   │           │   │   │   │   ├── test_physics_matrices.cpython-36.pyc
│   │           │   │   │   │   ├── test_pring.cpython-36.pyc
│   │           │   │   │   │   ├── test_qho_1d.cpython-36.pyc
│   │           │   │   │   │   ├── test_secondquant.cpython-36.pyc
│   │           │   │   │   │   └── test_sho.cpython-36.pyc
│   │           │   │   │   ├── test_clebsch_gordan.py
│   │           │   │   │   ├── test_hydrogen.py
│   │           │   │   │   ├── test_paulialgebra.py
│   │           │   │   │   ├── test_physics_matrices.py
│   │           │   │   │   ├── test_pring.py
│   │           │   │   │   ├── test_qho_1d.py
│   │           │   │   │   ├── test_secondquant.py
│   │           │   │   │   └── test_sho.py
│   │           │   │   ├── units
│   │           │   │   │   ├── definitions.py
│   │           │   │   │   ├── dimensions.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── prefixes.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── definitions.cpython-36.pyc
│   │           │   │   │   │   ├── dimensions.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── prefixes.cpython-36.pyc
│   │           │   │   │   │   ├── quantities.cpython-36.pyc
│   │           │   │   │   │   ├── unitsystem.cpython-36.pyc
│   │           │   │   │   │   └── util.cpython-36.pyc
│   │           │   │   │   ├── quantities.py
│   │           │   │   │   ├── systems
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── mksa.py
│   │           │   │   │   │   ├── mks.py
│   │           │   │   │   │   ├── natural.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── mksa.cpython-36.pyc
│   │           │   │   │   │   │   ├── mks.cpython-36.pyc
│   │           │   │   │   │   │   ├── natural.cpython-36.pyc
│   │           │   │   │   │   │   └── si.cpython-36.pyc
│   │           │   │   │   │   └── si.py
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_dimensions.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_dimensionsystem.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_prefixes.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_quantities.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_unitsystem.cpython-36.pyc
│   │           │   │   │   │   │   └── test_util.cpython-36.pyc
│   │           │   │   │   │   ├── test_dimensions.py
│   │           │   │   │   │   ├── test_dimensionsystem.py
│   │           │   │   │   │   ├── test_prefixes.py
│   │           │   │   │   │   ├── test_quantities.py
│   │           │   │   │   │   ├── test_unitsystem.py
│   │           │   │   │   │   └── test_util.py
│   │           │   │   │   ├── unitsystem.py
│   │           │   │   │   └── util.py
│   │           │   │   ├── vector
│   │           │   │   │   ├── dyadic.py
│   │           │   │   │   ├── fieldfunctions.py
│   │           │   │   │   ├── frame.py
│   │           │   │   │   ├── functions.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── point.py
│   │           │   │   │   ├── printing.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── dyadic.cpython-36.pyc
│   │           │   │   │   │   ├── fieldfunctions.cpython-36.pyc
│   │           │   │   │   │   ├── frame.cpython-36.pyc
│   │           │   │   │   │   ├── functions.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── point.cpython-36.pyc
│   │           │   │   │   │   ├── printing.cpython-36.pyc
│   │           │   │   │   │   └── vector.cpython-36.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_dyadic.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_fieldfunctions.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_frame.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_functions.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_output.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_point.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_printing.cpython-36.pyc
│   │           │   │   │   │   │   └── test_vector.cpython-36.pyc
│   │           │   │   │   │   ├── test_dyadic.py
│   │           │   │   │   │   ├── test_fieldfunctions.py
│   │           │   │   │   │   ├── test_frame.py
│   │           │   │   │   │   ├── test_functions.py
│   │           │   │   │   │   ├── test_output.py
│   │           │   │   │   │   ├── test_point.py
│   │           │   │   │   │   ├── test_printing.py
│   │           │   │   │   │   └── test_vector.py
│   │           │   │   │   └── vector.py
│   │           │   │   └── wigner.py
│   │           │   ├── plotting
│   │           │   │   ├── experimental_lambdify.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── intervalmath
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── interval_arithmetic.py
│   │           │   │   │   ├── lib_interval.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── interval_arithmetic.cpython-36.pyc
│   │           │   │   │   │   └── lib_interval.cpython-36.pyc
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_interval_functions.cpython-36.pyc
│   │           │   │   │       │   └── test_intervalmath.cpython-36.pyc
│   │           │   │   │       ├── test_interval_functions.py
│   │           │   │   │       └── test_intervalmath.py
│   │           │   │   ├── plot_implicit.py
│   │           │   │   ├── plot.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── experimental_lambdify.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── plot.cpython-36.pyc
│   │           │   │   │   ├── plot_implicit.cpython-36.pyc
│   │           │   │   │   └── textplot.cpython-36.pyc
│   │           │   │   ├── pygletplot
│   │           │   │   │   ├── color_scheme.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── managed_window.py
│   │           │   │   │   ├── plot_axes.py
│   │           │   │   │   ├── plot_camera.py
│   │           │   │   │   ├── plot_controller.py
│   │           │   │   │   ├── plot_curve.py
│   │           │   │   │   ├── plot_interval.py
│   │           │   │   │   ├── plot_mode_base.py
│   │           │   │   │   ├── plot_mode.py
│   │           │   │   │   ├── plot_modes.py
│   │           │   │   │   ├── plot_object.py
│   │           │   │   │   ├── plot.py
│   │           │   │   │   ├── plot_rotation.py
│   │           │   │   │   ├── plot_surface.py
│   │           │   │   │   ├── plot_window.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── color_scheme.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── managed_window.cpython-36.pyc
│   │           │   │   │   │   ├── plot_axes.cpython-36.pyc
│   │           │   │   │   │   ├── plot_camera.cpython-36.pyc
│   │           │   │   │   │   ├── plot_controller.cpython-36.pyc
│   │           │   │   │   │   ├── plot.cpython-36.pyc
│   │           │   │   │   │   ├── plot_curve.cpython-36.pyc
│   │           │   │   │   │   ├── plot_interval.cpython-36.pyc
│   │           │   │   │   │   ├── plot_mode_base.cpython-36.pyc
│   │           │   │   │   │   ├── plot_mode.cpython-36.pyc
│   │           │   │   │   │   ├── plot_modes.cpython-36.pyc
│   │           │   │   │   │   ├── plot_object.cpython-36.pyc
│   │           │   │   │   │   ├── plot_rotation.cpython-36.pyc
│   │           │   │   │   │   ├── plot_surface.cpython-36.pyc
│   │           │   │   │   │   ├── plot_window.cpython-36.pyc
│   │           │   │   │   │   └── util.cpython-36.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   └── test_plotting.cpython-36.pyc
│   │           │   │   │   │   └── test_plotting.py
│   │           │   │   │   └── util.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_plot.cpython-36.pyc
│   │           │   │   │   │   └── test_plot_implicit.cpython-36.pyc
│   │           │   │   │   ├── test_plot_implicit.py
│   │           │   │   │   └── test_plot.py
│   │           │   │   └── textplot.py
│   │           │   ├── polys
│   │           │   │   ├── agca
│   │           │   │   │   ├── extensions.py
│   │           │   │   │   ├── homomorphisms.py
│   │           │   │   │   ├── ideals.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── modules.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── extensions.cpython-36.pyc
│   │           │   │   │   │   ├── homomorphisms.cpython-36.pyc
│   │           │   │   │   │   ├── ideals.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   └── modules.cpython-36.pyc
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_extensions.cpython-36.pyc
│   │           │   │   │       │   ├── test_homomorphisms.cpython-36.pyc
│   │           │   │   │       │   ├── test_ideals.cpython-36.pyc
│   │           │   │   │       │   └── test_modules.cpython-36.pyc
│   │           │   │   │       ├── test_extensions.py
│   │           │   │   │       ├── test_homomorphisms.py
│   │           │   │   │       ├── test_ideals.py
│   │           │   │   │       └── test_modules.py
│   │           │   │   ├── benchmarks
│   │           │   │   │   ├── bench_galoispolys.py
│   │           │   │   │   ├── bench_groebnertools.py
│   │           │   │   │   ├── bench_solvers.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── bench_galoispolys.cpython-36.pyc
│   │           │   │   │       ├── bench_groebnertools.cpython-36.pyc
│   │           │   │   │       ├── bench_solvers.cpython-36.pyc
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   ├── compatibility.py
│   │           │   │   ├── constructor.py
│   │           │   │   ├── densearith.py
│   │           │   │   ├── densebasic.py
│   │           │   │   ├── densetools.py
│   │           │   │   ├── dispersion.py
│   │           │   │   ├── distributedmodules.py
│   │           │   │   ├── domains
│   │           │   │   │   ├── algebraicfield.py
│   │           │   │   │   ├── characteristiczero.py
│   │           │   │   │   ├── complexfield.py
│   │           │   │   │   ├── compositedomain.py
│   │           │   │   │   ├── domainelement.py
│   │           │   │   │   ├── domain.py
│   │           │   │   │   ├── expressiondomain.py
│   │           │   │   │   ├── field.py
│   │           │   │   │   ├── finitefield.py
│   │           │   │   │   ├── fractionfield.py
│   │           │   │   │   ├── gmpyfinitefield.py
│   │           │   │   │   ├── gmpyintegerring.py
│   │           │   │   │   ├── gmpyrationalfield.py
│   │           │   │   │   ├── groundtypes.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── integerring.py
│   │           │   │   │   ├── modularinteger.py
│   │           │   │   │   ├── mpelements.py
│   │           │   │   │   ├── old_fractionfield.py
│   │           │   │   │   ├── old_polynomialring.py
│   │           │   │   │   ├── polynomialring.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── algebraicfield.cpython-36.pyc
│   │           │   │   │   │   ├── characteristiczero.cpython-36.pyc
│   │           │   │   │   │   ├── complexfield.cpython-36.pyc
│   │           │   │   │   │   ├── compositedomain.cpython-36.pyc
│   │           │   │   │   │   ├── domain.cpython-36.pyc
│   │           │   │   │   │   ├── domainelement.cpython-36.pyc
│   │           │   │   │   │   ├── expressiondomain.cpython-36.pyc
│   │           │   │   │   │   ├── field.cpython-36.pyc
│   │           │   │   │   │   ├── finitefield.cpython-36.pyc
│   │           │   │   │   │   ├── fractionfield.cpython-36.pyc
│   │           │   │   │   │   ├── gmpyfinitefield.cpython-36.pyc
│   │           │   │   │   │   ├── gmpyintegerring.cpython-36.pyc
│   │           │   │   │   │   ├── gmpyrationalfield.cpython-36.pyc
│   │           │   │   │   │   ├── groundtypes.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── integerring.cpython-36.pyc
│   │           │   │   │   │   ├── modularinteger.cpython-36.pyc
│   │           │   │   │   │   ├── mpelements.cpython-36.pyc
│   │           │   │   │   │   ├── old_fractionfield.cpython-36.pyc
│   │           │   │   │   │   ├── old_polynomialring.cpython-36.pyc
│   │           │   │   │   │   ├── polynomialring.cpython-36.pyc
│   │           │   │   │   │   ├── pythonfinitefield.cpython-36.pyc
│   │           │   │   │   │   ├── pythonintegerring.cpython-36.pyc
│   │           │   │   │   │   ├── pythonrational.cpython-36.pyc
│   │           │   │   │   │   ├── pythonrationalfield.cpython-36.pyc
│   │           │   │   │   │   ├── quotientring.cpython-36.pyc
│   │           │   │   │   │   ├── rationalfield.cpython-36.pyc
│   │           │   │   │   │   ├── realfield.cpython-36.pyc
│   │           │   │   │   │   ├── ring.cpython-36.pyc
│   │           │   │   │   │   └── simpledomain.cpython-36.pyc
│   │           │   │   │   ├── pythonfinitefield.py
│   │           │   │   │   ├── pythonintegerring.py
│   │           │   │   │   ├── pythonrationalfield.py
│   │           │   │   │   ├── pythonrational.py
│   │           │   │   │   ├── quotientring.py
│   │           │   │   │   ├── rationalfield.py
│   │           │   │   │   ├── realfield.py
│   │           │   │   │   ├── ring.py
│   │           │   │   │   ├── simpledomain.py
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_domains.cpython-36.pyc
│   │           │   │   │       │   ├── test_polynomialring.cpython-36.pyc
│   │           │   │   │       │   └── test_quotientring.cpython-36.pyc
│   │           │   │   │       ├── test_domains.py
│   │           │   │   │       ├── test_polynomialring.py
│   │           │   │   │       └── test_quotientring.py
│   │           │   │   ├── euclidtools.py
│   │           │   │   ├── factortools.py
│   │           │   │   ├── fglmtools.py
│   │           │   │   ├── fields.py
│   │           │   │   ├── galoistools.py
│   │           │   │   ├── groebnertools.py
│   │           │   │   ├── heuristicgcd.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── modulargcd.py
│   │           │   │   ├── monomials.py
│   │           │   │   ├── multivariate_resultants.py
│   │           │   │   ├── numberfields.py
│   │           │   │   ├── orderings.py
│   │           │   │   ├── orthopolys.py
│   │           │   │   ├── partfrac.py
│   │           │   │   ├── polyclasses.py
│   │           │   │   ├── polyconfig.py
│   │           │   │   ├── polyerrors.py
│   │           │   │   ├── polyfuncs.py
│   │           │   │   ├── polymatrix.py
│   │           │   │   ├── polyoptions.py
│   │           │   │   ├── polyquinticconst.py
│   │           │   │   ├── polyroots.py
│   │           │   │   ├── polytools.py
│   │           │   │   ├── polyutils.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── compatibility.cpython-36.pyc
│   │           │   │   │   ├── constructor.cpython-36.pyc
│   │           │   │   │   ├── densearith.cpython-36.pyc
│   │           │   │   │   ├── densebasic.cpython-36.pyc
│   │           │   │   │   ├── densetools.cpython-36.pyc
│   │           │   │   │   ├── dispersion.cpython-36.pyc
│   │           │   │   │   ├── distributedmodules.cpython-36.pyc
│   │           │   │   │   ├── euclidtools.cpython-36.pyc
│   │           │   │   │   ├── factortools.cpython-36.pyc
│   │           │   │   │   ├── fglmtools.cpython-36.pyc
│   │           │   │   │   ├── fields.cpython-36.pyc
│   │           │   │   │   ├── galoistools.cpython-36.pyc
│   │           │   │   │   ├── groebnertools.cpython-36.pyc
│   │           │   │   │   ├── heuristicgcd.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── modulargcd.cpython-36.pyc
│   │           │   │   │   ├── monomials.cpython-36.pyc
│   │           │   │   │   ├── multivariate_resultants.cpython-36.pyc
│   │           │   │   │   ├── numberfields.cpython-36.pyc
│   │           │   │   │   ├── orderings.cpython-36.pyc
│   │           │   │   │   ├── orthopolys.cpython-36.pyc
│   │           │   │   │   ├── partfrac.cpython-36.pyc
│   │           │   │   │   ├── polyclasses.cpython-36.pyc
│   │           │   │   │   ├── polyconfig.cpython-36.pyc
│   │           │   │   │   ├── polyerrors.cpython-36.pyc
│   │           │   │   │   ├── polyfuncs.cpython-36.pyc
│   │           │   │   │   ├── polymatrix.cpython-36.pyc
│   │           │   │   │   ├── polyoptions.cpython-36.pyc
│   │           │   │   │   ├── polyquinticconst.cpython-36.pyc
│   │           │   │   │   ├── polyroots.cpython-36.pyc
│   │           │   │   │   ├── polytools.cpython-36.pyc
│   │           │   │   │   ├── polyutils.cpython-36.pyc
│   │           │   │   │   ├── rationaltools.cpython-36.pyc
│   │           │   │   │   ├── rings.cpython-36.pyc
│   │           │   │   │   ├── ring_series.cpython-36.pyc
│   │           │   │   │   ├── rootisolation.cpython-36.pyc
│   │           │   │   │   ├── rootoftools.cpython-36.pyc
│   │           │   │   │   ├── solvers.cpython-36.pyc
│   │           │   │   │   ├── specialpolys.cpython-36.pyc
│   │           │   │   │   ├── sqfreetools.cpython-36.pyc
│   │           │   │   │   └── subresultants_qq_zz.cpython-36.pyc
│   │           │   │   ├── rationaltools.py
│   │           │   │   ├── ring_series.py
│   │           │   │   ├── rings.py
│   │           │   │   ├── rootisolation.py
│   │           │   │   ├── rootoftools.py
│   │           │   │   ├── solvers.py
│   │           │   │   ├── specialpolys.py
│   │           │   │   ├── sqfreetools.py
│   │           │   │   ├── subresultants_qq_zz.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_constructor.cpython-36.pyc
│   │           │   │       │   ├── test_densearith.cpython-36.pyc
│   │           │   │       │   ├── test_densebasic.cpython-36.pyc
│   │           │   │       │   ├── test_densetools.cpython-36.pyc
│   │           │   │       │   ├── test_dispersion.cpython-36.pyc
│   │           │   │       │   ├── test_distributedmodules.cpython-36.pyc
│   │           │   │       │   ├── test_euclidtools.cpython-36.pyc
│   │           │   │       │   ├── test_factortools.cpython-36.pyc
│   │           │   │       │   ├── test_fields.cpython-36.pyc
│   │           │   │       │   ├── test_galoistools.cpython-36.pyc
│   │           │   │       │   ├── test_groebnertools.cpython-36.pyc
│   │           │   │       │   ├── test_heuristicgcd.cpython-36.pyc
│   │           │   │       │   ├── test_injections.cpython-36.pyc
│   │           │   │       │   ├── test_modulargcd.cpython-36.pyc
│   │           │   │       │   ├── test_monomials.cpython-36.pyc
│   │           │   │       │   ├── test_multivariate_resultants.cpython-36.pyc
│   │           │   │       │   ├── test_numberfields.cpython-36.pyc
│   │           │   │       │   ├── test_orderings.cpython-36.pyc
│   │           │   │       │   ├── test_orthopolys.cpython-36.pyc
│   │           │   │       │   ├── test_partfrac.cpython-36.pyc
│   │           │   │       │   ├── test_polyclasses.cpython-36.pyc
│   │           │   │       │   ├── test_polyfuncs.cpython-36.pyc
│   │           │   │       │   ├── test_polymatrix.cpython-36.pyc
│   │           │   │       │   ├── test_polyoptions.cpython-36.pyc
│   │           │   │       │   ├── test_polyroots.cpython-36.pyc
│   │           │   │       │   ├── test_polytools.cpython-36.pyc
│   │           │   │       │   ├── test_polyutils.cpython-36.pyc
│   │           │   │       │   ├── test_pythonrational.cpython-36.pyc
│   │           │   │       │   ├── test_rationaltools.cpython-36.pyc
│   │           │   │       │   ├── test_rings.cpython-36.pyc
│   │           │   │       │   ├── test_ring_series.cpython-36.pyc
│   │           │   │       │   ├── test_rootisolation.cpython-36.pyc
│   │           │   │       │   ├── test_rootoftools.cpython-36.pyc
│   │           │   │       │   ├── test_solvers.cpython-36.pyc
│   │           │   │       │   ├── test_specialpolys.cpython-36.pyc
│   │           │   │       │   ├── test_sqfreetools.cpython-36.pyc
│   │           │   │       │   └── test_subresultants_qq_zz.cpython-36.pyc
│   │           │   │       ├── test_constructor.py
│   │           │   │       ├── test_densearith.py
│   │           │   │       ├── test_densebasic.py
│   │           │   │       ├── test_densetools.py
│   │           │   │       ├── test_dispersion.py
│   │           │   │       ├── test_distributedmodules.py
│   │           │   │       ├── test_euclidtools.py
│   │           │   │       ├── test_factortools.py
│   │           │   │       ├── test_fields.py
│   │           │   │       ├── test_galoistools.py
│   │           │   │       ├── test_groebnertools.py
│   │           │   │       ├── test_heuristicgcd.py
│   │           │   │       ├── test_injections.py
│   │           │   │       ├── test_modulargcd.py
│   │           │   │       ├── test_monomials.py
│   │           │   │       ├── test_multivariate_resultants.py
│   │           │   │       ├── test_numberfields.py
│   │           │   │       ├── test_orderings.py
│   │           │   │       ├── test_orthopolys.py
│   │           │   │       ├── test_partfrac.py
│   │           │   │       ├── test_polyclasses.py
│   │           │   │       ├── test_polyfuncs.py
│   │           │   │       ├── test_polymatrix.py
│   │           │   │       ├── test_polyoptions.py
│   │           │   │       ├── test_polyroots.py
│   │           │   │       ├── test_polytools.py
│   │           │   │       ├── test_polyutils.py
│   │           │   │       ├── test_pythonrational.py
│   │           │   │       ├── test_rationaltools.py
│   │           │   │       ├── test_ring_series.py
│   │           │   │       ├── test_rings.py
│   │           │   │       ├── test_rootisolation.py
│   │           │   │       ├── test_rootoftools.py
│   │           │   │       ├── test_solvers.py
│   │           │   │       ├── test_specialpolys.py
│   │           │   │       ├── test_sqfreetools.py
│   │           │   │       └── test_subresultants_qq_zz.py
│   │           │   ├── printing
│   │           │   │   ├── ccode.py
│   │           │   │   ├── codeprinter.py
│   │           │   │   ├── conventions.py
│   │           │   │   ├── cxxcode.py
│   │           │   │   ├── defaults.py
│   │           │   │   ├── dot.py
│   │           │   │   ├── fcode.py
│   │           │   │   ├── glsl.py
│   │           │   │   ├── gtk.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── jscode.py
│   │           │   │   ├── julia.py
│   │           │   │   ├── lambdarepr.py
│   │           │   │   ├── latex.py
│   │           │   │   ├── llvmjitcode.py
│   │           │   │   ├── mathematica.py
│   │           │   │   ├── mathml.py
│   │           │   │   ├── octave.py
│   │           │   │   ├── precedence.py
│   │           │   │   ├── pretty
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── pretty.py
│   │           │   │   │   ├── pretty_symbology.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── pretty.cpython-36.pyc
│   │           │   │   │   │   ├── pretty_symbology.cpython-36.pyc
│   │           │   │   │   │   └── stringpict.cpython-36.pyc
│   │           │   │   │   ├── stringpict.py
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   └── test_pretty.cpython-36.pyc
│   │           │   │   │       └── test_pretty.py
│   │           │   │   ├── preview.py
│   │           │   │   ├── printer.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── ccode.cpython-36.pyc
│   │           │   │   │   ├── codeprinter.cpython-36.pyc
│   │           │   │   │   ├── conventions.cpython-36.pyc
│   │           │   │   │   ├── cxxcode.cpython-36.pyc
│   │           │   │   │   ├── defaults.cpython-36.pyc
│   │           │   │   │   ├── dot.cpython-36.pyc
│   │           │   │   │   ├── fcode.cpython-36.pyc
│   │           │   │   │   ├── glsl.cpython-36.pyc
│   │           │   │   │   ├── gtk.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── jscode.cpython-36.pyc
│   │           │   │   │   ├── julia.cpython-36.pyc
│   │           │   │   │   ├── lambdarepr.cpython-36.pyc
│   │           │   │   │   ├── latex.cpython-36.pyc
│   │           │   │   │   ├── llvmjitcode.cpython-36.pyc
│   │           │   │   │   ├── mathematica.cpython-36.pyc
│   │           │   │   │   ├── mathml.cpython-36.pyc
│   │           │   │   │   ├── octave.cpython-36.pyc
│   │           │   │   │   ├── precedence.cpython-36.pyc
│   │           │   │   │   ├── preview.cpython-36.pyc
│   │           │   │   │   ├── printer.cpython-36.pyc
│   │           │   │   │   ├── pycode.cpython-36.pyc
│   │           │   │   │   ├── python.cpython-36.pyc
│   │           │   │   │   ├── rcode.cpython-36.pyc
│   │           │   │   │   ├── repr.cpython-36.pyc
│   │           │   │   │   ├── rust.cpython-36.pyc
│   │           │   │   │   ├── str.cpython-36.pyc
│   │           │   │   │   ├── tableform.cpython-36.pyc
│   │           │   │   │   ├── tensorflow.cpython-36.pyc
│   │           │   │   │   ├── theanocode.cpython-36.pyc
│   │           │   │   │   └── tree.cpython-36.pyc
│   │           │   │   ├── pycode.py
│   │           │   │   ├── python.py
│   │           │   │   ├── rcode.py
│   │           │   │   ├── repr.py
│   │           │   │   ├── rust.py
│   │           │   │   ├── str.py
│   │           │   │   ├── tableform.py
│   │           │   │   ├── tensorflow.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_ccode.cpython-36.pyc
│   │           │   │   │   │   ├── test_codeprinter.cpython-36.pyc
│   │           │   │   │   │   ├── test_conventions.cpython-36.pyc
│   │           │   │   │   │   ├── test_cxxcode.cpython-36.pyc
│   │           │   │   │   │   ├── test_dot.cpython-36.pyc
│   │           │   │   │   │   ├── test_fcode.cpython-36.pyc
│   │           │   │   │   │   ├── test_glsl.cpython-36.pyc
│   │           │   │   │   │   ├── test_gtk.cpython-36.pyc
│   │           │   │   │   │   ├── test_jscode.cpython-36.pyc
│   │           │   │   │   │   ├── test_julia.cpython-36.pyc
│   │           │   │   │   │   ├── test_lambdarepr.cpython-36.pyc
│   │           │   │   │   │   ├── test_latex.cpython-36.pyc
│   │           │   │   │   │   ├── test_llvmjit.cpython-36.pyc
│   │           │   │   │   │   ├── test_mathematica.cpython-36.pyc
│   │           │   │   │   │   ├── test_mathml.cpython-36.pyc
│   │           │   │   │   │   ├── test_numpy.cpython-36.pyc
│   │           │   │   │   │   ├── test_octave.cpython-36.pyc
│   │           │   │   │   │   ├── test_precedence.cpython-36.pyc
│   │           │   │   │   │   ├── test_preview.cpython-36.pyc
│   │           │   │   │   │   ├── test_pycode.cpython-36.pyc
│   │           │   │   │   │   ├── test_python.cpython-36.pyc
│   │           │   │   │   │   ├── test_rcode.cpython-36.pyc
│   │           │   │   │   │   ├── test_repr.cpython-36.pyc
│   │           │   │   │   │   ├── test_rust.cpython-36.pyc
│   │           │   │   │   │   ├── test_str.cpython-36.pyc
│   │           │   │   │   │   ├── test_tableform.cpython-36.pyc
│   │           │   │   │   │   ├── test_tensorflow.cpython-36.pyc
│   │           │   │   │   │   └── test_theanocode.cpython-36.pyc
│   │           │   │   │   ├── test_ccode.py
│   │           │   │   │   ├── test_codeprinter.py
│   │           │   │   │   ├── test_conventions.py
│   │           │   │   │   ├── test_cxxcode.py
│   │           │   │   │   ├── test_dot.py
│   │           │   │   │   ├── test_fcode.py
│   │           │   │   │   ├── test_glsl.py
│   │           │   │   │   ├── test_gtk.py
│   │           │   │   │   ├── test_jscode.py
│   │           │   │   │   ├── test_julia.py
│   │           │   │   │   ├── test_lambdarepr.py
│   │           │   │   │   ├── test_latex.py
│   │           │   │   │   ├── test_llvmjit.py
│   │           │   │   │   ├── test_mathematica.py
│   │           │   │   │   ├── test_mathml.py
│   │           │   │   │   ├── test_numpy.py
│   │           │   │   │   ├── test_octave.py
│   │           │   │   │   ├── test_precedence.py
│   │           │   │   │   ├── test_preview.py
│   │           │   │   │   ├── test_pycode.py
│   │           │   │   │   ├── test_python.py
│   │           │   │   │   ├── test_rcode.py
│   │           │   │   │   ├── test_repr.py
│   │           │   │   │   ├── test_rust.py
│   │           │   │   │   ├── test_str.py
│   │           │   │   │   ├── test_tableform.py
│   │           │   │   │   ├── test_tensorflow.py
│   │           │   │   │   └── test_theanocode.py
│   │           │   │   ├── theanocode.py
│   │           │   │   └── tree.py
│   │           │   ├── __pycache__
│   │           │   │   ├── abc.cpython-36.pyc
│   │           │   │   ├── conftest.cpython-36.pyc
│   │           │   │   ├── galgebra.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── release.cpython-36.pyc
│   │           │   │   └── this.cpython-36.pyc
│   │           │   ├── release.py
│   │           │   ├── sandbox
│   │           │   │   ├── indexed_integrals.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── indexed_integrals.cpython-36.pyc
│   │           │   │   │   └── __init__.cpython-36.pyc
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   └── test_indexed_integrals.cpython-36.pyc
│   │           │   │       └── test_indexed_integrals.py
│   │           │   ├── series
│   │           │   │   ├── acceleration.py
│   │           │   │   ├── approximants.py
│   │           │   │   ├── benchmarks
│   │           │   │   │   ├── bench_limit.py
│   │           │   │   │   ├── bench_order.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── bench_limit.cpython-36.pyc
│   │           │   │   │       ├── bench_order.cpython-36.pyc
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   ├── formal.py
│   │           │   │   ├── fourier.py
│   │           │   │   ├── gruntz.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── kauers.py
│   │           │   │   ├── limitseq.py
│   │           │   │   ├── limits.py
│   │           │   │   ├── order.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── acceleration.cpython-36.pyc
│   │           │   │   │   ├── approximants.cpython-36.pyc
│   │           │   │   │   ├── formal.cpython-36.pyc
│   │           │   │   │   ├── fourier.cpython-36.pyc
│   │           │   │   │   ├── gruntz.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── kauers.cpython-36.pyc
│   │           │   │   │   ├── limits.cpython-36.pyc
│   │           │   │   │   ├── limitseq.cpython-36.pyc
│   │           │   │   │   ├── order.cpython-36.pyc
│   │           │   │   │   ├── residues.cpython-36.pyc
│   │           │   │   │   ├── sequences.cpython-36.pyc
│   │           │   │   │   ├── series_class.cpython-36.pyc
│   │           │   │   │   └── series.cpython-36.pyc
│   │           │   │   ├── residues.py
│   │           │   │   ├── sequences.py
│   │           │   │   ├── series_class.py
│   │           │   │   ├── series.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_approximants.cpython-36.pyc
│   │           │   │       │   ├── test_demidovich.cpython-36.pyc
│   │           │   │       │   ├── test_formal.cpython-36.pyc
│   │           │   │       │   ├── test_fourier.cpython-36.pyc
│   │           │   │       │   ├── test_gruntz.cpython-36.pyc
│   │           │   │       │   ├── test_kauers.cpython-36.pyc
│   │           │   │       │   ├── test_limits.cpython-36.pyc
│   │           │   │       │   ├── test_limitseq.cpython-36.pyc
│   │           │   │       │   ├── test_lseries.cpython-36.pyc
│   │           │   │       │   ├── test_nseries.cpython-36.pyc
│   │           │   │       │   ├── test_order.cpython-36.pyc
│   │           │   │       │   ├── test_residues.cpython-36.pyc
│   │           │   │       │   ├── test_sequences.cpython-36.pyc
│   │           │   │       │   └── test_series.cpython-36.pyc
│   │           │   │       ├── test_approximants.py
│   │           │   │       ├── test_demidovich.py
│   │           │   │       ├── test_formal.py
│   │           │   │       ├── test_fourier.py
│   │           │   │       ├── test_gruntz.py
│   │           │   │       ├── test_kauers.py
│   │           │   │       ├── test_limitseq.py
│   │           │   │       ├── test_limits.py
│   │           │   │       ├── test_lseries.py
│   │           │   │       ├── test_nseries.py
│   │           │   │       ├── test_order.py
│   │           │   │       ├── test_residues.py
│   │           │   │       ├── test_sequences.py
│   │           │   │       └── test_series.py
│   │           │   ├── sets
│   │           │   │   ├── conditionset.py
│   │           │   │   ├── contains.py
│   │           │   │   ├── fancysets.py
│   │           │   │   ├── handlers
│   │           │   │   │   ├── add.py
│   │           │   │   │   ├── functions.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── intersection.py
│   │           │   │   │   ├── mul.py
│   │           │   │   │   ├── power.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── add.cpython-36.pyc
│   │           │   │   │   │   ├── functions.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── intersection.cpython-36.pyc
│   │           │   │   │   │   ├── mul.cpython-36.pyc
│   │           │   │   │   │   ├── power.cpython-36.pyc
│   │           │   │   │   │   └── union.cpython-36.pyc
│   │           │   │   │   └── union.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── ordinals.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── conditionset.cpython-36.pyc
│   │           │   │   │   ├── contains.cpython-36.pyc
│   │           │   │   │   ├── fancysets.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── ordinals.cpython-36.pyc
│   │           │   │   │   ├── setexpr.cpython-36.pyc
│   │           │   │   │   └── sets.cpython-36.pyc
│   │           │   │   ├── setexpr.py
│   │           │   │   ├── sets.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_conditionset.cpython-36.pyc
│   │           │   │       │   ├── test_contains.cpython-36.pyc
│   │           │   │       │   ├── test_fancysets.cpython-36.pyc
│   │           │   │       │   ├── test_ordinals.cpython-36.pyc
│   │           │   │       │   ├── test_setexpr.cpython-36.pyc
│   │           │   │       │   └── test_sets.cpython-36.pyc
│   │           │   │       ├── test_conditionset.py
│   │           │   │       ├── test_contains.py
│   │           │   │       ├── test_fancysets.py
│   │           │   │       ├── test_ordinals.py
│   │           │   │       ├── test_setexpr.py
│   │           │   │       └── test_sets.py
│   │           │   ├── simplify
│   │           │   │   ├── combsimp.py
│   │           │   │   ├── cse_main.py
│   │           │   │   ├── cse_opts.py
│   │           │   │   ├── epathtools.py
│   │           │   │   ├── fu.py
│   │           │   │   ├── gammasimp.py
│   │           │   │   ├── hyperexpand_doc.py
│   │           │   │   ├── hyperexpand.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── powsimp.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── combsimp.cpython-36.pyc
│   │           │   │   │   ├── cse_main.cpython-36.pyc
│   │           │   │   │   ├── cse_opts.cpython-36.pyc
│   │           │   │   │   ├── epathtools.cpython-36.pyc
│   │           │   │   │   ├── fu.cpython-36.pyc
│   │           │   │   │   ├── gammasimp.cpython-36.pyc
│   │           │   │   │   ├── hyperexpand.cpython-36.pyc
│   │           │   │   │   ├── hyperexpand_doc.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── powsimp.cpython-36.pyc
│   │           │   │   │   ├── radsimp.cpython-36.pyc
│   │           │   │   │   ├── ratsimp.cpython-36.pyc
│   │           │   │   │   ├── simplify.cpython-36.pyc
│   │           │   │   │   ├── sqrtdenest.cpython-36.pyc
│   │           │   │   │   ├── traversaltools.cpython-36.pyc
│   │           │   │   │   └── trigsimp.cpython-36.pyc
│   │           │   │   ├── radsimp.py
│   │           │   │   ├── ratsimp.py
│   │           │   │   ├── simplify.py
│   │           │   │   ├── sqrtdenest.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_combsimp.cpython-36.pyc
│   │           │   │   │   │   ├── test_cse.cpython-36.pyc
│   │           │   │   │   │   ├── test_epathtools.cpython-36.pyc
│   │           │   │   │   │   ├── test_fu.cpython-36.pyc
│   │           │   │   │   │   ├── test_function.cpython-36.pyc
│   │           │   │   │   │   ├── test_gammasimp.cpython-36.pyc
│   │           │   │   │   │   ├── test_hyperexpand.cpython-36.pyc
│   │           │   │   │   │   ├── test_powsimp.cpython-36.pyc
│   │           │   │   │   │   ├── test_radsimp.cpython-36.pyc
│   │           │   │   │   │   ├── test_ratsimp.cpython-36.pyc
│   │           │   │   │   │   ├── test_rewrite.cpython-36.pyc
│   │           │   │   │   │   ├── test_simplify.cpython-36.pyc
│   │           │   │   │   │   ├── test_sqrtdenest.cpython-36.pyc
│   │           │   │   │   │   ├── test_traversaltools.cpython-36.pyc
│   │           │   │   │   │   └── test_trigsimp.cpython-36.pyc
│   │           │   │   │   ├── test_combsimp.py
│   │           │   │   │   ├── test_cse.py
│   │           │   │   │   ├── test_epathtools.py
│   │           │   │   │   ├── test_function.py
│   │           │   │   │   ├── test_fu.py
│   │           │   │   │   ├── test_gammasimp.py
│   │           │   │   │   ├── test_hyperexpand.py
│   │           │   │   │   ├── test_powsimp.py
│   │           │   │   │   ├── test_radsimp.py
│   │           │   │   │   ├── test_ratsimp.py
│   │           │   │   │   ├── test_rewrite.py
│   │           │   │   │   ├── test_simplify.py
│   │           │   │   │   ├── test_sqrtdenest.py
│   │           │   │   │   ├── test_traversaltools.py
│   │           │   │   │   └── test_trigsimp.py
│   │           │   │   ├── traversaltools.py
│   │           │   │   └── trigsimp.py
│   │           │   ├── solvers
│   │           │   │   ├── benchmarks
│   │           │   │   │   ├── bench_solvers.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       ├── bench_solvers.cpython-36.pyc
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   ├── bivariate.py
│   │           │   │   ├── decompogen.py
│   │           │   │   ├── deutils.py
│   │           │   │   ├── diophantine.py
│   │           │   │   ├── inequalities.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── ode.py
│   │           │   │   ├── pde.py
│   │           │   │   ├── polysys.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── bivariate.cpython-36.pyc
│   │           │   │   │   ├── decompogen.cpython-36.pyc
│   │           │   │   │   ├── deutils.cpython-36.pyc
│   │           │   │   │   ├── diophantine.cpython-36.pyc
│   │           │   │   │   ├── inequalities.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── ode.cpython-36.pyc
│   │           │   │   │   ├── pde.cpython-36.pyc
│   │           │   │   │   ├── polysys.cpython-36.pyc
│   │           │   │   │   ├── recurr.cpython-36.pyc
│   │           │   │   │   ├── solvers.cpython-36.pyc
│   │           │   │   │   └── solveset.cpython-36.pyc
│   │           │   │   ├── recurr.py
│   │           │   │   ├── solvers.py
│   │           │   │   ├── solveset.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_constantsimp.cpython-36.pyc
│   │           │   │       │   ├── test_decompogen.cpython-36.pyc
│   │           │   │       │   ├── test_diophantine.cpython-36.pyc
│   │           │   │       │   ├── test_inequalities.cpython-36.pyc
│   │           │   │       │   ├── test_numeric.cpython-36.pyc
│   │           │   │       │   ├── test_ode.cpython-36.pyc
│   │           │   │       │   ├── test_pde.cpython-36.pyc
│   │           │   │       │   ├── test_polysys.cpython-36.pyc
│   │           │   │       │   ├── test_recurr.cpython-36.pyc
│   │           │   │       │   ├── test_solvers.cpython-36.pyc
│   │           │   │       │   └── test_solveset.cpython-36.pyc
│   │           │   │       ├── test_constantsimp.py
│   │           │   │       ├── test_decompogen.py
│   │           │   │       ├── test_diophantine.py
│   │           │   │       ├── test_inequalities.py
│   │           │   │       ├── test_numeric.py
│   │           │   │       ├── test_ode.py
│   │           │   │       ├── test_pde.py
│   │           │   │       ├── test_polysys.py
│   │           │   │       ├── test_recurr.py
│   │           │   │       ├── test_solvers.py
│   │           │   │       └── test_solveset.py
│   │           │   ├── stats
│   │           │   │   ├── crv.py
│   │           │   │   ├── crv_types.py
│   │           │   │   ├── drv.py
│   │           │   │   ├── drv_types.py
│   │           │   │   ├── error_prop.py
│   │           │   │   ├── frv.py
│   │           │   │   ├── frv_types.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── joint_rv.py
│   │           │   │   ├── joint_rv_types.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── crv.cpython-36.pyc
│   │           │   │   │   ├── crv_types.cpython-36.pyc
│   │           │   │   │   ├── drv.cpython-36.pyc
│   │           │   │   │   ├── drv_types.cpython-36.pyc
│   │           │   │   │   ├── error_prop.cpython-36.pyc
│   │           │   │   │   ├── frv.cpython-36.pyc
│   │           │   │   │   ├── frv_types.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── joint_rv.cpython-36.pyc
│   │           │   │   │   ├── joint_rv_types.cpython-36.pyc
│   │           │   │   │   ├── rv.cpython-36.pyc
│   │           │   │   │   ├── rv_interface.cpython-36.pyc
│   │           │   │   │   └── symbolic_probability.cpython-36.pyc
│   │           │   │   ├── rv_interface.py
│   │           │   │   ├── rv.py
│   │           │   │   ├── symbolic_probability.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_continuous_rv.cpython-36.pyc
│   │           │   │       │   ├── test_discrete_rv.cpython-36.pyc
│   │           │   │       │   ├── test_error_prop.cpython-36.pyc
│   │           │   │       │   ├── test_finite_rv.cpython-36.pyc
│   │           │   │       │   ├── test_joint_rv.cpython-36.pyc
│   │           │   │       │   ├── test_mix.cpython-36.pyc
│   │           │   │       │   ├── test_rv.cpython-36.pyc
│   │           │   │       │   └── test_symbolic_probability.cpython-36.pyc
│   │           │   │       ├── test_continuous_rv.py
│   │           │   │       ├── test_discrete_rv.py
│   │           │   │       ├── test_error_prop.py
│   │           │   │       ├── test_finite_rv.py
│   │           │   │       ├── test_joint_rv.py
│   │           │   │       ├── test_mix.py
│   │           │   │       ├── test_rv.py
│   │           │   │       └── test_symbolic_probability.py
│   │           │   ├── strategies
│   │           │   │   ├── branch
│   │           │   │   │   ├── core.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── core.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── tools.cpython-36.pyc
│   │           │   │   │   │   └── traverse.cpython-36.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_core.cpython-36.pyc
│   │           │   │   │   │   │   ├── test_tools.cpython-36.pyc
│   │           │   │   │   │   │   └── test_traverse.cpython-36.pyc
│   │           │   │   │   │   ├── test_core.py
│   │           │   │   │   │   ├── test_tools.py
│   │           │   │   │   │   └── test_traverse.py
│   │           │   │   │   ├── tools.py
│   │           │   │   │   └── traverse.py
│   │           │   │   ├── core.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── core.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── rl.cpython-36.pyc
│   │           │   │   │   ├── tools.cpython-36.pyc
│   │           │   │   │   ├── traverse.cpython-36.pyc
│   │           │   │   │   ├── tree.cpython-36.pyc
│   │           │   │   │   └── util.cpython-36.pyc
│   │           │   │   ├── rl.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_core.cpython-36.pyc
│   │           │   │   │   │   ├── test_rl.cpython-36.pyc
│   │           │   │   │   │   ├── test_strat.cpython-36.pyc
│   │           │   │   │   │   ├── test_tools.cpython-36.pyc
│   │           │   │   │   │   ├── test_traverse.cpython-36.pyc
│   │           │   │   │   │   └── test_tree.cpython-36.pyc
│   │           │   │   │   ├── test_core.py
│   │           │   │   │   ├── test_rl.py
│   │           │   │   │   ├── test_strat.py
│   │           │   │   │   ├── test_tools.py
│   │           │   │   │   ├── test_traverse.py
│   │           │   │   │   └── test_tree.py
│   │           │   │   ├── tools.py
│   │           │   │   ├── traverse.py
│   │           │   │   ├── tree.py
│   │           │   │   └── util.py
│   │           │   ├── tensor
│   │           │   │   ├── array
│   │           │   │   │   ├── arrayop.py
│   │           │   │   │   ├── dense_ndim_array.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── mutable_ndim_array.py
│   │           │   │   │   ├── ndim_array.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── arrayop.cpython-36.pyc
│   │           │   │   │   │   ├── dense_ndim_array.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── mutable_ndim_array.cpython-36.pyc
│   │           │   │   │   │   ├── ndim_array.cpython-36.pyc
│   │           │   │   │   │   └── sparse_ndim_array.cpython-36.pyc
│   │           │   │   │   ├── sparse_ndim_array.py
│   │           │   │   │   └── tests
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │   │       │   ├── test_arrayop.cpython-36.pyc
│   │           │   │   │       │   ├── test_immutable_ndim_array.cpython-36.pyc
│   │           │   │   │       │   ├── test_mutable_ndim_array.cpython-36.pyc
│   │           │   │   │       │   └── test_ndim_array_conversions.cpython-36.pyc
│   │           │   │   │       ├── test_arrayop.py
│   │           │   │   │       ├── test_immutable_ndim_array.py
│   │           │   │   │       ├── test_mutable_ndim_array.py
│   │           │   │   │       └── test_ndim_array_conversions.py
│   │           │   │   ├── functions.py
│   │           │   │   ├── indexed.py
│   │           │   │   ├── index_methods.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── functions.cpython-36.pyc
│   │           │   │   │   ├── indexed.cpython-36.pyc
│   │           │   │   │   ├── index_methods.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── tensor.cpython-36.pyc
│   │           │   │   │   └── toperators.cpython-36.pyc
│   │           │   │   ├── tensor.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_functions.cpython-36.pyc
│   │           │   │   │   │   ├── test_indexed.cpython-36.pyc
│   │           │   │   │   │   ├── test_index_methods.cpython-36.pyc
│   │           │   │   │   │   ├── test_tensor.cpython-36.pyc
│   │           │   │   │   │   ├── test_tensor_element.cpython-36.pyc
│   │           │   │   │   │   └── test_tensor_operators.cpython-36.pyc
│   │           │   │   │   ├── test_functions.py
│   │           │   │   │   ├── test_indexed.py
│   │           │   │   │   ├── test_index_methods.py
│   │           │   │   │   ├── test_tensor_element.py
│   │           │   │   │   ├── test_tensor_operators.py
│   │           │   │   │   └── test_tensor.py
│   │           │   │   └── toperators.py
│   │           │   ├── this.py
│   │           │   ├── unify
│   │           │   │   ├── core.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── core.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── rewrite.cpython-36.pyc
│   │           │   │   │   └── usympy.cpython-36.pyc
│   │           │   │   ├── rewrite.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_rewrite.cpython-36.pyc
│   │           │   │   │   │   ├── test_sympy.cpython-36.pyc
│   │           │   │   │   │   └── test_unify.cpython-36.pyc
│   │           │   │   │   ├── test_rewrite.py
│   │           │   │   │   ├── test_sympy.py
│   │           │   │   │   └── test_unify.py
│   │           │   │   └── usympy.py
│   │           │   ├── utilities
│   │           │   │   ├── autowrap.py
│   │           │   │   ├── benchmarking.py
│   │           │   │   ├── codegen.py
│   │           │   │   ├── _compilation
│   │           │   │   │   ├── availability.py
│   │           │   │   │   ├── compilation.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── availability.cpython-36.pyc
│   │           │   │   │   │   ├── compilation.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── runners.cpython-36.pyc
│   │           │   │   │   │   └── util.cpython-36.pyc
│   │           │   │   │   ├── runners.py
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   │   └── test_compilation.cpython-36.pyc
│   │           │   │   │   │   └── test_compilation.py
│   │           │   │   │   └── util.py
│   │           │   │   ├── decorator.py
│   │           │   │   ├── enumerative.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── iterables.py
│   │           │   │   ├── lambdify.py
│   │           │   │   ├── magic.py
│   │           │   │   ├── matchpy_connector.py
│   │           │   │   ├── mathml
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── mmlctop.xsl
│   │           │   │   │   │   ├── mmltex.xsl
│   │           │   │   │   │   └── simple_mmlctop.xsl
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __pycache__
│   │           │   │   │       └── __init__.cpython-36.pyc
│   │           │   │   ├── memoization.py
│   │           │   │   ├── misc.py
│   │           │   │   ├── pkgdata.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── autowrap.cpython-36.pyc
│   │           │   │   │   ├── benchmarking.cpython-36.pyc
│   │           │   │   │   ├── codegen.cpython-36.pyc
│   │           │   │   │   ├── decorator.cpython-36.pyc
│   │           │   │   │   ├── enumerative.cpython-36.pyc
│   │           │   │   │   ├── exceptions.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── iterables.cpython-36.pyc
│   │           │   │   │   ├── lambdify.cpython-36.pyc
│   │           │   │   │   ├── magic.cpython-36.pyc
│   │           │   │   │   ├── matchpy_connector.cpython-36.pyc
│   │           │   │   │   ├── memoization.cpython-36.pyc
│   │           │   │   │   ├── misc.cpython-36.pyc
│   │           │   │   │   ├── pkgdata.cpython-36.pyc
│   │           │   │   │   ├── pytest.cpython-36.pyc
│   │           │   │   │   ├── randtest.cpython-36.pyc
│   │           │   │   │   ├── runtests.cpython-36.pyc
│   │           │   │   │   ├── source.cpython-36.pyc
│   │           │   │   │   ├── timeutils.cpython-36.pyc
│   │           │   │   │   └── tmpfiles.cpython-36.pyc
│   │           │   │   ├── pytest.py
│   │           │   │   ├── randtest.py
│   │           │   │   ├── runtests.py
│   │           │   │   ├── source.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── diagnose_imports.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── diagnose_imports.cpython-36.pyc
│   │           │   │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   │   ├── test_autowrap.cpython-36.pyc
│   │           │   │   │   │   ├── test_codegen.cpython-36.pyc
│   │           │   │   │   │   ├── test_codegen_julia.cpython-36.pyc
│   │           │   │   │   │   ├── test_codegen_octave.cpython-36.pyc
│   │           │   │   │   │   ├── test_codegen_rust.cpython-36.pyc
│   │           │   │   │   │   ├── test_code_quality.cpython-36.pyc
│   │           │   │   │   │   ├── test_decorator.cpython-36.pyc
│   │           │   │   │   │   ├── test_enumerative.cpython-36.pyc
│   │           │   │   │   │   ├── test_iterables.cpython-36.pyc
│   │           │   │   │   │   ├── test_lambdify.cpython-36.pyc
│   │           │   │   │   │   ├── test_misc.cpython-36.pyc
│   │           │   │   │   │   ├── test_module_imports.cpython-36.pyc
│   │           │   │   │   │   ├── test_pickling.cpython-36.pyc
│   │           │   │   │   │   ├── test_pytest.cpython-36.pyc
│   │           │   │   │   │   ├── test_source.cpython-36.pyc
│   │           │   │   │   │   ├── test_timeutils.cpython-36.pyc
│   │           │   │   │   │   └── test_wester.cpython-36.pyc
│   │           │   │   │   ├── test_autowrap.py
│   │           │   │   │   ├── test_codegen_julia.py
│   │           │   │   │   ├── test_codegen_octave.py
│   │           │   │   │   ├── test_codegen.py
│   │           │   │   │   ├── test_codegen_rust.py
│   │           │   │   │   ├── test_code_quality.py
│   │           │   │   │   ├── test_decorator.py
│   │           │   │   │   ├── test_enumerative.py
│   │           │   │   │   ├── test_iterables.py
│   │           │   │   │   ├── test_lambdify.py
│   │           │   │   │   ├── test_misc.py
│   │           │   │   │   ├── test_module_imports.py
│   │           │   │   │   ├── test_pickling.py
│   │           │   │   │   ├── test_pytest.py
│   │           │   │   │   ├── test_source.py
│   │           │   │   │   ├── test_timeutils.py
│   │           │   │   │   └── test_wester.py
│   │           │   │   ├── timeutils.py
│   │           │   │   └── tmpfiles.py
│   │           │   └── vector
│   │           │       ├── basisdependent.py
│   │           │       ├── coordsysrect.py
│   │           │       ├── deloperator.py
│   │           │       ├── dyadic.py
│   │           │       ├── functions.py
│   │           │       ├── __init__.py
│   │           │       ├── operators.py
│   │           │       ├── orienters.py
│   │           │       ├── point.py
│   │           │       ├── __pycache__
│   │           │       │   ├── basisdependent.cpython-36.pyc
│   │           │       │   ├── coordsysrect.cpython-36.pyc
│   │           │       │   ├── deloperator.cpython-36.pyc
│   │           │       │   ├── dyadic.cpython-36.pyc
│   │           │       │   ├── functions.cpython-36.pyc
│   │           │       │   ├── __init__.cpython-36.pyc
│   │           │       │   ├── operators.cpython-36.pyc
│   │           │       │   ├── orienters.cpython-36.pyc
│   │           │       │   ├── point.cpython-36.pyc
│   │           │       │   ├── scalar.cpython-36.pyc
│   │           │       │   └── vector.cpython-36.pyc
│   │           │       ├── scalar.py
│   │           │       ├── tests
│   │           │       │   ├── __init__.py
│   │           │       │   ├── __pycache__
│   │           │       │   │   ├── __init__.cpython-36.pyc
│   │           │       │   │   ├── test_coordsysrect.cpython-36.pyc
│   │           │       │   │   ├── test_dyadic.cpython-36.pyc
│   │           │       │   │   ├── test_field_functions.cpython-36.pyc
│   │           │       │   │   ├── test_functions.cpython-36.pyc
│   │           │       │   │   ├── test_operators.cpython-36.pyc
│   │           │       │   │   ├── test_printing.cpython-36.pyc
│   │           │       │   │   └── test_vector.cpython-36.pyc
│   │           │       │   ├── test_coordsysrect.py
│   │           │       │   ├── test_dyadic.py
│   │           │       │   ├── test_field_functions.py
│   │           │       │   ├── test_functions.py
│   │           │       │   ├── test_operators.py
│   │           │       │   ├── test_printing.py
│   │           │       │   └── test_vector.py
│   │           │       └── vector.py
│   │           ├── sympy-1.4.dist-info
│   │           │   ├── AUTHORS
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── terminado
│   │           │   ├── __init__.py
│   │           │   ├── management.py
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── management.cpython-36.pyc
│   │           │   │   ├── uimodule.cpython-36.pyc
│   │           │   │   └── websocket.cpython-36.pyc
│   │           │   ├── _static
│   │           │   │   └── terminado.js
│   │           │   ├── tests
│   │           │   │   ├── basic_test.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── __pycache__
│   │           │   │       ├── basic_test.cpython-36.pyc
│   │           │   │       └── __init__.cpython-36.pyc
│   │           │   ├── uimod_embed.js
│   │           │   ├── uimodule.py
│   │           │   └── websocket.py
│   │           ├── terminado-0.8.2.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── testpath
│   │           │   ├── asserts.py
│   │           │   ├── cli-32.exe
│   │           │   ├── cli-64.exe
│   │           │   ├── commands.py
│   │           │   ├── env.py
│   │           │   ├── __init__.py
│   │           │   ├── __pycache__
│   │           │   │   ├── asserts.cpython-36.pyc
│   │           │   │   ├── commands.cpython-36.pyc
│   │           │   │   ├── env.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   └── tempdir.cpython-36.pyc
│   │           │   └── tempdir.py
│   │           ├── testpath-0.4.2.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── tornado
│   │           │   ├── auth.py
│   │           │   ├── autoreload.py
│   │           │   ├── concurrent.py
│   │           │   ├── curl_httpclient.py
│   │           │   ├── escape.py
│   │           │   ├── gen.py
│   │           │   ├── http1connection.py
│   │           │   ├── httpclient.py
│   │           │   ├── httpserver.py
│   │           │   ├── httputil.py
│   │           │   ├── __init__.py
│   │           │   ├── ioloop.py
│   │           │   ├── iostream.py
│   │           │   ├── _locale_data.py
│   │           │   ├── locale.py
│   │           │   ├── locks.py
│   │           │   ├── log.py
│   │           │   ├── netutil.py
│   │           │   ├── options.py
│   │           │   ├── platform
│   │           │   │   ├── asyncio.py
│   │           │   │   ├── auto.py
│   │           │   │   ├── caresresolver.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── interface.py
│   │           │   │   ├── posix.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── asyncio.cpython-36.pyc
│   │           │   │   │   ├── auto.cpython-36.pyc
│   │           │   │   │   ├── caresresolver.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── interface.cpython-36.pyc
│   │           │   │   │   ├── posix.cpython-36.pyc
│   │           │   │   │   ├── twisted.cpython-36.pyc
│   │           │   │   │   └── windows.cpython-36.pyc
│   │           │   │   ├── twisted.py
│   │           │   │   └── windows.py
│   │           │   ├── process.py
│   │           │   ├── __pycache__
│   │           │   │   ├── auth.cpython-36.pyc
│   │           │   │   ├── autoreload.cpython-36.pyc
│   │           │   │   ├── concurrent.cpython-36.pyc
│   │           │   │   ├── curl_httpclient.cpython-36.pyc
│   │           │   │   ├── escape.cpython-36.pyc
│   │           │   │   ├── gen.cpython-36.pyc
│   │           │   │   ├── http1connection.cpython-36.pyc
│   │           │   │   ├── httpclient.cpython-36.pyc
│   │           │   │   ├── httpserver.cpython-36.pyc
│   │           │   │   ├── httputil.cpython-36.pyc
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── ioloop.cpython-36.pyc
│   │           │   │   ├── iostream.cpython-36.pyc
│   │           │   │   ├── locale.cpython-36.pyc
│   │           │   │   ├── _locale_data.cpython-36.pyc
│   │           │   │   ├── locks.cpython-36.pyc
│   │           │   │   ├── log.cpython-36.pyc
│   │           │   │   ├── netutil.cpython-36.pyc
│   │           │   │   ├── options.cpython-36.pyc
│   │           │   │   ├── process.cpython-36.pyc
│   │           │   │   ├── queues.cpython-36.pyc
│   │           │   │   ├── routing.cpython-36.pyc
│   │           │   │   ├── simple_httpclient.cpython-36.pyc
│   │           │   │   ├── tcpclient.cpython-36.pyc
│   │           │   │   ├── tcpserver.cpython-36.pyc
│   │           │   │   ├── template.cpython-36.pyc
│   │           │   │   ├── testing.cpython-36.pyc
│   │           │   │   ├── util.cpython-36.pyc
│   │           │   │   ├── web.cpython-36.pyc
│   │           │   │   ├── websocket.cpython-36.pyc
│   │           │   │   └── wsgi.cpython-36.pyc
│   │           │   ├── py.typed
│   │           │   ├── queues.py
│   │           │   ├── routing.py
│   │           │   ├── simple_httpclient.py
│   │           │   ├── speedups.cpython-36m-x86_64-linux-gnu.so
│   │           │   ├── tcpclient.py
│   │           │   ├── tcpserver.py
│   │           │   ├── template.py
│   │           │   ├── test
│   │           │   │   ├── asyncio_test.py
│   │           │   │   ├── auth_test.py
│   │           │   │   ├── autoreload_test.py
│   │           │   │   ├── concurrent_test.py
│   │           │   │   ├── csv_translations
│   │           │   │   │   └── fr_FR.csv
│   │           │   │   ├── curl_httpclient_test.py
│   │           │   │   ├── escape_test.py
│   │           │   │   ├── gen_test.py
│   │           │   │   ├── gettext_translations
│   │           │   │   │   └── fr_FR
│   │           │   │   │       └── LC_MESSAGES
│   │           │   │   │           ├── tornado_test.mo
│   │           │   │   │           └── tornado_test.po
│   │           │   │   ├── http1connection_test.py
│   │           │   │   ├── httpclient_test.py
│   │           │   │   ├── httpserver_test.py
│   │           │   │   ├── httputil_test.py
│   │           │   │   ├── import_test.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── ioloop_test.py
│   │           │   │   ├── iostream_test.py
│   │           │   │   ├── locale_test.py
│   │           │   │   ├── locks_test.py
│   │           │   │   ├── log_test.py
│   │           │   │   ├── __main__.py
│   │           │   │   ├── netutil_test.py
│   │           │   │   ├── options_test.cfg
│   │           │   │   ├── options_test.py
│   │           │   │   ├── options_test_types.cfg
│   │           │   │   ├── options_test_types_str.cfg
│   │           │   │   ├── process_test.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── asyncio_test.cpython-36.pyc
│   │           │   │   │   ├── auth_test.cpython-36.pyc
│   │           │   │   │   ├── autoreload_test.cpython-36.pyc
│   │           │   │   │   ├── concurrent_test.cpython-36.pyc
│   │           │   │   │   ├── curl_httpclient_test.cpython-36.pyc
│   │           │   │   │   ├── escape_test.cpython-36.pyc
│   │           │   │   │   ├── gen_test.cpython-36.pyc
│   │           │   │   │   ├── http1connection_test.cpython-36.pyc
│   │           │   │   │   ├── httpclient_test.cpython-36.pyc
│   │           │   │   │   ├── httpserver_test.cpython-36.pyc
│   │           │   │   │   ├── httputil_test.cpython-36.pyc
│   │           │   │   │   ├── import_test.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── ioloop_test.cpython-36.pyc
│   │           │   │   │   ├── iostream_test.cpython-36.pyc
│   │           │   │   │   ├── locale_test.cpython-36.pyc
│   │           │   │   │   ├── locks_test.cpython-36.pyc
│   │           │   │   │   ├── log_test.cpython-36.pyc
│   │           │   │   │   ├── __main__.cpython-36.pyc
│   │           │   │   │   ├── netutil_test.cpython-36.pyc
│   │           │   │   │   ├── options_test.cpython-36.pyc
│   │           │   │   │   ├── process_test.cpython-36.pyc
│   │           │   │   │   ├── queues_test.cpython-36.pyc
│   │           │   │   │   ├── resolve_test_helper.cpython-36.pyc
│   │           │   │   │   ├── routing_test.cpython-36.pyc
│   │           │   │   │   ├── runtests.cpython-36.pyc
│   │           │   │   │   ├── simple_httpclient_test.cpython-36.pyc
│   │           │   │   │   ├── tcpclient_test.cpython-36.pyc
│   │           │   │   │   ├── tcpserver_test.cpython-36.pyc
│   │           │   │   │   ├── template_test.cpython-36.pyc
│   │           │   │   │   ├── testing_test.cpython-36.pyc
│   │           │   │   │   ├── twisted_test.cpython-36.pyc
│   │           │   │   │   ├── util.cpython-36.pyc
│   │           │   │   │   ├── util_test.cpython-36.pyc
│   │           │   │   │   ├── websocket_test.cpython-36.pyc
│   │           │   │   │   ├── web_test.cpython-36.pyc
│   │           │   │   │   ├── windows_test.cpython-36.pyc
│   │           │   │   │   └── wsgi_test.cpython-36.pyc
│   │           │   │   ├── queues_test.py
│   │           │   │   ├── resolve_test_helper.py
│   │           │   │   ├── routing_test.py
│   │           │   │   ├── runtests.py
│   │           │   │   ├── simple_httpclient_test.py
│   │           │   │   ├── static
│   │           │   │   │   ├── dir
│   │           │   │   │   │   └── index.html
│   │           │   │   │   ├── robots.txt
│   │           │   │   │   ├── sample.xml
│   │           │   │   │   ├── sample.xml.bz2
│   │           │   │   │   └── sample.xml.gz
│   │           │   │   ├── static_foo.txt
│   │           │   │   ├── tcpclient_test.py
│   │           │   │   ├── tcpserver_test.py
│   │           │   │   ├── templates
│   │           │   │   │   └── utf8.html
│   │           │   │   ├── template_test.py
│   │           │   │   ├── test.crt
│   │           │   │   ├── testing_test.py
│   │           │   │   ├── test.key
│   │           │   │   ├── twisted_test.py
│   │           │   │   ├── util.py
│   │           │   │   ├── util_test.py
│   │           │   │   ├── websocket_test.py
│   │           │   │   ├── web_test.py
│   │           │   │   ├── windows_test.py
│   │           │   │   └── wsgi_test.py
│   │           │   ├── testing.py
│   │           │   ├── util.py
│   │           │   ├── web.py
│   │           │   ├── websocket.py
│   │           │   └── wsgi.py
│   │           ├── tornado-6.0.2.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── traitlets
│   │           │   ├── config
│   │           │   │   ├── application.py
│   │           │   │   ├── configurable.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── loader.py
│   │           │   │   ├── manager.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── application.cpython-36.pyc
│   │           │   │   │   ├── configurable.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── loader.cpython-36.pyc
│   │           │   │   │   └── manager.cpython-36.pyc
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_application.cpython-36.pyc
│   │           │   │       │   ├── test_configurable.cpython-36.pyc
│   │           │   │       │   └── test_loader.cpython-36.pyc
│   │           │   │       ├── test_application.py
│   │           │   │       ├── test_configurable.py
│   │           │   │       └── test_loader.py
│   │           │   ├── __init__.py
│   │           │   ├── log.py
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── log.cpython-36.pyc
│   │           │   │   ├── traitlets.cpython-36.pyc
│   │           │   │   └── _version.cpython-36.pyc
│   │           │   ├── tests
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   ├── test_traitlets.cpython-36.pyc
│   │           │   │   │   ├── test_traitlets_enum.cpython-36.pyc
│   │           │   │   │   ├── utils.cpython-36.pyc
│   │           │   │   │   └── _warnings.cpython-36.pyc
│   │           │   │   ├── test_traitlets_enum.py
│   │           │   │   ├── test_traitlets.py
│   │           │   │   ├── utils.py
│   │           │   │   └── _warnings.py
│   │           │   ├── traitlets.py
│   │           │   ├── utils
│   │           │   │   ├── bunch.py
│   │           │   │   ├── getargspec.py
│   │           │   │   ├── importstring.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── bunch.cpython-36.pyc
│   │           │   │   │   ├── getargspec.cpython-36.pyc
│   │           │   │   │   ├── importstring.cpython-36.pyc
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── sentinel.cpython-36.pyc
│   │           │   │   ├── sentinel.py
│   │           │   │   └── tests
│   │           │   │       ├── __init__.py
│   │           │   │       ├── __pycache__
│   │           │   │       │   ├── __init__.cpython-36.pyc
│   │           │   │       │   ├── test_bunch.cpython-36.pyc
│   │           │   │       │   └── test_importstring.cpython-36.pyc
│   │           │   │       ├── test_bunch.py
│   │           │   │       └── test_importstring.py
│   │           │   └── _version.py
│   │           ├── traitlets-4.3.2.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── wcwidth
│   │           │   ├── __init__.py
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── table_wide.cpython-36.pyc
│   │           │   │   ├── table_zero.cpython-36.pyc
│   │           │   │   └── wcwidth.cpython-36.pyc
│   │           │   ├── table_wide.py
│   │           │   ├── table_zero.py
│   │           │   ├── tests
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-36.pyc
│   │           │   │   │   └── test_core.cpython-36.pyc
│   │           │   │   └── test_core.py
│   │           │   └── wcwidth.py
│   │           ├── wcwidth-0.1.7.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   ├── WHEEL
│   │           │   └── zip-safe
│   │           ├── webencodings
│   │           │   ├── __init__.py
│   │           │   ├── labels.py
│   │           │   ├── mklabels.py
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   ├── labels.cpython-36.pyc
│   │           │   │   ├── mklabels.cpython-36.pyc
│   │           │   │   ├── tests.cpython-36.pyc
│   │           │   │   └── x_user_defined.cpython-36.pyc
│   │           │   ├── tests.py
│   │           │   └── x_user_defined.py
│   │           ├── webencodings-0.5.1.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── widgetsnbextension
│   │           │   ├── __init__.py
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-36.pyc
│   │           │   │   └── _version.cpython-36.pyc
│   │           │   ├── static
│   │           │   │   ├── extension.js
│   │           │   │   └── extension.js.map
│   │           │   └── _version.py
│   │           ├── widgetsnbextension-3.4.2.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           └── zmq
│   │               ├── asyncio
│   │               │   ├── __init__.py
│   │               │   └── __pycache__
│   │               │       └── __init__.cpython-36.pyc
│   │               ├── auth
│   │               │   ├── asyncio
│   │               │   │   ├── __init__.py
│   │               │   │   └── __pycache__
│   │               │   │       └── __init__.cpython-36.pyc
│   │               │   ├── base.py
│   │               │   ├── certs.py
│   │               │   ├── __init__.py
│   │               │   ├── ioloop.py
│   │               │   ├── __pycache__
│   │               │   │   ├── base.cpython-36.pyc
│   │               │   │   ├── certs.cpython-36.pyc
│   │               │   │   ├── __init__.cpython-36.pyc
│   │               │   │   ├── ioloop.cpython-36.pyc
│   │               │   │   └── thread.cpython-36.pyc
│   │               │   └── thread.py
│   │               ├── backend
│   │               │   ├── cffi
│   │               │   │   ├── _cdefs.h
│   │               │   │   ├── _cffi.py
│   │               │   │   ├── constants.py
│   │               │   │   ├── context.py
│   │               │   │   ├── devices.py
│   │               │   │   ├── error.py
│   │               │   │   ├── __init__.py
│   │               │   │   ├── message.py
│   │               │   │   ├── _poll.py
│   │               │   │   ├── __pycache__
│   │               │   │   │   ├── _cffi.cpython-36.pyc
│   │               │   │   │   ├── constants.cpython-36.pyc
│   │               │   │   │   ├── context.cpython-36.pyc
│   │               │   │   │   ├── devices.cpython-36.pyc
│   │               │   │   │   ├── error.cpython-36.pyc
│   │               │   │   │   ├── __init__.cpython-36.pyc
│   │               │   │   │   ├── message.cpython-36.pyc
│   │               │   │   │   ├── _poll.cpython-36.pyc
│   │               │   │   │   ├── socket.cpython-36.pyc
│   │               │   │   │   └── utils.cpython-36.pyc
│   │               │   │   ├── socket.py
│   │               │   │   ├── utils.py
│   │               │   │   └── _verify.c
│   │               │   ├── cython
│   │               │   │   ├── checkrc.pxd
│   │               │   │   ├── constant_enums.pxi
│   │               │   │   ├── constants.cpython-36m-x86_64-linux-gnu.so
│   │               │   │   ├── constants.pxi
│   │               │   │   ├── context.cpython-36m-x86_64-linux-gnu.so
│   │               │   │   ├── context.pxd
│   │               │   │   ├── _device.cpython-36m-x86_64-linux-gnu.so
│   │               │   │   ├── error.cpython-36m-x86_64-linux-gnu.so
│   │               │   │   ├── __init__.py
│   │               │   │   ├── libzmq.pxd
│   │               │   │   ├── message.cpython-36m-x86_64-linux-gnu.so
│   │               │   │   ├── message.pxd
│   │               │   │   ├── _poll.cpython-36m-x86_64-linux-gnu.so
│   │               │   │   ├── _proxy_steerable.cpython-36m-x86_64-linux-gnu.so
│   │               │   │   ├── __pycache__
│   │               │   │   │   └── __init__.cpython-36.pyc
│   │               │   │   ├── socket.cpython-36m-x86_64-linux-gnu.so
│   │               │   │   ├── socket.pxd
│   │               │   │   ├── utils.cpython-36m-x86_64-linux-gnu.so
│   │               │   │   └── _version.cpython-36m-x86_64-linux-gnu.so
│   │               │   ├── __init__.py
│   │               │   ├── __pycache__
│   │               │   │   ├── __init__.cpython-36.pyc
│   │               │   │   └── select.cpython-36.pyc
│   │               │   └── select.py
│   │               ├── decorators.py
│   │               ├── devices
│   │               │   ├── basedevice.py
│   │               │   ├── __init__.py
│   │               │   ├── monitoredqueue.cpython-36m-x86_64-linux-gnu.so
│   │               │   ├── monitoredqueuedevice.py
│   │               │   ├── monitoredqueue.pxd
│   │               │   ├── monitoredqueue.py
│   │               │   ├── proxydevice.py
│   │               │   ├── proxysteerabledevice.py
│   │               │   └── __pycache__
│   │               │       ├── basedevice.cpython-36.pyc
│   │               │       ├── __init__.cpython-36.pyc
│   │               │       ├── monitoredqueue.cpython-36.pyc
│   │               │       ├── monitoredqueuedevice.cpython-36.pyc
│   │               │       ├── proxydevice.cpython-36.pyc
│   │               │       └── proxysteerabledevice.cpython-36.pyc
│   │               ├── error.py
│   │               ├── eventloop
│   │               │   ├── _deprecated.py
│   │               │   ├── future.py
│   │               │   ├── __init__.py
│   │               │   ├── ioloop.py
│   │               │   ├── minitornado
│   │               │   │   ├── concurrent.py
│   │               │   │   ├── __init__.py
│   │               │   │   ├── ioloop.py
│   │               │   │   ├── log.py
│   │               │   │   ├── platform
│   │               │   │   │   ├── auto.py
│   │               │   │   │   ├── common.py
│   │               │   │   │   ├── __init__.py
│   │               │   │   │   ├── interface.py
│   │               │   │   │   ├── posix.py
│   │               │   │   │   ├── __pycache__
│   │               │   │   │   │   ├── auto.cpython-36.pyc
│   │               │   │   │   │   ├── common.cpython-36.pyc
│   │               │   │   │   │   ├── __init__.cpython-36.pyc
│   │               │   │   │   │   ├── interface.cpython-36.pyc
│   │               │   │   │   │   ├── posix.cpython-36.pyc
│   │               │   │   │   │   └── windows.cpython-36.pyc
│   │               │   │   │   └── windows.py
│   │               │   │   ├── __pycache__
│   │               │   │   │   ├── concurrent.cpython-36.pyc
│   │               │   │   │   ├── __init__.cpython-36.pyc
│   │               │   │   │   ├── ioloop.cpython-36.pyc
│   │               │   │   │   ├── log.cpython-36.pyc
│   │               │   │   │   ├── stack_context.cpython-36.pyc
│   │               │   │   │   └── util.cpython-36.pyc
│   │               │   │   ├── stack_context.py
│   │               │   │   └── util.py
│   │               │   ├── __pycache__
│   │               │   │   ├── _deprecated.cpython-36.pyc
│   │               │   │   ├── future.cpython-36.pyc
│   │               │   │   ├── __init__.cpython-36.pyc
│   │               │   │   ├── ioloop.cpython-36.pyc
│   │               │   │   └── zmqstream.cpython-36.pyc
│   │               │   └── zmqstream.py
│   │               ├── _future.py
│   │               ├── green
│   │               │   ├── core.py
│   │               │   ├── device.py
│   │               │   ├── eventloop
│   │               │   │   ├── __init__.py
│   │               │   │   ├── ioloop.py
│   │               │   │   ├── __pycache__
│   │               │   │   │   ├── __init__.cpython-36.pyc
│   │               │   │   │   ├── ioloop.cpython-36.pyc
│   │               │   │   │   └── zmqstream.cpython-36.pyc
│   │               │   │   └── zmqstream.py
│   │               │   ├── __init__.py
│   │               │   ├── poll.py
│   │               │   └── __pycache__
│   │               │       ├── core.cpython-36.pyc
│   │               │       ├── device.cpython-36.pyc
│   │               │       ├── __init__.cpython-36.pyc
│   │               │       └── poll.cpython-36.pyc
│   │               ├── __init__.py
│   │               ├── .libs
│   │               │   ├── libsodium-72341b7d.so.23.2.0
│   │               │   └── libzmq-39117701.so.5.2.1
│   │               ├── log
│   │               │   ├── handlers.py
│   │               │   ├── __init__.py
│   │               │   └── __pycache__
│   │               │       ├── handlers.cpython-36.pyc
│   │               │       └── __init__.cpython-36.pyc
│   │               ├── __pycache__
│   │               │   ├── decorators.cpython-36.pyc
│   │               │   ├── error.cpython-36.pyc
│   │               │   ├── _future.cpython-36.pyc
│   │               │   └── __init__.cpython-36.pyc
│   │               ├── ssh
│   │               │   ├── forward.py
│   │               │   ├── __init__.py
│   │               │   ├── __pycache__
│   │               │   │   ├── forward.cpython-36.pyc
│   │               │   │   ├── __init__.cpython-36.pyc
│   │               │   │   └── tunnel.cpython-36.pyc
│   │               │   └── tunnel.py
│   │               ├── sugar
│   │               │   ├── attrsettr.py
│   │               │   ├── constants.py
│   │               │   ├── context.py
│   │               │   ├── frame.py
│   │               │   ├── __init__.py
│   │               │   ├── poll.py
│   │               │   ├── __pycache__
│   │               │   │   ├── attrsettr.cpython-36.pyc
│   │               │   │   ├── constants.cpython-36.pyc
│   │               │   │   ├── context.cpython-36.pyc
│   │               │   │   ├── frame.cpython-36.pyc
│   │               │   │   ├── __init__.cpython-36.pyc
│   │               │   │   ├── poll.cpython-36.pyc
│   │               │   │   ├── socket.cpython-36.pyc
│   │               │   │   ├── stopwatch.cpython-36.pyc
│   │               │   │   ├── tracker.cpython-36.pyc
│   │               │   │   └── version.cpython-36.pyc
│   │               │   ├── socket.py
│   │               │   ├── stopwatch.py
│   │               │   ├── tracker.py
│   │               │   └── version.py
│   │               ├── tests
│   │               │   ├── asyncio
│   │               │   │   ├── __init__.py
│   │               │   │   ├── __pycache__
│   │               │   │   │   ├── __init__.cpython-36.pyc
│   │               │   │   │   ├── _test_asyncio.cpython-36.pyc
│   │               │   │   │   └── test_asyncio.cpython-36.pyc
│   │               │   │   ├── _test_asyncio.py
│   │               │   │   └── test_asyncio.py
│   │               │   ├── __init__.py
│   │               │   ├── __pycache__
│   │               │   │   ├── __init__.cpython-36.pyc
│   │               │   │   ├── test_auth.cpython-36.pyc
│   │               │   │   ├── test_cffi_backend.cpython-36.pyc
│   │               │   │   ├── test_constants.cpython-36.pyc
│   │               │   │   ├── test_context.cpython-36.pyc
│   │               │   │   ├── test_decorators.cpython-36.pyc
│   │               │   │   ├── test_device.cpython-36.pyc
│   │               │   │   ├── test_draft.cpython-36.pyc
│   │               │   │   ├── test_error.cpython-36.pyc
│   │               │   │   ├── test_etc.cpython-36.pyc
│   │               │   │   ├── test_future.cpython-36.pyc
│   │               │   │   ├── test_imports.cpython-36.pyc
│   │               │   │   ├── test_includes.cpython-36.pyc
│   │               │   │   ├── test_ioloop.cpython-36.pyc
│   │               │   │   ├── test_log.cpython-36.pyc
│   │               │   │   ├── test_message.cpython-36.pyc
│   │               │   │   ├── test_monitor.cpython-36.pyc
│   │               │   │   ├── test_monqueue.cpython-36.pyc
│   │               │   │   ├── test_multipart.cpython-36.pyc
│   │               │   │   ├── test_pair.cpython-36.pyc
│   │               │   │   ├── test_poll.cpython-36.pyc
│   │               │   │   ├── test_proxy_steerable.cpython-36.pyc
│   │               │   │   ├── test_pubsub.cpython-36.pyc
│   │               │   │   ├── test_reqrep.cpython-36.pyc
│   │               │   │   ├── test_retry_eintr.cpython-36.pyc
│   │               │   │   ├── test_security.cpython-36.pyc
│   │               │   │   ├── test_socket.cpython-36.pyc
│   │               │   │   ├── test_ssh.cpython-36.pyc
│   │               │   │   ├── test_version.cpython-36.pyc
│   │               │   │   ├── test_win32_shim.cpython-36.pyc
│   │               │   │   ├── test_z85.cpython-36.pyc
│   │               │   │   └── test_zmqstream.cpython-36.pyc
│   │               │   ├── test_auth.py
│   │               │   ├── test_cffi_backend.py
│   │               │   ├── test_constants.py
│   │               │   ├── test_context.py
│   │               │   ├── test_decorators.py
│   │               │   ├── test_device.py
│   │               │   ├── test_draft.py
│   │               │   ├── test_error.py
│   │               │   ├── test_etc.py
│   │               │   ├── test_future.py
│   │               │   ├── test_imports.py
│   │               │   ├── test_includes.py
│   │               │   ├── test_ioloop.py
│   │               │   ├── test_log.py
│   │               │   ├── test_message.py
│   │               │   ├── test_monitor.py
│   │               │   ├── test_monqueue.py
│   │               │   ├── test_multipart.py
│   │               │   ├── test_pair.py
│   │               │   ├── test_poll.py
│   │               │   ├── test_proxy_steerable.py
│   │               │   ├── test_pubsub.py
│   │               │   ├── test_reqrep.py
│   │               │   ├── test_retry_eintr.py
│   │               │   ├── test_security.py
│   │               │   ├── test_socket.py
│   │               │   ├── test_ssh.py
│   │               │   ├── test_version.py
│   │               │   ├── test_win32_shim.py
│   │               │   ├── test_z85.py
│   │               │   └── test_zmqstream.py
│   │               └── utils
│   │                   ├── buffers.pxd
│   │                   ├── compiler.json
│   │                   ├── config.json
│   │                   ├── constant_names.py
│   │                   ├── garbage.py
│   │                   ├── getpid_compat.h
│   │                   ├── __init__.py
│   │                   ├── interop.py
│   │                   ├── ipcmaxlen.h
│   │                   ├── jsonapi.py
│   │                   ├── monitor.py
│   │                   ├── mutex.h
│   │                   ├── __pycache__
│   │                   │   ├── constant_names.cpython-36.pyc
│   │                   │   ├── garbage.cpython-36.pyc
│   │                   │   ├── __init__.cpython-36.pyc
│   │                   │   ├── interop.cpython-36.pyc
│   │                   │   ├── jsonapi.cpython-36.pyc
│   │                   │   ├── monitor.cpython-36.pyc
│   │                   │   ├── sixcerpt.cpython-36.pyc
│   │                   │   ├── strtypes.cpython-36.pyc
│   │                   │   ├── win32.cpython-36.pyc
│   │                   │   └── z85.cpython-36.pyc
│   │                   ├── pyversion_compat.h
│   │                   ├── sixcerpt.py
│   │                   ├── strtypes.py
│   │                   ├── win32.py
│   │                   ├── z85.py
│   │                   ├── zmq_compat.h
│   │                   └── zmq_constants.h
│   ├── lib64 -> lib
│   ├── man
│   │   └── man1
│   │       └── nosetests.1
│   ├── pyvenv.cfg
│   └── share
│       ├── jupyter
│       │   ├── kernels
│       │   │   └── python3
│       │   │       ├── kernel.json
│       │   │       ├── logo-32x32.png
│       │   │       └── logo-64x64.png
│       │   └── nbextensions
│       │       └── jupyter-js-widgets
│       │           ├── extension.js
│       │           └── extension.js.map
│       ├── man
│       │   └── man1
│       │       ├── ipython.1.gz
│       │       └── isympy.1
│       └── python-wheels
│           ├── appdirs-1.4.3-py2.py3-none-any.whl
│           ├── CacheControl-0.11.7-py2.py3-none-any.whl
│           ├── certifi-2018.1.18-py2.py3-none-any.whl
│           ├── chardet-3.0.4-py2.py3-none-any.whl
│           ├── colorama-0.3.7-py2.py3-none-any.whl
│           ├── distlib-0.2.6-py2.py3-none-any.whl
│           ├── distro-1.0.1-py2.py3-none-any.whl
│           ├── html5lib-0.999999999-py2.py3-none-any.whl
│           ├── idna-2.6-py2.py3-none-any.whl
│           ├── ipaddress-0.0.0-py2.py3-none-any.whl
│           ├── lockfile-0.12.2-py2.py3-none-any.whl
│           ├── packaging-17.1-py2.py3-none-any.whl
│           ├── pip-9.0.1-py2.py3-none-any.whl
│           ├── pkg_resources-0.0.0-py2.py3-none-any.whl
│           ├── progress-1.2-py2.py3-none-any.whl
│           ├── pyparsing-2.2.0-py2.py3-none-any.whl
│           ├── requests-2.18.4-py2.py3-none-any.whl
│           ├── retrying-1.3.3-py2.py3-none-any.whl
│           ├── setuptools-39.0.1-py2.py3-none-any.whl
│           ├── six-1.11.0-py2.py3-none-any.whl
│           ├── urllib3-1.22-py2.py3-none-any.whl
│           ├── webencodings-0.5-py2.py3-none-any.whl
│           └── wheel-0.30.0-py2.py3-none-any.whl
├── README.md
├── requirements.txt
└── statistics
    ├── build
    │   └── geometric-random-variables-intro.pdf
    ├── doc
    │   ├── normal-z-table.pdf
    │   ├── shofeyn.md
    │   └── StatEtymologyA.doc
    ├── geometric-random-variables-intro.tex
    ├── gnu
    │   ├── auto.gpi
    │   ├── bernoulli.plt
    │   └── data.dat
    ├── img
    │   ├── correlation-coefficient-result.png
    │   ├── correlation-coefficient-sample.png
    │   ├── gnuplot-sample.png
    │   ├── standard-deviation-of-residuals.png
    │   └── stats2.pdf.png
    ├── intuition-variance-vs-standard-deviation.tex
    ├── pdf
    │   ├── 1-tex
    │   ├── correlation-coefficient.pdf
    │   ├── discrete-random-variable-mean-variance-standard-deviation.pdf
    │   ├── geometric-random-variables-intro.pdf
    │   ├── intuition-variance-vs-standard-deviation.pdf
    │   ├── least-squares-regression-equation.pdf
    │   ├── normal-distribution-intuition.pdf
    │   ├── permutations-combinations.pdf
    │   ├── set-notation-operations.pdf
    │   ├── standard-deviation-of-a-discrete-random-variable.pdf
    │   ├── standard-deviation-residuals.pdf
    │   ├── template.pdf
    │   ├── tree-diagrams-conditional-probabilty.pdf
    │   └── variance-standard-deviation.pdf
    ├── permutations-combinations.tex
    ├── poisson-distribution.tex
    ├── pyp
    │   ├── correlation_coefficient.py
    │   └── standard_deviation_of_residuals.py
    ├── raw
    │   ├── 4col.csv
    │   ├── mydat.dat
    │   └── stats2.dat
    ├── set-notation-operations.tex
    ├── standard-deviation-of-a-discrete-random-variable.tex
    └── tex
        ├── correlation-coefficient.tex
        ├── discrete-random-variable-mean-variance-standard-deviation.tex
        ├── least-squares-regression-equation.tex
        ├── normal-distribution-intuition.tex
        ├── standard-deviation-residuals.tex
        ├── tree-diagrams-conditional-probabilty.tex
        └── variance-standard-deviation.tex

1853 directories, 13931 files
last generated: Tue Jul 23 07:28:00 PDT 2019
```
###### packages
```
devDependencies


dependencies


auto-generated: Tue Jul 23 07:28:00 PDT 2019
```
###### notes

  - notes here

###### [changelog](CHANGELOG.md)


